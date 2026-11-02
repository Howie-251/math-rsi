# Frozen core-swap extension signature gate

2026-10-29, before the numerical signature and candidate checks.

Use the already saved `d13_D5_h9_transfer/fold13_classes.json`: singleton classes fixed, both labels of every split pair exchanged. Existing RESULT records this as an automorphism of the50554-vertex core; do not repeat that core-edge verification or reconstruct geometry.

Read original `source51417.edges` once. For each of the863 peripheral vertices e, form its exact core-neighbor set Ncore(e). Keep the full multiplicity of every such signature. An extension of the fixed core swap must permute peripheral vertices and therefore preserve signature multiplicities under the induced core permutation. Compare them in order of the least peripheral label in each group. A first multiplicity mismatch rigorously excludes every full-graph extension of this specified core operation, regardless of how peripheral vertices are permuted. Save the concrete source and transformed signatures and multiplicities, then stop this comparison.

If all multiplicities match, report singleton matching and duplicate groups. Only when every peripheral signature is unique may the resulting unique full permutation be checked against all saved edges. Do not pair duplicate-signature vertices arbitrarily or search their permutations. This is a necessary gate, not an assumption that peripherals are fixed. No D5/BFS/SAT, neighborhood balls, broad Aut search, or installation. One worker,≤5CPU seconds.

## Additional authorized candidate diagnostic, same source read

For each of the40 cached original successful S_i, apply the core swap to its core members but leave each peripheral guard's literal ID fixed. This explicitly defines a different candidate rule; it is **not** asserted to be a full graph automorphism. Record the literal40 candidate sets, which differ from their own source set or from every member of the original40 pool, and whether each individually fits original B0's degree13 spare-port budget and size≤13. Use degrees collected during the same original-edge read; no new graph read or distance calculation.

The actual global coverage of these candidates is unknown until separately authorized work. In particular, core-only walks are preserved, but paths through peripheral vertices cannot be assumed preserved. Do not add guards, change the rule, pack candidates, or generate complete new graphs. If all candidates are unchanged or capacity-invalid, stop; otherwise report the finite literal pool to root for a decision.
