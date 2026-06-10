# WORKLOG — WRIT 20833 2026 port (session handoff)

**Branch:** `claude/tender-thompson-13o19u` · **Last updated:** 2026-06-10

A running handoff so any new session (VS Code, web, or CLI) can resume with zero ramp-up.
Read this first, then `PORT_ASSESSMENT_2026.md` (context) and `PROPOSED_4WEEK_SCHEDULE.md`
(the plan + open decisions).

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
- **Assignment renumbering (2026):** HW1 = foundations · HW2 = term freq · HW3 = freq+sentiment
  · HW4 = topic modeling+integration · Capstone. (F25 map: HW1=F25 HW2, HW2=F25 HW1,
  HW3=F25 HW4-1, HW4=F25 HW4-2.)
- Stylometry exercise placement: **close-reading seed on Day 7**, computational half +
  synthesis in **Week 4 / capstone track**.

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

## HW2 (term frequency) — IN PROGRESS (design locked, data built, notebooks not yet authored)
**Resume here.** Decisions made with instructor this session:
- **Design:** "Whose words win? — a live debate vs. the document it invokes." Walsh-independent,
  built in the **2026 house style** (Parts A/B/C of discrete exercises + 2–3 Weekly Experiments +
  a clean-running ANSWER KEY). Pre-pandas (assigned Day 6) → **plain Python only, no pandas**.
  Builds directly on **HW1 C2** ("many comments → one word list").
- **Paired corpus (both committed to `notebooks/data/`, validated):**
  - `tc_youtube_comments.txt` — 93 real 2025 YouTube comments on the TX Ten Commandments law
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
- **Still TODO:** author `WRIT20833_HW2_2026.ipynb` + `_ANSWER_KEY.ipynb` (match HW1 metadata/badge/
  cell schema exactly — generate via a Python builder script), then **validate the key runs top-to-
  bottom** against the local data files.

## Other open threads / next steps
1. **Confirm scope** — drop-portfolio (current) vs. full-arc-tightened vs. foundations-only.
3. **Walsh-prereq strip on ported notebooks** — Tutorials 1–4 and the code-alongs open with an
   "assumes Walsh Ch 4–8" block; remove/replace as each is ported (HW1 already done).
4. **Port the carry-over-ready code-alongs** into this repo per the schedule (Variables already here;
   StrMethods/Conditionals/Loops, Lists/Loops, Dictionaries/Functions, Pandas 01/02, Instant Data
   Scraper, VADER, Topic Modeling). Dedup the topic-modeling notebooks (F25-canonical = combined Gensim).
5. **Author a 2026 syllabus** — none exists even in F25 (`WRIT20833_2025/docs/syllabus/index.md` is empty).
6. **Stylometry decisions** — fixed sample corpus vs. student-generated; essay weight; ethics emphasis.
7. **Test the topic-modeling install cell** (F25 HW4-2 pinned deps + runtime restart) on Colab's 2026 image.
8. **A4 / HW1 note:** A4 intentionally demonstrates a TypeError via try/except — by design.

## Useful facts for a fresh session
- The F25 source repo is **public**; if it's out of session scope, you can still read files via
  `raw.githubusercontent.com/TCU-DCDA/WRIT20833_2025/main/<path>` or `git clone` it (github.com is
  reachable). The Pages site `tcu-dcda.github.io` is NOT reachable from the sandbox allowlist.
- F25 full asset inventory is in that repo's `README.md`.
- No PR has been opened for this branch (per instructions — only on request).
