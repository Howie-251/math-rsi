# Checkpoint C — final actual Fin3840 theorem

Kernel status: COMPLETE. Configured external C review: pending. Earlier A/B calls returned output-limit ERROR with no substantive findings; neither is promoted to a pass. This is a new final-source review packet, not a repeat of either failed call.

Original fixed object and graph formula: ../PARAMETERS.json, ../generate.py and ../PROOF.md. The formula graph is on labels64*a+x0+4*x1+16*x2, with a∈Fin60 and coordinates in polynomial GF4. Each port p sends x to T[a,p]x+t*L[inv(p)] at controller C[a,p]. The target is finite order3840, every degree≤20, every pair connected by a true walk≤3, and not every pair connected by walks≤2. It includes no public-record claim or ASCII parser theorem.

Actual final declarations, with no extra arguments:

```
DegreeDiameter.Portfolio.F4Graph3840.concrete_order_degree_and_D3 :
  Fintype.card (Fin 3840) = 3840 ∧
  (∀ u : Fin 3840, graph.degree u ≤ 20) ∧
  DegreeDiameter.Portfolio.DiameterAtMost graph 3

DegreeDiameter.Portfolio.F4Graph3840.diameter_exact_three_in_project_definition :
  DegreeDiameter.Portfolio.DiameterAtMost graph 3 ∧
  ¬ DegreeDiameter.Portfolio.DiameterAtMost graph 2
```

The definition in formal/DegreeDiameter/Portfolio/SingleExtension.lean:15 is exactly:
`DiameterAtMost G D := ∀ u v, ∃ p : G.Walk u v, p.length ≤ D`.

Read the actual final bodies in this order (all under formal/DegreeDiameter/Portfolio/):

- F4Graph3840Field.lean: four-element operations, F.ofCode, F.code and symbolic vector linearity. Encoded2 means w; ring numeral2 means0.
- F4Graph3840.lean: read the definitions after the three numeric data declarations, especially encodeVec/decodeVec, matrix/direction selection, source-dependent stepVec/fiberStep, forward and graph. INPUT_BINDING_CHECK.json checks every original300controller/2700matrix/15direction/5inverse literal against PARAMETERS. It is unnecessary to print the numeric arrays into the review output.
- F4Graph3840MatrixCertificate.lean and F4Graph3840Routes.lean: actual reverse dart matrix/direction obligations, full forward reversal, neighborhood cardinality≤20 and actual3-edge Walk endpoint constructor.
- F4Graph3840Linear.lean, F4Graph3840DecoderInterface.lean and F4Graph3840DiameterInterface.lean: affine extension, basis-to-all-noise implication, before/after centers, and arbitrary-u,v final composition. Follow their real callers in Certificates and Diameter; the development premises do not remain on either final theorem.
- F4Graph3840FastTables.lean: proved matrix_eq_fast, preserving the unchanged original graph while using compact repeated matrices. F4Graph3840RouteData.lean defines the actual selected words and local decoders; its finite data is supported by the existing row proofs, not assumed valid by the theorem.
- F4Graph3840Certificates.lean and the60 imported CertificateRow00…59 modules: complete actual caller discharge. All60 modules have executed exit_code0 receipts. The kernel checks all3300 equal/nonadjacent pairs (each3 basis vectors) and all300 adjacent darts×64 targets. Read row00 as the representative obligation shape and the complete60-row assembly; no need to dump numeric tables or rerun the checks.
- F4Graph3840Diameter.lean: the unconditional D≤3 theorem supplies all local-decoder premises. F4Graph3840Lower.lean: concrete0→6 short-word checks plus real-Walk decomposition. F4Graph3840Exact.lean: the two unconditional exported results above.

Executed evidence here:

- FINAL_COMPILE_RESULT.json: current successful module receipts, final declarations, exact finite domains and scope boundaries.
- F4Graph3840Certificates.log, F4Graph3840Diameter.log, F4Graph3840Exact.log: actual final assembly compilation, all exit_code0.
- F4Graph3840Audit.log and its _RESULT.json: a separate process imported formal/F4Graph3840Audit.lean, printed the actual definitions/types and transitive axioms, exit_code0.
- Both final exported results depend only on `[propext, Classical.choice, Quot.sound]`; no sorryAx, native_decide or unproved extra axiom occurs in their dependency chains.
- CERTIFICATE_BATCH_RESULT.json:59 new rows all COMPLETE,2020.311852CPU within2400aggregate; current Row00 separately passed29.266997CPU. The initial source/degree/linearity modules and prior graph were not rerun for this batch.

Review request: independently back-translate the final definitions and printed theorem types, trace arbitrary original u,v through the actual assembly, and identify any concrete semantic or caller gap. Distinguish a missing external review from a mathematical failure. State precisely which bodies/logs were read; do not claim code execution unless you actually ran it. Keep the reply concise and avoid numeric table dumps.
