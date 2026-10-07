# External review brief — WRIT 20833, first half (Days 1–12)

**For:** an outside reviewer (Codex) checking that the course materials agree with each other.
**Review this commit:** `<fill in at hand-off>` on `main` of `TCU-DCDA/WRIT20833_2026`. Please don't
review a later commit; your line numbers need to match what the instructor sees.

## What this course is

WRIT 20833, "When Coding Meets Culture" (TCU, Fall 2026): an 8-week, in-person intro to Python for
humanities students, MWF, Oct 19 – Dec 18. It was re-paced from a 16-week version, so day numbers and
"next week" references are the most likely things to be wrong. Students have no prior coding.

## The job

Find places where the materials **disagree with each other** or **with the facts they cite**. Report
findings; **do not edit anything.** Most files here are generated, and fixes go through generators the
instructor runs (see `CLAUDE.md` §1). A direct edit to `docs/` or a homework `.ipynb` creates drift.

## In scope

| Material | Files |
|---|---|
| Syllabus | `SYLLABUS_2026.md` |
| Schedule | `COURSE_SCHEDULE_2026.md`, Days 1–12 (Weeks 1–4) |
| Code-alongs, Days 1–11 | `notebooks/codeAlongs/`: Variables_DataTypes, String_Methods, Lists_Loops_Conditionals, Dictionaries_Functions, Term_Frequency, Pandas_01_Found_Data, Pandas_02_Cleaning. The `_complete` copies are the unlinked instructor versions of the type-along notebooks; check that they match their student copies apart from the blanks. |
| Homework | `notebooks/homework/WRIT20833_HW1_2026.ipynb`, `WRIT20833_HW2_2026.ipynb` |
| Lecture pages | `materials/lectures/ml0, ml1, ml3, ml4, ml5, ml6.md` (Days 1, 3, 4, 8, 10). The built pages in `docs/lectures/` come from these. |
| Day 8 lab | `materials/stylometry/` (see the note under "Known") |
| Corpora | `notebooks/data/README.md` against `tc_youtube_comments.txt` and `us_constitution.txt` |
| Course site | `docs/index.html`, `docs/schedule.html` (generated; check what students see, report against the source) |
| *Optional:* Code Guide | The tutor's instructions and assignment blocks in the private `TCU-DCDA/WRIT20833-chatbot`, if you were given access: does the tutor describe the assignments, days and rules the way the course materials do? |

## Sources of truth

When two files disagree, these win:
- **Day numbers, dates, what happens on which day:** `COURSE_SCHEDULE_2026.md`.
- **Corpus facts** (counts, what a file contains): the data files themselves; `notebooks/data/README.md` describes them and can be wrong.
- **Policies** (grading, AI use, late work): `SYLLABUS_2026.md`.

## What to check

1. **Cross-references.** Every "Day N," "Week N," "next week," "last week," "in HW1," "the tools from…," and "you built/used…" points at the right thing, per the schedule.
2. **Stated facts.** Counts ("123 comments," "appears 25 times"), "top words," and "the first comment says…" hold when the code actually runs on the real files.
3. **Order of teaching.** Nothing uses a concept before the day it is taught, unless it is labeled as setup "plumbing" students run without reading.
4. **Prep lists.** Each homework's *Prepare* list names materials that exist, by their real titles, and that come before it.
5. **Structure and voice** (lighter touch). Homework: Part A/B/C + Weekly Experiments + Submit checklist. Code-alongs: warm cultural example → concept → code → "your turn" → Playground → "Sneak Preview." No points or grade framing: the course uses ungrading. Required work never depends on an outside textbook.

## Settled decisions: flag only if the materials contradict them

- Day 6 is a foundations recap where students **start HW1 in class**; HW1 is due Mon 11/2.
- `Lists_Loops_Conditionals` is ordered Conditionals → Lists → Loops and split across Days 3–4 at a "🛑 Day 3 stops here" marker.
- Term Frequency introduces `split_into_words` and the long `stopwords` list on Day 7; `Counter` first appears at the end of Day 5.
- List comprehensions are taught once, in Term Frequency.
- Day 9 is "HW2 (+ optional C2: text of your own)"; students collect their own data on Day 12.
- Ungrading, the "plumbing" framing of setup cells, and building a routine by hand before using the prefab or AI-written version are deliberate.
- Lecture slide design (title bar, callouts, images) was settled 2026-10-07; it is not in scope.

## Known: don't spend time on these

- **HW3 and HW4 raise six errors when run unfilled** (`KeyError`/`NameError`): each comes from a cell that depends on a column or variable the student creates in an earlier exercise. Expected. Both are second-half homework anyway.
- **The intentional `TypeError`** in Variables_DataTypes ("read the error message carefully").
- **Second half (Days 13–24):** the four lecture framings with no built material (Days 13, 14, 15, 18), the capstone sheet's placeholders, HW3, HW4, VADER, Topic Modeling. A second review covers these in November.
- **`us_constitution.txt` is the 1787 text without the amendments.** Found and reframed 2026-10-07 (the text was kept): HW2, the data README, Term Frequency's Sneak Preview, and the Code Guide's HW2 notes now call it the Constitution as signed in 1787, and HW2 B3 asks students why *religion* is absent (the First Amendment, 1791). Do report any place that still calls it the full or entire Constitution.
- **Stylometry materials:** `<instructor: fixed / excluded — fill in at hand-off>`.
- D2L (TCU Online) and the Word syllabus are outside this repository.

## Verification already done (2026-10-07)

All seven code-along builders reproduce the committed notebooks byte for byte. Every code-along, the
stylometry notebook, HW1 and HW2 execute top to bottom with no errors except the intentional one. A
simulated HW2 solution confirms 123 comments; "commandments" 25 and "constitution" 8 among the comments'
meaningful words; and that "10" and "ten" rank in the comments' top 5. HW1's and HW2's day references
match the schedule.

To execute a notebook here: `jupyter` is not installed; `exec` the code cells in order in one namespace,
skipping `!pip` lines, with `matplotlib.use("Agg")`.

## How to report

One list, most serious first. For each finding:
- **Where:** file and line (or notebook cell number).
- **What it says now**, quoted.
- **What it should say or match**, and the source that says so.
- **Severity:** *blocks students* (wrong instruction, broken code, false fact) · *confusing* (a stale reference a student would trip on) · *polish*.
- **Confidence:** checked by running code, or by reading.

Group repeats: one finding for "Day 7 should be Day 8" in five places, with all five locations listed.
Say when you're unsure. A short "checked and found nothing" list of what you covered also helps.
