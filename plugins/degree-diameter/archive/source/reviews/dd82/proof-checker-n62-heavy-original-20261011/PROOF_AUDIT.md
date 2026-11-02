# Fresh bounded review: heavy original subgraph

Verdict: **PASS, same-family provisional** for the new deductions, with the established connected/D1 reductions as imported hypotheses. No mathematical correction is needed in the reviewed 307-line version of `proofs/dd82/n62/CONNECTED_REPEAT_HEAVY_ORIGINAL_SUBGRAPH.md`. Cross-family acceptance is outside this subagent review and remains with the parent workflow.

Reviewer: `/root/proof_review_n62_heavy_original`. Review date: 2026-10-11. This review read the full target and the directly used source proofs; it did not use prior audit verdicts as evidence. It does not rerun the historical component-quotient classifications or claim a new formal proof.

The main chain is sound. Binary adjacency makes the even/binary commutation separation exact for all heavy indices. The exclusion of all-one $2\times2$ blocks uses the stronger fact that a heavy pair's entire common-neighbor set is its generated triple, disjoint from $D$. Thus the mate involution really is an automorphism of the actual induced graph, and the simple quotient really has a two-edge matching over every edge. The four-cycle argument checks both mate and nonmate opposite pairs. The maximum degree four uses the complete unit row at root label 4, rather than assuming that a light repeat endpoint cannot be heavy.

The pair count gives the stated squared-degree inequality. Equality is sufficient for the full entrywise matrix identity, including its diagonal and mate entries. Restriction to the integer mate-antisymmetric basis gives $Z^2+Z=\operatorname{diag}(r_i)$; hence adjacent base vertices have equal degrees. This correctly removes $m=7,12,18$ at $d=5,7,9$, respectively. The odd dimension argument at $d=9,m=18$ is valid over the rationals, since $t^2+t-4$ is irreducible.

The separation and port counts retain their hypotheses. At base distance two, the common neighbors provided by the lifted path and by a generated-triangle vertex are distinct because $D\cap S=\varnothing$. Under the additional diameter assumption, the exact original-edge count is $10d-4m$. For $d=9$, ports $4,b$ lie in $W$; counting their repeat edges does not require different generated triples to have different port vertices. The 27 external incidences make $e_B(S,W)$ odd, and the row sum on the 17 vertices of $W$ then gives $e_B(W)\le7$. No unconditional diameter bound or exclusion of a value of $d$ is asserted.

## Adversarial and arithmetic checks

- Equal indices and mate indices in the parity identity cause no exception: the same binary argument applies, and no diagonal repeat term is introduced.
- Allowing two lifted matchings between the same pair of fibers would give a heavy pair common neighbors in $D$, directly violating the actual generated-triple description.
- The square-count bound excludes adjacent and mate endpoint pairs separately; those classes are disjoint because heavy mates are original nonneighbors.
- The boundary $d=1,m=0$ satisfies the equality identities. At $d=3,m=3$, a negatively signed base triangle lifts to a six-cycle and satisfies $Z^2+Z=2I$; thus the equality argument does not accidentally remove this legitimate abstract lift pattern. This is only an abstract-pattern check, not a realizable order-62 graph.
- A short exact Python enumeration of nondecreasing integer degree tuples in ${0,1,2,3,4}$ confirmed the unique feasible extremal multisets $3^4,2$, $4^3,3^4$, and $4^9$, with square sums 40, 84, and 144. The mathematical balancing proofs already suffice; this was a small arithmetic check, not graph enumeration.
- Disconnected or large-diameter base graphs do not satisfy the diameter hypothesis merely from the established edge bounds. The proof explicitly leaves the two port-count consequences conditional.
- Shared unit mates and shared external port vertices do not invalidate edge counting: the incidences have distinct heavy or generated-triangle endpoints. All repeat edges within $W$ are unit because every double endpoint lies in $D$.

No counterexample or open proof obligation was found within this scope. No proof source was edited. The complete obligation list and source discharge are in `PROOF_SKELETON.md`. The target currently has no final near-maximum-degree paragraph; such an addition would require a separately recorded delta check.
