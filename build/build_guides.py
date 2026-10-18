"""Build the how-to guide pages from materials/guides/*.md -> docs/guides/<slug>.html.

Short practical pages (working in Colab, getting a YouTube API key) linked from the home page's
Resources section. Same markdown subset and "Reading Room" reading layout as the lecture pages
(build_lectures.py renders them); no slide deck. Links inside a guide are relative to docs/guides/,
so the Code Guide is ``../chatbot.html``.

Run from repo root:  python3 build/build_guides.py
"""
import os as _os
_os.chdir(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))  # repo root: paths below are repo-relative
import html, os
from site_theme import PAGE, site_header, site_footer
from build_lectures import parse_head, md_inline, render_body

OUT_DIR = "docs/guides"

# Registry — (slug, source_md, kicker). build_index.py links these from Resources.
GUIDES = [
    ("working-in-colab", "materials/guides/working_in_colab.md", "Course guide"),
    ("youtube-api-key", "materials/guides/youtube_api_key.md", "Course guide · Day 10"),
]


def build_guide(slug, src, kicker):
    lines = open(src, encoding="utf-8").read().splitlines()
    title, subtitle, _, body = parse_head(lines)
    masthead = (
        '<div class="backlink"><a href="../index.html#resources">← Resources</a></div>'
        '<header class="masthead">'
        f'<div class="kicker">{html.escape(kicker)}</div>'
        f"<h1>{md_inline(title)}</h1>"
        + (f'<p class="sub">{md_inline(subtitle)}</p>' if subtitle else "")
        + "</header>"
    )
    inner = f'<div class="reading">{masthead}{render_body(body, lead=True)}</div>'
    page = PAGE(html.escape(f"{title} — WRIT 20833"), inner, wrap=True, css_href="../styles.css",
                header=site_header(active="Resources", prefix="../"),
                footer=site_footer("WRIT 20833 · When Coding Meets Culture · course guide"))
    out = os.path.join(OUT_DIR, f"{slug}.html")
    open(out, "w", encoding="utf-8").write(page)
    return out


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    for slug, src, kicker in GUIDES:
        out = build_guide(slug, src, kicker)
        print(f"wrote {out} ({os.path.getsize(out)} b)")
