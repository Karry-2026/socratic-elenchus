# Design

Why this skill looks the way it does. Operational rules live in `SKILL.md`; the philosophical sources live in `references/design-notes.md`. This file is the middle layer: the decisions.

## 1. What problem it solves

Most "Socratic" prompts do one of two things:

- they turn the assistant into a character that **never answers** (and cannot be switched off), or
- they turn it into a **tutor** that still assumes a correct answer exists and grades the user against it.

Neither fits the case this skill was built for: a user brings a judgement they are not sure about, and needs it tested — not answered, not graded. The philosophical tradition has a name for that activity: *elenchus*, the refutation by question and answer in Plato's early dialogues.

## 2. The five steps

`define → counterexample → contradiction → revise → close`

Each step has a **done condition** and a **typical failure**, because the failure modes are known and repeating: examples offered as definitions, counterexamples offered by the examiner and then ruled on by the examiner, revisions written by the examiner, contradictions announced as verdicts.

Two rules keep the loop from collapsing into debate:

- **consent cannot be skipped** ("you may skip steps; you may not skip consent");
- **skipping is not deleting** (a skipped step must be declared in the closing).

## 3. Three decision points

**Verdicts.** The standard elenchus ends by declaring *p* false. That step is exactly the one the literature disputes: the argument establishes that a set of beliefs cannot all hold, not which one is false. The skill therefore only permits the weaker claim, and requires that any judgement in a closing be phrased as a falsifiable hypothesis ("— is that right?").

**Aporia.** Being stuck is treated as an outcome, not a fault. A valid aporia has three parts: the user says they do not know, the structure of the failure can be restated (which candidates are out, and why), and an exit is left. Without all three it is just confusion, or a discussion that fell apart.

**Friction.** "Never answer" is rejected. The skill ships four levels (L0 direct answer → L3 defence) with an explicit escape hatch: an explicit "just tell me" wins immediately.

## 4. Main text vs references

The main file is what the model reads on every invocation; the references are read only when needed. The split follows a rule: **anything that changes the next question stays in the main file; anything that is looked up stays out.**

- in `SKILL.md`: the five steps, four rules, closing conditions, output format, boundaries;
- in `references/decision.md`: constraint scan, substitution test, multi-cause ordering, level details;
- in `references/question-types.md`: the nine question types, used when stuck;
- in `references/design-notes.md`: sources and the arguments behind the rules.

## 5. Non-goals

- Not a tutor for questions with a correct answer.
- Not a therapy or crisis tool; it stops when those signals appear.
- Not a seminar facilitator: one-to-one only.
- Not a code-gated workflow: there is no pass/fail in philosophy, so the gate is a self-check list, not a hook.

## 6. How conformance is checked

`scripts/validate.py` checks the structural invariants (frontmatter, name, reference resolution, one-question-per-turn in the examples, no verdict phrasing, link integrity, bilingual parity). Behaviour is checked by `test/scenarios.md` + `docs/rubric.md`, with results in `test/RESULTS.md`.
