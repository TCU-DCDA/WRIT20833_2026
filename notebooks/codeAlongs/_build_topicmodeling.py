"""Builder for the 2026 'Topic Modeling with Gensim' code-along (Days 14-15).

Dedups F25's THREE overlapping topic-modeling notebooks (Topic_Modeling_Gensim 41c,
Topic_Modeling_Part1_Introduction 29c, Topic_Modeling_Part2_Research_Application 24c) into ONE
combined Gensim code-along in the 2026 house style (warm cultural examples; concept -> code ->
'your turn'; Putting It All Together -> Sneak Preview -> Playground; colab metadata; no HW-style
#comments). Walsh-independent. Spans the two sessions (Day 14 intro + Day 15 deep/num_topics/limits).

Design choices vs F25:
- ALIGNS WITH HW4's simplified stack: gensim only (NO nltk/WordNet lemmatization, NO pyLDAvis —
  both fragile), and reuses the course's EXACT split_into_words + stopwords idiom from HW2/HW3/HW4
  (copied verbatim below) so the code-along preprocessing == the homework preprocessing.
- Teaches mechanics on a CLEAR 3-theme toy corpus (sports / music / food — distinct vocab so LDA
  separates cleanly and topic interpretation actually lands), THEN applies LDA to the real
  single-issue Ten Commandments comments to show topics BLUR — which is the Day-15 'limits' lesson
  and matches the WORKLOG's HW4 caveat (single-issue corpus -> weak/overlapping topics).
- LDA is STOCHASTIC + version-sensitive: random_state=42 pins within-environment, but NO topic words
  are hardcoded in prose — everything is printed and described qualitatively, exactly as HW4's key does.

Run from repo root:  python3 notebooks/codeAlongs/_build_topicmodeling.py
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))

# verbatim from _build_hw4.py so the code-along uses the SAME stopwords as the homework
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
    md('''# WRIT 20833 — Topic Modeling with Gensim

**When Coding Meets Culture: Developing Data-Driven Opinions**

Make an editable copy of this worksheet by going to **File > Save a copy in Drive**'''),

    md('''Your text-analysis journey, in three questions:
- **Term frequency** asked *what words appear most?*
- **Sentiment** asked *how does it feel?*
- **Topic modeling** asks the biggest one yet: *what is this whole pile of text even about?*

Given hundreds of documents, topic modeling discovers the **recurring themes** running through them —
clusters of words that tend to show up together. It's the deepest "distant reading" move in the course:
the computer surfaces patterns no one could find by reading one comment at a time. But — as always — it
hands you statistics, and **you** decide whether they're meaningful.'''),

    md('''### What LDA actually does
We'll use **LDA** (Latent Dirichlet Allocation) from the **Gensim** library. Its two assumptions:
1. Each **document** is a *mixture* of topics.
2. Each **topic** is a *cluster* of words that co-occur.

LDA works backward from the text to guess what those topics must be. It returns **lists of words** —
never names. Naming "money, dream, decay, green, light" as *the American Dream* is the human's job.'''),

    # ---- setup ----
    md('''# Setup

One new library, `gensim`, plus the **same** word-splitter and stopwords you've used since HW2 — topic
modeling reuses your own tools.'''),
    code('''!pip install -q gensim'''),
    code('''import re
from gensim import corpora
from gensim.models import LdaModel

# the exact split_into_words + stopwords from HW2/HW3/HW4
def split_into_words(any_chunk_of_text):
    return re.split(r"\\W+", str(any_chunk_of_text).lower())

''' + STOPWORDS_SRC + '''

print("Gensim ready. Stopwords loaded:", len(stopwords))'''),

    md('''### Preprocessing for topics is *more aggressive* than for sentiment
Remember VADER wanted punctuation and CAPS left in — emotional intensity mattered. Topic modeling is
the opposite: it cares about *which content words co-occur*, so we strip everything down to lowercase
meaning-words and drop the stopwords (the, and, is...) that appear everywhere and signal nothing.'''),
    code('''def preprocess_for_topics(text):
    return [w for w in split_into_words(text) if w and w not in stopwords]

print(preprocess_for_topics("The PAINTINGS were absolutely amazing!!! I loved the colors."))'''),

    # ---- clear toy corpus ----
    md('''# Part 1 — A Clear Example First

Topic modeling only makes sense if you can watch it work on text whose themes you *already* know. Here
are fifteen short online comments pulled from three very different corners of the internet. **Predict:**
how many topics are here, and what are they?'''),
    code('''docs = [
    # one corner of the internet
    "The team won the game and the players thanked the coach after a long season.",
    "Fans filled the stadium as the team scored late to win the game.",
    "The coach pushed the players all season and the team won the championship game.",
    "Our players lost the game but the coach says the team will win next season.",
    "The stadium roared when the team scored; the fans love this winning season.",
    # another corner
    "The band recorded a new album and the singer wrote every song on guitar.",
    "At the concert the band played songs from the album on a huge stage.",
    "The singer and the guitar player recorded the album and every song is a hit.",
    "Crowds heard the band play the new album live, song after song on stage.",
    "The album songs feature guitar and vocals while the band tours every concert stage.",
    # a third corner
    "We cooked dinner with a recipe for pasta, tomato sauce, garlic, and cheese.",
    "The kitchen smelled of garlic and fresh bread while the pasta sauce simmered.",
    "I cooked a dinner of pasta and bread, adding garlic, cheese, and tomato sauce.",
    "The recipe needs garlic, cheese, and tomato; we baked bread for dinner in the kitchen.",
    "Dinner was pasta with garlic sauce and warm bread fresh from the kitchen.",
]

tokens = [preprocess_for_topics(d) for d in docs]
print("Example tokenized doc:", tokens[0])'''),

    md('''### Build the dictionary and corpus
Gensim needs the text in its own format. The **dictionary** gives every unique word an id number; the
**corpus** rewrites each document as a bag of `(word_id, count)` pairs — a "bag of words."'''),
    code('''dictionary = corpora.Dictionary(tokens)
corpus = [dictionary.doc2bow(doc) for doc in tokens]

print("Unique words:", len(dictionary))
print("First doc as bag-of-words:", corpus[0])
print("Readable:", [(dictionary[i], c) for i, c in corpus[0]])'''),

    md('''### Train the model
We ask for **3 topics** (we suspect three). `random_state=42` pins the randomness so the result is
repeatable on this machine; `passes` is how many times LDA reads the corpus while it learns.'''),
    code('''lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=3, random_state=42, passes=10)

for i in range(3):
    words = [w for w, prob in lda.show_topic(i, 6)]
    print(f"Topic {i}: {', '.join(words)}")'''),
    md('''### Your turn: name the topics
Read each word list above. What theme does each one point to? (You'll almost certainly recognize the
three corners these comments came from.)'''),
    code('''# your turn — write your label for each topic as a comment
# Topic 0 =>
# Topic 1 =>
# Topic 2 =>
'''),

    md('''### Which topic does each comment belong to?
LDA never files a document under one topic — it gives every document a **mixture** (e.g. "70% topic 1,
30% topic 2"). We can still ask for its **dominant** topic, the biggest slice of the mix.'''),
    code('''for i, doc_bow in enumerate(corpus):
    dist = lda.get_document_topics(doc_bow)
    dominant = max(dist, key=lambda pair: pair[1])[0]
    print(f"Topic {dominant}  |  {docs[i][:55]}...")'''),
    md('''Most land where you'd expect — but you'll likely spot a comment or two filed under a neighbor.
That's the *mixture* showing through: these comments are short (a few words each), so a single shared
word can tip the balance. The fix is more, longer text per document — exactly the difference you're
about to see between this tidy example and real data.'''),

    # ---- Day 15: the knob ----
    md('''# Part 2 — How Many Topics? (an authored choice)

There is **no correct number of topics**. `num_topics` is a dial *you* set, and it changes what the
model finds. Too few and unrelated themes get mashed together; too many and one real theme splinters.
Watch what happens when we ask the same nine comments for 2 topics, then 4.'''),
    code('''for k in (2, 4):
    print(f"\\n=== {k} topics ===")
    model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=k, random_state=42, passes=10)
    for i in range(k):
        words = [w for w, prob in model.show_topic(i, 6)]
        print(f"  Topic {i}: {', '.join(words)}")'''),
    md('''Neither is "wrong." Choosing the number of topics is a **research decision** you justify by how
interpretable the result is — not a truth the algorithm reveals.'''),

    # ---- Day 15: the limits, on the real corpus ----
    md('''# Part 3 — The Limits: Real Comments Fight Back

That toy corpus was easy on purpose — three obviously different subjects. Now point the same machine
at our actual course data: the Texas Ten Commandments comments. They're all arguing about **one issue**,
in overlapping vocabulary. Watch the topics get muddy.'''),
    code('''comments = [
    "The Ten Commandments belong in every classroom, period.",
    "This is a clear violation of church and state. Keep it out.",
    "Morals matter and kids today need them more than ever.",
    "Whose religion gets to decide? Not the government's job.",
    "God and country, that's what built this nation.",
    "Public schools serve everyone, not just one faith.",
    "Put the Constitution in classrooms, not commandments.",
    "Finally some common sense values in our schools.",
    "Freedom of religion means freedom from it too.",
    "My kids should learn this at home, not at school.",
]

c_tokens = [preprocess_for_topics(c) for c in comments]
c_dict = corpora.Dictionary(c_tokens)
c_corpus = [c_dict.doc2bow(t) for t in c_tokens]

c_lda = LdaModel(corpus=c_corpus, id2word=c_dict, num_topics=3, random_state=42, passes=10)
for i in range(3):
    words = [w for w, prob in c_lda.show_topic(i, 6)]
    print(f"Topic {i}: {', '.join(words)}")'''),
    md('''Compare these to the toy corpus. There, each topic was a *different subject* you could name in a
word — sports, music, food. Here, every "topic" is just **more of the same argument**: LDA still hands
back three tidy word-lists, but they're slices of one debate about one law, not three distinct themes.
The model grouped words by raw co-occurrence — that's all it ever does — and with a small, single-issue
feed there simply aren't separate subjects to find. (Rerun it, or run it on a different machine, and the
groupings shift — LDA is **stochastic** and version-sensitive, which is why `random_state` only pins it
*here*.) **This isn't a bug.** Topic modeling shines on a *large, thematically diverse* collection;
knowing *when a method has little to say* is as important as knowing how to run it — and it's why HW4
wants a richer dataset of your own.'''),

    # ---- Putting it together ----
    md('''# Putting It All Together

The whole pipeline, start to finish — the moves you'll run in HW4:'''),
    code('''# 1. preprocess  ->  2. dictionary + corpus  ->  3. train  ->  4. read topics  ->  5. YOU interpret
tokens = [preprocess_for_topics(d) for d in docs]
dictionary = corpora.Dictionary(tokens)
corpus = [dictionary.doc2bow(t) for t in tokens]
lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=3, random_state=42, passes=10)

print("Discovered topics (your job: name them):")
for i in range(3):
    print(f"  Topic {i}: {', '.join(w for w, p in lda.show_topic(i, 6))}")'''),
    code('''# your turn — change num_topics above to 2 or 5, rerun, and see how the story changes
'''),

    # ---- Sneak preview ----
    md('''# Sneak Preview: Where This Is Going

**HW4 is the capstone of the techniques.** You'll run topic modeling on a dataset *you* collected — and
then **integrate** all three analyses: term frequency (what words), sentiment (what feeling), and topics
(what themes), on the same texts. One line ties them together — *average sentiment per topic* — and
suddenly you can say not just "the crowd is split," but "the crowd is **angriest** about *this* theme and
**warmest** about *that* one."

That integrated, evidence-backed reading of a real cultural conversation is exactly what your final
**capstone** asks for. You now have every tool it needs.'''),

    md('# Playground'),
    code('# use this space to experiment!\n'),
]


out = os.path.join(HERE, "WRIT20833_Topic_Modeling_Gensim_2026.ipynb")
with open(out, "w", encoding="utf-8") as f:
    json.dump(notebook(cells), f, indent=1, ensure_ascii=False)
    f.write("\n")
print("wrote", out, "(%d cells)" % len(cells))
