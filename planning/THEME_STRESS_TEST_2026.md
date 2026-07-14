# WRIT 20833 — Theme Stress Test (2026)
### Nine plausible holes in the course's conceptual through-line, argued in good faith

> **Status: devil's-advocate document (2026-07-14).** A deliberate adversarial pass at the
> theme as it stands after the amathia / eloquence-is-not-evidence / "American people feel…"
> additions (see `CONCEPTUAL_FRAMEWORK_2026.md` §4). These are the objections a skeptical
> colleague, a sharp sophomore, or a curriculum reviewer could raise. Each entry: the
> objection, why it bites, a candidate patch, and a status. None is judged fatal; ranked
> assessment at the end. Treat open items as revision targets, not settled flaws.

---

## 1. The corpus falsifies the premise *(consistency — patchable)*

**Objection.** The guiding question is "how do we hear human voices *at a scale no person
could read by hand*" — and the corpus is 123 YouTube comments. A student can close-read all
123 in an hour. Every "scale" claim in the course is therefore simulated: the flattening
dangers are real in principle but staged in practice, and for this corpus distant reading is
demonstrably *worse* than the available alternative (just reading them). The stadium
metaphor sits atop a dinner party's worth of data.

**Candidate patch.** Own it explicitly and early: the 123 are a *training corpus* — small
enough that students can verify every computational claim by hand, which is precisely the
pedagogy (close → distant → close needs a corpus where the close reading is possible). Say
in ML0 or the Day-1 framing: "this corpus is small on purpose; the methods are what scale."
The honesty costs one sentence and defuses the smartest objection in the room.

**Status: open.**

## 2. The course's own trope critique applies to the course *(consistency — patchable)*

**Objection.** The "American people feel…" material teaches students to preserve the split
*within* the sample — but the trope's deeper sin is the *unrepresentative sample dressed as
a population*. The 123 are self-selected, platform-ranked, moderation-filtered voices;
"the crowd" is whatever YouTube's sorting surfaced on one summer day. Even a scrupulously
split-aware capstone sentence ("the commenters were divided 60/40") quietly overclaims:
*which* commenters? Who never commented? What did the ranking bury? The pipeline covers
this in principle (phenomena → raw), but the trope material doesn't cash it out, so the
drafting test can be passed while committing the trope's worst version.

**Candidate patch.** Extend the drafting test one clause: not just "say split," but "say
*who you heard*" — every crowd-claim names its sample ("of the 123 comments YouTube
surfaced…"). One line in ML9 and HW3 B4; it also strengthens the ML6 Data Archaeology tie.

**Status: open.**

## 3. "Bias is constitutive" has no floor under it *(structural — the week-2 question)*

**Objection.** If there is no clean signal anywhere and every arrow is a choice, what makes
one analysis *better* than another? The course's stated standard — "make your choices
visible" — concerns honesty, not validity. A student who annotates every biased choice with
a candid `#comment` has met the standard while potentially producing garbage. The theme
names dishonest confidence but never says what *earned* confidence looks like. Worst-case
exit state: sophisticated relativism ("it's all interpretation anyway") — the exact opposite
of a data-driven opinion, reached through the course's own logic.

**Candidate patch.** The course actually has the raw materials for an answer and hasn't
assembled it: convergence (freq + sentiment + topics agreeing — the Day 18 integration),
survival of close-reading spot-checks (the human-vs-VADER exercise), robustness (the
"change the 0.05 cutoff and see what moves" experiment), and adversarial honesty (naming
what would falsify you). That's a teachable four-part test for "earned insight" — arguably
*the* missing §4½ of the framework. Deserves a named home ("visible ≠ valid; here's what
valid looks like at our scale").

**Status: open — highest priority.**

## 4. The refrains are eloquence *(structural — Goodhart risk)*

**Objection.** "The score is never the meaning." "Eloquence is not evidence." "Preserve the
quarrel." "Say split." Polished, feel-true, low-friction slogans — optimized for exactly the
cognitive channel the course says to distrust. Under ungrading, the reward signal is
reflective *engagement*, and students will learn to produce fluent humility-boilerplate
("I must ask what my analysis flattens…") the way they learn any rubric: the course training
the *rhetoric* of wisdom without the substance — amathia with better vocabulary,
manufactured in-house. The D4 prompt now literally invites a confession genre ("a moment
you trusted a result because it sounded right"), which Goodhart's law converts into
performance.

**Candidate patch.** Grade the *artifact*, not the confession: feedback (and the 3-point
scale's "meets expectations") should key to whether the reflection changed something
checkable — a rerun cell, a revised cutoff, a corrected claim — not to the quality of the
self-critique prose. One sentence in the ungrading rubric ("a reflection counts when it
leaves a mark on the notebook") plus instructor discipline in feedback. Cannot be fully
patched in text; this is a grading-practice risk to monitor.

**Status: open — mitigable, not closable.**

## 5. The reflexive rule is asserted, not argued — and asymmetric *(calibration)*

**Objection.** The materials say amathia points at us, never at the commenters. But the
course's entire apparatus *diagnoses the commenters*: VADER scores their feelings, LDA sorts
their concerns, HW3 labels each person "positive" or "negative." Why is computationally
labeling a stranger's emotional state acceptable while judging their wisdom is forbidden?
Stipulated rules about potent words don't survive contact with sophomores; the term *will*
be aimed at the other side, and the course has no prepared move for when it happens out loud.

**Candidate patch.** Give the rule its missing argument (one paragraph, framework §4): the
sentiment/topic labels are *provisional artifacts of a method*, held loosely and checked
against close reading — the course spends whole assignments teaching students to distrust
them. "Amathic" is a *verdict on a person's character* with no check and no appeal. The
asymmetry is between labels-we-audit and verdicts-we-can't. Also script the classroom move:
when a student applies the term to a commenter, the response is the HW3 human-vs-VADER
exercise in miniature — "what would it take to be wrong about that?"

**Status: open.**

## 6. The Frankfurt claim is taught as more settled than it is *(calibration)*

**Objection.** "In Frankfurt's strict sense, an LLM is a bullshit engine" — but Frankfurt's
bullshitter *has intentions* (indifference to truth is a stance an agent takes), and whether
intention-laden categories apply to a text generator is precisely what's contested about
Hicks, Humphries & Slater (2024). ML4 currently hedges ("some philosophers now argue") and
then builds on the claim as established. The available irony: the course adopted the claim
partly because "ChatGPT Is Bullshit" is a memorable, eloquent title. Same overreach in the
"fluency was a costly signal until LLMs" story — ghostwriters, sophists, advertisers, and
propaganda mills made fluency cheap for centuries; LLMs automated an already-broken
heuristic. The tidy three-years-ago periodization *feels* true, which should worry a course
with this theme.

**Candidate patch.** Two small wording moves in ML4: (a) keep the Frankfurt frame but
mark it as a live argument ("whether a system with no intentions can bullshit is itself
philosophically contested — which is a fine seminar question"); (b) soften the history to
"fluency was *usually* expensive, and never this cheap, this uniform, or this available to
everyone at once" — the scale-and-access point survives; the false periodization doesn't.

**Status: open.**

## 7. Code-is-rhetoric contradicts nobody's-voice-lives-in-a-stopword-list *(consistency — patchable)*

**Objection.** The course's foundational thesis (ML1; the harvested Code-as-Rhetoric
material) is that every technical choice *argues* — code encodes values, classification is
authored, structure is rhetoric. ML4's borrow-freely rule rests on the opposite premise:
code is voiceless plumbing, so outsourcing it costs nothing. Both cannot be fully true. If
the stopword list is an argument (HW2 insists it is), then accepting an AI's stopword list
*is* letting the AI argue for you — the ventriloquism the course forbids for prose.

**Candidate patch.** Restate the ML4 line as **audit-and-own vs. constitutive**: borrow
freely anything you can fully audit, explain, and take responsibility for (code, once
understood, is yours in the way a quoted source is yours); never outsource what constitutes
you (the interpretive voice that can't be audited into existence). The prose/code split is a
useful *approximation* of that line, not the line itself — and the `#comment` requirement is
already the audit trail. This is a two-sentence fix that makes ML1 and ML4 allies instead of
contradictions.

**Status: open.**

## 8. Stakes inflation at the moral floor *(calibration)*

**Objection.** Auden and Brueghel are about attending to *suffering* — a drowning boy, the
ploughman's indifference. The corpus is a policy disagreement about classroom décor in which
both camps are vocally, publicly engaged; nobody in it is occluded the way Icarus is.
Importing the moral-attention frame wholesale teaches students to dramatize: every notebook
a small rescue mission, every `mean()` a potential moral failure. Predictable responses:
cynicism, or the performed solemnity of hole #4. Applied weekly, the moral floor
depreciates.

**Candidate patch.** Scope the moral floor explicitly: it is the *gravest case* for what
the tools are for, not the description of every use. One sentence where Auden is taught:
"our corpus is a quarrel, not a tragedy — the moral floor is where these methods can
ultimately point, not where this homework lives." Reserve the full frame for the capstone
framing and the CSV outcomes, where the stakes claim is doing licensed work.

**Status: open.**

## 9. "Data-driven opinion" vs. "preserve the quarrel" gives no exit *(structural — shares a fix with #3)*

**Objection.** The capstone requires taking a position; the theme forbids tidy verdicts and
warns that resolving the quarrel is flattening. The materials never say when a verdict is
*earned* — what evidence-plus-honesty threshold licenses a student to stop preserving and
start concluding. The predictable eight-week resolution is hedge-everything both-sides-ism:
manufactured false *equivalence*, the mirror twin of manufactured consensus, and equally a
failure to hear the crowd.

**Candidate patch.** Same missing piece as #3: a stated standard for earned conclusions.
Minimal version for ML9/capstone framing: "preserving the quarrel means your *description*
of the crowd keeps its disagreement; it does not mean your *argument* has no spine. You may
conclude — you must conclude — once you can show what you counted, what you left out, and
what would change your mind." Distinguish description-claims (must preserve) from
position-claims (must be owned).

**Status: open.**

---

## Ranked assessment

- **Structural risks — #3 and #4.** The theme currently cannot distinguish earned insight
  from well-documented bias (#3), and its own refrains can game its own reward system (#4).
  #3 is the question a smart student asks in week 2; it deserves the first patch (a named
  "what earned looks like" standard, which also closes most of #9).
- **Internal-consistency holes with straightforward patches — #1, #2, #7.** Own the
  toy-corpus honestly; extend the trope critique to sampling ("say who you heard"); restate
  the borrow rule as audit-and-own. Each is a one-to-two-sentence fix.
- **Calibration problems — #5, #6, #8 (and #9's tone).** A sentence or two of added
  humility or explicit argument closes each; none threatens the architecture.

None of the nine kills the theme. Collectively they argue the theme's next revision should
add one thing above all: **a positive epistemology to match its negative one** — the course
is rich in how analyses go wrong and thin on what makes one right enough to act on.

---

## Related documents
- `CONCEPTUAL_FRAMEWORK_2026.md` — the through-line these objections target (esp. §1, §4).
- `materials/lectures/ml0.md`, `ml4.md`, `ml9.md` — where patches #1, #6/#7, #2/#9 would land.
- `notebooks/homework/WRIT20833_HW3_2026.ipynb` (B4) — where patch #2's "say who you heard" would land.
- `WORKLOG.md` — decision log, if/when any patch is adopted.
