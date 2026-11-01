The revised draft is ready as a local skill draft. The earlier decision-changing holes are closed in the current text, and the executor’s dispositions of those suggestions are justified. No remaining defect would change a careful agent’s next action or let a different statement pass as the original theorem.

## 1. Files and scope

I read the current `SKILL.md`, `references/adversarial-review.md`, `references/verification-and-handoff.md`, `context/ARIS_LEAN_WORKFLOW.md`, and `context/skill-evaluation/lean-formalize/cross-model-r1/DISPOSITION.md`. I also read `agents/openai.yaml` and the operational spine of the installed `auto-review-loop` skill: packets, raw responses, fix-then-rereview, continuation, and stop rules, plus its backend, score, and state machinery. I did not edit files, run Lean or Lake, reopen Property B, or call a reviewer. Nothing here is a build result or a proof certificate.

## 2. Remaining issues

None found.

The five earlier holes are now instructions an agent can follow:

- Named Grok and Gemini requests are both required. A same-family or host-default reviewer does not fill either one. If a requested reviewer is unavailable, that checkpoint stays pending and the proof work can continue.
- Checkpoint C is tied to the final exported type, definition bodies, axiom output, and original statement. A Markdown or HTML change to the stated theorem is a claim change.
- Completion looks at the exported declaration’s type. A `theorem`, `lemma`, or `def` can be the proof. A `Prop` definition, a proof of `P → P`, or a moved specification is not the original theorem.
- Unread text, an unanswered question, a failed or empty call, a plan review, a log reading, and an older version are not a final review and are not a reproduction.
- Finite coverage and interpretation have to be in the proved dependency chain. A one-file project can be audited from its own type and axiom transcript.

The dispositions that rejected parts of the earlier advice are right:

- A universal one-retry or one-rereview cap should not override an invoked `auto-review-loop` contract. The draft already stops the harmful cases: no resubmission of unchanged artifacts for more agreement, no outer polling loop, exhaustion is not a proof, and a pending review is not a mathematical gap.
- Same signature with a new trust basis or argument can still need review. Routine tactic edits with the same meaning do not.
- A successful build answers a compilation question about that declaration. It does not settle a semantic mismatch.
- A candidate counterexample can be refuted by a proof or a checked certificate. A Lean negation test for every candidate, and a new status matrix, are unnecessary.
- Checkpoint A can withhold the intended reading. Checkpoints B and C need the actual proof text.

The mathematical corrections are also right. Changing `∀ ε > 0, ∃ N` into `∃ N, ∀ ε > 0` can be a strengthening; it completes the original claim only when the implication back is supplied. An empty object allowed by the original statement is not an error, and adding nonemptiness would change the claim. `#print axioms` belongs on the proof declaration, not on a `Target : Prop` definition. The untested `theorem t : Prop := …` snippet is not required for that distinction.

## 3. Depth, overhead, and missing detail

Nothing should be removed, and no further operational rule is needed.

`auto-review-loop` is much longer because it specifies Copilot, Codex, and manual routing, score thresholds, `review-stage` JSON, hashes, and acquittal receipts. Those are runtime and scoring controls. This skill already has the part that changes a Lean agent’s actions: what enters each packet, a blind first translation, the raw response, a disposition table, a repair before follow-up, follow-up only on the affected obligation, failed calls left pending, and resumption from the existing artifacts. Copying the rest would add a second state and identity system without improving the theorem check.

## 4. Recommendation

Ready as a local skill draft. It is not merged, not installed, and not a certification that a future formalization is mathematically correct.
