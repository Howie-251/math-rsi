# Twenty-one vertices: unique degree-seven center, unit-eight reduction

This is a rigorous partial reduction, not a completed coloring proof for the unique-seven branch. No Lean, MCP review or whole-hypergraph enumeration was used.

## Actual input and selection

Let H be simple five-uniform, pair-covering, on 21 vertices with 35 edges. Assume x is its unique degree-seven vertex. The other twenty vertices have degrees at least eight and degree sum 168, so their total degree excess above eight is exactly eight.

The codegree row of x sums to 28. If h other vertices have codegree one with x, the other 20-h have codegree at least two. Thus 28>=h+2(20-h), or h>=12. At most eight of the twenty vertices have degree greater than eight. Consequently at least four actual unit neighbors of x have degree eight.

For any selected s unit neighbors, their unique x-edges induce one common partition Pi. There are seven central edges and 28 noncentral edges. Central exact traces are one for each nonempty block and 7-|Pi| at the center singleton. With inclusive neighbor counts I_A, the noncentral exact traces are recovered by Mobius inversion from J_empty=28 and J_A=I_A-indicator(A is contained in a Pi-block). This is the actual-unit-star lemma, with center degree seven and n=21; no twenty-vertex counting value is used.

## Complete two- and three-neighbor gates

The existing present-parameter file `../../twentyone-high/UNIT_PAIRS.json` already contains all fifteen nonnegative (7,8,8) unit-star inventories: neighbor codegree 1 through 8 and both central block relations whenever nonnegative. These n=21 certificates were reused, not searched again. Their independent replay shows that all nine types with codegree at least four are strict. Thus any two unit-eight neighbors have codegree 1,2,3, with either central block relation.

For three actual unit-eight neighbors use all five partitions, their three pair codegrees in {1,2,3}, and inclusive triple count between zero and the minimum pair codegree. Recover all exact noncenter traces and retain the nonnegative ones. The full domain has 246 labelled inventories, agreeing with the pre-existing n=21 three-neighbor domain. Ten existing pilots were reused. `THREE_DP.json` contains all 246 fixed certificates: 135 strict. `THREE_JOINT.json` tests the 111 fixed failures with one bounded 24-order shared-layout calculation each; eleven further cases are strict. `THREE_REMAINDERS.json` contains the exact 100 remaining views. Fixed work took 3.28 seconds and total through the bounded joints took 5.02 seconds.

## Complete common four-neighbor domain and current boundary

For four actual unit-eight neighbors, use one of the fifteen partitions of all four labels and the same six pair counts. For each of the four triples, the restricted partition, pair counts and inclusive triple count must be one of the same 100 residual views, or that actual triple already supplies a coloring. Choose the inclusive four-count between zero and the minimum of the four triple counts, recover all exact traces, and retain nonnegative inventories. The actual H necessarily satisfies every one of these simultaneous conditions.

`FOUR_DOMAIN.json` contains the full resulting 7,777 labelled inventories and 547 true neighbor-S4 representatives, keeping the center fixed. It stores a concrete single permutation transporting each representative to each corresponding labelled inventory. It was generated in 0.39 seconds.

The 18-case spread pilot had 13 fixed strict cases. The complete fixed pass in `FOUR_DP.json`, reusing those pilots, has 400 strict cases out of 547 and took 10.59 seconds. The bounded joint pass processed all 147 fixed failures in less than the authorized 60 seconds, excluding another 83. Total through the joint pass was 25.34 seconds. The maximum accepted four-neighbor bound is 6434/6435. Exactly 64 representative inventories, comprising 668 labelled inventories, remain in `FOUR_REMAINDERS.json`. These are necessary residual views, not proven realizable hypergraphs. No free fifth-neighbor domain was generated.

Fixed five-lock certificates use denominator 16! at n=21; the earlier four-lock certificates use denominator 17!. All accepted inequalities, quota deductions and joint repairs use exact rational arithmetic. A non-strict result is retained and is not called an exclusion.

## Actual consequences for the whole unit-eight pool

Suppose no coloring has already been obtained, and let U8 be the entire unit-eight neighbor pool of x, of size s>=4. Every four-element subset of U8 must have one of the 64 residual views. `analyze_remainders.py` derives the following facts directly from their exact inventories, independently of the stored descriptive metadata:

* At most one of the six pairs in a residual four-tuple has codegree three. Hence the entire pool U8 has at most one codegree-three pair: any two distinct such pairs have a union of at most four vertices, extendible to a four-tuple in U8.
* No central partition block on four vertices has size four. Hence every central edge contains at most three vertices of U8.
* If a four-tuple contains the possible codegree-three pair, its number of codegree-one pairs is 0,2 or 4.
* Every four-tuple has pair-codegree sum at least nine.

The exact seven residual pair multisets and their orbit counts are in `REMAINDER_STRUCTURE.json`. Twenty-four of the 64 residual views have every pair codegree two. Thus the sparse codegree-three conclusion by itself leaves a substantial regular obstruction and does not close this branch.

## Whole-pool degree budget for the next choice

Let g be the number of unit neighbors having degree greater than eight, and let e be their summed degree excess above eight. Then

    s+g=h>=12,   g<=e<=8.

These are high-degree unit vertices; they are not all assumed to have degree nine. If q is the number of actual unit degree-nine vertices, the other g-q high unit vertices have excess at least two, so

    e >= q+2(g-q)=2g-q,
    q >= 2g-e >= 16-2s.

In particular s<=6 gives at least four unit degree-nine vertices; s=5 gives at least six; s=4 gives at least eight. For s=4 equality is forced throughout: g=e=8, all eight high unit vertices have degree nine, h=12, and no degree excess remains elsewhere. The complete degree spectrum is then 7^1 8^12 9^8, the eight degree-nine vertices are all unit neighbors, and the eight nonunit vertices all have degree eight and codegree two with x (their codegrees sum 28-12=16).

For s=5 or6 higher unit degrees ten or eleven remain possible within the excess budget; they must not be silently replaced by nine. A next step could exploit the guaranteed pool of actual degree-nine unit neighbors together with common mixed views, or prove a selection lemma on the large unit-eight pool. Neither next step is included in the current result.

## Independent replay

`replay.py` uses restricted growth strings for the partitions and an explicit Mobius sum, rather than the discovery recursion. It independently reconstructs the fifteen two-neighbor cases, all 246 three-neighbor inventories, the exact 100 residual views, and all 7,777 four-neighbor inventories. It checks distinctness of the 547 representative S4 orbits and every stored transport, binds each fixed certificate and each accepted joint certificate to its exact source inventory, and replays all 547 fixed and 83 strict joint four-neighbor certificates. The expanded-edge fixed verifier `audit21.py` uses the actual n=21 conditional counts and quotas; it was adapted from the prior exact verifier by changing the point count and every corresponding free-set and link-capacity term.

Reproduce without LP, DP or SciPy:

```sh
python3 -B context/propertyb35-paper/round01/middle/twentyone-single-seven/replay.py
python3 -B context/propertyb35-paper/round01/middle/twentyone-single-seven/analyze_remainders.py
```

`REPLAY.json` and `REMAINDER_STRUCTURE.json` record the exact scope. The unique-seven coloring branch remains open after these 64 residual inventories.
