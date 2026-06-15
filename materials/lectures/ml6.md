# Data Archaeology
## Where found data comes from

<!-- meta: ML6 · Day 8 · the through-line -->

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — aged parchment, muted greens, one clay accent; match the ml0 images): an archaeologist's hand with a soft brush sweeping dust off a half-buried clay tablet whose surface is inscribed not with cuneiform but with faint rows of a spreadsheet — excavating data like an artifact. -->
<!-- ![A hand brushing dust from a half-buried clay tablet inscribed with faint spreadsheet rows](materials/lectures/images/ml6_title.jpg) -->

Today you start working with **found data** — a table you didn't make, full of words real people wrote for
their own reasons. Before you load a single row in pandas, one idea has to land: **that data is not raw.**
It's an artifact. Someone produced it, by making choices, and reading it well is closer to archaeology than
to chemistry.

## Reading traces of a life

An archaeologist never has the thing itself — the meal, the ritual, the household. They have what survived:
a pottery shard, a posthole, a midden of bones. From those *traces* they reconstruct how people lived.

> Pottery shards → ancient dining habits.   Dataset rows → cultural patterns.

You're making the same move. Our 123 comments are a dig site — traces a community left while arguing about
a law one summer. You'll excavate patterns from them, but like any archaeologist you have to remember
you're holding **shards, not the meal**: a partial record of something larger you'll never fully recover.
(That's ML0's pipeline again — what reaches you is already several steps downstream of the lived thing.)

## You found it; you didn't make it

There are two kinds of data, and this course runs almost entirely on the second.

- **Created data** — surveys you design, experiments you run. *You* control the questions.
- **Found data** — traces that already exist because culture left them: comments, reviews, lyrics, posts.
  *Culture* chose the questions, not you.

Found data is thrilling because it's **real** — nobody was performing for a researcher. It's treacherous
for the same reason: it wasn't built for your question, its gaps aren't random, and *you weren't there when
it was made.* "Found" never means "neutral."

## "Raw data" is an oxymoron

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — parchment, muted greens, clay accent): a flowing river of human faces and voices narrowing as it pours through a wooden sieve; what drops out the bottom is a neat stack of identical paper cards, while most of the river spills off the sides, uncaptured. -->
<!-- ![A river of faces pouring through a sieve that emits neat identical cards while most spills off uncaptured](materials/lectures/images/ml6_raw.jpg) -->

We say "raw data" as if it arrived straight from nature, untouched. It never did. By the time a comment
reaches your notebook, someone chose **which** platform to pull from, **when**, **which** field counted,
and **what** got dropped — remember the wrap-fragments in our own corpus, sentences chopped in half by the
export. Every dataset is the *survivors* of a collection process, and the ones who didn't survive — the
people who never posted, the comment that was deleted, the language the scraper couldn't parse — leave no
row at all. **The empty seats aren't in the file.** Treat "raw" as a warning label, not a fact.

## Hear, don't extract

<!-- layout: split -->
<!-- IMG PROMPT (warm "Reading Room" oil painting — parchment, muted greens, clay accent): two hands cupped to an ear, leaning toward a small crowd of warmly glowing figures who are speaking, set against a faint, cold background of industrial mining and harvesting machinery — listening, not mining. -->
<!-- ![Hands cupped to listen toward a crowd of speaking figures, against faint mining machinery](materials/lectures/images/ml6_hear.jpg) -->

Listen to the verbs data culture uses: *mine, scrape, harvest, crawl, extract.* Every one treats people
like ore — raw material to be stripped out and processed. This course asks you to change the verb to
**hear.** "Hearing" assumes the other end is a *someone*, with something to say and a claim on being
received with care.

That one swap reframes the ethics of collection — which you'll practice in code today (robots.txt, fair
use, attribution). The legal question is *"am I allowed to take this?"* The humanist question underneath is
**"am I listening, or am I extracting?"** Both matter; only the second is about the people in the data.

## Keep a data biography

So before the analysis, become the artifact's biographer. An archaeologist logs an object's
**provenance**; you log your data's. Four things, written plainly in your notebook:

- **Origin** — who made this, when, and why?
- **Journey** — how was it collected, processed, shared?
- **Transformations** — what did *you* clean, filter, or drop?
- **Limitations** — what's missing, and *who's* missing?

This isn't busywork; it's **credibility.** A reader can only trust your reading if they can see where the
data came from and what you did to it — and remember that a single row is layered (surface: who/what/when;
cultural: the trend it hints at; societal: the values underneath). It's the habit the whole course keeps
asking for: **make your choices visible.** You're interpreting human cultural behavior — handle it with
care.

Going deeper (optional): Lisa Gitelman, ed., *"Raw Data" Is an Oxymoron*; Catherine D'Ignazio & Lauren
Klein, *Data Feminism*; Johanna Drucker, "Humanities Approaches to Graphical Display" (data as *capta*, not
"given").
