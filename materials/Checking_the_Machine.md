# Checking the Machine — a one-page validation routine

VADER, LDA, and the stylometry measures all hand you a confident-looking number whether or not
it means anything. This page is the routine for finding out. It is the same routine every time:
in **HW3** (sentiment), **HW4** (topics), and your **capstone**. It turns "check your result by
hand" into steps you can repeat, and it ends in a decision about your claim.

It takes about 20 minutes. It is not an extra assignment. Use it wherever a homework or the
capstone already asks you to check, read the extremes, or name a limit, and paste your table there.

---

## 1. Write the claim first

One sentence, before you check anything. Name the number it rests on.

> *"This crowd leans warm: 51 of the 123 rows score positive."*

Then write down, in a sentence each, what your **categories** mean in plain words. What counts as
"negative" tone? What counts as "support"? What is topic 2 *about*? If you can't say it yet,
that's your first finding.

## 2. Pick a sample: not just the exciting cases

| Pick | How many | Why |
|---|---|---|
| The **extremes** (highest and lowest score, or the strongest documents in a topic) | 3 + 3 | Where the tool is most confident |
| **Ordinary** cases, chosen at random | 3 | Where most of your data actually lives |
| **Odd** cases: a score of exactly 0, a very short text, a `-1` topic, anything surprising | 2 | Where the tool is most likely to be wrong |

```python
# plumbing: one way to pull the sample (sentiment version; swap in your own column names)
sample = pd.concat([df.nlargest(3, "sentiment"), df.nsmallest(3, "sentiment"),
                    df.sample(3, random_state=1), df[df["sentiment"] == 0].head(2)])
for row_number, row in sample.iterrows():
    print(f"[{row_number}]  {row[text_column]}")    # print the TEXT only, not the score
```

## 3. Judge first, then look

Read each text and write **your** label *before* you look at the tool's. (Printing only the text,
as above, keeps you honest.) Then fill in the table:

| Row | Your judgment | The tool's | Agree? | If not, why? |
|---|---|---|---|---|
| | | | | |

The last column is the valuable one. Common answers: sarcasm, negation ("not bad"), a word the
lexicon doesn't know, two opinions in one text, a fragment cut off from its context, a topic that
is really just one repeated phrase.

## 4. Look at what the summary number hides

- **Count behind every average.** A topic's mean sentiment from 4 rows is not the same evidence as
  one from 40. Report the count next to the mean.
- **Spread, not just the middle.** An average near 0 can be a calm crowd *or* a split one. Look at
  the bar chart or the extremes before you call it "neutral."
- **Which kind of zero?** A VADER compound of 0 can mean *no lexicon words found* (`neu` = 1.0) or
  *positive and negative cancelled out* (`pos` = `neg`). Those are different findings.
- **Mixed documents (topics).** If a document's strongest topic has a probability below about 0.5,
  it is genuinely mixed. Don't count it as clean evidence for one topic.
- **Rows vs. people.** The course corpus stores 93 comments as 123 rows, so a long comment can count
  more than once. Say "rows" when you mean rows.

## 5. Decide what your claim can bear

Choose one, and say why in a sentence:

- **Keep it.** Your sample mostly agreed, and the counts are big enough to matter.
- **Narrow it.** True for part of the data, or true only with a qualifier ("by VADER's lexicon...",
  "among the longer comments..."). Rewrite the sentence.
- **Decline it.** Too many disagreements, too few cases, or a category you couldn't define. Saying
  "this method can't answer that here" is a real result, not a failure.

A rough guide: if 3 or more of your ~11 sampled cases disagree with the tool for reasons that would
change your claim, narrow it or decline it.

## 6. Write the limit sentence

One sentence for your write-up: *what did this method flatten, who chose it, and how far can you
trust it here?* This is your "one honest limit." The work above is the evidence for it.

---

*Track B (stylometry):* the same steps work. Your "judgment" is your Day 9 attribution map; the
"tool" is the measures. Compare passages of similar length and genre, or say clearly that you
couldn't.
