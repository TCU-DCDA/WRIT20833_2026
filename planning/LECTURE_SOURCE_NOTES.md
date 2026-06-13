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

## Other F25 decks (not yet mined)
The per-lecture decks for ML1–ML9 live in `WRIT20833_2025/docs/lectures/mini-lectures/lecture-*` (e.g.
`lecture-1-connotations`, `lecture-3-classification`, `lecture-4-agency`, `lecture-5-memory`,
`lecture-6-archaeology`, `lecture-7-nlp-topic-modeling`, plus parked `lecture-2-boundaries`,
`lecture-8-code-rhetoric`, `lecture-9-public-arguments`). Mine each into its `materials/lectures/ml*.md`
when authored, and record the triage here. ML10–12 (GitHub/HTML/CSS) are cut.
