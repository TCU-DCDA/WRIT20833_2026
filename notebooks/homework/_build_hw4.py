"""Builder for WRIT20833 HW4 (topic modeling + integration) — student + answer key.

2026 house style, pandas-native, ports F25 HW4-2 logic (Gensim LDA + dominant-topic +
sentiment-by-topic integration). Simplifies F25: drops nltk/WordNet lemmatization and
pyLDAvis; reuses our split_into_words + stopwords; only new dependency is gensim.

LDA is STOCHASTIC + version-sensitive, so the answer key states exact values only for the
deterministic steps and describes LDA output QUALITATIVELY (interpretation in teaching notes).
random_state is fixed for within-environment reproducibility.

Run from repo root:  python3 notebooks/homework/_build_hw4.py
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

STOPWORDS = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "ve", "ll", "amp"]


def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": _lines(text)}


def code(text):
    return {"cell_type": "code", "metadata": {}, "execution_count": None,
            "outputs": [], "source": _lines(text)}


def _lines(text):
    text = text.strip("\n")
    lines = text.split("\n")
    return [l + "\n" for l in lines[:-1]] + [lines[-1]]


def notebook(cells):
    return {"cells": cells, "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python"}}, "nbformat": 4, "nbformat_minor": 4}


BADGE_STU = '<a href="https://colab.research.google.com/github/TCU-DCDA/WRIT20833_2026/blob/main/notebooks/homework/WRIT20833_HW4_2026.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>'
BADGE_KEY = '<a href="https://colab.research.google.com/github/TCU-DCDA/WRIT20833_2026/blob/main/notebooks/homework/WRIT20833_HW4_2026_ANSWER_KEY.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>'

STOPWORDS_SRC = "stopwords = " + json.dumps(STOPWORDS)

SETUP = '''# SETUP — run this cell first. (You're not expected to read every line yet — that's fine.)
import re, os, urllib.request
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

# Two borrowed tools: VADER (sentiment, from HW3) and Gensim (topic modeling, new this week).
!pip install -q gensim vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from gensim import corpora
from gensim.models import LdaModel
analyzer = SentimentIntensityAnalyzer()

# Same word-splitter + stopwords from HW2/HW3 (we reuse our own tools).
def split_into_words(any_chunk_of_text):
    return re.split(r"\\W+", str(any_chunk_of_text).lower())
''' + STOPWORDS_SRC + '''

def load_course_comments():
    """Load the course YouTube-comments corpus into a DataFrame, one comment per row."""
    filename = "tc_youtube_comments.txt"
    text = None
    for path in (filename, os.path.join("notebooks", "data", filename),
                 os.path.join("data", filename), os.path.join("..", "data", filename)):
        if os.path.exists(path):
            text = open(path, encoding="utf-8").read(); break
    if text is None:
        url = "https://raw.githubusercontent.com/TCU-DCDA/WRIT20833_2026/main/notebooks/data/" + filename
        text = urllib.request.urlopen(url).read().decode("utf-8")
    rows = [line.strip() for line in text.split("\\n") if line.strip()]
    return pd.DataFrame({"comment": rows})

# ----- Choose your data -----------------------------------------------------------
# EXPECTED PATH -- bring your own: the cleaned CSV from the Day 10 workshop (ideally the
# SAME dataset you used in HW3, so frequency + sentiment + topics all describe one corpus).
#     df = pd.read_csv("YOUR_FILE.csv")
#     text_column = "the_text_column"
#
# FALLBACK (runs out of the box) -- the course corpus on the TX Ten Commandments law:
df = load_course_comments()
text_column = "comment"
# ---------------------------------------------------------------------------------

# Sentiment carried over from HW3 (you already know this step):
df["sentiment"] = df[text_column].apply(lambda t: analyzer.polarity_scores(t)["compound"])

print(f"{len(df)} rows loaded and sentiment-scored. Text column: '{text_column}'.")
df.head()'''


LDA_NOTE = '''### A note: a topic is a *pattern*, not a fact — and you didn't build the math
Like VADER in HW3, **LDA is a borrowed tool** — you `pip install` gensim; nobody in this course
writes the statistics from scratch. But LDA differs from almost everything else you've run: it is
**stochastic**. Run it twice and the topics can come out in a different order, or shift, because it
starts from randomness (we set `random_state` to pin it down, but a different computer or gensim
version can still differ).

So a "topic" is **not a fact the data contains** — it's a *pattern the model proposes*, and a
**human decides** whether it means anything and what to call it (that's A5). Two analysts can label
the same topics differently. Hold your topics loosely. *(Day 7 again: judging a tool's output, not
just running it.)*'''


# ===================== STUDENT NOTEBOOK =====================
stu = [
    md(BADGE_STU),
    md('''# Homework 4 — Topic Modeling & Integration: What Is the Conversation Actually About?

**WRIT 20833 — Intro to Coding in the Humanities**

**Student Name:** _Replace with your name_

**Upload as:** `LASTNAME_HW4.ipynb`

---

## What you're doing
You now have three lenses on a text:
- **HW2 — frequency:** *which words* dominate.
- **HW3 — sentiment:** *how people feel* (support vs. opposition).
- **HW4 — topic modeling (new):** *what sub-conversations* the comments cluster into.

This week you let a tool (**Gensim LDA**) group the comments into **topics**, then you **integrate**
all three: which topics are people talking about, and how do they feel about each one? This is the
move your **capstone** is built on.'''),
    md('''## Prepare
Review **our own** materials first:
- **HW2** (`split_into_words`, `stopwords`, `Counter`) and **HW3** (pandas, `df.apply`, sentiment).
- **Pandas 01 / 02** — DataFrames, `groupby`, `df.plot()`.
- The **Topic Modeling (Gensim)** code-along (this week) — dictionary, corpus, `LdaModel`.'''),
    md('''## Required: `#comments` in every code block
In each code cell, add `#comments` saying **what you tried** and **what you learned**. Under this
course's **ungrading** approach, your interpretation — especially *naming and doubting* the
topics — matters more than any single number.'''),
    md('''## About the setup cell (read this, then just run it)
The next cell is **plumbing**: it imports pandas, installs **two** tools (VADER for sentiment,
**Gensim** for topic modeling), loads your data, and re-scores sentiment from HW3. **Run it, but
don't read every line.** Installing gensim can take a minute and may print a lot — that's normal.

After it runs you have: **`df`** (one comment per row, with a `sentiment` column), **`text_column`**,
the **`analyzer`**, `corpora`/`LdaModel` from gensim, and your **`split_into_words`** + **`stopwords`**.

**Bringing your own data?** Use the commented `pd.read_csv(...)` line — ideally the **same dataset
you used in HW3**, so all three lenses describe one corpus.'''),
    code(SETUP),

    # ---- Part A ----
    md('## Part A — From comments to topics (5 exercises)'),
    md('**A1 — Turn each comment into a list of meaningful words.** *(LDA reads a doc as a bag of words.)*'),
    code('''# A1
# TODO: make a column df["tokens"]: for each comment, the list of words from
#       split_into_words(...) that are non-empty AND not in stopwords.
#       (hint: df[text_column].apply(lambda t: [w for w in split_into_words(t) if w and w not in stopwords]))
# TODO: print df["tokens"].iloc[0]   (the first comment as a word list)

# #comments:
# This is HW2's "meaningful words" step, now kept PER COMMENT instead of one big pile. Why
# does topic modeling need each document kept separate?'''),
    md('**A2 — Build the dictionary and corpus.** *(Gensim\'s "bag of words" format.)*'),
    code('''# A2
dictionary = corpora.Dictionary(df["tokens"])   # every unique word gets an id number
corpus = [dictionary.doc2bow(toks) for toks in df["tokens"]]  # each doc -> [(word_id, count), ...]

print("vocabulary size:", len(dictionary))
# TODO: print corpus[0]  -- the first comment as (word_id, count) pairs
# TODO: to read it, print [(dictionary[i], c) for i, c in corpus[0]]

# #comments:
# A "bag of words" throws away word ORDER. What meaning is lost when "dog bites man" and
# "man bites dog" become the same bag?'''),
    md('**A3 — An edge case: predict, then run.**'),
    code('''# A3 — predict, then run
# Some lines in real data are fragments (e.g. "The"). FIRST predict: after we drop stopwords,
# what bag of words does a fragment produce? THEN run.
fragment_tokens = [w for w in split_into_words("The") if w and w not in stopwords]
print("tokens:", fragment_tokens)
print("bag of words:", dictionary.doc2bow(fragment_tokens))

# #comments:
# My prediction was:
# An EMPTY bag means the model has nothing to go on for that comment. What should happen to
# empty/fragment documents -- and how does messy data (recall HW3's 123 lines) cause this?'''),
    md('**A4 — Train the topic model.** *(Gensim does the math; you choose the settings.)*'),
    code('''# A4
NUM_TOPICS = 4   # a number YOU choose -- we revisit this in C1
lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=NUM_TOPICS,
               random_state=42, passes=10)

# TODO: print each topic with lda.print_topics(num_words=6)
#       (each topic = a weighted list of words the model grouped together)

# #comments:
# Run this cell again -- do the topics look exactly the same? Why might a model's output shift?'''),
    md('**A5 — Read and *name* the topics.** *(The model gives numbers; a human gives meaning.)*'),
    md('''Look at your A4 output. In the markdown cell below, **give each topic a short human label**
(e.g. "Topic 0 = church-and-state argument") and note any topic that seems vague or mixed. There is
no single right answer — that's the point.'''),
    md('_Replace this cell: list Topic 0…N and your label + one sentence of reasoning for each._'),
    md(LDA_NOTE),

    # ---- Part B ----
    md('## Part B — Integration: topics meet sentiment (4 exercises)'),
    md('**B1 — Assign each comment its dominant topic.**'),
    code('''# B1
def dominant_topic(bow):
    topic_probs = lda.get_document_topics(bow)
    if not topic_probs:                     # empty/fragment doc -> no real topic
        return -1
    return max(topic_probs, key=lambda pair: pair[1])[0]

# TODO: make df["topic"] by applying dominant_topic to each bag of words in `corpus`
#       (hint: df["topic"] = [dominant_topic(b) for b in corpus])
# TODO: print df[[text_column, "topic"]].head()

# #comments:
# Each comment is now filed under ONE topic. What is lost by forcing a comment that touches
# two themes into a single bin?'''),
    md('**B2 — How many comments per topic?** *(Plus a quick chart.)*'),
    code('''# B2
# TODO: print df["topic"].value_counts().sort_index()
# TODO: make a bar chart:
#       df["topic"].value_counts().sort_index().plot(kind="bar", title="Comments per topic")

# #comments:
# Are the topics evenly sized, or does one dominate? (A "-1" bar = empty/fragment comments.)'''),
    md('**B3 — The integration: how does each topic *feel*?** *(HW3 sentiment, grouped by HW4 topic.)*'),
    code('''# B3
# TODO: print the AVERAGE sentiment for each topic:
#       df.groupby("topic")["sentiment"].mean().round(3)

# #comments:
# This is the whole course in one line: frequency found the words, sentiment found the feeling,
# topics found the sub-conversations -- and now you can say WHICH sub-conversation is angriest or
# warmest. Which topic is most negative? Does that match the words in it (A4)?'''),
    md('''**B4 — Interpretation (write 5–7 sentences below).**

Bring all three lenses together for **one claim about this conversation.** Use specifics: name a
topic and its label (A5), its average sentiment (B3), and a word that "won" by frequency (HW2/recall
C1 of HW3). What is this conversation *actually about*, and how do the camps feel? Then the honest
part: name **one place the tools mislead** — a vague topic, a sentiment score you distrust, or an
empty/fragment document — and say how you'd check it by hand. *(This is exactly your capstone in
miniature.)*'''),
    md('_Replace this cell with your integrated interpretation._'),

    # ---- Part C ----
    md('## Part C — Going deeper / capstone bridge (2 exercises)'),
    md('**C1 — Change the number of topics.** *(The output depends on a number you picked.)*'),
    code('''# C1
# TODO: train a model with NUM_TOPICS = 2, print its topics.
# TODO: train another with NUM_TOPICS = 6, print its topics.
# (Copy the A4 pattern; just change num_topics. Keep random_state=42.)

# #comments:
# With 2 topics the story is coarse; with 6 it fragments. There is no "true" number --
# YOU author it. How would you defend the number you'd choose for your capstone?'''),
    md('''**C2 — Capstone bridge.**

In the markdown cell below, write 4–5 sentences planning your **capstone** using what you just did:
which dataset (your own, ideally), which of the three lenses (frequency / sentiment / topics) best
fits the question you care about, and one limitation you'll be honest about. If you used your own
data this week, say what surprised you.'''),
    md('_Replace this cell with your capstone plan._'),

    # ---- Experiments ----
    md('''## Weekly Experiments (your own work!)
After the required exercises, create **2–3 small experiments** of your own. Make them original.

Ideas:
- Re-run A4 a few times with `random_state` removed — watch the topics move.
- Print the 3 most *positive* and 3 most *negative* comments **within one topic**.
- Add a few custom stopwords and see whether the topics get cleaner.

It's fine if an experiment doesn't work at first — **documenting what went wrong and what you
learned is worth just as much as working code.**'''),
    code('''# Experiment 1


# #comments:
# What were you trying? What happened? What did you learn?'''),
    code('''# Experiment 2


# #comments:
# What were you trying? What happened? What did you learn?'''),
    code('''# Experiment 3


# #comments:
# What were you trying? What happened? What did you learn?'''),

    # ---- Submit ----
    md('''## Submit
- [ ] My name is at the top.
- [ ] I loaded a dataset (my own, or the course corpus) and the notebook runs top to bottom.
- [ ] I completed **Part A (5, incl. naming the topics)**, **Part B (4, incl. the B4 write-up)**, **Part C (2)**, and **2–3 experiments**.
- [ ] Every code cell has `#comments`.
- [ ] I **named and doubted** my topics honestly (engagement matters more than "right" topics).
- [ ] Saved as `LASTNAME_HW4.ipynb` and uploaded to the D2L Dropbox.

**Time estimate:** ~2 hrs for the exercises, ~1 hr for your experiments.'''),
]


# ===================== ANSWER KEY =====================
key = [
    md(BADGE_KEY),
    md('''# Homework 4 — Topic Modeling & Integration — INSTRUCTOR ANSWER KEY

**WRIT 20833 — Intro to Coding in the Humanities**

> Solutions are one valid approach. **Ungrading:** this key is a **worked example + discussion
> fodder, not a rubric** — reward how students *name and doubt* topics, not "correct" ones.
>
> ⚠️ **LDA is stochastic + version-sensitive.** Unlike HW2/HW3 (exact, reproducible numbers), the
> topic words, per-topic counts, and per-topic sentiment **will differ** by machine, gensim version,
> and run — even with `random_state=42`. So this key states exact values only for the **deterministic**
> steps (vocabulary size, the `[]` edge case) and describes LDA output **qualitatively**; the value is
> in the *method and interpretation*. The full pipeline was validated to run top-to-bottom on the
> course corpus (gensim 4.4.0; **123 rows**).

---'''),
    code(SETUP),

    md('## Part A — From comments to topics (5 exercises)'),
    md('**A1 — Turn each comment into a list of meaningful words.**'),
    code('''# A1 — solution
df["tokens"] = df[text_column].apply(
    lambda t: [w for w in split_into_words(t) if w and w not in stopwords])
print(df["tokens"].iloc[0])
# e.g. ['putting', 'constitution', 'classrooms']  -- HW2's "meaningful words", kept PER comment.'''),
    md('''> **Teaching note:** Goal: HW2's filter, but the list is kept per-document (LDA needs documents,
> not one pile). Good moment to connect back: same `split_into_words` + `stopwords`, new shape.'''),
    md('**A2 — Build the dictionary and corpus.**'),
    code('''# A2 — solution
dictionary = corpora.Dictionary(df["tokens"])
corpus = [dictionary.doc2bow(toks) for toks in df["tokens"]]
print("vocabulary size:", len(dictionary))   # ~650 unique words on the course corpus
print(corpus[0])                               # [(id, count), ...]
print([(dictionary[i], c) for i, c in corpus[0]])   # human-readable

# (Sidebar) the most negative comment from HW3 is long -> its bag has many words; a short
# comment's bag is tiny. Document length varies a lot in this corpus.'''),
    md('''> **Teaching note:** Goal: the bag-of-words representation; word ORDER is discarded. The
> "dog bites man" example lands the loss of syntax/context. Vocabulary size depends on the corpus
> (~650 here) — not a fixed number to evaluate against.'''),
    md('**A3 — An edge case: predict, then run.**'),
    code('''# A3 — solution
fragment_tokens = [w for w in split_into_words("The") if w and w not in stopwords]
print("tokens:", fragment_tokens)              # []  -- "the" is a stopword, so nothing remains
print("bag of words:", dictionary.doc2bow(fragment_tokens))   # []  -- an EMPTY document'''),
    md('''> **Teaching note:** Goal: predict-then-run (the house motif), here showing an **empty bag of
> words**. Ties directly to HW3's data-quality finding: the corpus has wrap-fragments ("Of Texas",
> "The") that reduce to nothing. Empty docs get a meaningless/near-uniform topic — students handle
> them with the `-1` guard in B1. Real data is messy; the pipeline must not crash on it.'''),
    md('**A4 — Train the topic model.**'),
    code('''# A4 — solution
NUM_TOPICS = 4
lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=NUM_TOPICS,
               random_state=42, passes=10)
for topic_id, words in lda.print_topics(num_words=6):
    print(f"topic {topic_id}: {words}")
# REPRESENTATIVE ONLY (yours will differ): on this single-issue corpus every topic is dominated
# by commandments / religion / god / ten / school -- the topics OVERLAP because the whole corpus
# is about one law. That overlap is itself the finding (see note).'''),
    md('''> **Teaching note:** Goal: train + read LDA topics. Expect heavy overlap here — a narrow,
> single-issue corpus doesn't separate into crisp topics, which is an honest lesson about LDA's
> limits on small/homogeneous data (and an argument for students bringing a richer dataset). Don't
> evaluate by specific words; evaluate the student's *reading* of whatever they get.'''),
    md('**A5 — Read and *name* the topics (model answer).**'),
    md('''> **Model answer:** Any defensible labels with reasoning, e.g. "Topic A = church/state
> separation argument (church, state, religion); Topic B = think-of-the-children framing (children,
> schools, want); Topic C = scripture/law literalism (ten, commandments, law, bible)." Full credit
> for naming + flagging at least one **vague or mixed** topic. The point is that humans author the
> meaning; two students may label the same topics differently and both be right.'''),
    md(LDA_NOTE),

    md('## Part B — Integration: topics meet sentiment (4 exercises)'),
    md('**B1 — Assign each comment its dominant topic.**'),
    code('''# B1 — solution
def dominant_topic(bow):
    topic_probs = lda.get_document_topics(bow)
    if not topic_probs:
        return -1
    return max(topic_probs, key=lambda pair: pair[1])[0]

df["topic"] = [dominant_topic(b) for b in corpus]
print(df[[text_column, "topic"]].head())'''),
    md('''> **Teaching note:** Goal: dominant-topic assignment + the `-1` guard for empty docs (the A3
> case). Critical hook: forcing a multi-theme comment into ONE bin loses nuance — the same flattening
> theme as HW2/HW3, now at the topic level.'''),
    md('**B2 — How many comments per topic?**'),
    code('''# B2 — solution
print(df["topic"].value_counts().sort_index())
df["topic"].value_counts().sort_index().plot(kind="bar", title="Comments per topic")
plt.xlabel("topic"); plt.ylabel("comments"); plt.show()
# Roughly 25-35 comments per topic on the course corpus (varies by run/version); a small "-1"
# group may appear for empty/fragment docs.'''),
    md('''> **Teaching note:** Goal: one-line pandas viz again (reinforcement). Read distribution as
> evidence; flag the `-1` bar as the data-quality residue, not a real theme.'''),
    md('**B3 — The integration: how does each topic feel?**'),
    code('''# B3 — solution
print(df.groupby("topic")["sentiment"].mean().round(3))
# REPRESENTATIVE ONLY (yours will differ): the per-topic means SPREAD OUT -- some topics run
# WARMER and some run COOLER (e.g. roughly 0.01 to 0.14 on one run; sign and order are not
# reproducible). The POINT is that different sub-conversations carry different average feeling.'''),
    md('''> **Teaching note:** Goal: **the synthesis** — `groupby(topic)["sentiment"].mean()` joins HW4
> topics to HW3 sentiment. This is the capstone move in one line. The robust lesson (independent of
> the stochastic numbers): sentiment is *not uniform across topics* — some sub-conversations are
> angrier than others. Push students to check a topic's mean against its A4 words for coherence.'''),
    md('**B4 — Interpretation (model answer).**'),
    md('''> **Model answer (accept variants; require all three lenses + one named failure):** e.g. "The
> conversation is really several arguments under one law. The church/state topic (label, A5) runs
> cooler (lower B3 mean) than the 'teach values' topic — so *commandments*, the word that 'won'
> HW2's frequency count, is actually shared across a warmer camp and a cooler one.
> **Where the tools mislead:** Topic C looked vague (overlapping words), one long sarcastic comment
> is mis-scored by VADER, and the `-1` fragments are noise — I'd re-read those by hand before
> trusting the averages."

> **Teaching note:** This is the assignment's capstone-in-miniature. Reward integration of all three
> methods + an honest limitation, not a "correct" reading. Bridges straight into the capstone.'''),

    md('## Part C — Going deeper / capstone bridge (2 exercises)'),
    md('**C1 — Change the number of topics (model).**'),
    code('''# C1 — solution
for k in (2, 6):
    m = LdaModel(corpus=corpus, id2word=dictionary, num_topics=k, random_state=42, passes=10)
    print(f"\\n=== {k} topics ===")
    for tid, words in m.print_topics(num_words=5):
        print(f"topic {tid}: {words}")
# With 2 topics the split is coarse (roughly pro/skeptical framings blur together); with 6 it
# fragments into near-duplicates. No "true" number -- the analyst authors the choice.'''),
    md('''> **Teaching note:** Goal: show that `num_topics` is an authored knob, not a discovered truth
> (callback to HW1/HW3 threshold choices). Reward a student who can *defend* a chosen number for
> their own data over one who finds the "right" one.'''),
    md('**C2 — Capstone bridge (model).**'),
    md('''> **Model answer:** Any concrete plan that names (a) a dataset — ideally the student's own,
> richer than 123 short comments — (b) which lens fits their question (frequency for "what words
> dominate," sentiment for "how do they feel," topics for "what sub-conversations exist"), and (c) one
> honest limitation. No code required.

> **Teaching note:** This *is* the capstone proposal in embryo. For BYO submissions, evaluate the fit
> between question and method, and the candor about limits — not the dataset's size or "results."'''),
]


def write(path, cells):
    full = os.path.join(HERE, path)
    with open(full, "w", encoding="utf-8") as f:
        json.dump(notebook(cells), f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("wrote", full, "(%d cells)" % len(cells))


write("WRIT20833_HW4_2026.ipynb", stu)
write("WRIT20833_HW4_2026_ANSWER_KEY.ipynb", key)
