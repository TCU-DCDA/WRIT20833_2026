# Connotations & Code
## Why no number is ever neutral

<!-- meta: Day 1 · the through-line -->


<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — aged parchment, muted greens, one clay accent; match the ml0 images): a single large printed numeral resting on parchment, casting a long shadow that resolves into a knot of small human figures arguing and gesturing — the bare number carries a story behind it. -->
![A printed numeral on parchment casting a shadow shaped like a crowd of arguing figures](materials/lectures/images/ml1_title.jpg)

<!-- slide:
![A printed numeral on parchment casting a shadow shaped like a crowd of arguing figures](materials/lectures/images/ml1_title_43.jpg)

Data doesn't arrive on its own. Getting from people's lives to an "insight"
about them takes many steps — what to record, how to count it, what to call it —
and **someone decides each one.**

Today we turn that on the very first thing you'll touch — **a plain number.**
-->

The opening lecture left us with a claim: data doesn't arrive on its own. Getting from what happens in
people's lives to an "insight" about them takes many steps — deciding what to record, how to count it, and
what to call it — and someone makes every one of those decisions. This lecture turns that claim on the very first thing you'll touch — a plain number — and asks
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

## Close reading, distant reading

<!-- layout: split -->

<!-- slide:
![A scale running from one sentence to one comment to potentially thousands of comments, with close reading at one end and distant reading at the other](materials/lectures/images/ml1_zoom.png)

Monday we asked: *why bring code into a humanities class?* Here's one answer.

- **Close reading** is what you do with one text: slow, careful attention to what it says and what it implies.
- **Distant reading** uses code to look for patterns across more text than any one person could read.

Code gives us distance. The humanities tell us what we're looking at.

**Distant reading still needs a close reader.**
-->

![A scale running from one sentence to one comment to potentially thousands of comments, with close reading at one end and distant reading at the other](materials/lectures/images/ml1_zoom.png)

Why bring code into a humanities class at all? Here's one answer. **Close reading** is what you already do
with a single text: slow, careful attention to what it says and what it implies. **Distant reading** uses
code to look for patterns across more text than any one person could read. Code gives us distance; the
humanities tell us what we're looking at. Ninety-three comments is few enough to read closely, which makes
this corpus a good place to practice both, and to see that distant reading still needs a close reader.

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
Before you decide what the number means, ask: **what else could have produced it?**

- **The topic.** The video is *about* the Ten Commandments. Of course the word dominates.
- **The counting.** To a computer, *Constitution* and *constitution* are two different words —
  4 of each. Ignore capitals and they merge into 8; keep them and each counts only 4.
  How you clean and prepare the data can literally change the result.
- **The crowd.** Who chose to comment at all — and who didn't?

*A number shows a difference. What the difference means is your argument, not the number's.*
-->

> In those 93 comments, ignoring capitals, the word **"commandments"** appears 25 times. **"Constitution"** appears 8.

A flat, true, countable fact. It's tempting to read it at once — *the crowd cares more about scripture than
law.* But ask what else could have produced it. The video is *about* the Ten Commandments, so the word was always
going to dominate. The count itself rests on a choice: to a computer, *Constitution* and *constitution* are
two different words, and our file has four of each. Ignore capitals and they merge into 8; keep them and
each counts only 4. Someone decided which before the number existed, and that is the general lesson: the
methods used to clean and prepare data can literally change the outcome. And the comments come only from people
who chose to post. Before we run a single line of code, ask the humanist's question: what could this number
mean, what else could explain it, and who decided what got counted?

## Denotation and connotation

<!-- slide:
![The same house painted three ways — warm cottage, notarized "residence," listing card — one denotation, three connotations](materials/lectures/images/ml1_denotation.jpg)

You already own the tool this lecture needs.

- A word's **denotation** is what it literally points to.
  *House, home,* and *residence* denote the same thing: a building people live in.
- Its **connotation** is what it *implies* — the emotional resonance and
  point of view it brings along: warmth, money, bureaucracy, belonging.

*Home* and *residence* denote alike and connote worlds apart.

By close reading, we can determine a text's tone, attitude, and mood — not just what it says, but what it implies.

Later, we'll look at ways a computer can try to detect what's implied.
-->

<!-- slide:
![The same house painted three ways — warm cottage, notarized "residence," listing card — one denotation, three connotations](materials/lectures/images/ml1_denotation.jpg)

Now the move that makes you a data humanist:

### Numbers have connotation too.

"Single-mother household" **denotes** a category on a form. It **connotes**
a whole contested story about blame and worth — and which story you hear
depends on who's speaking.

*The denotation is the surface. The connotation is where the culture lives —
and what we build the argument from.*
-->

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — parchment, muted greens, one clay accent): the same modest house painted three times on one canvas — a glowing lamplit cottage (home/belonging), a cold stamped notarial document reading "RESIDENCE," and a flat real-estate listing card — one denotation, three connotations. -->
![The same house painted three ways — warm cottage, notarized "residence," listing card — one denotation, three connotations](materials/lectures/images/ml1_denotation.jpg)

You already own the tool this lecture needs — you've used it on words your whole life.

- A word's **denotation** is what it literally points to. *House*, *home*, and *residence* denote the same
  thing: a building people live in.
- Its **connotation** is what it implies beyond that: the emotional resonance and the particular point of
  view it brings along — warmth, money, bureaucracy, belonging.
  *Home* and *residence* denote alike and connote worlds apart.

By close reading, we can determine a text's tone, attitude, and mood — not just what it says, but what it
implies. Later in the term, we'll look at ways a computer can try to detect what's implied.

Now the move that makes you a data humanist: **numbers have connotation too.** "Single-mother household"
denotes a category on a form; it *connotes* a whole contested story about blame and worth, and which story
you hear depends on who's speaking. The denotation is the surface. The connotation is where the culture
lives — and what we build the argument from.

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

![The same two SAT averages, 1240 and 980, drawn twice: with the axis starting at 0 the bars look close; starting at 900, School B looks like it is collapsing](materials/lectures/images/ml1_sat_axes.png)

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

Politicians make this move all the time: *"The American people want…"
"The good people of Texas feel…"* Each claims everyone's voice
on the strength of whoever showed up.

*Write "Texans think…" from these 93 comments, and you've made the same move.*
-->

<!-- slide:
![A schematic funnel: everyone the law affects, people who saw this one video, people who chose to comment, 93 comments the scraper caught, 123 rows in your file](materials/lectures/images/ml1_funnel.png)

The woman from the opening lecture made the choice
to post her thoughts about the debate.
Her neighbor felt just as strongly — but never typed a word,
and **is not captured by the dataset.**
Both women had the wifi and the time. Plenty of people don't,
and they never had a chance to be counted.

### Absence from the data is not absence from reality.
-->

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — parchment, muted greens, one clay accent): a hall of seated figures rendered in muted green; several chairs sit empty and a few silhouettes are faint and only half-painted — the uncounted. A handful of speech-bubbles rise from the solid figures while the faded ones stay silent. -->
![A hall of seated figures where several chairs are empty and some silhouettes are faint and half-painted — the uncounted](materials/lectures/images/ml1_missing.jpg)

The loudest thing about a dataset is often what isn't in it.

![A schematic funnel: everyone the law affects, people who saw this one video, people who chose to comment, 93 comments the scraper caught, 123 rows in your file](materials/lectures/images/ml1_funnel.png)

Our 93 comments are not "the public." They're the slice of the public that *posted* — people online,
fired up enough to type, willing to be seen arguing. The woman from the opening lecture made the
choice to post her thoughts about the debate. Her neighbor felt just as strongly but never typed a word,
and is not captured by the dataset at all. Both women had the wifi and the time; plenty of people don't,
and they never had a chance to be counted.

You've heard this move before. Politicians of every stripe make it: *"The American people want…"* or
*"The good people of Texas feel…"* Each claims to speak for everyone on the strength of whoever wrote in,
called, or showed up. Write "Texans think…" from these 93 comments, and you've made the same move. What
the data supports is narrower and more honest: *these commenters wrote…*

**Absence from the data is not absence from reality.** Some of the most important voices in any cultural
question are exactly the ones the counting never reaches. A good distant reading stays honest about the
silence at its edges.

## So: code is not neutral

<!-- slide:
![A hand at a keyboard whose keys are tiny brass levers, each keypress sending golden light down a branching track](materials/lectures/images/ml1_code_sq.jpg)

Code inherits every connotation above. Then it does two things more:

- **It amplifies them.** A program applies the same rule to every row,
  thousands of times, never pausing to ask whether this case is different.
- **It adds its own.** Code runs on logical patterns someone programmed —
  *if this, then that.* **Writing each pattern is a decision.**

Over the next weeks *you* decide. What counts as a "word" when you split
a comment? Which words are "stopwords" worth deleting? What score makes
a comment "positive"? Where do you cut one topic from the next?
-->

<!-- slide:
Each choice is a small act of interpretation that looks like a neutral function. Take one:

### Drop every word used fewer than five times.

Why would anyone do that? For reasons that sound sensible:

- **Noise.** Rare words are often typos and scraps — *chruch, obay, govmt.*
- **No pattern.** A word used once can't rise, fall, or keep company.
  Counting methods need repetition.
- **Size.** Most words are rare: in our file, **457 of 749** appear exactly once.
  In a big corpus they slow the computer and crowd every chart,
  so many tools and tutorials make the cut a default step.

*Reasonable motives. Now look at what the rule costs.*
-->

<!-- slide:
![Two bars: the rule "drop every word used fewer than 5 times" keeps 98 different words and drops 651 (87%); by word uses it drops 42%. Kept: the, to, of, and, is, commandments, religion, god. Dropped: slavery, adultery, empathy, Muslim, Jewish, atheist, separation](materials/lectures/images/ml1_filter_chart.png)

In our file, that one rule deletes **651 of 749** different words.

- **Gone:** *slavery, adultery, empathy, Muslim, Jewish, atheist.*
- **Kept:** *the, to, of.*

Even *separation* — as in church and state — goes. It appears 4 times,
plus once as "seperation." **One typo decides whether it survives.**

*You'll make a cousin of this cut yourself, every time you ask for the `most_common(10)` words.*
-->

<!-- slide:
So the cut doesn't merely *encode* a value. It **argues** one.

### Rhetoric: the art of persuasion

**Rhetoric** is how a speaker or writer shapes a message to move
a particular audience — what to say, in what order, and *what to leave out.*
Aristotle called it seeing "the available means of persuasion."

Hand a reader the surviving words and they'll conclude this conversation
was about *commandments, religion, God* — never learning anyone raised
slavery or empathy at all. Persuasion, with no speaker in sight.

*Code isn't only structure. It's rhetoric.*
-->

<!-- slide:
That's the trap
and the responsibility at once:

data and software look objective
**precisely because**
they hide from the general user
the choices that shaped them.
::: col
### Read data and code like a text, for denotation and connotation, and write code that shows your choices.

Leave the `#comment` that says what you chose, and why.

*Your `#comments` are not housekeeping. They're where you take the opportunity to be honest and transparent about your choices.*
-->

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — parchment, muted greens, one clay accent; echoes ml0's brass-valves "every arrow is a choice"): a hand over a keyboard whose keys are tiny brass levers and valves; each keypress releases a thread of golden light down a branching track — code as a chain of human choices behind a neutral-looking surface. -->
![A hand at a keyboard whose keys are tiny brass levers, each keypress sending golden light down a branching track](materials/lectures/images/ml1_code.jpg)

Code inherits every connotation above, and then does two things more. First, it **amplifies** them. A
human reader might pause over an odd comment and ask whether this case is different; a program applies the
same rule to every row, thousands of times, without hesitating. Whatever assumption the rule carries gets
carried out at scale. Second, code **adds its own** connotations, because code runs on logical patterns that
someone programmed — *if this, then that* — and writing each pattern is a decision.

Over the next eight weeks *you* will be the one deciding. What counts as a "word" when you split a comment?
Which words are "stopwords" worth deleting? What score makes a comment "positive"? Where do you cut one
topic from the next? Each is a small act of interpretation that looks like a neutral function.

In code, those decisions are concrete operations. You'll **split** text into words, **count** them,
**delete** the ones on a *stopword* list (common words like *the* and *of* that an analyst chooses to skip),
**score** each comment and set a *threshold* (a cutoff that turns a continuous score into a category like
"positive"), and **group** comments that use similar words. Every one of those verbs hides a choice.

![Two bars: the rule "drop every word used fewer than 5 times" keeps 98 different words and drops 651 (87%); by word uses it drops 42%. Kept: the, to, of, and, is, commandments, religion, god. Dropped: slavery, adultery, empathy, Muslim, Jewish, atheist, separation](materials/lectures/images/ml1_filter_chart.png)

Take one rule you'll find in countless tutorials: drop every word used fewer than five times. Why would
anyone do that? The motives are sensible. Rare words are often noise — typos and scraps like *chruch*,
*obay*, and *govmt*. A word that appears once can't show a pattern; it can't rise or fall over time or turn
up beside other words, and counting methods run on repetition. And rare words are most of any vocabulary:
in our file, 457 of the 749 different words appear exactly once. In a corpus of millions of words they slow
later methods like topic modeling and crowd every chart, so many tools make the cut a default step.

But look at what it costs. In our file, that rule deletes 651 of the 749 different words — *slavery*,
*adultery*, *empathy*, *Muslim*, and *Jewish* among them — while keeping *the*, *to*, and *of*. Even
*separation*, as in church and state, falls below the line: it appears four times, plus once spelled
"seperation," so a single typo decides whether it survives. And you'll make a cousin of this cut yourself,
every time you ask for the `most_common(10)` words.

So those choices don't merely *encode* a value — they *argue* one. That makes them **rhetoric**: the art of
persuasion, or how a speaker or writer shapes a message to move a particular audience — what to say, in
what order, and what to leave out. Aristotle defined it as the ability to see, in any given case, "the
available means of persuasion." A frequency cut does some of that leaving-out on your behalf. Hand a reader
the surviving words and they'll conclude the conversation was about *commandments*, *religion*, and *God*,
never learning that anyone raised slavery or empathy at all. Which number you make the headline, which chart
you reach for, what you put first and what you bury: every one is a claim about what matters, aimed at
whoever reads your result. Code isn't only structure; it's rhetoric. You'll feel that fully when you go
public with an analysis at the end of the term — but it starts here, in the smallest function.

That's the trap and the responsibility at once: data and software look objective *precisely because* they
hide from the general user the choices that shaped them. Your job as a humanist who codes is a double move:
**read data and code like a text, for denotation and connotation, and write code that shows your choices.**
Leave the `#comment` that says what you chose, and why. Your `#comments` are not housekeeping. They're where
you take the opportunity to be honest and transparent about your choices.

## Someone always cleans the text

<!-- IMG PROMPT (warm "Reading Room" oil painting — parchment, muted greens, one clay accent): a lamplit editor's desk; on one side a manuscript covered in red-pen corrections, on the other the finished, clean printed book. Alt: An editor's desk with a heavily marked-up manuscript beside its clean printed book. -->

<!-- slide:
The books you read for class didn't arrive that way. Before you saw a word, editors and publishers:

- standardized spelling and punctuation
- fixed typos
- chose which version, which edition, which words to keep

*You've been reading cleaned data your whole life. You just never saw the cleaning.*
-->

The books you read for class didn't arrive that way. Before you saw a word, editors and publishers
standardized the spelling and punctuation, fixed the typos, and chose which version, which edition, and
which words to keep. You've been reading cleaned data your whole life. You just never saw the cleaning.

## You clean as you read

<!-- layout: split -->

<!-- slide:
![A real comment, "Seperation of chruch and state.", beside the corrected version a reader automatically understands; to Python, seperation and separation are different words](materials/lectures/images/ml1_readers.png)

Comments and posts written on the fly don't get an editor. So you become one, without noticing.

You read *seperation* and *govmt* and silently fix them. You don't stop and wonder what "obay" means.

A computer doesn't do that. To Python, *seperation* and *separation* are two different words.

**Cleaning code makes your invisible reading habits visible.**
-->

![A real comment, "Seperation of chruch and state.", beside the corrected version a reader automatically understands; to Python, seperation and separation are different words](materials/lectures/images/ml1_readers.png)

Comments and posts written on the fly don't get an editor, so you become one without noticing. One comment
in our corpus begins "Seperation of chruch and state." You read *separation of church and state* and move
on; you don't stop to wonder what *govmt* or *obay* means. A computer does none of that. To Python,
*seperation* and *separation* are two different words, as different as *cat* and *dog*. That's why
cleaning text in code is worth slowing down for: it makes your invisible reading habits visible.

## You clean as you listen, too

<!-- IMG PROMPT (warm "Reading Room" oil painting — parchment, muted greens, one clay accent): two people in conversation; the words leaving the speaker are tangled with "ums" and crossed-out slips, and the words reaching the listener arrive as one smooth, clean line. Alt: A speaker's halting words becoming a smooth sentence by the time they reach the listener. -->

<!-- slide:
Someone says *um* every third word, picks the wrong word, mispronounces a name. You hear what they meant.

Speech-to-text has to make the same decisions: which *ums* to keep, which slips to fix.

*Every transcript is a cleaned version of what was said.*
-->

You do the same thing when you listen. Someone says *um* every third word, picks the wrong word,
mispronounces a name, and you hear what they meant. Speech-to-text software has to make those decisions
explicitly: which *ums* to keep, which slips to fix. Every transcript is a cleaned version of what was said.

## Today, you're the editor

<!-- layout: split -->

<!-- slide:
![Two real comments, "Separation of church and state…" and "Seperation of chruch and state.", pass through lower, split, and count, each step labeled a choice; the result counts separation, church, and state twice each under different spellings](materials/lectures/images/ml1_handoff.png)

In the code-along you'll try three string methods. Each one is a choice:

- `.lower()` — should *Constitution* and *constitution* count as one word?
- `.split()` — what counts as a "word"? What about *don't*, or *church-and-state*?
- `.replace()` — do you fix *seperation*? Who decides what's a typo?

**Every cleaning step is an edit. Comment why you made it.**
-->

![Two real comments, "Separation of church and state…" and "Seperation of chruch and state.", pass through lower, split, and count, each step labeled a choice; the result counts separation, church, and state twice each under different spellings](materials/lectures/images/ml1_handoff.png)

In the code-along you'll try three string methods, and each one is a choice. `.lower()` decides whether
*Constitution* and *constitution* count as one word. `.split()` decides what counts as a "word" at all —
what about *don't*, or *church-and-state*, or *state.* with its period still attached? `.replace()` lets you
fix *seperation*, which raises the question of who decides what's a typo. Run two real comments through
lowercasing, splitting, and counting, and three ideas come out as six different words. Every cleaning step
is an edit. Comment why you made it.
