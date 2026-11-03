# Independent attack: fixed q2 × q8 product, arbitrary free edges and helpers

2026-11-01. **The predicted necessary bound is supported under the stated
classical polarity-product interface.** In particular it excludes every
nonempty helper batch at caps27..30 in this fixed mandatory-edge-preserving
family, even with arbitrary additional free–free edges. The strict cap30
shortfall is2 targets. Cap31 is not excluded by this bound; no construction or
search at31 follows from that fact.

The original prediction was saved in `PREDICTION_AND_PROOF.md` before this
attack. This note checks the assumptions and every short-route type; one tiny
integer scalar check is recorded in `INDEPENDENT_RESULT.json`. No8775 graph,
field/polarity table, geometry calculation, BFS, Lean, solver, network query or
paid review was run. A complementary paper-only check by
`/root/f9_56862_independent` independently supports the2/6 factor bounds and the
clone reduction below, with zero tools or computations.

## Exact inherited interface and the saturation claim

Let A and B be the genuine looped polarity quotients of generalized
quadrangles GQ(2,2) and GQ(8,8). Their15 and585 vertices have adjacency-row
sizes3 and9, where a loop counts once. Their absolute sets O_A and O_B are
exactly the looped vertices, of sizes5 and65. This uses the published
classical existence and polarity interface, not a newly generated finite
geometry. The cached primary text
`../../public_baseline_audit/arxiv_2608_27253v2.txt` contains §7.1,
Propositions7.4–7.6, Corollary7.9, Lemma7.10 and §7.7; the online primary is
[Isham et al.2026v2, §7](https://arxiv.org/html/2608.27253v2#S7).

Distinct absolute vertices in either factor have no edge and no common
neighbor, including in the looped quotient. This is also derivable without a
finite table: an edge between two absolutes would give a4-cycle in the
incidence graph, and a common third neighbor would give a6-cycle. Both
contradict the generalized-quadrangle incidence girth8. Loops at the two
absolutes do not supply a common neighbor, because that would already require
the forbidden edge. Thus the distance condition in the primary replication
discussion remains valid with loops retained for this calculation.

Take S to be A tensor B with its product self-loops removed. Before removal
every adjacency row has3·9=27 distinct entries. A product self-loop occurs
exactly at C=O_A × O_B, so each of325 C vertices has simple degree26 and each
of the other8450 old vertices has degree27. Two distinct C vertices differ in
an absolute coordinate. A common product neighbor would therefore supply a
forbidden common factor neighbor. Likewise no distinct C vertices are
adjacent. Hence their26-element open neighborhoods are disjoint subsets of
U=V(S) minus C. Their total size325·26=8450=|U| proves they partition U.

Append exactly r copies of every full original N_S(c), r≥0, retaining every
source and clone edge. At cap Delta=27+r every U vertex receives exactly r
new mandatory clone edges and is saturated. The set F consists of old C and
the325r clones. Every F vertex has mandatory degree26, all its mandatory
neighbors are old U, and it has at most r+1 remaining slots. There are
initially no F–F edges. Thus any genuinely new edge among existing vertices
has both ends in F; every new helper can meet only F or another helper. In
particular no new helper can meet the hard targets

    X=(V(A) minus O_A) × O_B,       |X|=10·65=650.

Deleting product self-loops is important for these degrees and does not
increase any old-route count. The construction and barrier here are statements
about this published abstract source interface; no literal edge file has been
claimed to exist locally.

## Why each actual free pin has the2/6 mandatory profile

For c=(a,b) in C, a one-step old target in X must have second coordinate b:
distinct B absolutes are not adjacent. The A row of a contains its own loop
and exactly two nonabsolute neighbors. Consequently

    |N_S(c) intersect X| <= 2.

For an old walk from c of length at most2 ending in X, its B projection is a
factor walk of the same length, possibly using a factor loop. It still ends
at b: two different absolutes cannot be linked in one or two steps. In A,
the nonabsolute endpoints after at most2 steps are among the two immediate
nonabsolute neighbors of a, together with at most two further nonabsolute
neighbors from each. Each intermediate nonabsolute row already spends one
entry returning to a and has only two entries left. The possible loop at a
contributes the already counted immediate neighbors. Thus the union has size
at most2+2·2=6. No exact6-element ball is required.

A clone has the same old-neighbor list as c. A mandatory two-edge walk from
that clone to an old X vertex replaces its initial clone by c and becomes an
old S walk with the same endpoint. A two-edge walk ending at another clone
does not end in X; a clone has no mandatory clone neighbor. Original C
vertices cannot be adjacent to a mandatory clone either, since all clone
neighbors are in U. Therefore repeated clones do not create additional
mandatory two-step endpoints in X. Both bounds apply uniformly to every f
in F, including old centers and every copy.

These bounds concern mandatory source/clone edges. Later F–F edges are
explicitly counted next, rather than silently included in a fixed old ball.

## Exhaustive helper-to-X routes of length at most3

Let H be a finite nonempty batch of new helper vertices and let the final
graph be finite and simple, with every mandatory edge retained and maximum
degree at most Delta. For h in H write p_h=|N(h) intersect F| and
d_h=|N(h) intersect H|. Saturation gives p_h+d_h≤27+r. Multiple helpers may
share pins or use many copies of one base center; no owner uniqueness is
assumed.

Every h-to-X walk of length at most3 begins in one of two ways:

1. **h–f, f in F.** A direct mandatory suffix or a two-edge old suffix reaches
   at most6 targets in total. If the next edge is an added F-peer edge f–f',
   the only remaining edge f'–x must be mandatory, and reaches at most2 X
   targets for that peer. The edge h–f has already consumed one of f's at
   most r+1 extra slots, leaving at most r F peers. Any other helper
   neighbor of f reduces the available peers further. A suffix through a
   helper cannot end at saturated X. Thus this particular first pin covers
   at most6+2r targets.
2. **h–g, g in H.** With two edges left, g cannot meet U, and another helper
   cannot finish at X. The only possible suffix is g–f–x with f in F,
   covering at most2 targets for each actual pin of g. An F-peer after that
   pin would require four edges from h, so is not an omitted three-route.

This covers shorter walks too, and backtracking does not create another
type. In particular h–f–g–x and h–g–g'–x are impossible because x is
saturated. Hence diameter at most3 of the final graph necessarily gives

    650 <= (6+2r)p_h + 2 sum_{g adjacent to h in H} p_g.       (1)

It is a union upper bound, so overlap, repeated base classes and repeated
targets only weaken coverage. Both endpoint degree costs have been respected:
the actual helper–free edge pays one free slot at f, and each peer pays one
there too. Enforcing the peer's other endpoint cost or total free-slot budget
could only strengthen this necessary obstruction; ignoring those extra global
constraints cannot invalidate it.

## Summing eliminates arbitrary helper ownership

Put t=|H|>0. Since the helper graph is undirected, sum_h sum_{g adjacent h}p_g
=sum_g d_g p_g. Summing(1) therefore gives

    650t <= 2 sum_h p_h(r+3+d_h)
         <= 2 sum_h (27+r-d_h)(r+3+d_h).

For every integer d, the exact identity is

    (27+r-d)(r+3+d) = (r+15)^2 - (d-12)^2.

Its maximum for0≤d≤27+r is at d=12, giving

    650 <= 2(r+15)^2.                                    (2)

Actual helper degrees additionally obey d≤t−1 and actual free pins have
finite supply. Removing these restrictions only enlarged the upper bound,
so the maximization remains a valid necessary condition for any batch size.

|r|cap|maximum coverage bound|650 minus bound|consequence|
|---:|---:|---:|---:|---|
|0|27|450|200|no nonempty helper batch|
|1|28|512|138|no nonempty helper batch|
|2|29|578|72|no nonempty helper batch|
|3|30|648|2|no nonempty helper batch|
|4|31|722|−72|this inequality does not exclude it|

The single scalar script checks these five integer maxima and the identity
for every integer helper degree in their respective cap ranges. It builds no
graph and does not test feasibility of equality or of the r4 case.
Its sole execution exited0 under a5-second CPU limit; `time.process_time`
reported0.0 seconds for the tiny checked loop. This is a below-resolution
timing receipt, not a claim that preparation or execution had zero cost.

## Consequence and limits

The supported prediction justifies stopping blind append attempts at27..30
on this8775 source and its complete uniform copies, while allowing arbitrary
F–F additions and any nonempty helper batch. It does not forbid adding only
F–F edges without new vertices. A proposal at31 would need an actual joint
pin/helper/peer rule; favorable upper-bound numbers alone supply no such
rule. No such run is started.

Omitting or rewiring mandatory source/clone edges, nonuniform or incomplete
copying, changing the source or center set, and other graph families are not
excluded. This is not a global N(Delta,3) bound, not a new graph or kernel
proof, and not a public priority claim. It is separate from the existing
three-graph A/B/C review scope; those review outcomes are not evidence for
this new lemma. No root count, Wiki or frozen artifact was modified.
