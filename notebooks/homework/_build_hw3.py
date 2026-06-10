"""Builder for WRIT20833 HW3 (sentiment analysis) — student + answer key.

2026 house style, pandas-native, ports F25 HW4-1 logic (VADER + freq-in-pos/neg +
human-vs-automated check). BYO-primary: setup defaults to the course YouTube-comments
corpus as a runnable fallback (also the answer-key reference) but tells students to load
their Day-10 workshop CSV. Ungrading framing throughout.

Run from repo root:  python3 notebooks/homework/_build_hw3.py
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


BADGE_STU = '<a href="https://colab.research.google.com/github/TCU-DCDA/WRIT20833_2026/blob/main/notebooks/homework/WRIT20833_HW3_2026.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>'
BADGE_KEY = '<a href="https://colab.research.google.com/github/TCU-DCDA/WRIT20833_2026/blob/main/notebooks/homework/WRIT20833_HW3_2026_ANSWER_KEY.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>'

STOPWORDS_SRC = "stopwords = " + json.dumps(STOPWORDS)

SETUP = '''# SETUP — run this cell first. (You're not expected to read every line yet — that's fine.)
import re, os, urllib.request
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

# VADER is a ready-made sentiment tool. It is not built into Python, so we install it,
# then make one analyzer we reuse. (More on "borrowing" tools in the note after A5.)
!pip install -q vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Same word-splitter + stopwords you built in HW2 (we reuse our own tools).
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
# EXPECTED PATH -- bring your own: load the cleaned CSV you made in the Day 10 workshop.
#     df = pd.read_csv("YOUR_FILE.csv")
#     text_column = "the_text_column"      # e.g. "comment"
#
# FALLBACK (runs out of the box) -- the course corpus on the TX Ten Commandments law:
df = load_course_comments()
text_column = "comment"
# ---------------------------------------------------------------------------------

print(f"{len(df)} rows loaded. Text column: '{text_column}'.")
df.head()'''


VADER_NOTE = '''### A note: you didn't build VADER — and that's normal
VADER is a **sentiment lexicon**: thousands of words hand-scored for feeling, plus rules for
"!", ALL CAPS, and negation, compiled and tuned by researchers. Almost nobody writes one from
scratch — you `pip install` it. (Long before AI, you'd still have reached for a library like
this; today you might ask an AI to help use it.) **Borrowing it is expected, not cheating.**

But A4 showed the catch: a borrowed tool carries someone else's assumptions and can be
**confidently wrong** (it missed the sarcasm). So the real skill isn't *building* VADER — it's
**judging whether to trust it** on your text. That's exactly what the human-vs-VADER check in
**B3** is for. *(We pick this thread up on **Day 7**, reading and improving AI-written code.)*'''


# ===================== STUDENT NOTEBOOK =====================
stu = [
    md(BADGE_STU),
    md('''# Homework 3 — Sentiment Analysis: Support, Opposition, and What Counting Missed

**WRIT 20833 — Intro to Coding in the Humanities**

**Student Name:** _Replace with your name_

**Upload as:** `LASTNAME_HW3.ipynb`

---

## What you're doing
In **HW2** you found which *words* dominate a debate — but a raw count can't tell a **cheer**
from a **complaint**. The word *commandments* "won," yet some of those mentions were people
**for** the Texas law and some **against** it, and they looked identical.

This week you add **sentiment analysis**: a tool (VADER) that scores each comment from very
negative to very positive. You'll work in **pandas** now — a table where each row is one
comment — and use sentiment to hear the **stance** that counting alone missed.'''),
    md('''## Prepare
Review **our own** materials first:
- **HW2** — term frequency (`split_into_words`, `stopwords`, `Counter`); we reuse all of it.
- **Pandas 01 / Pandas 02** code-alongs — DataFrames, `df[...]`, `.apply()`, `df.plot()`.
- The **VADER Sentiment** code-along (this week) — `analyzer.polarity_scores()` and the chart.'''),
    md('''## Required: `#comments` in every code block
In each code cell, add `#comments` saying **what you tried** and **what you learned** (or what
surprised you). Under this course's **ungrading** approach, your thinking in these comments and
reflections matters more than getting a "right" number.'''),
    md('''## About the setup cell (read this, then just run it)
The next cell is **plumbing**: it imports pandas, installs the VADER sentiment tool, and loads
your data into a table. **Run it, but don't worry about reading every line** — installing a
library and downloading a file are things you'll meet later. You *use* a tool through its
**interface** long before you build its **insides**.

After it runs, you have: a DataFrame **`df`** (one comment per row), the name of its text column
**`text_column`**, the **`analyzer`** (VADER), and your HW2 **`split_into_words`** + **`stopwords`**.

**Bringing your own data?** The cell has a commented `pd.read_csv(...)` line — point it at the
cleaned CSV from the Day 10 workshop and set `text_column`. Otherwise it loads the course corpus
so everything runs out of the box.'''),
    code(SETUP),

    # ---- Part A ----
    md('## Part A — From text to a sentiment score (5 exercises)'),
    md('**A1 — Meet your data as a table.** *(HW2 was one big blob; now each row is one comment.)*'),
    code('''# A1
# TODO: print df.shape (rows, columns)
# TODO: print how many comments there are with len(df)
# TODO: show the first few rows with df.head()

# #comments:
# Each ROW is now one comment. How is a DataFrame different from HW2's flat word list?'''),
    md('**A2 — Clean text, but keep the feeling.** HW2 *dropped* punctuation and capitals — sentiment tools need them.'),
    code('''# A2
sample = df[text_column].iloc[0]      # the first comment
print("Original:   ", sample)
# TODO: print sample.lower() and notice what intensity would be LOST (CAPS, "!") if we
#       cleaned it the HW2 way.

# #comments:
# Why does lowercasing + stripping "!" HELP a word count (HW2) but HURT a sentiment score?'''),
    md('**A3 — Score a single comment with VADER.**'),
    code('''# A3
text = "This is a great day for religious freedom!"
scores = analyzer.polarity_scores(text)
print(scores)

# TODO: print just the 'compound' score (one number, -1 = most negative ... +1 = most positive)
# TODO: change `text` to something you might write, and re-run

# #comments:
# What do 'pos', 'neu', 'neg', and 'compound' each seem to measure?'''),
    md('**A4 — An edge case: predict, then run.**'),
    code('''# A4 — predict, then run
# FIRST predict, in a comment: will VADER score this sarcastic line positive or negative?
# THEN run the cell.
sarcasm = "Oh great, another set of commandments to follow."
print(analyzer.polarity_scores(sarcasm)["compound"])

# #comments:
# My prediction was:
# VADER sees "great" and scores this POSITIVE -- but a human hears sarcasm.
# What does that warn you about trusting an automated score on its own?'''),
    md('**A5 — Score every comment at once.** *(This is what pandas is for.)*'),
    code('''# A5
def get_sentiment(text):
    return analyzer.polarity_scores(text)["compound"]

# TODO: make a new column df["sentiment"] by applying get_sentiment to df[text_column]
#       (hint: df[text_column].apply(get_sentiment))
# TODO: print df["sentiment"].mean(), .min(), .max()
# TODO: df.head() to see the new column

# #comments:
# In HW2 you looped by hand; here .apply() runs your function on every row.
# What just happened to all the comments in one line?'''),
    md(VADER_NOTE),

    # ---- Part B ----
    md('## Part B — Support, opposition, and what counting missed (4 exercises)'),
    md('**B1 — Turn scores into labels.** A number becomes a category. *(Recall Classification Logic.)*'),
    code('''# B1
def label_sentiment(score):
    # Standard VADER cutoffs: >= 0.05 is positive, <= -0.05 is negative, otherwise neutral.
    # TODO: return "positive", "negative", or "neutral" based on score
    pass

# TODO: make df["label"] by applying label_sentiment to df["sentiment"]
# TODO: print df["label"].value_counts()

# #comments:
# WHO chose the 0.05 cutoff? How would moving it change how many comments count as "positive"?'''),
    md('**B2 — Picture the split.** One line of pandas makes a chart. *(You saw `df.plot()` in the code-alongs.)*'),
    code('''# B2
# TODO: make a bar chart of the label counts:
#       df["label"].value_counts().plot(kind="bar", title="Sentiment of the comments")

# #comments:
# Does the chart show a clear majority, or a divided crowd?'''),
    md('**B3 — Read the extremes. Do you agree with VADER?** *(The human-vs-machine check.)*'),
    code('''# B3
most_positive = df.loc[df["sentiment"].idxmax()]
most_negative = df.loc[df["sentiment"].idxmin()]
print("MOST POSITIVE (", round(most_positive["sentiment"], 3), "):")
print(most_positive[text_column])
print("\\nMOST NEGATIVE (", round(most_negative["sentiment"], 3), "):")
print(most_negative[text_column])

# TODO: read BOTH comments yourself. Do YOU agree with VADER's call on each?

# #comments:
# Where do you AGREE with VADER, and where does it miss something a human catches?
# (Recall A4: sarcasm, irony, context.)'''),
    md('''**B4 — Interpretation (write 4–6 sentences below).**

Using B1–B3: does this crowd mostly **support or oppose** the law — or is it split? Then the key
question: **what did sentiment let you see that HW2's word-counting could not?** In HW2 the word
*commandments* "won" by raw frequency. Cite at least two numbers from this notebook (a label
count, a sentiment score). Then name **one thing VADER still gets wrong** — a place the number and
your human reading disagree. *(Recall HW2 B4: a tally can't tell a cheer from a complaint.)*'''),
    md('_Replace this cell with your interpretation._'),

    # ---- Part C ----
    md('## Part C — Going deeper (2 exercises)'),
    md('**C1 — Whose words are whose? Frequency *inside* each camp.** *(HW2\'s tool, now split by stance.)*'),
    code('''# C1
def top_words(text_series, n=8):
    words = []
    for t in text_series:
        words.extend(w for w in split_into_words(t) if w and w not in stopwords)
    return Counter(words).most_common(n)

positive_comments = df[df["label"] == "positive"][text_column]
negative_comments = df[df["label"] == "negative"][text_column]

# TODO: print top_words(positive_comments) and top_words(negative_comments)

# #comments:
# Which words appear in BOTH lists? In HW2 those words "won" overall -- but frequency alone
# couldn't tell you they were used by BOTH sides. What does that mean for "what the data says"?'''),
    md('''**C2 — On your own data, or push this one further.**

- **If you loaded your own dataset in setup:** this whole notebook already ran on it. Write 3–4
  sentences on what the sentiment split showed about *your* corpus, and one place you doubt VADER.
- **If you used the course corpus:** try ONE of — change the `0.05` cutoff in B1 and see what
  moves; or compare the sentiment of comments that mention `"constitution"` vs. those that don't.'''),
    code('''# C2
# TODO: do ONE of the options above. Show your code and the result.

# #comments:
# What did you expect, and did the data agree?'''),

    # ---- Experiments ----
    md('''## Weekly Experiments (your own work!)
After the required exercises, create **2–3 small experiments** of your own with this week's
skills. Make them original.

Ideas:
- Write five comments yourself and see if VADER scores them the way you meant.
- Find a comment where VADER is **most wrong** and explain why.
- Filter `df` to a subset (e.g. comments mentioning "school") and compare its average sentiment.

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
- [ ] I loaded a dataset (my own from the workshop, or the course corpus) and the notebook runs top to bottom.
- [ ] I completed **Part A (5)**, **Part B (4, incl. the B4 write-up)**, **Part C (2)**, and **2–3 experiments**.
- [ ] Every code cell has `#comments`.
- [ ] I wrote honestly about where I **agree and disagree** with VADER (engagement matters more than "right" labels).
- [ ] Saved as `LASTNAME_HW3.ipynb` and uploaded to the D2L Dropbox.

**Time estimate:** ~2 hrs for the exercises, ~1 hr for your experiments.'''),
]


# ===================== ANSWER KEY =====================
key = [
    md(BADGE_KEY),
    md('''# Homework 3 — Sentiment Analysis — INSTRUCTOR ANSWER KEY

**WRIT 20833 — Intro to Coding in the Humanities**

> Solutions are one valid approach; students may reach the same result differently. Teaching
> notes appear under each solution. **Ungrading:** this key is a **worked example + discussion
> fodder, not a rubric** — reward engagement and honest human-vs-VADER judgment over "correct"
> labels. It **runs top-to-bottom on the course corpus** (the BYO fallback, since student data
> can't be keyed). Counts reflect that corpus: **123 rows, 2026-06**. *(Note: the corpus is 123
> one-per-row lines — a few are short CSV→txt wrap-fragments; the `data/README.md` count has been
> corrected from an earlier "93".)*

---'''),
    code(SETUP),

    md('## Part A — From text to a sentiment score (5 exercises)'),
    md('**A1 — Meet your data as a table.**'),
    code('''# A1 — solution
print(df.shape)          # (123, 1)
print(len(df), "comments")
df.head()'''),
    md('''> **Teaching note:** Goal: read a DataFrame's shape; each row = one comment (bridge from HW2's
> single blob). The corpus is **123 rows**; a handful are short wrap-fragments ("Of Texas", "The")
> left by the CSV→txt cleaning — a realistic data-quality wart worth naming, and a preview of why
> the Day-10 cleaning workshop matters.'''),
    md('**A2 — Clean text, but keep the feeling.**'),
    code('''# A2 — solution
sample = df[text_column].iloc[0]
print("Original:   ", sample)
print("Lowercased: ", sample.lower())
# Lowercasing + stripping "!" is RIGHT for term frequency (HW2) but WRONG for sentiment:
# "GREAT!!!" and "great" carry different intensity. VADER wants the raw text.'''),
    md('''> **Teaching note:** Goal: preprocessing is an interpretive choice — the "right" cleaning depends
> on the question. HW2 wanted word identity (drop case/punctuation); VADER wants intensity (keep them).'''),
    md('**A3 — Score a single comment with VADER.**'),
    code('''# A3 — solution
text = "This is a great day for religious freedom!"
scores = analyzer.polarity_scores(text)
print(scores)               # {'neg':0.0, 'neu':0.411, 'pos':0.589, 'compound':0.8622}
print(scores["compound"])   # 0.8622 -- the single summary score, -1..+1'''),
    md('''> **Teaching note:** Goal: read VADER's dict. `compound` is the one-number summary; `pos/neu/neg`
> are proportions that sum to ~1. Students only need `compound` going forward.'''),
    md('**A4 — An edge case: predict, then run.**'),
    code('''# A4 — solution
sarcasm = "Oh great, another set of commandments to follow."
print(analyzer.polarity_scores(sarcasm)["compound"])
# +0.625 -- VADER reads "great" as positive and MISSES the sarcasm; a human reads it as negative.'''),
    md('''> **Teaching note:** Goal: predict-then-run (like HW1/HW2 A4), here exposing VADER's blind spot —
> sarcasm, irony, context. This is the critical heart of the assignment and the bridge to the
> human-vs-VADER check (B3) and Day 7 (AI Agency). Tools are useful AND fallible.'''),
    md('**A5 — Score every comment at once.**'),
    code('''# A5 — solution
def get_sentiment(text):
    return analyzer.polarity_scores(text)["compound"]

df["sentiment"] = df[text_column].apply(get_sentiment)
print("mean:", round(df["sentiment"].mean(), 3))   # 0.082
print("min: ", round(df["sentiment"].min(), 3))    # -0.968
print("max: ", round(df["sentiment"].max(), 3))    # 0.92
df.head()'''),
    md('''> **Teaching note:** Goal: `.apply()` = HW2's hand-loop, vectorized over the column. The near-zero
> **mean (0.082)** is itself a finding — the crowd is split, not uniformly for or against. Preview of B.'''),
    md(VADER_NOTE),

    md('## Part B — Support, opposition, and what counting missed (4 exercises)'),
    md('**B1 — Turn scores into labels.**'),
    code('''# B1 — solution
def label_sentiment(score):
    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    return "neutral"

df["label"] = df["sentiment"].apply(label_sentiment)
print(df["label"].value_counts())
# positive    51
# neutral     38
# negative    34'''),
    md('''> **Teaching note:** Goal: thresholds turn a continuum into bins — an authored choice (callback to
> HW1 A3 age bins / Classification Logic). 0.05 is a convention, not a fact; moving it reshapes the
> story. Note positives lead but neutral+negative (72) outweigh them — a divided crowd, not a mandate.'''),
    md('**B2 — Picture the split.**'),
    code('''# B2 — solution
df["label"].value_counts().plot(kind="bar", title="Sentiment of the comments")
plt.ylabel("number of comments")
plt.show()
# Positive bar slightly tallest, but neutral + negative together are the larger story: a split crowd.'''),
    md('''> **Teaching note:** Goal: one-line pandas viz (`df.plot`) reinforcing the code-alongs — not new
> material. Under ungrading, "make a chart and say what it shows" is the whole bar; reward the reading,
> not chart polish.'''),
    md('**B3 — Read the extremes. Do you agree with VADER?**'),
    code('''# B3 — solution
most_positive = df.loc[df["sentiment"].idxmax()]
most_negative = df.loc[df["sentiment"].idxmin()]
print("MOST POSITIVE (", round(most_positive["sentiment"], 3), "):", most_positive[text_column])
print("MOST NEGATIVE (", round(most_negative["sentiment"], 3), "):", most_negative[text_column])
# Most positive ~0.920; most negative ~-0.968. Students read both and note where VADER's number
# matches their gut and where tone/context complicate it.'''),
    md('''> **Teaching note:** Goal: deterministic close-reading of the extremes (`idxmax`/`idxmin` — no random
> `sample()`, so the key is reproducible) plus the human-vs-automated judgment F25 ran on a 5-row
> sample. The assignment's critical core: **reward thoughtful disagreement with VADER, not "right"
> labels.** Great place to surface that the most-negative comment may be messy/ambiguous text.'''),
    md('**B4 — Interpretation (model answer).**'),
    md('''> **Model answer (accept variants; look for ≥2 numbers + a named VADER failure):** The crowd is
> **split, not a mandate** — 51 positive vs. 38 neutral and 34 negative, with a near-zero mean
> (0.082). Sentiment adds what HW2 couldn't: in HW2 *commandments* "won" on raw frequency, but here
> it tops **both** the positive and negative word lists (C1) — the same word was a cheer for some and
> a complaint for others, which a count alone flattened into one "winner." **What VADER still gets
> wrong:** sarcasm and scripture-quoting (A4's "Oh great…" scores +0.625; a "John 3:16" comment may
> score neutral despite a strong stance), so the labels need a human read.

> **Teaching note:** Reward any answer that (a) cites ≥2 concrete numbers and (b) names a real VADER
> limitation. This is the HW2→HW3→HW4 spine: count → stance → integration.'''),

    md('## Part C — Going deeper (2 exercises)'),
    md('**C1 — Whose words are whose? Frequency *inside* each camp.**'),
    code('''# C1 — solution
def top_words(text_series, n=8):
    words = []
    for t in text_series:
        words.extend(w for w in split_into_words(t) if w and w not in stopwords)
    return Counter(words).most_common(n)

print("POSITIVE:", top_words(df[df["label"] == "positive"][text_column]))
print("NEGATIVE:", top_words(df[df["label"] == "negative"][text_column]))
# POSITIVE: religion 11, commandments 8, god 7, freedom 6, children 6, want 6, religious 5, good 5
# NEGATIVE: commandments 11, ten 10, law 7, bible 6, god 6, schools 5, court 5, broken 4
# 'commandments' and 'god' top BOTH camps -- HW2's frequency "winners" are shared vocabulary used
# to argue opposite sides. Sentiment is what separates them.'''),
    md('''> **Teaching note:** Goal: the synthesis — reuse HW2's term-frequency idea on sentiment-split
> subsets. Payoff: HW2's winning words (*commandments*, *god*) appear on **both** sides, so frequency
> alone conflated support and opposition; sentiment disentangles them. The whole HW2→HW3 arc in one
> cell, and the setup for HW4's integration.'''),
    md('**C2 — On your own data, or push further (model).**'),
    code('''# C2 — solution (one valid version of the "constitution" comparison)
mentions = df[df[text_column].str.contains("constitution", case=False)]
others = df[~df[text_column].str.contains("constitution", case=False)]
print("mentions 'constitution':", len(mentions), "| mean sentiment:", round(mentions["sentiment"].mean(), 3))
print("does not:               ", len(others), "| mean sentiment:", round(others["sentiment"].mean(), 3))'''),
    md('''> **Teaching note:** Goal: open exploration; any defensible version earns full credit under
> ungrading. For BYO submissions, evaluate the reflection on *their* corpus + a named VADER doubt,
> not a fixed number. The "constitution" cut is a nice callback to HW2's pairing.'''),
]


def write(path, cells):
    full = os.path.join(HERE, path)
    with open(full, "w", encoding="utf-8") as f:
        json.dump(notebook(cells), f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("wrote", full, "(%d cells)" % len(cells))


write("WRIT20833_HW3_2026.ipynb", stu)
write("WRIT20833_HW3_2026_ANSWER_KEY.ipynb", key)
