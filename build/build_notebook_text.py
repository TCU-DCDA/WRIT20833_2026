"""Build search-only text pages for the student notebooks -> docs/notebook-text/<notebook>.html.

Pagefind indexes HTML, and the notebooks are .ipynb files that open in Colab, so each student notebook
(every code-along and homework on the home page, plus the stylometry notebook) gets a plain page holding
its markdown and code. Nothing on the site links to these pages. The search page sends a notebook result
to Colab, using the ``colab`` meta stamped here, and shows the ``kind`` meta ("Code-along · Day 7") as its
label. Headings get ids so a result can name the section where the match sits.

The release gate carries over: each page carries the same ``opens`` date as the notebook's home-page card
(release_dates.release), and the search page drops results that have not opened yet (``?all=1`` shows all).
Notebook text is weighted below site pages, so a word on a lecture or guide outranks the same word in code.

Only the public student copies are read; answer keys and ``_complete`` copies never reach this repo.
The pre-commit hook re-runs this whenever a commit stages a notebook, then rebuilds the index.

Run from repo root:  python3 build/build_notebook_text.py   (then: sh .githooks/build-search-index.sh)
"""
import os as _os
_os.chdir(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))  # repo root: paths below are repo-relative
import html, json, os, re, shutil
from build_index import CODEALONGS_BY_WEEK, HOMEWORK, COLAB
from release_dates import release

# Not under an underscore folder: GitHub Pages runs Jekyll, which would drop it.
OUT_DIR = "docs/notebook-text"

# (title, kind label, repo-relative notebook path) — titles and days come from the home page's cards.
NOTEBOOKS = (
    [(t, f"Code-along · {w}", p) for _, _, items in CODEALONGS_BY_WEEK for (t, _, w, p) in items]
    + [(t, f"Homework · {w}", p) for (t, _, w, p) in HOMEWORK]
    + [("Stylometry (computational)", "Notebook · Day 18",
        "materials/stylometry/WRIT20833_Stylometry_Reading_Seams_2026.ipynb")]
)

_HEADING = re.compile(r"^(#{1,4})\s+(.*)$")


def _plain(md):
    """Markdown/HTML -> plain text for indexing: drop tags and images, keep link and emphasis text."""
    md = re.sub(r"<[^>]+>", " ", md)
    md = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", md)
    md = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", md)
    md = re.sub(r"[*_`]{1,3}", "", md)
    return re.sub(r"\s+", " ", md).strip()


def _slug(text, seen):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "section"
    n, base = 1, s
    while s in seen:
        n += 1; s = f"{base}-{n}"
    seen.add(s)
    return s


def render(title, kind, path):
    nb = json.load(open(path, encoding="utf-8"))
    colab = COLAB + path
    seen, parts = set(), []
    for cell in nb["cells"]:
        src = "".join(cell.get("source", []))
        if not src.strip():
            continue
        if cell["cell_type"] == "code":
            parts.append(f'<pre data-pagefind-weight="0.5">{html.escape(src)}</pre>')
            continue
        para = []
        for line in src.splitlines():
            m = _HEADING.match(line.strip())
            if m:
                if para:
                    parts.append(f'<p data-pagefind-weight="0.5">{html.escape(_plain(" ".join(para)))}</p>'); para = []
                text = _plain(m.group(2))
                if text and not text.startswith("WRIT 20833"):   # the notebook's banner repeats the title
                    lvl = min(len(m.group(1)) + 1, 4)   # the page's own <h1> is the notebook title
                    parts.append(f'<h{lvl} id="{_slug(text, seen)}">{html.escape(text)}</h{lvl}>')
            else:
                para.append(line)
        text = _plain(" ".join(para))
        if text:
            parts.append(f'<p data-pagefind-weight="0.5">{html.escape(text)}</p>')
    r = release(path)
    opens = f'<span hidden data-pagefind-meta="opens:{r[0]}"></span>' if r else ""
    return (
        '<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<meta name="robots" content="noindex">\n'
        f"<title>{html.escape(title)} — notebook text — WRIT 20833</title>\n"
        '<link rel="stylesheet" href="../styles.css"></head>\n'
        '<body><div class="wrap"><div class="reading">'
        f'<span hidden data-pagefind-meta="kind:{html.escape(kind)}"></span>'
        f'<span hidden data-pagefind-meta="colab:{html.escape(colab)}"></span>{opens}'
        f'<p class="muted" data-pagefind-ignore="all">This page holds a notebook\'s text for the site search. '
        f'<a href="{html.escape(colab)}">Open it in Colab ↗</a></p>'
        f"<h1>{html.escape(title)}</h1>\n" + "\n".join(parts) +
        "</div></div></body></html>\n"
    )


if __name__ == "__main__":
    shutil.rmtree(OUT_DIR, ignore_errors=True)   # a notebook dropped from the home page drops out of search
    os.makedirs(OUT_DIR)
    for title, kind, path in NOTEBOOKS:
        out = os.path.join(OUT_DIR, os.path.basename(path).replace(".ipynb", ".html"))
        open(out, "w", encoding="utf-8").write(render(title, kind, path))
    print(f"wrote {len(NOTEBOOKS)} pages to {OUT_DIR}/")
