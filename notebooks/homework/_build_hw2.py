"""Builder for WRIT20833 HW2 (term frequency) — student + answer key.

Generates two .ipynb files matching the HW1 2026 house style exactly:
  WRIT20833_HW2_2026.ipynb
  WRIT20833_HW2_2026_ANSWER_KEY.ipynb

Run from the repo root:  python3 notebooks/homework/_build_hw2.py
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- exact F25 stopwords list (lifted from WRIT20833_2025 HW1), used in HW1 A6 ----
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


BADGE_STU = '<a href="https://colab.research.google.com/github/TCU-DCDA/WRIT20833_2026/blob/main/notebooks/homework/WRIT20833_HW2_2026.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>'
BADGE_KEY = '<a href="https://colab.research.google.com/github/TCU-DCDA/WRIT20833_2026/blob/main/notebooks/homework/WRIT20833_HW2_2026_ANSWER_KEY.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>'

STOPWORDS_SRC = "stopwords = " + json.dumps(STOPWORDS)

SETUP = '''# SETUP — run this cell first. (You're not expected to read every line yet — that's fine.)
import re
from collections import Counter
import os, urllib.request

def split_into_words(any_chunk_of_text):
    lowercase_text = any_chunk_of_text.lower()
    # Split on any run of non-letter/number characters (spaces, punctuation, newlines).
    return re.split(r"\\W+", lowercase_text)

# The same long stopwords list you met in HW1 (A6): tiny function words that carry
# little meaning on their own. We filter these out to find the "meaningful" words.
''' + STOPWORDS_SRC + '''

def load_text(filename):
    """Load a corpus. Checks this folder and notebooks/data/, then falls back to
    downloading from the course repo (works in Colab, and locally after merge)."""
    for path in (filename, os.path.join("notebooks", "data", filename),
                 os.path.join("data", filename), os.path.join("..", "data", filename)):
        if os.path.exists(path):
            return open(path, encoding="utf-8").read()
    url = "https://raw.githubusercontent.com/TCU-DCDA/WRIT20833_2026/main/notebooks/data/" + filename
    return urllib.request.urlopen(url).read().decode("utf-8")

# Two real corpora about the 2025 Texas Ten Commandments-in-schools law:
comments_text = load_text("tc_youtube_comments.txt")    # the public's voice (93 YouTube comments)
constitution_text = load_text("us_constitution.txt")    # the document the public keeps invoking
print("Setup complete. Both corpora loaded.")'''


# ===================== STUDENT NOTEBOOK =====================
stu = [
    md(BADGE_STU),
    md('''# Homework 2 — Term Frequency: Whose Words Win?

**WRIT 20833 — Intro to Coding in the Humanities**

**Student Name:** _Replace with your name_

**Upload as:** `LASTNAME_HW2.ipynb`

---

## What you're doing
Last week (HW1 **C2**) you turned many comments into one big word list. This week you'll
**count** those words to find what a text is *really* about — its **term frequency** — and
use it to stage a debate between **two real texts**:

- **`comments_text`** — 93 real YouTube comments on the 2025 Texas law putting the **Ten
  Commandments** in classrooms (the public's voice).
- **`constitution_text`** — the full **U.S. Constitution**, the document those commenters
  keep invoking.

Everything you need is loaded by the setup cell — **no pandas, no outside textbook.**'''),
    md('''## Prepare
Review **our own** materials before you start:
- HW1 **B3/C2** — building one word list from many texts (this is where we left off).
- The **String Methods / Conditionals / Loops** code-along (`.lower()`, `.split()`).
- HW1 **A6** — membership testing with a `stopwords` list.'''),
    md('''## Required: `#comments` in every code block
In each code cell, add `#comments` saying **what you are trying to do** and **what you
learned** (or what surprised you). For example:

```python
# I wanted to see the most common word before filtering.
# I learned that "the" wins every time -- raw counts are dominated by function words.
Counter(split_into_words(constitution_text)).most_common(1)
```'''),
    md('''## About the setup cell (read this, then just run it)
The next cell is **plumbing**: it loads the two texts and defines two helper tools. **Run it, but
don't worry about reading every line** — it uses a couple of things we haven't covered yet (a
pattern-matcher for splitting on punctuation, and code that downloads a file if it's missing).
You'll meet those later. This is a normal part of coding: you *use* a tool through its **interface**
long before you could *build* its **insides** — just like you drive a car without knowing the engine.

For this whole homework, you only need these things the setup cell hands you:
- `comments_text` and `constitution_text` — the two texts, as one big string each
- `split_into_words(text)` — turns a text into a list of lowercase words *(like `.split()` from HW1, but it also drops punctuation)*
- `stopwords` — the same skip-list of tiny words from HW1 **A6**
- `Counter(list)` and `.most_common(n)` — count how often each item appears, then take the top `n`

If you can use those, you can do every exercise below — no pattern-matching or downloading required.'''),
    code(SETUP),

    # ---- Part A ----
    md('## Part A — From words to counts (5 exercises)'),
    md('**A1 — How big is each corpus?** *(Recall HW1 C2: total vs. distinct words.)*'),
    code('''# A1
# TODO: split BOTH texts into word lists with split_into_words(...)
# TODO: for EACH corpus, print the TOTAL number of words and the number of DISTINCT words
#       (hint: len(...) for total; len(set(...)) for distinct)

# #comments:
# Which text has more words? Which has more DISTINCT words?
# What might a bigger vocabulary tell you about a text?'''),
    md('**A2 — The raw count problem.** Count words *without* filtering first.'),
    code('''# A2
# TODO: build a Counter of ALL the words in constitution_text (no filtering yet)
# TODO: print the 10 most common with .most_common(10)

# #comments:
# What kinds of words win? Are they meaningful?
# Why do almost ALL texts share the same top words?'''),
    md('**A3 — Keeping only the meaningful words.** *(Recall HW1 A6: skip stopwords.)*'),
    code('''# A3
# TODO: split constitution_text into words
# TODO: build `meaningful` = every word that is NOT empty AND NOT in stopwords
#       (hint: a list comprehension, or a for-loop with an if)
# TODO: print the 10 most common meaningful words

# #comments:
# Now what rises to the top? Does it match what the Constitution is "about"?
# A stopword list is an editorial choice -- who decides which words don't count?'''),
    md('''**A4 — An edge case: predict, then run.**'''),
    code('''# A4 — predict, then run
# We have a Counter of the comments' meaningful words below.
# FIRST predict, in a comment, what `.most_common(0)` returns. THEN run the cell.
comment_words = [w for w in split_into_words(comments_text) if w and w not in stopwords]
comment_counts = Counter(comment_words)
print(comment_counts.most_common(0))

# #comments:
# My prediction was:
# An empty result is not an error -- when might "zero results" still be a real answer?'''),
    md('**A5 — Wrap it in a reusable function.** *(Recall HW1 B/C: build the tool once, reuse it.)*'),
    code('''# A5
# TODO: finish this function so it returns the n most common meaningful words of ANY text.
def top_meaningful_words(text, n):
    # TODO: split `text` into words
    # TODO: keep only non-empty words that are NOT in stopwords
    # TODO: return Counter(...).most_common(n)
    pass

# TODO: test it -- print top_meaningful_words(constitution_text, 5)

# #comments:
# Why is a function better than copy-pasting the same 3 lines for each text?'''),
    md('''### A note: you just rebuilt something coders almost never write from scratch
Counting word frequency is one of the most common things people do with text — so common that
almost no working coder writes it from zero. **Long before AI**, they'd copy a tested version from
a resource like **Stack Overflow**, a blog, or a library; today they might ask an AI to write it.
Borrowing code is normal and expected — not cheating.

So why build it by hand here? Because borrowed code only helps if you can **read it and judge
whether it does what you need**: which words `stopwords` throws away, how `split_into_words` decides
where one word ends, what actually gets counted. We build it once, slowly, so that when you reuse a
prefab version later — and you will — you know exactly what you're looking at and where it might be
wrong. *(We pick this thread up on **Day 7**, reading and improving AI-written code.)*'''),

    # ---- Part B ----
    md('## Part B — Whose words win? (4 exercises)'),
    md('**B1 — Top 20 of each corpus, side by side.**'),
    code('''# B1
# TODO: use your A5 function to print the top 20 meaningful words of EACH corpus
print("CONSTITUTION:")
# TODO ...
print("COMMENTS:")
# TODO ...

# #comments:
# In one sentence each: what is the Constitution about? What are the comments about?'''),
    md('**B2 — A direct lookup: does the public speak the Constitution\'s language?**'),
    code('''# B2
# `comment_counts` was built in A4. You can look up ONE word's count directly:
# TODO: print comment_counts["constitution"]   (how often the commenters say "constitution")
# TODO: print comment_counts["commandments"]   (compare it)

# #comments:
# The commenters invoke the Constitution -- but how often, vs. their own keyword?
# This is "close reading" (one exact word) meeting "distant reading" (the whole count).'''),
    md('**B3 — Distinctive words: what one text says that the other never does.**'),
    code('''# B3
# TODO: build a SET of the constitution's meaningful words
# TODO: build a SET of the comments' meaningful words
# TODO: print the comments' top-20 words that DO NOT appear in the Constitution at all
#       (hint: loop your comments top-20; keep each word that is `not in` the constitution set)

# #comments:
# What does the public argue about that the founding document is simply silent on?'''),
    md('''**B4 — Interpretation (write 4–6 sentences below).**

Using your numbers from B1–B3, answer: **whose words "win," and what does term frequency
let you say that reading every comment by hand would not?** Name at least two specific words
and their counts. Then name **one thing the counts get wrong or hide** — a place where
counting flattens what a person actually meant. *(Recall Collective Memory: scale vs. nuance.)*'''),
    md('_Replace this cell with your interpretation._'),

    # ---- Part C ----
    md('## Part C — Going further (2 exercises)'),
    md('**C1 — Tuning your stopwords.** Real corpora need custom filtering.'),
    code('''# C1
# Numbers and leftover tokens (like "10", "amp" from "&amp;") can clutter the comments.
# TODO: make custom_stopwords = stopwords + a few of your own (e.g. "10", "ten", "would")
# TODO: re-rank the comments' top 10 meaningful words using custom_stopwords
#       (tip: copy your A5 logic but swap in custom_stopwords)

# #comments:
# Each word you remove is a judgment call. Did filtering "10"/"ten" clarify the
# meaning -- or quietly erase that people kept naming "the TEN commandments"?'''),
    md('''**C2 — Bring your own text (optional, recommended).**

Paste your own short corpus between the triple quotes — a batch of social-media comments,
song lyrics, a speech — and run term frequency on it. *(We don't scrape automatically until
Day 8; for now, copy/paste by hand.)*'''),
    code('''# C2 (optional)
my_text = """
PASTE your own text here -- a dozen comments, some lyrics, a short speech.
One per line is fine.
"""
# TODO: print top_meaningful_words(my_text, 10)

# #comments:
# What did you expect the top words to be? Did the count agree with your gut?'''),

    # ---- Experiments ----
    md('''## Weekly Experiments (your own work!)
After the required exercises, create **2–3 small experiments** of your own with this week's
skills. Make them original.

Ideas:
- Change `n` and watch the "long tail" appear (`most_common(50)` — where does meaning fade?).
- Compare a word's rank in BOTH corpora.
- Test an **edge case**: an empty string `""`, a text of pure stopwords, ALL CAPS text.

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
- [ ] I completed **Part A (5)**, **Part B (4, including the B4 write-up)**, **Part C (2)**, and **2–3 experiments**.
- [ ] Every code cell has `#comments`.
- [ ] The notebook **runs top to bottom without errors**.
- [ ] Saved as `LASTNAME_HW2.ipynb` and uploaded to the D2L Dropbox.

**Time estimate:** ~1.5–2 hrs for the exercises, ~1 hr for your experiments.'''),
]


# ===================== ANSWER KEY =====================
key = [
    md(BADGE_KEY),
    md('''# Homework 2 — Term Frequency: Whose Words Win? — INSTRUCTOR ANSWER KEY

**WRIT 20833 — Intro to Coding in the Humanities**

> Solutions are one valid approach; students may reach the same result differently. Teaching
> notes appear under each solution. This key **runs top-to-bottom** against the two corpora in
> `notebooks/data/`. Counts below reflect those exact files (2026-06).

---'''),
    code(SETUP),

    md('## Part A — From words to counts (5 exercises)'),
    md('**A1 — How big is each corpus?**'),
    code('''# A1 — solution
for name, text in [("CONSTITUTION", constitution_text), ("COMMENTS", comments_text)]:
    words = split_into_words(text)
    print(name, "-> total:", len(words), " distinct:", len(set(words)))
# CONSTITUTION -> total: ~4556  distinct: ~937   (includes one empty "" token from the split)
# COMMENTS     -> total: ~2282  distinct: ~748'''),
    md('''> **Teaching note:** Goal: `len` (total) vs. `len(set(...))` (distinct), reused from HW1 C2.
> Note the split can yield a single empty string `""` (leading/trailing punctuation) — that's why
> A3 filters `if w` as well as stopwords. The Constitution is longer but the comments are
> lexically *denser* (more distinct words per total) — vernacular variety vs. legal repetition.'''),
    md('**A2 — The raw count problem.**'),
    code('''# A2 — solution
all_counts = Counter(split_into_words(constitution_text))
print(all_counts.most_common(10))
# [('the', 411), ('of', 287), ('shall', 191), ('and', 189), ('be', 125),
#  ('to', 114), ('in', 88), ('states', 82), ('or', 79), ('united', 55)]'''),
    md('''> **Teaching note:** Goal: show that *unfiltered* counts are dominated by function words
> ("the", "of", "and") — nearly identical across any English text, so they reveal almost nothing.
> Motivates the stopword filter. "shall" sneaking into the raw top 5 is a nice preview that some
> high-frequency words ARE meaningful (legal obligation).'''),
    md('**A3 — Keeping only the meaningful words.**'),
    code('''# A3 — solution
words = split_into_words(constitution_text)
meaningful = [w for w in words if w and w not in stopwords]
print(Counter(meaningful).most_common(10))
# [('shall', 191), ('states', 82), ('united', 55), ('state', 48), ('president', 34),
#  ('may', 33), ('congress', 29), ('house', 23), ('law', 23), ('section', 22)]'''),
    md('''> **Teaching note:** Goal: the `if w and w not in stopwords` filter — the heart of term
> frequency. Now the top words actually describe the document (a structure of states, president,
> congress, law). Critical hook (Classification Logic): the stopword list is an *authored* filter —
> deciding "shall" stays but "should" goes is an editorial judgment, not a neutral fact.'''),
    md('**A4 — An edge case: predict, then run.**'),
    code('''# A4 — solution
comment_words = [w for w in split_into_words(comments_text) if w and w not in stopwords]
comment_counts = Counter(comment_words)
print(comment_counts.most_common(0))
# []  -- most_common(0) asks for ZERO items, so you get an empty list (NOT an error, NOT "all").'''),
    md('''> **Teaching note:** Goal: predict-then-run, like HW1 A4 — but here the surprise is a valid
> *empty* result rather than an error. Common wrong predictions: "it returns everything" or "it
> crashes." Discussion: an empty result is still data; in research, "we found zero" is a finding,
> not a failure. (`comment_counts` is defined here and reused in B2.)'''),
    md('**A5 — Wrap it in a reusable function.**'),
    code('''# A5 — solution
def top_meaningful_words(text, n):
    words = split_into_words(text)
    meaningful = [w for w in words if w and w not in stopwords]
    return Counter(meaningful).most_common(n)

print(top_meaningful_words(constitution_text, 5))
# [('shall', 191), ('states', 82), ('united', 55), ('state', 48), ('president', 34)]'''),
    md('''> **Teaching note:** Goal: refactor A3's logic into one reusable tool — the backbone of the
> rest of the homework (and HW3). Reinforce that a function is "write the recipe once, run it on
> any text." Students who hard-coded `constitution_text` inside the function should generalize it
> to the `text` parameter. The student note that follows makes the broader point — term frequency
> is prefab code nobody writes from scratch (Stack Overflow long before AI); we build it by hand
> so they can *read and judge* a borrowed/AI version later. Good spot to preview the **Day 7**
> AI-Agency lesson and set the norm that borrowing code is expected, not cheating.'''),

    md('## Part B — Whose words win? (4 exercises)'),
    md('**B1 — Top 20 of each corpus, side by side.**'),
    code('''# B1 — solution
print("CONSTITUTION:", top_meaningful_words(constitution_text, 20))
print("COMMENTS:", top_meaningful_words(comments_text, 20))
# CONSTITUTION -> shall, states, united, state, president, may, congress, house, law, section, ...
# COMMENTS     -> commandments, religion, ten, god, 10, children, schools, state, people, want, ...'''),
    md('''> **Teaching note:** Goal: reuse the A5 function twice — the payoff of writing it. The contrast
> is the whole lesson: a vocabulary of governance (shall/states/president) vs. a vocabulary of
> religion-in-schools (commandments/god/children/schools). "state" appears in BOTH — a good bridge
> word to point out.'''),
    md('**B2 — A direct lookup: does the public speak the Constitution\'s language?**'),
    code('''# B2 — solution
print("constitution:", comment_counts["constitution"])   # 8
print("commandments:", comment_counts["commandments"])   # 25'''),
    md('''> **Teaching note:** Goal: indexing a Counter for ONE exact word (close reading) against the
> ranked totals (distant reading). The commenters DO invoke "constitution" (8×) — the top comment is
> literally "how about putting the constitution in classrooms?" — but their own keyword "commandments"
> (25×) wins 3-to-1. A missing key returns `0`, not an error — worth demonstrating live.'''),
    md('**B3 — Distinctive words: what one text says that the other never does.**'),
    code('''# B3 — solution
con_set = {w for w in split_into_words(constitution_text) if w and w not in stopwords}
distinctive = [w for w, _ in top_meaningful_words(comments_text, 20) if w not in con_set]
print(distinctive)
# ['commandments', 'religion', 'god', 'children', 'schools', 'want', 'school', 'bible', 'follow', 'church', 'would']
# ('state'/'law'/'people'/'ten'/'one' drop out of the top-20 — they DO appear in the Constitution)'''),
    md('''> **Teaching note:** Goal: set membership for "distinctive" vocabulary — the words the public
> argues about that the founding text is simply silent on (religion, god, children, schools). Critical
> hook: term frequency makes the *gap* visible — the debate is happening in a vocabulary the
> Constitution never uses, which is itself the commenters' point about church and state.'''),
    md('**B4 — Interpretation (model answer).**'),
    md('''> **Model answer (accept reasonable variants; look for specific counts + a named limitation):**
> Term frequency shows the comments are dominated by *commandments* (25) and *religion* (20), while the
> Constitution is dominated by *shall* (191) and *states* (82) — so the public is arguing about religion
> in a document that never uses the word. The commenters invoke *constitution* (8×) but their own
> keyword wins 3-to-1, so by the numbers the religious frame "wins" the comment thread. **What counting
> hides:** a raw tally can't tell *support* from *opposition* — many of those 25 "commandments" mentions
> are people arguing *against* the law, yet they look identical to endorsements in a frequency count.
> (That sentiment gap is exactly what HW3 takes up.)

> **Teaching note:** Reward any answer that (a) cites at least two specific word counts and (b) names a
> real limitation of frequency — most naturally that counts erase stance/sarcasm/context. This bridges
> directly to HW3 (VADER sentiment) and the close-vs-distant reading thread.'''),

    md('## Part C — Going further (2 exercises)'),
    md('**C1 — Tuning your stopwords.**'),
    code('''# C1 — solution
custom_stopwords = stopwords + ["10", "ten", "would", "people"]
words = [w for w in split_into_words(comments_text) if w and w not in custom_stopwords]
print(Counter(words).most_common(10))
# [('commandments', 25), ('religion', 20), ('god', 14), ('children', 11), ('schools', 10),
#  ('state', 10), ('want', 9), ('law', 9), ('constitution', 8), ('one', 8)]'''),
    md('''> **Teaching note:** Goal: custom stopwords as an explicit, *visible* editorial act. Removing
> "10"/"ten" cleans the ranking — but note the cost: people deliberately said "the TEN commandments,"
> so filtering it slightly erases their emphasis. Good place to insist that every stopword choice be
> documentable, because it changes the result.'''),
    md('**C2 — Bring your own text (model).**'),
    code('''# C2 — solution (any pasted corpus works; this stub just proves the call runs)
my_text = """
Keep church and state separate.
My kids should learn history not scripture.
Whose ten commandments though there are different versions.
"""
print(top_meaningful_words(my_text, 5))
# e.g. [('keep', 1), ('church', 1), ('state', 1), ('separate', 1), ('kids', 1)]'''),
    md('''> **Teaching note:** Goal: prove the A5 function generalizes to *any* text students supply —
> the bridge to "bring your own cultural dataset" in the Week-2 workshop and the capstone. Remind
> students that real collection (scraping) is taught Day 8; hand-paste is fine now. Grade on a working
> call + a reflection, not on the corpus chosen.'''),
]


def write(path, cells):
    full = os.path.join(HERE, path)
    with open(full, "w", encoding="utf-8") as f:
        json.dump(notebook(cells), f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("wrote", full, "(%d cells)" % len(cells))


write("WRIT20833_HW2_2026.ipynb", stu)
write("WRIT20833_HW2_2026_ANSWER_KEY.ipynb", key)
