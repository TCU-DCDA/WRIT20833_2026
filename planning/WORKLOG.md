# WORKLOG — WRIT 20833 2026 port (session handoff)

**Status:** all work merged to `main`; repo **public**; course site **live** (GitHub Pages, `main/docs` →
https://tcu-dcda.github.io/WRIT20833_2026/). No active feature branch — start a fresh one per task off
`main`. · **Last updated:** 2026-07-01 (**project-evaluation pass — 🔴 found the HW answer keys + builders
re-committed to public `main`**; see the session entry directly below + `planning/PROJECT_EVALUATION_2026-07-01.md`.
Prior: 2026-06-26 FORMAT CHANGE to the 8-week in-person fall offering; 2026-06-21 verification pass;
chatbot-tutor MVP BUILT in the private `WRIT20833-chatbot` repo — deployment pending)

---

## Latest session — 2026-07-01 (project-evaluation pass — full open-state audit)
No content changed — an **evaluation-only** pass (report: `planning/PROJECT_EVALUATION_2026-07-01.md`,
authored on branch `claude/open-project-evaluation-lzee77`). Three parallel audits (re-pacing
consistency · day-by-day content coverage · open threads/git state), all claims re-verified directly.
- **🔴 URGENT FINDING — the HW1–4 answer keys + `_build_hw2/3/4.py` are tracked on public `main` again.**
  Merge `67899e9` merged a stale pre-scrub clone back over the 2026-06-11 BFG rewrite (parent ^1 has the
  7 files, parent ^2 = scrubbed main has 0) — the exact two-machine `pull`-after-force-push failure this
  WORKLOG warns about below. Remediation (instructor: re-scrub + force-push + hard-reset clones + a
  guard against recurrence) is spelled out in the report §1. **Not fixed in this pass** (history rewrite
  on `main` = instructor's call).
- **🟠 Bug:** `docs/schedule.html` has 2 broken `href="CAPSTONE_2026.md"` links (404 on Pages); fix =
  map it to the absolute GitHub URL in `build_schedule_html.py` (as `build_index.py` does) + regenerate.
- **✅ Otherwise clean:** the 8-week re-pacing is 100% consistent across every student-facing surface
  (dates, due dates, day-homes D8/D10/D16/D19, no stale summer text, no `[...]` left in the syllabus),
  and all 24 sessions have their promised artifacts (9/9 code-alongs, HW1–4, 8/8 lecture pairs, corpora,
  stylometry bundle). Readiness verdict ≈ the standing ~90% — the key exposure is the one real fire.

---

## Latest session — 2026-06-26 (FORMAT CHANGE: 4-week summer → 8-week fall, in-person)
**The July section was canceled.** The course now runs as the TCU **second 8-week session ("8W2"): Mon Oct
19 – Fri Dec 18, 2026, Monday/Wednesday/Friday, 2 hrs/day, IN PERSON, enrollment ≤ 20.** That's **24
sessions / ~48 contact hours** (up from the summer plan's 20/40 — actually back to F25's full budget). No
class the week of Thanksgiving (Nov 23–27; classes recess after Fri Nov 20, resume Mon Nov 30) — verified
against the TCU registrar's Fall-2026 8W2 calendar. The capstone presentation on Fri Dec 18 is the Final
Evaluative Exercise (no separate final; grades due Mon Dec 21).

**Key framing:** the **content is calendar-agnostic** (notebooks/lectures/HW use "Day N / Week N", not
dates) — so **no notebook or lecture content changed.** This was a **re-pacing + re-dating + in-person
re-framing**, not a content rebuild. **Assignments unchanged: 5 graded pieces (HW1–4 + Capstone).** The +4
sessions were spent as breathing room (Week-1 foundations un-compressed into 2 weeks; an HW2 work session;
more capstone development + a presentation dry-run), NOT new deliverables.

**New pacing (8 weeks × MWF = 24 sessions):**
- Wk1 (Oct 19–23): foundations — variables · strings · conditionals · **R1 due Fri 10/23** · D1
- Wk2 (Oct 26–30): foundations — lists/loops · functions/dicts · recap · **HW1 assigned**
- Wk3 (Nov 2–6): term frequency + HW1 debrief (**HW1 due, HW2 assigned**) · AI code+stylometry seed · HW2 work · D2
- Wk4 (Nov 9–13): pandas 01 (**HW2 due**) · pandas 02 · data workshop
- Wk5 (Nov 16–20): VADER (**R2 midterm, HW3 assigned**) · VADER deep · HW3 work · D3 — *break begins after Fri 11/20*
- Wk6 (Nov 30–Dec 4): topic intro (**HW3 due**) · topic deep (**HW4 assigned**) · integration demo (**capstone proposal due**)
- Wk7 (Dec 7–11): Going Public (**HW4 due**) · capstone work 1 · capstone work 2 · D4
- Wk8 (Dec 14–18): capstone work 3 + peer review · polish/dry-run · **presentations (Capstone + R3 due) Fri 12/18**

Lecture day-homes shifted: AI Agency D7→D8, Data Archaeology D8→D10, NLP & Topic Modeling D14→D16, Going
Public D17→D19 (updated in `build_lectures.py` + each `materials/lectures/ml*.md` meta + `build_index.py`).
Discussions now biweekly (Wks 1/3/5/7).

**Files updated this session (all in this student-facing repo; NOT yet committed):**
- `COURSE_SCHEDULE_2026.md` — full rewrite to the 8-week/24-session MWF grid + Thanksgiving gap.
- `SYLLABUS_2026.md` — term/dates/meeting block, **in-person modality** (dropped Zoom + class-recording;
  reworked Attendance, Technology, Class Norms), all due dates, skills map, embedded grid, lecture notes.
- `CAPSTONE_2026.md` — dates + timeline table.
- `build_index.py`, `build_schedule_html.py`, `build_lectures.py`, the 4 `ml*.md` metas — labels, session
  count, day-homes, 8-week week-tint palette. **Regenerated `docs/` (index + schedule + 8 lecture pages/decks).**
- `README.md` — front-matter; both `PROPOSED_4WEEK_SCHEDULE.md` copies banner-marked **SUPERSEDED**.

**Instructor follow-ups:**
- ✅ **Section / meeting time / room confirmed (2026-06-26):** section **020**, **MWF 10:00–11:50 AM**,
  **Schar Hall Room 2003** — filled into the syllabus.
- The AddRan Word copy is now `WRIT20833-020_Fall2026_Rode.docx` (instructor-maintained in Word).
- Secondary/historical docs NOT rewritten (still reference the summer framing): `planning/PORT_ASSESSMENT_2026.md`
  (contact-hour history), `planning/SYLLABUS_COMPLIANCE.md`, the chatbot scope/system-prompt drafts. Update
  if/when they're next touched; none are student-facing.

A running handoff so any new session (VS Code, web, or CLI) can resume with zero ramp-up.
Read this first, then `planning/PORT_ASSESSMENT_2026.md` (context) and
`planning/PROPOSED_4WEEK_SCHEDULE.md` (the plan + open decisions).
**Note the 2026-06 reorg:** the published course site is in `docs/`; instructor process docs (incl. this
file) moved to `planning/`; TCU/AddRan source docs are in `reference/`; answer keys + HW builders live in
the private `TCU-DCDA/WRIT20833_2026_keys`.

---

## Latest session — 2026-06-21 (verification pass: Day-14 install cell + first-half re-execution)
No content authored — a **readiness-verification** pass (re-running things rather than trusting the log).
- **Day-14 / HW4 topic-modeling install cell — ✅ VERIFIED (closes open-thread #7).** Tested
  `!pip install -q gensim vaderSentiment` in a clean **Python-3.12 venv** (mid-2026 Colab proxy): resolves
  **gensim 4.4.0 · numpy 2.4.6 · scipy 1.18.0**, the exact import chain imports clean, and a full LDA
  smoke test passes (Dictionary + doc2bow incl. the empty-bag `[]` edge + `LdaModel` train + `show_topic`
  + `get_document_topics`). Current gensim supports numpy 2.x + scipy ≥1.13 natively → the old
  `scipy.linalg.triu` breakage class is gone; since Colab already ships numpy 2.x, expect no downgrade /
  no restart. Older end of the range also confirmed (anaconda py3.11 · numpy 1.26 · scipy 1.11 · gensim
  4.3.0 imports fine). **Residual = one 60-sec live Colab click before Day 14.** (Already shipped as commit
  `c9c7a46`; open-thread #7 + top status line updated.)
- **First-half (Days 1–10) code-alongs — ✅ RE-EXECUTED CLEAN TODAY (no bit-rot since the 2026-06-17 check).**
  Ran all 7 first-half code-alongs top-to-bottom via `/opt/anaconda3/bin/python` (139 code cells; `!`
  shell/pip lines skipped): Variables (25 — the lone error is the **intentional** "read the error message"
  TypeError), Strings (21), Lists/Loops/Conditionals (30), Dictionaries/Functions (17), Term Frequency
  (11), Pandas 01 Found Data (19), Pandas 02 Cleaning (16) — **all clean**.
- **Readiness snapshot (this session's verdict):** **Day 1 = ready to teach (100%)** — both opening
  lectures (page+deck+imagery), the Variables code-along, and the D1 prompt all confirmed live.
  **Week 1 (Days 1–5) ≈ 98%**, **first half (Days 1–10) ≈ 96%**, **whole course ≈ 90%** (≈93–95% excluding
  the optional, un-deployed chatbot). Every residual is instructor-discretion polish or non-content
  paperwork (conceptual-framework fold-ins; AddRan Word `.docx` sync; CSV/HUM vetting-form trim) — **no
  unbuilt or broken teachable material** anywhere in the first half.

## Earlier session — 2026-06-18 (chatbot-tutor MVP BUILT — code-complete, deployment pending)
*Work lives in the private sibling repo **`TCU-DCDA/WRIT20833-chatbot`** (`../../WRIT20833-chatbot`), not this
repo. Full scope + build summary: `planning/CHATBOT_TUTOR_SCOPE.md`. The repo's own `CLAUDE.md` + `DEPLOY.md`
are the operating docs.*
- **Greenlit + built the MVP** "Python debugging companion" — an **after-hours tutor for the independent
  homework + capstone** (NOT code-along lessons; WRIT is synchronous). Re-aimed the existing March scaffold
  off the code-along-lesson model and **stripped all web-dev content → Colab + Python only.**
- **Five assignment-context blocks** authored (`worker/lessons/hw1.js…hw4.js`, `capstone.js`) from the
  **STUDENT notebooks / capstone sheet only — never the answer keys** — solution-free, in a shared format.
- **Hardened the "guide, not generator" guardrail** into a hard clamp: never writes code that completes an
  exercise (tested against ~15 attack vectors — "show me the syntax," "is this right?", pseudocode,
  authority, emotional pressure, multi-turn assembly, "similar template"…), tuned with worked ❌/✅ examples.
  Two block-specific guards: **HW4 never names/interprets a student's topics**; the **Capstone never
  ghostwrites the essay** (the AI-writing-honesty line — code help is fine, the prose must be theirs). It
  still teaches concepts freely on **neutral** examples.
- **Security added + verified:** access-code gate (`ACCESS_CODE` secret) + per-IP rate limiting (`RATE_LIMIT`
  KV, 12/min + 300/day → 429). Model `claude-haiku-4-5`, ~$30–50/term.
- **Docs:** the system-prompt draft in `planning/` is now **implemented** (live worker is source of truth);
  `CHATBOT_TUTOR_SCOPE.md` marked BUILT; the chatbot repo got a rewritten `CLAUDE.md` + a new `DEPLOY.md`.
- **Remaining = deployment only** (create KV namespace, set secrets, prod `API_URL` + CORS origins,
  `wrangler deploy`, host the frontend on Pages, embed in D2L). **Open dial:** the "confirm-my-guess" behavior.
- **Process note:** per instructor preference, this repo + the chatbot repo are **solo → commit straight to
  `main`, no per-task branches/PRs** (recorded in session memory).

---

## Earlier session — 2026-06-18 (ML9 authored + ML8 harvested → open thread #9 CLOSED; ALL lecture work done)
- **ML9 "Going Public" (Day 17) AUTHORED** (`materials/lectures/ml9.md`, branch `claude/lecture-ml9`).
  Mined the F25 `lecture-9-public-arguments` deck, **keeping the analysis→public-argument spine and cutting
  the web-portfolio delivery** (HTML/CSS/GitHub-Pages = the dropped web-dev half). **Re-homed to the
  capstone:** the 2026 public artifact is the data-driven-opinion **essay + presentation**, not a website.
  **Spine:** *your analysis isn't finished until it argues.* Kept *Mapping Police Violence* as the
  analysis-as-public-intervention case, the public-humanities tradition, the moral floor + knowledge→wisdom
  + preserve-the-quarrel framework ties, and the reflection-prompt-as-capstone-seed. Registered in
  `build_lectures.py` + `build_index.py` (card flipped from "(under review)"/`link=None` → live thumbnail
  using the already-generated `ml9_title.jpg`); Day-17 lecture cell set to "Going Public" in
  `COURSE_SCHEDULE_2026.md` + `SYLLABUS_2026.md` (work session keeps "validation / being wrong as learning").
- **ML8 "Code as Rhetoric" HARVESTED, not built** (instructor decision this session). Its examples are
  HTML/CSS (cut half); its durable thesis — *every technical choice is a rhetorical choice; structure =
  argument* — folded into **ML1 "Connotations & Code"** (closing slide now says code *argues* a value, not
  just encodes one, forward-linking to going public) and **ML9** (presentation as public argument). No
  `ml8.md`. F25 slide files were image-prompt specs only — nothing else to mine.
- **Open thread #9 (back-half lecture audit) is now FULLY CLOSED** — ML2 cut, ML8 harvested, ML9 authored.
  **There is no remaining lecture work.** All scheduled mini-lectures (ML0/1/3/4/5/6/7/9) are live reading
  pages + decks; ML8 harvested; ML2/ML10–12 cut. Updated `LECTURE_SOURCE_NOTES.md` (ML8+ML9 triage),
  `CONCEPTUAL_FRAMEWORK_2026.md` §6 (homing dial → decided), and both schedule/syllabus footnotes.
- **Build verified:** `build_lectures` + `build_index` + `build_schedule_html` all exit 0 (the
  `assert_accessible` guard passed); ml9 reading page + deck emitted (7 slides), card links, image resolves,
  no markdown leak. Shipped as **PR #29 (merged)** — branch `claude/lecture-ml9` deleted.

---

## Earlier session — 2026-06-17 (first-half readiness check + chatbot-tutor evaluation)
*(Authored on the home machine before a machine move; left on open PRs #27 + #28 that predated the ML9
merge. Reconciled onto `main` 2026-06-18 — see the chatbot-scope PR; #27 + #28 closed as superseded.)*
- **First-half readiness — ✅ READY TO TEACH (Days 1–10).** Verified every first-half asset by *executing*
  the notebooks: all 7 first-half code-alongs run clean (Variables has exactly **1 intentional** TypeError —
  the "read the error message" cell); HW1 + HW2 execute clean with **no leaked answer keys**; the pandas
  notebooks are self-contained (sample data embedded, live network calls commented out); six first-half
  lecture decks built; R1 + D1 + D2 prompts written.
- **Day-6 relabel (was PR #27, now folded in):** "Data as evidence" is the lone named lecture with no deck →
  relabeled **"(brief framing — no deck)"** in `COURSE_SCHEDULE_2026.md` + `SYLLABUS_2026.md` (the Week 1→2
  pivot, delivered live to open the Term-Frequency code-along). `docs/schedule.html` regenerated.
- **Chatbot-tutor evaluation (no build yet).** Evaluated whether to build a course Python tutor like the
  MALA 60970 bot. **Verdict: YES, re-aimed at the independent homework + capstone** (WRIT is synchronous, so
  a tutor helps after-hours, not during class); MVP "Python debugging companion," ~3–5 days, Haiku 4.5,
  ~$30–50/term. **Full eval + the open timing decision now live in
  [`CHATBOT_TUTOR_SCOPE.md`](CHATBOT_TUTOR_SCOPE.md)** (consolidated from this session's prose); the draft
  system prompt is at `CHATBOT_TUTOR_SYSTEM_PROMPT_DRAFT.md` (was PR #28, now folded in). **Build remains an
  open instructor decision** — nothing built.

---

## Earlier session — 2026-06-16 (ML7 authored → all scheduled lectures done; docs swept current)
- **ML7 "NLP & Topic Modeling" (Day 14) AUTHORED (PR #25)** → **all scheduled lectures now complete**
  (ML0/1/3/4/5/6/7). Mined the F25 `lecture-7-nlp-topic-modeling` deck into `materials/lectures/ml7.md`
  (reading page + self-contained deck), registered it in `build_lectures.py`, and flipped its dashboard
  card from placeholder → linked thumbnail in `build_index.py`. **Spine:** *the machine clusters the
  words — you name the meaning.* Locked to the Day-14 Topic Modeling code-along (LDA/Gensim, `num_topics`
  as an authored dial, the muddy 123-comment Texas Ten Commandments payoff, LDA stochasticity) and
  cross-refs Data Archaeology + Classification Logic by concept. Title art `ml7_title.jpg` active; one
  interior split slot (`ml7_tangle.jpg`) prepped inert. Triage logged in `LECTURE_SOURCE_NOTES.md`; the
  new pending deck image tracked in `IMAGE_PROMPTS.md`.
- **Handoff brought current (PRs #24, #26).** #24 caught the resume docs up from their stale "PR #18 /
  imagery-is-next" state to PR #23; #26 (this pass) swept **all** planning docs current after ML7 landed —
  NEXT_SESSION + WORKLOG now read "all scheduled lectures done, ML8/ML9 the only remaining (parked) work."
- **Only remaining lecture work = the parked back-half audit (#9):** ML8 (Code & Rhetoric) + ML9 (Going
  Public, Day 17) await a keep/cut/fold decision before any authoring. No open GitHub issues.
- **Session shipped PRs #24–#26, all merged + live.** Site at https://tcu-dcda.github.io/WRIT20833_2026/.

---

## Earlier session — 2026-06-16 (lecture imagery placed + CSV/HUM examples)
- **First-half lecture imagery COMPLETE (PR #21).** The 7 warm-palette "Reading Room" paintings were
  generated and placed: ML4 (AI Agency) + ML6 (Data Archaeology) got their title art + split-slide
  images (slots uncommented in the `.md`, paths added to the `build_index.py` LECTURES tuples), so the
  dashboard's last two **placeholder boxes for built lectures are now real thumbnails**. All six built
  lectures (ML0/1/3/4/5/6) now ship with imagery. (The handoff's old "clearest next task" — imagery —
  is **done**.)
- **`materials/lectures/IMAGE_PROMPTS.md` added (PR #20)** — the shareable, reusable prompt spec for the
  7 lecture images (warm parchment + muted-green palette), so re-generation/extension stays on-style.
- **CSV/HUM core work-examples drafted (PR #22)** → `planning/CSV_HUM_WORK_EXAMPLES.md`, for the
  instructor to trim to the AddRan re-vetting form (closes the #10 deliverable).
- **Handoff hygiene (PRs #19, #23):** marked the syllabus complete in the docs (#19) and dropped the
  instructor-only AddRan/Word to-do item from the handoff (#23).
- **Net state:** the two remaining dashboard lecture cards with `link=None` are **NLP & Topic Modeling**
  (ml7, Day 14) and **Going Public** (ml9, Day 17) — both have title art but **no `ml*.md` authored yet**.
  ML7 is the clear next content task (core Day-14 payoff, unblocked, F25 source = `lecture-7-nlp-topic-
  modeling`); ML8 (Code & Rhetoric) + ML9 stay **parked** pending the thread-#9 back-half audit.
- **Session shipped PRs #19–#23, all merged + live.** No open GitHub issues.

---

## Earlier session — 2026-06-15 (lectures complete + site polish)
- **Lectures ML4 (AI Agency) + ML6 (Data Archaeology) authored** (PR #8) → **first-half lectures complete**
  (ML0/1/3/4/5/6; reading page + self-contained deck each). ML5 + ML1/3/5 imagery merged first (PR #7).
- **ML2 "Sacred Boundaries" SETTLED → CUT** (PR #9, open thread #9): redundant now that ML6 carries the
  privacy/collection-ethics core + ML0 carries the noumena-limit point; Day 2 is a no-mini-lecture day.
- **ML numbers dropped from all student-facing surfaces** (PR #10): lectures shown by **title + day**;
  in-lecture cross-refs reworded to concepts/titles. ML-numbers kept ONLY as internal slugs (`ml*.md`/
  `.html`) + planning-doc labels. Live URLs unchanged.
- **Site UX polish:** deck **home-nav** (↤ Lectures · Reading, PR #11), masthead **hero banner**
  (messy_humanities, top-anchored crop, PR #11), **external links open in new tab** (auto via
  `site_theme.PAGE`, PR #11), **lecture-card thumbnails + proportioned placeholders** (PR #12), and
  **dashboard reorder** → 00 Start · **01 Lectures** · 02 Code-alongs · 03 Homework · 04 Capstone ·
  05 Resources (PR #13).
- **Lecture imagery state:** ML0/1/3/5 have warm-palette title art (real dashboard thumbnails); **ML4 +
  ML6 ship text-forward** with prepped inert image slots in their `.md` (`<!-- IMG PROMPT … -->` +
  commented `![]()`), and their dashboard cards show **placeholder boxes**. **To fill:** generate the
  warm-palette image → save to `materials/lectures/images/` → (a) uncomment the `![]()` in the lecture
  `.md` to activate its split slide, and (b) add the path to that lecture's `LECTURES` tuple in
  `build_index.py` to turn the dashboard placeholder into a thumbnail → rerun the generators. The 4 missing
  title images = AI Agency, Data Archaeology, Topic Modeling, Going Public.
- **Accessibility — WAVE-clean (PRs #15, #16).** WAVE flagged low-contrast + very-small-text. Fixed in the
  shared theme (cascades to dashboard/schedule/reading pages/decks): darkened three muted tokens to clear
  **WCAG AA 4.5:1** (`--muted` #6f7463→#696e5e, `--faint` #a6aa99→#6a6c61, `--clay` #9c6f3f→#8c6338) + the
  `.m-worksession` pill (#9c6f3f→#8d6539); raised every UI font under **12px** to a 12px floor (the 10–11.5px
  mono micro-labels). Structure (alt/lang/titles/headings/links) was already clean. **Baked into the build
  (#16):** `site_theme.assert_accessible(extra_css="")` fails the build if any `font:`/`font-size:` < 12px or
  if `--muted/--faint/--clay` drop below AA on paper/surface — called via `write_stylesheet()` (all
  generators) + `build_lectures` passes its `DECK_CSS`. So the WAVE fixes can't silently regress.
- **Syllabus fully filled (PR #18).** Pulled the instructor-completed fields out of
  `WRIT20833-020_Summer2026_Rode.docx` (section 020, component LCL, Zoom, Dr. Curt Rode, office Schar 2006,
  office hours via Calendly, phone, c.rode@tcu.edu, D2L d2l.tcu.edu, official catalog description, program
  connections, CSV+HUM confirmed) and finished the rest in markdown (meeting time 10:05 AM–12:00 PM
  Central; Grading Concerns; TCU Online submissions note; dropped loaner-laptop + supplementary-resources
  lines). **No `[...]` placeholders remain.** The `.docx` is the maintained AddRan submission copy (QR
  image + template formatting), **handled by the instructor** and not regenerated from the md.
- **Session shipped PRs #7–#18, all merged + live.** Site at https://tcu-dcda.github.io/WRIT20833_2026/.

---

## Context in one paragraph
WRIT 20833 ("Intro to Coding in the Humanities") runs **online synchronous, 4 weeks,
2 hrs/day × 5 days ≈ 40 contact hours, starting 2026-07-06**. It is a **port** of the mature
16-week Fall 2025 course (`TCU-DCDA/WRIT20833_2025`) — not new content. Chosen scope: **drop
the web-dev/portfolio half** (overlaps MALA 60970), keeping Python foundations + the
cultural-analytics arc (term frequency → sentiment → topic modeling) into a notebook+essay
capstone. The contact-hour budget is comparable to F25, so this is re-pacing + a modest trim,
not a content cliff.

## Locked decisions
- Scope: drop portfolio half (tentative-but-working; see open decision #1).
- **VADER stays**; topic modeling is **Gensim** (F25 replaced MALLET with Gensim).
- **Walsh independence is course-wide** — Walsh is optional reading only, credited as
  inspiration/model in `ACKNOWLEDGMENTS.md`.
- **Ungrading evaluation (course-wide)** — carries F25's philosophy ("earned insight over
  clean code", see `PORT_ASSESSMENT_2026.md`). Work is evaluated on engagement, reflection,
  and labor — the required `#comments`, predict-then-run guesses, Weekly Experiments, and
  reflective write-ups — **not** on correctness scores. Implications for authoring: avoid
  "grade/points/score" framing (say "evaluated/expected/complete"); answer keys are
  **instructor references + discussion fodder, not rubrics**; Submit checklists emphasize
  completion + reflection over right answers. The capstone "essay weight" open decision means
  *emphasis/expectation*, not a points scheme.
  - **Submit-checklist wording (fixed 2026-06-11, applies to all HW + future assignments):** do **not**
    ask that the notebook "runs top to bottom without errors" — that's a clean-code/correctness demand
    that contradicts ungrading + "errors are learning" (and HW1's own A4/experiments). House wording:
    *"I ran every cell. Where something still breaks, I left a `#comment` about what I tried and what I
    learned — errors are part of the work here, not something to hide or delete."* Applied to HW1–4.
  - **`#comments` requirement wording (same date/scope):** not "Required: `#comments` in **every** code
    block" / "Every code cell has `#comments`" (reads as a per-line mandate). House wording keeps the
    expectation but drops the rigidity — heading *"Expected: frequent, meaningful `#comments`"* (comment
    often and wherever a choice/question comes up, not every line; **frequent, relevant comments are
    expected** — they're where thinking shows); submit *"I used `#comments` frequently and meaningfully…
    (not every line, but throughout)."*
- **Assignment renumbering (2026):** HW1 = foundations · HW2 = term freq · HW3 = freq+sentiment
  · HW4 = topic modeling+integration · Capstone. (F25 map: HW1=F25 HW2, HW2=F25 HW1,
  HW3=F25 HW4-1, HW4=F25 HW4-2.)
- Stylometry exercise placement: **close-reading seed on Day 7**, computational half +
  synthesis in **Week 4 / capstone track**.
- **House convention — "honest about borrowed code"** (apply to every notebook from HW2 on,
  incl. HW3 + capstone). Two paired framings:
  1. **Setup cells are plumbing.** Any data-loading/import cell above a student's level
     (regex, `urllib`, `os.path`) gets a short "About the setup cell" markdown note first:
     run it, don't read every line; you *use* a tool via its **interface** before you can
     build its **insides**; then list the 3–5 names the cell hands them. (HW1 precedent:
     the A4 try/except parenthetical.)
  2. **Code you build by hand, you'd normally borrow.** When students hand-build a common
     routine (term frequency, sentiment, etc.), add a note: it's prefab code almost nobody
     writes from scratch (Stack Overflow long before AI, an AI today); **borrowing is
     expected, not cheating**; we build it once so you can *read and judge* a borrowed/AI
     version. Threads into **Day 7** (reading/improving AI code, ML4 AI Agency).

## Conceptual framework — see `CONCEPTUAL_FRAMEWORK_2026.md`
The course's full intellectual through-line now lives in its own canonical doc:
**`CONCEPTUAL_FRAMEWORK_2026.md`** — epistemological spine (noumena→wisdom), "hear the human at scale,"
the quarrel / ML0 "the mess," voice-through-difficulty (writing in the age of AI), the dinner-party /
stadium illustration, the moral floor ("billions who don't know to care"), the Auden / Brueghel anchor,
the theme→artifact map, and candidate fold-ins. **Edit that doc, not this section, to avoid drift.**

**Status of the conceptual work (handoff flags):**
- **Noumena→wisdom graphic** ported (`materials/images/noumena_to_wisdom_pipeline.png` + its README) and
  a **Day-1 framing passage drafted** (`materials/Day1_Framing_Noumena_to_Wisdom.md`). Not yet wired into
  an actual lecture or the syllabus.
- **Through-line + moral floor + Auden** captured in the framework doc. **Not yet woven into student-facing
  materials** — all fold-ins (subtitle gloss, a learning outcome, Day-1/Day-7/Day-12 sentences, the
  capstone standard, the AI-use-policy refinement) remain the instructor's call (framework doc §6).
- **Open dials:** keep the Kantian vocabulary explicit or swap to plain language; lecture homing
  (re-home ML9 → Day 17, harvest ML8) — see open thread #9. (ML2 "Sacred Boundaries" settled → **cut**.)

## Done this session (all committed + pushed)
- `PORT_ASSESSMENT_2026.md` — readiness/port analysis (kept in F25 numbering; documents history).
- `PROPOSED_4WEEK_SCHEDULE.md` — 20-session draft (drop-portfolio scope, 2026 numbering).
- `ACKNOWLEDGMENTS.md` — credits Walsh as inspiration/model.
- `notebooks/homework/WRIT20833_HW1_2026.ipynb` + `_ANSWER_KEY` — **HW1 (foundations),
  Walsh-independent**, 6/4/2 exercises + experiments; answer key runs clean (A4 uses
  try/except so the notebook runs top-to-bottom).
- `materials/stylometry/` — "Reading for the Seams" exercise: handout (`Reading_for_the_Seams.md`),
  computational notebook (`WRIT20833_Stylometry_Reading_Seams_2026.ipynb`, validated),
  and the `ai_voice_claude_analysis.pdf` exemplar.
- `notebooks/homework/WRIT20833_HW2_2026.ipynb` + `_ANSWER_KEY` — **HW2 (term frequency,
  "Whose Words Win?"), Walsh-independent**, pre-pandas plain Python. 5/4/2 exercises +
  experiments, built from the locked design below. Setup cell reuses F25's exact
  `split_into_words` + `stopwords` and a `load_text()` with raw-GitHub fallback. **Answer key
  validated: all 11 code cells run top-to-bottom against the local corpora; every inline
  expected-output comment matches the real counts.** Built via `_build_hw2.py` (kept in-folder
  for reproducibility / regenerating both notebooks).

## HW2 (term frequency) — ✅ DONE (was: design locked, data built, notebooks not yet authored)
**Now authored (see "Done this session"); the locked design is recorded below for reference.**
Decisions made with instructor this session:
- **Design:** "Whose words win? — a live debate vs. the document it invokes." Walsh-independent,
  built in the **2026 house style** (Parts A/B/C of discrete exercises + 2–3 Weekly Experiments +
  a clean-running ANSWER KEY). Pre-pandas (assigned Day 6) → **plain Python only, no pandas**.
  Builds directly on **HW1 C2** ("many comments → one word list").
- **Paired corpus (both committed to `notebooks/data/`, validated):**
  - `tc_youtube_comments.txt` — 123 lines of real 2025 YouTube comments on the TX Ten Commandments law
    (corrected from an earlier "93"; see `notebooks/data/README.md`)
    (cleaned from F25 `TenCommandmentsTX/20833_CBS1_youtube_F25.csv`). The public's voice.
  - `us_constitution.txt` — full Constitution from Gutenberg #5, boilerplate stripped. The text
    the commenters keep invoking (top comment = "put the constitution in classrooms?").
  - Confirmed contrast: Constitution→`shall/states/president/congress`; comments→`commandments/
    religion/god/children/schools`; "constitution" recurs in the comments. Same comment corpus
    feeds HW3 (sentiment) + capstone. See `notebooks/data/README.md`.
- **Planned exercise flow** (not yet written): A1 corpus size (len/set) · A2 raw count shows boring
  function words · A3 stopword-filtered "meaningful words" · A4 predict-then-run edge case (house
  motif — e.g. `most_common(0)`→`[]`) · A5 wrap in reusable `top_meaningful_words(text,n)`.
  B1 top-20 of each corpus · B2 direct count lookup (`counter['constitution']`) → close-vs-distant
  insight · B3 set-difference "distinctive words" · B4 interpretation markdown. C1 custom stopwords
  (10/amp/etc.) · **C2 = optional "bring your own text / paste social media" track** (the BYO/scrape
  arc; note scraping tooling isn't taught until Day 8). Then Experiments + Submit checklist.
- **Setup-cell pattern:** reuse F25's exact long `stopwords` list + `split_into_words` (re.split
  `\W+`, lowercased); `load_text()` checks local + `notebooks/data/` then falls back to the 2026
  raw-GitHub `main` URL (works after merge, like the Colab badges).
- **DONE:** authored `WRIT20833_HW2_2026.ipynb` + `_ANSWER_KEY.ipynb` (HW1 metadata/badge/cell
  schema matched; generated by `_build_hw2.py`) and **validated the key runs top-to-bottom**
  against the local data files. Final flow shipped: A1 corpus size · A2 raw-count problem ·
  A3 meaningful-words filter · A4 predict-then-run `most_common(0)`→`[]` · A5 reusable
  `top_meaningful_words(text,n)` · B1 top-20 each · B2 `comment_counts["constitution"]`=8 vs
  `["commandments"]`=25 · B3 set-difference distinctive words · B4 interpretation write-up ·
  C1 custom stopwords · C2 bring-your-own-text · experiments + submit checklist.

## HW3 (sentiment analysis) — ✅ DONE (built from the port inventory below)
- **Authored** `WRIT20833_HW3_2026.ipynb` + `_ANSWER_KEY.ipynb` via `_build_hw3.py`, 2026 house style,
  **pandas-native**. Title: "Sentiment Analysis: Support, Opposition, and What Counting Missed."
  Flow: A1 explore DataFrame · A2 clean-but-keep-punctuation (vs HW2) · A3 score one comment (VADER
  dict/compound) · A4 predict-then-run **sarcasm edge** ("Oh great…" → +0.625, misses sarcasm) ·
  A5 `.apply()` over the column (mean 0.082 = split crowd); **VADER borrowed-code note** · B1 label
  by ±0.05 cutoff (51 pos/38 neu/34 neg) · B2 one-line `df.plot(kind="bar")` viz · B3 read extremes +
  **human-vs-VADER** check (idxmax/idxmin, deterministic) · B4 interpretation write-up · C1 **freq
  inside pos vs neg camps** — `commandments`/`god` top BOTH (the HW2→HW3 payoff) · C2 BYO/"constitution"
  cut. Ungrading framing throughout; **BYO-primary** (setup defaults to the course corpus as runnable
  fallback + key reference, with a commented `pd.read_csv` for own data). VADER available locally →
  **answer key validated: all 11 code cells run top-to-bottom; inline expected values match.**
- **Data fix:** corrected `notebooks/data/README.md` — the corpus is **123 lines, not "93"** (0 dups;
  a few short CSV→txt wrap-fragments like "Of Texas"/"The"). Didn't affect HW2 (word-blob); does affect
  HW3 (row-per-comment). Left the data as-is (messy real data suits the Week-2 cleaning theme); re-clean
  later only if desired.
- **Open decisions resolved at build:** #1 pandas ✅, #3 viz ✅ (light `df.plot`), #2 BYO-primary 🔶
  (implemented as default-fallback-corpus; not hard-locked).

### HW3 port inventory (verified against F25 source — kept for reference)
Maps to **F25 HW4-1** (worklog renumbering). Lands **Day 13**, Week 3 — *after* pandas (Days 8–9),
so HW3 is **pandas-native** (unlike HW2's deliberately pre-pandas plain-Python). Inventory below was
checked directly against the live `WRIT20833_2025` files (2026-06-10), not just the renumber map.

- **Portable F25 sources (both confirmed to exist):**
  - `notebooks/homework/WRIT20833_HW4-1_Term_Frequency_Sentiment_F25.ipynb` (41 cells) — the homework.
  - `notebooks/codeAlongs/WRIT20833_VADER_Sentiment_Analysis_F25.ipynb` — teaches the technique (Days 11–12).
- **Reuse directly (logic/content):** the arc term-freq → VADER → freq in positive-vs-negative subsets →
  bridge to integration (HW4); its `split_into_words` + enhanced `stopwords` (cells 11–12) = the **same
  idiom HW2 already standardized**, so HW3 inherits our setup; VADER pattern (cells 21–24):
  `!pip install vaderSentiment` → `SentimentIntensityAnalyzer` → `.polarity_scores()['compound']`;
  the **"Human vs. automated sentiment check"** (cells 28–29) is a strong critical-thinking exercise.
- **Adapt before porting (each grounded in an actual F25 cell):**
  1. Pandas-native (`import pandas as pd`, `pd.read_csv`, DataFrame ops) — correct for Day 13; do NOT
     reuse HW2's plain-Python setup cell. **(Settled — keep pandas; see decision #1 below.)**
  2. Built around a student's own scraped CSV (`Replace 'your_filename.csv'`); `notebooks/data/README.md`
     says the YouTube-comments corpus is **reused for HW3** → open decision below (#2).
  3. matplotlib bar charts (cells 18, 27, 33) — **viz IS taught before HW3** (verified 2026-06-10):
     `df.plot()`/matplotlib appear in CA Pandas 01 (Day 8), Pandas 02 (Day 9), and the VADER
     code-along (Days 11–12) — the last is HW3's direct model. So keep viz, light/scaffolded; see
     decision #3. (Corrects an earlier note that said viz wasn't taught by Week 3.)
  4. `!pip install vaderSentiment` — needs the same Colab-2026-image check flagged for topic modeling (#7).
  5. Strip F25 framing: cell 1 = "Midterm Assignment Part 1 — Due October 5th"; drop the date + the
     midterm-part structure (2026 = plain HW3). Strip any Walsh prereq per course-wide convention.
  6. **House-style rebuild, not a copy:** F25 uses "Technical Checkpoint" + emoji "📝 Reflection"; rebuild
     into 2026 house style (Part A/B/C + Weekly Experiments + clean ANSWER KEY), as HW1/HW2 were.
  7. **No F25 answer key exists** (homework dir has student notebooks only) → author HW3 key fresh.
- **Fits the conventions:** VADER is the textbook case of the "honest about borrowed code" convention
  (a pip-installed sentiment model nobody writes from scratch). Corpus reuse keeps HW2→HW3 continuity.
- **Decisions:**
  1. ✅ **SETTLED — keep pandas.** HW3 is the first *independent (solo)* pandas application: pandas
     is taught Days 8–9 (CA Pandas 01/02) and practiced in the Day 10 workshop (whose schedule row
     literally reads "→ sets up HW3"), then reused for topic modeling (Days 14–15), integration
     (Day 16), and the capstone. Without it here, pandas only ever appears in instructor-led
     code-alongs + one workshop until the capstone. Bonus arc: **HW2 plain-Python (count by hand)
     → HW3 pandas (same logic at dataset scale)** mirrors the course's close→distant reading move.
  2. 🔶 **LEANING (not fully settled) — BYO-primary + provided fallback.** Bring-your-own data (from
     the Day 10 "collect & clean your cultural dataset" workshop) is the expected path: matches F25
     HW4-1 ("a dataset of your choosing"), the course's student-chosen-data identity, and maximizes
     the ownership ungrading rewards. The provided **YouTube-comments corpus is the documented
     fallback** (for students whose workshop data isn't clean by Day 13) **and what the answer key is
     authored on** — you can't key arbitrary student data, so the key is a *worked example* on a
     reference corpus (exactly what an ungrading key should be). Note this **inverts HW2's emphasis**
     (HW2 = provided-primary + optional BYO via C2; HW3 = BYO-primary + provided-fallback). Build can
     start under this leaning without fully locking it.
  3. ✅ **SETTLED — viz in, light/scaffolded.** Keep a chart, but students *reproduce* the pattern they
     just saw in the VADER code-along (Days 11–12), not invent one. Use pandas' built-in
     `df.plot(kind='bar')` (introduced Day 8 in Pandas 01) — one line, simpler than raw matplotlib;
     viz here is reinforcement, not new material. Ungrading-appropriate prompt: "make a chart and say
     what it shows" (engagement over correctness).

## HW4 (topic modeling + integration) — ✅ DONE (ports F25 HW4-2; the capstone bridge)
- **Authored** `WRIT20833_HW4_2026.ipynb` + `_ANSWER_KEY.ipynb` via `_build_hw4.py`, 2026 house style,
  pandas-native. Title: "Topic Modeling & Integration: What Is the Conversation Actually About?"
  Flow: A1 tokens-per-doc · A2 gensim dictionary+corpus (bag-of-words; vocab ~648) · A3 predict-then-run
  **empty-bag edge** (`doc2bow` of fragment "The" → `[]`, ties to the wrap-fragment data issue) ·
  A4 train `LdaModel` (num_topics=4, random_state=42, passes=10) · A5 **human names the topics**;
  **LDA borrowed+stochastic note** · B1 dominant topic per doc (`-1` guard for empty) · B2 docs/topic
  + bar chart · B3 **the integration** `groupby("topic")["sentiment"].mean()` (HW2 freq + HW3 sentiment
  + HW4 topics in one line) · B4 three-lens interpretation · C1 num_topics 2-vs-6 (authored knob) ·
  C2 capstone plan.
- **Simplified F25:** dropped nltk/WordNet lemmatization and pyLDAvis (fragile); reuses our
  `split_into_words` + `stopwords`. Only new dependency is **gensim** (installed locally as 4.4.0 for
  validation). VADER sentiment carried over in setup. BYO-primary, ungrading throughout.
- **Validation is weaker than HW1–3 by nature — flagged in the key header.** LDA is **stochastic +
  version-sensitive**, so topic words / per-topic counts / per-topic sentiment are NOT reproducible
  across machines/versions even with `random_state=42`. The key states exact values only for the
  **deterministic** steps (vocab size, the `[]` edge) and describes LDA output **qualitatively**
  (relative warmer/cooler, not absolute signs). **Confirmed: the full 9-cell pipeline runs
  top-to-bottom locally** (gensim 4.4.0); that's the guarantee, not exact-output matching.
- **Caveat for the instructor:** topic modeling on the 123-comment fallback corpus gives overlapping,
  weak topics (single-issue corpus) — fine as a *worked example*, but HW4 genuinely wants a richer BYO
  dataset. This is the same point as open thread #7 (still: test the install on Colab's 2026 image).

## Capstone assignment sheet — ✅ DONE (2026-06-12)
Authored **`CAPSTONE_2026.md`** (root, parallel to `SYLLABUS_2026.md`/`COURSE_SCHEDULE_2026.md`) — the
Final Evaluative Exercise, in 2026 house style + ungrading voice. Three deliverables (notebook + ~800–1,200-word
data-driven-opinion essay + ~3–5-min presentation) on one dataset; **two tracks** — Track A cultural
dataset (primary; own data, provided TX Ten Commandments corpus as fallback) and Track B stylometry
(alternate, links the `materials/stylometry/` handout + notebook). Built directly on **HW4 B4/C2** ("your
capstone in miniature"). Honors every locked convention: integrate ≥2 of the 3 lenses (all three is the
fullest, via HW4's `groupby("topic")["sentiment"].mean()`); **close → distant → close**; the framework
§6 capstone standard verbatim ("give voice… did your analysis sail calmly on, or make someone look?");
**preserve the quarrel**; borrowed-code honesty + AI policy split (borrow code/cite AI, voice your own
writing); 3-point ungrading rubric; CSV core tie. Submit checklist uses the **fixed house wording**
(`#comments` frequent & meaningful, not per-line; "ran every cell… errors are part of the work, not
something to hide"). Timeline matches the schedule (proposal Mon 7/27 → work sessions → peer review →
presentations + due Fri 7/31). **Residual `[...]`:** upload location + exact presentation length
(instructor specifics).
- **Wired in (no orphan):** `build_index.py` capstone card now links the sheet (was a `soon=True`
  placeholder) → **regenerated `docs/index.html`**; schedule Days 16 & 20 link it; README status line +
  Start-here table updated; syllabus capstone row points to it.
- **Open dials left for the instructor** (from the stylometry handout): essay weight/length *relative to*
  Track A vs. B, fixed-vs-student-generated stylometry corpus, and how heavily to foreground
  AI-detection-bias ethics. The sheet states a single shared length (~800–1,200 words) for now.

## Lecture pages — system + ML0 pilot (2026-06-12); ML1/3/4/5/6 since (see 2026-06-15 summary up top)
*(This section documents the original pilot + system design. Current state — ML0/1/3/4/5/6 done, ML2 cut,
de-numbered, thumbnailed — is in the "Latest session" summary at the top and `LECTURE_SOURCE_NOTES.md`.)*
Built the **lecture-page system** + authored **ML0** as the template. The dashboard's Lectures section
is no longer all placeholders — ML0 is a live reading page; the other 8 cards stay "soon."
- **`build_lectures.py`** (new, root) — renders `materials/lectures/*.md` → `docs/lectures/<slug>.html` in
  the shared "Reading Room" theme. Hand-rolled markdown subset (headings, paragraphs, lists, blockquotes,
  images, rules) to match the zero-dependency house style of `build_index.py`/`build_schedule_html.py`.
  Pages live one level under `docs/`, so they link **`../styles.css`** (via `PAGE(css_href=...)`) and
  rewrite repo-relative image paths (`materials/…`) → absolute **raw.githubusercontent** URLs (the same
  "outside /docs → absolute" rule the rest of the site follows; resolves once the repo is public).
- **Lecture format** = a student-facing **reading page** (centered ~50rem measure, serif lead, themed
  blockquote/figure) — reinforces the "reading room" identity, not F25's full-screen slide decks.
- **Theme:** added a `/* lecture / reading pages */` block to `site_theme.THEME_CSS` (so `styles.css`
  carries it for all lecture pages).
- **ML0 content** (`materials/lectures/ml0.md`) — authored as the **"mix"** the instructor chose: F25's
  ML0 "Studying the Mess of the Human Condition" (the human mess: contradiction/ambiguity/subjectivity;
  "where others see noise, we see signal"; Keats's *negative capability*; the code-vs-culture "productive
  tension") **woven with** the 2026 noumena→wisdom framing (the score is never the meaning; bias is
  constitutive; make your choices visible). ~750 words; validated (HTML parses, no markdown leak, figure
  resolves).
- **Dashboard wiring:** `build_index.py` `LECTURES` tuples gained a 4th field (page URL or `None`); the
  card grid links authored pages and keeps the rest `soon=True`. ML0 card now → `lectures/ml0.html`.
- **Slide deck (added same day):** `build_lectures.py` now emits a **second view** per lecture —
  `docs/lectures/<slug>.deck.html` — a **fully self-contained** slide deck (theme inlined via
  `PAGE(css_href=None)`; arrow-key/click nav; `print` → PDF). Same markdown source → reading page + deck,
  no drift. The reading-page masthead links the deck ("Slides ▸").
- **2-column split layout:** a per-slide `<!-- layout: split -->` directive renders text | image two
  columns on the deck (reading page ignores it / stacks). Title slide supports split too.
- **ML0 imagery (warm "Reading Room" palette, self-hosted in `materials/lectures/images/`, JPEG-downsized):**
  4 of 6 slides illustrated — **title** (quill-script → ordered characters), **the human mess**
  (`messy_humanities`, the one on-brand keeper from F25's ML0), **the score is never the meaning** (the
  noumena pipeline), **every arrow is a choice** (brass-valves painting = "every arrow is a human
  decision"). Slide 4's dense section was **split into two slides** ("The score…" + "Every arrow is a
  choice"). Other F25 ML0 images were off-palette; `data_as_categorization` + `tippingScales` earmarked
  for **ML3**. Instructor generated the title/valves images (ChatGPT) to match `messy_humanities`'s style.

**Scale-out — ✅ DONE (2026-06-16).** All settled lectures are authored as `materials/lectures/ml*.md`
with a registry line each: **ML0** Humanities & Coding, **ML1** Connotations & Code, **ML3**
Classification Logic, **ML5** Collective Memory, **ML4** AI Agency, **ML6** Data Archaeology, **ML7**
NLP & Topic Modeling (Day 14, PR #25) — all "Mix" from the F25 decks in
`WRIT20833_2025/docs/lectures/mini-lectures/lecture-*` + the framework. **ML2 CUT** (#9). **ML8/ML9 stay
parked** pending the open thread #9 audit (re-home ML9 → Day 17; harvest ML8's thesis into the
code-is-not-neutral thread). The authoring pattern, if those get greenlit: one md file + one `LECTURES`
line + rerun both generators.

## Other open threads / next steps
1. **Confirm scope** — drop-portfolio (current) vs. full-arc-tightened vs. foundations-only.
3. **Walsh-prereq strip on ported notebooks** — Tutorials 1–4 and the code-alongs open with an
   "assumes Walsh Ch 4–8" block; remove/replace as each is ported (HW1 already done).
4. **Port the carry-over-ready code-alongs — IN PROGRESS (foundations-first pilot).** Goal: every
   *coding* session in `COURSE_SCHEDULE_2026.md` names a real notebook (kill the conceptual bleed).
   - **Already in 2026:** Variables/DataTypes, Lists/Loops/Conditionals (combined; covers Days 3–4).
   - ✅ **Pilot done:** `notebooks/codeAlongs/WRIT20833_Dictionaries_Functions_2026.ipynb` (Day 5) —
     ported from F25 (52 cells → focused 35) into the **2026 code-along style** (warm cultural
     examples; concept→code→"your turn"; Putting-It-Together / Sneak Preview / Playground; `colab`
     metadata matched). Walsh-independent; builds a `count_words` dict → `Counter` to **seed Week-2
     term frequency**. Built by `_build_dictfunc.py`; **all 17 code cells validated top-to-bottom.**
   - **Decision (pilot fidelity):** match-2026-style (not faithful F25 copy) — confirmed.
   - ✅ **Strings & string methods (Day 2) DONE** — `notebooks/codeAlongs/WRIT20833_String_Methods_2026.ipynb`
     (built by `_build_strings.py`; all 21 demo code cells validated top-to-bottom). Ports the **string
     half** of F25's `StrMethods_Conditionals_Loops` (the comparisons/conditionals/lists/loops half already
     lives in `Lists_Loops_Conditionals_2026`, Days 3–4, so this is strings-ONLY). Goes deeper than the
     Day-1 Variables string section by adding replace, strip, membership (`in`), join, startswith/endswith,
     and a chained "clean a real comment → split → count" routine that seeds Week-2 term frequency.
     Walsh- and Drive-mount-independent (F25 read Kafka off Google Drive; here the text is inline).
   - ✅ **Found Data & Pandas Fundamentals (Day 8) DONE** — `notebooks/codeAlongs/WRIT20833_Pandas_01_Found_Data_2026.ipynb`
     (built by `_build_pandas01.py`; all 19 code cells validated top-to-bottom with pandas 2.1.4 +
     matplotlib via `/opt/anaconda3/bin/python`). **Merges the two F25 Day-8 notebooks** (Pandas 01
     Found Data, 54 cells + Instant Data Scraper Ethics, 31 cells) into one 2-hr arc: **collection
     ethics first** (3 pillars: robots.txt / fair-use+scale / attribution; Instant Data Scraper as the
     no-code tool; robots.txt status-code helper that runs **offline** — live `requests` shown
     commented), **then pandas fundamentals** (read DataFrame · head/shape/info · select cols Series-vs-
     DataFrame · boolean filter · value_counts · stats · one light `df.plot` bar) on an **inline sample
     of real-shaped TX-Ten-Commandments YouTube comments** (cols: comment/stance/likes/replies) — the
     course's actual corpus theme, the same table HW3/HW4 run on. **Cleaning deferred to Pandas 02.**
     No output values hardcoded in markdown (all computed), so nothing drifts. (Aside: the most-liked
     opposing comment computes to "Put the Constitution in classrooms…", echoing the real corpus.)
   - ✅ **Data Cleaning with Pandas (Day 9) DONE** — `notebooks/codeAlongs/WRIT20833_Pandas_02_Cleaning_2026.ipynb`
     (built by `_build_pandas02.py`; all 16 code cells validated with pandas via `/opt/anaconda3/bin/python`).
     Ports F25's Pandas 02 (57 cells, literary dataset) trimmed to the **cleaning core**: diagnose
     (isnull/unique/duplicated) → clean text (`.str.strip/.replace`) → standardize categories
     (`.str.lower` + `.replace` synonym map) → handle missing (`fillna(median)` + ethics-of-filling) →
     `drop_duplicates`. **Continuity move:** cleans a *messy version of Day-8's same YouTube-comments
     table* (8 stance spellings, whitespace/newlines, 1 missing likes, 1 exact dup) back into the tidy
     table — 12→11 rows; stance collapses to oppose 5 / support 4 / neutral 2. Dropped F25's heavy
     multi-agg groupby, bubble charts, regex author-origin guessing. Sneak Preview → Day-10 "clean YOUR
     data" workshop + Week-3 VADER. All values computed (none asserted in prose).
   - ✅ **Sentiment Analysis with VADER (Days 11–12) DONE** — `notebooks/codeAlongs/WRIT20833_VADER_Sentiment_2026.ipynb`
     (built by `_build_vader.py`; all 16 code cells validated with vaderSentiment + pandas via
     `/opt/anaconda3/bin/python` — `!pip` magic skipped in validation). Ports F25's VADER notebook
     (32 cells) as one basics→deep-dive arc spanning both sessions. **Continuity:** scores the SAME
     cleaned comments table from Days 8–9 (comment + hand `stance`). **Payoff exercise** compares
     VADER's *tone* to the human *stance* and shows they're different axes — the lone computed mismatch
     is "Freedom of religion means freedom from it too" (stance=oppose, VADER=positive, because
     "freedom" scores positive regardless of side) = the Day-12 close-vs-distant-reading lecture made
     concrete + the WORKLOG-flagged human-vs-automated check. Keeps the "honest about borrowed code"
     convention (VADER = pip-installed model we run to *judge*). Dropped F25's TextBlob detour +
     multi-panel viz; kept one light bar (mean tone by stance) + a where-VADER-breaks sarcasm set.
     VADER is deterministic but no scores hardcoded in prose (all printed) → no drift.
   - ✅ **Topic Modeling with Gensim (Days 14–15) DONE** — `notebooks/codeAlongs/WRIT20833_Topic_Modeling_Gensim_2026.ipynb`
     (built by `_build_topicmodeling.py`; all 13 code cells validated with gensim 4.3.0 via
     `/opt/anaconda3/bin/python` — `!pip` skipped). **Dedups F25's THREE overlapping topic-modeling
     notebooks** (Gensim 41c + Part1 29c + Part2 24c) into one combined code-along spanning both
     sessions. **Aligns with HW4's simplified stack:** gensim only (NO nltk/WordNet, NO pyLDAvis) and
     reuses HW4's EXACT `split_into_words` + `stopwords` (copied verbatim into the builder) so
     code-along preprocessing == homework preprocessing. **Teaches on a clear 3-theme toy corpus**
     (sports/music/food, 15 short docs → LDA separates into nameable topics: food/music/sports), **then
     applies to the real single-issue Ten Commandments comments to show the limit** (one debate = no
     distinct subjects to find; Day-15 "limits" lesson + matches the HW4 single-issue caveat). Part 2 =
     the `num_topics` knob (2 vs 4) as an authored choice. Dominant-topic-per-doc framed honestly as a
     *mixture* (short docs → fuzzy assignment). **No topic words hardcoded in prose** (LDA stochastic/
     version-sensitive) — all printed, described qualitatively, like HW4's key.
   - ✅ **CODE-ALONG BATCH COMPLETE** (Strings, Pandas 01, Pandas 02, VADER, Topic Modeling). The three
     analytics notebooks share ONE corpus arc: Day 8 builds the comments table → Day 9 cleans it →
     Days 11–12 score sentiment → Days 14–15 (limits) — the same corpus HW3/HW4 use.
   - ✅ **Day-6 term-frequency code-along DONE** — `notebooks/codeAlongs/WRIT20833_Term_Frequency_2026.ipynb`
     (built by `_build_termfreq.py`; 11/11 cells validated; all prose word-claims verified against output).
     **Authored fresh** (no F25 standalone existed). Plain Python / pre-pandas to match HW2; reuses HW2's
     exact `split_into_words` + `stopwords` + `Counter` + `top_meaningful_words` idiom verbatim. Picks up
     Day 5's `count_words`/Counter thread; arc = raw counts (noise: `the`/`and` lead) → stopword filter
     (content surfaces: schools/religion/country/god/kids) → reusable function → **two-corpus contrast**
     (comments vs a Constitution-style passage: shall/congress/states/law) = a mini preview of HW2's
     "Whose Words Win?". Keeps the critical frame (counting is already interpretation) + borrowed-code
     note (Counter does what Day-5 `count_words` did by hand). Schedule Day-6 cell now links it.
   - ✅ **Schedule rewrite done** (see above). **Code-along coverage now complete** — every coding day in
     `COURSE_SCHEDULE_2026.md` links a real notebook.
   - ✅ **Schedule rewrite DONE** — `COURSE_SCHEDULE_2026.md` rebuilt in one pass: every coding cell now
     carries an explicit **mode** (Code-along / Lab / Workshop / Work session / Presentations) and links
     its real notebook (all 12 links verified to resolve). Non-coding days (7 Lab, 10 Workshop, 13/17–19
     Work session, 20 Presentations) read as intentional. Notes flag the three two-session notebooks
     (Days 3–4, 11–12, 14–15 each share one) and the one gap (Day 6 term frequency = no standalone
     code-along yet; taught via the HW2 notebook). Added a "Coding modes" legend.
5. ✅ **2026 syllabus authored** — `SYLLABUS_2026.md` (DRAFT for instructor review). Term Mon 7/6–Fri
   7/31, M–F 2 hrs/day = 20 sessions (calendar verified; no weekday holidays). Maps the
   `PROPOSED_4WEEK_SCHEDULE` onto real dates with due dates for HW1–4 + capstone, **3 self-reflections**
   (R1 due Wed 7/8 · R2 midterm due Mon 7/20 · R3 final self-eval due Fri 7/31), and **4 weekly D2L
   threaded discussions** (post Wed / replies Fri; note says drop D4 to hit the 3-discussion minimum).
   Ungrading evaluation section, AI-use policy (explain-don't-avoid), Walsh-independence, sensitive-topic
   note. Placeholders in `[...]` for instructor name/contact/office hours + TCU policy boilerplate.
6. **Stylometry decisions** — fixed sample corpus vs. student-generated; essay weight; ethics emphasis.
7. **Topic-modeling install cell — ✅ VERIFIED ON py3.12 PROXY (2026-06-21); one live Colab click remaining.**
   The Day-14 code-along cell is `!pip install -q gensim`; HW4 is `!pip install -q gensim vaderSentiment`
   (lean — no nltk, no pinned deps, no kernel restart, simpler than F25's cell). Tested in a **clean
   Python-3.12 venv** (closest local proxy to a mid-2026 Colab image): bare install resolved
   **gensim 4.4.0 · numpy 2.4.6 · scipy 1.18.0** with no errors; the exact import chain
   (`from gensim import corpora` / `from gensim.models import LdaModel` / VADER) imports clean; and a full
   LDA smoke test passed — `Dictionary` + `doc2bow` (incl. the **empty-bag `[]` edge** HW4/Day-14 A3
   teaches) + `LdaModel(num_topics, random_state=42, passes=10)` + `show_topic` + `get_document_topics`.
   **Key result:** current gensim (4.4.0) supports **numpy 2.x + scipy ≥1.13 natively**, so the old
   `scipy.linalg.triu` / numpy-2 breakage class is gone — and since Colab already ships numpy 2.x, the
   bare install should pull a compatible gensim with **no downgrade and no "Restart runtime" prompt**. Also
   confirmed the *older* end of the range works (anaconda: py3.11 · numpy 1.26 · scipy 1.11 · gensim 4.3.0
   imports fine), bracketing whatever Colab lands on in July 2026. **Residual = one 60-sec live click:**
   open the notebook in Colab once before Day 14, run the install cell, confirm no red restart banner.
8. **A4 / HW1 note:** A4 intentionally demonstrates a TypeError via try/except — by design.
9. **Lecture audit — ✅ FULLY CLOSED (2026-06-18).** ML0–7 mapped cleanly; ML10–12 (GitHub/HTML/CSS) cut;
   **ML2 "Sacred Boundaries" CUT (2026-06-15)**; **ML9 "Going Public" AUTHORED + homed at Day 17
   (2026-06-18)**; **ML8 "Code as Rhetoric" HARVESTED into ML1 + ML9, no deck (2026-06-18)**. Nothing left
   to decide or build on the lecture track. (Authoring/harvest details in the 2026-06-18 session summary up
   top + `LECTURE_SOURCE_NOTES.md`.)
   - **ML2 decision (instructor, 2026-06-15): CUT.** Rationale that tipped it: now that **ML6 Data
     Archaeology (Day 8)** is built, it fully carries ML2's privacy/collection-ethics core
     (hear-don't-extract, robots.txt, attribution) — ML2 became redundant. Its one other durable idea
     (the noumena limit on religious conviction as an interiority distant reading can't reach) is already
     in **ML0**. Plus the "sacred/taboo" metaphor collided with the *literally* sacred corpus, and Day 1
     already front-loads ML0+ML1. **Day 2 is now a no-mini-lecture day** (dive into Strings).
   - **Propagated:** removed the ML2 dashboard card (`build_index.py`) + regenerated `docs/index.html`;
     Day-2 lecture cell → "—" in `COURSE_SCHEDULE_2026.md` + `SYLLABUS_2026.md` (+ both lecture-notes
     updated); `CONCEPTUAL_FRAMEWORK_2026.md` §6 dial marked decided; `LECTURE_SOURCE_NOTES.md` updated.
     **Not authored** (no ml2.md) — the cut means zero build. `lecture-2-boundaries` stays unmined in F25.
10. **TCU Core Curriculum — CSV vetting (context + a task).** The course **carries Citizenship & Social
    Values (CSV)** credit. Vetting docs are in `reference/`: `reference/TCU-Core-Curriculum-outcomes-1.pdf`
    (current outcomes matrix) + `reference/Citizenship-and-Social-Values-5-5-10.doc` (older HMVV form). Current CSV
    outcome: *"examine the knowledge, skills, values, or motivation needed to participate or lead within
    diverse communities."* The course meets it directly (a contested public-policy debate = a diverse
    community in disagreement; the data-driven-opinion capstone + discussions + reflections are the
    evidence). Full mapping + the course's adjacent resonance (Humanities, Written Comm 2, Cultural
    Awareness) in `CONCEPTUAL_FRAMEWORK_2026.md` §7; syllabus now names the CSV + HUM designations.
    **✅ DONE:** the **student-work examples** (3 per outcome) are drafted in
    `planning/CSV_HUM_WORK_EXAMPLES.md` — instructor trims to the vetting form's field limits.

11. **TCU syllabus — ✅ ALIGNED TO AddRan + F25 (2026-06-11, second pass).** Reviewed the AddRan syllabus
    docs in `/Users/curtrode/Code/AddRan/syllabus-checker/source_files` (AddRan Simplified Template,
    Fall-2026 review instructions, **the F25 WRIT 20833 syllabus co-authored with Lucas**). Big unblock:
    AddRan handles University-policy boilerplate via the **Student Resources & Policy Information QR/link**,
    not pasting — so the old `[paste …]` placeholders are **gone**. Revised `SYLLABUS_2026.md`: added the
    QR block (cte.tcu.edu image) + a Note-for-students; a **Land Acknowledgment**; the **University-Absence**
    + **Medical-Privacy** statements (AddRan text) under *Attendance & Engagement*; course **Recording** +
    **Academic Conduct** statements; **CSV outcome-mapping** in the assignments table; dropped the TCU-Online
    getting-started + the long University-Policies paste list. Crosswalk `planning/SYLLABUS_COMPLIANCE.md`
    updated. F25 syllabus also confirms this course already ran **ungrading** + no-attendance-deduction.
    *(Earlier first-pass verification against the standard TCU checklist remains below for history.)*

    **Syllabus fill + Word export — partial, 2026-06-12.** Filled the confirmable instructor/registrar
    fields into `SYLLABUS_2026.md`: **Curt Rode · 3 credits · Lecture · Office N/A—online · Response time
    (24 hrs weekdays) · Preferred contact (email via TCU Online)**. **Generated the AddRan Word export**
    via `pandoc … -f gfm` → `WRIT20833-[section]_Summer2026_Rode.docx` (38.6 KB; 9 tables, QR image
    embedded, AddRan section order preserved). The .docx is a **working draft edited in Word** and is
    **`.gitignore`d** (`WRIT20833-*_Summer2026_Rode.docx`) — `SYLLABUS_2026.md` stays the source of truth.
    **✅ SUPERSEDED — all of this is now done (PR #18, see the "Latest session" summary up top):** every
    `[...]` field is filled (section 020, meeting time, contact, Zoom, office/hours, catalog desc,
    CSV/HUM confirmed, Grading Concerns + submissions note authored, loaner/supplementary dropped). The
    only remaining task is instructor-side **in Word**: mirror the markdown-only edits into the .docx and
    run the accessibility checker (table headers + image alt text).

    **HUM core added (2026-06-12).** The course now carries **two** Core designations — CSV **and
    Humanities (HUM)**. Verified the official HUM outcome against `reference/TCU-Core-Curriculum-outcomes-1.pdf`:
    *"Use humanistic modes of inquiry to analyze human experiences and expressions across space and time."*
    Wove HUM in beside CSV in `SYLLABUS_2026.md` (Course-Description core subsection → now "CSV and HUM"
    with a paragraph each; Learning-Outcomes core block → two bullets; assignments table → column is now
    "Core (CSV · HUM)" with per-row codes + updated mapping note). Updated `CONCEPTUAL_FRAMEWORK_2026.md`
    §7 (HUM moved from "adjacent resonance" to a **claimed** designation) and the README core-credit line.
    **HUM evidence claimed:** the HW analyses + capstone; CSV evidence stays discussions + reflections +
    capstone. The Word docx (020) is the instructor's — paste the HUM blocks in by hand (md ≠ docx now).

    **TCU syllabus compliance — ✅ VERIFIED COMPLETE for course-specific content (2026-06-11).** Did a
    full item-by-item gap-check of `SYLLABUS_2026.md` against the **actual** TCU checklist PDF
    (`reference/TCU-Syllabus-Template-checklist-FINAL-9-2024.pdf`): every required section is present and
    correctly scaffolded. Crosswalk captured in **`planning/SYLLABUS_COMPLIANCE.md`** (each checklist item →
    where met → ✅ done / 🟦 instructor field / 📋 paste official text). Closed the one authorable gap by
    adding a **"Course Assignments & Final Grade" table** (checklist wants an assignments/points table;
    ours maps components to the ungrading 3-point scale + role, no points). Fixed moved template-path refs
    (`Syllabus-Template-Online.docx` → `reference/…`). **Remaining is instructor/registrar-only:** the
    `[...]` fields (name, contact, section, credit hours, component type, Zoom, response time, office
    hours) + 📋 official boilerplate pasted verbatim. The detailed gap notes below are **superseded by the
    crosswalk doc** (kept for history).
    `SYLLABUS_2026.md` was restructured to the **TCU Online Syllabus
    Template**: full Course Information block, Course Description + CSV core, Learning Outcomes (+ CSV),
    Course Materials, Teaching Philosophy, Course Policies & Requirements (Assignments, the 3 reflections
    + 4 discussions, **Grading**, Grading Concerns, Late Work, Participation/Attendance, Class Norms &
    Netiquette + course-specific sensitive-corpus note, **AI policy split code-vs-writing**, Tech/Email/
    Recording, Academic Misconduct), the 20-session schedule (Date·Lecture·Coding·Due) + skills map, the
    TCU Online section, and University Policies. **Grading model settled & written:** ungrading · per-piece
    **3/2/1** (exceeds/meets/not-yet) · pattern → whole-letter floor · **+/- set in the Reflection-3 final
    self-evaluation** · **TCU undergraduate +/- scale** (D's exist; F < 60). **Still to do (mostly
    instructor/registrar):** confirm **credit hours** + **course component type**; **paste official TCU
    boilerplate** (Title IX, Religious Observations, Disability/Access, Medical-doc statement, Audio
    Recording, Emergency Response, TCU Online section, Student Resources link+QR, Netiquette, Email,
    Recording) from `Syllabus-Template-Online.docx` — *not fabricated*, marked `[paste …]`; fill
    instructor `[...]` fields; confirm catalog description + exact CSV outcome wording.
    Earlier gap-analysis context (now resolved): template + checklist in `reference/`
    (`reference/2024-25-Syllabus-Template-Final-9-2024-1.docx`, `reference/TCU-Syllabus-Template-checklist-FINAL-9-2024.pdf`,
    `reference/Syllabus-Template-Online.docx`). **Already present:** course title, term, meeting
    days/time + online-synchronous, instructor/office-hours/email placeholders, Zoom placeholder, course
    description, prerequisites (none), course learning outcomes, **CSV core outcome** (just added),
    technology/AI policy, course description; the **course schedule** matches the template grid
    (Date·Topic·Assigned·Due ≈ our Date·Lecture·Coding·Due). **Still required / missing:** course
    component type; **number of credits** (the actual number); **response time**; office location (or
    "N/A — online"); **Final Evaluative Exercise** named (the capstone presentations, Fri 7/31, with
    details); **Student Resources & Policy Information** (TCU standard link + QR); **Required Materials**
    as its own section (Colab/D2L/Google account; note any cost); **Grading scale + a Final-Grade table**
    and **how ungrading maps to TCU's required letter grade** (the one real decision — see below);
    explicit **Late Work** policy (+ link Student Absences); **Participation/Engagement/Attendance** tied
    to the grade; **the medical-documentation compliance statement** (faculty will NOT seek medical
    docs; direct students to the Dean of Students Office). **Decision needed:** ungrading still must
    yield a TCU letter grade — settle the mapping (labor/completion contract vs. final self-evaluation
    proposes the grade vs. minimum-thresholds), then the grading section + grad grade scale can be
    written. Most items are mechanical/placeholder; the grading reconciliation is the instructor's call.
   **Use the ONLINE template** (`Syllabus-Template-Online.docx`) — it's the operative one. Beyond the
   checklist it mandates standard TCU **boilerplate sections**: Class Norms & Netiquette · Technology
   Policies · Email · Recording of Class Sessions · Academic Misconduct · TCU Online (LMS) getting-
   started/help/notifications/success-tools · Anti-Discrimination & Title IX · Religious Observations &
   Holidays · Audio Recording Notification · Emergency Response · Grading Concerns. **Do NOT fabricate
   this official policy text** — structure the sections and insert `[paste TCU standard text from
   Syllabus-Template-Online.docx]` placeholders; write only the *course-specific* content. Online
   template also requires that any tables/images be **accessible**.

## Answer keys live in a PRIVATE companion repo (2026-06-11)
This course repo is **student-facing** (Colab badges + the HW data-loader resolve against
`raw.githubusercontent.com/TCU-DCDA/WRIT20833_2026/main/...`), so answer keys must **never** be committed
here. They — plus the **solution-bearing** homework builders (`_build_hw2/3/4.py`, which generate both the
student notebook and the key) — now live in the private repo **`TCU-DCDA/WRIT20833_2026_keys`** (HW1's key
is hand-authored, no builder). This repo `.gitignore`s `*_ANSWER_KEY.ipynb` and
`notebooks/homework/_build_hw*.py` so they can't return by accident. The keys were also **scrubbed from
this repo's git history** (BFG, 2026-06-11) and `main` + the PR branch were force-pushed (old tip
`2424d13` → `bb6b2fb`); local clones must re-sync (`git fetch && git reset --hard origin/<branch>`).
**To edit a key:** do it in the keys repo, regenerate, and copy the regenerated *student* notebook back
here. (Residual: the old commit SHAs may stay cached server-side on a private repo until GitHub GC.)

## Working across two machines (solo dev)
Sole maintainer, two machines. Normally just `git pull` / `git push` as usual — BUT after a **history
rewrite** (like the BFG key scrub above), the other machine's clone has diverged from the rewritten
remote, so a plain `pull` would try to merge the old history back (and could reintroduce scrubbed files).
After any force-push, re-sync the **other** machine with a hard reset instead of a pull:
```
git fetch origin --prune
git checkout main && git reset --hard origin/main
git checkout <feature-branch> && git reset --hard origin/<feature-branch>   # if present locally
git reflog expire --expire=now --all && git gc --prune=now --aggressive      # drop old objects
git log --all --oneline -- '*_ANSWER_KEY.ipynb' 'notebooks/homework/_build_hw*.py'   # expect empty
```
Stash/commit any uncommitted work first (`reset --hard` discards it). **Do not push from the stale
machine before resetting** — it would force the old history (and the keys) back onto the remote. The
private keys repo (`WRIT20833_2026_keys`) can be cloned on both machines independently.

## Course site design system — "Reading Room" (2026-06-11, in progress)
First pass at a **unique visual identity** for the course's HTML (moving off the generic default look).
Lives in **`site_theme.py`** (`THEME_CSS` design tokens + a `PAGE()` wrapper) — a shared, reusable theme
that generated pages **inline** (kept self-contained so pages survive being opened from disk / Colab /
D2L / email). Direction: *coding meets culture* → an editorial "reading room": warm **parchment** paper,
deep muted **greens** (week tints deepen `#3a6b54`→`#1e3b2f` across the term), **serif** headings +
**monospace** data accents + sans body, **green** links (not default blue), one **clay** warm accent,
hairline rules instead of drop-shadow cards, and a restrained earthy mode-pill palette (no rainbow).
**Still a draft for instructor taste** — palette/type are tokens, easy to retune.
**Accessibility note (2026-06-15):** the muted tokens were darkened to clear WCAG AA and all UI text has a
12px floor (see the "Latest session" summary up top); `site_theme.assert_accessible()` now guards both at
build time, so if you retune the palette/type, keep `--muted/--faint/--clay` ≥ 4.5:1 on paper/surface and
fonts ≥ 12px or the build will fail.

**Site layout (Pages-friendly, F25 parity) — 2026-06-11.** The published site lives in **`docs/`** (so it
can be served by GitHub Pages → *Deploy from branch* → `main` /`docs`). The old instructor process-docs
were moved out of `docs/` to **`planning/`** (WORKLOG, PORT_ASSESSMENT, PROPOSED_4WEEK_SCHEDULE,
CONCEPTUAL_FRAMEWORK, ACKNOWLEDGMENTS, SYLLABUS_COMPLIANCE). Site pages:
- `docs/index.html` — landing **dashboard** (built by `build_index.py`), modeled on last year's site IA
  with a **left sidebar nav** (F25 parity) + sectioned card grids: Start here · Code-alongs (**split by
  week**) · Homework · Capstone & stylometry · Lectures (placeholders) · Resources.
- `docs/schedule.html` — the schedule (built by `build_schedule_html.py`); same left sidebar with week
  anchors + a Dashboard back-link.
Sidebar/shell are shared helpers in `site_theme.py` (`sidebar()`, `shell()`, `PAGE(..., wrap=False)`);
collapses to a top bar under 860px.

**Open design questions (revisit later):**
- **Sidebar icons** — F25 used lucide icons next to each nav item; ours is text-only. Add inline-SVG
  icons (keep self-contained — no external icon CDN) or leave text-only?
- **Nav behavior** — ours is plain anchor scroll-to-section; F25 used JS to *filter* the dashboard to
  one category at a time. Keep scroll, or add the filter?
- **Themed `docs/syllabus.html`** — dashboard currently links the syllabus as raw markdown on GitHub;
  build a themed HTML syllabus page (a `build_syllabus.py` from `SYLLABUS_2026.md`).
- **Tidy root** — optionally move `site_theme.py` + `build_*.py` into a `tools/` folder.
- **Theme retune** — palette/type are tokens; revisit greens/serif once lived-with.
Because Pages serves only `/docs`, links to things **outside** docs/ are absolute: notebooks → **Colab**
(`colab.research.google.com/github/.../blob/main/...`), repo files (syllabus, stylometry handout) →
**GitHub blob**. Intra-site links (index→schedule) stay relative. Generators (`site_theme.py`,
`build_index.py`, `build_schedule_html.py`) sit at repo root and write into `docs/`.

**CSS — now an external shared stylesheet (changed 2026-06-12).** Was inlined per page; the two site
pages always travel together in `/docs`, so the theme moved to a single **`docs/styles.css`** (written by
`site_theme.write_stylesheet`, linked via a relative `<link>`). `THEME_CSS` in `site_theme.py` stays the
one source of truth; both generators emit `styles.css` on every build. Pages dropped ~9KB each
(`index.html` 20.6KB→11.5KB). Escape hatch kept for single-file portability: `PAGE(..., css_href=None)`
inlines `THEME_CSS` for a fully self-contained page (to email / drop in D2L / open from disk detached).
Per-week tints are unaffected — they're inline `style="--wk:…"` on each `.week` (body content, not theme).
**To publish:** make the repo public, then *Settings → Pages → Deploy from branch → `main` / `docs`*.
Colab/badge links resolve only once public.

## Useful facts for a fresh session
- The F25 source repo is **public**; if it's out of session scope, you can still read files via
  `raw.githubusercontent.com/TCU-DCDA/WRIT20833_2025/main/<path>` or `git clone` it (github.com is
  reachable). The Pages site `tcu-dcda.github.io` is NOT reachable from the sandbox allowlist.
- F25 full asset inventory is in that repo's `README.md`.
- Code-along batch + Day-6 term frequency shipped on PR #2 (`claude/port-strings-codealong`).
