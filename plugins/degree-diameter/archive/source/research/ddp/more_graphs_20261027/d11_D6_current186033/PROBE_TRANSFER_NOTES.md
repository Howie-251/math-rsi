# Directed transfer of the successful near-neighborhood probe to D6

This is implementation support for the sole producer
/root/expert_brief_evidence. It does not download or parse raw source,
run a radius ball, produce a candidate, or repeat any old-source BFS.
The reviewed successful code is
d13_D5_h9_transfer/singlefault_star_probe/cover.cpp and its
continuation/run.py. No copy of their producer was launched here.

The existing actual profile binds n186033,m1010817,maxdegree11, with
24685 free vertices. It has exactly one one-fault prototype: v19161
has degree10, its only saturated neighbor is d78477, and its nine
other neighbors are

    M=[72425,85923,89934,95946,103392,107088,113094,120546,127006].

Here “remove the full pin” means omit d from the NEW neighbor set;
it does not delete any old edge. Retaining all old edges preserves
old–old D6. A new vertex adjacent to distinct current-free vertices
S, with |S|≤11, has D6 to all old vertices exactly when R5_G(S)=V(G).
Thus this one prototype allows zero, one or two guards, with the
complete selected-neighbor R5 union deciding acceptance.

Necessary code changes from the old native kernel are small but
important. Remove its assert(DEG==13) and pass DEG=11. Replace both
the radius4 BFS stop and its four bit-propagation steps by radius5.
Do not change just the BFS: an unchanged four-step guard propagation
would reject valid R5 guards. The old kernel uses vector<int> and
already has 32-bit vertex indices; retain that property. Do not use
the older point_to_core uint16 maps or any 65536 vertex bound. Current
CSR is little-endian uint32 n,2m,n+1 offsets,2m neighbors; degree bytes
remain sufficient. n+1=186034 and all literal pins must remain 32-bit.

Load the producer's existing CSR once, keeping its actual current
degree array and base n/m. A bounded radius routine can reuse a
uint32 visit-generation array and uint32 queue of length n. At each
depth, expand only the current queue frontier, for five layers.
The resulting visited tags identify full R5 and the missing list.
No all-pairs distance array or R5 row for every free vertex is needed.
After a successful append, either update current adjacency/degrees
or bind the next call to the new source; an older-base failure cannot
exclude a later-base candidate.

For the one actual prototype, first compute the mandatory R5(M).
The sole producer has now measured 4201 missing vertices and181832
covered, in MANDATORY_R5.json. This result was not recomputed here.
Useful exact guard options, all restricted to actual degree<11 and
outside M, are:

1. For one guard, intersect E∩R5(t) over missing targets t. Symmetry
   of this undirected graph makes this exactly the set of guards
   covering all mandatory holes. Target balls can be computed on
   demand, stopping when the candidate bitset becomes empty.
2. For up to two guards, choose one mandatory hole h. Every solution
   contains a guard a in E∩R5(h). For each such a, form the remaining
   holes and intersect their eligible-guard coverer sets to find b.
   This is complete if all such a and all required intersections
   finish. Do not impose b>a unless the enumeration order is proven
   to preserve every unordered pair: the first guard is constrained
   to cover h. A CPU stop is UNKNOWN, not an exact-two failure.
3. If the measured 4201-hole projection is cheaper than many individual
   balls, the existing target-bit propagation is valid after changing
   it to five rounds. Its two n×ceil(4201/64) uint64 buffers use about
   196.5MB decimal, not the full 24685×186033 free-anchor R5 matrix.
   This allocation is justified by the actual one-prototype hole
   count; do not preallocate it blindly for thousands of prototypes.

Store only required target coverer bitsets, projected guard masks,
and per-item temporary queues. Deduplicating identical guard masks
is sound for the present one-new-vertex search; a duplicate guard is
not needed as a second neighbor. A zero-cover target disproves all
one/two-guard completions of that item. Otherwise exact_one or
exact_two_complete must separately report completion. Retain the
old producer's complete current-degree check and final full selected
R5 check before accepting literal neighbors; no old all-source BFS
is required by this append-only induction.

The requested free-pin proxy analysis has also completed without
balls or source parsing. FREE_PIN_PROXY_ANALYSIS.json reads only
the saved CSR and degree bytes. The eleven neighbors of d78477 are

    [1274,9088,19161,24157,28380,36035,43458,51104,53063,63302,141164].

Among24676eligible guards excluding M, exactly16share one neighbor
with d; the other24660share none. The maximum overlap is only1, so
there is no high-overlap open-neighborhood proxy analogous to the
successful D13 source. The actual sixteen IDs and complete shared
and private neighbor sets are in POSITIVE_OVERLAP_GUARDS.json. They
may form a finite priority list, but their failure cannot exclude
other guards. The global smallest symmetric difference is18, from
degree7 vertices182711,182724,182873 with zero shared neighbors;
minimizing this raw set distance alone would give a poor proxy signal.

The profile's old182618 label denotes a numerical/legacy prefix,
not an identified geometric core. No core-color or geometry mapping
was inferred. This proxy analysis used0.040364CPU seconds plus
0.001064seconds to emit all16records, zero BFS and zero candidate
generation. Low direct overlap does not exclude long-radius coverage;
the producer's actual R5/guard result remains decisive.
