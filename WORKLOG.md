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

## Epistemological spine — the noumena→wisdom keystone (course-wide frame)
The unifying frame the course implies everywhere but never states. An F25 graphic
(`materials/images/noumena_to_wisdom_pipeline.png`, **ported 2026-06** from F25's orphaned
`_development/textbook/images/20833_noumena_wisdom_F25.png` — built, never wired into any
lecture/notebook) lays out an 8-stage pipeline: **NOUMENA → PHENOMENA → RAW DATA → STRUCTURED DATA
→ ANALYZED DATA → INSIGHT → KNOWLEDGE → WISDOM** (the DIKW pyramid extended *backward* into Kantian
epistemology). Left half = "the score is not the sentiment / a topic is proposed not found"; right
half = ungrading's "earned insight."
- **The instructor's argument:** every arrow is an occasion for human bias — and bias is
  **constitutive and cumulative, not "contaminating"** (the scare quotes matter: there's no clean
  origin to pollute; the phenomenon is already an interpretation, each step compounds the prior). You
  can't fix a result back to truth, only make the choices visible/accountable — which is what the
  `#comments` rule and the 3 reflections train.
- **Every arrow already maps to a built artifact** (collection→Day 8 scraping/wrap-fragments;
  raw→structured→HW2 stopwords + HW3 "keep punctuation"; structured→analyzed→VADER 0.05 cutoff +
  HW4 `num_topics`; analyzed→insight→HW4 "human names the topics"; etc.). **Full per-arrow table +
  teaching use live in `materials/images/README.md`** (kept there so it's discoverable, not re-orphaned).
- **Status / next:** graphic ported + documented; **Day-1 framing passage drafted**
  (`materials/Day1_Framing_Noumena_to_Wisdom.md` — student-facing script + per-unit callback notes;
  ~600 words, "the score is never the meaning"). **Still not wired into an actual lecture/the syllabus.**
  Candidate homes: **ML0 / Day 1** (founding "what can computation know?") with a callback at each
  unit, and/or the **Day 7** close-vs-distant hinge. Open dial: keep the explicit "noumena/phenomena"
  vocabulary or swap to "the thing itself / as it appears" (diagram + argument survive either way). Pairs with the orphaned **ML9 "Going Public"**
  (re-home at Day 17) — together they'd give the capstone its missing epistemology. Decision for the
  instructor: introduce the Kantian vocabulary explicitly, or keep it as the instructor's framing only.

## Through-line — "hear the human at scale" (course motto + ethics)
The unifying *why* behind the existing subtitle "Developing Data-Driven Opinions." We collect textual
data, in part, **to hear the human at scale** — to listen to more people than close reading ever could.
This reconciles the apparent contradiction the course keeps staging (computation *flattens* voices vs.
computation *empowers* them): the flattening is the **price of the scale, and the scale is the point**
— distant reading isn't *not* reading humans, it's hearing humans you'd otherwise never hear.
- **Listen vs. extract (governing metaphor + teachable enemy).** "Hear/listen" stands against the
  extractive verbs of data culture — *mine, scrape, harvest, crawl.* Those treat people as ore; "hear"
  presumes someone with something to say and a duty to receive it. Reframes Day-8 collection ethics from
  "is this allowed?" to **"am I listening or extracting?"**
- **Hearing the human means hearing the MESS (ties to ML0 "studying the mess of the human condition").**
  The humanities don't tidy up contradiction/ambiguity/subjectivity — they explore it. But every scale
  tool *wants* a tidy answer: a single mean sentiment, one "winning" word, a dominant topic. So the real
  danger isn't only going deaf to the individual — it's **manufacturing a false consensus that silences
  the quarrel.** To hear the human is to hear the **inevitable quarrels**; the disagreement is not noise
  to average away, it *is* the signal. The corpus is literally a quarrel (the TX Ten Commandments law).
- **The course already enacts "preserve the quarrel":** HW3's near-zero **mean sentiment (0.082)** is a
  *split* crowd, not neutrality (the average almost erased the fight); HW2→HW3's **`commandments` in both
  camps** is a quarrel hiding inside a frequency "winner"; HW4's **sentiment-by-topic** exposes
  sub-quarrels; **reading the extremes** + the **human-vs-VADER check** + **"the human names the topics"**
  are all *returning to the individual to confirm you can still hear a person, and still hear the
  disagreement.* The **close→distant→close** arc = hear one deeply → hear the many → go back to one to
  make sure the many are still people in conflict, not a manufactured consensus.
- **The dinner-party / stadium illustration (canonical for Day 12 close-vs-distant).** A guest at a
  12-person dinner notices a couple he just met bickering at the end of the table — a particular nuance
  he can observe. The *same* guest watching the *same* couple from across AT&T Stadium at a Cowboys
  game cannot. **The nuance still exists; it's only flattened from *view*.** The key refinement to the
  whole through-line: scale **occludes** the particular (epistemic — a matter of vantage / resolution);
  it does **not destroy** it (ontological) — the couple is still bickering, still *in* the data. So
  "flattened from view ≠ erased from existence," which is why the quarrel is **recoverable**: change
  vantage (close reading / reading the extremes / the human-vs-VADER check = walking down to that
  section of the stands). And the trade runs **both ways** — from the stadium you can see the **wave**,
  a coordinated macro-pattern of 90,000 people that *no one* at dinner-party scale could perceive (term
  frequency + topic modeling = seeing the wave). Neither vantage is "the truth"; each is blind to what
  the other reveals → the real argument for **close→distant→close**. *(Caveat keeping the edge: even
  the dinner seat isn't the noumenon — the guest sees the bicker, not its whole meaning; close reading
  is higher resolution, not truth. The analogy shakes hands with the noumena spine.)*
- **Two referents of "voice":** the people *in* the data (protect from flattening/misrepresentation,
  empower by making audible at scale — the home for orphaned **ML9 "Going Public"**) **and** the
  student's *own* voice (ungrading + `#comments` + reflections keep the learner a person-on-the-record,
  not a number — the course empowers voice by example).
- **Writing in the age of AI — developing your own voice through the difficulty (WRIT course!).** The
  third movement, and the one that makes this a *writing* course: you must *remain* a human voice to do
  justice to the human voices you hear. **Letting AI write for us forfeits the opportunity — available
  only through the difficulty — of developing a unique voice.** Voice is forged in the friction of
  finding words; remove the friction and you remove the forging.
  - **The asymmetry of borrowing (core literacy):** borrowing the *tool* (code) is expected and fine —
    nobody's voice lives in a stopword list; borrow the utility, *understand + judge* it (the
    borrowed-code convention). Borrowing the *voice* (writing) is self-erasure — the difficulty IS the
    point. The course teaches both coding-with-AI and writing, so it's built to teach the discernment:
    **borrow the tool, never outsource the voice — and know which is which.**
  - **The eerie parallel (same lesson, turned on the self):** AI-generated prose : your voice ::
    **mean sentiment : the crowd's quarrel** — a flattening of the particular into a statistical
    average, a *false consensus* that silences what's specific. The model writes the mean of all
    writing; a unique voice is its opposite. The whole apparatus the course builds against false
    consensus *in the data* applies unchanged to your own *writing*: resist the flattening — of others,
    **and of yourself.**
  - **Aligns with what's built:** ungrading already credits *struggle/labor/reflection over polish* —
    it values the difficulty as the point; AI-polished prose that skips the struggle is the opposite of
    what it rewards. Refines the syllabus **AI-use policy** (currently written mostly for code) with the
    missing distinction: AI is fine for code-you-understand and for *feedback*, but **generating the
    writing itself forfeits the voice the course exists to develop** (reflections, `#comments`, the
    capstone essay are where you become a writer). Natural home: **Day 7 / ML4 AI Agency** (extend from
    "reading AI's code" to "not ceding your voice to AI") + the **capstone essay standard**.
- **Secures both halves:** ties the **ethics** (voice) to the **epistemics** (evidence) — a data-driven
  opinion earns the right to drive only when the data has been *heard*, not merely processed; and lands
  on the **noumena spine** (the descent is justified by the aim of hearing the aggregate; the right
  column is the climb back to hearing the chorus *as humans, still quarreling*).
- **Caution (keep the edge):** pair "empower" with discipline — the failure mode is "let the data speak
  for itself" (it never speaks; *you* speak, having chosen). Hearing at scale is using a megaphone that
  distorts: amplify the signal, own the distortion, and don't resolve a quarrel the data didn't resolve.
- **Status / candidate fold-ins (instructor's call):** through-line captured; not yet woven in. Options —
  gloss the subtitle ("…Developing Data-Driven Opinions **to hear the human at scale**"); a learning
  outcome on *representing others' voices responsibly*; the **Day-1** noumena passage's ethical turn; the
  **Day-12** close-vs-distant thesis sentence; the **capstone standard** ("give voice to the people in
  your data — including their disagreements — and show where your tools risked flattening them").

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
4. **Port the carry-over-ready code-alongs — IN PROGRESS (foundations-first pilot).** Goal: every
   *coding* session in `COURSE_SCHEDULE_2026.md` names a real notebook (kill the conceptual bleed).
   - **Already in 2026:** Variables/DataTypes, Lists/Loops/Conditionals (combined; covers Days 3–4).
   - ✅ **Pilot done:** `notebooks/codeAlongs/WRIT20833_Dictionaries_Functions_2026.ipynb` (Day 5) —
     ported from F25 (52 cells → focused 35) into the **2026 code-along style** (warm cultural
     examples; concept→code→"your turn"; Putting-It-Together / Sneak Preview / Playground; `colab`
     metadata matched). Walsh-independent; builds a `count_words` dict → `Counter` to **seed Week-2
     term frequency**. Built by `_build_dictfunc.py`; **all 17 code cells validated top-to-bottom.**
   - **Decision (pilot fidelity):** match-2026-style (not faithful F25 copy) — confirmed.
   - **Remaining ports (batch after pilot review):** Strings & string methods (Day 2; partial today
     lives in the Variables nb), Pandas 01 + Instant Data Scraper (Day 8), Pandas 02 (Day 9), VADER
     (Days 11–12), Topic Modeling Gensim (Days 14–15; dedup → combined Gensim). Open: **term frequency
     (Day 6)** has no F25 standalone code-along — build a short one or teach via HW2.
   - **Also relabel genuinely non-coding days** in the schedule (7, 10, 13, 16, 17–20) as
     *Workshop / Work session / Lab* so their content reads as intentional, not vague code-along.
   - **Schedule rewrite (name every notebook + relabel) deferred until the batch lands**, so the grid
     updates in one consistent pass.
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

## Useful facts for a fresh session
- The F25 source repo is **public**; if it's out of session scope, you can still read files via
  `raw.githubusercontent.com/TCU-DCDA/WRIT20833_2025/main/<path>` or `git clone` it (github.com is
  reachable). The Pages site `tcu-dcda.github.io` is NOT reachable from the sandbox allowlist.
- F25 full asset inventory is in that repo's `README.md`.
- No PR has been opened for this branch (per instructions — only on request).
