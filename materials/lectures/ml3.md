# Classification Logic
## Whose categories? Sorting as judgment

<!-- meta: Day 3 · the through-line -->


<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — aged parchment, muted greens, one clay accent; match the ml0 images): a road forking like an if/else branch, with a gate at the split; an unseen hand waves a line of varied human figures left or right — sorting people into two paths. -->
![A road forking like an if/else branch, a gate at the split sorting a line of people left or right](materials/lectures/images/ml3_title.jpg)

<!-- slide:
![A road forking like an if/else branch, a gate at the split sorting a line of people left or right](materials/lectures/images/ml3_title_sq.jpg)

Today you learn `if`, `else`, and the booleans that drive them.

Most `if`s are plumbing: *is the file empty? is this a number?*
But the same basic logic decides who gets the loan, the match,
the apartment, the interview, the flag.

**When an `if` decides something about a person, it is sorting people —
and sorting is never neutral. Someone drew the line.**
-->

Today you learn `if`, `else`, and the booleans that drive them — `True` and `False`, greater-than and
equals. Most of the `if`s you'll ever write are plumbing: is the file empty, is this value a number. But the
same basic logic sits at the end of the systems that decide who gets the loan, the match, the apartment, the
interview, the flag.

This lecture is the humanities frame for the syntax you're about to practice. Because when an `if` decides
something about a *person*, it is **sorting people** — and sorting is never neutral. Someone drew the line.

## To classify is to judge

<!-- slide:
A category is a decision: **this counts as the same; that counts as different.**
Drawing the box is an act of judgment before it is ever an act of code.

- Put "single mother," "widow," and "divorced dad" in one bin marked
  *non-traditional household* — you've made an argument about what
  *traditional* is supposed to mean
- Mark a comment "positive" or "negative" — you've flattened a mixed,
  sarcastic, grieving, joking sentence into one of two boxes
-->

<!-- slide:
### Sort these yourself.

Positive, negative, or neutral? Hands up.

> "the bill of right says freedom of religion, not freedom from religion"

> "Seems pretty clear cut. If schools are government funded = keep your religion at home"

> "Anyone who thinks teaching kids about morality is a bad idea should have zero input on raising children!"

*Where did the room disagree? That disagreement is what a category hides.*
-->

<!-- slide:
### There is no neutral box.

Every classification system encodes **values** — about what matters,
what counts, and who belongs where.

*The last lecture said code is not neutral.
Classification is where you will feel it most directly.*
-->

A category is a decision: **this counts as the same; that counts as different.** Drawing the box is an act
of judgment before it is ever an act of code.

- Put "single mother," "widow," and "divorced dad" in one bin labeled *non-traditional household* and
  you've made an argument about what *traditional* is supposed to mean.
- Mark a comment "positive" or "negative" and you've flattened a person's mixed, sarcastic, grieving,
  joking sentence into one of two boxes.

Try it on three real comments from our file. Is *"the bill of right says freedom of religion, not freedom
from religion"* positive, negative, or neutral? What about *"Anyone who thinks teaching kids about morality
is a bad idea should have zero input on raising children!"* Where a room of careful readers disagrees, a category has to pick one answer anyway.

There is no neutral box. Every classification system encodes **values** — about what matters, what counts,
and who belongs where. The Connotations lecture said code is not neutral; classification is where you will
feel it most directly.

## Status has long gated access

<!-- slide:
Long before computers, a status decided which doors opened:
*noble* or *commoner*, *citizen* or *foreigner*, *insider* or *outsider*.

The variable was social — but it often worked like a boolean.
**One bit, and the gate swung open or stayed shut.**
-->

<!-- slide:
The software era didn't invent the gate. It **automated** it,
and renamed the variables:

> `credit_score` · `criminal_background` · `employment_status` · `immigration_status`

The same logic, renamed: a value about a person, checked at a threshold,
deciding what they get to reach.

*What changed is scale, speed — and that the judgment now hides
inside a function that looks like math.*
-->

Long before computers, a status decided which doors opened: *noble* or *commoner*, *citizen* or
*foreigner*, *insider* or *outsider*. The variable was social, and it often worked like a boolean — one bit,
and the gate swung open or stayed shut.

The software era didn't invent the gate. It **automated** it, and renamed the variables:

> `credit_score` · `criminal_background` · `employment_status` · `immigration_status`

The same logic, renamed: a value about a person, checked at a threshold, deciding what they get to reach.
What changed is scale and speed — and that the judgment now hides inside a function that looks like math.

## The threshold problem

<!-- slide:
![A number line from 646 to 654 with a dashed line between 650 and 651: 646 through 650 are marked "review," 651 through 654 "approve"; a note says 650 itself is turned away because the code uses > rather than >=](materials/lectures/images/ml3_threshold_line.png)

A simplified loan rule, in the syntax you'll write this week:

```
credit_score = 649
income = 72000
if credit_score > 650 and income > 50000:
    decision = "approve"
else:
    decision = "review"
```

**Who chose 650?** Is the person at 649 really different from the person at 651?

*And the person at exactly 650? `>` says review. `>=` would say approve.
Someone chose that symbol, too.*
-->

<!-- slide:
![Two bars of the same 123 rows: with VADER's standard cutoffs of plus or minus 0.05, 34 negative, 38 neutral, 51 positive; with stricter cutoffs of plus or minus 0.5, 17 negative, 76 neutral, 30 positive](materials/lectures/images/ml3_cutoffs.png)

A threshold is the most ordinary line in programming,
and one of the most consequential.

### It is an act of judgment that looks like arithmetic.

In HW3 you'll sort our comments with **two** cutoffs on VADER's score
(−1 to +1): **≥ 0.05** is positive, **≤ −0.05** is negative, everything between is neutral.

Move those lines to ±0.5 and "neutral" doubles — same rows, same scores.
-->

<!-- slide:
![A hand turning a brass dial on a gate; people just above the mark pass into light, those just below are turned away](materials/lectures/images/ml3_threshold_sq.jpg)

Two real rows from our file, a hair apart:

> "Considering the behavior and moral (?) actions of some prominent politicians I suspect they really don't follow their own philosophy." — **+0.03, neutral**

> "A schoolchild could tell you this outcome… Waste of time and resources" — **−0.05, negative**

*Those cutoffs came from VADER's authors. Keeping them is still a choice — and it will be yours.*
-->

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — parchment, muted greens, clay accent; cousin to ml0's brass-valves image): a hand turning a single brass dial set into a gate; the people just above the dial's mark pass through into warm light, the people just below are turned back into shadow — one arbitrary line. -->
![A hand turning a brass dial on a gate; people just above the mark pass into light, those just below are turned away](materials/lectures/images/ml3_threshold.jpg)

Here is a simplified loan rule, written in the syntax you'll learn this week:

```
credit_score = 649
income = 72000
if credit_score > 650 and income > 50000:
    decision = "approve"
else:
    decision = "review"
print(decision)    # review
```

Read it line by line. `credit_score > 650` is a **comparison**: it asks a yes-or-no question, and the answer
comes back as a **Boolean**, `True` or `False`. `and` means both comparisons must be `True`. If they are,
`if` runs the line under it; if not, `else` catches everything else. Here the score is 649, one point short,
so the answer is "review." The 650 is a **threshold**: a cutoff that turns a continuous number into a
category.

![A number line from 646 to 654 with a dashed line between 650 and 651: 646 through 650 are marked "review," 651 through 654 "approve"; a note says 650 itself is turned away because the code uses > rather than >=](materials/lectures/images/ml3_threshold_line.png)

Now ask the humanist's questions. **Who chose 650?** Is the person at 649 truly different from the person at
651, or did a round number just decide their year? And what about the person at exactly 650? The code says
`>`, so they're sent to review; `>=` would have approved them. Someone chose that symbol, too. Why income
*and* credit, and not rent history, or the reason the score dipped in the first place?

![Two bars of the same 123 rows: with VADER's standard cutoffs of plus or minus 0.05, 34 negative, 38 neutral, 51 positive; with stricter cutoffs of plus or minus 0.5, 17 negative, 76 neutral, 30 positive](materials/lectures/images/ml3_cutoffs.png)

A threshold is the most ordinary line in programming and one of the most consequential: an act of judgment
that looks like arithmetic. You'll meet your own soon. On Day 13 you'll use VADER, a tool that gives each
comment an overall `compound` score from −1 (most negative) to +1 (most positive). In HW3, **two** cutoffs
sort every row: a score of at least 0.05 is positive, at most −0.05 is negative, and anything between is
neutral. On our 123 rows, those lines give 51 positive, 34 negative, and 38 neutral. Move them to ±0.5 and
neutral jumps to 76.

The rows nearest the line show what is at stake. *"Considering the behavior and moral (?) actions of some
prominent politicians I suspect they really don't follow their own philosophy"* scores +0.03 and counts as
neutral: *prominent* and *suspect* nearly cancel out. *"A schoolchild could tell you this outcome… Waste of
time and resources"* scores −0.05 and only just counts as negative. Two skeptical comments, a few
hundredths apart, land in different boxes. Those
cutoffs came from VADER's authors. Keeping them is still a choice, and it will be yours.

## The tyranny of the tidy box

<!-- slide:
![Varied human figures pressed into identical pigeonhole drawers, the parts that don't fit spilling over and fading](materials/lectures/images/ml3_schema_sq.jpg)

Code needs clean categories, and people don't come clean.
So the system forces the fit — and whatever won't fit the schema
simply **disappears.**
-->

<!-- slide:
![A schematic of two form fields: one with only Female and Male radio buttons, stored as 0 or 1; one with a free-text box reading "In your own words"](materials/lectures/images/ml3_field.png)

Until 2014, Facebook asked every new user to choose one of two genders.
That year it added dozens of custom options.

A two-option field is, in effect, **a single bit**: `0` or `1`.
Cheap to store, easy to sort — and silent about everyone it doesn't fit.

### The schema, not reality, decided who was legible.
-->

<!-- slide:
Remember the missing voices from the last lecture:
**absence from the data isn't absence from reality.**

Here is one of the mechanisms. People go missing not only because
they never posted —

*but because the categories had no drawer for them.*
-->

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — parchment, muted greens, clay accent; recompose F25's "people sorted into category-circles" idea in warm paint, not cyberpunk): a crowd of richly varied human figures being pressed into a wall of identical rigid pigeonhole drawers; the parts of each person that don't fit the drawer spill over the edges and fade to nothing. -->
![Varied human figures pressed into identical pigeonhole drawers, the parts that don't fit spilling over and fading](materials/lectures/images/ml3_schema.jpg)

Code needs clean categories, and people don't come clean. So the system forces the fit — and whatever
won't fit the schema simply disappears.

![A schematic of two form fields: one with only Female and Male radio buttons, stored as 0 or 1; one with a free-text box reading "In your own words"](materials/lectures/images/ml3_field.png)

Until 2014, Facebook asked every new user to choose one of two genders, male or female; that year it added
dozens of custom options. A two-option field is, in effect, **a single bit**: `0` or `1`. It is cheap to
store and easy to sort, and it says nothing about everyone it doesn't fit. The schema, not reality, decided
who was legible. *(That's a central point of Catherine D'Ignazio and Lauren Klein's* Data Feminism*: a
"default" binary, chosen for computational convenience, quietly encodes a whole worldview — and erases
everyone who doesn't fit it.)*

Remember the missing voices from the Connotations lecture: **absence from the data isn't absence from reality.** Here is one of the
mechanisms. People go missing not only because they never posted, but because the categories had no drawer
for them.

## Classified by, or reading the sort

<!-- slide:
Everyone is sorted by systems like these — coders included.
What coding literacy changes is whether you can **see** the sort.

- **Without it**, the categories and cutoffs stay invisible: the logic
  that decides your loan, your feed, your risk score is someone else's secret
- **With it**, you can read the sort — question a category, expose a buried
  threshold, propose a box that fits the people it forgot
-->

<!-- slide:
You don't have to become an engineer.

### You only have to become unwilling to be sorted silently.

Most code really is plumbing. But the **key choices about people** —
the variables, the categories, the cutoffs — encode values and land on real lives.
-->

Everyone is sorted by systems like these, coders included. What coding literacy changes is whether you
can see the sort.

- **Without it**, the categories and cutoffs stay invisible: the logic that decides your loan, your feed,
  your risk score is someone else's secret.
- **With it**, you can read the sort — question a category, expose a buried threshold, propose a box that
  fits the people it forgot. You don't have to become an engineer. You only have to become unwilling to be
  sorted silently.

Most code really is plumbing. But the **key choices about people** — the variables, the categories, the
cutoffs — encode values and land on real lives.

## Your turn at the line

<!-- slide:
In a few weeks *you* will be the one drawing lines: which words are
"stopwords" worth deleting, which comment is "positive," where one "topic"
ends and the next begins.

**Each is a classification, and each is a judgment**
you are making *for* someone else.
-->

<!-- slide:
### Make the cut visible.

Leave the `#comment` that says where you drew the line, and why.

The honest classifier isn't the one who found the neutral categories —
there are no neutral ones.

*It's the one who shows you where they stood when they drew the box.*
-->

In the weeks ahead *you* will be the one drawing lines: which words are "stopwords" worth deleting, which comment
is "positive," where one "topic" ends and the next begins. Each is a classification, and each is a judgment
you are making *for* someone else.

The course's one demand holds here exactly as in the opening lecture: **make the cut visible.** Leave the `#comment` that
says where you drew the line, and why. The honest classifier isn't the one who found the neutral categories —
there are no neutral ones. It's the one who shows you where they stood when they drew the box.

Going deeper (optional): Safiya Noble, *Algorithms of Oppression*; Ruha Benjamin, *Race After Technology*;
Cathy O'Neil, *Weapons of Math Destruction*; Catherine D'Ignazio and Lauren Klein, *Data Feminism*.
