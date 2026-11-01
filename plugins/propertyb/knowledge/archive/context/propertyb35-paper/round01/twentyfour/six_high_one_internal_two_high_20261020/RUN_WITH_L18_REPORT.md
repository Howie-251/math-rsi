# P6 one-internal two-higher-trace pilot with both accurate18-point gates

## Exact scope and result

Both [EIGHT_MIXED_POSITIVE_EIGHTEEN_REPAIR](../../../../../proofs/propertyb35/EIGHT_MIXED_POSITIVE_EIGHTEEN_REPAIR.md) and [EIGHT_POSITIVE_18_ONE_TRIPLE](../../../../../proofs/propertyb35/EIGHT_POSITIVE_18_ONE_TRIPLE.md) were read in full. A fresh run added exactly their statements:

* seven positive four-sets and one positive triple, zero negative triples, at most20 negative quadruples, ground at most18 and D7;
* eight positive four-sets, at most one negative triple, at most19 negative quadruples, ground at most18 and D7.

The previous [first profile](PILOT.json) is unchanged. Source and output for the new run are [RUN_WITH_L18.py](RUN_WITH_L18.py), [RUN_WITH_L18.json](RUN_WITH_L18.json). The new run took0.0245 CPU seconds. It processed ten necessary P inventories in the first high-trace orbit, accepted the first nine, and stopped at the tenth. No later high-trace orbit, nine-at-a case, $(5,1,1)$ inventory or optional three-higher-trace inventory was processed.

The current stopping signature is outside the direct hypotheses of all the supplied dimension-correct repair predicates. It is a necessary P inventory, not a claimed actual H realization or an unrepairable signed system. The old17-point eight-positive theorems were not applied to the actual18-point exterior.

## Necessary inventory and complete actual signature list

Normalize the unique internal edge as $C=01234$, the remaining high point as $a=5$, with degrees $(9,8,8,8,8,8)$. The higher traces are disjoint:

$$T_1=012,\qquad T_2=345.$$

There are six pair traces and26 singleton traces. The first stopping multigraph is

$$J=2\cdot01+05+15+23+25,$$

with

$$s=(3,3,2,1,0,3),\qquad u=(4,3,4,5,6,4).$$

Every $a$--C pair not covered by either higher trace is covered by J: the required pairs05,15,25 are all present. All degree and exterior-capacity conditions from the first [report](REPORT.md) hold. The18 exterior vertices have degree seven under the actual standing assumptions.

Every eligible two-blue choice meets both triples, and therefore takes one point from012 and one from345. Its internal and two higher edges already have both colors. The exact signatures are:

| Blue pair | Positive four-sets | Positive triples | Negative triples | Negative quadruples |
|---|---:|---:|---:|---:|
|03|9|0|2|17|
|04|10|0|3|16|
|05|8|1|1|18|
|13|8|0|2|18|
|14|9|0|3|17|
|15|7|1|1|19|
|23|9|1|4|17|
|24|10|0|4|16|
|25|8|1|2|18|

These counts retain every all-blue pair trace as a positive triple, and every all-red pair trace as a negative triple. No negative singleton/pair is omitted: both higher traces are proper in every row. P hits every original edge, so no zero-P dual-sign risk occurs. Each exterior point's signed occurrence is at most seven because each original source edge contributes at most one signed constraint.

## Check against existing accurate gates

The smallest pure-four signature is blue13: eight positive four-sets, two negative triples and18 negative quadruples on18 points. The accurately proved18-point gate permits only one negative triple. The17-point eight gate cannot be applied without an additional proof that the actual positive union has at most17 points; no such bound has been established here.

Blue15 gives seven positive four-sets plus one positive triple, one negative triple and19 negative quadruples. Its eight positive constraints exceed the new seven-mixed gate, while the exact18-point eight-mixed theorem requires no negative triple. Blue05 and blue25 have nine positive constraints; the other signatures exceed these gates as well. The dimension-free ten-positive theorem allows no negative triples and hence does not accept the larger pure-four rows.

The canonical `POSITIVE`/`MIXED` repair files were checked for another direct accurate count gate. No present statement directly accepts one of these nine signatures. A tailored geometric repair remains possible; this pilot has not classified exterior intersections or shown failure of such a repair.

## Small next obligation, without a new computation

The closest generic extension is eight positive four-sets, two negative triples and18 negative quadruples, on18 points with D7. In the existing18-point eight-four proof, the old $E\ge4$ five-label graph branches have ample numerical room for this change: the old86 four-candidate blocker bound is at most134, below178; the zero-matching star/triangle bound is at most56, below80; $M_2\ge6$ gives $C_3\ge12$ against at most ten blocked candidates.

The uniform specified-pair/triple bound at the already classified $E=3$ boundary gives144 against the minimum144, so it needs a strict refinement. This is the same existing seven-type domain, not a request for a new free graph or hypergraph domain. For its triangle minimum, the actual pair extension counts are much smaller than the uniform50; evaluating the old seven representatives' actual target extensions may suffice. No such extension is asserted proved or used by this run.

The root agent was notified of this precise interface. The present pilot stops here, with all source records intact and the original P6 canonical proof unchanged.
