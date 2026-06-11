"""WRIT 20833 — course site visual identity ("Reading Room").

Shared design system for every generated HTML page, so the whole course site reads as one
hand-made thing rather than a default template. Pages **inline** `THEME_CSS` (kept self-contained —
no external stylesheet to break when a page is opened from disk, Colab, D2L, or email). Import it and
append page-specific rules as needed.

Design direction — *coding meets culture*, an editorial "reading room":
- Warm parchment paper with deep, muted **greens** — nothing bright, nothing black.
- **Serif** headings (the humanities) + **monospace** data accents (the code); body in a clean sans.
- Hairline rules and color do the work instead of drop-shadows and rounded "cards".
- **Green** links, not the default blue; an earthy **clay** as the single warm accent.
- A restrained, harmonious palette — no primary-colour rainbow of pills.

`PAGE` wraps a body fragment into a full self-contained document; pass extra CSS via `extra_css`.
"""

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
"""


def PAGE(title, body, extra_css=""):
    """Wrap an HTML body fragment in a full self-contained document with the course theme."""
    return (
        '<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"<title>{title}</title>\n<style>{THEME_CSS}{extra_css}</style></head>\n"
        f'<body><div class="wrap">{body}</div></body></html>\n'
    )
