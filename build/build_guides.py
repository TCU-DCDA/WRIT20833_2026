"""Build the how-to guide pages from materials/guides/*.md -> docs/guides/<slug>.html.

Short practical pages (working in Colab, getting a YouTube API key) linked from the home page's
Resources section. Same markdown subset and "Reading Room" reading layout as the lecture pages
(build_lectures.py renders them); no slide deck. Links inside a guide are relative to docs/guides/,
so the Code Guide is ``../chatbot.html``. A heading may end in ``{#id}`` to give it a link anchor
(``## Reflection 1 … {#r1}`` -> ``reflections.html#r1``).

Run from repo root:  python3 build/build_guides.py
"""
import os as _os
_os.chdir(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))  # repo root: paths below are repo-relative
import html, os, re
from site_theme import PAGE, site_header, site_footer
from build_lectures import parse_head, md_inline, render_body

OUT_DIR = "docs/guides"

# Registry — (slug, source_md, kicker, home section). build_index.py links each page from that
# section of the home page; the section also sets the back link and the highlighted menu pill.
GUIDES = [
    ("working-in-colab", "materials/guides/working_in_colab.md", "Course guide", "Resources"),
    ("youtube-api-key", "materials/guides/youtube_api_key.md", "Course guide · Day 10", "Resources"),
    ("reflections", "materials/guides/reflections.md", "Self-reflections", "Assignments"),
]

_ANCHOR = re.compile(r"^(#{2,3} .*?)\s*\{#([\w-]+)\}\s*$")


def with_anchors(lines):
    """Strip ``{#id}`` from headings; return (lines, [ids in heading order, None where absent])."""
    out, ids = [], []
    for ln in lines:
        m = _ANCHOR.match(ln.strip())
        if m:
            out.append(m[1]); ids.append(m[2])
        else:
            out.append(ln)
            if re.match(r"^#{2,3} ", ln.strip()):
                ids.append(None)
    return out, ids


def build_guide(slug, src, kicker, section):
    lines = open(src, encoding="utf-8").read().splitlines()
    title, subtitle, _, body = parse_head(lines)
    body, ids = with_anchors(body)
    masthead = (
        f'<div class="backlink"><a href="../index.html#{section.lower()}">← {section}</a></div>'
        '<header class="masthead">'
        f'<div class="kicker">{html.escape(kicker)}</div>'
        f"<h1>{md_inline(title)}</h1>"
        + (f'<p class="sub">{md_inline(subtitle)}</p>' if subtitle else "")
        + "</header>"
    )
    rendered = render_body(body, lead=True)
    it = iter(ids)                       # headings render in source order, so ids pair up one-to-one
    rendered = re.sub(r"<h([23])>", lambda m: (f'<h{m[1]} id="{i}">' if (i := next(it)) else m[0]), rendered)
    inner = f'<div class="reading">{masthead}{rendered}</div>'
    page = PAGE(html.escape(f"{title} — WRIT 20833"), inner, wrap=True, css_href="../styles.css",
                header=site_header(active=section, prefix="../"),
                footer=site_footer("WRIT 20833 · When Coding Meets Culture · course guide"))
    out = os.path.join(OUT_DIR, f"{slug}.html")
    open(out, "w", encoding="utf-8").write(page)
    return out


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    for slug, src, kicker, section in GUIDES:
        out = build_guide(slug, src, kicker, section)
        print(f"wrote {out} ({os.path.getsize(out)} b)")
