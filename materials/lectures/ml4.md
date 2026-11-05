# AI Agency
## Borrow the tool — don't outsource the thinking

<!-- meta: Day 9 · the through-line -->


<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — aged parchment, muted greens, one clay accent; match the ml0 images): a person at a lamplit desk working the strings of a small wooden marionette that is typing at a tiny keyboard — the angle leaves it ambiguous who is moving whom; scattered manuscripts. -->
![A person at a desk working a small marionette that types at a keyboard — ambiguous who moves whom](materials/lectures/images/ml4_title.jpg)

<!-- slide:
You can now say *"write me ten lines of Python to score the sentiment
of these comments"* — and ten seconds later you have ten working lines.

The question isn't *can the machine write the code.* It plainly can.

### Do you understand it well enough to judge it?
-->

You can now turn to an AI and say *"write me ten lines of Python to score the sentiment of these
comments,"* and ten seconds later you have ten working lines. The question this course cares about isn't
*can the machine write the code* — it plainly can. It's the one you'll have to answer about every line it
hands you: **do you understand it well enough to judge it?**

## Borrow freely; read what you borrow

<!-- layout: split -->
![Diagram: our comments go into a black box marked with a question mark, and a number that looks right comes out. Below it, three questions: will it hold on real data, can you fix it when it breaks, can you say what it leaves out](materials/lectures/images/ml4_blackbox.png)

<!-- slide:
AI-assisted coding genuinely **lowers the barrier.** And borrowing
isn't new: programmers have always borrowed from manuals, colleagues,
and Stack Overflow. You'll lean on VADER, pandas, and Gensim all term.

The danger is borrowing **what you can't read.** Code you can't
explain is a **black box**: when it breaks, you can't fix it, and you
can't vouch for the thing with your name on it.

*Feeling powerful while growing more dependent: that's pseudo-agency.*
-->

AI-assisted coding genuinely **lowers the barrier**, and borrowing isn't new: programmers have always
borrowed from manuals, colleagues, and Stack Overflow, and you'll lean on VADER, pandas, and Gensim all
term. The danger is borrowing what you can't read. Code you can't explain is a **black box**: you can't
say whether it will hold on real data, or fix it when it breaks. The quieter failure is **pseudo-agency**:
feeling powerful ("I built this!") while growing more dependent, unable to vouch for the thing with your
name on it.

## Scaffold, not replacement

<!-- layout: split -->
![Chart: who is responsible for what. Used as a scaffold, you are responsible for the question, the definitions, the interpretation, and the explanation, and the AI only for the boilerplate. Used as a replacement, the AI is responsible for all of it, and nobody can explain it](materials/lectures/images/ml4_scaffold.png)

<!-- slide:
The line isn't "AI or no AI." It's **who's responsible for what.**

- **Scaffold:** the AI writes the boilerplate; *you're* responsible for
  the question, the definitions, the interpretation, and every line.
- **Replacement:** paste a prompt, paste the answer, submit.
  Nobody can explain it.

*The syllabus rule: explain any code you submit, and note in a #comment where AI helped and what you changed.*
-->

So the line isn't "AI or no AI." It's **scaffold vs. replacement**: who's responsible for what. As a scaffold,
the AI writes boilerplate while *you're* responsible for the question, the definitions, the interpretation,
and every line. As a replacement, you paste the answer and submit, and the AI has spoken *for* you. Hence the
syllabus rule: **explain any code you submit, and note in a `#comment` where AI helped and what you
changed.**

## Code is borrowed; your voice isn't

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — parchment, muted greens, clay accent): a split composition — on one side a person speaking, their own breath/voice rendered as flowing handwritten script; on the other side the same person as a ventriloquist's dummy, mouth open, the words trailing in from offstage. -->
![On one side a person speaking in their own hand; on the other a ventriloquist's dummy mouthing borrowed words](materials/lectures/images/ml4_ventriloquism.jpg)

<!-- slide:
**Learning a language** means studying what each piece does and
determining through *trial and error* how to adapt and fix it.

Output you can't explain is **ventriloquism**: the words come out
of your mouth, but someone else chose them.

Borrow (and credit) the code you need. But your reflections, your posts, and your
capstone essay *are* your voice, and a voice is forged in the friction
of finding your own words.

*Borrow the tool; never outsource the voice.*
-->

**Learning a language** means studying what each piece does and determining through *trial and error* how
to adapt and fix it. Output you can't explain is **ventriloquism**: the words come out of your mouth, but someone else chose them. Here the rule
flips. Nobody's voice lives in a stopword list: borrow (and credit) the code you need. But your reflections, posts, and
capstone essay *are* your voice, forged in the friction of finding your own words. Let an AI write your
code and you've saved time; let it write your prose and you've handed away the one thing this course
exists to grow. **Borrow the tool; never outsource the voice.** (Ted Chiang calls ChatGPT "a blurry JPEG
of the web." A voice worth having is the opposite of a blur.)

## Eloquence is not evidence

<!-- layout: split -->
![Schematic chart, not measured. Before: the more work behind a piece of writing, the more polished it reads. Now: checked and invented claims read equally polished](materials/lectures/images/ml4_fluency.png)

<!-- slide:
The machine's writing is **fluent** whether it's right or wrong.

Polished prose used to be expensive, so polish hinted at the work
behind it. Now fluency is free, and an invented claim reads
*exactly* like a checked one.

Stephen Colbert's word for this is **truthiness**: believing a claim
is true because it *feels* true, without regard to evidence, logic,
or facts.

*Truthiness runs from ignorant assertion to deliberate propaganda.*
-->

The machine's writing is **fluent** *whether it is right or wrong.* Polished prose used to be expensive,
so polish was a rough proxy for the work behind it. Language models broke that link: fluency is free, and
an invented claim reads exactly like a checked one. Our instincts haven't caught up; a well-made paragraph
still *feels* vetted. Stephen Colbert's word for that feeling is **truthiness**: believing a claim
is true because it feels true, without regard to evidence, logic, or facts. It can range from ignorant
assertions of falsehoods to deliberate propaganda meant to sway opinion.

## Not lying. Something else.

<!-- layout: split -->
![Three cards after Harry Frankfurt: the honest speaker knows the truth and tells it; the liar knows the truth and hides it; the bullshitter doesn't care what's true, only what lands](materials/lectures/images/ml4_frankfurt.png)

<!-- slide:
Harry Frankfurt: the liar still cares about the truth, enough to hide
it. The **bullshitter** doesn't care what's true, only what lands.

Some philosophers argue "hallucination" is the wrong word for AI errors:
a model has *no regard for truth at all*, even when it's right.

*You needn't accept the label to take the point: fluency can't count as evidence.*
-->

Philosophy has a blunter word. Harry Frankfurt distinguished the **liar**, who knows the truth and hides
it, from the **bullshitter**, who doesn't care what's true, only what lands. Hicks, Humphries and Slater
(2024) argue that "hallucination" is the wrong name for AI errors: a model produces plausible next words,
and when they're true, that's incidental. You needn't accept their label to take the point: fluency can't
count as evidence.

## An old problem, with a Greek name

<!-- layout: split -->
![The Day 1 pipeline with only the final arrow, from knowledge to wisdom, lit](materials/images/pipeline_hl_wisdom.png)

<!-- slide:
In Plato's *Gorgias*, the rhetorician boasts he'd out-argue a doctor
about medicine, before an audience that knew no medicine.

Plato calls the conflict between rational judgment and our pleasures
and pains a profound **amathia**, or ignorance (*Laws* 689a–b). For this
course, **"un-wisdom"** names a related danger: having information and
assistance without exercising judgment.

*Day 1's last arrow, failed: knowledge that never becomes wisdom.*
-->

None of this is new. In Plato's *Gorgias*, Gorgias boasts that a skilled speaker would beat a physician
in a debate about medicine, before an audience that knew no medicine (*Gorgias* 456b–c, 459a–b), because
eloquence feels like expertise from the inside. Plato calls the conflict between rational judgment and our
pleasures and pains a profound **amathia**, or ignorance (*Laws* 689a–b). For this course, **"un-wisdom"**
names a related danger: having information and assistance without exercising judgment. It's the last arrow
on the Day 1 diagram, failed: knowledge that never becomes wisdom, because the labor between them got
outsourced.

## The fix is friction

<!-- slide:
run the code.
check the citation.
find the source.
read it line by line.
::: col
**Amathia points at us, never at them.** It isn't a diagnosis for the
commenters collected in our dataset. It's the temptation *you* face whenever an
eloquent answer arrives faster than your judgment.

An attitude ("trust AI less") won't beat a gut habit. A **procedure** will.

*Right next to "the score is never the meaning": eloquence is not evidence.*
-->

Two things follow. **Amathia points at us, never at them**: it isn't a diagnosis for the commenters collected in
our dataset or anyone across a political argument; it's the temptation *you* face when an eloquent answer
arrives faster than your judgment. And the fix isn't an attitude ("trust AI less"), which won't beat a gut
habit. It's **procedural friction**: run the code, check the citation, find the source, read it line by
line. Keep it next to *the score is never the meaning*: **eloquence is not evidence.**

## Today: read the code

<!-- layout: split -->
![Bar chart from our 93 comments: count_words returns five separate keys for one word — lowercase commandments 13, capitalized Commandments 7, then Commandments with a period 3, with a question mark 1, and with a comma 1 — 25 in all](materials/lectures/images/ml4_counter.png)

<!-- slide:
```
def count_words(text):
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```

It runs. It looks finished. What is `word` on each pass?
What does `.get(word, 0)` do?

*Today's lab: two pieces of AI-written code. Both run without an error. Both are wrong.*
-->

That's today's lab: two pieces of **AI-written code** to read line by line, test on our comments, and
improve. Both run without an error. Both are wrong. Here's the kind of word counter an AI will write for
you:

```
def count_words(text):
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```

It runs and looks finished. But what is `word` on each pass? What does `.get(word, 0)` do? (You
hand-built this function in the Dictionaries & Functions code-along, with an `if`/`else` where the `.get`
is.) And on our 93 comments, `.split()` keeps capitals and punctuation, so "commandments" comes back as
five keys: ask for `counts["commandments"]` and you get 13, where a reader sees the word 25 times.

## What understanding looks like

<!-- layout: split -->

<!-- slide:
![A person at a desk working a small marionette that types at a keyboard — ambiguous who moves whom](materials/lectures/images/ml4_title.jpg)

You understand code when you can:

- say what each line takes in and hands back
- name the type of each important variable
- predict what an unusual input will do
- name one thing it gets wrong
- change one thing, and test that it worked

### Learning to think computationally, or outsourcing the thinking?

*Make the choice visible: cite the AI, and say what you changed.*
-->

You understand code when you can say what each line takes in and hands back, name the type of each
important variable, predict what an unusual input will do, name one thing it gets wrong, and change one
thing and test that it worked. Carry one question out of here: **are you learning to think
computationally, or outsourcing the thinking?** The same tool allows either. As always: **make the choice
visible**: cite the AI, and say what you changed.

Going deeper (optional): Douglas Rushkoff, *Program or Be Programmed*; Ted Chiang, "ChatGPT Is a Blurry
JPEG of the Web" (*The New Yorker*, 2023); Nick Montfort, *Exploratory Programming for the Arts and
Humanities*; Harry Frankfurt, *On Bullshit* (2005); Michael Townsen Hicks, James Humphries & Joe Slater,
"ChatGPT Is Bullshit" (*Ethics and Information Technology*, 2024); Plato, *Gorgias* (the original argument
about persuasion without knowledge).
