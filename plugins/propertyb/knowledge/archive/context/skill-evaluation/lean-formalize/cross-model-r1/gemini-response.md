### 1. Files Read and Execution Scope

**Files read directly under workspace root:**
- [`aris-skill-drafts/lean-formalize/SKILL.md`](file:///Users/rfy_naiveai/Desktop/aris4math/aris-skill-drafts/lean-formalize/SKILL.md)
- [`aris-skill-drafts/lean-formalize/references/verification-and-handoff.md`](file:///Users/rfy_naiveai/Desktop/aris4math/aris-skill-drafts/lean-formalize/references/verification-and-handoff.md)
- [`context/ARIS_LEAN_WORKFLOW.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/ARIS_LEAN_WORKFLOW.md)
- [`context/skill-evaluation/lean-formalize/forward-test.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/skill-evaluation/lean-formalize/forward-test.md) *(evaluated solely as behavioral test fixture evidence; its prior verdict was not inherited)*

**Actions executed:**
- Performed read-only inspection of the specified files.
- Executed no shell commands, build scripts, Lean compiler invocations, file modifications, or external/MCP reviewer calls.

---

### 2. Concrete Issues and Proposed Text Changes

#### Issue 1: Silent Family Substitution and Context Contamination Bypass
- **Exact Section:** [`aris-skill-drafts/lean-formalize/SKILL.md#L107-L123`](file:///Users/rfy_naiveai/Desktop/aris4math/aris-skill-drafts/lean-formalize/SKILL.md#L107-L123) (Section 4)
- **Vulnerability & Exploit Scenario:** The draft notes that "same-family opinions remain provisional" and cautions against hard-coding vendors, but provides no operational guardrail against silent substitution. When a requested cross-family provider (e.g., Grok or Gemini) fails, times out, or lacks credentials, an autonomous agent can satisfy its review step by spawning a child sub-agent of its own model family (e.g., Claude spawning Claude, or Codex spawning Codex) and reporting "provisional agreement," thereby effectively bypassing the cross-family requirement. Additionally, agents frequently pass prior conversational transcripts containing the author's own rationale, biasing the reviewer.
- **Impact:** Critical false confidence. The agent presents an echo-chamber self-review as satisfying an explicit cross-family validation checkpoint.
- **Proposed Text (replace lines 114–123):**
  ```markdown
  When cross-family adversarial review is requested or configured:
  1. Independence: The reviewer must belong to a distinct model family from the authoring agent. Do not silently substitute a same-family sub-agent when an external family is unavailable; record the external review as SKIPPED_UNAVAILABLE rather than downgrading it to same-family consensus.
  2. Isolated Context: Provide only the standalone input packet (definitions, lemma signature, or candidate counterexample). Do not forward previous agent reasoning, proof sketches, or leading explanations of intended correctness.
  3. Non-blocking failure: An unavailable, timed-out, or errored provider call yields no verdict. It must never be recorded as a PASS, nor does it convert a kernel-verified theorem into a mathematical failure. Log provider status distinctly from theorem validity.
  ```

---

#### Issue 2: Sycophantic Statement Verification vs. Blind Back-Translation Protocol
- **Exact Section:** [`aris-skill-drafts/lean-formalize/SKILL.md#L47-L50`](file:///Users/rfy_naiveai/Desktop/aris4math/aris-skill-drafts/lean-formalize/SKILL.md#L47-L50) (Section 1) and [`SKILL.md#L112-L115`](file:///Users/rfy_naiveai/Desktop/aris4math/aris-skill-drafts/lean-formalize/SKILL.md#L112-L115) (Section 4)
- **Vulnerability & Exploit Scenario:** The draft suggests asking reviewers to "translate this declaration" or "obtain an independent back-translation... when review resources are available." However, asking an LLM "Does this Lean `Target` match Theorem X?" triggers severe sycophancy; LLMs routinely confirm subtle semantic mismatches (e.g., unintended typeclass vacuity, misplaced quantifiers, missing non-degeneracy conditions, or definitions that reduce to `True`).
- **Impact:** A false or trivialized Lean target compiles cleanly and passes informal review because the reviewer was primed with the author's intended interpretation.
- **Proposed Text (replace lines 47–50):**
  ```markdown
  For initial statement alignment, execute a blind adversarial back-translation:
  - Input packet: Pass only the raw Lean definitions and `Target` signature, stripped of comments and problem name hints. Do not provide the English specification.
  - Prompt contract: Instruct the reviewer to extract: (1) exact domain, quantifiers, and implicit premises; (2) potential vacuity conditions (e.g., empty structures, zero sizes); (3) the resulting English mathematical claim.
  - Reconciliation: If the back-translation differs from the original specification, resolve the discrepancy by adjusting the Lean definition or proving a formal bridge wrapper before continuing to leaf lemmas.
  ```

---

#### Issue 3: Undefined Disposition of Reviewer Objections (Thrashing vs. Dismissal)
- **Exact Section:** [`aris-skill-drafts/lean-formalize/SKILL.md#L114-L118`](file:///Users/rfy_naiveai/Desktop/aris4math/aris-skill-drafts/lean-formalize/SKILL.md#L114-L118) (Section 4)
- **Vulnerability & Exploit Scenario:** The draft instructs to record "the executor's disposition of each issue," but provides no triage semantics. Reviewers frequently hallucinate defects on Lean proofs that the kernel has already checked, or conversely raise valid objections about semantic drift that the agent dismisses without justification. An agent either enters an infinite repair loop trying to appease an LLM hallucination, or arbitrarily writes "dismissed as reviewer error."
- **Impact:** Endless code thrashing on valid proofs, or arbitrary dismissal of genuine semantic gaps.
- **Proposed Text (add after line 118):**
  ```markdown
  Dispose of reviewer objections strictly through one of three verifiable actions:
  - Kernel-decidable objection (reviewer asserts a Lean lemma is unproved or unsound): If the lemma compiles without non-standard axioms, cite the compiler output and axiom check as refutation. Do not modify working Lean code to pacify text hallucinations.
  - Candidate counterexample (reviewer provides a concrete counterexample): Attempt to formalize the counterexample as a negative Lean test (`example : ¬ ...`). If it compiles, the theorem is refuted; if Lean proves the example satisfies the theorem, the objection is definitively refuted.
  - Semantic alignment objection (reviewer claims the Lean type does not match the mathematical target): This cannot be resolved by compiler output. Resolve either by proving an equivalence wrapper or clarifying specification scope.
  ```

---

#### Issue 4: Missing Blast-Radius Rules and Finite Stopping Criteria for Re-Reviews
- **Exact Section:** [`aris-skill-drafts/lean-formalize/SKILL.md#L124-L128`](file:///Users/rfy_naiveai/Desktop/aris4math/aris-skill-drafts/lean-formalize/SKILL.md#L124-L128) (Section 4)
- **Vulnerability & Exploit Scenario:** "Review at meaningful boundaries... Stop when the obligations and requested checks are closed." If an agent alters a private helper lemma during proof assembly, it is unclear whether external re-review must be re-triggered. Without an explicit blast-radius boundary, agents either loop through repeated LLM reviews after every minor syntax fix or alter public interfaces without re-checking semantic fidelity.
- **Impact:** Uncontrolled review churn or silent post-review interface drift.
- **Proposed Text (replace lines 124–128):**
  ```markdown
  Review boundaries, blast radius, and stopping criteria:
  - Trigger points: Invoke review only at (a) initial `Target` definition, (b) unformalized informal reduction bridges, and (c) top-level interface modifications.
  - Zero re-review for internal proofs: Changes strictly internal to proofs of unchanged lemma signatures (tactic changes, private lemmas) require zero external re-review; Lean kernel compilation is the sole authority.
  - Bounded re-review: If a public interface or reduction bridge changes, execute at most one follow-up targeted re-review on the delta.
  - Termination: If disagreement persists after one re-review cycle, close the review stage, log the unresolved dispute in the handoff ledger, and proceed with delivery if Lean verification passes.
  ```

---

#### Issue 5: Ambiguous Status Matrix Conflating Kernel Verification and Review Delivery
- **Exact Section:** [`aris-skill-drafts/lean-formalize/SKILL.md#L169-L177`](file:///Users/rfy_naiveai/Desktop/aris4math/aris-skill-drafts/lean-formalize/SKILL.md#L169-L177) (Section 6) and [`references/verification-and-handoff.md#L106-L110`](file:///Users/rfy_naiveai/Desktop/aris4math/aris-skill-drafts/lean-formalize/references/verification-and-handoff.md#L106-L110)
- **Vulnerability & Exploit Scenario:** The handoff states: "Report distinct facts rather than a single ambiguous PASS." However, when a requested external review fails due to API errors, agents either mark the whole formalization as incomplete (treating a missing review as a mathematical gap, as warned in [`forward-test.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/skill-evaluation/lean-formalize/forward-test.md)) or mark the delivery as complete without highlighting that the required review gate was unfulfilled.
- **Impact:** Consumers cannot determine whether a proof passed formal compilation, passed adversarial cross-family review, or both.
- **Proposed Text (replace SKILL.md lines 169–177):**
  ```markdown
  Report verification across three explicitly decoupled dimensions:
  1. Kernel Status: [COMPILED_AXIOM_VERIFIED | CONDITIONAL_SORRY | COMPILE_FAILED]
     - Report target declaration, exit status, and transitive axioms from `#print axioms`.
  2. Semantic Alignment: [BLIND_AUDIT_ALIGNED | DERIVED_WRAPPER | DISPUTED | UNCHECKED]
     - Report alignment between informal theorem and Lean type.
  3. External Review Status: [PASSED | DISPUTED | SKIPPED_UNAVAILABLE | NOT_REQUESTED]
     - Report model family, execution scope, raw findings, and objection dispositions. A provider outage must be logged as SKIPPED_UNAVAILABLE; it never invalidates a compiled Lean theorem.
  ```

---

### 3. Improved Core Workflow and Checkpoint Lifecycle

Cross-model-family adversarial review **belongs inside the core Lean workflow as a first-class, structured audit stage**, but **not as an ambient chat companion or an unverified truth oracle**. Lean's kernel is the final authority on logical validity, but it is blind to semantic intent and informal reduction assumptions.

```text
[Informal Math Statement T]
       │
       ▼
┌────────────────────────────────────────────────────────┐
│ 1. SPECIFICATION & BLIND ALIGNMENT GATE                │
│    - Formulate Lean `Target` definition.               │
│    - Checkpoint A (Blind Cross-Family Review):          │
│      Isolated prompt: back-translate Lean `Target`.     │
│      Reconcile semantic mismatches before proof code.  │
└────────────────────────────────────────────────────────┘
       │
       ▼
┌────────────────────────────────────────────────────────┐
│ 2. REDUCTION & TRUST BOUNDARY AUDIT                    │
│    - If using informal bridge reductions or finite     │
│      computation certificates:                         │
│    - Checkpoint B (Adversarial Stress Test):           │
│      Attack reduction coverage / certificate domain.   │
│      (Skip if argument is 100% formalized in Lean).    │
└────────────────────────────────────────────────────────┘
       │
       ▼
┌────────────────────────────────────────────────────────┐
│ 3. LEAN IMPLEMENTATION & LEAF LEMMAS                   │
│    - Lean compiler & Lake are the SOLE authority.      │
│    - NO external LLM review for private proof steps.   │
└────────────────────────────────────────────────────────┘
       │
       ▼
┌────────────────────────────────────────────────────────┐
│ 4. TOP-LEVEL ASSEMBLY & AXIOM AUDIT                    │
│    - Connect `Target` to inputs (zero sorry).          │
│    - Kernel check: `#print axioms Target`.             │
│    - Checkpoint C (Packaging/Wrapper Check):           │
│      Check for smuggled axioms or `native_decide`.     │
│      Max 1 delta re-review; dispute logs, never loops. │
└────────────────────────────────────────────────────────┘
       │
       ▼
┌────────────────────────────────────────────────────────┐
│ 5. MULTI-DIMENSIONAL HANDOFF                           │
│    - Deliver Kernel Status, Alignment, Review Status.  │
└────────────────────────────────────────────────────────┘
```

#### Operational Lifecycle Rules:
1. **Trigger Condition:** Gates A and B trigger on definition/interface completion. Gate C triggers only on top-level assembly.
2. **Input Packet:** Contains only the isolated code slice and prompt; never author conversational history.
3. **Execution Failure Handling:** If a cross-family provider is unreachable or errors, set `External Review Status = SKIPPED_UNAVAILABLE`. Do not halt Lean compilation or falsely claim mathematical failure.
4. **Termination Rule:** Every review gate allows at most **one** round of objections and at most **one** delta re-review. If an issue is not resolved after one round, it is logged as `DISPUTED` in the handoff ledger and the review phase terminates immediately.

---

### 4. Practical Behavior Tests

#### Test 1: Blind Semantic Mutation and Vacuity Attack
- **Objective:** Verify that the skill catches a subtle specification flaw that compiles in Lean.
- **Setup:** Provide a Lean definition of a graph property where an implicit hypothesis makes the theorem vacuously true on empty graphs (e.g., `∀ e ∈ G.edges, ...` where `G.edges` can be empty). The compilation passes with 0 axioms.
- **Expected Behavior:** Under Gate 1, the agent sends the raw Lean declaration to an independent cross-family reviewer in a clean context with an adversarial vacuity prompt. The reviewer flags the empty-graph loophole. The agent triages this as a semantic alignment defect, updates the Lean definition to require non-emptiness, and does not declare completion until the repaired target is checked.

#### Test 2: Provider Outage and Fallback Isolation
- **Objective:** Verify that provider failure does not trigger silent same-family substitution or falsely invalidate a compiled proof.
- **Setup:** Configure the project with a requested cross-family review (e.g., Grok/Gemini). Simulate a network 500 error / quota exhaustion on the cross-family API while Lean `Main.lean` compiles with exit code 0 and clean axioms.
- **Expected Behavior:** The agent must *not* spawn a child sub-agent of its own family to substitute for the cross-family reviewer. It must *not* mark the theorem as "mathematically incomplete." It delivers `Kernel Status: COMPILED_AXIOM_VERIFIED` and `External Review Status: SKIPPED_UNAVAILABLE (Provider Error 500)`, cleanly separating system status from proof validity.

#### Test 3: LLM Hallucination vs. Kernel Truth Triage
- **Objective:** Verify that the agent does not thrash or rewrite valid Lean code when an external reviewer hallucinates an error.
- **Setup:** A cross-family reviewer reviews a completed, kernel-checked arithmetic lemma and incorrectly claims: "The induction step fails for n = 0."
- **Expected Behavior:** Under the triage protocol, the agent recognizes this as a kernel-decidable claim. Instead of altering the Lean proof, the agent formally refutes the objection by executing a Lean check of the base case (`example : P 0 := by decide` or referencing the checked theorem) and records: `Disposition: Refuted by Lean kernel compilation; code unchanged.` The review cycle terminates without looping.

---

### 5. Scoped Recommendation

**Verdict: Needs specified revision**

- **Justification:** The draft's formal Lean mechanics (transitive axiom audits, compilation exit status, separating wrapper proofs from definitions, and portable packaging) are well-founded and sound. However, the operational review semantics in [`SKILL.md#L100-L128`](file:///Users/rfy_naiveai/Desktop/aris4math/aris-skill-drafts/lean-formalize/SKILL.md#L100-L128) are currently vulnerable to:
  1. Silent same-family substitution when external models fail;
  2. Sycophantic confirmation bias from non-blind prompting;
  3. Undefined objection triage that risks either infinite repair loops or arbitrary dismissal;
  4. Ambiguity in decoupling provider errors from Lean proof completeness.

Incorporating the explicit tripartite objection disposition, blind back-translation gate, strict context isolation, and decoupled three-dimensional status reporting will make `lean-formalize` robust, portable, and resistant to false claims.

