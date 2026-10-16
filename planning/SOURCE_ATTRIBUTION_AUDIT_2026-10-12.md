# Source and attribution audit — WRIT 20833

Reviewed October 12, 2026, against checkout `49ce7a8`. Review only: no teaching content changed, no publication or deployment performed.

## Result

**No confirmed invented book, scholarly article, or named author was found in the current student-facing reading lists.** Several real sources are misrepresented, incompletely cited, or surrounded by unsupported claims. The most consequential confirmed error is the description of the course corpus: **123 rows are derived from 93 distinct comment texts, not 123 independent comments or people.** There are also apparently constructed teaching datasets described as collected online material, and altered constitutional language presented without a paraphrase label.

“Verified” below means the particular attribution or publication was checked, not that every claim made anywhere in that publication is endorsed. “Unverified” does not mean fabricated. Priorities: **P1** affects the interpretation of the running dataset; **P2** warrants correction before students use the material; **P3** is narrower citation or attribution cleanup.

## Scope and method

- Inventoried the 136 tracked files: 36 Markdown documents, 16 notebooks, 15 Python files, 19 generated HTML pages, JavaScript and supporting files, and institutional Word/PDF/legacy Word references. Also checked the existing D2L HTML snippets.
- Extracted notebook cells, the Word syllabus and template text, and PDF text; searched the source, generated views, planning documents, and notebook builders for quotations, author names, titles, links, source claims, and corpus provenance. Findings distinguish scheduled student material from historical planning notes.
- Checked named readings against author, publisher, journal, project, scholarly edition, and institutional sources. Compared quotation wording where accessible. Used the public Fall-2025 repository to retrieve the actual source CSV, rather than treating the 2026 README as independent proof.
- Rebuilt all seven code-along builders and the four site generators in an isolated scratch checkout. **All succeeded, with no differences in the checked-in notebooks or site outputs.** Source defects therefore propagate into both lecture views; they are not generated-file drift.
- Parsed all 15 Python source files successfully; checked chatbot JavaScript syntax and ran the existing renderer tests: **9 passed**. Recomputed corpus counts and selected VADER examples. This is an attribution-focused codebase review, not a full security assessment or execution of every completed homework solution.

The companion [reference inventory](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/planning/SOURCE_REFERENCE_INVENTORY_2026-10-12.md) records explicit URL occurrences separately from the named-source ledger below.

## Findings

### F01 — P1 — The corpus is 123 line records, not 123 comments or people

**Locations:** [data README:9](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/notebooks/data/README.md:9), [ML1:25](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/materials/lectures/ml1.md:25), [ML5:233](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/materials/lectures/ml5.md:233), and the corpus descriptions throughout ML0/ML6/ML7/ML9 and HW2–HW4.

**Confirmed evidence:** the [original CSV](https://github.com/TCU-DCDA/WRIT20833_2025/blob/main/datasets/TenCommandmentsTX/20833_CBS1_youtube_F25.csv) has 143 records and **93 distinct nonempty `comments` values** after trimming. Splitting those values at line breaks, trimming, and deduplicating the resulting lines produces **exactly the 123 nonblank rows in the current text file, in the same order**. Of those rows, 82 match a complete original comment; the other 41 are fragments. The current file contains 132 physical lines and 2,235 whitespace-separated words, as documented.

The source CSV retrieved for this comparison has Git blob SHA `a540c0283d56101f1b173eb6eef5785901194099`. The source is real. The error is the unit of observation. A fragment can be scored and assigned a topic independently of the comment it came from, and a multiline commenter can receive multiple rows. The source CSV contains neither author identifiers nor posting dates, so it also cannot establish “123 people” or “one summer day” in ML5, or the summer chronology in ML6.

**Correction:** describe the existing material as **“123 nonblank text rows derived from 93 distinct comment texts, including multiline fragments; author count and posting dates are unknown.”** Preserve the exercises until they can be rewritten deliberately. If reconstructing 93 complete comments instead, revise the row-count, sentiment, topic, and empty-document exercises together. Do not silently replace the data. Add the original CSV link, video URL/title if recoverable, collection date if known, and the exact transformation recipe to the data README.

### F02 — P2 — The recurring 11-comment table has no documented real-world provenance

**Locations:** [Pandas 01 builder:71](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/notebooks/codeAlongs/_build_pandas01.py:71), [Pandas 01:190](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/notebooks/codeAlongs/_build_pandas01.py:190), [Pandas 02:145](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/notebooks/codeAlongs/_build_pandas02.py:145), [VADER builder:116](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/notebooks/codeAlongs/_build_vader.py:116), and their generated notebooks, including the complete Pandas 01 version.

Pandas 01 calls the table “real-shaped,” but subsequent lessons call its entries real comments or the Texas comments without maintaining that distinction. None of its 11 comment strings matches a complete comment in the documented original CSV. There is no source for the exact likes, replies, or stance labels. The table appears to be a constructed teaching example; the repository does not establish otherwise.

**Correction:** explicitly label all three lessons **“constructed examples; comment wording, stance labels, and engagement counts are illustrative.”** If they were collected from a different source, document that source and transformations instead. Students should not mistake the resulting camp averages for evidence about the actual public debate.

### F03 — P2 — The topic-modeling toy corpus is described as collected internet comments

**Locations:** [topic-modeling builder:110](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/notebooks/codeAlongs/_build_topicmodeling.py:110), [ML7:242](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/materials/lectures/ml7.md:242), and the generated topic-modeling notebook/reading page.

The builder says the fifteen comments were pulled from three corners of the internet; the lecture names sports, music, and food forums. The strings are an inline, highly repetitive toy corpus with no forum names, URLs, collection record, or attribution. The lecture itself calls it a toy corpus, but still asserts actual collection.

**Correction:** call these **“fifteen constructed sentences with deliberately distinct vocabularies.”** If real provenance exists, supply it. The pedagogical contrast works without attributing invented or undocumented speech to real forum users.

### F04 — P2 — A constitutional “passage” is an altered composite

**Location:** [term-frequency builder:171](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/notebooks/codeAlongs/_build_termfreq.py:171), generated Term Frequency notebook, Part 4, `official_text`.

The prose introduces a passage from a founding legal document, but its five sentences are shortened/reworded composites drawn from the Constitution and later amendments. The opening changes the First Amendment's verb from “make” to “pass”; the Article I sentence omits the limiting words “herein granted”; other lines abbreviate the Tenth and Fourteenth Amendments. This is not a verbatim passage, and it is not the same 1787-only text assigned in HW2. Compare [Gutenberg's constitutional text](https://www.gutenberg.org/cache/epub/5/pg5-images.html).

**Correction:** label it **“a constructed paraphrase of constitutional language, including later amendments”**, or replace it with a short verbatim excerpt identified by article/amendment. Keep the constructed comment corpus in this notebook clearly labeled too; its current “real-sounding” introduction is more honest than the later data examples.

### F05 — P2 — A modern course definition is attributed to “the Greeks”

**Locations:** [ML4:212](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/materials/lectures/ml4.md:212), [ML4:258](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/materials/lectures/ml4.md:258), [ML9:192](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/materials/lectures/ml9.md:192), and [framework:193](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/planning/CONCEPTUAL_FRAMEWORK_2026.md:193).

*Amathia* is a real Greek word. The problem is the categorical claim that it is **not ignorance** but the condition of a well-informed person whom nothing teaches, contrasted with *agnoia* as merely missing information. [LSJ](https://atlas.perseus.tufts.edu/dictionaries/entry/urn:cite2:scaife-viewer:dictionaries.v1:lsj-n4860/) gives ignorance, stupidity, and related senses. [Plato's *Sophist*](https://classics.mit.edu/Plato/sophist.html), 229b–230d, supports a distinction involving mistakenly thinking one knows and the role of refutation; it does not supply the lecture's AI-era definition as a universal Greek distinction.

The physician/rhetorician example is genuinely in [*Gorgias*](https://classics.mit.edu/Plato/gorgias.html), 456b–459c. However, “Plato watched” converts a literary dialogue into an undocumented eyewitness report, and the connection from that scene to the course's definition needs its own explanation.

**Correction:** write **“We borrow a Platonic warning about thinking we know, and use ‘un-wisdom’ here as a course metaphor.”** Cite *Sophist* for the ignorance distinction, and introduce the physician scene as **“In Plato's dialogue, Gorgias claims…”** Preserve the useful reflexive framing without pretending the modern definition is an ancient lexical fact.

### F06 — P2 — Kant is made to define private lived experience as a noumenon

**Locations:** [ML0:233](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/materials/lectures/ml0.md:233), [Day-1 framing:27](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/materials/Day1_Framing_Noumena_to_Wisdom.md:27), and the pipeline explanation in the framework/image README.

The thing-in-itself gloss has a Kantian basis, but the course equates noumena with the whole lived human fact and a woman's complete private feeling, then equates phenomena with public expression. That is the course's analogy, not Kant's definition. Kant's distinction concerns objects considered apart from sensible intuition; private experience is not automatically noumenal merely because an observer cannot access it. See [*Critique of Pure Reason*, phenomenon/noumenon discussion](https://www.gutenberg.org/files/4280/4280-h/4280-h.htm), especially B306–311.

**Correction:** identify the diagram as **“a course model loosely inspired by Kant, not a literal account of his philosophy.”** Use “lived experience → expression → collection” for the practical stages, or provide a more careful philosophical explanation. Do not attribute the entire eight-stage model to Kant or to a canonical DIKW formulation.

### F07 — P2 — Open Syllabus does not establish a worldwide author-ranking claim

**Location:** [ML0:140](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/materials/lectures/ml0.md:140) and [ML0:150](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/materials/lectures/ml0.md:150), both generated views.

The project is real, but the claim that Plato is assigned more than any author on earth has no identified query, dataset version, or author aggregation. The project's [own methodological description](https://blog.opensyllabus.org/about-os) limits its collection to English-language syllabi, acknowledges uncertain representativeness, and distinguishes title rankings from imperfect author identities. Those limitations alone rule out the worldwide assertion. A frequently assigned *Republic* is not equivalent to the most assigned author worldwide.

**Correction:** say **“maps citations across millions of collected syllabi, showing which texts are commonly assigned.”** Retain a Plato comparison only with a dated, reproducible query and its actual population.

### F08 — P2 — The Facebook example attributes undocumented technical motives

**Location:** [ML3:170](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/materials/lectures/ml3.md:170) and [ML3:199](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/materials/lectures/ml3.md:199).

The 2014 addition of custom gender options is supported. But the lecture asserts that the earlier binary was not anyone's belief about gender and existed because it was cheap to store and easy to sort. No evidence supports that claim about intent or actual storage. [*Data Feminism*, chapter 4](https://data-feminism.mitpress.mit.edu/pub/h1w0nbqp/release/3), discusses Rena Bivens's finding that advertising classifications continued to collapse gender to a binary **after** custom options were added. It supports an advertiser-convenience explanation, not the stronger hardware-efficiency story or denial of ideological motives.

**Correction:** describe the documented distinction between user-facing choices and backend advertising categories. Credit Bivens via D'Ignazio and Klein. Mark the single-bit comparison as an analogy, not a claim about Facebook's schema.

### F09 — P2 — Shrout's real quotation has unmarked alterations and no source locator

**Location:** [ML5:186](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/materials/lectures/ml5.md:186) and [ML5:214](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/materials/lectures/ml5.md:214).

**The quotation is not fabricated.** It comes from Anelise Hanson Shrout's [(Re)Humanizing Data: Digitally Navigating the Bellevue Almshouse](https://crdh.rrchnm.org/essays/v01-10-re-humanizing-data/), *Current Research in Digital History* 1 (2018), DOI `10.31835/crdh.2018.10`, paragraph 5. The course replaces the original subject, nineteenth-century immigration data, with “This data” and silently changes “who” to “whom.” The latter smooths the original grammar but is still an editorial intervention in a block quotation. [Walsh's lesson](https://melaniewalsh.github.io/Intro-Cultural-Analytics/02-Python/10-Lists-Loops-Part2.html) also quotes and links the essay; the current lecture supplies only the author's name.

**Correction:** restore the wording or explicitly mark substitutions, add the essay title/link and paragraph number, and acknowledge Walsh if her lesson was the route through which this material was adopted. The planning ledger's description of the quote as “verbatim” should also be corrected.

### F10 — P2 — The stylometry exemplar is not independently verified authorship evidence

**Locations:** [stylometry handout:26](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/materials/stylometry/Reading_for_the_Seams.md:26), the stylometry notebook cells 2–3, and `materials/stylometry/ai_voice_claude_analysis.pdf`.

The PDF labels portions of an email likely Claude-written or human-edited, but contains no original generation transcript, prompt, model/version, revision history, or scholarly citation supporting those segment attributions. The planning outline identifies it as ChatGPT's analysis of a Claude-derived email; that origin is not documented in the PDF itself. It is an interpretive example, not independently established ground truth about which words came from whom.

The notebook additionally says its `hybrid` text is the email from the PDF, but silently omits both a clause about student voice and the final permission-giving sentence. That last omission directly changes the hedging feature being measured. Its `human` and `ai` samples are constructed style examples, not a documented paired human/model production record. The claim that its function-word list is the same list discarded in the term-frequency unit is also false; the lists differ.

**Correction:** identify the PDF as AI-generated interpretive commentary, document the known provenance, and separate interpretation from verified authorship. Label the notebook passage an **adapted excerpt**, identify the omissions, and explain their effect, or use the identical passage. The general warning about biased detectors has real research support: [Liang et al., 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10382961/); cite it and limit the claim to the detectors and populations studied.

### F11 — P2 — Chiang's analogy is extended into an unsupported literal claim

**Location:** [ML4:165](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/materials/lectures/ml4.md:165).

The attribution of the blurry-JPEG analogy is correct: Ted Chiang's [2023 essay](https://www.newyorker.com/tech/annals-of-technology/chatgpt-is-a-blurry-jpeg-of-the-web). The attached gloss, “a lossy average of everything ever written,” is not a literal model description supported by that essay. Training does not encompass all writing; compression and averaging are analogies here.

**Correction:** retain Chiang's named analogy and distinguish it from the course's argument about voice. Remove “everything ever written.”

### F12 — P3 — The country-music chart's alt text changes the plotted unit

**Location:** [ML0:131](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/materials/lectures/ml0.md:131).

The borrowed chart and source are real. The alt text describes mentions across songs, but [John W. Miller's explanation](https://www.johnwmillr.com/trucks-and-beer/) says each dot represents an **artist**, with percentages calculated over that artist's songs.

**Correction:** say **“Each dot is an artist; axes show the percentage of their songs containing ‘girl’ and ‘love’; color represents the artist's gender.”** Add the creator's name alongside the project title.

### F13 — P3 — Colbert coined the modern sense, not the previously nonexistent word

**Location:** [ML4:184](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/materials/lectures/ml4.md:184) and [ML4:247](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/materials/lectures/ml4.md:247).

The modern political meaning is correctly associated with Stephen Colbert in 2005, but the word itself had earlier recorded uses. See [Dictionary.com's etymology](https://www.dictionary.com/browse/truthiness) and [Benjamin Zimmer's examination of the earlier usage](https://itre.cis.upenn.edu/~myl/languagelog/archives/002764.html).

**Correction:** write **“Colbert popularized this sense of ‘truthiness’.”** This is a small historical qualification, not a fictitious reference.

### F14 — P3 — The planning framework treats a disputed painting attribution as settled

**Location:** [conceptual framework:181](/Users/crode/Code/curtrode/01-Teaching/4-WRIT/WRIT20833/WRIT20833_2026/planning/CONCEPTUAL_FRAMEWORK_2026.md:181).

Auden's poem and its 1938 date are genuine; its wording was checked against the [authorized Poetry Foundation text](https://www.poetryfoundation.org/poems/159364/musee-des-beaux-arts-63a1efde036cd). However, the framework repeatedly attributes the surviving *Landscape with the Fall of Icarus* directly to Bruegel. The owning museum's [account](https://fine-arts-museum.be/uploads/releases/files/bruegel_unseen_masterpieces_booklet.pdf) explicitly says technical tests have not confirmed that attribution.

**Correction:** use **“the painting traditionally attributed to Bruegel”** or distinguish the composition's traditional attribution from the authorship of the surviving work. This is currently a planning-document issue; do not mistake it for a confirmed false quotation in a scheduled lecture.

## Additional prose and citation issues

These are worth addressing, but are not evidence of invented authors or publications:

- **Constitution and faith:** the data README says its only mention of faith is the religious-test clause. The supplied text also contains the Sunday exception and the dating formula referring to the Lord. Narrow the claim to the absence of the exact word `religion`, rather than absence of religious language. The documented Gutenberg source and exclusion of amendments are valid.
- **VADER:** the no-lexicon explanation is correct for the four zero-scoring examples checked, but the general maxim that zero means no evidence is too broad: sentiment contributions can cancel. Likewise, the Pandas 02 preview incorrectly suggests sentiment scoring replaces support/oppose labels, contradicting the later tone/stance lesson. [VADER documentation](https://github.com/cjhutto/vaderSentiment) describes positive/negative/neutral sentiment, not political stance; it also uses inclusive `>= 0.05`/`<= -0.05` thresholds, while ML3 describes the strict positive threshold used in the homework. Explain the course's choice rather than implying a universal standard.
- **Digital memory and loops:** ML5's claims that all digital memory is total/permanent and loops cannot handle exceptions are absolutes, not sourced technical facts. A loop can contain case-specific conditions; records can be deleted or lost. Frame these as risks of particular policies/designs, consistent with the course's emphasis on authored choices.
- **Mapping Police Violence:** the project is real, but ML9 attributes a specific scraping/DataFrame/chart workflow without documenting its implementation. Its [methodology](https://mappingpoliceviolence.org/methodology) describes multiple sources, research, verification, and changing practices. Present the course techniques as an analogy to the project's analytical goals, and credit the source-gathering and verification labor.
- **Eight versus eight thousand readers:** the ML9 blockquote is unattributed course rhetoric, not an identified outside quotation or readership measurement. Label it a hypothetical illustration or set it as ordinary prose.
- **Instant Data Scraper:** the builder's Chrome/Firefox claim is not supported by the [official product listing](https://chromewebstore.google.com/detail/instant-data-scraper/ofaokhiedipichpaobibbnahnkdoiiah) or [former developer's site](https://webrobots.io/), which identify Chrome/Edge. The product supports automated pagination and scrolling, so “it won't flood a server” is not a built-in guarantee; pacing is a user responsibility.
- **Uncited historical psychology:** ML4's claim that polished prose reliably signaled actual thought throughout human history is presented as an established mechanism without a source. Treat it as a proposed explanation or remove the universal scope.
- **Optional readings:** most entries omit dates, editions, locators, and clickable links. Adding a compact bibliography would make verification possible for students. In particular, name the second edition for Montfort's page references and add the Shrout essay itself to ML5.
- **Brennan:** “Public, First” is correctly named and attributed. As further reading, explain that it centers communities in project design; availability or dissemination alone is not its definition of public humanities.

## Named-source ledger

Locations name canonical source files; generated lecture HTML inherits the same entries. Shortened book titles and omitted middle names are not, by themselves, false attribution. Existence checks for optional books do not amount to reading every chapter.

| Source or attributed figure | Where used | Verification and disposition |
|---|---|---|
| John Keats, negative capability | ML0 | Genuine wording; scholarly letter transcription at [University of Victoria](https://johnkeats.uvic.ca/1817-12-27.html). Add the December 1817 letter to George and Tom as the locator. |
| Immanuel Kant, noumena/phenomena | ML0, Day-1 framing, framework, image README | Real concepts; [primary text](https://www.gutenberg.org/files/4280/4280-h/4280-h.htm). Course application requires qualification: F06. |
| Douglas Rushkoff, *Program or Be Programmed* | ML0, ML4 | Real book; [publisher](https://orbooks.com/catalog/program-or-be-programmed/). ML0 passage independently confirmed in Montfort, 2nd ed., printed pp. 327–328, citing Rushkoff 2010, p. 19. Minor unmarked grammar normalization: `knows` becomes `know`. |
| Nick Montfort, *Exploratory Programming for the Arts and Humanities* | ML0, ML4 | [Author's edition page](https://nickm.com/books/exploratory_programming_2e/) and [open book](https://archive.org/download/montfort-exploratory-programming-2e/9780262363105.pdf). Both the Rushkoff page reference and three benefits of programming are confirmed. Specify second edition (2021); benefits appear on printed p. 321. |
| John W. Miller, “Trucks and Beer” | ML0 | [Original project](https://www.johnwmillr.com/trucks-and-beer/), 2018. Genuine; chart unit needs correction: F12. |
| Matt Daniels / The Pudding, “The Largest Vocabulary in Hip Hop” | ML0 | [Original project](https://pudding.cool/2017/02/vocabulary/). Genuine; main comparison uses 35,000 lyric words and the Wu-Tang subcomparison uses 3,500. Explain that these are word-token counts, not numbers of songs. |
| Every Noise at Once | ML0 | Named project and link found; direct fetch repeatedly timed out. The precise current count and description were not independently verified from the project in this run. **Unresolved, not fabricated.** |
| Open Syllabus | ML0 | [Project methodology](https://blog.opensyllabus.org/about-os). Genuine; worldwide Plato claim unsupported: F07. |
| Safiya Umoja Noble, *Algorithms of Oppression* | ML3 | [NYU Press](https://nyupress.org/9781479866762/algorithms-of-oppression/), 2018. Correct author/title; fuller subtitle is *How Search Engines Reinforce Racism*. |
| Ruha Benjamin, *Race After Technology* | ML3 | [Author's page](https://www.ruhabenjamin.com/race-after-technology), Polity, 2019. Correct; subtitle *Abolitionist Tools for the New Jim Code*. |
| Cathy O'Neil, *Weapons of Math Destruction* | ML3 | [Publisher](https://www.penguinrandomhouse.com/books/241363/weapons-of-math-destruction-by-cathy-oneil/9780553418835/), 2016 original publication. Correct. |
| Catherine D'Ignazio and Lauren F. Klein, *Data Feminism* | ML3, ML6, ML7, ML9, source notes | [MIT Press](https://mitpress.mit.edu/9780262044004/data-feminism/), 2020. Correct authors/title. Facebook gloss requires correction: F08. |
| Rena Bivens, Facebook gender research | Implicit in ML3's Data Feminism example | Explicitly credited in [chapter 4](https://data-feminism.mitpress.mit.edu/pub/h1w0nbqp/release/3), but not named in the lecture. Add her attribution when discussing that specific research. |
| Ted Chiang, “ChatGPT Is a Blurry JPEG of the Web” | ML4 | [Original essay](https://www.newyorker.com/tech/annals-of-technology/chatgpt-is-a-blurry-jpeg-of-the-web), 2023. Correct author/title/analogy; overextended gloss: F11. |
| Stephen Colbert, truthiness | ML4, framework | Modern sense correctly associated with 2005; historical word-coining requires qualification: F13. |
| Harry G. Frankfurt, *On Bullshit* | ML4, framework | Confirmed in [publisher's catalog](https://assets.press.princeton.edu/catalogs/lit09.pdf), 2005, and the Hicks et al. paper. The indifference-to-truth distinction is correctly attributed. |
| Michael Townsen Hicks, James Humphries, Joe Slater, “ChatGPT is bullshit” | ML4, framework | [Journal article](https://link.springer.com/article/10.1007/s10676-024-09775-5), 2024, *Ethics and Information Technology* 26, article 38. Correct authors/title/date. Current lecture correctly presents it as their argument, rather than consensus. |
| Plato, *Gorgias* | ML4 | [Primary dialogue](https://classics.mit.edu/Plato/gorgias.html). Physician/rhetorician example confirmed; mark the scene as a dialogue and separate it from the amathia definition: F05. |
| Greek *amathia* and *agnoia* | ML4, ML9, framework | Real terms; lexical and philosophical overclaim: F05. |
| Anelise Hanson Shrout, Bellevue quotation and dataset | ML5, source notes | [Original essay](https://crdh.rrchnm.org/essays/v01-10-re-humanizing-data/), 2018. Genuine; missing source and unmarked editorial changes: F09. |
| Paul Connerton, *How Societies Remember* | ML5 | [Cambridge University Press](https://www.cambridge.org/core/books/how-societies-remember/6CC86C87803676EB0559C10E0E228CC4). Genuine, 1989. |
| Viktor Mayer-Schönberger, *Delete: The Virtue of Forgetting in the Digital Age* | ML5 | [Author's Oxford institutional publication record](https://www.oii.ox.ac.uk/research/publications/delete/), 2009. Genuine. |
| José van Dijck, *Mediated Memories in the Digital Age* | ML5 | [Author's institutional record](https://research-portal.uu.nl/en/publications/mediated-memories-in-the-digital-age/), Stanford University Press, 2007. Genuine. |
| Lisa Gitelman, ed., *“Raw Data” Is an Oxymoron* | ML6 | [MIT Press](https://mitpress.mit.edu/9780262518284/raw-data-is-an-oxymoron/), 2013. Correct title and editor role. |
| Johanna Drucker, “Humanities Approaches to Graphical Display” | ML6 | [DHQ article](https://digitalhumanities.org/dhq/vol/5/1/000091/000091.html), 2011, 5(1). Genuine; capta gloss is supported. |
| David M. Blei, “Topic Modeling and Digital Humanities” | ML7 | [Original journal essay](https://journalofdigitalhumanities.org/2-1/topic-modeling-and-digital-humanities-by-david-m-blei/), JDH 2(1), Winter 2012. Genuine. |
| Ted Underwood, “Topic modeling made just simple enough” | ML7 | [Author's post](https://tedunderwood.com/2012/04/07/topic-modeling-made-just-simple-enough/), April 7, 2012. Genuine. |
| Benjamin Schmidt, “Words Alone: Dismantling Topic Models in the Humanities” | ML7 | [Author's publication record](https://benschmidt.org/publication/schmidt_words_2013/), April 2013, JDH 2(1), Winter 2012 issue. Genuine; publication year and issue label differ without implying fabrication. |
| Sheila A. Brennan, “Public, First” | ML9 | [Original chapter](https://dhdebates.gc.cuny.edu/read/untitled/section/11b9805a-a8e0-42e3-9a1c-fad46e4b78e5), *Debates in the Digital Humanities 2016*, ch. 32. Genuine. |
| Mapping Police Violence | ML9 | [Project methodology](https://mappingpoliceviolence.org/methodology). Genuine; exact implementation analogy is unsupported, as noted above. |
| Melanie Walsh, *Introduction to Cultural Analytics & Python* | README, syllabus, acknowledgments, site resources | [Book](https://melaniewalsh.github.io/Intro-Cultural-Analytics/) and [Bellevue lesson](https://melaniewalsh.github.io/Intro-Cultural-Analytics/02-Python/10-Lists-Loops-Part2.html). Genuine and correctly acknowledged; shortened title elsewhere is identifiable. |
| U.S. Constitution, Gutenberg eBook #5 | data README, HW2, term-frequency lesson | [Gutenberg edition](https://www.gutenberg.org/cache/epub/5/pg5-images.html). Genuine. Local file covers original articles and signatures, 4,541 whitespace words. Separate the constructed composite: F04. |
| CBS1 YouTube export / Fall-2025 corpus | data README, lectures, HW2–HW4 | [Original source file](https://github.com/TCU-DCDA/WRIT20833_2025/blob/main/datasets/TenCommandmentsTX/20833_CBS1_youtube_F25.csv). Exact derivation verified; unit-of-observation error: F01. Video identity/date remain undocumented. |
| AI voice analysis PDF / hybrid email | stylometry handout, notebook, outline | Existing local artifact, but model/human segment provenance not independently established: F10. |
| W. H. Auden, “Musée des Beaux Arts” | framework, historical planning | [Authorized poem](https://www.poetryfoundation.org/poems/159364/musee-des-beaux-arts-63a1efde036cd), December 1938. Genuine attribution/date/quoted wording. |
| Bruegel, *Landscape with the Fall of Icarus* | framework | Real work; surviving painting's attribution disputed by owning museum: F14. |
| Federalist Papers / Galbraith–Rowling stylometry examples | stylometry outline and next steps only | Real historical cases. [Mosteller and Wallace publisher record](https://press.uchicago.edu/ucp/books/book/distributed/I/bo5667096.html) confirms the Federalist study; [Oxford institutional account](https://www.hertford.ox.ac.uk/wp-content/uploads/2018/05/Hertford-College-news_i27_ws.pdf) discusses Rowling/Galbraith. No specific student reading is assigned yet. |
| Franco Moretti / distant reading | historical lecture source notes only | Name attached to the methodology, without a particular title, quotation, or required reading. No distinct source is available to audit there. |
| Ben Schmidt's teacher-reviews project; Photogrammar | historical lecture source notes only | Removed/unused examples, not current student assignments. Their historic links/attributions were not fully revalidated; do not count them as verified current references. |
| TCU Core outcomes, syllabus template/checklist | syllabus, reference files, compliance planning | Quoted CSV/HUM wording agrees with the supplied institutional outcomes PDF. Grade-scale figures agree with the supplied checklist and [official TCU checklist](https://ugradcouncil.tcu.edu/wp-content/uploads/NEW-UNDERGRADUATE-AND-GRADUATE-COURSE-PROPOSAL-CHECKLIST-Final-4.24.24-3.pdf). This verifies the quoted source, not the course's current approval status. |
| Python, pandas, VADER, Gensim | site resources and notebooks | Genuine [Python](https://docs.python.org/3/), [pandas](https://pandas.pydata.org/docs/), [VADER](https://github.com/cjhutto/vaderSentiment), [Gensim](https://radimrehurek.com/gensim/models/ldamodel.html) documentation. Add Hutto and Gilbert (2014) if treating VADER as a research method; the project requests that citation. |
| Instant Data Scraper | Pandas 01 | [Official store listing](https://chromewebstore.google.com/detail/instant-data-scraper/ofaokhiedipichpaobibbnahnkdoiiah). Genuine product; browser and pacing claims need correction. |

## What remains unverified

The current repository cannot establish the original video's identity, actual posting dates, distinct commenter count, or the email's human/model revision history. The instructor may be able to recover these from original collection and generation records. Every Noise timed out during direct verification. Institutional reference files establish what those documents say, but not current registrar approvals or live policy state. The Code Guide's private Worker, provider configuration, server logging, and retention behavior are outside this checkout; its student-facing privacy claims cannot be independently confirmed from the frontend alone. No live tutor conversation was submitted.

The review does not infer that missing provenance means a source was fabricated. It identifies what evidence is missing and supplies a correction that avoids claiming more than that evidence supports.

## Recommended correction order

1. Correct the corpus unit and undocumented participant/date claims everywhere, retaining the current file unless the exercises are deliberately redesigned.
2. Label constructed corpora, engagement counts, constitutional paraphrases, and adapted stylometry excerpts.
3. Repair the Greek/Kant/Open Syllabus/Facebook attributions and restore/cite the Shrout quotation accurately.
4. Add the linked bibliography, qualify narrower prose claims, rebuild generated notebooks/pages, and update the Word syllabus only where its content changes.

HW2–HW4 builders belong to the private keys repository, per `CLAUDE.md`; correcting their generated prose requires editing those builders there and copying back only regenerated student notebooks. No private files were accessed or changed in this audit.
