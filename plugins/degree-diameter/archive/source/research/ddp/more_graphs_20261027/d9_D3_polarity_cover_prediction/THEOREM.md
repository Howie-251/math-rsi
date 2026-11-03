# The actual 585-point source has no edge-preserving diameter-3 enlargement

Let G be the specific 585-vertex, 2600-edge graph saved as
source585.implicit_adj.txt, reused from the project's earlier
polarity585_replication source. Its primary published adjacency is
[n585d9k3.txt](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD3/n585d9k3.txt).
This theorem concerns this literal graph, not all graphs of order585.

**Theorem.** There is no finite simple graph J of maximum degree at
most9 and diameter at most3 that contains all585vertices and all2600
edges of G and has at least one additional vertex. Arbitrary edges
among new vertices and arbitrary additional edges between old vertices
are allowed in this statement. Thus every finite order N≥586 is
excluded for this specific old-edge-preserving extension rule.

The theorem does not exclude deleting or changing old edges, another
source, or arbitrary degree-9 diameter-3 graphs. It is not a general
upper bound on N(9,3), an optimality claim, a claim of historical
priority, or a completed Lean theorem.

## Actual finite premises

The existing source partition check, cited in SOURCE.json, establishes
65vertices of degree8 and520vertices of degree9. Let P be the former
and T the latter. The new targeted check in RESULT.json, BLOCKS.json
and PORT_R2.json establishes:

1. The closed one-neighborhoods of P cover every old vertex exactly
   once. In particular P is independent, and each t in T has a unique
   old port neighbor p(t).
2. For every p in P, R2_G(p) intersects P only in {p}. Thus distinct
   ports have no old path of length at most2. The inherited published
   source D3 makes their old distance exactly3, although the proof
   below needs only the checked separation.
3. The520literal sets S(t)=P intersect R2_G(t) have size9, are distinct,
   and contain each of the43680triples of P exactly once. They form
   a3-(65,9,1) design. Consequently each port belongs to72sets and
   each pair of ports belongs to9sets.

The finite check expanded65radius-2 neighborhoods and counted the
43680triples, using0.050057112CPU seconds. It reused the saved actual
source and prior degree partition; it did not redownload the source,
repeat its all-source diameter check, or search any helpers. These
facts discharge precisely the premises of the preserved prior
CONDITIONAL_COUNTING_LEMMA.md. PROOF_CHECK.md independently checks
the paper deduction.

## Proof

Suppose such J exists, and write X for its nonempty new-vertex set.
All old vertices outside P are already saturated, so every new edge
incident with an old vertex uses P. A port has only one free slot.
In particular, every additional old–old edge would have to join two
ports and consume their slots.

Fix any x in X and any p in P. On an x-to-p path of length at most3,
take its last new vertex y, followed by its first old vertex q.
The edge yq consumes q's sole free slot. At most two steps remain,
all within old vertices. The next step cannot use an additional
port–port edge at q, whose slot is already consumed. Any original
step from q goes to a saturated nonport, where an additional edge
is also impossible. If q differs from p, the suffix therefore would
be an original path of length at most2 between distinct ports,
contradicting the actual radius-2 separation. Hence q=p.

Every one of the65ports must therefore have a new neighbor. All old
free slots are consumed by new–old edges, leaving no possible
additional old–old edge. This conclusion did not assume the absence
of such edges in advance.

Let H=J[X], and choose a vertex x of minimum H-degree r. Then
0≤r≤9. Its set A of attached old ports has size a≤9−r. Each of its
r H-neighbors has H-degree at least r and attaches to at most9−r
ports. Let B be the union of these neighbors' port attachments.
Then |B|≤r(9−r).

Consider an old nonport target t. A path of length at most3 from x
either enters the old graph directly at A and uses at most two
further old edges, or first takes one H-edge, enters at B, and uses
one further old edge. Taking two H-edges leaves time only to reach
an old port, not t. An old port cannot provide a different new
neighbor for a reentry shortcut: its only new edge is already fixed.
Consequently t must satisfy

    A intersects S(t), or p(t) belongs to B.

Apply third-order Bonferroni to the first class. The actual design's
single, pair and triple multiplicities are72,9,1, respectively, so

    |{t in T : S(t) intersects A}| <= U(a),
    U(a)=72a−9*C(a,2)+C(a,3).

For integer0≤a≤8, its increment72−9a+C(a,2) is positive. Thus the
first class has at most U(9−r) vertices. Each port has exactly8old
nonport neighbors, so the second class has at most8|B|≤8r(9−r)
vertices. Counting possible overlap twice only weakens this upper
bound. The number of old nonports that x could reach is at most:

| r | U(9−r) | 8r(9−r) | Total |
|---:|---:|---:|---:|
| 0 | 408 | 0 | 408 |
| 1 | 380 | 64 | 444 |
| 2 | 350 | 112 | 462 |
| 3 | 317 | 144 | 461 |
| 4 | 280 | 160 | 440 |
| 5 | 238 | 160 | 398 |
| 6 | 190 | 144 | 334 |
| 7 | 135 | 112 | 247 |
| 8 | 72 | 64 | 136 |
| 9 | 0 | 0 | 0 |

The maximum462 is below |T|=520. At least58old nonports cannot be
within three steps of x, contradicting the diameter bound. This
proves the theorem for every finite number and arrangement of new
vertices, including arbitrary proposed old–old additions.

## Constraint on future order-586 constructions

Independently of this particular source, a degree-at-most8 root in
any maximum-degree9 graph has at most

    1+8+8*8+8*8*8 = 585

vertices within distance3. Therefore a maximum-degree9, diameter-3
graph on586vertices must be9-regular, with2637edges. More generally
the same regularity requirement holds at every order above585.
This is a construction constraint attached to the present result,
not a separate construction method. Since the theorem rules out
retaining the entire actual source, future source-based attempts
must change old edges as well as satisfy that regularity requirement.
