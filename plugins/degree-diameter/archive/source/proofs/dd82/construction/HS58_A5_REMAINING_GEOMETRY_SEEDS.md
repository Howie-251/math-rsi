# Actual a5 seeds for adjacent and crossing HS deletion pairs

Date: 2026-10-12. Two complete 58-vertex, 232-edge, eight-regular
graphs were constructed for the two requested deletion geometries.
Both use exactly five original-nonedge additions and catalog type 3
on the eight new vertices. Neither is a target: their independently
checked diameters are three. The crossing-deletion seed has 72 bad
pairs; the adjacent-deletion seed has 94.

No SAT, auxiliary enumeration, or iterative optimization was run.
Each old core and its deletion-endpoint attachments were specified
explicitly, followed by one exact minimum-cost capacity flow for the
remaining singleton attachments. The flow minimizes the number of
old-old bad pairs affected by those singleton choices, subject to
all remaining new-vertex degree capacities. It does not claim to
minimize the full graph's bad-pair count or optimize over old cores.

## Common input and exact construction

The program uses the existing explicitly checked HS50 edge table,
and confirms both original deletion sets are actual Q edges:

* Adjacent: D={(0,1),(0,4)}.
* Crossing: D={(0,1),(2,3)}. The unique retained Q edge between the
  two deleted edges' endpoints is (1,2).

In both seeds H is the stored canonical type-3 representative:

```
02,03,04,05,06,07,12,13,14,15.
```

Its only internal bad pairs are {1,6} and {1,7}. New vertex labels
in the expanded graph are 50 through 57. Its old-neighbor capacities
are (2,4,6,6,6,6,7,7), totaling 44. These capacities and each old
vertex's row degree p_x=1+d_D(x)-d_A(x) are enforced exactly by the
saved construction. The chosen deletion-endpoint ports already cover
both bad H pairs, so neither full graph has a new-new bad pair.

Source and full results:

* [Construction source](../../../computations/dd82/construction/hs58_a5_remaining_seeds.py).
* [Resources and concise results](../../../computations/dd82/construction/hs58_a5_remaining_seeds_run/result.json).

## Adjacent deletions: a capacity-valid core with unavoidable old failures

The five additions are

```
(1,45), (25,29), (30,34), (35,39), (40,44).
```

They are original HS nonedges. The addition at deleted leaf 1 lowers
its port count, so this construction does not belong to the already
excluded branch in which all three deletion endpoints keep their
maximal ports. The chosen endpoint attachments, in new labels 0-7,
are

\[
B_0=\{1,6,7\},\qquad B_1=\{1\},\qquad B_4=\{1,6\}.
\]

The nine zero-port vertices are
{25,29,30,34,35,39,40,44,45}. Their Q-induced graph is empty. Each
has at least eight total ports among its M neighbors: the four
vertices 25,30,35,40 have nine, the four 29,34,39,44 have eight,
and 45 has ten. Thus this old core passes the zero-port capacity
test before assigning any singleton color.

Nevertheless the following five old pairs are unrepairable by any
attachment assignment with this core:

```
(1,25), (1,30), (1,35), (1,40), (4,45).
```

For q in {25,30,35,40}, the unique old Q path q-0-1 is broken.
Vertex q has no new port. Its added partner belongs to N_Q(4) and
is not adjacent to 1, while 1's added partner 45 is not adjacent
to q because both lie in N_Q(0). No old repair exists. Likewise
45-0-4 is broken, and the only added edge at 45 leads to 1, which
is not Q-adjacent to 4. The zero port at 45 prevents a new repair.

The singleton flow has objective value zero: it repairs every other
old-old pair requiring a new common neighbor for these chosen
endpoint ports. The resulting complete graph therefore has exactly
five old-old bad pairs, plus 89 old-new bad pairs, totaling 94.

* [Full graph and attachments](../../../computations/dd82/construction/hs58_a5_remaining_seeds_run/adjacent.seed.json).
* [Independent BFS with all 94 bad pairs](../../../computations/dd82/construction/hs58_a5_remaining_seeds_run/adjacent.seed.verification.json).
* [Old-core witnesses, flow data, and all old-new route sets](../../../computations/dd82/construction/hs58_a5_remaining_seeds_run/adjacent.analysis.json).

## Crossing deletions: exact zero-pair repair, then a column bottleneck

The five additions are

```
(25,26), (30,31), (35,36), (42,43), (47,48).
```

This matching avoids all four deletion endpoints, so all four retain
two ports. Its ten zero-port vertices form an independent set in Q.
Each zero vertex has exactly one Q neighbor among the four deletion
endpoints. Each added pair joins the neighbor cells of opposite
ends of one deleted edge. Thus the matching obeys the partner-cell
repair condition in
[the saturated disjoint zero-set lemma](HS58_SATURATED_DISJOINT_ZERO_SET.md).
Every zero vertex has total neighboring port capacity exactly eight.
There is no old bad pair with a zero-port endpoint: the explicit
matching repairs all such lost routes.

The endpoint ports were chosen as

\[
B_0=B_3=\{1,6\},\qquad B_1=B_2=\{1,7\}.
\]

All old-old demands between these endpoints are covered. However,
these fixed port sets have a precise capacity bottleneck. New label
1 has old capacity four, already filled by the four endpoints.
The six ordinary old vertices {4,28,33,38,40,45} must lie in
B_1 or B_2 to repair their respective lost old routes; those sets
are both {1,7}. All six therefore need label 7. Together with the
two existing incidences at endpoints 1 and 2 this demands eight
old neighbors for label 7, whose capacity is only seven.

The exact flow objective is consequently at least one, and the
actual flow attains one. Its only old-old bad pair is (1,40).
The complete graph has 71 further old-new bad pairs, giving 72 in
total. This bottleneck is a statement about these chosen endpoint
ports, not a proof that the old core or crossing-deletion family
has no other port assignment.

* [Full graph and attachments](../../../computations/dd82/construction/hs58_a5_remaining_seeds_run/cross.seed.json).
* [Independent BFS with all 72 bad pairs](../../../computations/dd82/construction/hs58_a5_remaining_seeds_run/cross.seed.verification.json).
* [Old-core witnesses, exact flow objective, and route sets](../../../computations/dd82/construction/hs58_a5_remaining_seeds_run/cross.analysis.json).

## Resources and the concrete next obligation

The complete parent construction used 0.015497 CPU seconds. Independent
BFS processes used 0.060621 CPU seconds. Total wall time was 0.185944
seconds on one pinned CPU, below the five-CPU-second construction
target. Both saved edge lists were checked independently; every
degree is eight, and every bad pair and its distance is retained.

For adjacent deletions, further assembly must change the additions
to repair the five exhibited zero-endpoint old pairs; reassigning
attachments cannot repair that fixed core. For crossing deletions,
the old zero-pair conditions are already satisfied, but the endpoint
port sets must be changed to remove the eight-versus-seven column
demand while preserving their old-old intersections and the two
required new-new shared pairs. These are explicit constraints for
the parent-managed joint completion inputs. No additional solver or
search was launched by this seed construction task.
