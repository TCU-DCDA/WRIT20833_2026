# Stylometry Unit — Next Steps

*Companion to `stylometry_unit_outline.md`. Picks up where the planning conversation paused.*

---

## Where things stand

The unit's shape is settled:

- 2-week unit, ~4 sessions, late semester
- Pandas-forward, Colab-based, no regex
- Hybrid exploratory/forensic framing
- Student-assembled corpus (6–8 short essays, matched pairs, mixed genres)
- Instructor-prepared mystery texts (3 difficulty levels + false-positive case) plus peer-contributed pool
- Two ungraded deliverables: methods notebook (mid-unit) and reflection notebook (end)
- Solo build → paired stress-test → solo argument
- Spine: tool not oracle. Threads: what appeals about AI writing; writing better with AI; bias through analyst's feature choices.

What's *not* yet done: any of the concrete artifacts students or instructor would actually use.

---

## Open items, roughly grouped

### Decisions still to make

- **Corpus pooling model** — opt-in, anonymized, two-tier, or other. Decide by end of Session 1.
- **Homework cadence** — what happens between sessions vs. in-class.
- **D2 format** — single combined notebook, or notebook + companion essay?
- **When pairs are formed for Session 4** — likely end of Session 2 or start of Session 3.
- **Peer-contributed mystery logistics** — pool with sealed answers, paired exchange, or other structure.
- **Whether to add an explicit AI-detector demo** to Session 4 (running mystery texts through GPTZero, Turnitin's detector, or similar) as a real-world reference point for the false-positive discussion.

### Artifacts to draft

These are the concrete things the unit needs in order to actually run. Roughly in order of dependency:

1. **Session 1 reflective writing prompt** — "what do you value about AI writing?" framing. Short, open, parked for later return. Probably the easiest to draft and the foundation for the unit's *what appeals* thread.
2. **Feature lists** — starter lexical, syntactic, structural, and negative-space features. Some prescribed, some left for student proposal. Worth deciding which are mandatory vs. invitational.
3. **Mystery text design and preparation** — the four instructor-prepared texts plus documentation (prompts, generation settings, edit logs, estimated human/Claude ratios). Time-intensive; worth budgeting a few hours.
4. **Assignment prompts** — actual language for D1 and D2, in whatever WRIT 20833 house style is appropriate.
5. **Reflection prompts for D2** — the questions students respond to in the essay-section. Sharper than the assignment prompt itself; carries much of the unit's interpretive weight.
6. **Session 1 readings** — Federalist/Galbraith framing materials, possibly excerpts from the source PDF, possibly a short piece on computational authorship attribution.
7. **Starter Colab notebook(s)** — at minimum, a scaffolded notebook for Session 2 that loads a corpus into pandas and computes a couple of example features, so students can extend rather than start from zero.

### Loose ends to think about

- **How does this unit get introduced relative to what came before?** The transition from whatever the previous unit was into "now we're doing stylometry" matters for whether students arrive curious or confused.
- **Whether any reading or discussion happens *before* Session 1** — a pre-unit reading could front-load the conceptual frame and free Session 1 for more corpus-assembly time.
- **How the unit closes** — is there a beyond-D2 moment? A class discussion, a connection forward to whatever closes the semester, a brief "what would you do differently with another two weeks" prompt?
- **Whether the unit's lessons should be made explicit anywhere as bullet-pointed takeaways**, or whether keeping them latent is more honest to the humanities approach.

---

## Possible next-session directions

When picking this back up, several natural starting points — in no particular order:

- **Start with the Session 1 reflective writing prompt.** Small, contained, and it anchors the *what appeals* thread for the whole unit. Good warm-up.
- **Start with feature lists.** The most code-adjacent piece, and the one that most determines what Sessions 2–3 look like in practice. If you want to mentally walk through what students will actually be doing in those sessions, this is where to start.
- **Start with mystery text design.** The most time-intensive and most consequential single artifact. Doing it first lets the rest of the unit be designed *toward* the mystery texts rather than backfilling them at the end.
- **Start with assignment prompts.** Once written, they constrain the rest of the artifacts in useful ways. But probably best done after at least one of the above is settled, since the prompts will be more concrete with one example in hand.
- **Start with the Session 1 readings.** If there's reading to assign, students need lead time, and this is independent of most other decisions.

If picking just one: **the Session 1 reflective writing prompt** is the smallest and most generative starting point. It's quick to draft, doesn't depend on other decisions, and once written, it clarifies what the unit's *what appeals* thread is actually asking students to do — which makes the other artifacts easier to write.

---

## Useful context to recover quickly

If returning to this after a long pause, the most efficient re-entry is:

1. Reread the *Unit framing* section of `stylometry_unit_outline.md` (spine and three threads).
2. Reread the *Session 4* section and the *Mystery text difficulty ladder* — the unit's intellectual payoff sits there, and most downstream design decisions point toward it.
3. Skim the *Assignment sketches* for the collaboration shape (solo → paired → solo) and the ungraded framing rationale.

Everything else is downstream of those three pieces.
