"""Build lecture pages from materials/lectures/*.md — the mini-lectures.

Each mini-lecture renders into TWO self-consistent views from one markdown source:
  * a student-facing **reading page**  -> docs/lectures/<slug>.html        (async reference)
  * a **slide deck** for live delivery -> docs/lectures/<slug>.deck.html   (synchronous class)

Both use the shared "Reading Room" theme (site_theme.py). The reading page links the external
../styles.css; the deck is **fully self-contained** (inlines the theme via PAGE(css_href=None) so it
can be presented offline / from a downloaded file). The markdown stays the single source of truth, so
the two views can never drift. Rendered subset: headings, paragraphs, lists, blockquotes, images, rules.

Pages sit one level below docs/, so repo-relative image paths (materials/…) are rewritten to absolute
raw.githubusercontent URLs the published site can reach (resolves once the repo is public).

Run from repo root:  python3 build_lectures.py
"""
import re, html, os
from site_theme import PAGE, write_stylesheet

REPO = "TCU-DCDA/WRIT20833_2026"
RAW = f"https://raw.githubusercontent.com/{REPO}/main/"
OUT_DIR = "docs/lectures"

# Registry — which mini-lectures have authored pages. (slug, source_md, ml, day)
# The dashboard (build_index.py) links these; lectures without an entry stay "soon" placeholders.
LECTURES = [
    ("ml0", "materials/lectures/ml0.md", "ML0", "Day 1"),
    ("ml1", "materials/lectures/ml1.md", "ML1", "Day 1"),
    ("ml3", "materials/lectures/ml3.md", "ML3", "Day 3"),
    ("ml5", "materials/lectures/ml5.md", "ML5", "Day 4"),
    ("ml4", "materials/lectures/ml4.md", "ML4", "Day 7"),
    ("ml6", "materials/lectures/ml6.md", "ML6", "Day 8"),
]


def _img_src(src):
    """Repo-relative image path -> absolute raw URL the /docs site can load; pass through http(s)."""
    if src.startswith(("http://", "https://")):
        return src
    return RAW + src.lstrip("./")


def md_inline(t):
    """Minimal inline markdown -> HTML: escape, then links/bold/italic/code."""
    t = html.escape(t, quote=False)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    return t


def parse_head(lines):
    """Pull the title (# ), subtitle (## ), and optional <!-- meta: … --> off the top.

    Returns (title, subtitle, meta, body_lines) — body is everything after the consumed head.
    """
    title = subtitle = meta = None
    consumed = -1
    for idx, ln in enumerate(lines):
        s = ln.strip()
        if not s:
            continue
        if title is None and s.startswith("# ") and not s.startswith("## "):
            title = s[2:].strip(); consumed = idx; continue
        if title is not None and subtitle is None and s.startswith("## "):
            subtitle = s[3:].strip(); consumed = idx; continue
        m = re.match(r'<!--\s*meta:\s*(.+?)\s*-->', s)
        if m and meta is None:
            meta = m.group(1).strip(); consumed = idx; continue
        break  # first real body line
    return title, subtitle, meta, lines[consumed + 1:]


_BLOCK_START = re.compile(r'^(#{2,3}\s|>\s|-\s|!\[|---\s*$)')


def render_blocks(lines, lead=False):
    """Render the markdown subset to a list of (kind, html) blocks — kind is 'figure' or 'text'.

    HTML comments (e.g. layout directives) are skipped. If lead, the first paragraph gets .lead.
    """
    out, i, n, lead_done = [], 0, len(lines), not lead
    while i < n:
        s = lines[i].strip()
        if not s or s.startswith("<!--"):                      # blank / comment / directive
            i += 1; continue
        m = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', s)          # standalone image -> figure
        if m:
            alt = html.escape(m.group(1))
            cap = f"<figcaption>{alt}</figcaption>" if alt else ""
            out.append(("figure", f'<figure><img src="{_img_src(m.group(2))}" alt="{alt}">{cap}</figure>'))
            i += 1; continue
        if s == "---":
            out.append(("text", "<hr>")); i += 1; continue
        if s.startswith("### "):
            out.append(("text", f"<h3>{md_inline(s[4:])}</h3>")); i += 1; continue
        if s.startswith("## "):
            out.append(("text", f"<h2>{md_inline(s[3:])}</h2>")); i += 1; continue
        if s.startswith("> "):                                 # blockquote (consecutive > lines)
            block = []
            while i < n and lines[i].strip().startswith(">"):
                block.append(lines[i].strip().lstrip(">").strip()); i += 1
            out.append(("text", "<blockquote>" + "".join(f"<p>{md_inline(b)}</p>" for b in block if b) + "</blockquote>"))
            continue
        if s.startswith("- "):                                 # unordered list (items may wrap)
            items = []
            while i < n:
                st = lines[i].strip()
                if st.startswith("- "):                         # new item
                    items.append(st[2:]); i += 1
                elif items and st and not st.startswith("<!--") and not _BLOCK_START.match(st):
                    items[-1] += " " + st; i += 1               # wrapped continuation of current item
                else:
                    break                                       # blank / comment / next block ends the list
            out.append(("text", "<ul>" + "".join(f"<li>{md_inline(it)}</li>" for it in items) + "</ul>"))
            continue
        para = [s]; i += 1                                      # paragraph (until blank/comment/next block)
        while i < n and lines[i].strip() and not lines[i].strip().startswith("<!--") \
                and not _BLOCK_START.match(lines[i].strip()):
            para.append(lines[i].strip()); i += 1
        cls = ' class="lead"' if not lead_done else ""
        lead_done = True
        out.append(("text", f"<p{cls}>{md_inline(' '.join(para))}</p>"))
    return out


def render_body(lines, lead=False):
    """Flatten render_blocks into one HTML string (normal stacked flow — the reading page)."""
    return "\n".join(h for _, h in render_blocks(lines, lead=lead))


# ---------- reading page ----------

def build_reading(slug, title, subtitle, kicker, body):
    masthead = (
        '<div class="backlink"><a href="../index.html">← Dashboard</a>'
        '<span class="sep">·</span><a href="../index.html#lectures">Lectures</a>'
        f'<span class="sep">·</span><a href="{slug}.deck.html">Slides ▸</a></div>'
        '<header class="masthead">'
        f'<div class="kicker">{html.escape(kicker)}</div>'
        f"<h1>{md_inline(title)}</h1>"
        + (f'<p class="sub">{md_inline(subtitle)}</p>' if subtitle else "")
        + "</header>"
    )
    footer = "<footer>WRIT 20833 · When Coding Meets Culture · mini-lecture</footer>"
    inner = f'<div class="reading">{masthead}{render_body(body, lead=True)}{footer}</div>'
    page = PAGE(html.escape(f"{title} — WRIT 20833"), inner, wrap=True, css_href="../styles.css")
    out = os.path.join(OUT_DIR, f"{slug}.html")
    open(out, "w", encoding="utf-8").write(page)
    return out


# ---------- slide deck (self-contained) ----------

DECK_CSS = r"""
.deck{position:fixed;inset:0;background:var(--paper);overflow:hidden;}
.slide{position:absolute;inset:0;display:none;flex-direction:column;justify-content:flex-start;
  padding:7vh 8vw 9vh;overflow:auto;}
.slide.active{display:flex;} .slide.title{justify-content:center;}
.slide>*{max-width:62rem;width:100%;}
.slide .kicker{font:600 13px/1 var(--mono);letter-spacing:.22em;text-transform:uppercase;
  color:var(--clay);margin-bottom:18px;}
.slide.title h1{font-family:var(--serif);color:var(--green);font-size:clamp(30px,5.4vw,56px);
  line-height:1.08;margin:0 0 16px;}
.slide.title .sub{font-family:var(--serif);font-style:italic;font-size:clamp(18px,2.7vw,27px);
  color:#464b3d;margin:0 0 20px;}
.slide h2{font-family:var(--serif);color:var(--green);font-size:clamp(24px,4vw,42px);line-height:1.12;
  margin:0 0 22px;padding-bottom:12px;border-bottom:2px solid var(--green);}
.slide p{font-size:clamp(16px,2.05vw,24px);line-height:1.5;margin:0 0 16px;color:var(--ink);}
.slide p.lead{font-family:var(--serif);color:#3c4133;}
.slide ul{font-size:clamp(16px,2vw,23px);line-height:1.45;margin:0 0 16px;padding-left:1.1em;}
.slide li{margin:10px 0;}
.slide blockquote{margin:10px 0 18px;padding:6px 0 6px 22px;border-left:4px solid var(--clay);
  font-family:var(--serif);font-style:italic;color:#474c3d;}
.slide blockquote p{font-size:clamp(19px,2.9vw,31px);line-height:1.38;margin:0;}
.slide figure{margin:6px 0;text-align:center;}
.slide figure img{max-height:62vh;width:auto;max-width:100%;border:1px solid var(--rule);
  border-radius:3px;background:var(--surface);padding:6px;}
.slide figcaption{font:12px/1.5 var(--mono);color:var(--muted);margin-top:8px;}
/* two-column split slide (text | image) */
.slide.split>.split-grid{display:grid;grid-template-columns:1.04fr .96fr;gap:5%;align-items:center;
  max-width:76rem;width:100%;}
.slide.split .col-text>*:first-child{margin-top:0;}
.slide.split .col-img figure{margin:0;}
.slide.split .col-img figure img{max-height:72vh;}
@media (max-width:760px){.slide.split>.split-grid{grid-template-columns:1fr;gap:20px;}}
/* gallery slide — text on top, figures in a row underneath */
.slide.gallery .fig-row{display:grid;gap:4%;align-items:start;max-width:74rem;width:100%;margin-top:6px;}
.slide.gallery .fig-row.cols-2{grid-template-columns:1fr 1fr;}
.slide.gallery .fig-row.cols-3{grid-template-columns:repeat(3,1fr);}
.slide.gallery .fig-row.cols-4{grid-template-columns:repeat(2,1fr);}
.slide.gallery .fig-row figure{margin:0;}
.slide.gallery .fig-row figure img{max-height:42vh;width:100%;object-fit:contain;background:#fbfaf6;}
.slide.gallery .fig-row figcaption{font-size:12px;}
@media (max-width:760px){.slide.gallery .fig-row{grid-template-columns:1fr !important;gap:16px;}}
.deck-progress{position:fixed;left:0;bottom:0;height:4px;background:var(--green);width:0;
  transition:width .2s;z-index:10;}
.deck-count{position:fixed;right:16px;bottom:11px;font:600 12px/1 var(--mono);color:var(--muted);z-index:10;}
.deck-hint{position:fixed;left:16px;bottom:11px;font:600 12px/1 var(--mono);letter-spacing:.1em;
  text-transform:uppercase;color:var(--faint);z-index:10;}
.deck-home{position:fixed;left:16px;top:13px;z-index:10;display:flex;gap:11px;align-items:baseline;
  font:600 12px/1 var(--mono);letter-spacing:.1em;text-transform:uppercase;opacity:.5;transition:opacity .2s;}
.deck-home:hover{opacity:1;}
.deck-home a{color:var(--green-mid);border:none;text-decoration:none;}
.deck-home a:hover{color:var(--clay);}
.deck-home .sep{color:var(--faint);}
@media print{.deck{position:static;overflow:visible;}
  .slide{display:flex !important;position:relative;inset:auto;min-height:88vh;page-break-after:always;
    border-bottom:1px solid var(--rule);}
  .deck-progress,.deck-count,.deck-hint,.deck-home{display:none;}}
"""

DECK_SCRIPT = """
<script>
(function(){
  var s=[].slice.call(document.querySelectorAll('.slide'));
  var prog=document.querySelector('.deck-progress'), cnt=document.querySelector('.deck-count'), i=0;
  function show(n){i=Math.max(0,Math.min(s.length-1,n));
    s.forEach(function(el,k){el.classList.toggle('active',k===i);el.scrollTop=0;});
    if(prog)prog.style.width=((i+1)/s.length*100)+'%';
    if(cnt)cnt.textContent=(i+1)+' / '+s.length;
    if(history.replaceState)history.replaceState(null,'','#'+(i+1));}
  document.addEventListener('keydown',function(e){
    if(['ArrowRight','ArrowDown','PageDown',' '].indexOf(e.key)>-1){e.preventDefault();show(i+1);}
    else if(['ArrowLeft','ArrowUp','PageUp'].indexOf(e.key)>-1){e.preventDefault();show(i-1);}
    else if(e.key==='Home'){show(0);} else if(e.key==='End'){show(s.length-1);}});
  document.addEventListener('click',function(e){if(!e.target.closest('a'))show(i+1);});
  var h=parseInt((location.hash||'').slice(1),10); show(h?h-1:0);
})();
</script>
"""


def split_slides(body_lines):
    """Split body into (heading_or_None, content_lines) segments at each '## ' boundary.

    The first segment (before any ## ) is the lead — it rides on the title slide.
    """
    slides, head, cur = [], None, []
    for ln in body_lines:
        if ln.strip().startswith("## "):
            slides.append((head, cur)); head, cur = ln.strip()[3:].strip(), []
        else:
            cur.append(ln)
    slides.append((head, cur))
    return slides


def _content_slide(head, lines):
    """One deck content slide.

    Layout directives (HTML comments anywhere in the segment):
      * '<!-- layout: split -->'   -> text | image, two columns
      * '<!-- layout: gallery -->' -> text on top, the figures in a row of equal columns underneath
    """
    split = any("<!-- layout: split -->" in ln for ln in lines)
    gallery = any("<!-- layout: gallery -->" in ln for ln in lines)
    blocks = render_blocks(lines)
    figs = [h for k, h in blocks if k == "figure"]
    if gallery and figs:
        text = "\n".join(h for k, h in blocks if k != "figure")
        figrow = f'<div class="fig-row cols-{min(len(figs), 4)}">' + "".join(figs) + "</div>"
        return f'<section class="slide gallery"><h2>{md_inline(head)}</h2>{text}{figrow}</section>'
    if split and figs:
        text = "\n".join(h for k, h in blocks if k != "figure")
        inner = (f"<h2>{md_inline(head)}</h2>"
                 f'<div class="split-grid"><div class="col-text">{text}</div>'
                 f'<div class="col-img">{"".join(figs)}</div></div>')
        return f'<section class="slide split">{inner}</section>'
    body_html = "\n".join(h for _, h in blocks)
    return f'<section class="slide"><h2>{md_inline(head)}</h2>{body_html}</section>'


def build_deck(slug, title, subtitle, kicker, body):
    segs = split_slides(body)
    lead_lines = segs[0][1]
    lead_split = any("<!-- layout: split -->" in ln for ln in lead_lines)
    lead_blocks = render_blocks(lead_lines, lead=True)
    lead_figs = [h for k, h in lead_blocks if k == "figure"]
    title_head = (
        f'<div class="kicker">{html.escape(kicker)}</div>'
        f"<h1>{md_inline(title)}</h1>"
        + (f'<p class="sub">{md_inline(subtitle)}</p>' if subtitle else "")
    )
    if lead_split and lead_figs:
        lead_text = "\n".join(h for k, h in lead_blocks if k != "figure")
        title_slide = (
            '<section class="slide title split">'
            f'<div class="split-grid"><div class="col-text">{title_head}{lead_text}</div>'
            f'<div class="col-img">{"".join(lead_figs)}</div></div>'
            "</section>"
        )
    else:
        title_slide = (
            '<section class="slide title">'
            + title_head
            + "\n".join(h for _, h in lead_blocks)
            + "</section>"
        )
    content = "".join(_content_slide(head, lines) for head, lines in segs[1:] if head)
    nav = (f'<div class="deck-home"><a href="../index.html#lectures">↤ Lectures</a>'
           f'<span class="sep">·</span><a href="{slug}.html">Reading</a></div>'
           '<div class="deck-progress"></div><div class="deck-count"></div>'
           '<div class="deck-hint">← → navigate · click to advance</div>')
    body_html = f'<div class="deck">{title_slide}{content}</div>{nav}{DECK_SCRIPT}'
    page = PAGE(html.escape(f"{title} (slides) — WRIT 20833"), body_html,
                extra_css=DECK_CSS, wrap=False, css_href=None)
    out = os.path.join(OUT_DIR, f"{slug}.deck.html")
    open(out, "w", encoding="utf-8").write(page)
    return out


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    write_stylesheet("docs")  # ensure the shared stylesheet exists for standalone runs
    for slug, src, ml, day in LECTURES:
        title, subtitle, meta, body = parse_head(open(src, encoding="utf-8").read().splitlines())
        kicker = meta or f"{ml} · {day}"
        r = build_reading(slug, title, subtitle, kicker, body)
        d = build_deck(slug, title, subtitle, kicker, body)
        print(f"wrote {r} ({os.path.getsize(r)} b) + {d} ({os.path.getsize(d)} b)")
