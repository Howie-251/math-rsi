# HS58, two original deletions and five additions: complete auxiliary input

Date: 2026-10-12. This directory contains one completed necessary-domain
screen for the eight new vertices H. It is an assembly catalog only:
no HS completion, SAT search, graph optimization, or new proof queue
was started. Earlier a4 sources and outputs were left unchanged.

For an eight-regular extension, the old-new degree sum is
50+2*2-2*5=44, so H has (64-44)/2=10 edges. For each H, let K(H) contain
exactly the vertex pairs farther than two steps apart in H. Each such
pair needs a common old neighbor. Deletion endpoints supply at most
four K2 cliques if D is disjoint, or one K3 and two K2 cliques if D is
adjacent. Thus the exact auxiliary-only budget tests used here are:

* Disjoint D: K(H) has at most four edges.
* Adjacent D: some three-element set contains at least |E(K(H))|-2 of
  its edges. The program checks all 56 three-element sets, rather than
  retaining all graphs with at most five bad pairs.

The source [hs58_two_delete_five_add_auxiliary.cpp](../hs58_two_delete_five_add_auxiliary.cpp)
checks all binom(28,10)=13,123,110 labeled edge subsets without topology,
degree, or symmetry pruning. For each newly encountered surviving
isomorphism type it explicitly generates all 8!=40,320 vertex
permutations and records the complete orbit. This is exact S8 orbit
classification; it does not reuse the old unicyclic AHU key. The run
checks each orbit size against its labeled count, and checks orbit
size times automorphism order equals 40,320.

The single run completed with complete=true, stop_reason=complete_domain,
and exit code zero. It used one pinned CPU, a 9.8-second internal CPU
stop, and OS CPU limits of 10/11 seconds. Actual screen CPU time was
2.765032 seconds and wall time 2.773698 seconds. Compilation was
separate: 0.882222 CPU seconds and 0.888149 wall seconds. No rerun was
performed.

| Necessary budget | Labeled survivors | Isomorphism types |
|---|---:|---:|
| Disjoint D | 1,043,840 | 72 |
| Adjacent D | 1,487,360 | 89 |
| Union | 1,487,360 | 89 |

In this completed domain every disjoint-budget survivor also passes
the adjacent budget. This is an actual result, not an assumption that
the two abstract tests are generally equivalent. The 17 extra types
have exactly five bad pairs; their compatible three-element cover must
be a triangle in K(H), leaving at most two bad pairs for the other
two deleted endpoints.

| Number of bad pairs | Surviving types | Labeled survivors |
|---:|---:|---:|
| 0 | 5 | 10,640 |
| 2 | 9 | 56,280 |
| 3 | 17 | 219,240 |
| 4 | 41 | 757,680 |
| 5 | 17 | 443,520 |

Use [representatives.json](representatives.json) for the reusable full
edge lists, all bad pairs, degree sequences, both compatibility flags,
actual multiplicities, and adjacent-budget cover witnesses.
[enumeration.json](enumeration.json) contains those same final records
plus the complete bad-pair histogram over all 13,123,110 inputs.
[summary.json](summary.json) gives type IDs by compatible budget and
bad-pair count. [resources.json](resources.json) and
[compilation.json](compilation.json) record actual resources. The launcher
is [hs58_two_delete_five_add_auxiliary_run.py](../hs58_two_delete_five_add_auxiliary_run.py).
The streamed enumeration.representatives.jsonl contains discovery-time
snapshots; its accumulated multiplicities are not final. Use the final
JSON files for all counts and downstream assembly.

There are five universal-vertex types, IDs 1,5,6,10,52, each with center
label 0. Their three extra edges on the seven leaves have respective
shapes K1,3; K3; P4; P3 plus K2; and three disjoint K2. They are the five
types with zero bad pairs; all other 84 types are nonuniversal.

One additional construction condition, supplied separately by the
parent analysis, was not imposed in this screen. If H has a universal
vertex with unique old neighbor v, let E=sum_x max(p_x-1,0), and let z
count old vertices with zero ports. At a=5, the port sum gives z=E+6.
Every zero-port vertex must be an old neighbor of v to reach the
universal new vertex, so z<=8-p_v. Together with E>=p_v-1 and p_v>=1,
this forces p_v=1 and E<=1. Thus z is six or seven. These are useful
additional conditions for assembling the universal cases; they do not
change the raw auxiliary counts above.

## Subsequent mathematical reductions, kept separate from the raw screen

All 17 adjacent-only types have exactly five bad pairs. Covering five
distinct pairs by one K3 and two K2 cliques forces the capacities
3+1+1 to be attained with no overlap. Thus all three deletion endpoints
have maximal ports 3,2,2, all additions avoid those endpoints, and the
five additions form a nonempty matching on the other old vertices.
The reusable lemma “Adjacent deletions with all endpoint ports maximal”
in
[HS58_TWO_DELETE_FOUR_ADDITIONS_NONUNIVERSAL_EXCLUSION.md](../../../../proofs/dd82/construction/HS58_TWO_DELETE_FOUR_ADDITIONS_NONUNIVERSAL_EXCLUSION.md)
excludes this situation for every H. Its argument requires only a
nonempty addition matching avoiding the deletion endpoints, not that
the addition count is four. Hence these 17 types are closed at a=5
without another auxiliary computation or solver run.

The subsequent pure result
[HS58_TWO_DELETE_UNIVERSAL_H_EXCLUSION.md](../../../../proofs/dd82/construction/HS58_TWO_DELETE_UNIVERSAL_H_EXCLUSION.md)
excludes every universal auxiliary graph when a>=5, for either shape
of the two original deletions. It therefore closes the five universal
types 1,5,6,10,52 in this a5 catalog.

After just these two deductions, the next assembly domain has
89-17-5=67 nonuniversal isomorphism types, representing 1,033,200 labeled
auxiliary graphs. Equivalently, these are the 72 disjoint-budget types
minus the five universal types. The reusable
[survivor_ids.json](survivor_ids.json) records their exact IDs and both
excluded ID lists, with references to the two deductions. The raw
89-type catalog, compatibility flags, and original screen counts have
not been changed. These 67 types remain necessary auxiliary inputs;
none is asserted to admit a full HS completion. The new deductions have
been checked locally by the root agent. C17 and both authorized retries,
which included the subsequent C18 delta scope, returned authentication
errors; no external acceptance is claimed.

The later no-cross deletion-endpoint theorem gives a stricter conditional
subdomain. Its [derived filter](no_cross_filter.json) reads these saved
67 representatives and retains only type 3 when the two deleted HS edges
have no original cross-edge between their endpoints. The original 67-type
general list is not replaced by that conditional list. See
[the endpoint proof](../../../../proofs/dd82/construction/HS58_NO_CROSS_ENDPOINT_COVERAGE.md)
and the [checked completion and verified orbit connection](../../../../proofs/dd82/construction/HS58_A5_NO_CROSS_DELETIONS_EXCLUSION.md)
for the complete exclusion of this narrower a5 stratum.
