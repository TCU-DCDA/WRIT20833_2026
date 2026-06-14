# Lecture source notes — what to harvest from F25 for the 2026 mini-lectures

A running ledger of **reusable content mined from the F25 lecture decks** (`WRIT20833_2025/docs/lectures/`),
so the scale-out of ML1–ML7 doesn't re-discover the same material. Pairs with the `build_lectures.py`
registry and the WORKLOG "Lecture pages" section. When a later ML is authored, move the relevant rows here
into that lecture and check them off.

---

## F25 `docs/lectures/main/lecture1.html` (the full 23-slide Day-1 deck) — harvested 2026-06-13

The 2026 **ML0** (`materials/lectures/ml0.md`) is a tight single-thesis argument, *not* a port of this
survey deck. Triage below.

### ✅ Folded into ML0 (done this pass)
- **Rushkoff quote** ("…not the power to determine the value-creating capabilities of these technologies
  for [ourselves]") + the **Montfort** "think in new ways / understand culture / improve society" line —
  now the **"Use the programs, or shape them"** slide. This is ML0's own thesis, said by someone citable.
- **Project gallery** ("what distant reading looks like in the wild") — now the **"What it looks like in
  the wild"** slide: Every Noise at Once, Pudding hip-hop vocabulary, Trucks & Beer (country lyrics),
  Ben Schmidt gendered teacher reviews, Open Syllabus. (Photogrammar dropped to keep the list to 5; it's
  a good swap-in if one link rots.) The Trucks & Beer / hip-hop-vocabulary items also **preview HW2 + the
  Day-6 term-frequency code-along** (counting words in lyrics).
- **Two project chart images** for that slide (a 2-up row via the new `gallery` layout): the F25
  country-music "girl/love" scatter (`slide_09` → `materials/lectures/images/proj_country_love.png`) and
  Ben Schmidt's gendered-teacher-review dot plot (`slide_12` → `proj_teacher_reviews.png`). **Image audit
  (2026-06-13):** these were the *only two* F25 project screenshots that are legible data-viz; the rest
  are text-screenshots (`slide_08`/`slide_10`) or muddy/illegible (`slide_11`), and Open
  Syllabus/Photogrammar are logos only. **Every Noise at Once has no F25 image.** If a fuller image grid
  is wanted later, generate warm-palette images to match ML0's other slides (the `gallery` layout already
  supports `cols-2/3/4`).

### 🔶 Earmarked for LATER MLs (do NOT put in ML0 — would blur its spine)
- **→ ML1 "Connotations & Code" / "Code is not neutral":** the **data-feminism binaries material** —
  *"Rethink Binaries and Hierarchies"* (slide 17) and **Facebook's gender binary** (slide 18, with the
  quote: technical systems "default to binary classifications for computational efficiency and advertiser
  convenience… embed[ding] particular worldviews about gender into algorithmic systems"). Source cited:
  Data Feminism, https://data-feminism.mitpress.mit.edu/pub/h1w0nbqp/release/3. Strong "neutral coding
  decisions aren't neutral" anchor.
  - Also reusable for ML1: the **Rushkoff "program or be programmed"** framing has a second life here as
    "whose values are in the tool," if ML0 only uses the value-capabilities half.
- **→ ML3 "Classification Logic" (whose categories?):** the same binaries/Facebook-gender example doubles
  as a *sorting-as-judgment* case — pick whichever lecture (ML1 vs ML3) leans harder on it so they don't
  duplicate. Open Syllabus ("the canon," whose authority?) also fits ML3's "whose categories" frame.
  (WORKLOG already earmarks F25 `data_as_categorization` + `tippingScales` images for ML3.)
- **→ ML4 "AI Agency" (reading/judging machine code):** Rushkoff's "use the programs made for us" is the
  perfect setup for "…and now the programs write themselves — can you still judge them?"
- **Close vs. distant reading as *named* methodologies** (slides 7–8, "Traditional/Newer Methodology") —
  ML0 enacts the move but never names "distant reading" (Moretti). If a later lecture wants the vocabulary
  explicit, it's here. Candidate: wherever the close→distant→close arc is taught (Day 12 lecture).

### ❌ Skip (off-scope or contradicts ML0's honesty)
- **Semester overview** (Sept–Dec, "10 Labs / 12 Journal Entries") — F25 16-week structure; wrong course.
  The 2026 schedule already lives in `COURSE_SCHEDULE_2026.md` / `docs/schedule.html`.
- **Tools / Skills slides** listing **HTML/CSS/JavaScript / web publishing / version control** — the cut
  web-dev half (overlaps MALA 60970). Off-scope for the drop-portfolio 2026 port.
- **Two-instructor slide** (Dr. Lucas, Calendly, photos) — 2026 is Rode solo; contact lives in the syllabus.
- **"Coding gives us superpowers" framing** (scale/pattern/preservation/accessibility as unalloyed wins) —
  techno-optimist; ML0 deliberately balances the payoff against "what the counting flattens."
- **DH definition grid** (Traditional Humanities vs Digital Methods two-column) — ML0's close-vs-distant
  move covers this more elegantly without the listy survey feel.

---

## F25 `mini-lectures/lecture-1-connotations/` ("Data Has Connotations") — harvested 2026-06-13 → ML1

Authored **ML1 "Connotations & Code"** (`materials/lectures/ml1.md`, 7 slides) in ML0's voice, ported from
F25's 8-slide deck. Title page links live (`build_lectures.py` registry + `build_index.py` card).

### ✅ Folded into ML1
- **Denotation vs. connotation** (the deck's core) — reframed as "the humanities' oldest tool, and it
  works on numbers too" (house/home/residence → "single-mother household" → numbers have connotation).
- **The myth of neutral data** (3 false sayings) — kept, tied back to ML0's "bias is the material."
- **Test-scores case study** (School A 1240 / School B 980 → deficit/systemic/cultural) — kept; the
  cleanest "same denotation, three connotations" example.
- **Who controls the story** (institutions/media/researchers) and **missing data / missing voices** —
  kept; the "missing voices" slide is re-grounded in *our* corpus (the 123 comments are only the public
  that *posted*; ML0's woman who said nothing isn't in the file).
- Synthesis slide **"code is not neutral"** ties the linguistic concept to the code students will write
  (what counts as a "word," stopwords, the "positive" cutoff) → back to ML0's "make your choices visible."

### Image audit (2026-06-13): nothing usable to harvest
- The deck references 8 `images/JPEG/*.jpg` that **were never generated** — only `.prompt` files exist.
- The one rendered image (`lecture-1-connotations/images/slide1_data_connotations.jpg`) is **deep-purple/
  neon** (the old F25 cyberpunk palette) — clashes with the warm "Reading Room" look, same reason ML0's
  F25 images were rejected. **ML1 ships text-forward.** If imagery is wanted later, generate warm-palette
  images (as the instructor did for ML0) and drop them in via the `split`/`gallery` layouts; F25's
  `IMAGE_PROMPTS.md` / `image-generation-prompts.md` in that deck folder are usable prompt starting points.
- **Image slots prepped (2026-06-13):** 4 slides are marked `<!-- layout: split -->` with a ready-to-use
  warm-palette **image prompt + target filename + a commented `![]()` line** embedded right in
  `ml1.md` — title (`ml1_title.jpg`), Denotation (`ml1_denotation.jpg`), Missing/uncounted
  (`ml1_missing.jpg`), Code-is-not-neutral (`ml1_code.jpg`). The prompts are HTML comments (inert — the
  slides render clean full-width until art exists). **To add an image:** generate it, save to
  `materials/lectures/images/<name>.jpg`, uncomment the `![]()` line, rerun the generators — the 2-column
  split activates automatically. Same pattern is the template for future lectures' image slots.

### Division of labor with ML3 (decided 2026-06-13)
- ML1 owns **connotation / the myth of neutral data**. The **data-feminism binaries + Facebook
  gender-binary** example (from `lecture1.html`, earmarked above) stays with **ML3 "Classification Logic"**
  (forced categories / sorting-as-judgment) to avoid duplication.

## F25 `mini-lectures/lecture-3-classification/` ("Coding Taboo Logic") — harvested 2026-06-14 → ML3

Authored **ML3 "Classification Logic"** (`materials/lectures/ml3.md`, 7 slides). Pairs with the **Day-3
(Wed 7/8) conditionals/booleans code-along** (schedule-confirmed) — it's the humanities frame for the
`if/else` students learn that day. Registered in both build scripts; dashboard card links it.

### ✅ Folded into ML3
- **Code decides / classification encodes values** (F25 slides 2, 6) — reframed as "to classify is to
  judge; there is no neutral box."
- **Status as data** (F25 slide 3) — kept as "status has always gated access," boolean variables
  (`credit_score`, `criminal_background`, …) as the automated gate.
- **The threshold** (F25's `if credit_score > 650` example) — built into its own slide and **threaded to
  HW3's `compound > 0.05` cutoff** (framework's "classification is authored" row).
- **Classified BY vs. building the sort** (F25 slide 6/8) — kept nearly whole; the power point.
- **Readings** (Noble *Algorithms of Oppression*, Benjamin *Race After Technology*, O'Neil *Weapons of
  Math Destruction*) — kept as an optional "going deeper" line on the last slide.
- **The binaries / Facebook gender-binary example** (earmarked from `lecture1.html`) **landed here**, on
  "The tyranny of the tidy box," with the Data Feminism gloss — as decided in the ML1 entry.

### Deliberately changed / dropped
- **De-emphasized the "sacred / taboo" framing** that titles the F25 deck ("Coding Taboo Logic," ritual
  purity, sacred/profane). That's **parked-ML2 territory** (open thread #9), and leaning on "sacred
  categories" sits badly next to a *literally sacred* corpus (the Ten Commandments). ML3 keeps the durable
  core — sorting as judgment — and only gestures at the historical "status gated access" point.
- Dropped F25's `1847`-data Colab tutorial link (F25-specific) and the emoji/checkpoint chrome.

### Image audit (2026-06-14): earmark superseded — used as composition comps, not dropped in raw
- The two earmarked images **exist but are off-palette**: `images/JPEG/data_as_categorization.jpg` is
  black/cyan **cyberpunk** (people routed into category-circles); `images/JPEG/tippingScales.png` is a
  **blue cartoon** (people-vs-institutions balance). Neither matches the warm oil-painting "Reading Room"
  look (same call as ML0/ML1's F25 art).
- **Resolution:** ML3 ships text-forward with **3 split-ready slides + embedded warm-palette prompts**
  (title `ml3_title.jpg`, threshold `ml3_threshold.jpg`, tidy-box `ml3_schema.jpg`). The prompts **reuse
  the *concepts*** of the two F25 images recomposed in warm paint (the schema prompt explicitly recomposes
  `data_as_categorization`'s people-into-boxes idea; the threshold prompt echoes ml0's brass-valves). Same
  inert-comment pattern as ML1 — generate → save → uncomment → rebuild activates the 2-column split.

## F25 `mini-lectures/lecture-5-memory/` ("Collective Digital Memory") — harvested 2026-06-14 → ML5

Authored **ML5 "Collective Memory"** (`materials/lectures/ml5.md`, 7 slides). Pairs with the **Day-4 (Thu
7/9) lists & loops code-along** — the humanities frame for lists/loops, exactly as ML3 framed `if/else`.
Registered in both build scripts; dashboard card links it.

### ✅ Folded into ML5
- **Two kinds of memory** (F25 slide 2) — selective/forgiving human memory vs. total/unforgiving digital
  memory; reframed around "forgetting was also grace."
- **Lists = populations** (slide 3) and **loops = systematic processing** (slide 4) — kept as the two core
  slides ("a list is a population," "a loop is a verdict, repeated"); the loop slide threads back to ML3's
  threshold ("the loop is how that one cutoff hits a million people").
- **Counting = surveillance** (slide 5) — "the power to count is the power to decide what matters" + the
  who-counts/who-sees/what-about-the-uncounted questions (ties ML1 missing voices).
- **Historical echoes** (slide 6) — kept the **Bellevue Almshouse + Anelise Shrout quote** verbatim (the
  moral heart) and the "list of dicts = the same reduction" parallel.
- **Readings** (Connerton *How Societies Remember*, Mayer-Schönberger *Delete*, van Dijck *Mediated
  Memories*) — kept as the optional "going deeper" line; the forgetting-as-virtue angle is distinctive.
- Dropped F25's Colab tutorial link + the "tools for social justice" agency slide's lighter bullets
  (folded the agency point into the synthesis "What we choose to keep").

### Image audit (2026-06-14): `newImages/` higher-craft but still off-palette
- ML5 has its own `newImages/` (9 imgs) — better than the older decks but still **neon cyberpunk**
  (slide01 purple→green filing cabinets/servers); slide06 is **half warm-sepia / half cold-blue**. Not
  consistently warm Reading Room.
- **Resolution (same pattern):** text-forward + **3 split-ready slides with warm-palette prompts** (title
  `ml5_title.jpg` = warm card-catalog-of-memory, recomposing slide01; population `ml5_population.jpg`;
  echoes `ml5_echoes.jpg` = recompose slide06's then/now records office kept warm/sepia). Inert comments;
  generate → uncomment → rebuild activates the split.

## Other F25 decks (not yet mined)
The per-lecture decks for ML1–ML9 live in `WRIT20833_2025/docs/lectures/mini-lectures/lecture-*` (e.g.
`lecture-1-connotations`, `lecture-3-classification`, `lecture-4-agency`, `lecture-5-memory`,
`lecture-6-archaeology`, `lecture-7-nlp-topic-modeling`, plus parked `lecture-2-boundaries`,
`lecture-8-code-rhetoric`, `lecture-9-public-arguments`). Mine each into its `materials/lectures/ml*.md`
when authored, and record the triage here. ML10–12 (GitHub/HTML/CSS) are cut.
