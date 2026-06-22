# Chatbot tutor — scope & decision note

**Status:** ✅ **MVP BUILT (2026-06-18)** — the instructor greenlit the MVP and it is **code-complete** in the
private repo **`TCU-DCDA/WRIT20833-chatbot`** (cloned as a sibling at `../../WRIT20833-chatbot`). Remaining
work is **deployment only** (see that repo's `DEPLOY.md`). The original evaluation/scope is preserved below
for the record. · *Last updated 2026-06-18.*

> **What got built (all on `main` in `WRIT20833-chatbot`):**
> - Re-aimed the existing March scaffold from code-along lessons → an **after-hours homework/capstone tutor**
>   (the synchronous-course logic in this doc). Stripped all web-dev content → **Colab + Python only.**
> - **Five assignment-context blocks** — HW1–4 + Capstone — in `worker/lessons/`, authored from the STUDENT
>   notebooks / capstone sheet only (no answer keys), solution-free.
> - **Hardened the "guide, not generator" guardrail** into a hard clamp, tuned with worked ❌/✅ examples and
>   adversarially tested (~15 attack vectors: "show me the syntax," "is this right?," pseudocode,
>   authority, emotional, multi-turn assembly, "similar template," etc.). Plus two block-specific guards:
>   HW4 won't name/interpret topics; the **Capstone won't ghostwrite the essay** (the AI-writing-honesty line).
> - **Security:** access-code gate (`ACCESS_CODE` secret) + per-IP rate limiting (`RATE_LIMIT` KV, 12/min +
>   300/day) — both verified locally.
> - The **draft system prompt** in this folder is now **implemented** as
>   `worker/lessons/system-prompt.js` (and hardened well beyond the draft). The live worker is the source of
>   truth; the draft here is the historical starting point.
> - **Open dial:** the "confirm-my-guess" behavior (light confirmation vs. verify-by-running).
> - **Not done:** deployment (KV namespace, secrets, prod URL + CORS, `wrangler deploy`, host frontend,
>   embed in D2L); authoring is not needed for that.

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
