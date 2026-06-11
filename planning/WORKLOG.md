# WORKLOG — WRIT 20833 2026 port (session handoff)

**Branch:** `claude/port-strings-codealong` (prior work merged to `main` via PR #1) · **Last updated:** 2026-06-11

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
  (re-home ML9 → Day 17, harvest ML8, decide ML2 "Sacred Boundaries" cut-vs-repurpose) — see open thread #9.

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
7. **Test the topic-modeling install cell on Colab's 2026 image.** HW4 uses a lean `!pip install -q
   gensim vaderSentiment` (no nltk, no pinned deps, no kernel restart — simpler than F25's cell);
   still verify it resolves cleanly on Colab's 2026 default image before Day 14.
8. **A4 / HW1 note:** A4 intentionally demonstrates a TypeError via try/except — by design.
9. **Lecture audit — ML8/ML9 (orphaned) and ML2 "Sacred Boundaries" (overreach?).** ML0–7 map cleanly
   to 2026; ML10–12 (GitHub/HTML/CSS) cut. Still to decide: **re-home ML9 "Going Public"** at Day 17
   (its analysis→public-argument spine fits the capstone; only the web-portfolio delivery is cut), and
   **harvest ML8 "Code as Rhetoric"**'s thesis into the code-is-not-neutral thread (its HTML/CSS examples
   belong to the cut half). **ML2 "Sacred Boundaries" (Day 2)** = a taboo→privacy analogy (Polynesian
   *tapu* → biometric/data autonomy). Instructor leans *overreach*; my read agrees for this scope: its
   privacy/ethics core is better + more concretely served by **ML6 Data Archaeology (Day 8)**, and the
   "sacred" metaphor risks colliding with the **literal** sacred content of the corpus (Ten Commandments).
   Options on the table: (a) cut ML2, fold its one durable point (analyzing public speech isn't
   consequence-free) into Day 8; or (b) **repurpose** the slot — "the sacred meets the computational,"
   pointing at the actual corpus, as a vivid case of the noumena limit (religious conviction = an
   interiority distant reading can't reach). **Undecided — instructor's call.**
10. **TCU Core Curriculum — CSV vetting (context + a task).** The course **carries Citizenship & Social
    Values (CSV)** credit. Vetting docs are in `reference/`: `reference/TCU-Core-Curriculum-outcomes-1.pdf`
    (current outcomes matrix) + `reference/Citizenship-and-Social-Values-5-5-10.doc` (older HMVV form). Current CSV
    outcome: *"examine the knowledge, skills, values, or motivation needed to participate or lead within
    diverse communities."* The course meets it directly (a contested public-policy debate = a diverse
    community in disagreement; the data-driven-opinion capstone + discussions + reflections are the
    evidence). Full mapping + the course's adjacent resonance (Humanities, Written Comm 2, Cultural
    Awareness) in `CONCEPTUAL_FRAMEWORK_2026.md` §7; syllabus now names the CSV designation. **Task when
    wanted:** draft the **2–3 concrete student-work examples** the CSV submission form requires (from the
    capstone + discussions), once the instructor confirms the exact outcome to claim.

11. **TCU syllabus — ✅ ALIGNED TO AddRan + F25 (2026-06-11, second pass).** Reviewed the AddRan syllabus
    docs in `/Users/curtrode/Code/AddRan/syllabus-checker/source_files` (AddRan Simplified Template,
    Fall-2026 review instructions, **the F25 WRIT 20833 syllabus co-authored with Lucas**). Big unblock:
    AddRan handles University-policy boilerplate via the **Student Resources & Policy Information QR/link**,
    not pasting — so the old `[paste …]` placeholders are **gone**. Revised `SYLLABUS_2026.md`: added the
    QR block (cte.tcu.edu image) + a Note-for-students; a **Land Acknowledgment**; the **University-Absence**
    + **Medical-Privacy** statements (AddRan text) under *Attendance & Engagement*; course **Recording** +
    **Academic Conduct** statements; **CSV outcome-mapping** in the assignments table; dropped the TCU-Online
    getting-started + the long University-Policies paste list. **Only residual:** `[...]` instructor/registrar
    fields + **export to Word** (`WRIT20833-[section]_Summer2026_Rode`) for AddRan submission (Word, in
    template order; see the review instructions). Crosswalk `planning/SYLLABUS_COMPLIANCE.md` updated.
    F25 syllabus also confirms this course already ran **ungrading** + no-attendance-deduction.
    *(Earlier first-pass verification against the standard TCU checklist remains below for history.)*

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
**GitHub blob**. Intra-site links (index→schedule) stay relative. CSS is still **inlined** per page
(self-contained), not a shared stylesheet. Generators (`site_theme.py`, `build_index.py`,
`build_schedule_html.py`) sit at repo root and write into `docs/`.
**To publish:** make the repo public, then *Settings → Pages → Deploy from branch → `main` / `docs`*.
Colab/badge links resolve only once public.

## Useful facts for a fresh session
- The F25 source repo is **public**; if it's out of session scope, you can still read files via
  `raw.githubusercontent.com/TCU-DCDA/WRIT20833_2025/main/<path>` or `git clone` it (github.com is
  reachable). The Pages site `tcu-dcda.github.io` is NOT reachable from the sandbox allowlist.
- F25 full asset inventory is in that repo's `README.md`.
- Code-along batch + Day-6 term frequency shipped on PR #2 (`claude/port-strings-codealong`).
