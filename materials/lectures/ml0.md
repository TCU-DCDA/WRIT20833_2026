# Humanities & Coding
## Why a humanist learns to code

<!-- meta: ML0 · Day 1 · the through-line -->

<!-- layout: split -->

![A warm oil painting of a hand with a quill turning cursive manuscript lines into ordered rows of abstract printed characters](materials/lectures/images/humanities_coding_script_to_structure.jpg)

Before we write a single line of code, a question: **what do you do with knowledge that can't be
measured?**

That question *is* the humanities. Love and grief, justice and beauty, the meaning of a poem or a
protest — the things that matter most about being human tend to be exactly the things that resist a
number. This course is going to spend four weeks turning human language *into* numbers. So let's be
honest, on day one, about what that does and doesn't get us.

## The human mess

<!-- layout: split -->

![A warm sepia painting of the humanities — a bust, a seated thinker, a portrait on an easel, a guitar, a theatre mask, and scattered manuscripts](materials/lectures/images/messy_humanities.jpg)

The humanities study the **mess** of the human condition — and they don't tidy it up. They explore it.

- **Contradiction** — we hold conflicting values at once; we can love and resent the same person.
- **Ambiguity** — a text means more than one thing. Is Hamlet mad, or pretending?
- **Subjectivity** — experience shapes interpretation; beauty and justice look different from different lives.

The sciences reduce complexity to principles — one elegant law that explains every case. The humanities
do something else: they **map the contours of the complexity itself.** Where other fields see noise to
filter out, we often see the signal. The poet John Keats called the needed temperament *negative
capability* — being "in uncertainties, mysteries, doubts, without any irritable reaching after fact and
reason." Hold onto that phrase; this whole course lives inside it.

## So why learn to code?

Here is the productive tension you'll feel all month:

> **Code wants to categorize, measure, and systematize. Culture is ambiguous, contextual, and messy.**

Can a sentiment score capture the nuance of a sarcastic comment? What gets lost when we flatten a heated
public argument into one average number? Who decides which categories matter when we collect data? These
aren't bugs in the software — they're *humanities questions*, and a humanist is exactly the person
equipped to ask them.

So we don't learn to code in order to stop thinking like humanists. We learn it to **bring humanities
questions to computational methods** — to hear more voices than close reading alone could ever reach,
while staying honest about what the counting flattens. That double move — listen at scale, *and* refuse
the false tidy answer — is the whole course.

## What it looks like in the wild

Before the cautions, the payoff — real projects that turn a pile of culture into a pattern you can
suddenly *see*. Start with two that count words much the way you soon will:

<!-- layout: gallery -->

- ["Trucks and Beer"](https://www.johnwmillr.com/trucks-and-beer/) — counts what country songs *actually* sing about (turns out, not just trucks and beer).
- [Gendered Language in Teacher Reviews](https://benschmidt.org/profGender/) — the same words land very differently depending on the professor's gender.

![Scatter plot — mentions of "girl" vs. "love" across popular country songs, colored by artist gender (the "Trucks and Beer" analysis)](materials/lectures/images/proj_country_love.png)

![Dot plot — words from 14 million RateMyProfessor reviews split by professor gender (Ben Schmidt, "Gendered Language in Teacher Reviews")](materials/lectures/images/proj_teacher_reviews.png)

## A few more worth a look

No screenshots — these are worth visiting live:

- [Every Noise at Once](https://everynoise.com/) — a navigable map of 6,000+ music genres, drawn from audio analysis.
- [The Pudding, "The Largest Vocabulary in Hip-Hop"](https://pudding.cool/2017/02/vocabulary/) — ranks rappers by how many unique words they use.
- [Open Syllabus](https://opensyllabus.org/) — maps millions of college syllabi; Plato is assigned more than any other author on earth.

Notice the move every one of them makes: a question about *people* comes first, then the counting. The
tool serves the question — never the other way around.

## Use the programs, or shape them

Two writers worth hearing on *why* a humanist bothers with this at all.

> The underlying capability of the computer era is actually programming — which almost none of us know how to do. We simply use the programs that have been made for us, and enter our text in the appropriate box on the screen… This means [we] have access to the capabilities given to [us] by others, but not the power to determine the value-creating capabilities of these technologies for [ourselves].

— Douglas Rushkoff, *Program or Be Programmed* (qtd. in Nick Montfort, *Exploratory Programming for the Arts and Humanities*, 327–28)

Nick Montfort names the upside just as plainly: learning to code in the humanities lets us **think in new
ways**, **understand culture and media systems** more deeply, and maybe even **help improve society.** You
don't have to leave here a programmer. But knowing what's inside the box — even a little — is the
difference between *using* the tools that sort our culture and being able to *question* them.

## The score is never the meaning

<!-- layout: split -->

Look at this diagram. We'll come back to it every week.

![The noumena-to-wisdom pipeline: noumena, phenomena, raw data, structured data, analyzed data, insight, knowledge, wisdom](materials/images/noumena_to_wisdom_pipeline.png)

It begins much further from "the truth" than you'd guess. At the top sits the *noumenon* — the
philosopher Immanuel Kant's word for a thing **as it actually is**, the whole lived human fact. A woman
in Texas reads that her child's classroom will display the Ten Commandments and feels something complete
and entirely her own. We will never have that feeling. What we *can* have is what she typed — a comment, already a lossy,
public projection of an inner state. Then we **scrape** it (and some comments are missed), **clean** it
(we choose what counts as a "word"), **model** it (a tool decides what "great" means), and only *then* do
we reach for **insight, knowledge,** and — maybe, by the end — **wisdom.**

## Every arrow is a choice

<!-- layout: split -->

![A warm oil painting of a hand reaching to turn one of several brass valves along a pipe carrying flowing golden light](materials/lectures/images/every_arrow_valves.jpg)

**Every arrow on that diagram is a human decision** — not a neutral pipe, but a choice, with a person and
a value behind it. It's tempting to call each step *contamination*, as if a clean signal up top got
dirtied on the way down. But look again: there *is* no clean signal up top. The very first step is
already an interpretation. **Bias isn't what sneaks into the data — bias is the material the data is made
of.**

That's not cause for despair, and it's not a reason to distrust everything. It's the reason for the one
habit this course asks of you constantly: **make your choices visible.** Every time you delete a word,
set a threshold, or name a topic, you'll leave a `#comment` saying what you did and why. The honest move
isn't pretending you found the truth; it's showing your work so someone else can see where you stood.

## What this course is really grading

This is why we don't grade you on clean code. **Insight, knowledge, wisdom** aren't outputs you can
compute — they're what's left after you've been honest about every arrow above them. By your final
reflection, the question won't be *"did you get the right answer?"* It will be **"do you understand
everything you chose along the way?"**

The humanities aren't about solving the mess of being human. They're about understanding it — and now,
with a new set of tools, understanding it at a scale you could never reach by hand.
