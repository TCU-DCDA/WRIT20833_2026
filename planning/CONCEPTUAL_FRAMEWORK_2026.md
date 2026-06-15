# WRIT 20833 — Conceptual Framework (2026)
### The intellectual through-line of "When Coding Meets Culture"

This is the **canonical statement** of the course's unifying ideas — the *why* beneath the Python, the
pandas, and the homeworks. It is the reference for authoring lectures, the syllabus, and the capstone,
and the place a future session should read to understand what the course is *about*.

> **A note on audience.** This document is the **instructor's framing**. How much of its vocabulary
> reaches students explicitly (Kant, "noumena," etc.) is a deliberate design dial, flagged in §6. The
> *ideas* are already enacted in every homework; the question is only how loudly to name them.

The course teaches three computational methods — **term frequency, sentiment analysis, topic
modeling** — but its real subject is a single humanistic problem: **how do we attend to human voices at
a scale no person could read by hand, without flattening the humans out of view?** Everything below is
one elaboration of that question.

---

## 1. The epistemological spine — noumena → wisdom

The course's founding image (`materials/images/noumena_to_wisdom_pipeline.png`) is an eight-stage
pipeline:

> **NOUMENA → PHENOMENA → RAW DATA → STRUCTURED DATA → ANALYZED DATA → INSIGHT → KNOWLEDGE → WISDOM**

It extends the classic **DIKW** pyramid (Data → Information → Knowledge → Wisdom) *backward* into Kantian
epistemology. *Noumena* is the thing **as it actually is, in itself** — the whole, lived human fact.
*Phenomena* is the thing **as it appears to us**, already filtered through perception and language. We
never reach the noumenon; we only ever work with appearances, and then with appearances of appearances.

**Concretely:** a person reads about a law and feels something whole and hers (the *noumenon*). We will
never have that. We have what she *typed* — a comment (a *phenomenon*) — then what we *scraped*, *cleaned*,
and *modeled*. By the time a result reaches a notebook, it sits seven steps downstream of the human.

### Every arrow is a human decision — bias is *constitutive*, not "contaminating"
It is tempting to call each step *contamination*, as if a clean signal up top gets dirtied on the way
down. The diagram says otherwise: **there is no clean signal up top.** The first step is already an
interpretation, and every step inherits the choices before it. So bias doesn't *sneak into* pure data —
**bias is the material the data is made of.** The honest response is not to chase a truth you can't have;
it is to **make every choice visible** (the `#comments` requirement and the reflections train exactly
this). One-line version: **the score is never the meaning.**

Every arrow already has a home in the built materials:

| Transition | The choice that enters | Where the course shows it |
|---|---|---|
| Noumena → Phenomena | What is even *noticed* worth studying | Choosing *this* law / *these* commenters; ML0 "the mess" |
| Phenomena → Raw data | Collection: captured vs. excluded | Day 8 Data Archaeology + scraping ethics; the wrap-fragments are capture artifacts |
| Raw → Structured | Cleaning, tokenizing, what is a "row" | HW2 stopwords (authored deletion); HW3 "clean *but keep* punctuation"; the 123-vs-93 decision |
| Structured → Analyzed | Method + parameters | HW3 VADER lexicon + the 0.05 cutoff; HW4 `num_topics`, `random_state` |
| Analyzed → Insight | What we read into the output | HW4 "the *human* names the topics"; the sarcasm misread; B3/B4 |
| Insight → Knowledge | Generalizing; confirmation bias | HW4 "name where the tools mislead"; "being wrong as learning" (Day 17) |
| Knowledge → Wisdom | Values — what we *do* with it | The capstone data-driven-opinion essay; ML9 "Going Public" |

The **left column** is "the score is not the meaning"; the **right column** is ungrading's "earned
insight." (Full graphic notes: `materials/images/README.md`. Day-1 teaching passage:
`materials/Day1_Framing_Noumena_to_Wisdom.md`.)

---

## 2. The through-line — "hear the human at scale"

The *why* beneath the subtitle "Developing Data-Driven Opinions." **We collect textual data, in part, to
hear the human at scale** — to listen to more people than close reading ever could. This reconciles the
contradiction the course keeps staging (computation *flattens* voices vs. *empowers* them): **the
flattening is the price of the scale, and the scale is the point.** Distant reading is not *not* reading
humans — it is hearing humans you'd otherwise never hear.

**Listen vs. extract (the governing metaphor — and a teachable enemy).** "Hear / listen" stands against
the verbs that dominate data culture — *mine, scrape, harvest, crawl.* Those treat people as ore; "hear"
presumes someone with something to say and a duty to receive it. It reframes the ethics of collection
(Day 8) from *"is this allowed?"* to **"am I listening, or extracting?"**

The through-line has **three movements**:

### (a) Hear the human — the voices *in* the data
Term frequency, sentiment, and topic modeling are listening instruments. The reason to tolerate reducing
a person to a word-count or a polarity score is that it lets you hear the **chorus** — what hundreds or
thousands of people are collectively saying — which gut instinct cannot.

### (b) Hear the *mess* — the inevitable quarrels (tie to ML0)
ML0 frames the humanities as "studying the mess of the human condition" — contradiction, ambiguity,
subjectivity — which they **explore rather than tidy up.** But every scale tool *wants* a tidy answer: a
single mean sentiment, one "winning" word, a dominant topic. So the deepest danger is not only going deaf
to the individual — it is **manufacturing a false consensus that silences the quarrel.** To hear the
human is to hear them *disagreeing*; the disagreement is not noise to average away — **it is the signal.**
The course already enacts *preserve the quarrel*:
- HW3's near-zero **mean sentiment (0.082)** is a *split* crowd, not neutrality — the average nearly
  erased the fight.
- HW2 → HW3's **`commandments` topping both camps** is a quarrel hiding inside a frequency "winner."
- HW4's **sentiment-by-topic** exposes sub-quarrels.
- **Reading the extremes**, the **human-vs-VADER check**, and **"the human names the topics"** are all
  *returning to the individual to confirm you can still hear a person — and still hear the disagreement.*

The **close → distant → close** arc, restated: hear one deeply → hear the many → go back to one to make
sure the many are still people in conflict, not a manufactured consensus.

### (c) Remain a human voice yourself — writing in the age of AI
The movement that makes this a **writing** course. You must *remain* a human voice to do justice to the
voices you hear. **Letting AI write for us forfeits the opportunity — available only through the
difficulty — of developing a unique voice.** Voice is forged in the friction of finding words; remove the
friction and you remove the forging.
- **The asymmetry of borrowing (a core literacy).** Borrowing the *tool* (code) is expected and fine —
  nobody's voice lives in a stopword list; borrow the utility, *understand and judge* it (the
  borrowed-code convention). Borrowing the *voice* (writing) is self-erasure. The course teaches both
  coding-with-AI and writing, so it is built to teach the discernment: **borrow the tool, never outsource
  the voice — and know which is which.**
- **The exact parallel — the same lesson, turned on the self.** AI-generated prose : your voice ::
  **mean sentiment : the crowd's quarrel** — a flattening of the particular into a statistical average, a
  *false consensus* that silences what's specific. The model writes the mean of all writing; a unique
  voice is its opposite. The whole apparatus the course builds against false consensus *in the data*
  applies, unchanged, to your own *writing*: **resist the flattening — of others, and of yourself.**
- Aligns with **ungrading** (credits struggle/labor/reflection over polish — the difficulty *is* the
  point) and refines the syllabus **AI-use policy**: AI is fine for code-you-understand and for feedback,
  but **generating the writing itself forfeits the voice the course exists to develop.**

### The two referents of "voice"
1. The people **in** the data — protect from flattening/misrepresentation, empower by making audible at
   scale (the home for the orphaned mini-lecture **ML9 "Going Public"**).
2. The student's **own** voice — ungrading, `#comments`, and the reflections keep the learner a
   person-on-the-record, not a number. The course empowers voice *by example.*

**This secures both halves of "data-driven opinion."** It ties the **ethics** (voice) to the
**epistemics** (evidence): a data-driven opinion earns the right to drive only when the data has been
*heard*, not merely processed.

**Keep the edge.** Pair "empower" with discipline. The failure mode is "let the data speak for itself" —
it never speaks; *you* speak, having chosen. Hearing at scale is using a megaphone that distorts: amplify
the signal, own the distortion, and don't resolve a quarrel the data didn't resolve.

---

## 3. Scale, vantage, and what is "flattened from view"

### The dinner-party / stadium illustration *(canonical for Day 12, close vs. distant)*
A guest at a 12-person dinner notices a couple he just met bickering at the end of the table — a nuance
he can observe. The *same* guest, watching the *same* couple from across AT&T Stadium at a Cowboys game,
cannot. **The nuance still exists; it is only flattened from *view*.**

This is the key refinement to all the "flattening" language: scale **occludes** the particular (an
*epistemic* matter of vantage and resolution); it does **not destroy** it (an *ontological* matter). The
couple is still bickering, still *in* the data. So **"flattened from view ≠ erased from existence,"**
which is why the quarrel is **recoverable** — you change vantage (close reading; reading the extremes;
the human-vs-VADER check = walking down to that section of the stands).

And the trade runs **both ways**: from the stadium you can see the **wave** — a coordinated macro-pattern
of ninety thousand people that *no one* at dinner-party scale could perceive (term frequency and topic
modeling = seeing the wave). Neither vantage is "the truth"; each is blind to what the other reveals.
*That* is the real argument for **close → distant → close**.

*(Caveat that keeps the edge: even the dinner seat is not the noumenon — the guest sees the bicker, not
its whole meaning. Close reading is higher *resolution*, not *truth*. The analogy shakes hands with §1.)*

---

## 4. The moral floor

Put bluntly: **for every individual tragedy, there are billions of people who don't know to care.**

At the scale of humanity, almost every individual tragedy is occluded from almost everyone — not
callousness, but **"don't know to care"**: an *epistemic* failure with *moral* consequence. Caring
requires knowing, and scale withholds the knowing. The hopeful seam: if the failure is *not knowing*,
then making the occluded individual visible can convert "don't know" into "now you know to care." This is
the gravest case for what the tools are *for* — **instruments of moral attention.**

**Double-edged.** Aggregation also *anesthetizes* — the apocryphal *"one death is a tragedy; a million is
a statistic."* The same averaging that makes scale legible can flatten a tragedy into a number no one
feels. The tools can extend care *or* manufacture the numbness that lets us not care, depending on whether
you stop at the aggregate.

**The moral close → distant → close.** You need *distant* reading to **comprehend** the scale (you cannot
act on what you cannot measure — a crisis of millions) *and* *close* reading to **preserve** the moral
charge (you will not act on what you cannot feel — this one child). Drop either and you fail differently:
all aggregate, you understand the catastrophe but feel nothing; all anecdote, you weep for one and are
blind to the million. The oscillation is an **ethical** skill — a strong thing for a coding course to
teach. And it closes the loop to **voice**: the aggregate *informs*; the single voice *moves*. The
statistic is the stadium; the voice walks the reader down to the table.

### Literary anchor — Auden, "Musée des Beaux Arts" (1938)
The canonical statement of the moral floor: suffering takes place "while someone else is eating or
opening a window or just walking dully along." Auden reads Brueghel's *Landscape with the Fall of Icarus*,
where the tragedy (Icarus drowning) is tiny in the corner while the ploughman ploughs and "the expensive
delicate ship … sailed calmly on."
- **Brueghel's composition *is* the stadium / occlusion** — the tragedy flattened to the margin by a busy
  foreground.
- **Auden's poem *is* the close reading** — it walks us to the corner to see the white legs vanishing into
  the green water, and makes us *know to care.*

It grounds the whole computational enterprise in the oldest humanistic question — *how do we attend to
suffering that isn't ours?* — is itself an *image-about-seeing* that pairs with the noumena graphic, and
is voice doing exactly the work the course asks of students. (A poem, in a writing course, doing the job.)

---

## 5. How the framework maps to the built materials

| Idea | Lives in |
|---|---|
| Bias is constitutive; "make your choices visible" | The `#comments` requirement in every HW; the three reflections |
| Classification is authored | HW1 (moderation flags, age bins); HW3 (the 0.05 cutoff); HW4 (`num_topics`) |
| What counting flattens / preserve the quarrel | HW2 → HW3 (`commandments` in both camps); HW3 split mean; HW4 sentiment-by-topic |
| Borrow the tool, judge it | The "honest about borrowed code" notes (VADER, Gensim, `Counter`) |
| Hear, don't extract | Day 8 collection ethics (ML6 Data Archaeology) |
| Return to the individual | HW3 reading the extremes + human-vs-VADER; HW4 "human names the topics" |
| Voice through difficulty | Ungrading; the reflections; the capstone essay; the AI-use policy |
| The whole spine, visualized | `materials/images/noumena_to_wisdom_pipeline.png` + Day-1 framing |

---

## 6. How it could reach students (candidate fold-ins — instructor's call)

None of this is yet woven into student-facing materials; each is a small, optional addition:
- **Subtitle gloss:** "…Developing Data-Driven Opinions **to hear the human at scale**."
- **A learning outcome** on *representing others' voices responsibly* (incl. their disagreements).
- **Day 1:** the noumena passage (`materials/Day1_Framing_Noumena_to_Wisdom.md`) + Auden/Brueghel as the
  humanities frame.
- **Day 7 (ML4 AI Agency):** extend from "reading AI's code" to "not ceding *your voice* to AI."
- **Day 12 (close vs. distant):** the dinner-party / stadium illustration as the thesis image.
- **Capstone standard:** "give voice to the people in your data — including their disagreements — and
  show where your tools risked flattening them. Did your analysis sail calmly on, or make someone look?"

**Open design dials:**
- **Vocabulary:** keep the explicit Kantian terms ("noumena/phenomena") or swap to plain language ("the
  thing itself / as it appears"). The diagram and argument survive either way.
- **Lecture homing:** re-home **ML9 "Going Public"** at Day 17 (its analysis→public-argument spine fits
  the capstone); harvest **ML8 "Code as Rhetoric"**'s thesis into the code-is-not-neutral thread.
- **ML2 "Sacred Boundaries"** (Day 2): **CUT (2026-06-15).** Its privacy/collection-ethics core is served
  by **ML6 Data Archaeology** (Day 8), and its one durable idea — the noumena limit on religious
  conviction as an interiority distant reading can't reach — is already in **ML0** (the woman who "feels
  something whole and hers"). The "sacred/taboo" metaphor also collided with the *literally* sacred corpus.
  Day 2 is now a no-mini-lecture day (dive into Strings).

---

## 7. Civic stakes — TCU Core Curriculum (CSV + HUM vetting)

> **Update (2026-06-12):** the course carries **two** Core designations — **CSV** *and* **Humanities
> (HUM)**. HUM (below, formerly listed under "adjacent resonance") is now a **claimed** designation; the
> syllabus names both. Official HUM outcome (verified against `TCU-Core-Curriculum-outcomes-1.pdf`):
> *"Use humanistic modes of inquiry to analyze human experiences and expressions across space and time."*
> The course meets it by reading real human expression both **closely and at scale** — interpreting
> cultural texts (public comments, the Constitution, a chosen corpus), across contemporary and historical
> voices, always asking what computation reveals and flattens. Evidence: the HW analyses, the capstone
> notebook + essay, and the close-vs-distant-reading work.

WRIT 20833 carries TCU's **Citizenship & Social Values (CSV)** designation in the **TCU Core Curriculum**,
under the **Responsible Citizenship** competency ("describe concepts or theories of social responsibility
in diverse or global communities"). *(Sources: `TCU-Core-Curriculum-outcomes-1.pdf` — current outcomes
matrix; `Citizenship-and-Social-Values-5-5-10.doc` — the earlier HMVV-era CSV submission form.)* This is
not incidental — the conceptual through-line above *is* the mechanism by which the course delivers its
civic outcome.

**The CSV Student Learning Outcome (current):** *"Examine the knowledge, skills, values, or motivation
needed to participate or lead within diverse communities."*

The course meets it directly. Its running case — a contested **public-policy choice** (the 2025 TX law
placing the Ten Commandments in classrooms) — is exactly a **diverse community in disagreement about its
values.** Students examine:
- the **values** in tension (religious expression vs. church-state separation), heard through the
  community's own words;
- the **skills** needed to participate — the computational literacy to weigh evidence at scale *and* the
  rhetorical skill to argue responsibly (the data-driven-opinion capstone);
- the **knowledge / motivation** for responsible participation — including the ethic of *hearing* the
  other side rather than flattening it (the moral floor §4; the quarrel §2). "Hear the human at scale"
  is, at bottom, civic-participation pedagogy.

The earlier HMVV form elaborates the same competency into outcomes the course also hits — *informed
participation in civic discourse and decision-making; examine civic issues as public policy choices;
articulate the rights and responsibilities of individuals and groups* — useful language for the vetting
narrative.

**Adjacent core resonance (context, not claimed designations).** Beyond the two designations it now
carries (CSV + HUM, above), the course also strongly embodies two further Core outcomes — worth knowing
if it's ever submitted for additional credit or to show its breadth: **Written Communication 2**
("analyze and compose evidence-based arguments in various forms" — the capstone essay), and **Cultural
Awareness** ("explore culture and cultural phenomena as sites of identity, difference, understanding, or
collaboration" — cultural analytics of a site of difference).

**Produced work that would be evaluated** (CSV evidence): the **capstone data-driven-opinion essay**
(central artifact), the **four threaded discussions**, the **three reflections**, and the **HW analyses**
of the civic corpus.

**Action items (re-vetting):** Core syllabi should *reflect* the CSV outcome; the submission form wants
**2–3 concrete examples** of student work achieving it. `SYLLABUS_2026.md` now names the CSV designation;
the 2–3 examples can be drafted from the capstone + discussions on request.

## Related documents
- `SYLLABUS_2026.md` · `COURSE_SCHEDULE_2026.md` — the course as students meet it.
- `TCU-Core-Curriculum-outcomes-1.pdf` — the current TCU Core Curriculum outcomes matrix (see §7).
- `Citizenship-and-Social-Values-5-5-10.doc` — the earlier HMVV-era CSV vetting form (see §7).
- `materials/images/README.md` — the noumena→wisdom graphic and its per-arrow bias map.
- `materials/Day1_Framing_Noumena_to_Wisdom.md` — the drafted Day-1 teaching passage.
- `PORT_ASSESSMENT_2026.md` · `PROPOSED_4WEEK_SCHEDULE.md` — the port rationale and design.
- `WORKLOG.md` — running session handoff and decision log (points here for the conceptual framework).
