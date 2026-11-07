# Authorized one-shot complete order18 D7 with tau(red-six)>=5

Saved before implementation of the new decision. The main agent explicitly
authorized this single decision only if the published geometric D26 fixture
does not already have tau five. The completed calibration found D7-valid,
2506 red-six paths and unique minimum cover {25}, tau one. Thus the condition
for this one new finite decision is met. The old D30 decision is not rerun.

The target contains all C(18,3)=816 triple colors, all C(18,4)=3060 packet
conditions, no blue-five, no weak-seven (same actual ends, length sum nine,
shared interiors allowed), and no actual EndR5/SrcB4 intersection. No R7 is
entailed by no weak7 and the same-endpoint blue-two vacuous path. There are
no root, endpoint-set, E-cardinality, partition or template restrictions.

The unchanged copied D7 base builder supplies the full negative-domain CNF.
Its forward actual-path=>reach flags prohibit paths but do not witness new
positive existence. New positive witnesses are separate exact H[S] flags,
one for every one of the C(18,6)=18564 six-subsets:

`H[S] <-> AND(red[t] for every one of the20 triples t subset S)`.

Encode all20 clauses `not H[S] OR red[t]` and the reverse clause
`H[S] OR OR(not red[t] for t subset S)`. Complete packets imply a
monochromatic consecutive-triple path induces all same-color triples, by
successive deletion of internal points using monochromatic first/last
packet entries. Therefore H[S] exactly means actual red-six on S.

For every four-subset D, add the full clause
`OR(H[S] for ALL six-subsets S of V minus D)`.
There are3060 such clauses, each of length C(14,6)=3003. No selected path
family or fixed tail is substituted. The layer has9189180 literal occurrences.
This is equivalent to tau>=5: a cover of size<=4 extends to a four-set cover,
and every four-set not being a cover means some actual R6 survives its deletion.

Soundness: every actual forbidden D7 path/junction forces a prohibited base
flag by induction, so the color projection is D7. Each positive H chosen by
a deletion clause certifies every one of its20 red triples and hence a
real disjoint R6. Every four-set therefore fails to cover all actual R6.

Completeness: for any full D7 coloring with tau>=5, extend all old flags by
actual path existence, and all H flags by actual red-six clique existence.
All base implications/prohibitions hold, all H equivalences hold, and every
deletion clause has a true witness. Thus the existential auxiliary projection
is exactly the stated target. No old one-way reach is used as a positive flag.

Before launch, finite deterministic H6 gate controls check a known actual
geometric red-six, all-red colors, and every single-blue perturbation with
both possible flag values. The valid D26/tau1 and actual R11/tau2 controls
remain positive D7/negative criticality examples. These are engineering
selfchecks, never independent mathematical review or formal acceptance.

One controlled external designated AE process receives max180 seconds,
3GiB and its own process group. No restart, order change or budget increase.
Complete SAT is checked clause-wise and by the independent color-only path
checker; all actual R6 and all3060 four-deletion conditions are checked, and
all minimum transversals are enumerated when bounded execution permits.
The existing full D7 tau<=5 theorem then identifies a valid tau>=5 witness
as tau exactly five. SAT has no automatic H49/50 embedding or numerical bound.

Complete UNSAT needs retained source/CNF/proof bindings and a bounded actual
proof check where a checker is available. Even checked UNSAT excludes only
this exact order18 target. D7 is hereditary but tau>=5 is not; no inference
about smaller/larger orders or D<=29 follows from this finite negative result.
Timeout remains undecided. No partial-proof checking or extra solve is allowed.
