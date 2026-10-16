"""WRIT 20833 — course site visual identity ("Reading Room").

Shared design system for every generated HTML page, so the whole course site reads as one
hand-made thing rather than a default template. `THEME_CSS` is the single source of truth.

The published `/docs` site links a shared **external** stylesheet (`styles.css`, written by
`write_stylesheet`) — its two pages always travel together, so external CSS is the cleaner, cached
choice. Need a *single self-contained* file instead (to email, drop in D2L, or open from disk
detached)? Call `PAGE(..., css_href=None)` and `THEME_CSS` is inlined as before. One source, both modes.

Design direction — *coding meets culture*, an editorial "reading room":
- Warm parchment paper with deep, muted **greens** — nothing bright, nothing black.
- **Serif** headings (the humanities) + **monospace** data accents (the code); body in a clean sans.
- Hairline rules and color do the work instead of drop-shadows and rounded "cards".
- **Green** links, not the default blue; an earthy **clay** as the single warm accent.
- A restrained, harmonious palette — no primary-colour rainbow of pills.

`PAGE` wraps a body fragment into a full document; pass extra CSS via `extra_css`.
"""
import os
import re

STYLESHEET_NAME = "styles.css"  # the shared external stylesheet site pages link

# external links (http/https) open in a new tab so the course site isn't navigated away from;
# relative/anchor links (intra-site) are untouched.
_A_TAG = re.compile(r'<a\b[^>]*>', re.I)


def _external_blank(html_fragment):
    """Add target=_blank + rel=noopener to <a> tags whose href is absolute http(s)."""
    def fix(m):
        tag = m.group(0)
        if "target=" in tag or not re.search(r'href="https?://', tag, re.I):
            return tag
        return '<a target="_blank" rel="noopener noreferrer"' + tag[2:]
    return _A_TAG.sub(fix, html_fragment)

THEME_CSS = r"""
:root{
  /* surfaces & ink */
  --paper:#f1eee4; --surface:#fbfaf3; --ink:#262a20; --muted:#696e5e; --faint:#6a6c61;
  --rule:#dcd8c9;
  /* greens — deepen across the term (week tints) + the primary */
  --wk1:#3a6b54; --wk2:#2f5d49; --wk3:#26513e; --wk4:#1e3b2f;
  --green:#1e3b2f; --green-mid:#2f5d49; --green-link:#2f6a4e;
  /* the one warm accent */
  --clay:#8c6338; --clay-bg:#ebdfc7; --clay-ink:#6a4922;
  /* type */
  --serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,"Times New Roman",serif;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  --mono:ui-monospace,"SF Mono","Cascadia Mono",Menlo,Consolas,monospace;
}
*{box-sizing:border-box;}
body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.6 var(--sans);
  border-top:5px solid var(--green);-webkit-font-smoothing:antialiased;}
.wrap{max-width:1060px;margin:0 auto;padding:36px 20px 64px;}
a{color:var(--green-link);text-decoration:none;
  border-bottom:1px solid color-mix(in srgb,var(--green-link) 26%,transparent);}
a:hover{border-bottom-color:var(--green-link);}
code{font:.88em var(--mono);background:color-mix(in srgb,var(--green) 8%,var(--surface));
  padding:1px 5px;border-radius:4px;color:var(--green-mid);}
h1,h2,h3{font-family:var(--serif);font-weight:600;color:var(--green);letter-spacing:-.01em;}

/* masthead */
.masthead{padding:2px 0 20px;border-bottom:2.5px solid var(--green);margin-bottom:28px;}
.kicker{font:600 12px/1 var(--mono);letter-spacing:.2em;text-transform:uppercase;
  color:var(--clay);margin-bottom:16px;}
.masthead h1{margin:0 0 10px;font-size:31px;line-height:1.1;}
.masthead .sub{margin:0 0 16px;font-family:var(--serif);font-style:italic;font-size:17.5px;color:#464b3d;}
.masthead .meta{margin:0;font-size:13.5px;color:var(--muted);max-width:74ch;}
/* masthead hero — a full-width landscape banner above the title */
.mast-banner{margin:0 0 22px;}
.mast-banner img{display:block;width:100%;height:clamp(150px,26vw,280px);object-fit:cover;
  object-position:center top;border:1px solid var(--rule);border-radius:4px;}

/* legend + mode pills (restrained, earthy — not a rainbow) */
.legend{display:flex;flex-wrap:wrap;gap:7px;align-items:center;margin-top:20px;}
.legend .lbl{font:600 12px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;
  color:var(--muted);margin-right:4px;}
.mode{display:inline-block;font:600 12px/1 var(--sans);letter-spacing:.02em;
  padding:5px 9px;border-radius:4px;color:#f3f0e6;white-space:nowrap;}
.m-codealong{background:#2f5d49;} .m-lab{background:#4a6b67;} .m-workshop{background:#6d7a42;}
.m-worksession{background:#8d6539;} .m-present{background:#825764;} .m-other{background:#6f7463;}

/* week sections */
.week{background:var(--surface);border:1px solid var(--rule);border-left:4px solid var(--wk);
  border-radius:3px;margin:22px 0;overflow:hidden;}
.week h2{margin:0;padding:13px 20px;font-size:17px;color:var(--wk);
  background:color-mix(in srgb,var(--wk) 7%,var(--surface));border-bottom:1px solid var(--rule);}

/* tables */
table{width:100%;border-collapse:collapse;}
th,td{text-align:left;padding:12px 16px;vertical-align:top;border-top:1px solid var(--rule);}
thead th{border-top:none;font:600 12px/1 var(--mono);letter-spacing:.12em;text-transform:uppercase;
  color:var(--faint);padding-top:13px;padding-bottom:11px;}
tbody tr:nth-child(even){background:color-mix(in srgb,var(--green) 3%,var(--surface));}
.c-day{width:72px;} .c-lec{width:25%;} .c-due{width:23%;}

/* day cell — date leads, session number is a quiet mono tag */
.day .wd{display:block;font-weight:700;font-size:14px;color:var(--ink);}
.day .dt{display:block;font-size:13px;color:var(--muted);}
.day .num{display:block;font:12px/1 var(--mono);color:var(--faint);margin-top:4px;letter-spacing:.02em;}
.c-lec{font-size:14.5px;color:#3c4133;}
.c-code{font-size:14.5px;}
.c-code .mode{margin-right:5px;}

/* due chips */
.chip{display:inline-block;font-size:12px;padding:3px 8px;border-radius:4px;
  background:color-mix(in srgb,var(--green) 6%,var(--surface));border:1px solid var(--rule);
  color:var(--muted);margin:1px 0;}
.chip-key{background:var(--clay-bg);border-color:color-mix(in srgb,var(--clay) 35%,transparent);
  color:var(--clay-ink);font-weight:600;}
.due-none{color:var(--faint);}

/* notes + footer */
.notes{border:1px solid var(--rule);border-radius:3px;background:var(--surface);
  padding:16px 24px;margin:26px 0 0;color:#54594a;font-size:13.5px;line-height:1.65;}
.notes p{margin:10px 0;} .notes strong{color:var(--green);}
footer{font:12px/1.5 var(--mono);letter-spacing:.04em;color:var(--faint);text-align:center;margin-top:30px;}

@media (max-width:720px){.c-lec,.c-due{width:auto;} body{font-size:15px;}}
@media print{body{background:#fff;border-top-color:#000;} .week{break-inside:avoid;}}

/* ---- site components (landing dashboard) ---- */
/* site chrome — the same sticky top bar + footer on every page (the 40363 model, in these tokens) */
.site-header{position:sticky;top:0;z-index:20;background:var(--green);
  border-bottom:1px solid color-mix(in srgb,var(--paper) 16%,transparent);}
.site-header .bar{max-width:1060px;margin:0 auto;display:flex;align-items:center;gap:16px;padding:11px 20px;}
.site-header .brand{display:flex;flex-direction:column;gap:4px;border:none;color:var(--paper);white-space:nowrap;}
.site-header .brand .k{font:600 12px/1 var(--mono);letter-spacing:.18em;text-transform:uppercase;color:var(--clay-bg);}
.site-header .brand .name{font:600 16px/1.1 var(--serif);}
.site-nav{margin-left:auto;display:flex;flex-wrap:wrap;gap:5px;}
.nav-pill{padding:7px 12px;border-radius:999px;border:1px solid color-mix(in srgb,var(--paper) 22%,transparent);
  font:600 13px/1 var(--sans);color:var(--paper);white-space:nowrap;}
.nav-pill:hover{background:color-mix(in srgb,var(--paper) 12%,transparent);
  border-color:color-mix(in srgb,var(--paper) 45%,transparent);}
.nav-pill.active{background:var(--clay-bg);border-color:transparent;color:var(--clay-ink);}
.nav-pill.active:hover{background:var(--clay-bg);}
.nav-toggle{display:none;margin-left:auto;align-items:center;justify-content:center;width:42px;height:38px;
  border-radius:8px;border:1px solid color-mix(in srgb,var(--paper) 32%,transparent);background:transparent;
  color:var(--paper);font-size:19px;line-height:1;cursor:pointer;}
.nav-toggle:hover{background:color-mix(in srgb,var(--paper) 12%,transparent);}
.site-footer{border-top:1px solid var(--rule);margin-top:24px;}
.site-footer .bar{max-width:1060px;margin:0 auto;padding:20px;display:flex;flex-wrap:wrap;gap:8px 22px;
  font:12px/1.5 var(--mono);letter-spacing:.04em;color:var(--faint);}
.site-footer .spacer{flex:1;}
.site-footer a{color:var(--muted);border:none;white-space:nowrap;} .site-footer a:hover{color:var(--clay);}
/* in-page jump row (the schedule's weeks) */
.jump{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin-top:16px;}
.jump .lbl{font:600 12px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin-right:4px;}
.jump a{font:600 12px/1 var(--mono);padding:6px 9px;border:1px solid var(--rule);border-radius:4px;
  background:var(--surface);color:var(--green);}
.jump a:hover{border-color:var(--green-mid);color:var(--clay);}
@media (max-width:860px){
  .site-header .bar{flex-wrap:wrap;}
  .nav-toggle{display:inline-flex;}
  .site-nav{display:none;margin-left:0;width:100%;flex-basis:100%;flex-direction:column;gap:6px;padding-top:10px;}
  .site-nav.open{display:flex;}
  .site-nav .nav-pill{text-align:left;}
}
@media (max-width:560px){.site-header .brand .name{display:none;}}

/* sections */
.sec{margin:38px 0 0;}
.sec>h2{display:flex;align-items:baseline;gap:10px;font-size:21px;margin:0;
  padding-bottom:8px;border-bottom:2px solid var(--green);}
.sec>h2 .n{font:600 12px/1 var(--mono);color:var(--clay);letter-spacing:.1em;}
.sec>.lede{margin:12px 0 16px;color:var(--muted);font-size:14px;max-width:76ch;}

/* card grid */
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(248px,1fr));gap:14px;margin-top:16px;}
.card{display:block;border:1px solid var(--rule);border-left:3px solid var(--green-mid);
  border-radius:3px;background:var(--surface);padding:14px 16px;color:inherit;}
a.card{text-decoration:none;border-bottom:none;}
a.card:hover{border-left-color:var(--clay);background:color-mix(in srgb,var(--green) 3%,var(--surface));}
.card .lbl{font:600 12px/1 var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--muted);}
.card h3{margin:6px 0 5px;font-size:16px;line-height:1.22;}
.card p{margin:0;font-size:13px;color:var(--muted);line-height:1.5;}
.card .when{display:inline-block;font:600 12px/1 var(--mono);color:var(--clay);margin-top:9px;letter-spacing:.03em;}
.card.linked{position:relative;}
.card.linked:hover{border-left-color:var(--clay);background:color-mix(in srgb,var(--green) 3%,var(--surface));}
.card a.stretch{color:inherit;border:none;text-decoration:none;}
.card a.stretch::after{content:"";position:absolute;inset:0;}
.card a.alt{position:relative;z-index:1;margin-left:12px;font:600 12px/1 var(--mono);letter-spacing:.03em;
  color:var(--green-mid);border-bottom:1px solid currentColor;text-decoration:none;}
.card a.alt:hover{color:var(--clay);}
.card.soon{opacity:.62;} .card.soon:hover{border-left-color:var(--green-mid);background:var(--surface);}
/* thumbnail cards — image (or proportion-matched placeholder) above the text */
.card.has-thumb{padding:0;overflow:hidden;}
.card .thumb{display:block;aspect-ratio:3/2;border-bottom:1px solid var(--rule);
  background:color-mix(in srgb,var(--green) 7%,var(--surface));}
.card .thumb img{width:100%;height:100%;object-fit:cover;object-position:center top;display:block;}
.card .thumb.ph{background:
  repeating-linear-gradient(45deg,transparent 0 11px,color-mix(in srgb,var(--green) 7%,transparent) 11px 12px),
  color-mix(in srgb,var(--green) 6%,var(--surface));}
.card-body{display:block;padding:13px 16px 15px;}

/* resource list */
.reslist{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:8px 26px;
  list-style:none;padding:0;margin:16px 0 0;}
.reslist li{font-size:14px;border-bottom:1px solid var(--rule);padding:8px 0;}
.reslist li .k{display:block;font:600 12px/1 var(--mono);letter-spacing:.1em;text-transform:uppercase;
  color:var(--faint);margin-bottom:3px;}
.muted{color:var(--muted);}

/* week sub-groups (e.g. code-alongs split by week) */
.wkgroup{margin-top:20px;}
.wkgroup>h3{display:flex;align-items:baseline;gap:9px;margin:0 0 2px;font-family:var(--sans);
  font-size:14px;color:var(--green);}
.wkgroup>h3 .wkn{font:600 12px/1 var(--mono);letter-spacing:.1em;text-transform:uppercase;
  color:var(--clay);}


/* ---- lecture / reading pages ---- */
.reading{max-width:50rem;margin:0 auto;}
.reading .backlink{display:flex;gap:13px;align-items:baseline;font:600 12.5px/1 var(--sans);margin-bottom:14px;}
.reading .backlink a{color:var(--green);border:none;} .reading .backlink a:hover{color:var(--clay);}
.reading .backlink .sep{color:var(--faint);}
.reading p{margin:0 0 17px;font-size:16.5px;}
.reading p.lead{font-family:var(--serif);font-size:19px;line-height:1.5;color:#3c4133;margin-bottom:22px;}
.reading h2{font-size:22px;margin:34px 0 10px;}
.reading h3{font-size:16.5px;margin:24px 0 7px;color:var(--green-mid);}
.reading ul{margin:0 0 17px;padding-left:22px;} .reading li{margin:6px 0;}
.reading blockquote{margin:22px 0;padding:4px 0 4px 20px;border-left:3px solid var(--clay);
  font-family:var(--serif);font-style:italic;color:#474c3d;}
.reading blockquote p{margin:0 0 8px;font-size:17.5px;line-height:1.5;} .reading blockquote p:last-child{margin-bottom:0;}
pre.codeblock{margin:6px 0 18px;padding:12px 16px;background:color-mix(in srgb,var(--green) 6%,var(--surface));
  border:1px solid var(--rule);border-left:3px solid var(--green-mid);border-radius:6px;overflow-x:auto;
  font:14.5px/1.55 var(--mono);color:var(--ink);}
pre.codeblock code{font:inherit;background:none;padding:0;color:inherit;}
figure a{border-bottom:none;}   /* a linked image needs no underline */
.reading figure{margin:24px 0;}
.reading figure img{display:block;max-width:100%;max-height:min(60vh,520px);width:auto;height:auto;margin:0 auto;border:1px solid var(--rule);
  border-radius:3px;background:var(--surface);padding:6px;}
.reading figcaption{margin:8px auto 0;max-width:60ch;text-align:center;font:12px/1.5 var(--mono);letter-spacing:.02em;color:var(--muted);}
/* portrait/square art sits beside the text that follows it; headings start below it */
.reading figure.upright{float:right;width:min(42%,340px);margin:6px 0 18px 28px;}
.reading figure.upright img{max-height:none;width:100%;}
.reading figure.upright figcaption{text-align:left;}
.reading h2,.reading h3,.reading hr,.reading footer,.reading pre.codeblock{clear:both;}   /* code needs the full column */
@media (max-width:700px){.reading figure.upright{float:none;width:auto;margin:24px 0;}
  .reading figure.upright img{width:auto;max-height:min(60vh,520px);}}
.reading hr{border:none;border-top:1px solid var(--rule);margin:30px 0;}
"""


def PAGE(title, body, extra_css="", wrap=True, css_href=STYLESHEET_NAME, header="", footer=""):
    """Wrap an HTML body fragment in a full document with the course theme.

    ``header`` / ``footer`` (from ``site_header()`` / ``site_footer()``) are emitted full-width
    outside the ``.wrap`` column, and a header brings the small menu-toggle script with it.

    By default the theme loads from the external stylesheet ``css_href`` (written by
    ``write_stylesheet``), so the shared CSS lives in one cached file. Pass ``css_href=None``
    to inline ``THEME_CSS`` instead and get a single fully self-contained page (e.g. to hand
    someone one .html file). Page-specific ``extra_css`` is always inlined.

    wrap=True  -> body is centered in a max-width column (.wrap) — single-column pages.
    wrap=False -> body is emitted as-is — for full-bleed layouts (the slide decks).
    """
    body = _external_blank(body)
    inner = f'<div class="wrap">{body}</div>' if wrap else body
    inner = _external_blank(header) + inner + _external_blank(footer) + (NAV_JS if header else "")
    if css_href is None:
        head_css = f"<style>{THEME_CSS}{extra_css}</style>"
    else:
        head_css = f'<link rel="stylesheet" href="{css_href}">'
        if extra_css:
            head_css += f"<style>{extra_css}</style>"
    return (
        '<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"<title>{title}</title>\n{head_css}</head>\n"
        f"<body>{inner}</body></html>\n"
    )


def write_stylesheet(out_dir, name=STYLESHEET_NAME):
    """Write the shared theme to ``out_dir/name`` — the external stylesheet pages link.

    Call this from each site generator so the published ``/docs`` folder always ships a
    current ``styles.css`` beside its HTML pages. Returns the path written.
    """
    assert_accessible()  # guard: fail the build if a font/contrast regression crept in
    path = os.path.join(out_dir, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(THEME_CSS.strip() + "\n")
    return path


REPO = "TCU-DCDA/WRIT20833_2026"
GH_URL = f"https://github.com/{REPO}"
COLAB_URL = "https://colab.research.google.com/"
SYLLABUS_URL = f"{GH_URL}/blob/main/SYLLABUS_2026.md"

# The site-wide menu, in order. (href, label); relative hrefs get the page's ``prefix``.
NAV_ITEMS = [
    ("schedule.html", "Schedule"),
    ("index.html#lectures", "Lectures"),
    ("index.html#codealongs", "Code-alongs"),
    ("index.html#homework", "Homework"),
    ("index.html#capstone", "Capstone"),
]
CHAT_ITEM = ("chatbot.html", "Code Guide")       # appended only once the Worker is deployed
SYLLABUS_ITEM = (SYLLABUS_URL, "Syllabus ↗")     # leaves the site, so it goes last

NAV_JS = ('<script>(function(){var t=document.querySelector(".nav-toggle"),n=document.getElementById("site-nav");'
          'if(!t||!n)return;t.addEventListener("click",function(){var o=n.classList.toggle("open");'
          't.setAttribute("aria-expanded",o?"true":"false");});'
          'n.querySelectorAll("a").forEach(function(a){a.addEventListener("click",function(){'
          'n.classList.remove("open");t.setAttribute("aria-expanded","false");});});})();</script>')


def site_header(active=None, prefix="", chat=False):
    """The sticky top bar every site page shares: brand (→ home) + the menu as pills.

    active: the label of the pill for the current page (None on the dashboard).
    prefix: path back to the site root for pages in a subfolder (``"../"`` for lectures).
    chat:   include the Code Guide pill (callers pass ``bool(CHAT_API_URL)``).
    """
    items = NAV_ITEMS + ([CHAT_ITEM] if chat else []) + [SYLLABUS_ITEM]
    pills = []
    for href, label in items:
        if not href.startswith("http"):
            href = prefix + href
        cls = "nav-pill active" if label == active else "nav-pill"
        cur = ' aria-current="page"' if label == active else ""
        pills.append(f'<a href="{href}" class="{cls}"{cur}>{label}</a>')
    return (
        '<header class="site-header"><div class="bar">'
        f'<a href="{prefix}index.html" class="brand"><span class="k">WRIT 20833 · Fall 2026</span>'
        '<span class="name">When Coding Meets Culture</span></a>'
        '<button class="nav-toggle" type="button" aria-label="Toggle menu" aria-expanded="false" '
        'aria-controls="site-nav">☰</button>'
        f'<nav class="site-nav" id="site-nav" aria-label="Primary">{"".join(pills)}</nav>'
        '</div></header>'
    )


def site_footer(text):
    """The footer bar: a page-specific line on the left, GitHub and Colab on the right."""
    return (
        '<footer class="site-footer"><div class="bar">'
        f'<span>{text}</span><span class="spacer"></span>'
        f'<a href="{GH_URL}">GitHub ↗</a><a href="{COLAB_URL}">Colab ↗</a>'
        '</div></footer>'
    )


# ---- accessibility guardrails (keep the site WAVE-clean across rebuilds) ----
MIN_FONT_PX = 12.0   # no UI text smaller than this (WAVE "very small text")
MIN_CONTRAST = 4.5   # WCAG AA for normal-size text


def _luminance(hexc):
    hexc = hexc.lstrip("#")
    chans = [int(hexc[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [(c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4) for c in chans]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def _contrast(a, b):
    la, lb = sorted((_luminance(a), _luminance(b)))
    return (lb + 0.05) / (la + 0.05)


def assert_accessible(extra_css=""):
    """Build-time guard so a future edit can't silently reintroduce the WAVE issues
    we fixed. Every ``font:``/``font-size:`` px value (in THEME_CSS + any extra_css a
    page inlines, e.g. the deck CSS) must be >= MIN_FONT_PX, and the muted text tokens
    (--muted/--faint/--clay) must clear WCAG AA on the paper/surface backgrounds.
    Raises AssertionError — failing the build — on regression. Generators call this
    via write_stylesheet(); build_lectures also passes its DECK_CSS.
    """
    css = THEME_CSS + extra_css
    small = sorted({float(sz)
                    for sz in re.findall(r'font(?:-size)?:[^;{]*?(\d+(?:\.\d+)?)px', css)
                    if float(sz) < MIN_FONT_PX})
    assert not small, f"accessibility: UI font(s) below {MIN_FONT_PX}px — {small}"
    tokens = dict(re.findall(r'--([\w-]+):\s*(#[0-9a-fA-F]{6})', THEME_CSS))
    for fg in ("muted", "faint", "clay"):
        for bg in ("paper", "surface"):
            r = _contrast(tokens[fg], tokens[bg])
            assert r >= MIN_CONTRAST, \
                f"accessibility: --{fg} on --{bg} is {r:.2f}:1 (< {MIN_CONTRAST} WCAG AA)"
