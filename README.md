# WRIT 20833 — Intro to Coding in the Humanities (2026)
### "When Coding Meets Culture: Developing Data-Driven Opinions"

A **lower-division undergraduate, 4-week, online-synchronous** offering of WRIT 20833 at TCU — **Mon Jul 6 – Fri Jul 31,
2026**, Monday–Friday, 2 hrs/day (20 sessions). Students with **no prior coding experience** learn just
enough Python to ask humanistic questions of real text (term frequency → sentiment → topic modeling),
and to argue from what they find — while staying honest about what computation reveals and flattens.

This repo is a **port** of the mature 16-week Fall 2025 course (`TCU-DCDA/WRIT20833_2025`), re-paced and
trimmed to a 4-week cultural-analytics arc (the web-dev/portfolio half is dropped — it overlaps MALA
60970). See `planning/PORT_ASSESSMENT_2026.md` for the rationale.

The course carries TCU **Citizenship & Social Values (CSV)** core-curriculum credit — it trains
evidence-based civic participation around a real public-policy debate. (Vetting: `reference/TCU-Core-Curriculum-outcomes-1.pdf`
+ `reference/Citizenship-and-Social-Values-5-5-10.doc`; how the course delivers it: `planning/CONCEPTUAL_FRAMEWORK_2026.md` §7.)

> **Status: in active development (draft).** The homework spine (HW1–HW4) and **all code-along notebooks**
> (one per coding day) are complete and validated; the **syllabus** is drafted and aligned to the AddRan
> template; and a **course website** (`docs/`) is up. Remaining: instructor/registrar `[...]` fields, the
> capstone sheet, lecture pages, and the student-facing fold-ins of the conceptual framework. See
> `planning/WORKLOG.md`.

---

## Start here
| Document | What it is |
|---|---|
| **`docs/index.html`** | The **course website** — a left-nav dashboard that launches the schedule, code-alongs (→ Colab), homework, capstone, lectures, and resources. Built by `build_index.py` + `site_theme.py`; publishes via GitHub Pages (`main` / `docs`). |
| **`SYLLABUS_2026.md`** | The course as students meet it — outcomes, ungrading policy, schedule, AI-use policy, the 3 reflections + 4 discussions. *(DRAFT, aligned to the AddRan template; has `[...]` instructor placeholders + a final Word export.)* |
| **`COURSE_SCHEDULE_2026.md`** | Day-at-a-glance grid: **Date · Lecture · Coding · Due** across the 20 sessions (rendered as `docs/schedule.html`). |
| **`planning/CONCEPTUAL_FRAMEWORK_2026.md`** | The course's intellectual through-line — *why* beneath the code. Read this to understand what the course is *about*. |
| **`planning/WORKLOG.md`** | Running session handoff + decision log. Read first to resume work with zero ramp-up. |
| **`planning/PORT_ASSESSMENT_2026.md`** | The 2026 readiness/port analysis vs. the F25 source. |
| **`planning/PROPOSED_4WEEK_SCHEDULE.md`** | The design draft behind the schedule (F25-asset mappings, scope rationale). |
| **`planning/ACKNOWLEDGMENTS.md`** | Credits Melanie Walsh's *Intro to Cultural Analytics* as inspiration/model (the course is otherwise self-contained — "Walsh-independent"). |

## Course materials
- **`notebooks/homework/`** — **HW1** (foundations) · **HW2** (term frequency) · **HW3** (sentiment) ·
  **HW4** (topic modeling + integration), as student notebooks. *Answer keys and the solution-bearing
  `_build_hw*.py` generators live in the **private** instructor repo `TCU-DCDA/WRIT20833_2026_keys`, not
  in this student-facing repo.*
- **`notebooks/codeAlongs/`** — one notebook per coding day: Variables/Data Types · Strings · Lists/Loops/
  Conditionals · Dictionaries/Functions · Term Frequency · Found Data & Pandas · Data Cleaning · VADER
  Sentiment · Topic Modeling (see `COURSE_SCHEDULE_2026.md` for the day-by-day mapping).
- **`notebooks/data/`** — the corpora (123 real YouTube comments on the TX Ten Commandments law; the U.S.
  Constitution) + a `README.md`. Reused across HW2–HW4 and the capstone.
- **`materials/stylometry/`** — "Reading for the Seams" close-reading exercise + notebook + exemplar.
- **`materials/images/`** — the **noumena → wisdom** epistemological-spine graphic + its teaching notes.
- **`materials/Day1_Framing_Noumena_to_Wisdom.md`** — a drafted Day-1 framing passage.

## Repository layout
- **`docs/`** — the published **course site** (GitHub Pages from `/docs`): `index.html` dashboard + `schedule.html`.
- **`notebooks/`** — `codeAlongs/` (one per coding day), `homework/` (HW1–4 student notebooks), `data/` (corpora).
- **`materials/`** — the stylometry exercise, images, and the Day-1 framing passage.
- **`reference/`** — TCU/AddRan syllabus templates + core-curriculum vetting (source documents, not course content).
- **`planning/`** — instructor process docs (WORKLOG, conceptual framework, port assessment, syllabus crosswalk…).
- **Root** — this README, `SYLLABUS_2026.md`, `COURSE_SCHEDULE_2026.md`, and the site generators (`site_theme.py`, `build_index.py`, `build_schedule_html.py`).
- *Answer keys + the solution-bearing `_build_hw*.py` generators live in the **private** `TCU-DCDA/WRIT20833_2026_keys`.*

## The idea in one paragraph
The course teaches three computational methods, but its real subject is one humanistic problem: **how do
we hear human voices at a scale no person could read by hand, without flattening the humans out of
view?** Every homework stages the same move — run a computation, then ask *what did this flatten, who
chose this, can you trust it?* The full architecture (the noumena→wisdom spine; "hear the human at
scale"; the quarrel; voice-through-difficulty in the age of AI; the moral stakes) is in
`planning/CONCEPTUAL_FRAMEWORK_2026.md`. Assessment is **ungrading**: earned insight over clean code.

## Conventions (for anyone authoring materials)
- **Walsh-independent** — required work never depends on an outside textbook.
- **Ungrading** — evaluate engagement/reflection/labor, not correctness; answer keys are references, not
  rubrics; avoid grade/points framing.
- **Honest about borrowed code** — setup cells are "plumbing" (run, don't read every line); common
  routines are prefab you'd normally borrow (build once to *read and judge* a borrowed/AI version).
- **House style** — homeworks share a Part A/B/C + Weekly Experiments + Submit structure; code-alongs use
  warm cultural examples + concept→code→"your turn" + Playground.

*Full detail and rationale: `planning/CONCEPTUAL_FRAMEWORK_2026.md` and `planning/WORKLOG.md`.*
