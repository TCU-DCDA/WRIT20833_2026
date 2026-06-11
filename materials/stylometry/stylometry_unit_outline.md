# Stylometry Unit — WRIT 20833 (Intro to Python in the Humanities)

*A 2-week unit on stylometry as a method for examining AI-assisted writing.*

---

## Unit framing

### Spine

**Quantitative method is a tool, not an oracle.** The unit teaches students to build a small stylometric classifier and then to discover, through their own work, what it can and cannot reliably do. The exercise is not "learn to detect AI"; it is "learn what happens when we try."

### Secondary threads (woven throughout)

- **What appeals to us about AI when it comes to writing?** Why is Claude's smoothness seductive? What does it give us — confidence, fluency, getting unstuck, a sense of competence? Worth examining directly rather than treating as background noise.
- **How could we write better with AI as positive and negative example?** Seeing what Claude does well and what it flattens becomes a mirror for students' own stylistic choices. The contrast sharpens their sense of voice, register, and texture.
- **Bias enters through the analyst's feature choices.** When students decide which features matter, they encode beliefs about what Claude sounds like. Those beliefs get operationalized into a tool that then judges other texts. This is continuous with the course's existing frame: the coder's assumptions sneak into the tool (the M/F dropdown problem), often invisibly, with real consequences. The bias moment lands *after* students' classifiers fail, so the realization comes through their own work rather than as pre-loaded critique.

### What the unit deliberately resists

The "you can catch AI writing" framing. Students will arrive expecting that; the unit reframes early and explicitly: this is not a tutorial in building an AI detector. Real ones exist, they are unreliable, and the unit will show why from the inside.

---

## Design parameters (settled)

- **Position in course:** late semester, after pandas has had its deep dive
- **Duration:** 2 weeks, roughly 4 class sessions plus homework
- **Coding skills assumed:** file I/O, lists/dicts/loops/functions, string methods, `collections.Counter`, pandas DataFrames. *No regex* — the unit is designed around its absence.
- **Environment:** Google Colab notebooks
- **Tokenization approach:** approximate (split on `.!?` for sentences, whitespace for words). The failure cases ("Dr.", "...", etc.) are themselves teachable.
- **Corpus per student:** 6–8 short essays, 300–800 words each, with at least one matched pair (same prompt, human and Claude versions). Mixed genres encouraged.
- **Corpus pooling model:** flexible — decided by end of Session 1 based on class composition and consent. Likely candidates: opt-in pooling, anonymized pooling, or two-tier (private + small shared).
- **Mystery texts:** instructor-prepared (3 difficulty levels + a false-positive case) plus peer-contributed pool. Instructor maintains documentation of generation/editing process for each instructor-prepared text, used at the reveal.
- **Framing of the exercise:** hybrid — exploratory in sessions 2–3 (build features, characterize corpus), forensic in session 4 (apply method to mystery texts).

---

## Session-by-session outline

### Session 1 — Framing and corpus assembly

**Spine work:** introduce stylometry as a humanities method with real history (Federalist Papers, Galbraith/Rowling), but also as a method with known failure modes. Position the unit as *building a small classifier to see what it can and can't do*, not *learning to detect AI*.

**Threads:** open the "what appeals to us about AI writing?" conversation early, before any analysis. Discussion prompt or short reflective writing: what do students value when they use Claude — confidence, fluency, getting unstuck, a sense of competence, something to push against? Park those answers; they return in session 4.

**Practical work:** students commit to their corpus. 6–8 short texts, 300–800 words each, at least one matched pair. Discussion of the corpus-pooling question — what students are comfortable contributing, what stays private. Light norm-setting around consent.

**Setup for next session:** by end of session 1, students have a Drive folder with their texts as `.txt` files, named consistently, and a small CSV/sheet logging metadata (author, source, genre, prompt, word count).

### Session 2 — Feature building in pandas (lexical and syntactic)

**Spine work:** the technical heart. Students load their corpus into a DataFrame, one row per text. Compute and add columns for a starter set of lexical and syntactic features. Start to see distributions.

**Likely features at this stage:**

- Word count, sentence count (approximate split on `.!?`), mean sentence length, sentence-length variance
- Type-token ratio (with the length caveat surfaced explicitly — a teachable moment about what TTR does and doesn't measure)
- Function word frequencies (a small list: *the, of, and, to, a, in, that, is, it, for, with, as, but*)
- Hedge-word frequency (a small list students can debate: *might, perhaps, often, generally, tends to, it's worth noting, importantly*)
- Punctuation ratios — em-dashes per 1000 words, semicolons, parenthetical asides
- Optional: a list of "Claude tells" students propose collectively (*delve, tapestry, navigate, robust, leverage, multifaceted*)

**Threads:** the *what appeals* thread comes in lightly — "hedge words feel polite and considered; that's part of what makes Claude sound trustworthy."

**Output:** a DataFrame with one row per text, ~10–15 feature columns. Students start comparing their human vs. Claude rows informally — eyeballing differences.

### Session 3 — Structural and negative-space features, plus comparison

**Spine work:** extend the feature set into structural territory (list presence, header presence, paragraph length consistency, presence of a summary/wrap-up sentence) and negative-space territory (absence of typos, absence of sentence fragments, absence of idiosyncratic punctuation, absence of colloquialisms). Use pandas `groupby` to compare human vs. Claude distributions across the whole class corpus (if pooled) or within each student's corpus.

**Methodological work:** students articulate a *method* — a small set of features they'd weight most heavily to classify an unknown text. This is effectively building a tiny classifier, but by hand and with explicit reasoning rather than via ML. Each student writes down their attribution rule, e.g., *"If hedge-word frequency is above X and em-dash density is above Y and there are no sentence fragments, I'd call it Claude."*

**Threads:** the *writing-better* thread starts to surface — students notice what their human writing has that Claude's doesn't, and vice versa. The bias thread is not yet explicit; it's being set up.

**Pivot moment, end of session:** "Next session, we test your method against texts where you don't know the answer."

### Session 4 — Mystery texts, failure analysis, and reflection

**Spine work:** students apply their methods to the mystery texts (instructor-prepared at three difficulty levels, plus the false-positive case, plus peer-contributed). They commit to attributions *in writing* before the reveal.

**The reveal:** the instructor shares what each text actually is, with documentation — original prompt, generation settings, edit log, estimated human/Claude ratio. The conversation centers on *where methods failed and why*.

**Threads converge:**

- *Tool-not-oracle:* methods that worked on training corpus failed on edge cases. Quantification narrows perception even as it sharpens it.
- *What appeals:* the human-edited Claude text is interesting precisely because it kept what Claude gave (scaffolding, fluency) and added what Claude lacks (compression, idiom, situated specificity). That's the productive collaboration shape.
- *Writing-better:* the texture the human editor added — "structural tic," "gave it away" — is exactly the kind of move students can practice in their own writing. Claude's drafts make the value of human texture visible by contrast.
- *Bias:* on the false-positive case especially — where formal human writing got classified as Claude — students examine *what assumptions they baked into their feature choices*. The M/F dropdown analogy gets named here. The connection to commercial AI detectors and academic-integrity tools gets made.

**Reflection writing or notebook-as-essay:** students produce a final artifact arguing what their method showed, what it missed, and what they now think about quantitative stylometric detection. Hedged, situated, methodologically honest.

---

## Mystery text difficulty ladder

1. **Easy:** raw Claude output, no editing
2. **Medium:** Claude draft with sentence-level edits (word swaps, light rephrasing)
3. **Hard:** Claude scaffolding with substantial human texture inserted (the case the source PDF analyzes)
4. **False-positive check:** fully human text that *reads* AI-ish (formal, hedged, listy). Pedagogically critical — tests whether students' methods detect Claude or just detect "smoothness."

For each instructor-prepared mystery, maintain documentation: original prompt, generation model/settings, edit log (what was changed and why), estimated human/Claude ratio. This documentation becomes the teaching artifact at the reveal — students see not just "the answer" but the *process* of human-AI collaboration that produced the text.

---

## Decisions made

- **Unit length:** 2 weeks, ~4 sessions
- **Coding level:** later in semester; pandas-forward; no regex
- **Environment:** Colab
- **"Claude-ness" features to address:** all four categories on the table — lexical, syntactic, structural, negative-space — sequenced across sessions 2–3
- **Framing:** hybrid exploratory/forensic
- **Corpus:** 6–8 texts per student, 300–800 words, mixed genres, at least one matched pair, drawn from WRIT 20833 work and other coursework
- **Mystery texts:** instructor-prepared + peer-contributed combination; instructor prepares 3 difficulty levels plus false-positive case
- **Primary takeaway:** tool not oracle
- **Secondary takeaways:** what appeals about AI writing; writing better with AI as positive/negative example
- **Bias frame:** continuous with existing course frame (analyst's choices encode assumptions, à la the M/F dropdown); surfaces *after* classifier failure, not before

## Still open

- **Corpus pooling model** — opt-in, anonymized, two-tier, or other. Decide by end of Session 1 based on class composition.
- **Homework cadence** — what work happens between sessions vs. in-class. Depends on actual class meeting pattern.
- **Specific feature lists** — the lists above are illustrative starting points, not prescriptions. Final selection may shift based on what's surfaced during the unit.
- **Assignment language and rubric** — not yet drafted. Rubric likely needs to span technical execution, interpretive argument, methodological hedging, and engagement with the broader question.
- **Whether peer-contributed mysteries go into a pool with sealed answers, or are exchanged in pairs, or some other structure.**
- **Specific readings for Session 1** — Federalist/Galbraith framing materials, possibly excerpts from the source PDF or a short piece on computational authorship attribution.

---

## Source material referenced in planning

- ChatGPT analysis of a Claude-derived email passage (the "AI writing, voice, and style analysis" PDF) — useful as illustrative reading for Session 1 and/or as the hard-case mystery text in Session 4.
