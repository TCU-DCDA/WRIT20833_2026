# Chatbot tutor — scope & decision note

**Status:** evaluation complete; **build NOT yet decided** (awaiting the instructor's timing call). This is
the single consolidated scoping doc — it supersedes the eval prose that was buried in `WORKLOG.md`
(2026-06-17). The high-leverage artifact, the **draft system prompt**, lives beside it at
[`CHATBOT_TUTOR_SYSTEM_PROMPT_DRAFT.md`](CHATBOT_TUTOR_SYSTEM_PROMPT_DRAFT.md). · *Last updated 2026-06-18.*

---

## The question
Is there value in building a course chatbot tutor for WRIT 20833, modeled on the **MALA 60970 bot**
(`../../MALA/MALA60970-chatbot`)?

## The reference model (MALA 60970 bot) — verified by reading the repo, 2026-06-18
A Socratic *"guide-not-code-generator"* tutor that, in MALA, **replaces video code-alongs**. Architecture:
- **Split deploy:** static frontend (`index.html` + `script.js` + `style.css`) on GitHub Pages; a
  **Cloudflare Worker** backend (`mla60970-codeguide.workers.dev`) that calls **Claude Haiku 4.5** via the
  Anthropic API and streams over SSE. ~5K LOC, **no database, no RAG.**
- **Content stays server-side:** the system prompt + per-lesson guides live in `worker/lessons/` as JS
  modules, registered in `registry.js`, exposed via an `index.html` dropdown — never sent to the browser
  (the student sees only the bot's replies).
- **Guardrails for a public, billed endpoint:** per-IP rate limiting (10/min burst + 300/day, fail-closed in
  Cloudflare KV), an optional access-code gate (`wrangler secret`), a CORS allowlist (GitHub Pages / D2L),
  API key as a secret.
- **Governance:** a `CLAUDE.md` — *make no assumptions, ask before adding course content, don't invent
  material* — downstream of a planning repo, with an explicit source-priority chain.
- **Economics:** ~**$30–50/term**, ~2–3 weeks to build originally. Near-zero maintenance.
- **Why it transfers cleanly:** same instructor, same TCU/D2L/Cloudflare plumbing, **same developer** → the
  architecture is effectively copy-paste; only the content (system prompt + context modules) changes.

## Recommendation: **YES — but re-aimed**
MALA is **async**, so its bot fills in for absent live instruction. WRIT is **online synchronous**, so a
tutor adds little *during* class. Point it instead at the **independent work** — homework (HW1–4) + the
capstone — done solo, at night, on the student's **own dataset the instructor can't pre-debug.** It is
*"office hours that never close."*

**Why the fit is unusually good:**
1. The course's **"errors are learning" + ungrading** pedagogy is exactly what a Socratic, traceback-reading,
   no-solutions tutor does best.
2. Python tracebacks intimidate humanities students more than broken HTML; demystifying them one at a time
   matches the course's incremental, predict-then-run voice.
3. Ungrading lowers the cheating incentive, so a *"guide not generator"* bot **reinforces** the model rather
   than undermining it.

## Scope: an MVP "Python debugging companion"
**Not** a clone of MALA's 19 fixed lessons. Python homework is open-ended, so the analog is **one strong
system prompt** + a **light assignment-context selector** (a dropdown of HW1 / HW2 / HW3 / HW4 / Capstone /
"just exploring" that appends a short per-assignment context block — task spec, libraries in play, the most
common errors for that unit — to the base prompt).
- **Effort:** ~3–5 days (the architecture already exists to fork).
- **Model:** Haiku 4.5 (step up to Sonnet only if traceback reasoning feels thin in testing).
- **Cost:** ~$30–50/term.
- **Stack:** fork the MALA Cloudflare Worker; swap `system-prompt.js` for the WRIT draft; replace the fixed
  lesson modules with assignment-context blocks.

## OPEN DECISION (instructor's call): timing — *still open*
- **Ship the MVP before launch** (2026-07-06; HW1 lands Day 5) → a tutor from day one.
- **OR launch first, observe** where students actually get stuck, build for the back half / next offering →
  lower risk; real failures shape the prompt (mirrors how the MALA lessons were frozen only after an eval).

*Working lean (not a decision):* MVP-before-launch **if** a few days are free before launch; otherwise
observe-first is the safer call. **No build work has started.**

## Artifacts
- [`CHATBOT_TUTOR_SYSTEM_PROMPT_DRAFT.md`](CHATBOT_TUTOR_SYSTEM_PROMPT_DRAFT.md) — the **full draft system
  prompt** (the high-leverage piece): WRIT voice; **Colab not VS Code**; pandas/VADER/gensim; the TX Ten
  Commandments corpus; ungrading + predict-then-run; the **one rule — guide, not code generator**;
  AI-honesty `#comment` disclosure aligned to the syllabus AI policy. Editable prose — tune the voice freely.

## Offered next steps (not yet done — pick when build is greenlit)
1. **Draft the HW1 assignment-context block** — the first thing the bot needs at launch (HW1 is the Day-5
   assignment, and the only one with an *intentional* error cell to read).
2. **Write adversarial test conversations** ("just give me the answer, I'm out of time") to pressure-test the
   no-solutions guardrail *before* students see it — the single guardrail most likely to leak under pressure.
3. **Fork & wire the worker** — clone the existing private `TCU-DCDA/WRIT20833-chatbot` repo first to see
   whether it's an empty placeholder or already has a start, then port the MALA architecture.
