# Authorized complete D7 order-30 decision

This specification precedes implementation. Authorization: main agent's explicit
2026-10-27 instruction, one order-30 AE decision with a 300-second maximum;
no restart or expanded budget. Existing artifacts and jobs remain untouched.

## Exact projected domain

All 4,060 increasing triples on the actual ordered vertices `0,...,29` receive
red/blue colors. Every one of the 27,405 four-vertex packets, ordered as
`abc,abd,acd,bcd`, has at most one color change. There is no blue-five path,
no weak-seven (opposite-color paths with the same actual endpoints whose
vertex counts sum to nine; shared interiors are allowed), and no actual
vertex simultaneously ending a red-five path and starting a blue-four path.
There are no partition, root, geometry, template, E-set, or criticality
requirements. Red-seven exclusion is permitted as the D7 consequence supplied
by the main mathematical specification and is recorded separately below.

## Forward reach encoding and projection proof

Triple variable `x[a,i,j]` is true for red. For each color `c`, actual first
vertex `a`, last pair `i<j`, and feasible length `l>=4`, introduce a flag
`P_c[a,i,j,l]`. Feasibility is `a<i<j` and `i-a>=l-2`.
The length-three reach literal is exactly the signed triple color literal;
length-two paths are true for all actual pairs. For every feasible predecessor
`h<i`, add the implication

`P_c[a,h,i,l-1] AND color(h,i,j)=c => P_c[a,i,j,l]`.

For length four, the predecessor is the exact length-three triple literal.
Reach lengths are red four through seven and blue four through five. Force
every blue-five reach and every red-seven reach false.

For `R5,R6,B3,B4`, endpoint flags `Q_c[a,j,l]` receive an implication from
every reach literal with that first/last vertex. For B3 this is each actual
triple; for longer paths it is each relevant last-pair flag. Prohibit
`Q_R[a,j,5] AND Q_B[a,j,4]` and
`Q_R[a,j,6] AND Q_B[a,j,3]`. These are all nonredundant weak-seven cases
under no B5/no R7; every other length-sum-nine pair contains B5 or R7.
No disjoint-interior condition occurs.

Every red-five reach implies `D[j]`; every blue-four reach implies `S[a]`.
For every actual vertex v add `not D[v] OR not S[v]`.

Soundness of projection: by induction on path length, every actual monochrome
path forces its last-pair reach flag. The length-three base is its actual
color, and the final consecutive triple triggers the predecessor implication.
Consequently every actual endpoint witness forces Q, and every actual D/S
witness forces its vertex flag. The false reach flags exclude B5/R7; the Q
clauses exclude every weak-seven possibility; the D/S clauses exclude the
actual forbidden vertex intersection. Packet clauses enforce every packet.
Thus every CNF model projects to an element of the stated D7 domain.

Completeness: for an arbitrary coloring in the stated domain, set every P to
actual existence of the indexed monochrome path, every Q to actual
same-endpoint existence, and D/S to actual end/source existence. Every forward
implication then holds by appending the matching final consecutive triple.
All prohibitions hold by the assumptions and their supplied no-R7 consequence.
The canonical actual-reach extension therefore satisfies the CNF. Unnecessary
reverse implications cannot exclude any coloring and are omitted; auxiliary
flags are not used as exact counts or as semantic evidence.

## Independent semantic checks and interpretation

The SAT checker uses only the complete triple coloring. It recomputes every
packet and all longest monochrome paths by a separate fixed-first/last-pair
maximization recurrence over all predecessor triples, with concrete witnesses.
It checks maximum blue/red lengths, the two largest same-endpoint color
lengths, and actual EndR5/SrcB4. It independently enumerates all relevant small
subsets for fixture controls before the decision. At order 30, it enumerates
all red-six subsets for the red-six path hypergraph, computes a minimum vertex
transversal without assuming a matroid, and preserves explicit transversals
and all minimum ones when tractable. Any use of scoped b25/tau5 is recorded
as an existing dependency, never as a new acceptance.

SAT requires both clause-wise validation of the solver assignment and the
independent coloring check. UNSAT requires a nonempty retained proof with
fresh source/CNF/proof binding, and any bounded checker outcome is recorded
separately. Timeout/unknown is inconclusive. There is no independent review,
formal acceptance, or global bound update from selfchecks or raw status.
