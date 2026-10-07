// Configuration. SOURCE file: build_chatbot.py copies this to docs/chatbot.js and fills in
//  from its CHAT_API_URL setting. Edit here, never in docs/.
const API_URL = '';

// Max messages sent to the API (sliding window — older messages are kept in
// the chat display and localStorage but not sent to the AI, keeping costs
// low and avoiding context window limits). Matches the Worker's own ceiling
// (MAX_HISTORY_MESSAGES = 40 in the private WRIT20833-chatbot repo), which the
// tutor's prompt describes to it; change both together.
const MAX_HISTORY_TO_API = 40;

// Welcome message content (single source of truth)
const WELCOME_MESSAGE = `<p>Welcome! I'm your after-hours tutor for WRIT 20833. Pick the assignment you're working on from the dropdown above, and tell me where you're stuck.</p>
<p>Have your Google Colab notebook open — everything in this course runs in Colab. Paste your code and the full error message anytime, and we'll work through it together. I won't write your answers for you, but I'll help you get them yourself.</p>`;

// Conversation history (sent with each request so the AI has context)
let conversationHistory = [];

// --- Access code (lazy) ---
// The worker enforces a code only when its ACCESS_CODE secret is set. We send whatever is
// stored (possibly empty); if the worker returns 401 we prompt once, store it, and ask the
// student to resend. This way local dev (no gate) never prompts.
const ACCESS_CODE_KEY = 'writ-codeguide-access-code';
function storedAccessCode() { return localStorage.getItem(ACCESS_CODE_KEY) || ''; }

// DOM elements
const messagesContainer = document.getElementById('messages');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const lessonSelect = document.getElementById('lesson-select');
const startOverBtn = document.getElementById('start-over-btn');
const exportBtn = document.getElementById('export-btn');

// --- localStorage persistence ---
function getStorageKey() {
    return `codeguide-history-${lessonSelect.value}`;
}

function saveHistory(key = getStorageKey(), history = conversationHistory) {
    try {
        localStorage.setItem(key, JSON.stringify(history));
        console.log('[CodeGuide] Saved', history.length, 'messages to', key);
    } catch (e) {
        console.warn('[CodeGuide] Failed to save history:', e.message);
    }
}

function loadHistory() {
    try {
        const saved = localStorage.getItem(getStorageKey());
        const parsed = saved ? JSON.parse(saved) : null;
        console.log('[CodeGuide] Loaded from', getStorageKey(), ':', parsed ? parsed.length + ' messages' : 'nothing saved');
        return parsed;
    } catch (e) {
        console.warn('[CodeGuide] Failed to load history:', e.message);
        return null;
    }
}

function clearHistory() {
    conversationHistory = [];
    try {
        localStorage.removeItem(getStorageKey());
    } catch (e) {
        // fail silently
    }
}

function resetToWelcome() {
    messagesContainer.innerHTML = `
        <div class="message assistant">
            <div class="message-content">
                ${WELCOME_MESSAGE}
            </div>
        </div>
    `;
}

// Restore saved conversation on page load
function restoreConversation() {
    const saved = loadHistory();
    if (saved && saved.length > 0) {
        conversationHistory = saved;

        // Clear the default welcome message
        messagesContainer.innerHTML = '';

        // Re-render all saved messages
        for (const msg of conversationHistory) {
            appendMessage(msg.role, msg.content);
        }

        // Show welcome-back notice
        const notice = document.createElement('div');
        notice.className = 'message assistant';
        notice.innerHTML = `
            <div class="message-content" style="background: var(--accent-light); border-color: var(--accent); font-size: 13px;">
                <p>Welcome back! Your previous conversation has been restored. You can pick up where you left off, or hit <strong>Start Over</strong> to begin fresh.</p>
            </div>
        `;
        messagesContainer.appendChild(notice);
        scrollToBottom();

        startOverBtn.style.display = 'block';
        exportBtn.style.display = 'block';
    }
}

// Start Over button
startOverBtn.addEventListener('click', () => {
    if (!confirm('Start a new conversation? Your current progress for this lesson will be cleared.')) return;

    clearHistory();
    startOverBtn.style.display = 'none';
    exportBtn.style.display = 'none';
    resetToWelcome();
});

// Export Chat button
exportBtn.addEventListener('click', () => {
    if (conversationHistory.length === 0) return;

    const lessonName = lessonSelect.options[lessonSelect.selectedIndex].text;
    const timestamp = new Date().toLocaleString();

    let text = `WRIT 20833 — Code Guide Chat Export\n`;
    text += `Lesson: ${lessonName}\n`;
    text += `Exported: ${timestamp}\n`;
    text += `${'—'.repeat(50)}\n\n`;

    for (const msg of conversationHistory) {
        const label = msg.role === 'user' ? 'STUDENT' : 'CODE GUIDE';
        text += `${label}:\n${msg.content}\n\n`;
    }

    // Create and download the file
    const blob = new Blob([text], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `codeguide-${lessonSelect.value}-${new Date().toISOString().slice(0, 10)}.txt`;
    a.click();
    URL.revokeObjectURL(url);
});

// When lesson changes, load that lesson's saved conversation (or reset)
lessonSelect.addEventListener('change', () => {
    conversationHistory = [];
    resetToWelcome();
    startOverBtn.style.display = 'none';
    exportBtn.style.display = 'none';
    restoreConversation();
});

// Deep link: a course-site link like chatbot.html?assignment=hw3 opens on that assignment. With no
// (or an unrecognized) parameter the page stays on "Choose your assignment…" rather than silently
// defaulting to HW1. (The WRIT 40363 bot found that a default first option sends questions to the wrong context.)
{
    const wanted = new URLSearchParams(location.search).get('assignment');
    if (wanted && [...lessonSelect.options].some(o => o.value === wanted && !o.disabled)) {
        lessonSelect.value = wanted;
    }
}

// Initial view: the welcome message (single source: WELCOME_MESSAGE), then any saved conversation.
resetToWelcome();
restoreConversation();

// Auto-resize textarea as user types
userInput.addEventListener('input', () => {
    userInput.style.height = 'auto';
    userInput.style.height = Math.min(userInput.scrollHeight, 150) + 'px';
});

// Handle Enter to send, Shift+Enter for new line
userInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        chatForm.dispatchEvent(new Event('submit'));
    }
});

// Handle form submission
//
// Invariant: what the student sees and what is saved stay in step. A reply is saved only after the Worker
// says it finished (`[DONE]`). If anything goes wrong (an HTTP error, a refusal, a provider error, a reply
// cut off), the whole turn is rolled back: the partial reply and the student's bubble are removed, the
// pending turn leaves the history, and their message goes back in the box for a retry.
let requestInFlight = false;

chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    if (requestInFlight) return;

    const message = userInput.value.trim();
    if (!message) return;

    // Built without a Worker URL (build_chatbot.py's CHAT_API_URL is empty): say so plainly.
    if (!API_URL) {
        appendMessage('error', "The Code Guide isn't open yet. Check back soon, or ask Dr. Rode in class.");
        return;
    }

    // Pin everything this request touches to the conversation it started in. The assignment picker and
    // Start Over are locked while it runs (setInputEnabled), and even if one weren't, a late reply lands in
    // the conversation it belongs to, never the one on screen.
    const lessonId = lessonSelect.value;
    const storageKey = getStorageKey();
    const history = conversationHistory;

    const userEl = appendMessage('user', message);
    history.push({ role: 'user', content: message });
    userInput.value = '';
    userInput.style.height = 'auto';

    requestInFlight = true;
    setInputEnabled(false);
    const typingEl = showTypingIndicator();

    const rollback = (notice) => {
        typingEl.remove();
        userEl.remove();
        const last = history[history.length - 1];
        if (last && last.role === 'user' && last.content === message) history.pop();
        if (!userInput.value) {
            userInput.value = message;
            userInput.style.height = 'auto';
            userInput.style.height = Math.min(userInput.scrollHeight, 150) + 'px';
        }
        appendMessage('error', `${notice} Your message is back in the box, ready to send again.`);
    };

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                message: message,
                lessonId: lessonId,
                accessCode: storedAccessCode(),
                // Send recent history only (sliding window) — exclude the message we just added
                history: history.slice(-MAX_HISTORY_TO_API - 1, -1)
            })
        });
        typingEl.remove();

        // 401 = the access gate is on and our code was missing/wrong. Prompt once and store it.
        if (response.status === 401) {
            const code = (window.prompt('Enter the course access code to use the Code Guide:') || '').trim();
            if (code) {
                localStorage.setItem(ACCESS_CODE_KEY, code);
                rollback('Access code saved.');
            } else {
                localStorage.removeItem(ACCESS_CODE_KEY);
                rollback('An access code is required to use the tutor.');
            }
            return;
        }
        if (response.status === 429) {
            const errorData = await response.json().catch(() => ({}));
            rollback(errorData.error || 'Too many requests. Please wait a bit and try again.');
            return;
        }
        if (!response.ok || !response.headers.get('content-type')?.includes('text/event-stream')) {
            const errorData = await response.json().catch(() => ({}));
            rollback(`Something went wrong (${errorData.error || `server error ${response.status}`}).`);
            return;
        }

        const result = await handleStreamingResponse(response);
        if (result.status !== 'done') {
            rollback(result.notice);
            return;
        }

        history.push({ role: 'assistant', content: result.text });
        saveHistory(storageKey, history);
        if (history === conversationHistory) {
            startOverBtn.style.display = 'block';
            exportBtn.style.display = 'block';
        }
    } catch (error) {
        rollback("Something went wrong reaching the tutor.");
    } finally {
        requestInFlight = false;
        setInputEnabled(true);
        userInput.focus();
    }
});

// Read the Worker's SSE stream into an assistant bubble. Returns { status, text, notice }:
// status is 'done' only when the Worker sent [DONE] after a non-empty reply. For every other ending
// ('refusal', 'error', 'interrupted') the partial bubble is removed here and `notice` says what happened.
async function handleStreamingResponse(response) {
    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    const messageEl = document.createElement('div');
    messageEl.className = 'message assistant';
    const contentEl = document.createElement('div');
    contentEl.className = 'message-content';
    messageEl.appendChild(contentEl);
    messagesContainer.appendChild(messageEl);

    let fullText = '';
    let buffer = '';
    let status = 'interrupted';
    let notice = 'The reply was cut off before it finished.';

    try {
        while (status === 'interrupted') {
            const { done, value } = await reader.read();
            if (done) break;
            buffer += decoder.decode(value, { stream: true });
            const lines = buffer.split('\n');
            buffer = lines.pop(); // keep the incomplete line for the next chunk

            for (const line of lines) {
                if (!line.startsWith('data: ')) continue;
                const data = line.slice(6).trim();
                if (data === '[DONE]') { status = 'done'; break; }
                let parsed;
                try { parsed = JSON.parse(data); } catch { continue; }   // skip a malformed chunk
                if (parsed.type === 'text') {
                    fullText += parsed.content;
                    contentEl.innerHTML = renderMarkdown(fullText);
                    scrollToBottom();
                } else if (parsed.type === 'refusal') {
                    status = 'refusal';
                    notice = `${parsed.content}.`;
                    break;
                } else if (parsed.type === 'error') {
                    status = 'error';
                    notice = 'The reply broke off partway because of a problem on the AI service\'s end.';
                    break;
                }
            }
        }
    } catch {
        status = 'interrupted';
    }

    if (status === 'done' && !fullText.trim()) {
        status = 'error';
        notice = 'The tutor sent back an empty reply.';
    }
    if (status !== 'done') {
        messageEl.remove();
        return { status, text: '', notice };
    }
    contentEl.innerHTML = renderMarkdown(fullText);
    scrollToBottom();
    return { status, text: fullText, notice: null };
}

// Append a message to the chat
function appendMessage(role, text) {
    const messageEl = document.createElement('div');
    messageEl.className = `message ${role}`;

    const contentEl = document.createElement('div');
    contentEl.className = 'message-content';
    contentEl.innerHTML = role === 'user' ? escapeHtml(text) : renderMarkdown(text);

    messageEl.appendChild(contentEl);
    messagesContainer.appendChild(messageEl);
    scrollToBottom();
    return messageEl;
}

// Show typing indicator, returns the element so caller can remove it
function showTypingIndicator() {
    const el = document.createElement('div');
    el.className = 'message assistant';
    el.innerHTML = `
        <div class="message-content typing-indicator">
            <span></span><span></span><span></span>
        </div>
    `;
    messagesContainer.appendChild(el);
    scrollToBottom();
    return el;
}

// Enable/disable input. While a reply is loading, everything that could change which conversation is on
// screen (the assignment picker, Start Over) is locked too, so a late reply can't land in the wrong one.
function setInputEnabled(enabled) {
    userInput.disabled = !enabled;
    sendBtn.disabled = !enabled;
    lessonSelect.disabled = !enabled;
    startOverBtn.disabled = !enabled;
    exportBtn.disabled = !enabled;
}

// Scroll chat to bottom
function scrollToBottom() {
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

// renderMarkdown() and escapeHtml() live in render.js (loaded first; unit-tested in Node).

// Copy code block content to clipboard
function copyCode(button) {
    const codeEl = button.closest('.code-block').querySelector('code');
    navigator.clipboard.writeText(codeEl.textContent).then(() => {
        button.textContent = 'Copied!';
        setTimeout(() => { button.textContent = 'Copy'; }, 2000);
    });
}

