# Chen360 source interface; no numerical construction yet

Status: SOURCE_LITERAL_AVAILABLE_UNTESTED. The cached primary entry at desc_g8#38 names Jianxiang
Chen,2018-10-16,(degree3,diameter8,order360),Moore766. It constructs H from the
144-vertex symmetric diameter7/girth8 graph by replacing each edge with an edge
vertex and adding a complete pairing among the216 edge vertices. The published
H has three vertex orbits. These source properties are inherited, not checked.

The exact NetworkX adjacency link was extracted from the cached primary entry:
https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD8/360-deg3-D8_adjlist.txt
There was one HTTP download attempt and no guessed filename. The literal is
only retained as input for a possible later batch; no adjacency structure was
built. The existing Q8 lift recipe is an alternative description of the same
360 graph, not an additional source or result.

The old canonical strict scopes close the two frozen q5/q7 field controls and
the q5 free-semi3-normal variant. They do not close edge surgery on the original
360 literal. The consulted method ledger and source scope notes contain no
same-rule single-edge-subdivision exclusion. This is a scoped history finding,
not proof that no such fact exists anywhere.

For e={u,v}, put K=G-e and H=K+{uz,zv} with newlabel z. For every oldx,

    d_H(z,x)=1+min(d_K(u,x),d_K(v,x)).

Any simple path starting at z chooses u or v and cannot revisit z, so this is
exact, including infinite distances. Therefore the newroot condition is

    ecc_H(z)<=8  iff  R7_K({u,v})=V(G).

Also d_K({u,v},x)=d_G({u,v},x): a shortest path from the endpoint set can
never benefit from traversing e, because starting at its other endpoint would
shorten it. Thus the newroot condition may equivalently use R7_G({u,v}).
This equivalence does not apply to an individual endpoint distance or old-old
distances after deletion. A full D8 candidate needs both this newroot condition
and every old-old distance in H at most8. The sourceD8 certificate alone only
gives old-old distance at most9 after replacing one edge by a length2 route.

Degree accounting would be n361,m541,oldvertices degree3,newz degree2,max3;
the degree sum1082 is even. A degree2 root in a max3 graph has B8 size at most
1+2(1+2+...+2^7)=511, so the simple rooted-capacity obstruction does not exclude
361. Compare(3,6): its corresponding bound127 is below133. The classical
Moore766 and this511 rooted capacity are upperbounds, not existence evidence.

No sourceD8/degree/BFS check, graph construction, edge enumeration, search,
solver, field, Lean, ARIS, install or hash was performed. The source-read budget
is5CPU including a conservative1CPU preparation charge; no automatic numerical
continuation is authorized. Root owns any next numerical budget and global
acceptance. Same Goal remains active; no new graph count is made.
