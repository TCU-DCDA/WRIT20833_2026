"""Builder for the 2026 'Dictionaries & Functions' code-along (Day 5).

Ports F25's WRIT20833_Dictionaries_Functions_F25.ipynb into the existing 2026 code-along
house style (warm cultural examples; concept -> code -> 'your turn'; Putting It All Together ->
Sneak Preview -> Playground; colab metadata; no HW-style #comments). Walsh-independent. Trimmed
from F25's 52 cells to a focused Day-5 set that builds toward Week 2 term frequency (a count_words
dictionary -> Counter), matching the Lists/Loops notebook's own Sneak Preview of this lesson.

Two outputs from one cell list (2026-10-15, same approach as _build_variables.py / _build_lists.py /
_build_strings.py / _build_pandas01.py):
- WRIT20833_Dictionaries_Functions_2026.ipynb — the STUDENT copy. The first worked example of each
  idea stays complete; the next move is a "type along" blank (a one-line comment says what to
  write). One "predict first" guess. The `is_long` "your turn" no longer prints its own answer in a
  comment. This is the file the schedule, site, and D2L link to.
- WRIT20833_Dictionaries_Functions_2026_complete.ipynb — every blank filled in. Not linked yet.
A cell is either shared, or a pair(student, complete).

No complete cell depends on a name that only a blank defines (classify_year and count_words stay
complete because later cells call them). Expected errors: none.

Run from repo root:  python3 notebooks/codeAlongs/_build_dictfunc.py
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))


def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": _lines(text)}


def code(text):
    return {"cell_type": "code", "metadata": {}, "execution_count": None,
            "outputs": [], "source": _lines(text)}


def _lines(text):
    text = text.strip("\n")
    lines = text.split("\n")
    return [l + "\n" for l in lines[:-1]] + [lines[-1]]


def pair(student, complete):
    """A cell that differs between the student copy and the complete copy."""
    return {"student": student, "complete": complete}


STUDENT_NB = "WRIT20833_Dictionaries_Functions_2026.ipynb"
COMPLETE_NB = "WRIT20833_Dictionaries_Functions_2026_complete.ipynb"


def badge(name):
    return md('<a href="https://colab.research.google.com/github/TCU-DCDA/WRIT20833_2026/blob/main/'
              'notebooks/codeAlongs/' + name + '" target="_parent"><img src="https://colab.research.'
              'google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>')


def notebook(cells):
    # match the existing 2026 code-alongs' metadata exactly
    return {"cells": cells, "metadata": {
        "colab": {"provenance": []},
        "kernelspec": {"name": "python3", "display_name": "Python 3"},
        "language_info": {"name": "python"}}, "nbformat": 4, "nbformat_minor": 0}


cells = [
    pair(badge(STUDENT_NB), badge(COMPLETE_NB)),

    md('''# WRIT 20833 — Dictionaries & Functions

**When Coding Meets Culture: Developing Data-Driven Opinions**

Make an editable copy of this worksheet by going to **File > Save a copy in Drive**'''),

    pair(md('''**How today works.** Some code cells are blank on purpose:
- **type along** — a comment says what to write; type it with me, then run it.
- **predict first** — write your guess in the comment *before* you run the cell.
- **your turn** — try it on your own.

If a cell gives you an error, read the message — errors are part of the work here, not something to
hide.'''),
         md('''**Complete copy.** Every blank in the class worksheet is filled in here, so you can check your
work after class. The "predict first" guesses are left for you.''')),

    # ---- Dictionaries ----
    md('''# Dictionaries

Last time, **lists** stored items in order. But a lot of cultural data isn't just a sequence — it's
**labeled**. A song has a title, an artist, a year. A **dictionary** stores **key–value pairs**: each
value gets a name (its *key*) that you look it up by.

- Created with curly braces `{}`
- Each entry is `key: value`, entries separated by commas
- Look a value up by its key with `dictionary["key"]`'''),
    code('''album = {
    "title": "Renaissance",
    "artist": "Beyoncé",
    "year": 2022,
    "tracks": 16
}

print(album["title"])
print(album["artist"], "—", album["year"])'''),
    md('### Keys and values\nYou can ask a dictionary for all of its keys or all of its values.'),
    pair(code('''# type along — print the album's .keys(), then its .values()
'''),
         code('''print(album.keys())
print(album.values())''')),
    md('''### Adding and changing entries
Dictionaries are editable. Assign to a key to **add** it (if it's new) or **change** it (if it
already exists).'''),
    pair(code('''# type along — add a "genre" key set to "dance-pop"; change "tracks" to 17; then print the whole dictionary
'''),
         code('''album["genre"] = "dance-pop"   # a new key
album["tracks"] = 17           # change an existing value
print(album)''')),
    md('### Your turn'),
    code('''# your turn — build a dictionary for a movie, video game, or creator you know
my_thing = {
    "title": "",
    "creator": "",
    "year": 0,
}

print(my_thing)'''),

    # ---- A collection ----
    md('''# A Small Cultural Archive

Real datasets are usually **many records that share the same fields** — a *list of dictionaries*.
Here's a tiny archive of artists.

**Predict first.** `artists[1]` is one record. Which artist is it? Write your guess, then run.'''),
    code('''artists = [
    {"name": "Kendrick Lamar", "city": "Compton", "grammys": 17},
    {"name": "Beyoncé", "city": "Houston", "grammys": 32},
    {"name": "Bad Bunny", "city": "San Juan", "grammys": 3},
]

# my guess: artists[1] is
print(artists[1]["name"], "is from", artists[1]["city"])'''),
    md('Loop through the whole archive — the same `for` loop from last lesson, now over dictionaries:'),
    pair(code('''# type along — loop through `artists` and print each name with its Grammy count
'''),
         code('''for artist in artists:
    print(f"{artist['name']} — {artist['grammys']} Grammys")''')),

    # ---- Counting with a dict (the bridge) ----
    md('''# Counting with a Dictionary

Here's the move that powers most text analysis: use a dictionary to **count** things. The **key** is
the thing; the **value** is how many times you've seen it. This is exactly how we'll count words in
real comments next week.'''),
    code('''# count how often each word appears
words = ["god", "law", "god", "freedom", "god", "law"]

counts = {}                 # start with an empty dictionary
for word in words:
    if word in counts:
        counts[word] = counts[word] + 1   # seen before — add one
    else:
        counts[word] = 1                  # first time — start at one

print(counts)'''),
    md('### Your turn'),
    code('''# your turn — count the platforms in this list using the same pattern
posts = ["TikTok", "YouTube", "TikTok", "Instagram", "YouTube", "TikTok"]

counts = {}
# loop through `posts` and count each platform here


print(counts)'''),

    # ---- Functions ----
    md('''# Functions

A **function** packages code into a reusable tool. You *define* it once with `def`, give it inputs
(*parameters*), and it can hand back a result with `return`.

```python
def function_name(input):
    do something
    return result
```'''),
    code('''def greet(name):
    return f"Welcome, {name}!"

print(greet("Frog fan"))
print(greet("Dr. Rode"))'''),
    md('''### Why functions? Write the recipe once.
Without a function you'd copy-paste the same lines every time you needed them. With one, you write the
logic **once** and reuse it — and if you fix it, you fix it everywhere at once.'''),
    code('''def classify_year(year):
    if year <= 1964:
        return "Boomer"
    elif year <= 1980:
        return "Gen X"
    elif year <= 1996:
        return "Millennial"
    else:
        return "Gen Z"

print(classify_year(1990))
print(classify_year(2005))'''),
    md('The payoff: call your function inside a loop to process a whole list.'),
    pair(code('''# type along — loop over `birth_years` and print each year with its generation, using classify_year
birth_years = [1962, 1985, 1997, 2004]
'''),
         code('''birth_years = [1962, 1985, 1997, 2004]

for year in birth_years:
    print(f"{year} → {classify_year(year)}")''')),
    md('''### More than one input
Functions can take several parameters.'''),
    pair(code('''# type along — define with_tax(price, rate) that returns price * (1 + rate); then call it with 9.99 and 0.0825
'''),
         code('''def with_tax(price, rate):
    return price * (1 + rate)

print(with_tax(9.99, 0.0825))   # Texas sales tax''')),
    md('### Your turn'),
    pair(code('''# your turn — finish this function so it returns True when a word is "long" (more than 6 letters)
def is_long(word):
    pass   # replace this line with a return statement

print(is_long("god"))      # want: False
print(is_long("freedom"))  # want: True'''),
         code('''# your turn — finish this function so it returns True when a word is "long" (more than 6 letters)
def is_long(word):
    return len(word) > 6

print(is_long("god"))      # want: False
print(is_long("freedom"))  # want: True''')),

    # ---- Putting it together ----
    md('''# Putting It All Together

Now combine **functions** and **dictionaries** into one reusable tool: a function that takes a list of
words and returns a dictionary of how often each appears. This is a first draft of the term-frequency
counter you'll use on real data next week.'''),
    code('''def count_words(word_list):
    counts = {}
    for word in word_list:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    return counts

sample = ["god", "law", "freedom", "god", "school", "god", "law"]
print(count_words(sample))'''),
    code('''# your turn — run count_words on your own list of words
my_words = ["frogs", "purple", "frogs", "tcu", "purple", "frogs"]

print(count_words(my_words))'''),

    # ---- Sneak preview ----
    md('''# Sneak Preview: Where This Is Going

Next week we leave practice data behind for **real** text — 93 actual YouTube comments about a Texas
law. Your `count_words` function is the seed of **term frequency**: finding what a text is *really*
about by counting its words. Python even ships with a tool, `Counter`, that does what you just wrote:'''),
    code('''from collections import Counter

comment = "god god law freedom god school law god"
words = comment.split()

print(Counter(words).most_common(3))   # the 3 most frequent words'''),
    md('''That little count is already a tiny act of *interpretation*: **we** chose to split on spaces,
**we** decided every word counts equally. Next week we'll ask what choices like these reveal — and what
they flatten.'''),

    md('# Playground'),
    code('# use this space to experiment!\n'),
]


for name, version in ((STUDENT_NB, "student"), (COMPLETE_NB, "complete")):
    picked = [c[version] if "student" in c else c for c in cells]
    out = os.path.join(HERE, name)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(notebook(picked), f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("wrote", out, "(%d cells)" % len(picked))
