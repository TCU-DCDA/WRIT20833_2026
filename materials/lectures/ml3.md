# Classification Logic
## Whose categories? Sorting as judgment

<!-- meta: ML3 · Day 3 · the through-line -->

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — aged parchment, muted greens, one clay accent; match the ml0 images): a road forking like an if/else branch, with a gate at the split; an unseen hand waves a line of varied human figures left or right — sorting people into two paths. -->
<!-- TODO: generate -> materials/lectures/images/ml3_title.jpg, then uncomment the next line (it turns on the 2-column layout): -->
<!-- ![A road forking like an if/else branch, a gate at the split sorting a line of people left or right](materials/lectures/images/ml3_title.jpg) -->

Today you learn `if`, `else`, and the booleans that drive them — `True` and `False`, greater-than and
equals. It is the most innocent-looking tool in all of programming. It is also the exact machinery by which
software decides who gets the loan, the match, the apartment, the interview, the flag.

This lecture is the humanities frame for the syntax you're about to practice. Because the moment your code
says `if ... :`, it has begun **sorting people** — and sorting is never neutral. Someone drew the line.

## To classify is to judge

A category is a decision: **this counts as the same; that counts as different.** Drawing the box is an act
of judgment before it is ever an act of code.

- Put "single mother," "widow," and "divorced dad" in one bin labeled *non-traditional household* and
  you've made an argument about what *traditional* is supposed to mean.
- Mark a comment "positive" or "negative" and you've flattened a person's mixed, sarcastic, grieving,
  joking sentence into one of two boxes.

There is no neutral box. Every classification system encodes **values** — about what matters, what counts,
and who belongs where. ML1 said code is not neutral; classification is the sharpest place you will feel it.

## Status has always gated access

Long before computers, a single status decided which doors opened: *noble* or *commoner*, *citizen* or
*foreigner*, *insider* or *outsider*. The variable was social, but it worked exactly like a boolean — one
bit, and the gate swung open or stayed shut.

The software era didn't invent the gate. It **automated** it, and renamed the variables:

> `credit_score` · `criminal_background` · `relationship_status` · `employment_status` · `immigration_status`

Same logic, new costume: a value about a person, checked at a threshold, deciding what they get to reach.
What changed is scale and speed — and that the judgment now hides inside a function that looks like math.

## The threshold problem

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — parchment, muted greens, clay accent; cousin to ml0's brass-valves image): a hand turning a single brass dial set into a gate; the people just above the dial's mark pass through into warm light, the people just below are turned back into shadow — one arbitrary line. -->
<!-- TODO: generate -> materials/lectures/images/ml3_threshold.jpg, then uncomment the next line: -->
<!-- ![A hand turning a brass dial on a gate; people just above the mark pass into light, those just below are turned away](materials/lectures/images/ml3_threshold.jpg) -->

Here is a real loan rule, in the syntax you'll write this week:

> `if credit_score > 650 and income > 50000: approve()`

Now ask the humanist's questions. **Who chose 650?** Is the person at 649 truly different from the person at
651, or did a round number just decide their year? Why income *and* credit, and not rent history, or the
reason the score dipped in the first place?

A threshold is the most ordinary line in programming and one of the most consequential. It is an act of
power wearing the costume of arithmetic. You'll meet your own threshold soon: in HW3, a single cutoff
(`compound > 0.05`) will sort every comment into positive, negative, or neutral. The number will feel
objective. It won't be. It will be yours.

## The tyranny of the tidy box

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — parchment, muted greens, clay accent; recompose F25's "people sorted into category-circles" idea in warm paint, not cyberpunk): a crowd of richly varied human figures being pressed into a wall of identical rigid pigeonhole drawers; the parts of each person that don't fit the drawer spill over the edges and fade to nothing. -->
<!-- TODO: generate -> materials/lectures/images/ml3_schema.jpg, then uncomment the next line: -->
<!-- ![Varied human figures pressed into identical pigeonhole drawers, the parts that don't fit spilling over and fading](materials/lectures/images/ml3_schema.jpg) -->

Code needs clean categories, and people don't come clean. So the system forces the fit — and whatever
won't fit the schema simply disappears.

For years a certain social platform stored **gender as a single bit**: male or female, `0` or `1`. Not
because its engineers believed that was the whole truth of human gender, but because one bit is cheap to
store, easy to sort, and convenient for advertisers. The schema, not reality, decided who was legible.
*(That's the Data Feminism point: a "default" binary, chosen for computational convenience, quietly encodes
a whole worldview — and erases everyone who doesn't fit it.)*

Remember ML1's missing voices: **absence from the data isn't absence from reality.** Here is one of the
mechanisms. People go missing not only because they never posted, but because the categories had no drawer
for them.

## Classified by, or building the sort

So there are two ways to stand in relation to all this machinery.

- **Without coding literacy, you are classified BY systems** you can't see: algorithms sort you, other
  people define the categories, and you never get a vote in the logic that decides your loan, your feed,
  your risk score.
- **With it, you can read the sort** — question a category, expose a buried threshold, redraw a box to fit
  the people it forgot. You don't have to become an engineer. You only have to become unwilling to be
  sorted silently.

That isn't every line of code — most of it really is plumbing. But the **key choices about people** — the
variables, the categories, the cutoffs — encode values and land on real lives.

## Your turn at the line

In four weeks *you* will be the one drawing lines: which words are "stopwords" worth deleting, which comment
is "positive," where one "topic" ends and the next begins. Each is a classification, and each is a judgment
you are making *for* someone else.

The course's one demand holds here exactly as in ML0: **make the cut visible.** Leave the `#comment` that
says where you drew the line, and why. The honest classifier isn't the one who found the true categories —
there are none. It's the one who shows you where they stood when they drew the box.

Going deeper (optional): Safiya Noble, *Algorithms of Oppression*; Ruha Benjamin, *Race After Technology*;
Cathy O'Neil, *Weapons of Math Destruction*.
