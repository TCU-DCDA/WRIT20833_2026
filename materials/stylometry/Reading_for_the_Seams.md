# Reading for the Seams — Stylometry of Human, AI, and Hybrid Writing

> **Status: DRAFT exercise for instructor review.** New content extrapolated this session
> from the `ai_voice_claude_analysis.pdf` artifact. Extends Tutorial 3 (AI Agency) from
> analyzing AI *code* to analyzing AI *prose*.

**Course:** WRIT 20833 · **Theme tie-ins:** Mini-Lecture 4 (AI Agency), Mini-Lecture 8
(Code as Rhetoric) · **Method tie-in:** close vs. distant reading (taught in the VADER unit)

---

## Big idea

AI-assisted writing has recognizable habits — not obvious errors, but **smoothness**: a
predictable *macrostructure* (praise → softened critique → a tidy menu of options →
permission-giving close) and *micro-tells* (burden-reducing language, balanced low-friction
syntax). Human writing shows up as **friction**: compression, idiom, domain-specific
vocabulary, locally-grounded detail.

This exercise teaches students to read for those seams two ways — by hand (**close reading**)
and by measurement (**distant reading**) — and to hold conclusions loosely. **AI-detection is
unreliable and biased** (notably against non-native English writers); the goal is *insight
about voice, averaging, and standardization*, not catching cheaters.

The companion file **`ai_voice_claude_analysis.pdf`** is the worked exemplar: an AI model
close-reading a human-edited AI email, separating "likely AI scaffolding" from "likely human
texture," building an attribution map, and ending with a "practical heuristic" that explicitly
says *avoid overclaiming*.

---

## Two-part, split placement

### Part B — Close reading (Day 7, with AI Agency). No code.
Students read a short hybrid passage and, using the PDF as a model, build their own
**attribution map**:

| Passage segment | Likely source (AI / human / mixed) | Reason |
|---|---|---|

They identify **scaffolding** vs. **texture**, then write a short paragraph applying the PDF's
practical heuristic. This produces a **prediction**: *which parts are AI, and what gave it away?*
(Requires no programming — it rides the Day-7 AI Agency theme.)

### Part A + C — Distant reading + synthesis (Week 4 capstone). The notebook.
See `WRIT20833_Stylometry_Reading_Seams_2026.ipynb`. Using the term-frequency tools students
already know, they **measure** style signatures across human / AI / hybrid texts:
- **Function-word share** — the elegant inversion of the term-frequency unit: there, stopwords were *noise to
  remove*; here, function words are the *signal*.
- **Type–token ratio** (lexical diversity)
- **Average sentence length** (and how varied it is)
- **Hedging / softening phrase counts** ("perhaps", "a quick example or two", "whatever feels")

Then **Part C — synthesis**: do the numbers confirm or upend the Day-7 close read? This is the
course's "being wrong as learning" engine and its close → distant → close validation loop.

---

## Capstone track
Students may choose the **stylometry capstone** instead of the cultural-dataset track:
assemble their own small human / AI / hybrid corpus, run Part A on it, and write the
data-driven-opinion essay around what the signatures + close reading reveal about voice.

## Learning objectives
- Define stylometry; distinguish close vs. distant reading of style.
- Reuse term-frequency / function-word methods to quantify a stylistic signature.
- Read critically for AI scaffolding vs. human texture; build an attribution map.
- Practice epistemic humility — articulate why AI-detection claims must stay probabilistic.
- Connect computational measures to the course's critical themes (agency, classification, voice).

## Materials needed
- `ai_voice_claude_analysis.pdf` (exemplar — included).
- A short hybrid passage for Part B (the PDF's email works; or supply your own).
- For Part A: instructor-provided human/AI/hybrid samples, **or** student-generated ones
  (write one, prompt an LLM for one, edit an AI draft for the third).

## Assessment
Notebook (Part A code + brief interpretation) + written attribution map and reflection
(Parts B/C) — fits the capstone "notebook + essay" format.

## Open decisions
- Provide a fixed sample corpus, or have students generate their own?
- Essay weight/length relative to the cultural-dataset capstone track.
- How heavily to foreground the AI-detection-bias ethics (recommended: prominently).
