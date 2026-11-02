# Fresh scoped proof audit: order61, (12,21,28)

**Verdict: PASS.** No mathematical issue found in the complete new exclusion. The final exactly-three-components corollary follows with the explicit inherited finite classification and companion (6,25,30) exclusion. This is a same-family, provisional semantic review, not an external or formal acceptance.

Reviewer: `/root/n61_c3_lift_fresh_check`; model `gpt-6-astra`, reasoning `ultra`. This canonical identity is the actual identifier exposed by the collaboration tool; no separate opaque UUID was exposed. One fresh review round; no prior review artifacts or root commentary were consulted. The manuscripts contain their own historical status text, which was not used as evidence of correctness.

## Scope and actual inputs

- `AGENTS.md` and `.agents/skills/proof-checker/SKILL.md`, complete; the requested V3 adaptation controls this review.
- `proofs/dd82/n61/THREE_COMPONENT_12_21_28_EXCLUSION.md`, complete, lines 1–346: all mathematics freshly checked.
- `proofs/dd82/n61/GENERAL_THREE_DEFECT_COMPONENT_QUOTIENTS.md`, complete, lines 1–204: actual definitions, quotient reduction, inherited finite classification and its exact domain.
- `proofs/dd82/n61/THREE_COMPONENT_6_25_30_EXCLUSION.md`, complete, lines 1–238: read for the companion theorem's hypotheses and scope; its exclusion remains inherited.
- `computations/dd82/n61/component_quotient_three.py` and `.result.json`, complete and read-only: inspected domain, necessary filters and retained output. The earlier complete finite run was neither repeated nor recertified.

No proof or wiki was edited. No subagent, external reviewer, solver, graph enumeration, new finite-table computation, rendering, Lean or old62–65 work was used. No hashes, checksums or manifests were generated.

## Checked obligations

| Obligation | Location in new manuscript | Finding |
|---|---|---|
| Actual B, all blocks and commutation | 40–85 | PASS: regularity, zero diagonal, nonnegative weighted entries and row sum 4 give the stated identities and spectral interval. Optional T-connectivity has the correct 13-versus-4 contradiction. |
| Exhaustion of R cycles | 89–124 | PASS: integral row sums force multiples of 4; the five-dimensional injected space requires at least five even cycles. The four partitions exhaust 28 vertices. |
| Four-periodicity of X | 128–157 | PASS: the finite sum of squares forces alternating pair sums; the difference recurrence forces opposite residue classes. Four supports partition the 12 rows into triples. |
| Compression and C12 exclusion | 161–199 | PASS: the factor is exactly k/2, with projected columns repeated 2k times per parity. The Rayleigh lower bound is (8k+7)/3 and the upper bound is 9. |
| C8 weighted commutator | 203–261 | PASS: B_88=2P4+W, and the (z,z+2) entry of the commutator gives w_(z−1)=w_z with no additional terms. |
| C8 two-way edge count | 263–291 | PASS: (n_0,n_1,n_2)=(5,8,8), and the same T edges are counted as 5×4=20 and 8×2=16. |
| Seven C4 labels | 298–337 | PASS: the local neighbor labels exhaust all disjoint triples. The nonempty image is neighbor-closed in connected KG(7,3), forcing 35 images from 21 vertices. |
| Combining two quotient cases | 5–29, 341–346 | PASS relative to the explicit inherited dependencies: exactly c=3 is excluded for arbitrary targets, with every simultaneous relabeling included. |

The classification's actual quotient reduction was checked directly: the row-four eigenspace is the component-constant space; AB=BA makes the partition equitable; detailed balance symmetrizes Q; the polynomial relation and irrational conjugate multiplicities give odd c≤17. At c=3 the inherited finite domain is all 45³ nonnegative integer matrices of row sum eight. Source and retained output match that necessary-condition domain and the two permutation classes. This review does not newly certify the enumeration run.

## Relevant counterexample attempts

- Weighted, nonbinary B and the extreme eigenvalue −4 do not invalidate the spectral argument: the injection still has lower norm bound 1.
- Minimal C4 cycles and the five-, six- and seven-cycle boundaries are all covered. Cycles of other lengths are excluded before the partition argument.
- Repeated/opposite balanced sign vectors and cycle orientation changes preserve the Rayleigh bound; repeated types only strengthen it.
- In the C8 case zero rows are included, h=0 violates nonnegative defect, h≥2 violates the 24-incidence total, and each unordered step-three pair is represented exactly once.
- Repeated labels or disconnected T do not evade the seven-C4 argument: injectivity and T-connectivity are not assumed.

No counterexample or unresolved candidate was found. All inequalities and theorem applications use the stated finite, real, binary or nonnegative hypotheses at their application points. Limits, probability modes, asymptotic uniformity and infinite interchanges are inapplicable.

## Dependency and issue status

The dependency chain is acyclic: actual graph → defect/block identities → cycle exhaustion and periodicity → C12/C8/7C4 contradictions → new quotient exclusion. The final c=3 corollary adds the earlier classification and companion theorem; neither is derived from the new result.

**Issues: none.** No fixes required or applied. The complete new theorem is established within the reviewed scope; the full c=3 conclusion retains the two named inherited inputs.

**Still open:** connected defect, the allowed component counts at least five, arbitrary order61 nonexistence, and the user's original all58–61 goal. This PASS does not close that goal.
