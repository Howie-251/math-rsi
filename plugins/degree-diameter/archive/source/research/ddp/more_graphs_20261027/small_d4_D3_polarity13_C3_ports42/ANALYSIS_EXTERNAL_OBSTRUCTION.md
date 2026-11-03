# Uniform obstruction to every three-helper free-port completion

Verdict: **VALID**. Preserving all39 vertices and72 edges of any C3 voltage lift of the loopless F3 dot-product polarity graph, then adding three helpers and only degree-legal edges, cannot produce a maximum-degree4 graph of diameter3. This includes the prepared P3 construction, but does not depend on its fixed helper topology, voltage choices, spanning-tree gauge, or exact port pairing. The proof is purely structural; no assignment, candidate graph, SAT call, word enumeration, or BFS is executed.

## Old vertex classes

Projective vectors over F3 have weight1,2,or3 according to their number of nonzero coordinates. For the dot-product polarity graph:

* The four weight3 points A are absolute and have degree3. Each is adjacent to one weight2 point with each possible zero coordinate, and to no weight1 point.
* The six weight2 points S each have two A neighbors, one paired S neighbor with the same zero coordinate, and exactly one weight1 neighbor E, namely that coordinate axis.
* The three weight1 points E form a triangle and each has two S neighbors; they have degree4.

These statements follow directly from the dot product. For S=(0,1,epsilon), for example, its E neighbor is(1,0,0), its paired S is(0,1,-epsilon), and its two A neighbors satisfy a+epsilon*b=0. The same computation holds after permuting coordinates.

In a C3 lift the class sizes are12 A-ports,18 S-lifts, and9 E-lifts. Every old A-port has exactly three S neighbors, one leading to each of the three E base classes. Every S-lift has exactly one E neighbor. All old S/E vertices already have degree4, while each A-port has room for at most one new edge if all old edges are retained.

Therefore any allowed added edge touching an old vertex must touch an A-port. Its one free slot may be used for one helper spoke or one new A-A edge, never both and never two helper spokes. New old-old edges consequently form a matching on unattached ports. This capacity conclusion needs only the maximum-degree4 bound, not an assumption that every slot is filled.

## Each helper needs at least three direct spokes

Let h have r direct A-port neighbors and d neighbors among the other helpers. A path of length at most3 from h to an old E-lift must be

    h - A - S - E.

If its first step is to another helper, only two steps remain and no A-E edge exists. If its first step is to an A-port, that port's one new slot is already occupied by the spoke, so its other usable edges are old A-S edges; it cannot take an additional A-pair edge or another helper spoke. The E-E triangle adds no missing short type: reaching the first E already takes three steps, leaving no time to traverse another E edge.

Each direct A spoke has exactly three such length3 walks, ending in one lift of each E base class. Thus h can reach at most3r of the nine E-lifts within3 steps. Diameter3 requires

    3r >= 9, hence r >= 3.

Since r+d<=4, every helper must have d<=1. For the prepared P3 specifically, its middle helper has d=2 and r=2, so it reaches at most six E-lifts and must miss at least three, uniformly for every voltage and port assignment. More precisely, its two spokes reach at most two of the three lifts in each E base fibre, so each of the three fibres has a missing target. This already rejects the compiled P3 family without SAT.

## No short external path can join different helper components

The stronger conclusion uses all three helpers, with arbitrary induced graph H. Any shortest helper-to-helper path of length at most3 can be taken simple. If it leaves H, its old endpoints must be A-ports.

A two-step helper-A-helper path would require two helper spokes at one port, exceeding its single available slot. A three-step helper-A-A-helper path cannot use an old A-A edge, because distinct absolute base points are independent and there are no such old lift edges. It also cannot use a newly added A-A edge: both endpoints already use their one new slot to attach to the helpers. A three-step path with one old port and another helper edge again requires that old port to be attached to two helpers. A route using S or E cannot return to a helper within three steps because neither class has a free slot or a helper neighbor.

These exhaust the possible short path types containing old vertices. Consequently, any helper pair at distance at most3 in the completed graph must already be connected by a path of length at most3 entirely inside H.

But every helper has degree at most1 in H, from the E-target argument. A graph on three vertices of maximum degree1 is disconnected. Some helper pair therefore has no path of length at most3 in the full graph, a contradiction.

Equivalently, all E targets require at least nine helper spokes. The helpers' combined degree bound permits at most one internal edge, while short helper-to-helper coverage requires H to be connected and hence at least two. The internal edges cannot simultaneously satisfy these two global coverage duties.

## Degree regularity and the exact excluded scope

The parent's local Moore observation is also correct: if a root had degree at most3 while all graph degrees were at most4, its closed radius3 ball would contain at most1+3+9+27=40 vertices. A42-vertex D3 target must therefore be4regular. The obstruction above is stronger in the sense that it already assumes only the upper bound4; leaving a port unfilled cannot circumvent it.

The theorem excludes every completion with all of these premises: the old39-vertex C3 lift is retained without deleting or rewiring any old edge; exactly three new helpers are added; the final graph is simple with maximum degree4; and any new edges obey those degree limits. The limits themselves restrict old endpoints to the12 A-ports and at most one additional edge per port. Any helper induced graph and any legal port matching/spokes are allowed in the proof.

It does not exclude arbitrary42-vertex graphs, deleting old lift edges, a different old source or vertex-class incidence pattern, or a different number of helpers. It is not an upper bound41 for the general(4,3) problem and does not reopen the paused old D2 work. No further helper topology or parameter continuation is proposed here.

The prepared [CNF](model.cnf) has a valid exact structural/reachability encoding, as reviewed in [ANALYSIS_CONSTRUCTION.md](ANALYSIS_CONSTRUCTION.md). The theorem shows that its target family is mathematically empty. This is a paper exclusion, not a raw solver UNSAT or an unrun numerical failure. There is no actual42-vertex candidate or measured diameter/bad-pair total.
