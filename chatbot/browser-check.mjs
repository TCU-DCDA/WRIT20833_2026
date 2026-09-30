/**
 * Browser checks for the Code Guide page's conversation state, against a fake Worker.
 * Needs Playwright, which this repo deliberately doesn't install. Run it from a scratch folder that has it:
 *
 *   python3 build_chatbot.py                                   # (in this repo) build docs/ first
 *   mkdir /tmp/cg && cd /tmp/cg && npm i playwright@1.58 && npx playwright install chromium
 *   cp <this repo>/chatbot/browser-check.mjs . && DOCS=<this repo>/docs node browser-check.mjs
 *
 * Covers the 2026-09-30 review's defects: code shown verbatim (#9), a reply can't land in another
 * assignment's conversation (#8), and every failed turn rolls back cleanly with the draft restored (#10).
 */
import { chromium } from 'playwright';
import { readFileSync, mkdtempSync, cpSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

// A copy of the built site whose API_URL points at a fake Worker.
const docs = process.env.DOCS ?? join(dirname(fileURLToPath(import.meta.url)), '..', 'docs');
const site = mkdtempSync(join(tmpdir(), 'codeguide-'));
cpSync(docs, site, { recursive: true });
const MOCK = 'https://mock.test/api/chat';
writeFileSync(join(site, 'chatbot.js'),
    readFileSync(join(site, 'chatbot.js'), 'utf8').replace("const API_URL = '';", `const API_URL = '${MOCK}';`));
const page_url = (q = '') => `file://${site}/chatbot.html${q}`;

const sse = (...events) => events.map(e => `data: ${typeof e === 'string' ? e : JSON.stringify(e)}\n\n`).join('');
const text = t => ({ type: 'text', content: t });
const reply = (status, body, headers = {}) => ({ status, headers: { 'access-control-allow-origin': '*', ...headers }, body });

let failures = 0;
const check = (name, ok, detail = '') => {
    console.log(`${ok ? 'ok  ' : 'FAIL'}  ${name}${ok ? '' : `  ${detail}`}`);
    if (!ok) failures++;
};

const browser = await chromium.launch();
const page = await browser.newPage();
page.on('pageerror', e => check('no page errors', false, e.message));
page.on('dialog', d => d.accept('CODE'));

let next = null;   // what the fake Worker returns for the next request (+ optional delay)
await page.route(MOCK, async route => {
    const { delay = 0, ...r } = next;
    if (delay) await new Promise(res => setTimeout(res, delay));
    await route.fulfill(r);
});
const stream = (...events) => reply(200, sse(...events), { 'content-type': 'text/event-stream' });

async function send(msg) {
    await page.fill('#user-input', msg);
    await page.press('#user-input', 'Enter');
    await page.waitForFunction(() => !document.querySelector('#send-btn').disabled);
}
const state = () => page.evaluate(() => ({
    bubbles: [...document.querySelectorAll('.message.user, .message.assistant')].map(e => e.innerText.trim()),
    history: conversationHistory.map(m => m.role + ':' + m.content),
    input: document.querySelector('#user-input').value,
    saved: Object.fromEntries(Object.keys(localStorage).filter(k => k.startsWith('codeguide-history-'))
        .map(k => [k.replace('codeguide-history-', ''), JSON.parse(localStorage.getItem(k)).length])),
}));

await page.goto(page_url('?assignment=hw1'));
await page.evaluate(() => localStorage.clear());
await page.reload();

// #9 — code arrives verbatim, including the Copy button's text.
next = stream(text('Try:\n\n```python\nprint(2 ** 3)  # **x**\n\ny = 1\n```'), '[DONE]');
await send('show me exponent');
const code = await page.$eval('.message.assistant:last-child code', el => el.textContent);
check('#9 code block is verbatim', code === 'print(2 ** 3)  # **x**\n\ny = 1', JSON.stringify(code));

// A normal finished reply is saved.
let s = await state();
check('finished reply is saved', s.history.length === 2 && s.saved.hw1 === 2, JSON.stringify(s));

// #8 — controls are locked while a reply is loading; the late reply lands in its own conversation.
next = { ...stream(text('HW1 ANSWER'), '[DONE]'), delay: 1200 };
await page.fill('#user-input', 'slow one');
await page.press('#user-input', 'Enter');
await page.waitForTimeout(200);
check('#8 assignment picker locked during a request', await page.isDisabled('#lesson-select'));
check('#8 Start Over locked during a request', await page.isDisabled('#start-over-btn'));
await page.waitForFunction(() => !document.querySelector('#send-btn').disabled);
s = await state();
check('#8 reply saved to hw1 only', s.saved.hw1 === 4 && !s.saved.hw3, JSON.stringify(s.saved));

// #10 — every failure rolls the turn back and restores the draft.
const before = await state();
async function failing(label, response, notice) {
    next = response;
    await send(`${label} draft`);
    const after = await state();
    check(`#10 ${label}: partial reply and question removed`,
        JSON.stringify(after.bubbles) === JSON.stringify(before.bubbles), JSON.stringify(after.bubbles));
    check(`#10 ${label}: history rolled back`, after.history.length === before.history.length, after.history.length);
    check(`#10 ${label}: draft restored`, after.input === `${label} draft`, JSON.stringify(after.input));
    const shown = await page.$eval('.message.error:last-child', el => el.innerText);
    check(`#10 ${label}: notice shown`, notice.test(shown), shown);
    await page.fill('#user-input', '');
}
await failing('refusal', stream(text('Partial ans'), { type: 'refusal', content: "I couldn't answer that one" }), /couldn't answer/);
await failing('provider error', stream(text('Half a'), { type: 'error', content: 'x' }), /broke off/);
await failing('cut off', stream(text('No done marker')), /cut off/);
await failing('401', reply(401, '{"error":"x"}', { 'content-type': 'application/json' }), /Access code saved/);
await failing('429', reply(429, '{"error":"Too many requests."}', { 'content-type': 'application/json' }), /Too many/);
await failing('500', reply(500, '{"error":"Internal server error"}', { 'content-type': 'application/json' }), /went wrong/);
check('#10 nothing extra saved after failures', (await state()).saved.hw1 === 4);

await browser.close();
console.log(failures ? `\n${failures} check(s) failed` : '\nall checks passed');
process.exit(failures ? 1 : 0);
