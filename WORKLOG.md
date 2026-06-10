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
- **Ungrading evaluation (course-wide)** — carries F25's philosophy ("earned insight over
  clean code", see `PORT_ASSESSMENT_2026.md`). Work is evaluated on engagement, reflection,
  and labor — the required `#comments`, predict-then-run guesses, Weekly Experiments, and
  reflective write-ups — **not** on correctness scores. Implications for authoring: avoid
  "grade/points/score" framing (say "evaluated/expected/complete"); answer keys are
  **instructor references + discussion fodder, not rubrics**; Submit checklists emphasize
  completion + reflection over right answers. The capstone "essay weight" open decision means
  *emphasis/expectation*, not a points scheme.
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

## Other open threads / next steps
1. **Confirm scope** — drop-portfolio (current) vs. full-arc-tightened vs. foundations-only.
3. **Walsh-prereq strip on ported notebooks** — Tutorials 1–4 and the code-alongs open with an
   "assumes Walsh Ch 4–8" block; remove/replace as each is ported (HW1 already done).
4. **Port the carry-over-ready code-alongs** into this repo per the schedule (Variables already here;
   StrMethods/Conditionals/Loops, Lists/Loops, Dictionaries/Functions, Pandas 01/02, Instant Data
   Scraper, VADER, Topic Modeling). Dedup the topic-modeling notebooks (F25-canonical = combined Gensim).
5. **Author a 2026 syllabus** — none exists even in F25 (`WRIT20833_2025/docs/syllabus/index.md` is empty).
6. **Stylometry decisions** — fixed sample corpus vs. student-generated; essay weight; ethics emphasis.
7. **Test the topic-modeling install cell on Colab's 2026 image.** HW4 uses a lean `!pip install -q
   gensim vaderSentiment` (no nltk, no pinned deps, no kernel restart — simpler than F25's cell);
   still verify it resolves cleanly on Colab's 2026 default image before Day 14.
8. **A4 / HW1 note:** A4 intentionally demonstrates a TypeError via try/except — by design.

## Useful facts for a fresh session
- The F25 source repo is **public**; if it's out of session scope, you can still read files via
  `raw.githubusercontent.com/TCU-DCDA/WRIT20833_2025/main/<path>` or `git clone` it (github.com is
  reachable). The Pages site `tcu-dcda.github.io` is NOT reachable from the sandbox allowlist.
- F25 full asset inventory is in that repo's `README.md`.
- No PR has been opened for this branch (per instructions — only on request).
