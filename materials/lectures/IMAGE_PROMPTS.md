# Lecture image prompts — WRIT 20833 ("Reading Room" set)

Prompts for the **four lecture title images still missing** (AI Agency, Data Archaeology, Topic Modeling,
Going Public) plus the **two extra ML4/ML6 deck-slide images**. Generate them in the **same tool you used
for the existing paintings** (`messy_humanities`, the brass valves, `humanities_coding_script_to_structure`,
`ml1/3/5_title`) so the set stays consistent.

## How to use
1. Paste the **block below** into ChatGPT (or your image tool).
2. **Attach one existing image** (e.g. `materials/lectures/images/messy_humanities.jpg`) as a style
   reference and say "match this painting's look" — this is the single biggest lever for consistency.
3. Generate **one at a time**, in order; save each with the **exact `FILE` name** given.
4. Hand the files back and they get wired in: downsize → JPEG → `materials/lectures/images/` →
   uncomment the deck slots + add the dashboard tuples in `build_index.py` → rebuild → push.

## What each image fills
| File | Dashboard card | Deck slide |
|---|---|---|
| `ml4_title.jpg` | AI Agency (placeholder → thumbnail) | ML4 title slide (split) |
| `ml4_ventriloquism.jpg` | — | ML4 "Learning a language vs. ventriloquism" (split) |
| `ml6_title.jpg` | Data Archaeology (placeholder → thumbnail) | ML6 title slide (split) |
| `ml6_raw.jpg` | — | ML6 "'Raw data' is an oxymoron" (split) |
| `ml6_hear.jpg` | — | ML6 "Hear, don't extract" (split) |
| `ml7_title.jpg` | Topic Modeling (placeholder → thumbnail) | (future ML7 deck) |
| `ml9_title.jpg` | Going Public (placeholder → thumbnail) | (future ML9 deck) |

---

## ↓↓↓ Copy everything below into ChatGPT ↓↓↓

```
I need 7 illustrations for a humanities course website. They must all share ONE
consistent visual style. I'll give the shared style first, then the 7 scenes.
Please generate them ONE AT A TIME, in order, each as its own image, and label
each with the filename I give so I can keep them straight.

=== SHARED STYLE (apply to all 7) ===
Warm, painterly oil-painting illustration with an analog, hand-made feel. Muted
earth-tone palette ONLY — parchment cream, sepia, ochre, warm brown, deep muted
forest green, a touch of terracotta clay. Soft single-source warm light, like a
study lamp at dusk. No bright neon, no blue or cyan, no glossy 3D render, no UI
screenshots, no on-image text or labels. Calm, contemplative, a little literary.
Uncluttered composition with breathing room. SQUARE format (1:1, generate at
1024x1024 or larger). IMPORTANT: keep the main subject in the UPPER-CENTER of the
frame and leave the lower third less essential — the website also displays these
cropped to a short banner taken from the TOP, so nothing critical should sit at
the very bottom.
[Recommended: I've attached one of my existing paintings — match its look.]

=== THE 7 SCENES ===
1. FILE ml4_title.jpg — A person at a lamplit desk working the strings of a small
   wooden marionette that is typing at a tiny keyboard; the angle leaves it
   ambiguous who is moving whom. Scattered manuscripts.

2. FILE ml4_ventriloquism.jpg — A split composition: on one side a person speaking,
   their own voice rendered as flowing handwritten script leaving their mouth; on
   the other side the same person as a ventriloquist's dummy, mouth open, the words
   trailing in from offstage.

3. FILE ml6_title.jpg — An archaeologist's hand with a soft brush sweeping dust off
   a half-buried clay tablet whose surface is inscribed not with cuneiform but with
   faint rows of a spreadsheet — excavating data like an artifact.

4. FILE ml6_raw.jpg — A flowing river of human faces and voices narrowing as it
   pours through a wooden sieve; what drops out the bottom is a neat stack of
   identical paper cards, while most of the river spills off the sides, uncaptured.

5. FILE ml6_hear.jpg — Two hands cupped to an ear, leaning toward a small crowd of
   warmly glowing figures who are speaking, set against a faint, cold background of
   industrial mining and harvesting machinery — listening, not mining.

6. FILE ml7_title.jpg — A scholar at a long wooden table sorting one large scattered
   heap of handwritten letters into several distinct stacks, each stack bound with a
   different muted-color ribbon (clay, sage, ochre) — many documents resolving into
   a few themes. Warm lamplight.

7. FILE ml9_title.jpg — A person leaving a quiet lamplit study, a notebook of
   hand-drawn charts under one arm, stepping up to a modest public lectern in a warm
   town square as a small crowd gathers to listen — private analysis becoming public
   argument.
```

## ↑↑↑ Copy everything above into ChatGPT ↑↑↑

---

*Notes:* the existing `ml1/3/5_title` + `humanities_coding` images are ~4:5 portrait; on the dashboard
that's invisible (all cropped to 3:2 alike) and in the decks the slight portrait-vs-square difference reads
fine — not worth regenerating. Standardize on **square** for anything new. Scene 1–5 prompts also live as
`<!-- IMG PROMPT -->` comments inside `ml4.md` / `ml6.md`; this file is the consolidated, shareable copy.
