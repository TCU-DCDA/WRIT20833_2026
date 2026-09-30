"""Build the Code Guide chat page (docs/chatbot.html + docs/chatbot.js) — the after-hours tutor.

Only the chat WINDOW lives here, in the public course repo. The tutor's instructions, the per-assignment
context, and the Cloudflare Worker that calls the model live in the private `TCU-DCDA/WRIT20833-chatbot`
repo: publishing the rules would publish the recipe for talking the tutor out of them.

Sources: `chatbot/chatbot.js` (the page script), `chatbot/render.js` (reply rendering; unit tests in
`chatbot/render.test.js`) + this file (markup and page CSS, in the site theme).
Set CHAT_API_URL once the Worker is deployed; until then the page builds but build_index.py does not
link it, so students can't land on a chat window with nothing behind it.

Run from repo root:  python3 build_chatbot.py
"""
import html
import os
from site_theme import PAGE, sidebar, shell, write_stylesheet, assert_accessible

OUT = "docs/chatbot.html"
JS_SRC = "chatbot/chatbot.js"
JS_OUT = "docs/chatbot.js"
RENDER_SRC = "chatbot/render.js"   # reply rendering, no DOM: unit-tested with `node --test chatbot/render.test.js`
RENDER_OUT = "docs/render.js"

# The deployed Worker's chat endpoint, e.g. "https://writ20833-codeguide.<subdomain>.workers.dev/api/chat".
# Empty = not deployed yet: the page is built but not linked from the home page.
CHAT_API_URL = ""

GH = "https://github.com/TCU-DCDA/WRIT20833_2026"

ASSIGNMENTS = [
    ("hw1", "Homework 1 — Conditionals & Loops"),
    ("hw2", "Homework 2 — Term Frequency"),
    ("hw3", "Homework 3 — Sentiment Analysis"),
    ("hw4", "Homework 4 — Topic Modeling & Integration"),
    ("capstone", "Capstone — Data-Driven Opinion"),
]

CHAT_CSS = """
.chat{display:flex;flex-direction:column;height:min(72vh,720px);background:var(--surface);
  border:1px solid var(--rule);border-top:2.5px solid var(--green);}
.chat-bar{display:flex;flex-wrap:wrap;align-items:center;gap:10px;padding:12px 16px;
  border-bottom:1px solid var(--rule);}
.chat-bar label{font:600 12px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--muted);}
#lesson-select{flex:1;min-width:200px;padding:7px 10px;font:15px var(--sans);color:var(--ink);
  background:var(--paper);border:1px solid var(--rule);}
.chat-tools{display:flex;gap:8px;margin-left:auto;}
.chat-tools button{padding:6px 12px;font:600 13px var(--sans);color:var(--green-link);cursor:pointer;
  background:transparent;border:1px solid var(--rule);}
.chat-tools button:hover{border-color:var(--green-link);}
.messages{flex:1;overflow-y:auto;padding:18px;display:flex;flex-direction:column;gap:12px;}
.message{display:flex;}
.message.user{justify-content:flex-end;}
.message-content{max-width:84%;padding:11px 15px;font-size:15px;line-height:1.6;color:var(--ink);
  background:var(--paper);border:1px solid var(--rule);}
.message.user .message-content{background:#e3ebe2;border-color:#bccdbd;}
.message.error .message-content{background:var(--clay-bg);border-color:var(--clay);color:var(--clay-ink);}
.message-content p{margin:0 0 9px;}
.message-content p:last-child,.message-content ul:last-child,.message-content ol:last-child{margin-bottom:0;}
.message-content h2,.message-content h3,.message-content h4{font-family:var(--serif);font-size:17px;margin:12px 0 6px;}
.message-content ul,.message-content ol{margin:0 0 9px;padding-left:20px;}
.message-content code{font:13.5px var(--mono);background:#e9e6da;padding:1px 5px;}
.message-content blockquote,.callout{margin:0 0 9px;padding:8px 12px;border-left:3px solid var(--green-mid);
  background:var(--surface);}
.callout-tip{border-left-color:var(--clay);}
.code-block{position:relative;margin:0 0 10px;}
.code-block pre{margin:0;padding:26px 14px 12px;overflow-x:auto;background:#262a20;}
.code-block code{font:13.5px/1.55 var(--mono);color:#eeeadc;background:none;padding:0;}
.code-lang{position:absolute;top:6px;left:12px;font:600 12px var(--mono);color:#c9c5b6;text-transform:uppercase;}
.copy-btn{position:absolute;top:4px;right:6px;padding:2px 8px;font:600 12px var(--sans);cursor:pointer;
  color:#eeeadc;background:transparent;border:1px solid #6f7466;}
.typing-indicator span{display:inline-block;width:7px;height:7px;margin-right:4px;border-radius:50%;
  background:var(--muted);animation:blink 1.2s infinite both;}
.typing-indicator span:nth-child(2){animation-delay:.2s;}
.typing-indicator span:nth-child(3){animation-delay:.4s;}
@keyframes blink{0%,80%,100%{opacity:.25;}40%{opacity:1;}}
@media (prefers-reduced-motion:reduce){.typing-indicator span{animation:none;opacity:.6;}}
.chat-input{display:flex;gap:10px;padding:12px 16px;border-top:1px solid var(--rule);}
#user-input{flex:1;resize:none;padding:9px 11px;font:15px/1.5 var(--sans);color:var(--ink);
  background:var(--paper);border:1px solid var(--rule);}
#send-btn{padding:0 18px;font:600 14px var(--sans);color:var(--surface);background:var(--green);
  border:none;cursor:pointer;}
#send-btn:disabled{opacity:.55;cursor:default;}
.chat-note{margin:0 0 18px;padding:12px 16px;font-size:14px;color:var(--ink);background:var(--surface);
  border:1px solid var(--rule);border-left:3px solid var(--clay);max-width:78ch;}
.chat-note p{margin:0 0 6px;}
.chat-note p:last-child{margin:0;}
"""


def render():
    side = sidebar(
        "WRIT 20833 · Fall 2026",
        "When Coding Meets Culture",
        [("index.html#start", "Start here", "00"),
         ("index.html#homework", "Homework", "03"),
         ("index.html#capstone", "Capstone", "04"),
         ("chatbot.html", "Code Guide", None)],
        [(GH, "GitHub ↗"), ("https://colab.research.google.com/", "Colab ↗")],
    )
    options = "".join(f'<option value="{v}">{html.escape(t)}</option>' for v, t in ASSIGNMENTS)
    main = (
        '<header class="masthead">'
        '<div class="kicker">WRIT 20833 · after-hours tutor</div>'
        '<h1>Code Guide</h1>'
        '<p class="sub">Help with your homework and capstone when class isn’t in session.</p>'
        '</header>'
        '<div class="chat-note">'
        '<p><strong>Optional, and still new.</strong> Using it is up to you. It guides you toward your own '
        'answers; it won’t write your code, your topic names, or your essay. If it contradicts your '
        'notebook or the assignment, <strong>the notebook wins</strong>.</p>'
        '<p>Chats are saved <strong>in this browser only</strong> and are not stored by the course. There is no '
        'login and no name attached to what you send. The course counts which assignments, exercises, and kinds '
        'of errors come up, so Dr. Rode can see what the class is stuck on: counts only, never what anyone '
        'wrote. If it gets something wrong, press <strong>Export Chat</strong> '
        'and email the file to <a href="mailto:c.rode@tcu.edu">c.rode@tcu.edu</a>.</p>'
        '</div>'
        '<section class="chat" aria-label="Code Guide chat">'
        '<div class="chat-bar">'
        '<label for="lesson-select">Working on</label>'
        '<select id="lesson-select">'
        '<option value="" disabled selected>Choose your assignment…</option>'
        f'{options}</select>'
        '<div class="chat-tools">'
        '<button id="export-btn" type="button" style="display:none">Export Chat</button>'
        '<button id="start-over-btn" type="button" style="display:none">Start Over</button>'
        '</div></div>'
        '<div id="messages" class="messages" aria-live="polite"></div>'  # chatbot.js renders the welcome
        '<form id="chat-form" class="chat-input">'
        '<label for="user-input" class="sr-only" style="position:absolute;left:-9999px">Your message</label>'
        '<textarea id="user-input" rows="1" '
        'placeholder="Type your message (Enter to send, Shift+Enter for a new line)"></textarea>'
        '<button type="submit" id="send-btn">Send</button>'
        '</form>'
        '</section>'
        '<script src="render.js"></script>'
        '<script src="chatbot.js"></script>'
    )
    return PAGE("Code Guide — WRIT 20833", shell(side, main), extra_css=CHAT_CSS, wrap=False)


def write_js():
    with open(JS_SRC, encoding="utf-8") as f:
        src = f.read()
    assert "__CHAT_API_URL__" in src, f"{JS_SRC} lost its __CHAT_API_URL__ placeholder"
    with open(JS_OUT, "w", encoding="utf-8") as f:
        f.write(src.replace("__CHAT_API_URL__", CHAT_API_URL))
    with open(RENDER_SRC, encoding="utf-8") as f, open(RENDER_OUT, "w", encoding="utf-8") as g:
        g.write(f.read())


if __name__ == "__main__":
    assert_accessible(CHAT_CSS)
    css = write_stylesheet(os.path.dirname(OUT) or ".")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(render())
    write_js()
    print(f"wrote {OUT} ({os.path.getsize(OUT)} bytes) + {JS_OUT} + {css}")
    if not CHAT_API_URL:
        print("  note: CHAT_API_URL is empty — the page is built but NOT linked from index.html until it's set")
