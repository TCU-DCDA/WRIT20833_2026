"""Build the VADER Lexicon Explorer -> docs/guides/vader-lexicon.html.

A searchable view of the two data files that ship with vaderSentiment: the rated word list
(``vader_lexicon.txt``: token, mean, SD, ten human ratings) and the emoji descriptions
(``emoji_utf8_lexicon.txt``: emoji, text description, no rating). Linked from the Sentiment with VADER
code-along (Days 13-14) and from the home page's Resources section.

The data is read from the *installed* package, not copied by hand, so the page always matches what
``pip install vaderSentiment`` gives students. The build refuses to run against any version other than
``VADER_VERSION`` (the notebooks pin it); bump both together and re-read the page's notes when you do.

Emoji scores are VADER's own ``polarity_scores()`` compound for each emoji typed alone. The "words VADER
scored" beside each emoji are the per-word valences VADER computed on the way to that score, captured
by wrapping ``score_valence`` (VADER's last step) rather than re-implementing its rules.

Needs vaderSentiment importable (see the instructor CLAUDE.md, section 3, for which python3 has it).
Run from repo root:  python3 build/build_vader_lexicon.py
"""
import os as _os
_os.chdir(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))  # repo root: paths below are repo-relative
import ast, html, json, os, re, statistics
from importlib import metadata

from site_theme import PAGE, site_header, site_footer, assert_accessible, _contrast

VADER_VERSION = "3.3.2"
OUT = "docs/guides/vader-lexicon.html"
NOTEBOOK = "https://colab.research.google.com/github/TCU-DCDA/WRIT20833_2026/blob/main/notebooks/codeAlongs/WRIT20833_VADER_Sentiment_2026.ipynb"
PAPER = "https://ojs.aaai.org/index.php/ICWSM/article/view/14550"

SKIN_TONES = {chr(c) for c in range(0x1F3FB, 0x1F400)}
_WORDISH = re.compile(r"[a-z]{2,}", re.I)


# ---------------------------------------------------------------- data

def is_emoticon(token):
    """Emoticons are built from punctuation: no two letters in a row, and at least one character
    that is neither a letter nor a digit. Keeps ``:-p``, ``x-d``, ``<3`` on the emoticon side and
    textspeak like ``gr8``, ``143``, ``j/k``, ``r&r`` on the word side."""
    if re.fullmatch(r"[a-z]&[a-z]|[a-z]/[a-z]", token, re.I):
        return False
    return not _WORDISH.search(token) and bool(re.search(r"[^a-z0-9]", token, re.I))


def load_words(path):
    """Rows: [token, mean, sd, ratings[10], dup, emoticon, ratings_mean_if_different].
    dup: 0 listed once, 1 an earlier entry VADER overwrites, 2 the entry VADER keeps."""
    rows, seen = [], {}
    with open(path, encoding="utf-8") as f:
        for line in f.read().rstrip("\n").split("\n"):
            line = line.strip()
            if not line:
                continue
            token, mean, sd, ratings = line.split("\t")[:4]
            ratings = ast.literal_eval(ratings)
            mean, sd = float(mean), float(sd)
            avg = round(statistics.mean(ratings), 1)
            off = avg if abs(avg - mean) > 0.051 else 0
            if token in seen:
                rows[seen[token]][4] = 1
                dup = 2
            else:
                dup = 0
            seen[token] = len(rows)
            rows.append([token, mean, sd, ratings, dup, int(is_emoticon(token)), off, 0])
    # VADER lowercases every token before looking it up (sentiment_valence: item.lower()), so an entry
    # with a capital letter is never used. Field 7 records what VADER looks up instead:
    # [lowercase token, its rating] or [lowercase token, None] when nothing matches.
    final = {}
    for r in rows:
        final[r[0]] = r[1]                # later duplicates win, as in make_lex_dict
    for r in rows:
        low = r[0].lower()
        if low != r[0]:
            r[7] = [low, final.get(low)]
    return rows


def load_emoji(path, analyzer):
    """Rows: [glyph, description, reads_as or 0, [[word, valence], ...], compound, skin_variant]."""
    captured = {}
    original = analyzer.score_valence

    def capture(sentiments, text):
        captured["sentiments"], captured["text"] = list(sentiments), text
        return original(sentiments, text)

    from vaderSentiment.vaderSentiment import SentiText
    analyzer.score_valence = capture
    rows = []
    try:
        with open(path, encoding="utf-8") as f:
            for line in f.read().rstrip("\n").split("\n"):
                glyph, desc = line.strip().split("\t")[:2]
                compound = analyzer.polarity_scores(glyph)["compound"]
                text = captured["text"]
                tokens = SentiText(text).words_and_emoticons
                hits = [[w, round(v, 2)] for w, v in zip(tokens, captured["sentiments"]) if v]
                reads = text if text != desc else 0
                skin = int(any(ch in SKIN_TONES for ch in glyph))
                rows.append([glyph, desc, reads, hits, compound, skin])
    finally:
        analyzer.score_valence = original
    return rows


# The "Emoticon vs emoji" tab: hand-picked pairs that mean roughly the same thing. A pairing is a
# judgment call, so the page says so; the scores beside each are computed, never typed in.
# The heart appears twice on purpose (VS16 vs plain), and 🥲 is there because it is newer than
# VADER's emoji file.
PAIRS = [
    ("smile", ":)", "\U0001F642"),
    ("big grin", ":D", "\U0001F600"),
    ("laughing", "XD", "\U0001F606"),
    ("happy tears", ":')", "\U0001F602"),
    ("smiling through tears", ":')", "\U0001F972"),
    ("wink", ";)", "\U0001F609"),
    ("tongue out", ":P", "\U0001F61B"),
    ("kiss", ":*", "\U0001F618"),
    ("love (heart + VS16)", "<3", "❤️"),
    ("love (plain heart)", "<3", "❤"),
    ("heartbreak", "</3", "\U0001F494"),
    ("frown", ":(", "☹️"),
    ("crying", ":'(", "\U0001F62D"),
    ("angry", ">:(", "\U0001F621"),
    ("angry", ":@", "\U0001F620"),
    ("unsure", ":/", "\U0001F615"),
    ("straight face", ":|", "\U0001F610"),
    ("surprised", ":o", "\U0001F62E"),
    ("cool", "8)", "\U0001F60E"),
    ("angel", "o:)", "\U0001F607"),
    ("devilish", ">:)", "\U0001F608"),
]


def load_pairs(analyzer, words, emoji):
    """Rows: [meaning, emoticon, stored rating, emoticon compound,
              emoji, description or 0 if not in VADER's file, hits, emoji compound, reads_as or 0]."""
    rating = {}
    for w in words:                     # later duplicates overwrite earlier ones, as in VADER
        rating[w[0]] = w[1]
    by_glyph = {e[0]: e for e in emoji}
    rows = []
    for meaning, emoticon, glyph in PAIRS:
        used = emoticon.lower()         # what VADER actually looks up
        stored = rating.get(used)
        assert stored is not None, f"VADER finds no rating for {emoticon} (looks up {used})"
        e = by_glyph.get(glyph)
        compound = analyzer.polarity_scores(glyph)["compound"]
        if e:
            assert e[4] == compound
            glued = 0
        else:                           # unsupported: stays in the text and can hide the word before it
            glued = [analyzer.polarity_scores("good" + glyph)["compound"],
                     analyzer.polarity_scores("good " + glyph)["compound"]]
        rows.append([meaning, emoticon, stored, analyzer.polarity_scores(emoticon)["compound"],
                     glyph, e[1] if e else 0, e[3] if e else [], compound, e[2] if e else 0,
                     used if used != emoticon else 0, glued])
    return rows


def build_data():
    version = metadata.version("vaderSentiment")
    assert version == VADER_VERSION, f"installed vaderSentiment is {version}; this page documents {VADER_VERSION}"
    from vaderSentiment import vaderSentiment as vs
    pkg = os.path.dirname(vs.__file__)
    analyzer = vs.SentimentIntensityAnalyzer()
    words = load_words(os.path.join(pkg, "vader_lexicon.txt"))
    emoji = load_emoji(os.path.join(pkg, "emoji_utf8_lexicon.txt"), analyzer)
    pairs = load_pairs(analyzer, words, emoji)
    return {"words": words, "emoji": emoji, "pairs": pairs}


# ---------------------------------------------------------------- page

# Diverging pair on the site's paper: green for positive (the site's link green), a muted wine for
# negative. Both carry text, so both are checked against WCAG AA below. Direction (left/right of the
# centre line) and the sign on the number carry the same information as the colour.
NEG, POS, NEU = "#9a3446", "#2f6a4e", "#696e5e"
NEG_SOFT, POS_SOFT = "#f2e1e2", "#dfeadf"

EXTRA_CSS = f"""
.lex{{--neg:{NEG};--pos:{POS};--neu:{NEU};--neg-soft:{NEG_SOFT};--pos-soft:{POS_SOFT};
  --emoji:"Apple Color Emoji","Segoe UI Emoji","Noto Color Emoji",sans-serif;display:grid;gap:22px;}}
.lex [hidden]{{display:none!important;}}
.lex .backlink{{display:flex;gap:13px;align-items:baseline;font:600 12.5px/1 var(--sans);}}
.lex .backlink a{{color:var(--green);border:none;}} .lex .backlink a:hover{{color:var(--clay);}}
.lex .masthead{{margin-bottom:0;}}
.lex .masthead p{{max-width:72ch;}}
.lex p{{margin:0;}}
.facts{{display:flex;flex-wrap:wrap;gap:8px 28px;font-size:14px;color:var(--muted);}}
.facts b{{color:var(--ink);font:600 14px var(--mono);}}
.tabs{{display:flex;gap:4px;border-bottom:1px solid var(--rule);overflow-x:auto;}}
.tab{{appearance:none;background:none;border:0;border-bottom:2.5px solid transparent;margin-bottom:-1px;
  font:600 15px var(--sans);color:var(--muted);padding:10px 14px;cursor:pointer;white-space:nowrap;}}
.tab[aria-selected="true"]{{color:var(--green);border-bottom-color:var(--green);}}
.tab .n{{font:400 12px var(--mono);color:var(--muted);margin-left:6px;}}
.lex :focus-visible{{outline:2px solid var(--clay);outline-offset:2px;}}
.panel{{display:grid;gap:14px;}}
.about{{color:var(--muted);font-size:14.5px;max-width:74ch;}}
.about b{{color:var(--ink);}}
.controls{{display:flex;flex-wrap:wrap;gap:10px;align-items:center;}}
.search{{flex:1 1 240px;min-width:0;font:15px var(--sans);padding:9px 12px;border-radius:4px;
  border:1px solid var(--rule);background:var(--surface);color:var(--ink);}}
.lex select{{font:14px var(--sans);padding:8px 10px;border-radius:4px;border:1px solid var(--rule);
  background:var(--surface);color:var(--ink);}}
.chips{{display:flex;flex-wrap:wrap;gap:6px;}}
.lex .chip{{font:13px var(--sans);padding:5px 11px;border-radius:999px;cursor:pointer;margin:0;
  border:1px solid var(--rule);background:var(--surface);color:var(--muted);}}
.lex .chip[aria-pressed="true"]{{background:var(--green);border-color:var(--green);color:var(--paper);}}
.toggle{{display:inline-flex;align-items:center;gap:6px;font-size:13px;color:var(--muted);cursor:pointer;}}
.status{{font:13px var(--mono);color:var(--muted);}}
.list{{background:var(--surface);border:1px solid var(--rule);border-radius:4px;overflow:hidden;
  box-shadow:0 1px 2px rgba(38,42,32,.06);}}
.row{{display:grid;align-items:center;gap:6px 16px;padding:9px 14px;border-top:1px solid var(--rule);}}
.row:first-child{{border-top:0;}}
.row.colhead{{font:600 12px/1.2 var(--mono);text-transform:uppercase;letter-spacing:.1em;color:var(--faint);
  padding-block:10px;background:color-mix(in srgb,var(--green) 4%,var(--surface));}}
.words .row{{grid-template-columns:minmax(0,1.3fr) minmax(170px,1.6fr) 52px 112px;}}
.emoji .row{{grid-template-columns:48px minmax(0,1.6fr) minmax(0,1.4fr) minmax(150px,1.2fr);}}
.tok{{font:14px var(--mono);overflow-wrap:anywhere;min-width:0;}}
.dup .tok,.dup .score,.dup .sd{{opacity:.6;}}
.pill{{display:inline-block;font:500 12px var(--sans);padding:1px 7px;border-radius:999px;margin-left:6px;
  vertical-align:1px;border:1px solid var(--rule);color:var(--muted);white-space:nowrap;}}
.num{{font:13px var(--mono);font-variant-numeric:tabular-nums;}}
.muted{{color:var(--muted);}}
.score{{display:grid;grid-template-columns:1fr 50px;gap:10px;align-items:center;}}
.ruler{{position:relative;height:10px;border-radius:2px;background:color-mix(in srgb,var(--green) 6%,var(--paper));}}
.ruler::before{{content:"";position:absolute;left:50%;top:-3px;bottom:-3px;width:1px;background:var(--muted);opacity:.6;}}
.fill{{position:absolute;top:0;bottom:0;border-radius:2px;}}
.fill.neg{{background:var(--neg);}} .fill.pos{{background:var(--pos);}}
.v-neg{{color:var(--neg);}} .v-pos{{color:var(--pos);}} .v-zero{{color:var(--neu);}}
.hist{{display:grid;grid-template-columns:repeat(9,1fr);gap:2px;height:24px;align-items:end;}}
.hist span{{display:block;border-radius:1px;min-height:1px;background:var(--rule);}}
.hist span.n{{background:var(--neg);}} .hist span.p{{background:var(--pos);}} .hist span.z{{background:var(--neu);}}
.glyph{{font-family:var(--emoji);font-size:26px;line-height:1;text-align:center;}}
.name{{min-width:0;overflow-wrap:anywhere;}}
.reads{{display:block;font-size:12.5px;color:var(--muted);}}
.hits{{display:flex;flex-wrap:wrap;gap:4px;min-width:0;}}
.hit{{font:12px var(--mono);padding:1px 7px;border-radius:3px;white-space:nowrap;}}
.hit.n{{background:var(--neg-soft);color:var(--neg);}} .hit.p{{background:var(--pos-soft);color:var(--pos);}}
.inv{{font:12px var(--mono);padding:0 4px;margin:0 1px;border:1px dashed var(--muted);border-radius:3px;color:var(--muted);font-style:normal;}}
.none{{font-size:13px;color:var(--muted);font-style:italic;}}
.empty{{padding:28px 14px;text-align:center;color:var(--muted);}}
.more{{justify-self:start;font:600 14px var(--sans);cursor:pointer;padding:8px 14px;border-radius:4px;
  border:1px solid var(--rule);background:var(--surface);color:var(--green);}}
.lex .about-data{{display:grid;gap:10px;font-size:14.5px;color:#464b3d;max-width:74ch;
  border-top:1px solid var(--rule);padding-top:20px;}}
.lex .about-data h2{{margin:0;font-size:21px;}}
.pairs .row{{grid-template-columns:minmax(110px,.7fr) minmax(0,1fr) minmax(0,1.25fr);align-items:start;}}
.meaning{{font-weight:600;color:var(--green);padding-top:4px;}}
.side{{display:grid;grid-template-columns:52px minmax(0,1fr);gap:10px;align-items:start;min-width:0;}}
.side .sym{{text-align:center;padding-top:2px;}}
.side .tok.sym{{font-size:17px;}}
.side .glyph{{font-size:24px;}}
.side .hits{{margin-top:5px;}}
.side .reads{{margin-top:4px;}}
.pairs .pill{{margin:6px 0 0;}}
@media (max-width:640px){{
  .row.colhead{{display:none;}}
  .pairs .row{{grid-template-columns:minmax(0,1fr);}}
  .words .row{{grid-template-columns:minmax(0,1fr) 96px;}}
  .words .row .score{{grid-column:1/-1;grid-row:2;}}
  .words .row .sd{{display:none;}}
  .emoji .row{{grid-template-columns:40px minmax(0,1fr);}}
  .emoji .row .hits,.emoji .row .score{{grid-column:2;}}
}}
"""

BODY = """
<div class="lex">
  <div class="backlink" data-pagefind-ignore="all"><a href="../index.html#resources">← Resources</a>
    <a href="{notebook}">Sentiment with VADER notebook ↗</a></div>
  <header class="masthead">
    <div class="kicker">Reference · Days 13–14</div>
    <h1>VADER Lexicon Explorer</h1>
    <p class="sub">Every word, emoticon, and emoji VADER knows, and the numbers it gives them.</p>
    <p class="meta">The two data files bundled with VADER (version {version}), side by side. Words and emoticons come with
    human ratings. The emoji file holds only short English descriptions, not ratings: VADER swaps each emoji it recognizes
    for its description and scores whatever words in it are on the word list.</p>
    <p class="meta" style="margin-top:10px">These lists are only part of how VADER scores a sentence. Rules for “not,”
    “very,” ALL CAPS, “!!!” and “but” can change a score, using words that aren't on either list.</p>
  </header>
  <div class="facts" id="facts"></div>

  <nav class="tabs" role="tablist" aria-label="Lexicon">
    <button class="tab" role="tab" id="tab-words" aria-controls="panel-words">Words &amp; emoticons<span class="n" id="n-words"></span></button>
    <button class="tab" role="tab" id="tab-emoji" aria-controls="panel-emoji">Emoji<span class="n" id="n-emoji"></span></button>
    <button class="tab" role="tab" id="tab-pairs" aria-controls="panel-pairs">Emoticon vs emoji<span class="n" id="n-pairs"></span></button>
  </nav>

  <section class="panel" id="panel-words" role="tabpanel" aria-labelledby="tab-words">
    <p class="about">Each score is the rating stored in <code>vader_lexicon.txt</code>, on a scale from −4 (extremely
    negative) to +4 (extremely positive). It is meant to be the <b>mean of the 10 human ratings</b> listed beside it, and it
    is for every entry but {n_off}, which {off_verb} marked. The small chart shows how those 10 people voted, one bar per point
    on the scale. A wide spread means the raters disagreed. An average sums up what those ten people judged for one study; it
    doesn't settle what a word means in every community or context. These are stored ratings, not the −1 to +1 compound
    scores on the Emoji tab, so the numbers on the two tabs can't be compared directly.</p>
    <p class="about"><b>Being listed doesn't guarantee being used.</b> VADER lowercases text before it looks anything up, so
    the {n_caps} entries with capital letters (like <code>:P</code>) are never used. Each is marked with what VADER looks
    up instead.</p>
    <div class="controls">
      <input class="search" id="q-words" type="search" placeholder="Search words or emoticons, e.g. love, :(" autocomplete="off" spellcheck="false" aria-label="Search words and emoticons">
      <select id="sort-words" aria-label="Sort words">
        <option value="file">A–Z (file order)</option>
        <option value="neg">Most negative first</option>
        <option value="pos">Most positive first</option>
        <option value="sd">Most rater disagreement</option>
      </select>
    </div>
    <div class="controls">
      <div class="chips" id="tone-words" role="group" aria-label="Filter by score">
        <button class="chip" data-v="all" aria-pressed="true">All</button>
        <button class="chip" data-v="neg" aria-pressed="false">Negative</button>
        <button class="chip" data-v="pos" aria-pressed="false">Positive</button>
      </div>
      <div class="chips" id="kind-words" role="group" aria-label="Filter by kind">
        <button class="chip" data-v="all" aria-pressed="true">Everything</button>
        <button class="chip" data-v="word" aria-pressed="false">Words &amp; slang</button>
        <button class="chip" data-v="emo" aria-pressed="false">Emoticons</button>
      </div>
    </div>
    <div class="status" id="status-words" aria-live="polite"></div>
    <div class="list words" id="list-words"></div>
    <button class="more" id="more-words" hidden>Show 150 more</button>
  </section>

  <section class="panel" id="panel-emoji" role="tabpanel" aria-labelledby="tab-emoji" hidden>
    <p class="about">The score here is VADER's <b>compound</b> score (−1 to +1) for the emoji typed on its own, the same
    number the class notebook uses. It is calculated from the highlighted words in the emoji's description, which comes from
    <code>emoji_utf8_lexicon.txt</code>. It is not a stored rating, so it can't be compared directly with the −4 to +4
    numbers on the other tab, and the same emoji can score differently inside a sentence. Positive means ≥ 0.05 and negative
    means ≤ −0.05, the same cutoffs as <code>label_sentiment()</code> in the notebook.</p>
    <p class="about">The number beside each highlighted word is the value VADER used <i>in that description</i>. It is
    usually the word's rating from the other tab, but a rule can change it: a word in ALL CAPS counts for more when the rest
    of the text isn't in caps, “slightly” makes the next word count for less, and in “sad but relieved face” the word after
    “but” counts for more and the word before it for less.</p>
    <p class="about"><b>A score of 0 does not mean the emoji is neutral.</b> For the emoji on this page it means VADER found
    no word it could score in what the emoji became. Usually that's because no word in the description is on the word
    list. {zero_examples} Sometimes a known word is there but hidden: an invisible character attached to “heart” keeps
    ❤️ at 0 (see the notes at the bottom). In a longer sentence, positive and negative words can also cancel out to 0.</p>
    <div class="controls">
      <input class="search" id="q-emoji" type="search" placeholder="Search descriptions or paste an emoji, e.g. heart" autocomplete="off" spellcheck="false" aria-label="Search emoji">
      <select id="sort-emoji" aria-label="Sort emoji">
        <option value="file">Unicode order</option>
        <option value="neg">Most negative first</option>
        <option value="pos">Most positive first</option>
        <option value="name">Description A–Z</option>
      </select>
    </div>
    <div class="controls">
      <div class="chips" id="tone-emoji" role="group" aria-label="Filter by score">
        <button class="chip" data-v="all" aria-pressed="true">All</button>
        <button class="chip" data-v="pos" aria-pressed="false">Positive</button>
        <button class="chip" data-v="neg" aria-pressed="false">Negative</button>
        <button class="chip" data-v="zero" aria-pressed="false">Scores 0</button>
      </div>
      <label class="toggle"><input type="checkbox" id="skin-emoji" checked> Hide skin-tone variants</label>
    </div>
    <div class="status" id="status-emoji" aria-live="polite"></div>
    <div class="list emoji" id="list-emoji"></div>
    <button class="more" id="more-emoji" hidden>Show 150 more</button>
  </section>

  <section class="panel" id="panel-pairs" role="tabpanel" aria-labelledby="tab-pairs" hidden>
    <p class="about">An emoticon and an emoji can mean the same thing and still get very different scores. Both columns
    here are the same kind of number, VADER's <b>compound</b> score (−1 to +1) for the symbol typed on its own, so they
    <i>can</i> be compared directly. What differs is where the number comes from.</p>
    <p class="about"><b>Emoticons were rated by people.</b> Ten raters scored <code>:)</code> itself, and VADER converts
    their average into the compound score. <b>VADER's emoji file contains descriptions, not ratings.</b> VADER swaps each
    emoji it recognizes for the English description stored in that file, then scores the words in the description. The
    description is a layer of interpretation someone wrote, and the score can only be as good as that wording.</p>
    <p class="about">So 💔 counts as positive: “heart” (+3.2) outweighs “broken” (−2.1). VADER can't tell that the phrase
    means heartbreak. Typing the words “broken heart” scores the same {broken_heart}. And 😡 counts as 0, because VADER's
    description for it is “pouting face” and neither word is on the list.</p>
    <p class="about">A gap between the two columns shows two VADER numbers disagreeing. It doesn't tell you which symbol
    people actually feel more strongly about. The pairs are our choice of rough equivalents, not part of VADER. Try
    others: search the Words tab for an emoticon and the Emoji tab for its match.</p>
    <div class="controls">
      <select id="sort-pairs" aria-label="Sort pairs">
        <option value="file">Grouped by meaning</option>
        <option value="gap">Biggest disagreement first</option>
      </select>
    </div>
    <div class="list pairs" id="list-pairs"></div>
  </section>

  <section class="about-data">
    <h2>About the data</h2>
    <p>Both files come from <b>vaderSentiment {version}</b>, the version the course notebooks install
    (<code>pip install vaderSentiment=={version}</code>). The emoji scores were produced by running VADER's own
    <code>polarity_scores()</code> on each emoji. The word list's ratings were collected by Hutto and Gilbert for
    <a href="{paper}">their 2014 ICWSM paper</a>.</p>
    <p><b>Listed twice.</b> {n_dup} tokens appear twice in the word file with different ratings ({dup_examples}). VADER keeps
    the second entry. The first is marked “not used.”</p>
    {off_note}
    <p><b>VADER swaps emoji one character at a time.</b> Before it scores anything, VADER walks through the text one
    character (one Unicode code point) at a time and replaces each character it finds in its emoji file. Emoji built from
    several characters (skin tones, flags, family groups) are never looked up as a whole. Each part it recognizes is
    replaced on its own, so {skin_example} Parts it doesn't recognize stay in the text unchanged: {flag_example} Invisible
    joining and style characters stay too, shown here as <span class="inv">ZWJ</span> and <span class="inv">VS16</span>, and
    they can break a word VADER would otherwise know. {heart_note} When what VADER reads differs from the description, it
    is shown under the description.</p>
    <p><b>Unsupported emoji aren't harmlessly skipped.</b> An emoji missing from VADER's file (newer ones, like 🥲) stays in
    the text. Typed right after a word, it glues onto that word and hides it: {glued_example}</p>
    {caps_note}
    <p><b>Version matters.</b> The counts on this page are for version {version}. Another version may ship different files.</p>
  </section>
</div>
<script type="application/json" id="data">{data}</script>
"""

SCRIPT = r"""<script>
(function () {
  var D = JSON.parse(document.getElementById("data").textContent);
  // words: [token, mean, sd, ratings[10], dup(0|1 not used|2 kept), isEmoticon, ratingsMeanIfDifferent|0,
  //         [lowercase token VADER looks up instead, its rating|null]|0]
  // emoji: [glyph, description, readsAs|0, hits[[word,valence]], compound, isSkinVariant]
  var W = D.words, E = D.emoji, PAGE = 150;

  function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); }
  function fmt(v, d) { var s = v.toFixed(d); return v > 0 ? "+" + s : (v < 0 ? "−" + s.slice(1) : s); }
  function vis(s) { return esc(s).replace(/‍/g, '<span class="inv">ZWJ</span>').replace(/️/g, '<span class="inv">VS16</span>'); }
  function cls(v) { return v > 0 ? "v-pos" : (v < 0 ? "v-neg" : "v-zero"); }
  function ruler(v, max) {
    var w = Math.min(Math.abs(v) / max, 1) * 50;
    var f = v === 0 ? "" : '<span class="fill ' + (v < 0 ? "neg" : "pos") + '" style="' + (v < 0 ? "right:50%" : "left:50%") + ";width:" + w.toFixed(2) + '%"></span>';
    return '<div class="score"><div class="ruler" aria-hidden="true">' + f + '</div><span class="num ' + cls(v) + '">' + fmt(v, max === 4 ? 1 : 3) + "</span></div>";
  }
  function hist(r) {
    var c = [0,0,0,0,0,0,0,0,0];
    r.forEach(function (x) { c[x + 4]++; });
    var h = "";
    for (var i = 0; i < 9; i++) {
      var k = i < 4 ? "n" : (i > 4 ? "p" : "z");
      h += '<span class="' + (c[i] ? k : "") + '" style="height:' + (c[i] ? Math.max(c[i] * 10, 12) : 4) + '%"></span>';
    }
    return '<div class="hist" role="img" aria-label="Ratings: ' + r.join(", ") + '" title="Ratings: ' + r.join(", ") + '">' + h + "</div>";
  }

  var nf = new Intl.NumberFormat("en-US");
  var used = W.filter(function (w) { return w[4] !== 1 && !w[7]; }).length;
  var zero = E.filter(function (e) { return e[4] === 0; }).length;
  document.getElementById("n-words").textContent = nf.format(W.length);
  document.getElementById("n-emoji").textContent = nf.format(E.length);
  document.getElementById("facts").innerHTML =
    "<span><b>" + nf.format(W.length) + "</b> rated words, slang and emoticons (" + nf.format(used) + " that VADER can use)</span>" +
    "<span><b>" + nf.format(E.length) + "</b> emoji descriptions, no ratings</span>" +
    "<span><b>" + nf.format(zero) + "</b> emoji (" + Math.round(zero / E.length * 100) + "%) score 0 on their own</span>";

  var S = {
    words: { q: "", sort: "file", tone: "all", kind: "all", limit: PAGE },
    emoji: { q: "", sort: "file", tone: "all", skin: true, limit: PAGE }
  };

  function rowsWords() {
    var s = S.words, q = s.q.trim().toLowerCase();
    var out = W.filter(function (w) {
      if (q && w[0].toLowerCase().indexOf(q) === -1) return false;
      if (s.tone === "neg" && !(w[1] < 0)) return false;
      if (s.tone === "pos" && !(w[1] > 0)) return false;
      if (s.kind === "emo" && !w[5]) return false;
      if (s.kind === "word" && w[5]) return false;
      return true;
    });
    if (s.sort === "neg") out.sort(function (a, b) { return a[1] - b[1]; });
    else if (s.sort === "pos") out.sort(function (a, b) { return b[1] - a[1]; });
    else if (s.sort === "sd") out.sort(function (a, b) { return b[2] - a[2]; });
    if (q && s.sort === "file") out.sort(function (a, b) { return (a[0].toLowerCase() !== q) - (b[0].toLowerCase() !== q); });
    return out;
  }
  function rowsEmoji() {
    var s = S.emoji, raw = s.q.trim(), q = raw.toLowerCase();
    var out = E.filter(function (e) {
      if (q && e[1].toLowerCase().indexOf(q) === -1 && e[0].indexOf(raw) === -1) return false;
      if (s.skin && e[5] && !(raw && e[0] === raw)) return false;
      if (s.tone === "pos" && !(e[4] >= 0.05)) return false;
      if (s.tone === "neg" && !(e[4] <= -0.05)) return false;
      if (s.tone === "zero" && e[4] !== 0) return false;
      return true;
    });
    if (s.sort === "neg") out.sort(function (a, b) { return a[4] - b[4]; });
    else if (s.sort === "pos") out.sort(function (a, b) { return b[4] - a[4]; });
    else if (s.sort === "name") out.sort(function (a, b) { return a[1].localeCompare(b[1]); });
    return out;
  }

  function render(tab) {
    var s = S[tab], all = tab === "words" ? rowsWords() : rowsEmoji();
    var shown = all.slice(0, s.limit), h;
    if (tab === "words") {
      h = '<div class="row colhead" aria-hidden="true"><span>Token</span><span>Mean rating (−4 to +4)</span><span>SD</span><span>10 raters</span></div>';
      h += shown.map(function (w) {
        var tag = w[4] === 1 ? '<span class="pill">not used</span>' : (w[4] === 2 ? '<span class="pill">listed twice</span>' : "");
        if (w[6]) tag += '<span class="pill">ratings average ' + w[6].toFixed(1) + "</span>";
        if (w[7]) tag += '<span class="pill">never used: VADER looks up \u201c' + esc(w[7][0]) + "\u201d" +
          (w[7][1] === null ? ", which isn't listed" : (w[7][1] === w[1] ? ", same rating" : ", rated " + fmt(w[7][1], 1))) + "</span>";
        return '<div class="row' + (w[4] === 1 || w[7] ? " dup" : "") + '"><span class="tok">' + esc(w[0]) + tag + "</span>" + ruler(w[1], 4) +
          '<span class="num muted sd">' + w[2].toFixed(2) + "</span>" + hist(w[3]) + "</div>";
      }).join("");
    } else {
      h = '<div class="row colhead" aria-hidden="true"><span></span><span>Description</span><span>Words VADER scored</span><span>Compound score (−1 to +1)</span></div>';
      h += shown.map(function (e) {
        var hits = e[3].length ? e[3].map(function (x) {
          return '<span class="hit ' + (x[1] < 0 ? "n" : "p") + '">' + esc(x[0]) + " " + fmt(x[1], Math.abs(x[1] * 10 - Math.round(x[1] * 10)) < 1e-9 ? 1 : 2) + "</span>";
        }).join("") : '<span class="none">no known words</span>';
        var reads = e[2] ? '<span class="reads">VADER reads “' + vis(e[2]) + "”</span>" : "";
        return '<div class="row"><span class="glyph">' + esc(e[0]) + '</span><span class="name">' + esc(e[1]) + reads + "</span>" +
          '<div class="hits">' + hits + "</div>" + ruler(e[4], 1) + "</div>";
      }).join("");
    }
    if (!all.length) h = '<div class="empty">Nothing matches. Try a shorter search or set the filters back to All.</div>';
    document.getElementById("list-" + tab).innerHTML = h;
    document.getElementById("status-" + tab).textContent = all.length
      ? "Showing " + nf.format(shown.length) + " of " + nf.format(all.length) : "";
    document.getElementById("more-" + tab).hidden = shown.length >= all.length;
  }

  ["words", "emoji"].forEach(function (tab) {
    var s = S[tab], t;
    document.getElementById("q-" + tab).addEventListener("input", function (ev) {
      clearTimeout(t);
      t = setTimeout(function () { s.q = ev.target.value; s.limit = PAGE; render(tab); }, 120);
    });
    document.getElementById("sort-" + tab).addEventListener("change", function (ev) { s.sort = ev.target.value; s.limit = PAGE; render(tab); });
    document.querySelectorAll("#tone-" + tab + " .chip, #kind-" + tab + " .chip").forEach(function (b) {
      b.addEventListener("click", function () {
        var group = b.parentNode, key = group.id.split("-")[0];
        group.querySelectorAll(".chip").forEach(function (c) { c.setAttribute("aria-pressed", c === b ? "true" : "false"); });
        s[key] = b.dataset.v; s.limit = PAGE; render(tab);
      });
    });
    document.getElementById("more-" + tab).addEventListener("click", function () { s.limit += PAGE; render(tab); });
  });
  document.getElementById("skin-emoji").addEventListener("change", function (ev) { S.emoji.skin = ev.target.checked; S.emoji.limit = PAGE; render("emoji"); });

  // pairs: [meaning, emoticon, storedRating, emoticonCompound, emoji, description|0, hits, emojiCompound, readsAs|0,
  //         tokenVaderLooksUp|0, [score "good"+emoji, score "good "+emoji]|0]
  var P = D.pairs, pairSort = "file";
  document.getElementById("n-pairs").textContent = P.length;
  function renderPairs() {
    var rows = P.slice();
    if (pairSort === "gap") rows.sort(function (a, b) { return Math.abs(b[3] - b[7]) - Math.abs(a[3] - a[7]); });
    var h = '<div class="row colhead" aria-hidden="true"><span>Meaning</span><span>Emoticon: rated by people</span><span>Emoji: scored from its description</span></div>';
    h += rows.map(function (p) {
      var hits = p[6].length ? p[6].map(function (x) {
        return '<span class="hit ' + (x[1] < 0 ? "n" : "p") + '">' + esc(x[0]) + " " + fmt(x[1], Math.abs(x[1] * 10 - Math.round(x[1] * 10)) < 1e-9 ? 1 : 2) + "</span>";
      }).join("") : '<span class="none">no known words</span>';
      var name = p[5] ? '<span class="reads">“' + esc(p[5]) + "”" + (p[8] ? ", but VADER reads “" + vis(p[8]) + "”" : "") + "</span>"
                      : '<span class="reads">not in VADER\'s emoji file, so it stays in the text unconverted and adds nothing. ' +
                        "Right after a word it hides the word too: \u201cgood" + esc(p[4]) + "\u201d scores " + fmt(p[10][0], 3) +
                        ", \u201cgood " + esc(p[4]) + "\u201d scores " + fmt(p[10][1], 3) + ".</span>";
      var flag = "";
      if (p[3] * p[7] < 0) flag = '<span class="pill">opposite directions</span>';
      else if (p[7] === 0 && p[3] !== 0) flag = '<span class="pill">emoji scores 0</span>';
      return '<div class="row"><div><span class="meaning">' + esc(p[0]) + "</span><br>" + flag + "</div>" +
        '<div class="side"><span class="sym tok">' + esc(p[1]) + "</span><div>" + ruler(p[3], 1) +
        '<span class="reads">' + (p[9] ? "VADER looks up <code>" + esc(p[9]) + "</code>, " : "") + "rated " + fmt(p[2], 1) +
        " by 10 people (\u22124 to +4)</span></div></div>" +
        '<div class="side"><span class="sym glyph">' + esc(p[4]) + "</span><div>" + ruler(p[7], 1) + name +
        (p[5] ? '<div class="hits">' + hits + "</div>" : "") + "</div></div></div>";
    }).join("");
    document.getElementById("list-pairs").innerHTML = h;
  }
  document.getElementById("sort-pairs").addEventListener("change", function (ev) { pairSort = ev.target.value; renderPairs(); });

  var TABS = ["words", "emoji", "pairs"];
  function show(tab) {
    TABS.forEach(function (k) {
      document.getElementById("tab-" + k).setAttribute("aria-selected", k === tab ? "true" : "false");
      document.getElementById("panel-" + k).hidden = k !== tab;
    });
  }
  TABS.forEach(function (k) {
    document.getElementById("tab-" + k).addEventListener("click", function () {
      show(k);
      try { history.replaceState(null, "", "#" + k); } catch (e) { location.hash = k; }
    });
  });
  function fromHash() { var k = location.hash.slice(1); show(TABS.indexOf(k) > 0 ? k : "words"); }
  window.addEventListener("hashchange", fromHash);
  render("words"); render("emoji"); renderPairs(); fromHash();
})();
</script>"""


def prose(data):
    """The counts and examples quoted in the page's notes, computed so they can't drift from the data."""
    words, emoji = data["words"], data["emoji"]
    by_glyph = {e[0]: e for e in emoji}

    dups = [w[0] for w in words if w[4] == 1]
    offs = [w for w in words if w[6]]
    out = {"n_dup": len(dups),
           "dup_examples": "for example " + " and ".join(f"<code>{html.escape(t)}</code>" for t in
                                                          [t for t in ("lol", "ok") if t in dups] or dups[:2]),
           "n_off": "none" if not offs else ("one" if len(offs) == 1 else str(len(offs))),
           "off_verb": "is" if len(offs) == 1 else "are"}
    if offs:
        bits = "; ".join(f"<code>{html.escape(w[0])}</code> is stored as {w[1]}, but its 10 listed ratings average {w[6]}"
                         for w in offs)
        out["off_note"] = (f"<p><b>Stored rating that doesn't match its ratings.</b> {bits}. VADER uses the stored "
                           f"number. {'It is' if len(offs) == 1 else 'They are'} marked in the list.</p>")
    else:
        out["off_note"] = ""

    zeros = [g for g in ("\U0001F44D", "\U0001F480") if g in by_glyph and by_glyph[g][4] == 0]
    out["zero_examples"] = (" and ".join(zeros) + " both score 0.") if len(zeros) == 2 else ""

    thumbs = "\U0001F44D\U0001F3FD"
    if thumbs in by_glyph:
        out["skin_example"] = f"“{thumbs}” reaches VADER as “{html.escape(by_glyph[thumbs][2] or by_glyph[thumbs][1])}.”"
    else:
        out["skin_example"] = "a thumbs-up with a skin tone reaches VADER as two descriptions in a row."

    heart_vs16, heart = "❤️", "❤"
    if heart_vs16 in by_glyph and heart in by_glyph:
        a, b = by_glyph[heart_vs16][4], by_glyph[heart][4]
        out["heart_note"] = (f"The red heart with the emoji-style character attached ({heart_vs16}, heart + VS16) "
                             f"scores {a:+.2f}, while the plain {heart} scores {b:+.2f}: VADER reads “heart” with VS16 "
                             f"stuck to it, which isn't on the word list.").replace("+0.00", "0")
    else:
        out["heart_note"] = ""

    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    analyzer = SentimentIntensityAnalyzer()
    score = lambda t: analyzer.polarity_scores(t)["compound"]
    out["broken_heart"] = f"{score('broken heart'):+.2f}"

    flag = "\U0001F1FA\U0001F1F8"
    if flag in by_glyph and by_glyph[flag][2] == flag:
        out["flag_example"] = f"{flag} is listed as “{by_glyph[flag][1]}”, but VADER never converts it."
    else:
        out["flag_example"] = "flags, for example, are listed but never converted."

    new = "\U0001F972"
    assert new not in by_glyph, "🥲 is now in VADER's emoji file: rewrite the unsupported-emoji note"
    out["glued_example"] = (f"“good{new}” scores {score('good' + new):+.3f}, while “good {new}” scores "
                            f"{score('good ' + new):+.3f}.").replace("+0.000", "0")

    caps = [w for w in words if w[7]]
    out["n_caps"] = len(caps)
    differ = [w for w in caps if w[7][1] != w[1]]
    bits = []
    for w in differ:
        t, low, v = html.escape(w[0]), html.escape(w[7][0]), w[7][1]
        bits.append(f"<code>{t}</code> is listed at {w[1]:+.1f}, but VADER uses <code>{low}</code> at {v:+.1f}"
                    if v is not None else f"<code>{t}</code> never scores, because <code>{low}</code> isn't listed")
    out["caps_note"] = (f"<p><b>Capital letters.</b> VADER lowercases every word before looking it up, so the {len(caps)} "
                        f"entries with capital letters are never used directly. Most have a lowercase twin with the same "
                        f"rating, but not all: {'; '.join(bits)}.</p>") if differ else ""
    # typographic minus in prose, to match the page's numbers
    return {k: (re.sub(r"(?<![\w<])-(?=\d)", "\u2212", v) if isinstance(v, str) else v) for k, v in out.items()}


def check_colours():
    for name, fg in (("neg", NEG), ("pos", POS), ("neu", NEU)):
        for bg in ("#fbfaf3", "#f1eee4"):
            r = _contrast(fg, bg)
            assert r >= 4.5, f"accessibility: --{name} {fg} on {bg} is {r:.2f}:1"
    assert _contrast(NEG, NEG_SOFT) >= 4.5 and _contrast(POS, POS_SOFT) >= 4.5, "accessibility: score chips"


def build():
    assert_accessible(EXTRA_CSS)
    check_colours()
    data = build_data()
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    body = BODY.format(version=VADER_VERSION, notebook=NOTEBOOK, paper=PAPER, data=payload, **prose(data)) + SCRIPT
    page = PAGE("VADER Lexicon Explorer — WRIT 20833", body, extra_css=EXTRA_CSS, css_href="../styles.css",
                header=site_header(active="Resources", prefix="../"),
                footer=site_footer("WRIT 20833 · When Coding Meets Culture · VADER lexicon"))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(page)
    return OUT, data


if __name__ == "__main__":
    out, data = build()
    print(f"wrote {out} ({os.path.getsize(out):,} b): {len(data['words']):,} words, {len(data['emoji']):,} emoji")
