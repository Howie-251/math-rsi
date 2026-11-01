# Degree-seven formal continuation

This file maps the remaining formal work after the October 13 final 30-minute window. Read REPORT.md and the most recent successful build/audit logs for the final completed scope. The original problem remains T34: at most 34 five-edges imply Property B. T32 and T33 are frozen.

## Completed reusable actual interfaces

- `TwentyOneSevenTriples.residual777`: three actual degree-seven points under noB have all pair codegrees at most two.
- `TwentyOneSevenTriples.residual778`: two actual sevens and one actual eight have all pair codegrees at most two.
- `TwentyOneSevenTriples.unit_neighbors_pair_le_two`: two degree-eight unit neighbors of an actual seven have pair codegree at most two.
- `TwentyOneSevenUnitQuad.residual` and `TwentyOneSevenUnitSet.unit_set_structure_of_not_propertyB`: an actual unit-neighbor set of at least three eights has all pair codegrees two and at most two such vertices on any center-edge.
- `TwentyOneSevenSelection`: total degree budget, unit-eights budgets, and `one_seven` / `two_sevens` actual set cardinality and structure.
- `TwentyOneSevenQuads.residual`: every actual four-sevens embedding under noB can be relabelled to one of nine exact residual inventories; all 674 finite profiles have complete kernel coverage.
- `TwentyOneSevenOne.propertyB_of_one_seven`: full actual unique-seven branch, with its independent raw Finset and bare Finite audit.

The at-least-five branch is complete: `TwentyOneSevenMany.propertyB_of_many_sevens`, r38 actual build and `many-audit.log` pass. The final Assembly reduces 21-point work to exactly two, three or four sevens. All other 22–25-point obligations remain in Assembly.

## Exactly four sevens

Paper: `../twentyone-math/AT_LEAST_THREE_SEVENS.md`, section 2, r=4. At least eleven eights; choose one, normalize the four sevens with the now-proved residual theorem, and lift that permutation while fixing the added lock with `LockLiftRelabel`. The nine old profiles have 2,000 degree-eight extensions with new-old pair codegrees one or two. All are strict: 1,993 pure labels and seven joint labels, compressible under permutations to 522 pure representatives and four joint representatives.

Only `TwentyOneSevenFive77778Batch000` (first 16 pure representatives) is currently compiled. `generate_seven_large_single.py 77778 <batch> 16` generates further exact-replayed batches. Do not regenerate or claim unbuilt remaining batches as complete. Full joint export, full promotion coverage and actual caller are still needed. `FOUR_SEVEN_EXTEND.json`, `FOUR_SEVEN_EXTEND_JOINT.json` and corresponding verification files contain paper evidence.

## Exactly three sevens

Paper section 3. Eights set has at least thirteen points. The excess budget forces two equal non-222 incidence patterns; the 77788 five-lock domain has 13,944 labels / 1,722 representatives: 1,707 pure, 12 joint, three exact residues. Reusing the same actual five-lock conclusion then forces at least four common unit eights; add a third such eight to obtain the complete 67-label six-lock domain (17 pure representatives plus one joint representative after compression).

None of the 1,707 large pure cases or the final six-lock family is accepted as built yet. `generate_seven_large_single.py 77788 <batch> 16` and `... 777888 ...` support generation. The actual pattern-pigeonhole argument and residual-to-common-unit-set argument also remain. Avoid dumping all 1,707 profiles into one definition; first evaluate the coefficient-caching experiment described in the high-math report, or an equivalent exact row-sharing representation, against a small actual consumer.

## Exactly two sevens

Paper: `../twentyone-math/TWO_SEVENS.md`. `TwentyOneSevenSelection.two_sevens` already supplies the real eights and unit-set bounds, but the full four-pattern bookkeeping is not formalized. The five-lock 77888 classification has 565 profiles, 465 pure labels, 34 joint labels and 66 residues (22 oriented orbits). These imply the A/B/C population bounds. For pair codegree one, four A points give two strict six-lock profiles. For pair codegree two, the complete six-lock domain has 99 representatives: 76 pure, 19 joint and four exact residuals. The resulting two-matchings contradiction is an additional actual graph/counting obligation.

`generate_seven_large_single.py 77888 <batch> 16` and `... 778888 ...` support pure generation; neither full family is compiled. The exact rows and all proof restrictions are in `TWO_SEVEN_THREE_EIGHT*`, `TWO_SEVEN_FOUR_EIGHT*`, and the paper. Do not use only the four displayed matching rows as a classification assumption; derive them from complete actual promotion/projection coverage first.

## Working implementation pattern

`ActualAllocations` binds high-trace counts to a capacity-pruned finite list. `PromotionCatalog`, `PromotionReconstruction`, `LockProjection`, and `LockLiftRelabel` bind lock extensions, all reconstructed counts, projections and label permutations to actual H. They compile and are reusable. Prefer a strict full profile or a strict lower-lock projection over introducing a new global graph theorem when this reduces formal complexity.

Keep Data, expensive Certificates, small coverage dispatcher, and actual caller separate. Use sparse association lists for large natural-number codes. Huge Nat pattern matches and large dense array literals have both failed here for different reasons. Prove the final symbolic inventory dispatch with an abstract `values : List Nat` before substituting actual edge-count expressions; mark the computational `Matched` proposition locally irreducible for elaboration, explicitly unfolding it only at the abstract dispatch. This prevents unnecessary symbolic reduction without changing the kernel trust model.

Heavy Lean checks remain serial and owned by one executor. A light structural import or isolated probe can be checked by that same executor while one numerical process runs if its resource use is controlled; do not launch another numerical table concurrently. Stop a queued dependent target when a prerequisite fails instead of silently rerunning the same expensive failing proof. Preserve commands, failure logs and actual scope, and audit the precise final exported theorem.
