# Connotations & Code
## Why no number is ever neutral

<!-- meta: Day 1 · the through-line -->


<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — aged parchment, muted greens, one clay accent; match the ml0 images): a single large printed numeral resting on parchment, casting a long shadow that resolves into a knot of small human figures arguing and gesturing — the bare number carries a story behind it. -->
![A printed numeral on parchment casting a shadow shaped like a crowd of arguing figures](materials/lectures/images/ml1_title.jpg)

<!-- slide:
![A printed numeral on parchment casting a shadow shaped like a crowd of arguing figures](materials/lectures/images/ml1_title_43.jpg)

Every arrow from a lived human fact to an "insight" is a human choice.
Today we turn that on the very first thing you'll touch — **a plain number.**
-->

The opening lecture left us with a claim: every arrow in the pipeline from a lived human fact to an "insight" is a human
choice. This lecture turns that claim on the very first thing you'll touch — a plain number — and asks
what it can, and can't, tell us on its own.

Here is a fact about the corpus we'll work with all term: 93 YouTube comments on a Texas law that puts
the Ten Commandments in public-school classrooms. (A **corpus** is simply a collection of texts gathered
for analysis.) The comments sit under one CBS News video from August 20, 2025, reporting that a federal judge
had blocked the law in some school districts, and they were copied within the following month using a
browser scraping tool. So many of them are reacting to the judge as much as to the law. The tool caught
top-level comments but not the replies under them, and blank and duplicate entries were removed. Some
comments are tiny: one reads, in full, "Of Texas." And one more choice shapes everything
you'll compute: a few long comments ran over several lines, and the cleaning split them at their line
breaks. So the file you'll load has **123 rows**, not 93, and some rows are only pieces of a comment. The
export kept no names or dates, either, so we don't know how many people wrote these comments, or exactly
when. They are not a sample of Texans, or even of YouTube:
they're whoever chose to comment on that one video, and whatever the tool caught. We'll come back to who
that leaves out.

## What does the count say?

<!-- layout: split -->

![Bar chart: in 93 comments, with capitals ignored, "commandments" appears 25 times and "constitution" 8](materials/lectures/images/ml1_count_chart.png)

<!-- slide:
**Our corpus:** 93 YouTube comments under one CBS News video (Aug 20, 2025) about the federal ruling that blocked Texas's law putting the Ten Commandments in public-school classrooms — copied soon after with a free browser scraper.

> Capitals ignored, **"commandments"** appears **25** times. **"Constitution"** appears **8**.

Flat, true, countable.

*So what is it telling us?*
-->

<!-- slide:
Before you read meaning into it, list what else could explain it.

- **The topic.** The video is *about* the Ten Commandments. Of course the word dominates.
- **The counting.** Keep the capitals and "Constitution" drops to 4.
- **The crowd.** Who chose to comment at all — and who didn't?

*A number shows a difference. What the difference means is your argument, not the number's.*
-->

> In those 93 comments, ignoring capitals, the word **"commandments"** appears 25 times. **"Constitution"** appears 8.

A flat, true, countable fact. It's tempting to read it at once — *the crowd cares more about scripture than
law.* But list what else could explain it. The video is *about* the Ten Commandments, so the word was always
going to dominate. Count with capitals and "Constitution" falls to 4. And the comments come only from people
who chose to post. Before we run a single line of code, ask the humanist's question: what could this number
mean, what else could explain it, and who decided what got counted?

## Denotation and connotation

<!-- slide:
![The same house painted three ways — warm cottage, notarized "residence," listing card — one denotation, three connotations](materials/lectures/images/ml1_denotation.jpg)

You already own the tool this lecture needs.

- A word's **denotation** is what it literally points to.
  *House, home,* and *residence* denote the same thing: a building people live in.
- Its **connotation** is everything it carries on top — warmth, money,
  bureaucracy, belonging.

*Home* and *residence* denote alike and connote worlds apart.
-->

<!-- slide:
![The same house painted three ways — warm cottage, notarized "residence," listing card — one denotation, three connotations](materials/lectures/images/ml1_denotation.jpg)

Now the move that makes you a data humanist:

### Numbers have connotation too.

"Single-mother household" **denotes** a category on a form. It **connotes**
a whole contested story about blame and worth — and which story you hear
depends on who's speaking.

*The denotation is the surface. The connotation is where the culture lives —
and where the argument is.*
-->

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

<!-- slide:
![A weaver at a lamplit loom drawing threads from spools carved with faces; the cloth coming off the loom is woven in rows of tally marks](materials/lectures/images/ml1_loom_sq.jpg)

Three comforting things people say about data. Each one is too simple.

- *"Data doesn't lie."* — It doesn't have to lie to mislead.
  It can simply leave things out.
- *"The numbers speak for themselves."* — They never do.
  Someone always speaks for them, by choosing the frame.
- *"It's just objective analysis."* — Every dataset records somebody's
  choices about what was worth counting.
-->

<!-- slide:
![A weaver at a lamplit loom drawing threads from spools carved with faces; the cloth coming off the loom is woven in rows of tally marks](materials/lectures/images/ml1_loom_sq.jpg)

Data carries the **values, assumptions, and blind spots** of whoever
collected, sorted, and counted it.

That isn't a flaw you can scrub out. It's the opening lecture's diagram again:
every arrow there was a choice, and so is every column here.

### A dataset is a record of choices before it is a record of anything else.
-->

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — parchment, muted greens, one clay accent): a weaver at a lamplit loom; the cloth coming off it is woven in rows of tally marks, and every thread runs back to the weaver's own spools — the bias is the material, not dirt on the cloth. -->
![A weaver at a lamplit loom drawing threads from spools carved with faces; the cloth coming off the loom is woven in rows of tally marks](materials/lectures/images/ml1_loom.jpg)

Three comforting things people say about data. Each one is too simple.

- *"Data doesn't lie."* — It doesn't have to lie to mislead. It can simply leave things out.
- *"The numbers speak for themselves."* — Numbers never speak for themselves. Someone always speaks for
  them, by choosing the frame.
- *"It's just objective analysis."* — Every dataset is a record of somebody's choices about what was worth
  counting, and what wasn't.

Data carries the **values, assumptions, and blind spots** of whoever collected, sorted, and counted it.
That isn't a flaw you can scrub out. It's the opening lecture's diagram again: every arrow there was a
choice, and so is every column here. A dataset is a record of choices before it is a record of anything else.

## Same numbers, three stories

<!-- slide:
![Two stacks of graded papers on a schoolroom table, one tall and one short; tired students, a man pointing at a leaking ceiling, and a woman pointing at a thick exam booklet each blame something different](materials/lectures/images/ml1_three_stories.jpg)

> School A — average SAT **1240**
> School B — average SAT **980**

Watch the *same denotation* spin into three connotations,
each quietly handing the blame to someone else:

- **Deficit story** — School B's students are underperforming. *(It's the kids.)*
- **Systemic story** — School B is under-resourced and underfunded. *(It's the system.)*
- **Cultural story** — the SAT measures one kind of knowledge. *(It's the test.)*
-->

<!-- slide:
![The same two SAT averages, 1240 and 980, drawn twice: with the axis starting at 0 the bars look close; starting at 900, School B looks like it is collapsing](materials/lectures/images/ml1_sat_axes.png)

Nothing *in* the numbers tells you which story is true.
They show a **difference**, not its **cause**.

And even the difference can be staged. Same two numbers, two charts —
on the right, School B looks like it's collapsing.

*Choosing the story is the human part — an argument about fairness, wearing the costume of arithmetic.*
-->

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — parchment, muted greens, one clay accent): two stacks of graded exam papers on a table, one tall, one short; three figures each point elsewhere — at tired students, at a water-stained schoolhouse ceiling, at a thick exam booklet. Same papers, the blame moves. -->
![Two stacks of graded papers on a schoolroom table, one tall and one short; tired students, a man pointing at a leaking ceiling, and a woman pointing at a thick exam booklet each blame something different](materials/lectures/images/ml1_three_stories.jpg)

Two plain numbers:

> School A — average SAT **1240**. School B — average SAT **980**.

Watch the *same denotation* spin into three different connotations, each one quietly handing the blame to
someone else:

- **Deficit story** — School B's students are underperforming. *(It's the kids.)*
- **Systemic story** — School B is under-resourced and underfunded. *(It's the system.)*
- **Cultural story** — the SAT measures one particular kind of knowledge. *(It's the test.)*

Nothing *in* the numbers tells you which story is true. They show a *difference*, not its *cause*; to
argue about causes, you'd need more evidence than the two scores. Even the difference can be staged: draw
the same two bars with the axis starting at 900 instead of 0, and School B seems to collapse. The numbers
are the easy part. Choosing the story is the human part — and it is already an argument about fairness,
wearing the costume of arithmetic.

## Who's doing the telling?

<!-- slide:
![A hand holds an empty wooden picture frame up to a crowded market street; only a small slice of the scene falls inside it](materials/lectures/images/ml1_frame_sq.jpg)

If numbers don't tell their own story, someone does —
usually someone with power over the frame.

- **Institutions** define the categories — a government writes the census
  boxes, a university decides what "success" counts as
- **Media** sets the frame — the headline, the axis a chart starts at,
  the context cut for space
- **Researchers** choose the question — who gets sampled, and who paid for the asking
-->

<!-- slide:
![A hand holds an empty wooden picture frame up to a crowded market street; only a small slice of the scene falls inside it](materials/lectures/images/ml1_frame_sq.jpg)

So the reflex this course wants to build.
Every time a number lands in front of you, ask:

### Who collected this, why, and whose story does it tell?
-->

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — parchment, muted greens, one clay accent): a hand holding an empty wooden picture frame up to a crowded market street; only a small slice falls inside the frame while the scene carries on all around it. -->
![A hand holds an empty wooden picture frame up to a crowded market street; only a small slice of the scene falls inside it](materials/lectures/images/ml1_frame.jpg)

If numbers don't tell their own story, someone does — usually someone with power over the frame.

- **Institutions** define the categories: a government writes the census boxes, a university decides what
  "success" counts as, a platform decides what "engagement" means.
- **Media** sets the frame: the headline, the axis a chart starts at, the context that gets cut for space.
- **Researchers** choose the question: what gets studied, who gets sampled, and who paid for the asking.

So the reflex this course wants to build: every time a number lands in front of you, ask **who collected
this, why, and whose story does it tell?**

## The missing and the uncounted

<!-- slide:
![A hall of seated figures where several chairs are empty and some silhouettes are faint and half-painted — the uncounted](materials/lectures/images/ml1_missing_sq.jpg)

The loudest thing about a dataset is often **what isn't in it.**

Our 93 comments are not "the public." They're the slice of the public
that *posted* — people online, fired up enough to type,
willing to be seen arguing.
-->

<!-- slide:
![A schematic funnel: everyone the law affects, people who saw this one video, people who chose to comment, 93 comments the scraper caught, 123 rows in your file](materials/lectures/images/ml1_funnel.png)

The woman from the opening lecture posted.
Her neighbor — who felt just as strongly and never typed a word —
**is not in the file at all.** Neither is anyone without
the wifi, the time, or the nerve.

### Absence from the data is not absence from reality.
-->

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — parchment, muted greens, one clay accent): a hall of seated figures rendered in muted green; several chairs sit empty and a few silhouettes are faint and only half-painted — the uncounted. A handful of speech-bubbles rise from the solid figures while the faded ones stay silent. -->
![A hall of seated figures where several chairs are empty and some silhouettes are faint and half-painted — the uncounted](materials/lectures/images/ml1_missing.jpg)

The loudest thing about a dataset is often what isn't in it.

Our 93 comments are not "the public." They're the slice of the public that *posted* — people online,
fired up enough to type, willing to be seen arguing. The woman from the opening lecture posted. Her
neighbor, who felt just as strongly and never typed a word, is not in the file at all. Neither is anyone
without the wifi, the time, or the nerve.

**Absence from the data is not absence from reality.** Some of the most important voices in any cultural
question are exactly the ones the counting never reaches. A good distant reading stays honest about the
silence at its edges.

## So: code is not neutral

<!-- slide:
![A hand at a keyboard whose keys are tiny brass levers, each keypress sending golden light down a branching track](materials/lectures/images/ml1_code_sq.jpg)

Code inherits every connotation above — and adds its own,
because **code runs on definitions, and a definition is a decision.**

Over the next weeks *you* decide. What counts as a "word" when you split
a comment? Which words are "stopwords" worth deleting? What score makes
a comment "positive"? Where do you cut one topic from the next?
-->

<!-- slide:
![Two bars: the rule "drop every word used fewer than 5 times" keeps 98 different words and drops 651 (87%); by word uses it drops 42%. Kept: the, to, of, and, is, commandments, religion, god. Dropped: slavery, adultery, empathy, Muslim, Jewish, atheist, separation](materials/lectures/images/ml1_filter_chart.png)

Each choice is a small act of interpretation that looks like a neutral function.

And those choices don't merely *encode* a value — they **argue** one.

Drop every word used fewer than five times, and your code has *claimed*
that rare words matter less. In our file, that one rule deletes
**651 of 749** different words.

*Code isn't only structure. It's rhetoric.*
-->

<!-- slide:
That's the trap and the responsibility at once: a machine looks objective
**precisely because** it hides the choices inside it.

### Read data like a text, and write code that shows its choices.

Leave the `#comment` that says what you chose, and why.
*That comment is not housekeeping. It's where the honesty shows.*
-->

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — parchment, muted greens, one clay accent; echoes ml0's brass-valves "every arrow is a choice"): a hand over a keyboard whose keys are tiny brass levers and valves; each keypress releases a thread of golden light down a branching track — code as a chain of human choices behind a neutral-looking surface. -->
![A hand at a keyboard whose keys are tiny brass levers, each keypress sending golden light down a branching track](materials/lectures/images/ml1_code.jpg)

Code inherits every connotation above — and then adds its own, because code runs on definitions, and a
definition is a decision.

Over the next eight weeks *you* will be the one deciding. What counts as a "word" when you split a comment?
Which words are "stopwords" worth deleting? What score makes a comment "positive"? Where do you cut one
topic from the next? Each is a small act of interpretation that looks like a neutral function.

In code, those decisions are concrete operations. You'll **split** text into words, **count** them,
**delete** the ones on a *stopword* list (common words like *the* and *of* that an analyst chooses to skip),
**score** each comment and set a *threshold* (a cutoff that turns a continuous score into a category like
"positive"), and **group** comments that use similar words. Every one of those verbs hides a choice.

And those choices don't merely *encode* a value — they *argue* one. Which number you make the headline,
which chart you reach for, what you put first and what you bury: every one is a claim about what matters,
aimed at whoever reads your result. If your code drops every word that appears fewer than five times, it
has made a claim: that rare words are less useful, or less meaningful. In our file, that rule deletes 651 of
the 749 different words — *slavery*, *adultery*, *empathy*, *Muslim*, and *Jewish* among them — while
keeping *the*, *to*, and *of*. Code isn't only structure; it's rhetoric. You'll feel that fully when
you go public with an analysis at the end of the term — but it starts here, in the smallest function.

That's the trap and the responsibility at once: a machine looks objective *precisely because* it hides the
choices inside it. Your job as a humanist who codes is the double move from the opening lecture — **read data like a text,
and write code that shows its choices.** Leave the `#comment` that says what you chose, and why. That comment
is not housekeeping. It's where the honesty shows.
