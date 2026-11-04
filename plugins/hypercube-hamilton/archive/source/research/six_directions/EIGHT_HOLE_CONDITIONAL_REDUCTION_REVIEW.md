# Eight-hole conditional reduction: independent review

Date: 2026-11-01. **PASS for the stated conditional reduction, relative to explicit imports.**
Reviewer route: ARIS proof-checker, user-selected GPT-6.1-sol / high.
`review_independence: same-family`; `acceptance_status: provisional`.
The reviewed draft, producer census and producer result are hashed in the accompanying JSON.
The draft and main research state were not changed by this review.

The checked conclusion is **A6 implies the complete Q6 eight-hole free-target theorem**,
and the stated nine-cut criterion handles the indicated covered targets. Conditional on A6,
full eight-hole P6 is equivalent to the additional R8-covered assertion. A6 and R8-covered
remain unproved here; full P6 remains unproved. No local FATAL, CRITICAL or MAJOR gap was found.

## Imported assumptions and dependency boundary

This review imports the perfect-matching extension theorem for arbitrary matchings of
K(Q5); N10 from `GENERAL_NEAR_PERFECT.md`; N14 from the initial lemma of
`TWO_ODD_HOLES_TRANSFER.md`; full A4 from `CANONICAL_A4_CLOSURE.md`; K4 from
`SIX_HOLE_MIXED_AND_GEOMETRY.md`, with its A4 assumption discharged by that closure;
and full six-hole Q6 P6 from `SIX_HOLE_CLOSED.md`. These inputs are not recursively
reproved or recertified in this audit. The full six-hole and A4 packages retain their
same-family/provisional assurance and finite-certificate dependencies.

The five-direction theorem is also imported: local `paper.txt`, Theorem 8, lines 189ff.
For c=0, the original short matching avoids a coordinate. Its free root excludes C1,
C2 and C3 (each requires covering the root), so its hypotheses hold. This audit does
not recertify that theorem's computer-assisted five-dimensional input.

A6 is an explicit additional universal hypothesis about arbitrary K(Q5) matchings,
not merely short or bipartite matchings, with hole parity counts 4 and 2 and any
prescribed majority hole omitted. All imported parity statements allow exchanging
the parity classes. Consequently global parity labels can be used on either face.

Dependency DAG: perfect/N10/K4 and N14/A4/A6 -> local endpoint lemma -> nine transfer
rows; full six-hole P6 -> preliminary augmentations; five-direction theorem -> c=0;
these reductions plus the geometry certificate and root-bridge argument -> all free
targets; nine-row complement -> R8-covered characterization. No use of eight-hole P6,
R8-covered, or a consequence of either occurs upstream. Historical open-A4 wording
in older imports does not supersede the explicitly selected closure dependency.

## Proof-obligation ledger

| ID | Application and hypothesis discharge | Result |
|---|---|---|
| L1 | Section 1, free y: adding ry is a matching, consumes two holes with parity sum h, and leaves 0,2,4 balanced holes. Perfect/N10/K4 supply a full circle; remove ry. | Closed modulo imports |
| L2 | Section 1, covered y: k=F(y), replace yk by kr. The holes replace r by y, hence imbalance h-epsilon(r)+epsilon(y)=2epsilon(y), with 2t unchanged and y free. N14/A4/A6 omits precisely y. Opening kr and restoring original ky gives the requested full path. | Closed modulo imports/A6 |
| L3 | Balanced 2/4/6-hole circle corollary: choose a short neighbor of a free root as target. A 32-vertex Hamilton path cannot already contain its endpoint edge; closing adds a permitted short edge. | Closed |
| P1 | A nonroot adjacent hole pair can be adjoined without covering u. Exactly six holes remain, so full six-hole P6 applies to the original prescribed endpoints. | Closed modulo import |
| P2 | Free v adjacent to u: adjoin uv, close a six-hole Hamilton path from another free root to its short neighbor, then delete uv. The enlarged matching really contains uv. | Closed modulo import |
| F1 | D uses only crossports and, when needed, the chosen original hole x; it is disjoint from M_A. For delta=0 the root port p is even, so p differs from odd v. | Closed |
| F2 | Removing D from the A path gives a path forest. Each crossport receives a different B endpoint. A covered v in X_A can be isolated when its D edge is deleted; its real crossedge restores its terminal segment. | Closed |
| F3 | For delta=1, D is nonempty and its removal separates u and v even if a D edge touches v. Thus rs joins distinct terminals. For delta=0, ur joins the free B root to a crossport, so its endpoints differ. | Closed |
| F4 | Bridge mirror y is internally covered: it is neither a hole (by independence and the explicit root exclusion) nor a crossport (its unique opposite-face neighbor is the free x). A nonterminal y yields exactly one M_B/R conflict. | Closed |
| F5 | In the conflict repair k is internally covered, d a crossport, and k,d,y are distinct. Thus kd forms a matching after removing yk and yd. Expansion restores both originals and the omitted y exactly once. | Closed |
| T0 | b=a+1, a=0,1,2: port imbalance b-a-delta is 0 or 1; D completion leaves A holes (a+1,a+1); after terminal closure B holes are (3-a,3-a). Every local hole total is 2,4,6. | Closed |
| TE | b=a, a=1,2,3: choose an even nonroot hole x; its odd mirror y is internal. A holes (a,a). Nonterminal repair plus rs/ur leaves (3-a,5-a), with majority hole y; use A6/A4/N14 at a=1/2/3. | Closed modulo A6 |
| TO | b=a+2, a=0,1,2: choose an odd hole x distinct from free v and with mirror y not u; A holes (a+1,a+1). Nonterminal B holes are (4-a,2-a), with majority y; use A6/A4/N14 at a=0/1/2. | Closed modulo A6 |
| TY | Terminal mirrors: TE,delta=1 has holes (3-a,4-a) plus q, allowing q-y by L1/L2; TE,delta=0 is balanced (4-a,4-a), allowing u-y. TO,delta=1 has (3-a,2-a) plus q, allowing q-y; TO,delta=0 has (4-a,2-a), allowing u-y. Root is free and y covered in each call. Totals are 2,4,6. | Closed modulo local lemma |
| RB | Section 6's failed odd-hole choice forces a=0,b=2,delta=0 and W intersect A={v,x}, x mirror of u. Pair all ports; c is even and at least 2. N10 gives x-v with exactly two odd holes. After deletion/attachment, its distinct terminal segments are u-r and s-v. M_B+R+rs has (4,2) holes including u; A6 omits u, and the terminal bridge restores it exactly once. | Closed modulo A6 |
| G | The independently implemented exhaustive free-hole census covers every remaining geometry after normalization, with no matching realizability restriction. Both canonical targets have zero uncovered geometries. | Deterministically verified |
| RC | Nine good rows and the eleven displayed bad rows partition all 20 (a,b) pairs. The four sequential branches exhaust free/covered targets after augmentation. Full eight-hole P6 implies R8-covered by specialization; under A6 the converse follows from this partition. | Closed |

In every transfer, the compressed edges occur in the local extending path/circle as
required edges. They can therefore be expanded, while rs or ur is deleted. All
surviving new edges are short: local extension edges and the selected short bridge.
Expansion of a single local path, with disjoint terminal segments, yields one global
Hamilton path; the argument is stronger than checking degrees alone.

## Independent finite check

Reviewer-owned `EIGHT_HOLE_CONDITIONAL_REDUCTION_REVIEW_check.cpp` uses set-bit
subset enumeration, 64-bit neighbor masks, and face-intersection masks. Its good-cut
test comes from the three algebraic transfer families, rather than the producer's
four-row predicate. `EIGHT_HOLE_CONDITIONAL_REDUCTION_REVIEW_check.py` compiles and
runs it, checks agreement with the producer's claimed source hash/counts, independently
verifies the residual matching, and checks the finite row partition and hole totals.
Both checkers are standalone and do not invoke the producer's census implementation.

Run: `D:\anaconda\python.exe EIGHT_HOLE_CONDITIONAL_REDUCTION_REVIEW_check.py` in this directory.
Compiler: `D:\mingw64\bin\g++.exe -O3 -std=c++17`. Exit code: 0.

| normalized target | geometries | no good cut | only root-bridge good cuts |
|---:|---:|---:|---:|
| 7 | 1,300,674 | 0 | 31 |
| 31 | 1,287,690 | 0 | 30 |
| total | 2,588,364 | 0 | 61 |

The last column counts geometries, without asserting they are realizable matchings.
It shows why ignoring the root-bridge boundary would leave the geometry argument incomplete.

Coverage justification: translation sends the chosen free root to 0, flipping parity
if necessary. An opposite-parity free target then has distance 1,3,5. The distance-1
case was proved separately. Coordinate permutations normalize distances 3 and 5 to
7 and 31. Enumerating every nonzero even triple Z not neighboring v, followed by
every odd triple outside v and all neighborhoods of Z, gives exactly every remaining
independent Z union W. Same-parity adjacency is impossible. Root-to-other-hole
adjacency is deliberately allowed. Unordered subset enumeration has no repetitions,
and it omits no geometry satisfying the stated preprocessing. The transfer proof
works for every short matching with such holes; matchings need not be enumerated.

The concrete residual witness was independently checked as 28 disjoint short edges,
with exactly holes {0,6,17,53,11,35,41,47}, covered target 4, independent nonroot holes,
and all six directions present. Its cut rows are
(1,0),(2,1),(2,1),(3,1),(1,4),(2,1), all bad. Thus it survives even the optional
six-direction restriction. It obstructs universal coverage by the nine-cut scheme;
it is not a counterexample to Hamilton extension or to A6 sufficiency by another proof.

## Adversarial edge cases and remaining limits

Checked candidates included an arbitrary long/same-parity required edge in each local
application; free versus covered y in the local lemma; a covered v whose partner crosses
the cut; empty D for delta=0; the smallest nonempty D for delta=1; either parity of the
other terminal q; y terminal versus nonterminal; root-other-hole adjacency; c=0; and
all 61 root-bridge-only geometries in the census. No contradiction to the claimed
conditional argument was found. These attempts support but do not replace the proofs
and finite coverage argument above.

There are no open local proof gaps in the stated conditional claims. The open obligations
are the assumed A6 and the separately identified universal R8-covered endpoint statement.
No claim that A6 is logically independent of R8-covered was established. Closing even
both would still leave the 10--18-hole levels needed for full P6.
