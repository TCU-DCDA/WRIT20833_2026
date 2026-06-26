# NLP & Topic Modeling
## The machine clusters the words — you name the meaning

<!-- meta: Day 16 · the through-line -->

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — aged parchment, muted greens, one clay accent; match the ml0 images): A scholar at a long wooden table sorting one large scattered heap of handwritten letters into several distinct stacks, each stack bound with a different muted-color ribbon (clay, sage, ochre) — many documents resolving into a few themes. Warm lamplight. -->
![A scholar sorting a scattered heap of letters into a few ribbon-bound stacks by theme](materials/lectures/images/ml7_title.jpg)

Your text-analysis journey has been a ladder of bigger questions. Counting words asked *what appears most?*
Sentiment asked *how does it feel?* Today you climb to the biggest one yet: *what is this whole pile of text
even **about**?* Topic modeling is the deepest "distant reading" move in the course — it surfaces themes
running through hundreds of documents that no one could find reading one comment at a time. But it works by a
move you should be suspicious of, and getting clear on that move is the whole lesson.

## You already do this — instantly

Drop into a conversation halfway through and you figure out what it's about in seconds. Somebody keeps saying
*budget* and *deadline* — it's a work project. *Election*, *campaign*, *vote* — politics. You read the
**repeated words**, the **keywords**, the **tone**, and you infer the subject without anyone announcing it.
And when you can't tell, you do the one thing that matters most: you **ask** — *"wait, the group project or
the internship?"*

That instant, unconscious sorting is exactly the skill we're about to hand to a machine. Watching it try is
the fastest way to see what's easy about reading and what's quietly hard.

## The computer gets only the words

Here's the gap. You bring tone of voice, facial expression, cultural memory, and the prior conversation to
every sentence — and you can always ask *"what do you mean?"* A computer gets **just the words on the
screen.** No tone, no context, no cultural knowledge unless someone programmed it in, and no way to ask a
clarifying question. Closing that gap is the whole field of **Natural Language Processing** — the autocorrect,
spam filters, and translation you already use daily.

Language fights back, because it was built for humans, not machines. *"I saw her duck"* — the pet or the
motion? *"That's sick"* — disgust or delight? *"Oh, great, another meeting"* — the words say positive, the
meaning is the opposite. Ambiguity, idiom, and sarcasm are easy for you and brutal for a machine, because they
live in the **context** the machine can't see. Keep that blind spot in mind; it comes back at the end.

## Organizing a library without reading the books

So how does a machine find themes in text it can't actually understand? Imagine sorting a library with no
time to read a single book. You'd look at which words appear together on each cover and back, and infer
shelves: *history, romance, science fiction.* You never read for meaning — you just notice **what co-occurs.**

That's topic modeling. We'll use **LDA** (Latent Dirichlet Allocation) from the **Gensim** library, and it
rests on two assumptions:

- Each **topic** is a *cluster of words that tend to show up together.*
- Each **document** is a *mixture* of those topics — not filed under one, but "70% this, 30% that."

LDA works *backward* from the finished text to guess what clusters must have produced it — like
reverse-engineering a recipe from the plated dish. *tomato + basil + mozzarella* → an "Italian" topic. It
finds the pattern by raw co-occurrence. That is **all it ever does.**

## The machine clusters; you name

Here is the move to be suspicious of — and the most important sentence in this lecture. LDA hands you back
**lists of words.** It never hands you a name.

> Topic 3: *money, dream, green, light, decay, gold.* The algorithm does not know this is "the American Dream."
> **You** know that. Naming it is your move, not the machine's.

The computer discovered that those words travel together; it has no idea what they *mean*, that they're about
ambition or disappointment or Gatsby. **Interpretation is the humanist's job** — and it's not neutral. What
you name a cluster depends on what you already know, what you're looking for, and where you stand. Two readers
can label the same word-list differently and both be defensible. The statistics are the machine's; the meaning
is yours. Own that, and don't dress your interpretation up as something the algorithm "found."

## There is no correct number of topics

Before LDA runs, you tell it how many topics to look for — `num_topics`. People assume the algorithm will
*reveal* the right number. It won't. Ask the same comments for two topics and unrelated themes get mashed
together; ask for ten and one real theme splinters into fragments.

Neither answer is "wrong." **Choosing the number of topics is a research decision you justify** — by how
interpretable and useful the result is, not by a truth the model uncovered. It's the course's recurring
lesson wearing new clothes: a knob you turned is doing work that's easy to mistake for a fact the data
handed you. Make the choice visible, and say why you made it.

## When real data fights back

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — aged parchment, muted greens, one clay accent; match the ml0 images): A person trying to sort one single tangled ball of yarn into three separate baskets, but every strand runs into all three baskets at once — the sorting refuses to come apart cleanly. Warm lamplight, scattered index cards. -->
<!-- ![Hands trying to sort one tangled ball of yarn into three baskets, every strand crossing all three](materials/lectures/images/ml7_tangle.jpg) -->

A toy corpus — fifteen comments pulled from sports, music, and food forums — topic-models beautifully: three
obvious subjects, three clean word-lists you can name in a second. That clarity is a setup. Now point the same
machine at our **123 Texas Ten Commandments comments**, where every voice is arguing about *one law*, in
overlapping vocabulary.

The topics come back **muddy.** LDA still hands you three tidy word-lists — it always will — but here each one
is just *more of the same argument*, not three distinct themes. There weren't separate subjects to find, so the
model imposed structure anyway. **That's the warning:** the algorithm produces clusters whether or not real
themes exist, so part of your job is judging whether the output means anything at all. (And because LDA is
**stochastic**, rerun it or run it on another machine and the groupings shift — which is why we pin
`random_state` just to talk about the *same* result twice.)

## What the model can't hear

The bird's-eye view is real power — you can see across hundreds of documents at once, a scale no close reading
reaches. But hold it to the same questions you've asked all term:

- **Whose text got counted?** Topic models only see what was digitized and collected. The empty seats aren't in
  the file — the same lesson the data-as-artifact work pressed on you.
- **Who decides what it means?** The algorithm produces word clusters; *humans* name them. Whose categories,
  whose authority? You've met this question before as the logic of classification.
- **What does it miss?** Irony, sarcasm, coded language, the context that flips a meaning — exactly the things
  that made language hard at the start of this lecture. Computational reading has blind spots, and they're not
  random.

LDA assumes topics are stable categories. Culture is fluid and contextual. So use the model for what it's
genuinely good at — a map of a pile too big to read — and never confuse the map for the territory. The
machine finds the pattern; **you** decide whether the pattern is a finding or just order imposed on noise.

Going deeper (optional): David M. Blei, "Topic Modeling and Digital Humanities" (*Journal of Digital
Humanities*); Ted Underwood, "Topic Modeling Made Just Simple Enough"; Benjamin Schmidt, "Words Alone: 
Dismantling Topic Models in the Humanities" (the skeptic's case); Catherine D'Ignazio & Lauren Klein,
*Data Feminism* (whose data, whose categories).
