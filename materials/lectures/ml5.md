# Collective Memory
## What a culture keeps, and what it lets go

<!-- meta: Day 4 · the through-line -->

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — aged parchment, muted greens, one clay accent; match the ml0 images): a tall wall of wooden card-catalog drawers; a few drawers hang open, spilling warm handwritten letters and old photographs into the light, while most stay sealed shut — memory as a thing that keeps some of us and loses the rest. -->
![A wall of wooden card-catalog drawers, a few open and spilling letters and photographs into the light](materials/lectures/images/ml5_title.jpg)

<!-- slide:
![A wall of wooden card-catalog drawers, a few open and spilling letters and photographs into the light](materials/lectures/images/ml5_title_sq.jpg)

Today: **lists** and **loops** — how to hold many things at once,
and how to do the same thing to every one of them.

That's the technical skill. The human story underneath it is **memory**:
who gets remembered, who gets forgotten, and what changes when
the record is kept by a machine that keeps whatever it is given.
-->

Today you learn **lists** and **loops** — how to hold many things at once, and how to do the same thing to
every one of them. That's the technical skill. The human story underneath it is **memory**: who gets
remembered, who gets forgotten, and what changes when the record is kept by a machine that keeps whatever it
is given.

```
violations = []
for person in community:
    if person["broke_a_rule"]:
        violations.append(person)
```

A list, a loop, a condition — and a community that now keeps a permanent record of everyone who ever broke
one of its rules. Let's talk about what that does.

## Two kinds of memory

<!-- layout: split -->

<!-- slide:
![A flow diagram: a row of people passes one at a time through "for person in community", then the check "if this person broke a rule"; three rule-breakers drop into a box labelled violations, "appended, and kept"; everyone else passes on with "no record kept"](materials/lectures/images/ml5_loop.png)

```
violations = []
for person in community:
    if person["broke_a_rule"]:
        violations.append(person)
```

A list, a loop, a condition — and a community
that now keeps a **permanent record** of everyone
who ever broke one of its rules.
-->

<!-- slide:
![A schematic line chart, not measured data: over twenty years after a bad day, a village's memory of it fades toward nothing, while a database keeps the record flat, exactly as written](materials/lectures/images/ml5_memory.png)

For most of history, a community's memory was **human**, and it forgot.

- **People forget, a little at a time.** Details fade. Stories soften
  as they're retold. Someone gets a second chance.
- **A database keeps the row as it was written.** Ten years on it
  reads the same, and it can still turn up in a background check.
-->

<!-- slide:
### But computers lose things too

- **Corruption doesn't care what it hits.** Flip one byte in the wrong
  place and the whole file won't open. Flip another and nothing changes.
- **Platforms disappear.** In 2019, MySpace lost roughly twelve years
  of uploaded music in a server migration, all at once.

People forget the details and keep the gist. Machines keep every
detail exactly, until they keep nothing.
-->

<!-- slide:
That shift, from a memory that forgets **gradually** to one that
keeps everything until it loses it all at once, is what this lecture
is about. A machine can lose a record. It can't **forgive** one.

### Forgetting was never only a failure. It is also how people get a second chance.
-->

For most of human history, a community's memory was a **human** thing — and being human, it forgot.

![A schematic line chart, not measured data: over twenty years after a bad day, a village's memory of it fades toward nothing, while a database keeps the record flat, exactly as written](materials/lectures/images/ml5_memory.png)

- **People forget, a little at a time.** Details fade. Stories soften with each retelling. Someone gets a
  second chance, and the village eventually lets a thing go.
- **A database keeps the row exactly as it was written.** A record doesn't mellow with age. Ten years on it
  reads the same, and it can still turn up when you apply for a job, an apartment, or a loan.

Computers do lose things, but not the way people do. When data is corrupted, the damage doesn't care what
it hits: flip one byte in the wrong place and a whole file won't open; flip another and nothing visibly
changes. Platforms disappear, too. In 2019 MySpace admitted that roughly twelve years of music its users had
uploaded was lost in a server migration, all at once. People forget the details and keep the gist. Machines
keep every detail exactly, until they keep nothing.

That shift, from a memory that forgets gradually to one that keeps everything until it loses it all at once,
is what this lecture is about. A machine can lose a record. It can't forgive one. Forgetting was never only a
failure. It is also how people get a second chance.

## A list is a population

<!-- slide:
![Distinct individuals being threaded onto one long ledger-line like beads, separate faces becoming rows in a register](materials/lectures/images/ml5_population_sq.jpg)

> `community = ["Mary", "John", "Kate", "Ahmed", "Rosa", ...]`

Notice what just happened. A moment ago these were **people.**
Now they're a **population** — a thing you can sort, filter, slice,
and count all at once.

This week your own posts will become a list like this:
**names removed, persona kept, one post per item.**
-->

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — parchment, muted greens, clay accent): a crowd of distinct individuals, each one being threaded onto a single long ledger-line like beads on a string — separate faces becoming uniform rows in a register. -->
![Distinct individuals being threaded onto one long ledger-line like beads, separate faces becoming rows in a register](materials/lectures/images/ml5_population.jpg)

A list looks like the most harmless thing in Python:

> `community = ["Mary", "John", "Kate", "Ahmed", "Rosa", ...]`

But notice what just happened. A moment ago these were people. Now they're a **population** — a thing you
can sort, filter, slice, and count all at once.

This week you'll watch that happen to your own writing. At the end of class today you'll each write a short
post in a role-play discussion, and on Wednesday those posts become a Python list: names removed, persona
kept, one post per item. Whatever the record doesn't have a place for — who wrote it, what they meant by
it, what they'd say if asked again — it doesn't keep.

The list treats every item the same. That move is enormously powerful (it's how you'll hear a hundred voices
at once) and quietly dangerous (it's how a crowd of people becomes a single number someone can act on).

## A loop is a verdict, repeated

<!-- layout: split -->

<!-- slide:
A village elder judged **case by case** — knowing the person, weighing
the circumstances, leaving room for an exception.

```
for person in population:
    apply_the_same_rule(person)
```

A loop applies one rule to every item, the same way,
thousands of times a second.
-->

<!-- slide:
![The number line from Classification Logic, scores 646 to 654, with a dashed line at 650. Above it, a loop that approves every applicant whose score is over 650, and an arrow: the loop asks each one the same question. 646 through 650 land on review, 651 through 654 on approve. A note on 649 and 650: no second look, unless someone wrote one in.](materials/lectures/images/ml5_loopline.png)

"The same rule for everyone" *sounds* like the definition of fairness.
It is fair in one way: nobody gets special treatment.

It also means nobody gets a second look.
A loop can't make an exception unless someone wrote the exception in first.

*Remember the 650 loan cutoff from Classification Logic?
A loop is how that one line reaches every applicant in the file.*
-->

A village elder judged **case by case** — knowing the person, weighing the circumstances, leaving room for
the exception, the second look. A loop doesn't.

```
for person in population:
    apply_the_same_rule(person)
```

A `for` loop applies one rule to every item in a list, the same way, thousands of times a second. A loop makes
no mistakes in the usual sense: it does exactly what the rule says, to every item. "The same rule for everyone"
*sounds* like the definition of fairness, and in one way it is: nobody gets special treatment. It also means
nobody gets a second look. A loop can't make an exception unless someone wrote the exception in first.
Remember the 650 loan cutoff from *Classification Logic*? A loop is how that one line reaches every applicant
in the file.

![The number line from Classification Logic, scores 646 to 654, with a dashed line at 650. Above it, a loop that approves every applicant whose score is over 650, and an arrow: the loop asks each one the same question. 646 through 650 land on review, 651 through 654 on approve. A note on 649 and 650: no second look, unless someone wrote one in.](materials/lectures/images/ml5_loopline.png)

## The power to count

<!-- layout: split -->

<!-- slide:
Counting feels neutral — you're just tallying what's there.

But someone has to **choose the categories** first,
and choosing categories is choosing what's worth seeing.

> `Counter(violations).most_common()`

*One line, and a messy human record becomes a ranked list of "what's wrong here."*
-->

<!-- slide:
A `Counter` reports only the categories it was given.
Anything that fits none of them **doesn't appear in its output at all.**

So ask:

- Who chose the categories?
- Who gets to see the tally?
- When does a count become a **reason** — for a policy, a denial, a crackdown?

### And what happened to the people who fit no category, and so were never counted at all?
-->

Counting feels neutral — you're just tallying what's there. But someone has to **choose the categories**
first, and choosing categories is choosing what's worth seeing.

> `Counter(violations).most_common()`

One line, and a messy human record becomes a ranked list of "what's wrong here." A `Counter` reports only
the categories it was given. Anything that fits none of them doesn't appear in its output at all.

So ask: who chose the categories? Who gets to see the tally? When does a count become a *reason* — for a
policy, a denial, a crackdown? And the question from *Connotations & Code* that never goes away: what happened
to the people who fit no category, and so were never counted at all?

## Historical echoes

<!-- slide:
![A 19th-century almshouse records office, clerks reducing waiting people to ledger entries that dissolve into modern data-rows](materials/lectures/images/ml5_echoes_sq.jpg)

None of this is new. Only the machinery is.

The [**Bellevue Almshouse**](http://web.archive.org/web/20200216100344/http://www.nyuirish.net:80/almshouse/public-health-in-new-york-city/),
on Manhattan's East River, was New York City's hospital, poorhouse,
and asylum in one: where the city sent people who couldn't pay for care.

During the [Irish Famine](http://web.archive.org/web/20200221165339/http://www.nyuirish.net:80/almshouse/irish-immigration-to-19th-century-new-york/)
(1845–52), over a million Irish emigrants landed in New York.
Many who fell ill or ran out of money ended up at Bellevue,
and a clerk wrote each one into a ledger.

The historian Anelise Shrout describes what records like these were *for*:
-->

<!-- slide:
> Nineteenth-century immigration data was produced with the express purpose
> of reducing people to bodies; bodies to easily quantifiable aspects; and
> assigning value to those aspects which proved that the marginalized people
> to [whom] they belonged were worth less than their elite counterparts.

— Anelise Hanson Shrout, ["(Re)Humanizing Data"](https://crdh.rrchnm.org/essays/v01-10-re-humanizing-data/), *Current Research in Digital History* 1 (2018)
-->

<!-- slide:
Before counting anything, read the rows. These are the first 8 of the
12,110 in the file Shrout published (5 of its 11 columns):

```
date_in     age  gender  occupation  disease
1847-05-31   54  m       laborer     destitution
1847-05-19   91  m       laborer     destitution
1847-06-02   25  m       NA          recent emigrant
1847-03-03   51  m       laborer     recent emigrant
1847-05-22   28  m       laborer     recent emigrant
1847-05-27   35  m       laborer     lame
1847-05-27   63  m       laborer     recent emigrant
1847-05-27   40  m       laborer     destitution
```

"disease" is the ledger's own heading. `NA`: nothing was recorded.
[See all 12,110 rows](https://github.com/shrouta/bellevue_R_script/blob/master/bellevue_for_R.csv)
-->

<!-- slide:
The first row, as a Python dictionary:

```
{"date_in": "1847-05-31", "age": 54,
 "occupation": "laborer", "disease": "destitution"}
```

Now run a loop and a `Counter` over the "disease" entry
in all 12,110 rows.
-->

<!-- slide:
![A bar chart of the Bellevue Almshouse ledger's "disease" column, Irish-born admissions 1845 to 1847, counted with Counter: sickness 4,284; recent emigrant 3,147; destitution 1,616; intemperance 450; sore limb 356; pregnant 335; insane 327; fever 225. "Recent emigrant" and "destitution" are highlighted: being poor and being newly arrived, filed as diseases.](materials/lectures/images/ml5_ledger.png)

After "sickness," the two most common entries are:

- **recent emigrant** — 3,147
- **destitution** — 1,616

Being poor, and being an immigrant on public aid,
entered under "disease."

### The tools changed. The power to reduce, sort, and leave people out did not.
-->

<!-- layout: split -->
<!-- IMG PROMPT (warm sepia oil painting — aged parchment tones, muted greens, clay accent; recompose F25's then/now idea but keep it warm, not blue/neon): a 19th-century almshouse records office, clerks at wooden desks reducing a line of waiting people to entries in heavy ledgers; the ledger rows trail off to the right and dissolve into an endless stream of identical modern data-rows. -->
![A 19th-century almshouse records office, clerks reducing waiting people to ledger entries that dissolve into modern data-rows](materials/lectures/images/ml5_echoes.jpg)

None of this is new. Only the machinery is.

The [Bellevue Almshouse](http://web.archive.org/web/20200216100344/http://www.nyuirish.net:80/almshouse/public-health-in-new-york-city/),
opened in 1816 on Manhattan's East River, was New York City's hospital, poorhouse, and asylum in one. People
who could pay went to private hospitals; Bellevue was where the city sent everyone else: the sick poor,
orphans, people judged insane, victims of contagious disease. During the
[Irish Famine](http://web.archive.org/web/20200221165339/http://www.nyuirish.net:80/almshouse/irish-immigration-to-19th-century-new-york/)
of 1845–52, over a million Irish emigrants landed in New York. Many who fell ill or ran out of money after
arriving ended up at Bellevue, and a clerk wrote each one into an admissions ledger. (In May 1847 the city and
state created a Commission of Emigration with its own hospitals, and
[Irish admissions to Bellevue fell sharply](http://web.archive.org/web/20200216100354/http://www.nyuirish.net:80/almshouse/the-irish-in-bellevue/).)

The historian Anelise Shrout describes what records like these were *for*:

> Nineteenth-century immigration data was produced with the express purpose of reducing people to
> bodies; bodies to easily quantifiable aspects; and assigning value to those aspects which proved that the
> marginalized people to [whom] they belonged were worth less than their elite counterparts.
>
> — Anelise Hanson Shrout, ["(Re)Humanizing Data: Digitally Navigating the Bellevue Almshouse"](https://crdh.rrchnm.org/essays/v01-10-re-humanizing-data/), *Current Research in Digital History* 1 (2018)

Those ledgers were transcribed in 2004–06 for NYU's Digital Almshouse Project, and Shrout cleaned the
transcription and [published it as data](https://github.com/shrouta/bellevue_R_script): 12,110 admissions of
Irish-born people between 1845 and 1847. Before counting anything, read some rows. Here are the file's first
eight, showing five of its eleven columns:

```
date_in     age  gender  occupation  disease
1847-05-31   54  m       laborer     destitution
1847-05-19   91  m       laborer     destitution
1847-06-02   25  m       NA          recent emigrant
1847-03-03   51  m       laborer     recent emigrant
1847-05-22   28  m       laborer     recent emigrant
1847-05-27   35  m       laborer     lame
1847-05-27   63  m       laborer     recent emigrant
1847-05-27   40  m       laborer     destitution
```

"disease" is the heading the ledger itself used (the file calls its cleaned version `reason_cleaned`), and
`NA` means nothing was recorded. You can [read all 12,110 rows](https://github.com/shrouta/bellevue_R_script/blob/master/bellevue_for_R.csv).
Here is the first one as a Python dictionary:

```
{"date_in": "1847-05-31", "age": 54, "occupation": "laborer", "disease": "destitution"}
```

Run a loop and a `Counter` over the "disease" entry in every row, and after "sickness" the two most common
entries are **recent emigrant** (3,147) and **destitution** (1,616). Being poor, and being an immigrant on
public aid, were entered under "disease." ("Recent emigrant" did not measure time in the city: the project
read it as marking people bonded to shipping firms who were now relying on the city's aid; see the archived
[Digital Almshouse Project](http://web.archive.org/web/20200218041124/http://www.nyuirish.net:80/almshouse/disease/).
Its counts come from an earlier version of the data, so they differ from the ones here.) Notice where that
link goes: we can read the project's website only because the Internet Archive saved a copy. The paper
ledger has survived since 1847. The website built to study it is already gone.

![A bar chart of the Bellevue Almshouse ledger's "disease" column, Irish-born admissions 1845 to 1847, counted with Counter: sickness 4,284; recent emigrant 3,147; destitution 1,616; intemperance 450; sore limb 356; pregnant 335; insane 327; fever 225. "Recent emigrant" and "destitution" are highlighted: being poor and being newly arrived, filed as diseases.](materials/lectures/images/ml5_ledger.png)

**The tools changed. The power to reduce, sort, and leave people out did not.** When you write your own loops
this week, you're picking up a very old instrument.

## What we choose to keep

<!-- slide:
Lists and loops are how a culture decides **what it keeps and what it lets go** —
and now you're one of the people writing them.

Today you'll write the first entries in a small class record.
On Wednesday we'll look at what survived the trip into data.

### Am I remembering these people, or just reducing them?
-->

So lists and loops were never just technical skills. They're how a culture decides **what it keeps and what
it lets go** — and now you're one of the people writing them.

At the end of class today you'll write the first entries in a small class record. On Wednesday we'll look at
what survived the trip into data, and what didn't. Here, and every time you count and sort people's words
this term, keep the live question open: *am I
remembering these people, or just reducing them?* And the one the whole course keeps asking — **make the
choice visible.** What you keep, what you drop, and what you let stay forgotten is an argument; leave the
`#comment` that admits it.

Going deeper (optional): Paul Connerton, *How Societies Remember*; Viktor Mayer-Schönberger, *Delete: The
Virtue of Forgetting in the Digital Age*; José van Dijck, *Mediated Memories in the Digital Age*.

## Your turn: a class record

<!-- slide:
**The proposal** *(made up for this activity)*: the library will convert one of its quiet study
floors into a collaborative workspace — group tables, whiteboards, talking allowed.

- **Take a persona card.** Write as that person, not as yourself.
- **Now, in D2L** (*The Quiet Floor*): start a thread, subject = your card's code. 40–60 words: one concrete thing you need, and how this would help, hurt, or not matter.
- **By Tuesday 11:59 p.m.:** reply to a *different* persona, 20–40 words.

Like Bellevue's clerks, we'll choose the columns: the post, the persona, what it replied to.
Your name won't be one of them.

### Write it yourself, and take the person on your card seriously.
-->

At the end of class you'll start a small record of your own. The proposal, made up for this activity: *the
library will convert one of its quiet study floors into a collaborative workspace (group tables,
whiteboards, talking allowed), open the same hours as the rest of the building.* Each of you gets a persona
card. Writing as that person, you'll post a short response in the D2L discussion *The Quiet Floor* during
class, and reply to a different persona by Tuesday at 11:59 p.m. The full instructions are in the D2L topic.

Write it yourself, without AI, and take the person on your card seriously: their circumstances, not a
stereotype of them. On Wednesday these posts become our practice data. Like Bellevue's clerks, we'll choose
the columns: the post, the persona, and what it replied to. Your name won't be one of them.
