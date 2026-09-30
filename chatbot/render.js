/**
 * Code Guide reply rendering: text in, HTML out. No DOM, so it can be unit-tested in Node
 * (render.test.js). SOURCE file: build_chatbot.py copies it to docs/. The page loads it before chatbot.js.
 *
 * The rule that matters: CODE IS NEVER REFORMATTED. Fenced blocks and inline code are set aside first
 * and restored last, so `2 ** 3`, `a*b*c`, indentation, and blank lines inside a block reach the student
 * (and the Copy button) exactly as written. A tutor whose display changes Python teaches the wrong Python.
 */

function escapeHtml(text) {
    return String(text)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
}

function renderMarkdown(text) {
    // Protected pieces wait in `slots`; the text carries a \u0000n\u0000 marker where each goes back.
    const slots = [];
    const hold = (html) => `\u0000${slots.push(html) - 1}\u0000`;
    let src = String(text).replace(/\u0000/g, '');

    // 1. Fenced code. An unclosed fence (a reply still streaming in) runs to the end of the text.
    //    Only the one newline that ends the block is dropped: leading indentation is kept.
    src = src.replace(/```([\w+-]*)[^\n]*\n?([\s\S]*?)(?:```|$)/g, (_, lang, code) => {
        const label = lang ? `<span class="code-lang">${escapeHtml(lang)}</span>` : '';
        const block = `<div class="code-block">${label}`
            + `<button class="copy-btn" type="button" onclick="copyCode(this)">Copy</button>`
            + `<pre><code>${escapeHtml(code.replace(/\n$/, ''))}</code></pre></div>`;
        return `\n\n${hold(block)}\n\n`;
    });

    // 2. Inline code (single line only).
    src = src.replace(/`([^`\n]+)`/g, (_, code) => hold(`<code>${escapeHtml(code)}</code>`));

    // 3. Everything left is prose: escape it, then apply emphasis. Markers need a non-space on the inside,
    //    so "* item" bullets and "2 * 3" in prose aren't italicized.
    let html = escapeHtml(src)
        .replace(/\*\*(?=\S)([^*\n]+?)\*\*/g, '<strong>$1</strong>')
        .replace(/(?<![*\w])\*(?=\S)([^*\n]+?)\*(?![*\w])/g, '<em>$1</em>');

    // 4. Blocks.
    const isSlot = (b) => /^\u0000\d+\u0000$/.test(b);
    html = html.split(/\n\n+/).map(b => b.trim()).filter(Boolean).map(block => {
        if (isSlot(block)) return block;   // a code block stands alone, never wrapped in <p>

        const lines = block.split('\n');
        if (lines.every(l => l.startsWith('&gt; ') || l === '&gt;')) {
            const inner = lines.map(l => l.replace(/^&gt; ?/, '')).join('<br>');
            if (/checkpoint|you should see|check your|preview|output/i.test(inner)) {
                return `<div class="callout callout-check">${inner}</div>`;
            }
            if (/tip|hint|remember/i.test(inner)) {
                return `<div class="callout callout-tip">${inner}</div>`;
            }
            return `<blockquote>${inner}</blockquote>`;
        }
        const heading = block.match(/^(#{1,3}) (.+)$/);
        if (heading) {
            const tag = `h${Math.min(heading[1].length + 1, 4)}`;   // # = h2: no h1 inside a chat
            return `<${tag}>${heading[2]}</${tag}>`;
        }
        if (lines.every(l => /^[-*] /.test(l))) {
            return `<ul>${lines.map(l => `<li>${l.replace(/^[-*] /, '')}</li>`).join('')}</ul>`;
        }
        if (lines.every(l => /^\d+\. /.test(l))) {
            return `<ol>${lines.map(l => `<li>${l.replace(/^\d+\. /, '')}</li>`).join('')}</ol>`;
        }
        return `<p>${block.replace(/\n/g, '<br>')}</p>`;
    }).join('');

    // 5. Put the protected code back.
    return html.replace(/\u0000(\d+)\u0000/g, (_, i) => slots[Number(i)]);
}

if (typeof module !== 'undefined' && module.exports) {
    module.exports = { escapeHtml, renderMarkdown };
}
