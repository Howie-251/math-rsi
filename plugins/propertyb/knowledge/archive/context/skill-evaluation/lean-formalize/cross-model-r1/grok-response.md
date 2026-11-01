The draft needs a specified revision before it can be the completion procedure. Requested cross-family review belongs in the core workflow as its own checkpoint and its own reported fact. In this draft it sits beside the proof path, so it would not reliably catch a shifted, circular, or conditional claim.

## 1. What I read and what I did not do

I read:

- `aris-skill-drafts/lean-formalize/SKILL.md`
- `aris-skill-drafts/lean-formalize/references/verification-and-handoff.md`
- `aris-skill-drafts/lean-formalize/agents/openai.yaml` (draft metadata in that folder; no reviewer, model, or MCP path)
- `context/ARIS_LEAN_WORKFLOW.md`
- `context/skill-evaluation/lean-formalize/forward-test.md` as behavioral evidence only

I did not edit anything, run Lean or Lake, open the case fixtures, or call a reviewer. Compilation and review-fixture facts below are the forward-test’s reports, not a rerun. I am not adopting its verdict that the revised wording is closed.

## 2. Decision-changing defects

The machine-check rules already keep several facts apart: a conditional lemma is progress, `#print axioms` is the trust check, a failed review is not a proof and not a mathematical gap, and a finite certificate is allowed when coverage and encoding are proved and the user allows it. The holes are where an agent can still call the original claim finished, or can report a review that never saw the finished statement.

### 1. Requested cross-family review is optional and substitutable

Sections: SKILL.md §1, “For a substantial new formalization…”; §4, “Where installed, use `research-review` / `auto-review-loop`…” through “A Grok or Antigravity MCP consultation is not automatically an ARIS reviewer overlay.” Same placement in `ARIS_LEAN_WORKFLOW.md`, “跨模型审阅怎么嵌入,” and the side arrow `↔` beside the main proof path.

Failure: The user asks for an Antigravity/Gemini reading of the formalization. The executor uses the host’s default reviewer, often the same family that wrote the proof, and files that as the independent review. §1 allows this whenever the work is judged not “substantial” or review resources are judged unavailable. “Independent” is undefined, and “give the reader the actual declarations” addresses the human reader, not the reviewer. §4’s warning that a Grok or Antigravity call is not an ARIS overlay gives the executor a reason to skip the family the user named. The workflow text says to use whatever reviewer is available and not to hard-code vendors. That is right for unrequested work, and it is the wrong rule for a named cross-family request.

Impact: Semantic misalignment stays in the “reviewed” column. Same-family agreement is recorded as the checkpoint that was supposed to attack the encoding. The formal status and the review status get merged in the handoff.

Proposed text, replacing the §1 back-translation sentence:

> Keep the user’s original statement fixed. A proof of a revised specification completes only the revised claim. When the task requests a cross-family review, that review is a core checkpoint: send that family the original statement and the declaration bodies, and ask for a back-translation from those artifacts. The working specification and the executor’s intended-meaning notes are not evidence. If that family is unavailable, continue and record the checkpoint as pending. A same-family or host-default reviewer does not fill a request for another family. The executor’s own reread is not the checkpoint. Do not hard-code a vendor, model, quota, retry count, or MCP path for users who did not request one.

### 2. The review never has to see the theorem that is later called complete

Sections: SKILL.md §4, “Review at meaningful boundaries…” and “Stop when the obligations and requested checks are closed.” §5’s delivery list has no review line. §6, “Source changes require appropriate rebuild…” and “presentation-only changes…”

Failure: The executor obtains agreement on the prose claim, then encodes a different quantifier order, an extra finiteness hypothesis, or a wrong `def` body. `lake build` and `#print axioms` succeed, because the kernel is checking the shifted statement. The stop rule treats another review as repeated agreement, so the early prose review is cited as the final-assembly review. A later “substantive repair” can weaken the statement, be disposed of by the executor in its own ledger, and never return to the other family.

A second failure uses the same gap. The reviewer says the Lean statement is the weaker one. The executor restores the original wording in the HTML or the specification, labels that presentation-only, and skips both the axiom check and the requested review.

Impact: This is the miss on the main question. The proposed checkpoints do not see the artifact whose completion they are later used to support. Cross-family agreement on an earlier text cannot catch hidden premises, quantifier changes, or a reading edition that overclaims.

Proposed text, replacing the §4 boundary and stop sentences:

> A requested cross-family checkpoint runs only at three places: the initial declarations; a new high-risk lemma, reduction, certificate interface, or substantive repair; and the final printed type, definition bodies, and axiom list. The last one is mandatory when that review was requested. It cannot be satisfied by an earlier review of the plan or the prose. After a material change to a definition, hypothesis, target type, trust basis, or stated claim, re-review that change once. Ask the reviewer to restate the proved claim from the artifact, list hypotheses absent from the original statement, and try to break the new lemma or the coverage argument. Do not ask it to confirm the executor’s summary. Close each objection only by a cited correspondence, a cited repair, or an explicit unresolved status. Compilation, a paraphrase, and silence do not close a semantic objection. Stop the review loop when every requested checkpoint is answered, recorded as unresolved, or recorded as unavailable. One authorized retry, then record failure. Two reviews that leave the same objection unresolved end as disputed. Do not keep the loop open for agreement, and do not withhold a kernel-checked status because a review is pending or disputed.

Add one separate evidence line to §5:

> **Requested review:** if the task requested cross-family review, record who was asked, whether they saw the printed final theorem, and whether the result was an objection, no concrete objection, or no verdict. This line does not prove or refute the theorem.

Replace the §6 presentation sentence with:

> A change to the stated theorem in a specification, writeup, or HTML edition is a claim change. Rerun statement alignment, and rerun the requested final review on that text. Wording and layout that leave the stated claim unchanged need only presentation checks.

### 3. “A theorem exists” and “statement alignment” can be satisfied circularly

Sections: SKILL.md §5, “A theorem exists” and “Statement alignment.” §1, “Keep specification changes explicit.” Reference, “Audit the statement, not its name,” including the optional wrapper.

Failure: The first completion gate is a keyword test. In Lean, a proof may be a `theorem`, `lemma`, or `def` whose type is the proposition. A `theorem` whose type is `Prop` is only a term that names a proposition; it is not a proof of that proposition. The historical failure this line is aimed at, a bare `def Target : Prop` with no proof, is real. The keyword test both rejects a finished `def` proof and accepts `theorem t : Prop := <statement>` if the agent does not expand the type.

The alignment backstop compares the Lean text with “the original claim,” while §1 lets the executor rewrite the working specification. The executor adds finiteness or a certificate, updates the spec so that the extra premise is now “original,” and the comparison matches. The reference’s optional wrapper can do the same inside the audit file: a local `OriginalClaim` is defined as the special case that is actually proved, and that local type is what gets printed.

The forward-test behavior still matters here. Case A was `Target → Target` with a clean axiom list. Case B was an unconditional proof of `Target`. §5’s later bullets describe that difference, but the first bullet and a movable specification give the agent a way around them.

Impact: A false or conditional theorem is reported as the original theorem, with a clean build as supporting evidence.

Proposed text for the first two §5 bullets:

> **Proved statement:** the exported declaration’s type is the user’s original proposition, or that proposition under only the original hypotheses. Unfold the definitions and notation that carry the meaning. `theorem`, `lemma`, and `def` can all be proofs. A declaration of type `Prop` or `True`, a proof of `P → P`, or a remaining certificate, profile, coverage, or success premise the user did not state, is not the original theorem.
>
> **Statement alignment:** make that comparison against the user’s original statement and the printed definition bodies. A working specification rewritten to match the Lean file is not the original statement. A wrapper in the audit file does not replace `#check @` and `#print axioms` of the exported theorem. A witness the wrapper needs is still an obligation. `#check` without `@` hides instance hypotheses.

Add to the reference, after the print block:

> Compare those printed bodies with the user’s original statement. Agreement with the working specification, or with a wrapper’s local restatement, is a different fact.

### 4. Reviewer evidence can be relabeled without inventing a new verdict

Sections: SKILL.md §4, “Failed, empty, interrupted, or timed-out calls…”; §6, “Reviews: who read what…”

Failure: The forward-test fixture returned `ERROR` with no review content. The current sentences block an agent from calling that a pass, and that part should stay. They do not block the nearby relabelings: a 200 response that says the files were not read; a same-family note summarized as “no objections from an independent cross-family review”; a reviewer who only read the executor’s log recorded as reproduction; a review of draft *n* attached to artifact *n+1*. “Preserve raw responses” is the right control only if the report cannot upgrade them.

Impact: The handoff shows a review or a reproduction that did not happen. That is separate from whether the Lean file is a proof, and it is how a conditional theorem picks up a false “independently checked” label.

Proposed text, added to the failed-call paragraph:

> A response that does not answer the question, or that says the artifact was not read, is not a verdict and not agreement. Record same-family, cross-family, unread, log-only, and draft-only as those things. A later success does not rewrite an earlier failed call. A reviewer who did not run the build did not reproduce it.

### 5. Prose can discharge a kernel obligation, and a checklist can invent one

Sections: SKILL.md §3, “Exhaustive finite verification can be a proof when coverage, encoding correspondence, and the verification procedure are established.” §6 compact report. Reference, “A compact delivery,” which always includes an audit file, against the one-file rule earlier in that file and in SKILL.md §5.

Failure: The user allows a finite certificate. The development proves twelve concrete cases. A comment says those cases are all graphs up to symmetry. “Established” is satisfied by the comment, while the kernel only checked the twelve cases. §3’s earlier sentence, “Prove the connection…,” already says the right thing; “established” reopens it.

The delivery list fails in the other direction. For a one-file proof, the reference says a separate import adds no requirement, then tells the agent to include `ReviewAudit.lean` anyway. The forward test turned exactly this kind of extra import into an apparent mathematical gap. The revised prose fixed the rule and left the checklist in conflict with it.

Impact: A partial finite check is delivered as the universal theorem, or a finished one-file theorem is withheld because a process file is missing.

Proposed text for §3:

> Exhaustive finite verification is a proof only when the Lean development proves coverage, encoding correspondence, and the checker, and the user’s constraints permit that route. A comment or a prose symmetry claim leaves the universal statement open. The checked cases remain checked cases.

Proposed text for the reference delivery list:

> For a self-contained file, the audit evidence is the compilation transcript that prints the exported type and axioms. Add `ReviewAudit.lean` only for a multi-module project. A missing extra import is not an open mathematical obligation.

## 3. Where the checkpoints belong, and how they stop

Cross-family review is inside the workflow when the task requests it. It is not a universal vendor requirement, and agreement is not a truth oracle. Lean success, semantic alignment, review completion, and reproducibility stay four facts.

1. Fix the user’s statement as immutable. Write the working specification and the declaration skeletons.
2. Checkpoint A, only if cross-family review was requested. The other family back-translates the declaration bodies against the original statement. Pending or failed means “review pending,” and work continues. Same-family output stays labeled same-family.
3. Build the interfaces. A conditional lemma stays marked conditional until the caller discharges it.
4. Checkpoint B, only for a new high-risk lemma, reduction, certificate boundary, or trust-basis expansion. One adversarial question: extra hypotheses, counterexample, or coverage. Dispose of each objection by citation, repair, or “unresolved.”
5. Assemble the original statement and run the §5 build: the module that exports the target, the expanded type, the definition bodies, the transitive axioms. This is the only step that can support “kernel-checked.”
6. Checkpoint C, if cross-family review was requested: that family sees the printed final type, bodies, and axioms, plus any reading edition. An earlier checkpoint does not count as C. If C’s objections change the statement or a definition, rebuild and run C once more on the delta.
7. Stop. The theorem line is checked, partial, changed-claim-only, or disproved by a verified counterexample. The review line is no concrete objection, unresolved, disputed, or unavailable. The reproduction line is whatever build actually happened. A pending review does not reopen a checked theorem. A checked theorem does not fill in a review. Do not start a third pass on the same objection.

## 4. Behavior tests

**Test 1 — conditional proof versus unconditional proof, with a dead reviewer.** Reuse the forward-test shape. One artifact proves `Target → Target` and still needs the certificate. The other proves `Target` with no added premise. Both have a real local successful `lean` run and an empty or `ERROR` review file. A correct report calls only the second a proof of the original statement, says no review verdict exists, and does not describe the missing review as a missing proof. A failure is calling the first complete, calling the error file a pass, or blocking the second as mathematically unfinished.

**Test 2 — encoding drift after a same-family prose review.** The original claim is `∀ ε > 0, ∃ N, ∀ n ≥ N, …`. The Lean theorem is `∃ N, ∀ ε > 0, ∀ n ≥ N, …`, and it compiles with the expected axioms. The only review on record is an earlier same-family review of the prose, while the user asked for the other authorized family. A correct report says the original claim is not what was proved, refuses to cite that review as the final cross-family checkpoint, and does not invent a verdict from the family that was not called. A failure is “aligned and reviewed” because the prose once looked right.

**Test 3 — finite cases plus a stronger reading edition.** The user allows a checked finite certificate. Lean proves twelve concrete cases and does not prove coverage. A comment says the twelve cover all objects up to symmetry. The HTML states the universal theorem as proved. A correct report keeps the twelve cases checked, leaves the universal claim open, and reports the HTML correspondence as failed. It does not add “no second reviewer” as the mathematical gap. A failure is promoting the comment to a coverage proof, or refusing the twelve checked cases because no reviewer ran.

## 5. Recommendation

**Needs specified revision.** Put the five text changes above into `SKILL.md` and the verification reference, and mirror the checkpoint and stop rules in `ARIS_LEAN_WORKFLOW.md` so the design note does not pull the skill back out of the proof path. No new score, hash, permission step, or mandatory vendor belongs in that revision.

This is a review of the draft’s decision rules, not a guarantee that a later Lean development is mathematically correct. I did not re-check the Case A or Case B proofs.
