// Unit tests for render.js. Run from the repo root:  node --test chatbot/render.test.js
const { test } = require('node:test');
const assert = require('node:assert/strict');
const { renderMarkdown, escapeHtml } = require('./render.js');

// What a student would see (and copy) from a rendered <code>: the text with entities decoded.
const codeText = (html) => [...html.matchAll(/<code>([\s\S]*?)<\/code>/g)]
    .map(m => m[1].replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&amp;/g, '&'));

test('fenced code keeps ** and * exactly (the 2026-09-30 defect)', () => {
    const html = renderMarkdown('```python\nprint(2 ** 3)  # **not bold**\nx = a * b * c\n```');
    assert.deepEqual(codeText(html), ['print(2 ** 3)  # **not bold**\nx = a * b * c']);
    assert.doesNotMatch(html, /<strong>|<em>/);
});

test('a blank line inside a fence stays inside one code block', () => {
    const html = renderMarkdown('```python\nx = 1\n\ny = 2\n```');
    assert.deepEqual(codeText(html), ['x = 1\n\ny = 2']);
    assert.doesNotMatch(html, /<p>/);
});

test('indentation inside a fence is preserved', () => {
    const src = 'for c in comments:\n    if len(c) > 3:\n        print(c)';
    assert.deepEqual(codeText(renderMarkdown('```python\n' + src + '\n```')), [src]);
});

test('inline code keeps * and ** too', () => {
    const html = renderMarkdown('Try `a*b*c` and `2 ** 3` here.');
    assert.deepEqual(codeText(html), ['a*b*c', '2 ** 3']);
    assert.doesNotMatch(html, /<em>|<strong>/);
});

test('code is escaped, never interpreted as HTML', () => {
    const html = renderMarkdown('```\n<script>alert(1)</script>\n```\nand `<b>`');
    assert.doesNotMatch(html, /<script>|<b>/);
    assert.deepEqual(codeText(html), ['<script>alert(1)</script>', '<b>']);
});

test('an unclosed fence (still streaming) renders as code, not prose', () => {
    const html = renderMarkdown('Here:\n```python\nprint(2 ** 3');
    assert.deepEqual(codeText(html), ['print(2 ** 3']);
    assert.doesNotMatch(html, /<strong>/);
});

test('prose formatting still works outside code', () => {
    const html = renderMarkdown('**Bold** and *italic*.\n\n- one\n- two\n\n> **Tip:** remember this');
    assert.match(html, /<strong>Bold<\/strong>/);
    assert.match(html, /<em>italic<\/em>/);
    assert.match(html, /<ul><li>one<\/li><li>two<\/li><\/ul>/);
    assert.match(html, /callout-tip/);
});

test('prose asterisks with spaces are left alone', () => {
    assert.doesNotMatch(renderMarkdown('2 * 3 * 4 is 24'), /<em>/);
});

test('prose is escaped', () => {
    assert.doesNotMatch(renderMarkdown('<img src=x onerror=alert(1)>'), /<img/);
    assert.equal(escapeHtml(`<a href="x">'&'</a>`), '&lt;a href=&quot;x&quot;&gt;&#39;&amp;&#39;&lt;/a&gt;');
});
