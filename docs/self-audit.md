# Self-audit

A record of what was reviewed before release, what was found, and what remains open. Written so a third-party reviewer can check the claims rather than take them on faith.

## Process

Three review passes so far:

1. **Spec review** — can this be loaded as a skill, and is it internally executable? Dimensions: discovery layout, frontmatter contract, reference resolution, rule conflicts, output format determinism, repository conventions.
2. **Alignment review** — does it actually do what it claims? Compared line by line against the philosophical research (`references/design-notes.md` sources) and against the mechanisms used by comparable open-source skills.
3. **External review** — a third party cloned the repository, ran the validator in a renamed directory, read `SKILL.md`, `design-notes`, `self-audit` and `RESULTS`, and reported three defects the first two passes missed.

Passes 1–2 were text-only: no behavioural run was performed in that round. That gap is what `test/RESULTS.md` closes. Pass 3 was the first review by someone who did not build the project.

## What the spec review found

Installation was clean — the skill loads, the catalogue entry renders, the directory layout is the one-deep bundle the host expects, and the reference paths are relative and resolvable. No blocking issue there.

The blocking findings were internal:

| Finding | Status |
|---|---|
| `LICENSE` still carried a placeholder holder | fixed |
| "never pronounce a verdict" contradicted "give a judgement" in the closing, and the self-check flagged the compliant behaviour as an error | fixed: closings must be falsifiable hypotheses ending in a confirmation question |
| Closing trigger conditions were mutually exclusive and undecidable ("round 5", "no new information" undefined); the same stall signal was read as two different actions | fixed: rounds and "no new information" defined; order fixed to drop-level-then-close; user's explicit stop outranks the round floor |
| Examples violated the skill's own one-question rule in four places; one example's revision was written by the coach | fixed: examples rewritten; the revision is handed back to the user |
| "Drop a level" referenced a level table living in a reference file that only loaded for decision questions | fixed: a one-line level definition moved into the main file |
| Output format covered only ordinary turns; "lines" is not measurable | fixed: three turn templates with word limits |
| Chinese-only body shipped with an English README | fixed: `SKILL.en.md` added, plus a follow-the-user's-language rule |

## What the alignment review found

Coverage against the philosophical source material was uneven: the elenchus rule, the aporia-as-outcome rule and the consent rules were implemented; the stopping criteria, question typology and self-scrutiny of the examiner were only partly implemented.

The sharpest criticism was that the skill **claimed** things its own examples did not show:

- an example labelled "aporia closing" did not contain an aporia (the user never said they did not know);
- an example labelled as demonstrating elenchus actually demonstrated decision coaching;
- the design notes cited a page number for a source the research itself marked as unverified — the project broke its own citation rule.

All three were fixed: `examples/04-aporia.md` now demonstrates a real aporia, the decision example states which steps it skips and why, and the page number is marked unverified in `references/design-notes.md`.

## What the external review found

Three defects, two of them found by running the repository rather than reading it:

| Finding | Status |
|---|---|
| **Rule 4 contradicted the output format.** Rule 4 requires quoting the user's words; the format required "restate the target (one sentence)" inside a word limit. When the user's message has several clauses, "one sentence" and "the original words" cannot both hold, so the model merges them — and merging generates its own wording. The two paraphrase drifts recorded in `RESULTS` were consequences of the spec, not model carelessness. | fixed: the format now says "quote their words; multiple clauses allowed; the quote is not counted against the limit", and rule 4 is stated as a hard constraint |
| **Nothing defended against manufactured consent.** Rule 2 guarantees a premise has a source, not that the user really agrees. A chain of one-sided prompts ("Would you say that …?") reliably produces nods, and step 3 then builds its contradiction on scenery the examiner erected. | fixed: a section "Consent has to be real" — load-bearing premises are put in both directions, or the user is asked "in what situation would you disagree?"; a premise obtained by a nod does not count in step 3 |
| **Natural closing was structurally untestable.** Scenarios ran three rounds; the closing rule required five rounds plus two empty rounds, and — in the old wording — another two after a level drop. A three-round script could never reach it. | fixed: the closing gate is now "drop a level at two empty rounds, close one empty round later"; scenario S6 (five turns) covers it, run twice |

A fourth issue was a portability bug, not a design one: `scripts/validate.py` required the skill name to equal the checkout directory name, so a downloaded ZIP (`socratic-elenchus-main`) scored 58/59 while CI passed. The check now only runs inside a git checkout and reports why it was skipped elsewhere.

## What remains open

- **Behavioural evidence is still thin.** Six scripted scenarios, 21 turns, judged by a rubric. This tests rule execution, not long-dialogue stability, and the user turns are fixed rather than responsive.
- **Manufactured consent has no dedicated scenario.** The new rule appears incidentally in S6 but was not tested against a deliberately leading question chain.
- **No cross-host verification.** Only the host this was developed on has been tested; the flat-file installation form loses the `references/` directory.
- **One external review, no external *use*.** The skill has still not been run by anyone who was not reviewing it.
- **Distribution was unsolved, and is now only partly solved.** `npx skills add Karry-2026/socratic-elenchus` was tested and installs correctly into `.agents/skills/` with a Claude Code symlink; a synthetic demo GIF (`docs/demo.gif`) was added. What is still missing is a real user: nobody outside the author has run this in anger.
- **The version was rolled back from 1.0.0 to 0.9.0** one day after publication. A first-day 1.0.0 is a promise the evidence did not support; the two entries are the same content, and `CHANGELOG.md` records the rollback.
- **English text is a translation, not an original.** If the two diverge later, the Chinese file is the source of truth and `scripts/validate.py` only checks that they stay structurally aligned.

## Reproduce

```bash
python scripts/validate.py --root .
```

59 structural checks. Behavioural runs: `test/scenarios.md`, scoring: `docs/rubric.md`.
