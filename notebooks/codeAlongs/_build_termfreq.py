"""Builder for the 2026 'Term Frequency' code-along (Day 6).

No F25 standalone source existed for term frequency (it was taught inside HW1/HW2), so this is
authored fresh in the 2026 code-along house style (warm cultural examples; concept -> code -> 'your
turn'; Putting It All Together -> Sneak Preview -> Playground; colab badge + metadata; no HW-style
#comments). Walsh-independent.

Design:
- PLAIN PYTHON, pre-pandas — matches HW2's deliberate pre-pandas approach (Day 6 introduces term
  frequency; HW2 "Whose Words Win?" then applies it). Reuses the EXACT split_into_words + stopwords +
  Counter + top_meaningful_words idiom from _build_hw2.py (copied verbatim) so the code-along teaches
  precisely what HW2 expects.
- Picks up the Day-5 Dictionaries/Functions thread (its count_words dict -> Counter sneak preview) and
  turns it into real term-frequency analysis: raw counts -> stopword filter -> reusable function ->
  two-corpus contrast (a mini preview of HW2's comments-vs-Constitution "Whose Words Win?").
- Keeps the course's critical frame: counting is already interpretation; and the "honest about
  borrowed code" note (Counter does what we hand-built).
- All outputs computed, not asserted in prose; qualitative claims (which words surface) verified.

Run from repo root:  python3 notebooks/codeAlongs/_build_termfreq.py
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))

# verbatim from _build_hw2.py / _build_hw4.py so the code-along uses the SAME stopwords as the homework
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
        "colab": {"provenance": []},
        "kernelspec": {"name": "python3", "display_name": "Python 3"},
        "language_info": {"name": "python"}}, "nbformat": 4, "nbformat_minor": 0}


STOPWORDS_SRC = "stopwords = " + json.dumps(STOPWORDS)

cells = [
    md('<a href="https://colab.research.google.com/github/TCU-DCDA/WRIT20833_2026/blob/main/notebooks/codeAlongs/WRIT20833_Term_Frequency_2026.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>'),

    md('''# WRIT 20833 — Term Frequency

**When Coding Meets Culture: Developing Data-Driven Opinions**

Make an editable copy of this worksheet by going to **File > Save a copy in Drive**'''),

    md('''Last week you learned to *handle* text. This week we start to *analyze* it — and the very first
move in cultural analytics is the simplest one imaginable: **count the words**. The idea is that if a
word shows up a lot, the text is probably *about* that word. We call this **term frequency**, and on
Day 5 you already built its engine — a `count_words` dictionary that tallied a word list. Today we turn
that into a real tool for asking *what is this text actually about?*'''),

    # ---- setup ----
    md('''# Setup

Run this cell. These are the same tools from Day 5 and HW1: a `split_into_words` helper, the long
`stopwords` skip-list, and Python's built-in `Counter`. You'll *use* them today; you don't need to read
every line yet.'''),
    code('''import re
from collections import Counter

def split_into_words(any_chunk_of_text):
    lowercase_text = any_chunk_of_text.lower()
    # split on any run of non-letter/number characters (spaces, punctuation, newlines)
    return re.split(r"\\W+", lowercase_text)

''' + STOPWORDS_SRC + '''

print("Ready. The stopwords skip-list has", len(stopwords), "words in it.")'''),

    # ---- Part 1: raw counts ----
    md('''# Part 1 — Count Every Word

Here's a small pile of real-sounding comments about the Texas law that puts the Ten Commandments in
classrooms. Let's count what's in it. First, split it into words, then let `Counter` tally them and
hand back the **10 most common**.'''),
    code('''comments_text = """
The Ten Commandments belong in every classroom in this country, and our kids need them.
Morals matter, and our schools are where our kids learn about right and wrong.
God and country are what built this nation, and the schools should teach that.
It is common sense to put these values back in the schools.
Religion has no place in a public school that is paid for by all of us.
And whose religion are we talking about? Religion is for the home, not the schools.
Freedom of religion has to mean freedom from religion in our public schools too.
The government should not be putting religion or god into the schools of this country.
"""

words = [w for w in split_into_words(comments_text) if w]   # `if w` drops empty strings
print("Total words:", len(words))
print(Counter(words).most_common(10))'''),
    md('''Look at the very top of that list: **the** and **and** — the little connective words that hold
*any* English sentence together, carrying nothing about the topic. (A couple of content words like
*schools* and *religion* are climbing up too, because they repeat a lot — but they're elbow to elbow with
noise.) The single most frequent words are meaningless, which makes the whole ranking untrustworthy.
Let's clear the noise out so the count actually means something.'''),

    # ---- Part 2: meaningful words ----
    md('''# Part 2 — Keep Only the Meaningful Words

Those tiny words have a name — **stopwords** — and we already have a list of them. If we keep only the
words that are **not** stopwords (and not empty), the noise drops away and the *content* words rise to
the top.'''),
    code('''meaningful = [w for w in split_into_words(comments_text) if w and w not in stopwords]

print("Meaningful words kept:", len(meaningful))
print(Counter(meaningful).most_common(10))'''),
    md('''*That's* term frequency. Now the top words — **schools, religion, country, god, kids** —
actually tell you what this pile of comments is about. Same text, same counting; we just stopped
counting the noise.'''),
    md('''> **About borrowed code.** `Counter` is a tool you `import` — it does in one line what your
> Day-5 `count_words` function did by hand. Hand-building it once is *why* you can trust it now: you
> know exactly what "count the words" means, so when you borrow `Counter` (or get word-count code from
> an AI), you can read it and judge whether it's doing the right thing.'''),
    md('### Your turn'),
    code('''# your turn — show the top 15 meaningful words instead of 10
# print(Counter(meaningful).most_common( ... ))
'''),

    # ---- Part 3: reusable function ----
    md('''# Part 3 — Make It Reusable

You'll want to run this on text after text, so wrap it in a **function** (recall Day 5). Give it a text
and a number `n`; get back the top `n` meaningful words. Write the recipe once, reuse it forever.'''),
    code('''def top_meaningful_words(text, n):
    meaningful = [w for w in split_into_words(text) if w and w not in stopwords]
    return Counter(meaningful).most_common(n)

print(top_meaningful_words(comments_text, 5))'''),
    md('### Your turn'),
    code('''# your turn — paste a few sentences of your own (a review, some lyrics, a comment thread)
my_text = "Type or paste some text here, the longer the better"

print(top_meaningful_words(my_text, 5))
'''),

    # ---- Part 4: the contrast ----
    md('''# Part 4 — Whose Words Win?

Term frequency gets *interesting* when you **compare two texts**. Here's a second one: a passage in the
flat, official voice of a founding legal document — the kind of thing those commenters keep invoking.
Run the same function on both and watch two completely different vocabularies appear.'''),
    code('''official_text = """
Congress shall pass no law respecting an establishment of religion.
The powers not delegated to the United States by the Constitution are reserved to the States.
All legislative powers shall be vested in a Congress of the United States.
No State shall make any law which shall abridge the privileges of citizens.
The Congress shall have power to make all laws necessary and proper.
"""

print("Comments:", top_meaningful_words(comments_text, 5))
print("Official: ", top_meaningful_words(official_text, 5))'''),
    md('''Same method, two different *aboutnesses*. The official text runs on **shall, congress, states,
law**; the comments on **schools, religion, country, god**. Neither list is the "right" one —
together they show two voices talking about the same issue in completely different words. That gap *is*
the analysis.'''),
    md('''We can even name the words that are distinctive to one side — the meaningful words in the
comments that the official text never reaches for:'''),
    code('''comment_top = {word for word, count in top_meaningful_words(comments_text, 8)}
official_top = {word for word, count in top_meaningful_words(official_text, 8)}

print("Distinctive to the comments:", comment_top - official_top)'''),

    # ---- Putting it together ----
    md('''# Putting It All Together

The whole term-frequency move, start to finish — split, drop the stopwords, count, take the top. This is
the engine you'll run on real data in HW2.'''),
    code('''def top_meaningful_words(text, n):
    meaningful = [w for w in split_into_words(text) if w and w not in stopwords]
    return Counter(meaningful).most_common(n)

for label, text in [("Comments", comments_text), ("Official", official_text)]:
    print(label, "->", top_meaningful_words(text, 5))'''),
    code('''# your turn — compare TWO of your own texts (two artists, two subreddits, two news sources...)
text_a = "first text here"
text_b = "second text here"

print("A ->", top_meaningful_words(text_a, 5))
print("B ->", top_meaningful_words(text_b, 5))
'''),

    # ---- Sneak preview ----
    md('''# Sneak Preview: Where This Is Going

**HW2 ("Whose Words Win?")** is this exact move at full scale: you'll run term frequency on **123 real
YouTube comments** about the Texas law and on the **entire U.S. Constitution**, and read what the
contrast reveals about a public's voice versus the document it keeps invoking.

And keep one thing in mind as you go — *counting is already interpreting.* **We** decided to split on
spaces, to treat every word as equal, to throw out exactly the words on that stopword list. Change those
choices and the "most meaningful words" change too. Term frequency isn't the neutral truth of a text;
it's a lens, and part of your job is knowing what it reveals and what it flattens.

Next week, **pandas** lets us run this same lens over thousands of rows at once.'''),

    md('# Playground'),
    code('# use this space to experiment!\n'),
]


out = os.path.join(HERE, "WRIT20833_Term_Frequency_2026.ipynb")
with open(out, "w", encoding="utf-8") as f:
    json.dump(notebook(cells), f, indent=1, ensure_ascii=False)
    f.write("\n")
print("wrote", out, "(%d cells)" % len(cells))
