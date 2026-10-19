# Self-audit

A record of what was reviewed before release, what was found, and what remains open. Written so a third-party reviewer can check the claims rather than take them on faith.

## Process

Two independent review passes, run in parallel on the 1.0.0 draft:

1. **Spec review** — can this be loaded as a skill, and is it internally executable? Dimensions: discovery layout, frontmatter contract, reference resolution, rule conflicts, output format determinism, repository conventions.
2. **Alignment review** — does it actually do what it claims? Compared line by line against the philosophical research (`references/design-notes.md` sources) and against the mechanisms used by comparable open-source skills.

Both passes were text-only: no behavioural run was performed in that round. That gap is what `test/RESULTS.md` closes.

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

## What remains open

- **Behavioural evidence is thin.** Four scripted scenarios, three turns each, judged by a rubric. This tests rule execution, not long-dialogue stability, and the user turns are fixed rather than responsive.
- **No cross-host verification.** Only the host this was developed on has been tested; the flat-file installation form loses the `references/` directory.
- **No third-party use.** The skill has not been run by anyone who did not build it.
- **English text is a translation, not an original.** If the two diverge later, the Chinese file is the source of truth and `scripts/validate.py` only checks that they stay structurally aligned.

## Reproduce

```bash
python scripts/validate.py --root .
```

59 structural checks. Behavioural runs: `test/scenarios.md`, scoring: `docs/rubric.md`.
