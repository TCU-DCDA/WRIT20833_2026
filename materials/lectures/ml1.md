# Connotations & Code
## Why no number is ever neutral

<!-- meta: ML1 · Day 1 · the through-line -->

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — aged parchment, muted greens, one clay accent; match the ml0 images): a single large printed numeral resting on parchment, casting a long shadow that resolves into a knot of small human figures arguing and gesturing — the bare number carries a story behind it. -->
![A printed numeral on parchment casting a shadow shaped like a crowd of arguing figures](materials/lectures/images/ml1_title.jpg)

ML0 left us with a claim: every arrow in the pipeline from a lived human fact to an "insight" is a human
choice. This lecture turns that claim on the very first thing you'll touch — a plain number — and shows
that even *it* arrives already leaning.

Here is a fact about the corpus we'll work with all term: 123 YouTube comments on a Texas law that puts
the Ten Commandments in public-school classrooms.

> In those 123 comments, the word **"commandments"** appears 25 times. **"Constitution"** appears 8.

A flat, true, countable fact. And already it leans — already it's *telling* you something about whose
ground the argument is being fought on. Before we run a single line of code, ask the humanist's question:
what is that number already saying, and who decided what got counted?

## Denotation and connotation

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — parchment, muted greens, one clay accent): the same modest house painted three times on one canvas — a glowing lamplit cottage (home/belonging), a cold stamped notarial document reading "RESIDENCE," and a flat real-estate listing card — one denotation, three connotations. -->
![The same house painted three ways — warm cottage, notarized "residence," listing card — one denotation, three connotations](materials/lectures/images/ml1_denotation.jpg)

You already own the tool this lecture needs — you've used it on words your whole life.

- A word's **denotation** is what it literally points to. *House*, *home*, and *residence* denote the same
  thing: a building people live in.
- Its **connotation** is everything it carries on top of that — warmth, money, bureaucracy, belonging.
  *Home* and *residence* denote alike and connote worlds apart.

Now the move that makes you a data humanist: **numbers have connotation too.** "Single-mother household"
denotes a category on a form; it *connotes* a whole contested story about blame and worth, and which story
you hear depends on who's speaking. The denotation is the surface. The connotation is where the culture
lives — and where the argument is.

## The myth of neutral data

Three comforting things people say about data. Each one is false.

- *"Data doesn't lie."* — It doesn't have to lie to mislead. It can simply leave things out.
- *"The numbers speak for themselves."* — Numbers never speak for themselves. Someone always speaks for
  them, by choosing the frame.
- *"It's just objective analysis."* — Every dataset is a record of somebody's choices about what was worth
  counting, and what wasn't.

Data carries the **values, assumptions, and blind spots** of whoever collected, sorted, and counted it.
That isn't a flaw to scrub out — it's ML0's point again, one layer down: bias isn't contamination that
sneaks *into* the data, it's the material the data is made *of*.

## Same numbers, three stories

Two real numbers:

> School A — average SAT **1240**. School B — average SAT **980**.

Watch the *same denotation* spin into three different connotations, each one quietly handing the blame to
someone else:

- **Deficit story** — School B's students are underperforming. *(It's the kids.)*
- **Systemic story** — School B is under-resourced and underfunded. *(It's the system.)*
- **Cultural story** — the SAT measures one particular kind of knowledge. *(It's the test.)*

Nothing *in* the numbers tells you which story is true. The numbers are the easy part. Choosing the story
is the human part — and it is already an argument about fairness, wearing the costume of arithmetic.

## Who's doing the telling?

If numbers don't tell their own story, someone does — usually someone with power over the frame.

- **Institutions** define the categories: a government writes the census boxes, a university decides what
  "success" counts as, a platform decides what "engagement" means.
- **Media** sets the frame: the headline, the axis a chart starts at, the context that gets cut for space.
- **Researchers** choose the question: what gets studied, who gets sampled, and who paid for the asking.

So the reflex this course wants to build: every time a number lands in front of you, ask **who collected
this, why, and what story do they need it to tell?**

## The missing and the uncounted

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — parchment, muted greens, one clay accent): a hall of seated figures rendered in muted green; several chairs sit empty and a few silhouettes are faint and only half-painted — the uncounted. A handful of speech-bubbles rise from the solid figures while the faded ones stay silent. -->
![A hall of seated figures where several chairs are empty and some silhouettes are faint and half-painted — the uncounted](materials/lectures/images/ml1_missing.jpg)

The loudest thing about a dataset is often what isn't in it.

Our 123 comments are not "the public." They're the slice of the public that *posted* — people online,
fired up enough to type, willing to be seen arguing. The woman from ML0 — who felt something complete and
entirely her own and then said nothing — is not in the file at all. Neither is anyone without the wifi,
the time, or the nerve.

**Absence from the data is not absence from reality.** Some of the most important voices in any cultural
question are exactly the ones the counting never reaches. A good distant reading stays honest about the
silence at its edges.

## So: code is not neutral

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — parchment, muted greens, one clay accent; echoes ml0's brass-valves "every arrow is a choice"): a hand over a keyboard whose keys are tiny brass levers and valves; each keypress releases a thread of golden light down a branching track — code as a chain of human choices behind a neutral-looking surface. -->
![A hand at a keyboard whose keys are tiny brass levers, each keypress sending golden light down a branching track](materials/lectures/images/ml1_code.jpg)

Code inherits every connotation above — and then adds its own, because code runs on definitions, and a
definition is a decision.

Over the next four weeks *you* will be the one deciding. What counts as a "word" when you split a comment?
Which words are "stopwords" worth deleting? What score makes a comment "positive"? Where do you cut one
topic from the next? Each is a small act of interpretation wearing the costume of a neutral function.

That's the trap and the responsibility at once: a machine looks objective *precisely because* it hides the
choices inside it. Your job as a humanist who codes is the double move from ML0 — **read data like a text,
and write code that shows its seams.** Leave the `#comment` that says what you chose, and why. That comment
is not housekeeping. It's the honesty.
