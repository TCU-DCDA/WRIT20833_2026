# Capstone — A Data-Driven Opinion

**WRIT 20833 — Intro to Coding in the Humanities · "When Coding Meets Culture" · Summer 2026**

> **DRAFT for instructor review.** Authored in the 2026 house style and ungrading voice; cross-checked
> against `SYLLABUS_2026.md`, `COURSE_SCHEDULE_2026.md`, and `planning/CONCEPTUAL_FRAMEWORK_2026.md`.
> A few `[...]` spots are instructor/submission specifics (where to upload, presentation length).

---

## What this is

The capstone is the course's **Final Evaluative Exercise** — it stands in for a final exam. You take a
cultural text you care about, run the tools you've learned on it, and **argue from what you find.** It is
the moment the whole course has been pointing at: *frequency → sentiment → topic modeling*, and then the
harder human work of saying what the numbers mean and where they mislead.

You hand in three things, all about the **same** dataset:

1. **A notebook** — your analysis, with `#comments` that show your thinking.
2. **A short essay** (~800–1,200 words) — your **data-driven opinion**, argued from the notebook.
3. **A short presentation** (~`[3–5]` min) on the last day — one finding and one thing your tools got wrong.

This is **HW4's B4/C2 grown up.** In HW4 you wrote "your capstone in miniature"; this is the full size.

**Due dates** (see the schedule): **proposal — Mon 7/27** · **notebook + essay — Fri 7/31** (presented in
class that day). The final self-evaluation (**Reflection 3**) is also due Fri 7/31 — the capstone is the
biggest piece of evidence you'll cite in it.

---

## Choose a track

You pick **one**. Both end in the same deliverables (notebook + essay + presentation) and are evaluated
the same way.

### Track A — Cultural dataset *(the main path)*
Analyze a corpus of real human language about something you care about — ideally **your own dataset**,
the one you collected and cleaned in the Week-2 workshop and carried through HW3/HW4. Examples: comments
on a news video or post, song lyrics by an artist, reviews, a public figure's speeches, forum threads,
your own social feed. If your own data didn't come together, the **provided Ten Commandments comment
corpus** (`notebooks/data/`) is a ready fallback — the same one our code-alongs and homeworks use.

The question that drives Track A: **what is this conversation actually about, and how do the people in it
feel — including where they disagree?**

### Track B — Stylometry *(the alternate path)*
Instead of a cultural debate, study **voice itself** — human vs. AI vs. hybrid writing. Assemble a small
corpus (write one short piece, prompt an LLM for one, edit an AI draft into a third — or use the
instructor-provided samples), then use the **function-word / lexical-diversity / sentence-length /
hedging** measures from `materials/stylometry/` to read for the *seams* between human texture and AI
smoothness. See the [stylometry handout](materials/stylometry/Reading_for_the_Seams.md) and its
[notebook](materials/stylometry/WRIT20833_Stylometry_Reading_Seams_2026.ipynb).

The question that drives Track B: **what does a writer's style measurably reveal — and why must any
claim about "this is AI" stay a probability, never a verdict?** *(AI-detection is unreliable and biased,
notably against non-native English writers. The point is insight about voice and standardization, not
catching anyone.)*

---

## The notebook — analyze your data

Your notebook should let a reader follow you from raw text to a claim. There's no one right shape, but a
strong capstone notebook does roughly this:

1. **Load and look.** Read your data in (pandas), show its size and a few rows, and say in a `#comment`
   what it *is* and where it came from.
2. **Clean, and say what you changed.** Cleaning is already interpretation — note what you dropped or
   standardized and what that choice might hide. (Recall HW3: clean *but keep* punctuation for sentiment.)
3. **Run at least two of the three lenses, and bring them together.**
   - **Frequency** — which words dominate (HW2 / the term-frequency code-along).
   - **Sentiment** — how the crowd feels, VADER (HW3).
   - **Topics** — what sub-conversations cluster, Gensim LDA (HW4).
   - Using **all three and integrating them** — e.g. `groupby("topic")["sentiment"].mean()`, as in HW4
     B3 — is the fullest version, and the one the course is built toward. *(Track B: the stylometry
     measures are your lenses; use at least two and compare them.)*
4. **Close → distant → close.** Don't stop at the aggregate. Read a few **individual** texts by hand —
   the extremes, a surprising case, a document the tool labeled oddly — and check the numbers against
   them. This is the move the whole course teaches: *hear one deeply → hear the many → return to one to
   make sure the many are still people.*
5. **One honest limit, shown in code.** Find a place the tools mislead — a vague topic, a sentiment score
   you distrust (sarcasm?), an empty/fragment document — and show how you'd check it by hand.

**On borrowed code (it's expected).** VADER, Gensim, `Counter`, pandas — almost nobody writes these from
scratch; you *use* them through their interface. Borrowing a tool, a Stack Overflow snippet, or AI-written
code is normal practice in this course. The rule is **understanding, not avoidance**: you should be able
to explain any code you submit, and you should **note in a `#comment` where you used AI and what you
changed.** (See the syllabus AI policy.)

---

## The essay — your data-driven opinion

About **800–1,200 words** (a guide, not a quota — this is ungrading). Argue **one claim** about your text,
grounded in specifics from your notebook: name a word that won by frequency, a topic and its label, an
average sentiment, an individual comment you read closely. The essay is where the *opinion* in
"data-driven opinion" lives — the numbers are your evidence, not your conclusion.

Hold yourself to the course's standard:

> **Give voice to the people in your data — including their disagreements — and show where your tools
> risked flattening them. Did your analysis sail calmly on, or did it make someone look?**

Concretely, a strong essay:
- **Makes an argument**, not a summary. You chose this reading; own it. ("Let the data speak for itself"
  is a trap — data never speaks; *you* speak, having chosen.)
- **Preserves the quarrel.** If your crowd is split, say so — don't let a near-zero average sentiment
  report a false calm over a real fight. The disagreement is the signal, not noise to average away.
- **Names its limits.** What did your method flatten or miss? Where would you distrust your own result?
  Naming this *strengthens* the essay — it's the honesty the whole course is about.
- **Connects to the stakes.** Why does hearing these voices, at this scale, matter? *(Track B: what does
  it mean that AI writing has a measurable "average" — and what's lost when a voice regresses to it?)*

**Write it in your own voice.** Your reflections, `#comments`, and this essay are where you *become a
writer.* You may use AI to help with code and even for feedback on a draft — but **the writing itself
must be yours.** A unique voice is forged in the difficulty of finding your own words; outsourcing that
forfeits the one thing the tools can't give back.

---

## The presentation *(last day, Fri 7/31)*

A short, low-stakes share (~`[3–5]` minutes): your dataset and question, **one finding**, and **one thing
your method got wrong.** No slides required — walk us through a cell or two of your notebook. This mirrors
the Week-4 discussion (D4): what computation reveals *and* hides.

---

## Timeline

| When | What | Due |
|---|---|---|
| **Mon 7/27** (Day 16) | Integration demo + stylometry demo in class | **Proposal due** |
| **Tue 7/28** (Day 17) | "Being wrong as learning" · capstone framing; validation | HW4 due |
| **Wed 7/29** (Day 18) | Capstone work session 1 (with support) | — |
| **Thu 7/30** (Day 19) | Capstone work session 2 + **peer review** | — |
| **Fri 7/31** (Day 20) | **Capstone presentations** + course wrap | **Capstone due** · **R3 due** |

### The proposal (due Mon 7/27)
One short paragraph — really an expanded version of your **HW4 C2** plan. Tell me:
- **which dataset** (your own, ideally — or the provided corpus / a stylometry corpus);
- **your question** — the humanistic question you're actually curious about;
- **which lenses** (frequency / sentiment / topics — or the stylometry measures) you expect to use, and why;
- **one limitation** you already know you'll have to be honest about.

The proposal isn't a contract — questions shift once you're in the data, and that's fine. It exists so I
can point you somewhere useful before the work sessions.

---

## How it's evaluated (ungrading)

Like everything in this course, the capstone is marked on the **3-point scale** — for **engagement,
reflection, and growth**, not for whether your code or analysis came out "right." A finding that didn't
hold up, paired with a clear account of what you tried and learned, **meets expectations.** This is the
course's most heavily weighted single piece in the final holistic judgment (see the syllabus), so it's
worth your real effort — but "effort" here means honest thinking made visible, not polish.

- **3 — Exceeds:** integrates the lenses into a genuine argument; returns to individual voices; names its
  own limits with insight; takes an intellectual risk.
- **2 — Meets** *(the expected standard, and a success)*: does the analysis with honest engagement, draws
  a grounded claim, and is candid about at least one thing the tools got wrong.
- **1 — Not yet:** missing, minimal, or a summary with no argument and no reckoning with limits.

**TCU Core (CSV).** The capstone is the central piece of evidence for this course's **Citizenship &
Social Values** credit: forming, arguing, and reflecting on an **evidence-based opinion about a real
public debate**, while representing the values and voices of a community in disagreement responsibly.

---

## Submit checklist

Before you turn in your notebook + essay `[to: upload location / TCU Online]`:

- [ ] My notebook loads my data, runs **at least two** of the three lenses, and **brings them together**.
- [ ] I **returned to individual texts** by hand (close → distant → close) — not just the aggregate.
- [ ] I named **at least one limit** — a place my tools mislead — and showed how I'd check it.
- [ ] I used **`#comments` frequently and meaningfully** — wherever a choice or question came up (not
      every line, but throughout) — and noted **where I used AI** and what I changed.
- [ ] I **ran every cell.** Where something still breaks, I left a `#comment` about what I tried and what
      I learned — **errors are part of the work here, not something to hide or delete.**
- [ ] My essay (~800–1,200 words) makes **one argument**, grounded in specifics from the notebook,
      **preserves any disagreement** in my data, and is honest about what my method flattens.
- [ ] The **writing is my own voice** (AI for code and feedback is fine; the prose is mine).
- [ ] I'm ready to share **one finding and one thing my tools got wrong** in class on Fri 7/31.

---

*This assignment is a working plan and may be adjusted to fit the class's pace; any changes are announced
in class and on TCU Online.*
