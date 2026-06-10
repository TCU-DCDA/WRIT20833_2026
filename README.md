# WRIT 20833 — Intro to Coding in the Humanities (2026)
### "When Coding Meets Culture: Developing Data-Driven Opinions"

A **graduate, 4-week, online-synchronous** offering of WRIT 20833 at TCU — **Mon Jul 6 – Fri Jul 31,
2026**, Monday–Friday, 2 hrs/day (20 sessions). Students with **no prior coding experience** learn just
enough Python to ask humanistic questions of real text (term frequency → sentiment → topic modeling),
and to argue from what they find — while staying honest about what computation reveals and flattens.

This repo is a **port** of the mature 16-week Fall 2025 course (`TCU-DCDA/WRIT20833_2025`), re-paced and
trimmed to a 4-week cultural-analytics arc (the web-dev/portfolio half is dropped — it overlaps MALA
60970). See `PORT_ASSESSMENT_2026.md` for the rationale.

> **Status: in active development (draft).** The homework spine (HW1–HW4) is complete and validated; the
> syllabus, schedule, and conceptual framework are drafted. Code-along porting, the capstone sheet, and
> the student-facing fold-ins of the conceptual framework are in progress. See `WORKLOG.md`.

---

## Start here
| Document | What it is |
|---|---|
| **`SYLLABUS_2026.md`** | The course as students meet it — outcomes, ungrading policy, schedule, AI-use policy, the 3 reflections + 4 discussions. *(DRAFT; has `[...]` instructor placeholders.)* |
| **`COURSE_SCHEDULE_2026.md`** | Day-at-a-glance grid: **Date · Lecture · Coding · Due** across the 20 sessions. |
| **`CONCEPTUAL_FRAMEWORK_2026.md`** | The course's intellectual through-line — *why* beneath the code. Read this to understand what the course is *about*. |
| **`WORKLOG.md`** | Running session handoff + decision log. Read first to resume work with zero ramp-up. |
| **`PORT_ASSESSMENT_2026.md`** | The 2026 readiness/port analysis vs. the F25 source. |
| **`PROPOSED_4WEEK_SCHEDULE.md`** | The design draft behind the schedule (F25-asset mappings, scope rationale). |
| **`ACKNOWLEDGMENTS.md`** | Credits Melanie Walsh's *Intro to Cultural Analytics* as inspiration/model (the course is otherwise self-contained — "Walsh-independent"). |

## Course materials
- **`notebooks/homework/`** — **HW1** (foundations) · **HW2** (term frequency) · **HW3** (sentiment) ·
  **HW4** (topic modeling + integration), each with an `_ANSWER_KEY` and a `_build_*.py` generator.
  *All answer keys validated to run top-to-bottom.*
- **`notebooks/codeAlongs/`** — Variables/Data Types · Lists/Loops/Conditionals · Dictionaries/Functions
  *(more being ported from F25 — see WORKLOG thread #4).*
- **`notebooks/data/`** — the corpora (123 real YouTube comments on the TX Ten Commandments law; the U.S.
  Constitution) + a `README.md`. Reused across HW2–HW4 and the capstone.
- **`materials/stylometry/`** — "Reading for the Seams" close-reading exercise + notebook + exemplar.
- **`materials/images/`** — the **noumena → wisdom** epistemological-spine graphic + its teaching notes.
- **`materials/Day1_Framing_Noumena_to_Wisdom.md`** — a drafted Day-1 framing passage.

## The idea in one paragraph
The course teaches three computational methods, but its real subject is one humanistic problem: **how do
we hear human voices at a scale no person could read by hand, without flattening the humans out of
view?** Every homework stages the same move — run a computation, then ask *what did this flatten, who
chose this, can you trust it?* The full architecture (the noumena→wisdom spine; "hear the human at
scale"; the quarrel; voice-through-difficulty in the age of AI; the moral stakes) is in
`CONCEPTUAL_FRAMEWORK_2026.md`. Assessment is **ungrading**: earned insight over clean code.

## Conventions (for anyone authoring materials)
- **Walsh-independent** — required work never depends on an outside textbook.
- **Ungrading** — evaluate engagement/reflection/labor, not correctness; answer keys are references, not
  rubrics; avoid grade/points framing.
- **Honest about borrowed code** — setup cells are "plumbing" (run, don't read every line); common
  routines are prefab you'd normally borrow (build once to *read and judge* a borrowed/AI version).
- **House style** — homeworks share a Part A/B/C + Weekly Experiments + Submit structure; code-alongs use
  warm cultural examples + concept→code→"your turn" + Playground.

*Full detail and rationale: `CONCEPTUAL_FRAMEWORK_2026.md` and `WORKLOG.md`.*
