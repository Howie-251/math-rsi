# C5 quotient lift obstruction — frozen proof obligation

Status: ORIGINAL_TARGET_PROVED_AND_REVIEWED, 2026-10-13. Full proof is linked as local-proof.md; root and fresh local reviewer found no gap, and same-thread Gemini round3 accepted. The written local audit is complete at reviews/dd82/proof-checker-c5-twelve-pentagons-20261013/PROOF_AUDIT.md. A direct broader corollary and its second actual quotient instance have since been checked by root and writer and sent to same-thread round4; round4 returned SUCCESS and accepted the addition. The scoped proof run is complete, not the full Goal. Parent research run:
dd82-v3-c5-full60-20261013, same Gemini thread
96b3d1dd-a98e-4f75-8fb8-d0ec91fa37fe. This is a new proof run,
not a reset of either research review loop.

Prove that the exact twelve-orbit matrix in
../../computations/dd82/construction/cyclic5_full60_quotient_run/best_quotient.json
admits no simple degree-eight diameter-two free-C5 lift. Quantify over
every voltage set and both possible internal steps, not merely a seed.
The actual quotient is feasible as an integer matrix and was found by a
real bounded construction. It has not been realized as a target graph.

Sufficient proof obligations, in order:
1. The actual defect quotient is two K6 components; original-graph
   nonnegativity forces the cross-defect block to vanish.
2. Each induced thirty-point graph consists of a C5 plus five C5s or
   a C25. The cross Sylvester equation rules out C25 using fifth and
   twenty-fifth roots and the actual defect row budget.
3. For two sides of six C5s, each cross block is a perfect matching
   that maps the cycle to its complement. Such matchings have slopes ±2.
4. Exact six-route coverage forces a sign matrix switching to all+
   or a single−. The all+ case imports the already proved K66 lift
   exclusion; the single− case has incompatible Gram rank conditions.
5. Recombine to exclude all lifts of this quotient. The general free-C5
   family and arbitrary58–61 remain open.

Sources already read: the saved full matrix and D, quotient experiment
source/result, CYCLIC5_WITHIN_ORBIT_DIFFERENCE_CONSTRAINTS.md,
CYCLIC5_K66_QUOTIENT_EXCLUSION.md, full-C5 preparation and definition.
Writer: petersen_six_fibers60, with root-supplied sign/Gram derivation;
root read the complete final proof. Fresh proof-checker and same
Gemini thread reviewed the actual completed original argument. The added
corollary requires only a zero cross-defect block and the same internal
cycle shapes; earlier reviews are not represented as covering new text.

ARIS adaptation: project-local proof-orchestrator and notation-audit
instructions actually read. Keep target, dependencies, proof, local
correctness review, exposition and final scope. V3/global user rules
disable mechanical scorecards, hashes/manifests, browser handoffs,
DeepSeek/GPT fallback and old Lean. Check definitions and notation
directly rather than producing arbitrary notation scores. No external
approval question: relevant research to existing Gemini is authorized.

The fixed-M voltage step was design only and is now cancelled: no source,
CNF, runner, seed check or solver was created. This is a pure obstruction,
not a SAT/UNSAT result.
