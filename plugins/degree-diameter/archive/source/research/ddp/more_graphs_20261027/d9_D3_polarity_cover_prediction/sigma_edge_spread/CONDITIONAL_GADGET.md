# Conditional five-cut spread gadget: paper check, not an actual graph

The degree/simple and new-root-to-port argument below is correct
conditional on the stated spread. The parent has since reported that
the actual fixed sigma-edge pool has32valid16-port blocks but no
four-block exact cover of its32nonfixed port pairs (complete MRV,
17nodes). Thus the required spread premise failed in that pool and
no producer was started. This note neither assumes an actual spread
nor searches another involution, gadget or failed pair.

Let G be the actual585source, P its65degree8ports, and T its520degree9
nonports. Assume an involution sigma fixes p in P and pairs the other
64ports. Assume four distinct old edges u_i—sigma(u_i) form a matching
with eight core endpoints A. Write S(a)=P intersect R2_G(a). Require
the four sets S(u_i) union S(sigma(u_i)) to have size16, be pairwise
disjoint and have union P minus {p}. These are unverified gadget
premises except where the separate actual pool certificate says so.

Choose a core vertex b in R2_G(p), outside A. Choose its old core
neighbor w outside A and outside N_G(p). In particular b and w are
distinct and neither belongs to A. Delete the four paired edges and
the edge b—w. Add a new vertex x adjacent to A union {b}; add p—w;
and add the32sigma matching edges on P minus {p}.

This graph is simple and9-regular. Every A vertex loses one paired
edge and gains x; b loses w and gains x; w loses b and gains p. Each
of the64nonfixed ports gains its sigma partner; p gains w. All these
vertices are distinct where required. The new p—w edge was absent
because w is outside N_G(p), and old ports are independent so the
32matching edges were also absent. Vertex x has nine distinct
neighbors. The counts are586vertices and

    2600−5+9+1+32 = 2637edges.

For a nonfixed port q, choose a in A with old distance at most2 to q.
An old a-to-q witness cannot use b—w: its first edge does not have an
A endpoint, and its second edge would have to end at the port q,
whereas both b and w are core vertices. An A-paired deleted edge
could occur only as the first edge a—sigma(a), followed by sigma(a)—q.
Replace x—a—sigma(a)—q by x—sigma(a)—q; sigma(a) is itself in A and
is an x neighbor. An A-paired deleted edge cannot be the final edge
to a port. Thus x remains within3 of every one of the64ports, even
if w happens to be adjacent to A. No deleted A—b or A—w edge exists.

For the fixed port p, take an old b-to-p witness of length at most2.
The A-paired cuts cannot affect its first edge because b is outside A,
or its final edge because p is a port. The only possible loss to b—w
would be b—w—p, which would require w in N_G(p), expressly excluded.
Therefore this witness survives and x—b followed by it reaches p in
at most3 steps. Loss of a separate b—w—port(w) route is immaterial:
w is outside N(p), so port(w) is among the64already protected by A.

This proves only all65port coverage, not the520core coverage or all
old–old distances. If the spread premise ever holds in an explicitly
authorized different scope, those remaining conditions require actual
modified adjacency checks. For complete old–old verification let
Q=R1_G(A union {b,w}), at most100old roots. Any old pair outside Q
has an original length-at-most3 path using no cut edge: a path using
a cut would require at least2+1+2=5steps. Hence BFS from Q plus x
against the complete modified graph checks every potentially damaged
pair; this is a complete certificate, not a sample. No such BFS or
candidate construction was run for this paper note.
