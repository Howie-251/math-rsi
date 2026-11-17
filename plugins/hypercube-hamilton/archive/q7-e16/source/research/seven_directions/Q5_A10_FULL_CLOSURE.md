# Full Q5 A10: assembly from augmentation and three marked orbits

2026-11-01. ARIS proof-writer candidate; final independent acceptance pending.

## Claim

For every matching $F$ of $K(Q_5)$ with four holes of one parity and six
of the other, and every specified majority hole $v$, there is a simple
cycle on exactly $Q_5\setminus\{v\}$ containing every edge of $F$.
Every edge of the cycle outside $F$ is a cube edge. Required edges of
$F$ may be long or join vertices of equal parity.

## Status and dependencies

The proof below is a complete assembly conditional on acceptance of
the final-orbit GF(2) certificate package. The original theorem is not
weakened. Its dependencies are full A8, the accepted exact A10 geometry
classification, the first two accepted A10 orbit theorems, and the new
last-orbit forest/rank theorem. Independent review must discharge that
last dependency and inspect the assembly before marking full A10 true.

## Proof

Translate the cube by $v$. This is an automorphism preserving short
edges, arbitrary matching edges, and the specified omitted vertex;
after translation $v=0$ and its parity class is the even class.
Write the other majority holes as $Z$, $|Z|=5$, and the minority holes
as $W$, $|W|=4$.

If $z\in Z$ and $w\in W$ are short-adjacent, add $zw$ to $F$.
The resulting matching has five even and three odd holes and still
leaves $0$ free. Full A8 gives the required 31-cycle containing this
larger matching and omitting $0$. Relative to $F$ its one additional
required edge $zw$ is short, so this cycle proves the original claim.

Otherwise $Z\cup W$ is independent. The exact geometry classification
accepted in `Q5_HIGHER_HOLE_REDUCTION_REVIEW.json` contains 55 such
marked geometries. Under coordinate permutations they form exactly
these three disjoint orbits:

| representative $Z$ | representative $W$ | orbit size | positive input |
|---|---|---:|---|
| $3,5,6,15,23$ | $8,16,25,26$ | 30 | `A10_FIRST_ORBIT_REVIEW.json` |
| $3,5,6,15,23$ | $8,25,26,28$ | 20 | `A10_ORBIT2_REVIEW.json` |
| $15,23,27,29,30$ | $1,2,4,8$ | 5 | final-orbit forest/rank theorem |

The first theorem uses two forced closed matching sets with an odd
intersection. The second uses one forced closed set and a complete
canonical family with independently checked positive cycles. The third
uses legal short-complement forests whose endpoint-pairing rows have
full rank in the matching connectivity matrix. Each theorem quantifies
over every arbitrary matching on the complement of its marked hole set.

Choose a coordinate permutation taking the normalized instance to its
listed representative. Apply the relevant orbit theorem and invert
the permutation and translation. This preserves each required edge,
shortness of every new edge, simplicity, and the exact omitted vertex.
The augmentation case and the three orbits exhaust all inputs, so the
stated full A10 theorem follows once the listed inputs are accepted.

## Consequences of accepted full A10

Together with full A8, A10 discharges the two assumptions of
`Q5_HIGHER_HOLE_REDUCTION.md`, whose reduction and finite neighbor bound
were independently accepted in `Q5_HIGHER_HOLE_REDUCTION_REVIEW.json`.
Consequently every feasible Q5 imbalance-two avoid-one input holds;
every arbitrary $K(Q_5)$ matching with balanced holes has a spanning
path from any free root to every opposite-parity target, covered or
free, and a spanning cycle extension. All surviving new edges are short.
The zero-hole cycle case is the explicit perfect-matching import, and
the 32-hole endpoint case has no covered target, as checked in that
reduction. No infeasible 17-hole parity class is used.

These are Q5 auxiliary results. They do not by themselves discharge the
marked multiple-omission inputs in Q6. Complete ten-hole covered targets,
the complete 12/14/16/18-hole layers, and full P6 remain open.

## Required final audit

Verify all upstream final reviews and source hashes, the last-orbit
forest and rank certificates and the precise published rank theorem,
the exact disjoint 30+20+5 geometry cover, the augmentation and symmetry
steps, and the hypotheses of the already audited Q5 consequence theorem.
The complete Q6 goal must remain open in the resulting state.
