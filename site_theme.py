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

STYLESHEET_NAME = "styles.css"  # the shared external stylesheet site pages link

THEME_CSS = r"""
:root{
  /* surfaces & ink */
  --paper:#f1eee4; --surface:#fbfaf3; --ink:#262a20; --muted:#6f7463; --faint:#a6aa99;
  --rule:#dcd8c9;
  /* greens — deepen across the term (week tints) + the primary */
  --wk1:#3a6b54; --wk2:#2f5d49; --wk3:#26513e; --wk4:#1e3b2f;
  --green:#1e3b2f; --green-mid:#2f5d49; --green-link:#2f6a4e;
  /* the one warm accent */
  --clay:#9c6f3f; --clay-bg:#ebdfc7; --clay-ink:#6a4922;
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

/* legend + mode pills (restrained, earthy — not a rainbow) */
.legend{display:flex;flex-wrap:wrap;gap:7px;align-items:center;margin-top:20px;}
.legend .lbl{font:600 10.5px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;
  color:var(--muted);margin-right:4px;}
.mode{display:inline-block;font:600 11.5px/1 var(--sans);letter-spacing:.02em;
  padding:5px 9px;border-radius:4px;color:#f3f0e6;white-space:nowrap;}
.m-codealong{background:#2f5d49;} .m-lab{background:#4a6b67;} .m-workshop{background:#6d7a42;}
.m-worksession{background:#9c6f3f;} .m-present{background:#825764;} .m-other{background:#6f7463;}

/* week sections */
.week{background:var(--surface);border:1px solid var(--rule);border-left:4px solid var(--wk);
  border-radius:3px;margin:22px 0;overflow:hidden;}
.week h2{margin:0;padding:13px 20px;font-size:17px;color:var(--wk);
  background:color-mix(in srgb,var(--wk) 7%,var(--surface));border-bottom:1px solid var(--rule);}

/* tables */
table{width:100%;border-collapse:collapse;}
th,td{text-align:left;padding:12px 16px;vertical-align:top;border-top:1px solid var(--rule);}
thead th{border-top:none;font:600 10.5px/1 var(--mono);letter-spacing:.12em;text-transform:uppercase;
  color:var(--faint);padding-top:13px;padding-bottom:11px;}
tbody tr:nth-child(even){background:color-mix(in srgb,var(--green) 3%,var(--surface));}
.c-day{width:72px;} .c-lec{width:25%;} .c-due{width:23%;}

/* day cell — date leads, session number is a quiet mono tag */
.day .wd{display:block;font-weight:700;font-size:14px;color:var(--ink);}
.day .dt{display:block;font-size:13px;color:var(--muted);}
.day .num{display:block;font:11px/1 var(--mono);color:var(--faint);margin-top:4px;letter-spacing:.02em;}
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
footer{font:11.5px/1.5 var(--mono);letter-spacing:.04em;color:var(--faint);text-align:center;margin-top:30px;}

@media (max-width:720px){.c-lec,.c-due{width:auto;} body{font-size:15px;}}
@media print{body{background:#fff;border-top-color:#000;} .week{break-inside:avoid;}}

/* ---- site components (landing dashboard) ---- */
/* top nav — an anchor launchpad */
.topnav{position:sticky;top:0;z-index:5;display:flex;flex-wrap:wrap;gap:6px 18px;align-items:center;
  background:var(--paper);border-bottom:1px solid var(--rule);padding:11px 0;margin-bottom:6px;
  font:600 12.5px/1 var(--sans);}
.topnav a{color:var(--green);border:none;}
.topnav a:hover{color:var(--clay);}
.topnav .spacer{flex:1;}
.topnav .ext{font:600 10.5px/1 var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--muted);}

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
.card .lbl{font:600 10.5px/1 var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--muted);}
.card h3{margin:6px 0 5px;font-size:16px;line-height:1.22;}
.card p{margin:0;font-size:13px;color:var(--muted);line-height:1.5;}
.card .when{display:inline-block;font:600 10.5px/1 var(--mono);color:var(--clay);margin-top:9px;letter-spacing:.03em;}
.card.soon{opacity:.62;} .card.soon:hover{border-left-color:var(--green-mid);background:var(--surface);}

/* resource list */
.reslist{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:8px 26px;
  list-style:none;padding:0;margin:16px 0 0;}
.reslist li{font-size:14px;border-bottom:1px solid var(--rule);padding:8px 0;}
.reslist li .k{display:block;font:600 10px/1 var(--mono);letter-spacing:.1em;text-transform:uppercase;
  color:var(--faint);margin-bottom:3px;}
.muted{color:var(--muted);}

/* ---- two-column app layout (left sidebar) ---- */
.app{display:grid;grid-template-columns:240px minmax(0,1fr);min-height:100vh;}
.sidebar{position:sticky;top:0;align-self:start;height:100vh;overflow:auto;
  background:color-mix(in srgb,var(--green) 5%,var(--paper));border-right:1px solid var(--rule);
  padding:26px 20px;}
.sidebar .brand{font:600 10.5px/1.4 var(--mono);letter-spacing:.16em;text-transform:uppercase;
  color:var(--clay);margin-bottom:6px;}
.sidebar .brandname{display:block;font-family:var(--serif);font-size:18px;line-height:1.18;
  color:var(--green);margin-bottom:24px;}
.sidenav{display:flex;flex-direction:column;gap:2px;}
.sidenav a{display:flex;align-items:baseline;gap:9px;padding:8px 11px;border-radius:6px;border:none;
  color:var(--ink);font:600 13.5px/1.2 var(--sans);}
.sidenav a .n{font:600 10px/1 var(--mono);color:var(--faint);min-width:16px;}
.sidenav a:hover{background:color-mix(in srgb,var(--green) 9%,transparent);color:var(--green);}
.sidenav a.active{background:var(--green);color:var(--paper);}
.sidenav a.active .n{color:color-mix(in srgb,var(--paper) 65%,transparent);}
.side-ext{margin-top:24px;padding-top:16px;border-top:1px solid var(--rule);
  display:flex;flex-direction:column;gap:9px;}
.side-ext a{border:none;font:600 11px/1 var(--mono);letter-spacing:.09em;text-transform:uppercase;
  color:var(--muted);}
.side-ext a:hover{color:var(--clay);}
.main{min-width:0;padding:34px 34px 64px;}
.main>*{max-width:960px;}

/* week sub-groups (e.g. code-alongs split by week) */
.wkgroup{margin-top:20px;}
.wkgroup>h3{display:flex;align-items:baseline;gap:9px;margin:0 0 2px;font-family:var(--sans);
  font-size:14px;color:var(--green);}
.wkgroup>h3 .wkn{font:600 10.5px/1 var(--mono);letter-spacing:.1em;text-transform:uppercase;
  color:var(--clay);}

@media (max-width:860px){
  .app{grid-template-columns:1fr;}
  .sidebar{position:static;height:auto;overflow:visible;border-right:none;
    border-bottom:1px solid var(--rule);padding:14px 18px;}
  .sidebar .brandname{display:none;} .sidebar .brand{margin-bottom:10px;}
  .sidenav{flex-direction:row;flex-wrap:wrap;gap:4px 6px;}
  .sidenav a{padding:5px 9px;font-size:12.5px;}
  .sidenav a .n{display:none;}
  .side-ext{flex-direction:row;gap:14px;margin-top:12px;padding-top:12px;}
  .main{padding:22px 18px 48px;}
}

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
.reading figure{margin:24px 0;}
.reading figure img{display:block;max-width:100%;height:auto;border:1px solid var(--rule);
  border-radius:3px;background:var(--surface);padding:6px;}
.reading figcaption{margin-top:8px;font:11.5px/1.5 var(--mono);letter-spacing:.02em;color:var(--muted);}
.reading hr{border:none;border-top:1px solid var(--rule);margin:30px 0;}
.reading footer{text-align:left;border-top:1px solid var(--rule);padding-top:14px;margin-top:34px;}
"""


def PAGE(title, body, extra_css="", wrap=True, css_href=STYLESHEET_NAME):
    """Wrap an HTML body fragment in a full document with the course theme.

    By default the theme loads from the external stylesheet ``css_href`` (written by
    ``write_stylesheet``), so the shared CSS lives in one cached file. Pass ``css_href=None``
    to inline ``THEME_CSS`` instead and get a single fully self-contained page (e.g. to hand
    someone one .html file). Page-specific ``extra_css`` is always inlined.

    wrap=True  -> body is centered in a max-width column (.wrap) — single-column pages.
    wrap=False -> body is emitted as-is — for full-bleed layouts like the sidebar shell (.app).
    """
    inner = f'<div class="wrap">{body}</div>' if wrap else body
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
    path = os.path.join(out_dir, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(THEME_CSS.strip() + "\n")
    return path


def sidebar(brand_kicker, brand_name, nav_items, externals):
    """Build the left sidebar. nav_items: [(href, label, num_or_None)]; externals: [(href, label)]."""
    links = "".join(
        f'<a href="{href}">' + (f'<span class="n">{n}</span>' if n else "") + f"{label}</a>"
        for (href, label, n) in nav_items
    )
    ext = "".join(f'<a href="{href}">{label}</a>' for (href, label) in externals)
    return (
        '<aside class="sidebar">'
        f'<div class="brand">{brand_kicker}</div>'
        f'<span class="brandname">{brand_name}</span>'
        f'<nav class="sidenav">{links}</nav>'
        f'<div class="side-ext">{ext}</div>'
        "</aside>"
    )


def shell(side, main):
    """Two-column app layout: sticky left sidebar + main content."""
    return f'<div class="app">{side}<main class="main">{main}</main></div>'
