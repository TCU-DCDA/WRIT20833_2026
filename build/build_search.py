"""Build the site search page -> docs/search.html.

Search runs entirely in the browser over a static Pagefind index in docs/pagefind/, the same
approach as the WRIT 40363 site. The index is *not* written here: `.githooks/build-search-index.sh`
builds it from the finished pages in docs/ (the pre-commit hook runs it whenever a commit stages a
docs/ page). Every header carries a search box that GETs search.html?q=… (site_theme.site_search).

What is searched: the home page, the schedule, every lecture reading page and guide, and the text of
every student notebook. Notebooks are .ipynb files that open in Colab, so build_notebook_text.py writes
an unlinked text page for each into docs/notebook-text/; a notebook result links to Colab (its ``colab``
meta) and is labelled by its ``kind`` meta. Kept out with ``PAGE(searchable=False)``: this page, the
slide decks (the same text as their reading pages), and the Code Guide chat page.

The release gate carries over. Lecture reading pages and notebook text pages carry
``data-pagefind-meta="opens:YYYY-MM-DD"`` (build_lectures.py, build_notebook_text.py); results whose date is still ahead on the viewer's clock are dropped, and
``?all=1`` shows everything, as on every other page.

This page draws its own results with Pagefind's JS API rather than the stock Pagefind UI, so the
results look like the rest of the site and the date filter runs before anything is shown.

Run from repo root:  python3 build/build_search.py   (then the index: sh .githooks/build-search-index.sh)
"""
import os as _os
_os.chdir(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))  # repo root: paths below are repo-relative
import os
from site_theme import PAGE, SEARCH_ICON, site_header, site_footer, write_stylesheet, assert_accessible

OUT = "docs/search.html"

SEARCH_CSS = r"""
.search-box{position:relative;display:flex;align-items:center;max-width:44rem;margin:0 0 8px;}
.search-box svg{position:absolute;left:14px;color:var(--muted);pointer-events:none;}
.search-box input{width:100%;padding:12px 14px 12px 40px;font:17px/1.3 var(--sans);color:var(--ink);
  background:var(--surface);border:1px solid var(--rule);border-radius:4px;box-shadow:0 1px 3px rgba(0,0,0,.06);}
.search-box input:focus{outline:2px solid var(--green-mid);outline-offset:1px;}
.search-status{min-height:1.6em;margin:6px 0 4px;font:13px/1.5 var(--mono);color:var(--muted);letter-spacing:.02em;}
.results{list-style:none;padding:0;margin:0;max-width:50rem;}
.results>li{padding:16px 0 15px;border-bottom:1px solid var(--rule);}
.results .r-title{font:600 18px/1.3 var(--serif);color:var(--green);border:none;}
.results .r-title:hover{color:var(--clay);}
.results .r-path{display:block;margin-top:4px;font:12px/1.4 var(--mono);color:var(--faint);letter-spacing:.02em;}
.results p{margin:7px 0 0;font-size:14.5px;line-height:1.55;color:#3c4133;}
.results mark{background:var(--clay-bg);color:var(--clay-ink);padding:0 2px;border-radius:2px;}
.results .subs{list-style:none;padding:0;margin:10px 0 0 18px;}
.results .subs li{margin:8px 0 0;}
.results .subs a,.results .subs .sub-h{font:600 14px/1.3 var(--sans);}
.results .subs .sub-h{color:var(--green-mid);}
.results .subs p{margin-top:3px;font-size:13.5px;color:var(--muted);}
.search-more{margin:18px 0 0;font:600 12px/1 var(--mono);padding:9px 12px;border:1px solid var(--rule);
  border-radius:4px;background:var(--surface);color:var(--green);cursor:pointer;}
.search-more:hover{border-color:var(--green-mid);color:var(--clay);}
"""

# Pagefind's own module, loaded from beside this page so links work on GitHub Pages
# (/WRIT20833_2026/) and from the docs/ root in a local server alike.
SEARCH_JS = r"""<script>
(function () {
  var base = new URL('.', location.href).pathname;
  var showAll = /[?&]all(=|&|$)/.test(location.search);
  var d = new Date(), p = function (n) { return (n < 10 ? '0' : '') + n; };
  var today = d.getFullYear() + '-' + p(d.getMonth() + 1) + '-' + p(d.getDate());
  var form = document.getElementById('search-form'), input = document.getElementById('search-q');
  var status = document.getElementById('search-status'), list = document.getElementById('results');
  var more = document.getElementById('search-more');
  var STEP = 8, found = [], shown = 0, run = 0, timer = null, pagefind = null;

  function load() {
    if (!pagefind) pagefind = import(base + 'pagefind/pagefind.js').then(function (pf) {
      return Promise.resolve(pf.options({ baseUrl: base })).then(function () { return pf; });
    });
    return pagefind;
  }
  function esc(s) { var e = document.createElement('span'); e.textContent = s; return e.innerHTML; }
  function path(url) { return url.indexOf(base) === 0 ? url.slice(base.length) || 'index' : url; }
  function open(r) { return showAll || !r.meta || !r.meta.opens || r.meta.opens <= today; }

  function item(r) {
    // Pagefind's first sub-result is usually the page top; list only the ones under a heading.
    var subs = (r.sub_results || []).filter(function (s) { return s.url !== r.url && s.url.indexOf('#') > -1; }).slice(0, 3);
    // A notebook's text page is only there to be searched: send the reader to Colab, and name the
    // section as plain text, since Colab can't jump to a heading.
    var nb = r.meta.colab;
    var link = nb ? '<a class="r-title" href="' + esc(nb) + '" target="_blank" rel="noopener">'
                  : '<a class="r-title" href="' + r.url + '">';
    var where = nb ? (r.meta.kind || 'Notebook') + ' · opens in Colab ↗' : path(r.url).replace(/\.html$/, '');
    return '<li>' + link + esc(r.meta.title || path(r.url)) + '</a>' +
      '<span class="r-path">' + esc(where) + '</span>' +
      '<p>' + r.excerpt + '</p>' +
      (subs.length ? '<ul class="subs">' + subs.map(function (s) {
        var h = nb ? '<span class="sub-h">' + esc(s.title) + '</span>' : '<a href="' + s.url + '">' + esc(s.title) + '</a>';
        return '<li>' + h + '<p>' + s.excerpt + '</p></li>';
      }).join('') + '</ul>' : '') + '</li>';
  }
  function showMore() {
    list.insertAdjacentHTML('beforeend', found.slice(shown, shown + STEP).map(item).join(''));
    shown = Math.min(found.length, shown + STEP);
    more.hidden = shown >= found.length;
  }
  function remember(q) {
    var u = new URL(location.href);
    if (q) u.searchParams.set('q', q); else u.searchParams.delete('q');
    history.replaceState(null, '', u);
  }

  function search(q) {
    var mine = ++run;
    q = q.trim(); remember(q);
    if (!q) { list.innerHTML = ''; status.textContent = ''; more.hidden = true; return; }
    status.textContent = 'Searching…';
    load().then(function (pf) { return pf.search(q); }).then(function (res) {
      // The site is small, so load every hit's data and apply the release gate before showing any.
      return Promise.all(res.results.map(function (r) { return r.data(); }));
    }).then(function (data) {
      if (mine !== run) return;
      found = data.filter(open); shown = 0; list.innerHTML = '';
      status.textContent = found.length ? found.length + (found.length === 1 ? ' page' : ' pages') + ' mention “' + q + '”'
                                        : 'Nothing on the site matches “' + q + '”. Try a shorter or different word.';
      showMore();
    }).catch(function () {
      if (mine !== run) return;
      status.textContent = 'Search could not load. Open this page from the course site (not straight from a file).';
    });
  }

  form.addEventListener('submit', function (e) { e.preventDefault(); clearTimeout(timer); search(input.value); });
  input.addEventListener('input', function () { clearTimeout(timer); timer = setTimeout(function () { search(input.value); }, 250); });
  more.addEventListener('click', showMore);
  var q = new URLSearchParams(location.search).get('q');   // search.html?q=vader opens with that search run
  if (q) { input.value = q; search(q); } else { input.focus(); }
})();
</script>"""


def render():
    masthead = (
        '<header class="masthead">'
        '<div class="kicker">Search</div>'
        '<h1>Search the course site</h1>'
        '<p class="meta">Searches the home page, the schedule, every mini-lecture, the course guides, and the '
        'text of every code-along and homework notebook. A notebook result opens the notebook in Colab. '
        'Lectures and notebooks show up here once they open on the site.</p>'
        '</header>'
    )
    main = (
        masthead
        + '<form id="search-form" class="search-box" role="search" action="search.html" method="get">'
          '<label class="visually-hidden" for="search-q">Search the course site</label>'
          f'{SEARCH_ICON.replace("16", "18")}'
          '<input type="search" id="search-q" name="q" placeholder="Search lectures, notebooks, guides" autocomplete="off">'
          '</form>'
          '<div id="search-status" class="search-status" role="status" aria-live="polite"></div>'
          '<ul id="results" class="results"></ul>'
          '<button id="search-more" class="search-more" type="button" hidden>More results</button>'
          '<noscript><p class="muted">Search needs JavaScript. Every page is also reachable from the '
          '<a href="index.html">home page</a> and the <a href="schedule.html">schedule</a>.</p></noscript>'
        + SEARCH_JS
    )
    return PAGE("Search — WRIT 20833", main, extra_css=SEARCH_CSS,
                header=site_header(search=False),
                footer=site_footer("WRIT 20833 · When Coding Meets Culture · site search"),
                searchable=False)


if __name__ == "__main__":
    assert_accessible(SEARCH_CSS)
    css = write_stylesheet(os.path.dirname(OUT) or ".")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(render())
    print(f"wrote {OUT} ({os.path.getsize(OUT)} bytes) + {css}")
