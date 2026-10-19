# socratic-elenchus

A Socratic questioning skill for AI assistants: it does not hand you answers, it makes your own beliefs take shape.

Version 1.0.0 · Works with DSH's local skill provider (`.agents/skills` or `.dsh/skills`); other hosts not yet verified.

## What it is

A skill (a set of instructions an AI assistant loads on demand) that runs the *elenchus* — the question-and-answer refutation practised in Plato's early dialogues — as a disciplined, five-step loop:

**take the target claim → clarify the definition → test it with counterexamples → expose the contradiction → revise, or end in aporia.**

It is not a personality you switch on. It is a procedure with hard rules: one question at a time, only the user's own beliefs are tested, the examiner never pronounces a verdict, and the user's own words are what get quoted back.

## What it does

- Turns a vague judgement ("I think X is Y") into a claim that can be tested.
- Forces abstract words down to a criterion you can apply to any case.
- Exposes a contradiction as **one single conflict statement**, never as a verdict on which premise is false.
- Accepts "a precisely stated open question" as a legitimate result. No conclusion is a valid outcome.

## What it is not

- Not a tutor for questions with a correct answer (maths, code, exams) — just ask for the explanation.
- Not therapy, legal, medical or investment advice. On crisis signals it stops questioning.
- Not "argumentative questioning", and not a facilitator for group seminars.
- Not "never answer". If you say "just tell me", it answers and flags the uncertainty.

## Install

Copy the folder so that `SKILL.md` sits in a scanned skills root, for example:

```text
<your-project>/.agents/skills/socratic-elenchus/SKILL.md
<your-project>/.dsh/skills/socratic-elenchus/SKILL.md
~/.agents/skills/socratic-elenchus/SKILL.md
```

Send the next message (or start a new session) and the skill appears in the catalogue.

The flat-file form (`socratic-elenchus.md` at the top of a scanned root) is accepted by DSH's local skill provider, but it has no sibling `references/` directory, so the optional reference files are unavailable in that mode — prefer the folder form.

## Use

```text
Help me examine this: I think good content is content people watch.

Use the Socratic method on me: our team should ship faster.

This paragraph claims remote work kills culture — is that argued or just asserted?
```

Or invoke it directly with `/socratic-elenchus`.

## Layout

```text
SKILL.md                       the procedure, Chinese (the source of truth)
SKILL.en.md                    the same procedure in English (interchangeable)
references/design-notes.md     why the rules are what they are (elenchus, aporia, who judges)
references/decision.md         optional tools: real-world constraints, substitution test, ordering
references/question-types.md   nine question types — what to switch to when stuck
examples/                      four worked transcripts (Chinese), with English copies under examples/en/
docs/design.md                 the design decisions, one layer above the rules
docs/rubric.md                 the 10-dimension evaluation rubric
docs/self-audit.md             what two review passes found, and what is still open
scripts/validate.py            structural checks (frontmatter, links, one-question rule, parity)
test/scenarios.md              five fixed behavioural scenarios
test/RESULTS.md                the actual run: scores, evidence, findings
```

`SKILL.md` and `SKILL.en.md` are equivalent. Use `SKILL.md` as-is for a Chinese-speaking user; if your host expects English instructions, copy `SKILL.en.md` over `SKILL.md`.

Documentation language: the README, `SKILL.en.md` and `examples/en/` are in English; the process documents (`docs/rubric.md`, `test/`) are in Chinese because the transcripts they score are Chinese. `docs/design.md` and `docs/self-audit.md` are in English.

## Contributing

Small fixes (typos, clearer wording) are welcome as PRs. Behavioural changes should open an issue first: every rule here is load-bearing, and relaxing one can turn the skill back into an interrogation. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
