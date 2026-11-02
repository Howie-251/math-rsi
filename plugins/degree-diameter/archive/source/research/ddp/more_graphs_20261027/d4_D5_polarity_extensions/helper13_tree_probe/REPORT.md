# Fixed H3 host: all13-helper377 extensions excluded

No graph was generated. Two complete cached-mask checks exclude every13-helper tree in the fixed naturalH3 extension class: retain all364/714 old edges, add no old-old edges, keep maximum degree4, and attach new vertices only through the28 actual degree3 ports. This does not exclude arbitrary377-point graphs, changed hosts, old-edge deletions or rewiring.

The sourceagent's actual R2 cells form a partition of364 vertices into28 cells of size13, one cell R2(p) for each free portp. The R3/R4 cache and these cells were reused; no balls or BFS were recomputed. Distinct ports are at old distance5, by the R4 port-incidence identity and inherited sourceD5.

## Why13 helpers force a diameter4 tree

Every old port must receive a new edge: otherwise any new-root route to an unattached port has a last old-host entry at a different port, followed by at least5 old steps, totaling at least6. Each port has only one degree slot, so all28 are used exactly once.

The new induced graph H must be connected. Passage between different components through the old host costs at least1+5+1=7. For13 new vertices, the degree budget gives

    4·13 ≥ 28+2|E(H)| ≥ 28+2·12 = 52.

Equality holds. Thus H is a13-vertex tree, every new vertex has total degree4, and a helper of H-degree d has exactly4−d old ports. In particular every leaf has3 ports.

For any helperu and any leafw, take an old portp attached to w. A route of length≤5 fromu to p cannot make its last host entry at any other port, and cannot leave/re-enter H before reaching w because such a passage costs≥7. Hence d_H(u,w)≤4. A tree's diameter is attained between leaves, so diam(H)≤4.

Choose its center c. Let b≤4 be its number of branches, and let k_i≤3 be the leaves beyond branchi. Then

    1+b+Σk_i=13.

This forces b=3 or4. For b=3, k=(3,3,3). For b=4, Σk_i=8; either some k_i=3, or all four k_i equal2. These are the only structural cases needed, not a sampled tree list.

## Stage1: no triple fully covers any foreign cell interior

For a leaf's three portsT, define

    good(T)={p∉T : R2(p)\{p} ⊆ R4(T)}.

All3276 triples were checked exactly. **Every good(T) is empty**: histogram{0:3276}, maximum0. Enumeration CPU was approximately0.019s. Full records are in triple_good_sets.json and the stage1 summary in CAPACITY.json.

In the3-branch333 tree, a leaf sees its own ports through R4, its six same-branch sibling ports and the center port through R2, and18 foreign leaf ports only as the ports themselves. The disjoint R2-cell interiors of those18 ports therefore must lie in R4(T), requiring at least18 members of good(T). Maximum0 excludes this topology.

For4 branches with some k_i=3, choose a leaf in that branch. Its parent has no old port and neither does the center. There are15 foreign level2-leaf ports. Other exits contribute R2 only within same-branch cells, R1 only within foreign-parent cells, or the foreign leaf ports themselves. Those15 foreign leaf-cell interiors can only be supplied by R4(T). Again good(T)=∅ excludes the case.

## Stage2: the remaining2222 tree also fails uniformly

The only remaining topology has center degree4, four parents each with2 leaves and1 old port, and8 leaves each with3 old ports. If T is one leaf triple and p its parent port, define

    good(T,p)={q∉T∪{p} : R2(q)\{q} ⊆ R4(T)∪R3(p)}.

The leaf must cover18 foreign leaf-cell interiors. Its other sibling contributes R2 only within its three cells; foreign parent ports contribute R1 only within their own cells; foreign leaves contribute just their ports. Thus those18 interiors must all be supplied by R4(T)∪R3(p). Necessarily |good(T,p)|≥18.

The prediction maximum<18 was frozen before this check. All3276×25=81900 pairs were evaluated exactly. **Every good(T,p) is empty**: histogram{0:81900}, maximum0. The first1000 profile is included once; total recorded CPU was approximately0.300s, below the5CPU budget. No assignment search followed. The first witness is T=[2,11,24], parent port56. Results are in PARENT_PORT_CAPACITY.json; the81900 exact counts are saved as parent_port_good_counts.u8.bin in the documented lexicographic order.

Combining the exhaustive tree reduction with these two uniform necessary failures excludes all13-helper cases in the stated fixed-host class. The original existence prediction is refuted; the second-stage obstruction prediction is supported. The earlier1..12-helper degree/port barrier and this result together imply that a successful extension in this same class would require at least14 helpers. No14-helper topology or computation was started.

Evidence: PREDICTION.json; STAGE2_PREDICTION.json; capacity.py; parent_port_capacity.py; RESULT.json; ../MULTI_VERTEX_PORT_BARRIER.md; ../source_and_single/{PORT_BINDING.json,PORT_BALLS.json,PORT_CLASSES.json}. No global Wiki, ZIP, delivery family, source graph or source cache was changed.
