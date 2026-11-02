# Proof obligations for the actual quotient lift exclusion

This is the compact ledger for one same-family/provisional audit. Locations
refer to `CYCLIC5_QUOTIENT_TWELVE_PENTAGONS_EXCLUSION.md` as read (289 lines).

## Quantified claims and assumptions

For every simple graph G on 60 vertices with a free C5 automorphism whose
degree quotient equals the saved M, G cannot simultaneously have degree eight
and diameter at most two. The quantification includes every invariant edge
selection realizing that M, hence every allowed voltage set and either
internal step. If only maximum degree eight is specified, M's row sums already
give degree exactly eight.

For every graph made of two groups of six disjoint C5s, with exactly one
perfect matching between each opposite pair of C5s and every matching sending
cycle adjacency to nonadjacency, its diameter is greater than two. Such a
graph is simple, has 60 vertices and is 8-regular. All 36 orientation signs
and all translations are allowed. No fixed free C5 action is assumed for this
second claim.

A directly inherited structural corollary was subsequently checked from
the parent's proposed statement: for every target quotient M whose defect
quotient is two K6 components, if each corresponding six-orbit diagonal
block of M is exactly a unit C5 plus an isolated diagonal-two orbit, no
target lift exists. The target is again simple, order60, degree8,
diameter at most two, under a free C5 action. No additional restriction
on M's cross-block entries is needed. The combination of both structural
hypotheses is essential to the proved scope; the ledger makes no exclusion
claim from `D=2K6` alone.

The assumptions used in the first reduction are simplicity, order 60,
8-regularity, diameter at most two, and the specified equitable quotient.
The free C5 action is used to describe the unit-interface cycle lift and
isolated orbit steps. Once twelve actual pentagons and anti-cycle matchings
are obtained, only that architecture and diameter at most two remain in use.

## Typed notation

`A,B : 60×60 integer symmetric matrices`, actual adjacency and defect.
`M,D : 12×12 integer symmetric matrices`, degree and defect quotients.
`U,V : disjoint six-element sets` of original orbit labels.
`R,T : 30×30 binary symmetric matrices`, actual half-graph adjacencies.
`X : 30×30 binary matrix`, cross adjacency with row/column sums six.
`C_p : p×p cycle adjacency`, p in {5,25}; `C=C_5` in §§4–5.
`Y : p×q binary block` in §3; it is distinct from the normalized voltage
matrix named Y in the imported K6,6 proof.
`P,Q_j,W : 5×5 permutation matrices` after their respective derivations.
`epsilon : 6×6 matrix over {−1,+1}`; `a : 6×6 matrix over F5`.
`eta : primitive 25th complex root`; `zeta : primitive fifth complex root`.
`Z : 5×5 complex matrix`; `w : nonzero 1×5 complex row vector`.
`*` denotes conjugate transpose; `I_n,J_(p,q)` are identity/all-ones matrices.
There is no symbol drift affecting an inference; the imported proof's names
are used within its own scope.

## Dependency DAG and discharged microclaims

`target + actual M -> B,D and half structure -> Sylvester equation`
`cyclotomic lemma + Sylvester equation -> no C25`
`no C25 + Sylvester equation -> anti-cycle matchings`
`diameter coverage + anti-cycle matchings -> dihedral covering lemma`
`dihedral covering lemma -> sign switching classification`
`all+ -> new free C5 action -> old K6,6 §§2–4 -> contradiction`
`single− + covering lemma -> character null vector and positive Gram -> contradiction`.

The old K6,6 argument does not depend on the present theorem. The broader
architecture enters directly at the anti-cycle matching node. There is no
dependency cycle.
The structural corollary enters at MC1–MC3 with the stated two hypotheses
replacing the saved-data check; all later nodes are unchanged.

| ID | Context and goal | Rule and discharged conditions |
|---|---|---|
| MC1 | Target and M imply B cross-block zero; lines 23–51 | Actual defect nonnegative; exact quotient verified from saved data; zero aggregate of nonnegative integers. |
| MC2 | Half quotient implies 6C5 or C5+C25; lines 53–59 | Equivariant unit matchings, total voltage of order 1 or5; each allowed internal step generates F5. |
| MC3 | Block adjacency implies RX+XT+X=J; lines 61–68 | Direct block multiplication; MC1; no missing diagonal/cross term. |
| MC4 | Five roots with paired exponents summing to zero force Phi25; lines 72–106 | Zero exponents excluded; 5-Eisenstein; monic division; degree at most24 and coefficient sum5. |
| MC5 | C25 component contradicts defect row budget; lines 110–135 | Finite Fourier bases; MC4 excludes primitive-mode resonances; period5 gives four distinct nonadjacent equal-neighborhood partners. |
| MC6 | Opposite C5 block is an affine anti-cycle matching; lines 139–164 | Invertible C+3I; binary row/column sums1; conjugation to complement; all isomorphisms of C5 are dihedral. |
| MC7 | Six routes permit rotation counts only 0,1,5,6; lines 168–198 | Diameter covers every same-half cross-pentagon pair; excess permutation commutes C; invertibility of 2 in F5; adjusted-count nonnegativity explicitly established. |
| MC8 | Sign matrix switches to all+ or one−; lines 202–219 | Allowed distances stable under d↔6−d; coordinate reversals arbitrary; first-row normalization; row and column constraints both used. |
| MC9 | All+ is impossible; lines 223–234 | New automorphism free and graph-preserving; its degree quotient exactly 2I+A(K6,6); old §§2–4 checked directly. |
| MC10 | Single− is impossible; lines 238–272 | MC7 applies to row0/regular and regular/regular routes; inverse of2 is3; all tail sums equal in F5; character null vector conflicts with ZZ*=5I. |

All obligations above were discharged. No asymptotic/limit-order map is
needed: the proof concerns fixed finite graphs, finite-dimensional matrices,
and exact finite sums. Focused counterexample attempts and the input check are
recorded in `PROOF_AUDIT.md`.
