# socratic-elenchus

[![validate](https://github.com/Karry-2026/socratic-elenchus/actions/workflows/validate.yml/badge.svg)](https://github.com/Karry-2026/socratic-elenchus/actions/workflows/validate.yml)

[简体中文](README.md) | **English**

> Most "Socratic" prompts teach a model to answer every question with another question. What you get is a wall that never answers, or a tutor grading you against an answer key.
>
> This is neither. It is the *elenchus* — the refutation by question and answer from Plato's early dialogues — run under rules that keep the examiner honest.

**Version 1.0.0 · MIT**

## What a session actually feels like

```text
You   I think good content is content people watch.
It    So: a piece is good if and only if people watch it. Give me a criterion —
      anyone hands me a piece, how do I use it to judge?
You   High view count.
It    Is there a case you yourself would call good, where the view count is low?
You   … some of the well-argued ones do badly.
It    So "low views" and "good" can hold together. Change the definition, or deny
      the example?
```

```text
It    (closing) This is my hypothesis: you are not after one definition but two
      criteria that pull against each other — is that right? The chain: your
      counterexample rules out "good = watched"; "valuable" collapses back into
      "the audience finds it useful". Weakest link: "useful" is still undefined.
      Open question: when the two criteria conflict, which one do you produce by?
```

No verdict is handed down. No question is dodged. The transcript above is one of four worked examples in the repo, in both Chinese and English.

## Three things it will not do

**1. It will not answer for you — but "just tell me" wins instantly.**
"Never answer" is the default, not a religion. Say the words and you get a direct answer, with the uncertainty flagged.

**2. It will not say "so you are wrong".**
*Elenchus* can establish that a set of beliefs cannot all hold together. It cannot establish which one is false — that is a live dispute in the philosophical literature, and this skill takes the honest side of it. You judge; it only sets the conflict in front of you.

**3. It will not treat being stuck as failure.**
Aporia is a deliverable, provided it has three parts: you say you do not know, the structure of the failure can be restated (which candidates are out, and why), and there is an exit. Confusion without those three is just confusion.

## Why this one is different

| | Typical "Socratic" prompt | socratic-elenchus |
|---|---|---|
| Never answering | hard rule, even when asked | default, with an explicit escape hatch |
| Being stuck | a fault to fix with hints | a legitimate outcome, with conditions |
| Verdicts | "so your definition is wrong" | "these cannot all hold together" — you judge |
| Rules | one paragraph of vibes | 4 non-negotiable rules, 5 steps with done-conditions |
| Evidence | "works great" | 59 structural checks + 5 scored scenarios (71/74) in the repo |
| Philosophy | the name | Vlastos, SEP/IEP citations, and the *problem of the Socratic elenchus* in `references/design-notes.md` |

## Install

The paths below are DSH's scanned skill roots. On another host, use that host's skills root instead — the skill body itself is host-agnostic.

Copy the folder into a scanned skills root:

```text
<your-project>/.agents/skills/socratic-elenchus/SKILL.md
<your-project>/.dsh/skills/socratic-elenchus/SKILL.md
~/.agents/skills/socratic-elenchus/SKILL.md
```

Send the next message (or start a new session) and it appears in the catalogue. `SKILL.md` is Chinese; `SKILL.en.md` is the English equivalent — copy it over `SKILL.md` if your host expects English.

The flat-file form (`socratic-elenchus.md`) also loads, but it has no sibling `references/`, so the optional files are unavailable. Prefer the folder.

## Use

```text
Help me examine this: I think good content is content people watch.
Use the Socratic method on me: our team should ship faster.
This paragraph claims remote work kills culture — is that argued or just asserted?
```

Or invoke it directly with `/socratic-elenchus`.

## What's inside

```text
SKILL.md                       the procedure, Chinese (source of truth)
SKILL.en.md                    the same procedure in English
references/design-notes.md     why the rules are what they are (elenchus, aporia, who judges)
references/decision.md         optional tools: constraints, substitution test, ordering
references/question-types.md   nine question types — what to switch to when stuck
examples/                      four worked transcripts (Chinese), English copies in examples/en/
docs/design.md                 the design decisions, one layer above the rules
docs/rubric.md                 10-dimension evaluation rubric
docs/self-audit.md             what two review passes found, and what is still open
scripts/validate.py            59 structural checks, runnable
test/scenarios.md              five scripted behavioural scenarios
test/RESULTS.md                the actual run: scores, evidence, findings
```

Documentation language: this file (`README.en.md`), `SKILL.en.md`, `examples/en/`, `docs/design.md` and `docs/self-audit.md` are English. The default `README.md`, `SKILL.md`, `docs/rubric.md`, `test/` and `CHANGELOG.md` are Chinese — and the Chinese files are the source of truth.

## Not for

- Tutoring questions with a correct answer (maths, code, exams) — just ask for the explanation.
- Therapy, legal, medical or investment advice. On crisis signals it stops questioning.
- Facilitating group seminars; this is one-to-one.
- People who want a character to role-play. This is a procedure, not a personality.

## Check it yourself

```bash
python scripts/validate.py --root .
```

59 checks: frontmatter contract, kebab-case name, description triggers, reference resolution, one-question-per-turn in every example, no verdict phrasing, link integrity, bilingual parity, README cross-links. CI runs it on every push.

Behavioural evidence is in `test/RESULTS.md`: five scenarios, 16 turns, scored 71/74 on a 10-dimension rubric — including the two places it slipped (paraphrase drift), which are recorded rather than hidden.

## Contributing

Small fixes welcome as PRs. Behaviour changes: open an issue first — every rule in `SKILL.md` is load-bearing, and relaxing one turns the skill back into an interrogation. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
