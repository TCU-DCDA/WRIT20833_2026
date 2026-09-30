// Configuration. SOURCE file: build_chatbot.py copies this to docs/chatbot.js and fills in
//  from its CHAT_API_URL setting. Edit here, never in docs/.
const API_URL = '';

// Max messages sent to the API (sliding window — older messages are kept in
// the chat display and localStorage but not sent to the AI, keeping costs
// low and avoiding context window limits)
const MAX_HISTORY_TO_API = 50;

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

function saveHistory() {
    try {
        localStorage.setItem(getStorageKey(), JSON.stringify(conversationHistory));
        console.log('[CodeGuide] Saved', conversationHistory.length, 'messages to', getStorageKey());
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
chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const message = userInput.value.trim();
    if (!message) return;

    // Built without a Worker URL (build_chatbot.py's CHAT_API_URL is empty): say so plainly.
    if (!API_URL) {
        appendMessage('error', "The Code Guide isn't open yet. Check back soon, or ask Dr. Rode in class.");
        return;
    }

    // Add user message to UI
    appendMessage('user', message);
    conversationHistory.push({ role: 'user', content: message });

    // Clear input
    userInput.value = '';
    userInput.style.height = 'auto';

    // Disable input while waiting
    setInputEnabled(false);

    // Show typing indicator
    const typingEl = showTypingIndicator();

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                message: message,
                lessonId: lessonSelect.value,
                accessCode: storedAccessCode(),
                // Send recent history only (sliding window) — exclude the message we just added
                history: conversationHistory.slice(-MAX_HISTORY_TO_API - 1, -1)
            })
        });

        // Remove typing indicator
        typingEl.remove();

        // 401 = the access gate is on and our code was missing/wrong. Prompt once, store it,
        // and ask the student to resend (we don't auto-retry to keep the flow simple).
        if (response.status === 401) {
            const code = (window.prompt('Enter the course access code to use the Code Guide:') || '').trim();
            if (code) {
                localStorage.setItem(ACCESS_CODE_KEY, code);
                appendMessage('error', 'Access code saved — send your message again.');
            } else {
                localStorage.removeItem(ACCESS_CODE_KEY);
                appendMessage('error', 'An access code is required to use the tutor.');
            }
            return;
        }

        if (response.status === 429) {
            const errorData = await response.json().catch(() => ({}));
            appendMessage('error', errorData.error || 'Too many requests — please wait a bit and try again.');
            return;
        }

        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.error || `Server error (${response.status})`);
        }

        // Handle streaming response
        if (response.headers.get('content-type')?.includes('text/event-stream')) {
            const assistantText = await handleStreamingResponse(response);
            conversationHistory.push({ role: 'assistant', content: assistantText });
        } else {
            // Non-streaming fallback
            const data = await response.json();
            const assistantText = data.response || data.content || 'Sorry, I didn\'t get a response.';
            appendMessage('assistant', assistantText);
            conversationHistory.push({ role: 'assistant', content: assistantText });
        }

        // Persist conversation and show Start Over button
        saveHistory();
        startOverBtn.style.display = 'block';
        exportBtn.style.display = 'block';
    } catch (error) {
        typingEl.remove();
        appendMessage('error', `Something went wrong: ${error.message}. Please try again.`);
        // Remove the failed user message from history so conversation stays clean
        conversationHistory.pop();
    } finally {
        setInputEnabled(true);
        userInput.focus();
    }
});

// Handle streaming SSE response
async function handleStreamingResponse(response) {
    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    // Create the assistant message element
    const messageEl = document.createElement('div');
    messageEl.className = 'message assistant';
    const contentEl = document.createElement('div');
    contentEl.className = 'message-content';
    messageEl.appendChild(contentEl);
    messagesContainer.appendChild(messageEl);

    let fullText = '';
    let buffer = '';

    while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });

        // Parse SSE events from buffer
        const lines = buffer.split('\n');
        buffer = lines.pop(); // keep incomplete line in buffer

        for (const line of lines) {
            if (line.startsWith('data: ')) {
                const data = line.slice(6);
                if (data === '[DONE]') continue;

                try {
                    const parsed = JSON.parse(data);
                    if (parsed.type === 'text') {
                        fullText += parsed.content;
                        contentEl.innerHTML = renderMarkdown(fullText);
                        scrollToBottom();
                    } else if (parsed.type === 'error') {
                        throw new Error(parsed.content);
                    }
                } catch (e) {
                    if (e.message && !e.message.includes('JSON')) {
                        throw e;
                    }
                    // Ignore JSON parse errors for incomplete chunks
                }
            }
        }
    }

    // Final render
    contentEl.innerHTML = renderMarkdown(fullText);
    scrollToBottom();
    return fullText;
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

// Enable/disable input
function setInputEnabled(enabled) {
    userInput.disabled = !enabled;
    sendBtn.disabled = !enabled;
}

// Scroll chat to bottom
function scrollToBottom() {
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

// Markdown rendering (code blocks, inline code, bold, italic, lists, headings, paragraphs)
function renderMarkdown(text) {
    // Escape HTML first (except we'll add back our formatted elements)
    let html = escapeHtml(text);

    // Code blocks: ```lang\ncode\n``` — with copy button and language label
    html = html.replace(/```(\w*)\n([\s\S]*?)```/g, (_, lang, code) => {
        const langLabel = lang ? `<span class="code-lang">${lang}</span>` : '';
        return `<div class="code-block">${langLabel}<button class="copy-btn" onclick="copyCode(this)">Copy</button><pre><code>${code.trim()}</code></pre></div>`;
    });

    // Inline code: `code`
    html = html.replace(/`([^`]+)`/g, '<code>$1</code>');

    // Bold: **text**
    html = html.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');

    // Italic: *text*
    html = html.replace(/(?<!\*)\*([^*]+)\*(?!\*)/g, '<em>$1</em>');

    // Split into blocks by double newline
    const blocks = html.split(/\n\n+/).map(b => b.trim()).filter(b => b);

    html = blocks.map(block => {
        // Don't wrap code blocks
        if (block.startsWith('<div class="code-block">')) return block;
        if (block.startsWith('<pre>')) return block;

        // Blockquotes: lines starting with >
        const lines = block.split('\n');
        if (lines.every(l => l.startsWith('&gt; ') || l === '&gt;')) {
            const inner = lines.map(l => l.replace(/^&gt; ?/, '')).join('<br>');
            // Detect callout type
            if (/checkpoint|you should see|check your|preview|output/i.test(inner)) {
                return `<div class="callout callout-check">${inner}</div>`;
            }
            if (/tip|hint|remember/i.test(inner)) {
                return `<div class="callout callout-tip">${inner}</div>`;
            }
            return `<blockquote>${inner}</blockquote>`;
        }

        // Headings: ### heading, ## heading, # heading
        if (/^#{1,3} /.test(block)) {
            const match = block.match(/^(#{1,3}) (.+)$/);
            if (match) {
                const level = match[1].length + 1; // offset so # = h2, ## = h3 (don't use h1 in chat)
                const tag = `h${Math.min(level, 4)}`;
                return `<${tag}>${match[2]}</${tag}>`;
            }
        }

        // Unordered lists: lines starting with - or *
        if (lines.every(l => /^[\-\*] /.test(l))) {
            const items = lines.map(l => `<li>${l.replace(/^[\-\*] /, '')}</li>`).join('');
            return `<ul>${items}</ul>`;
        }

        // Ordered lists: lines starting with 1. 2. etc.
        if (lines.every(l => /^\d+\. /.test(l))) {
            const items = lines.map(l => `<li>${l.replace(/^\d+\. /, '')}</li>`).join('');
            return `<ol>${items}</ol>`;
        }

        // Regular paragraph
        return `<p>${block.replace(/\n/g, '<br>')}</p>`;
    }).join('');

    return html;
}

// Copy code block content to clipboard
function copyCode(button) {
    const codeEl = button.closest('.code-block').querySelector('code');
    navigator.clipboard.writeText(codeEl.textContent).then(() => {
        button.textContent = 'Copied!';
        setTimeout(() => { button.textContent = 'Copy'; }, 2000);
    });
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
