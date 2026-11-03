# Fixed cooperative P40 clique pool: route support excludes every nonempty subset

The exact frozen family is excluded by a two-round provider-deletion proof. No solver was needed. This is a comparison of shared route coverage, not a total missing-target score or a failure of one chosen clique size.

For each of the40 saved successful neighborhoods S_i, P_i contains exactly the members still below degree13 in the current51457 graph. All40 P_i were kept unchanged, including two empty sets. One read of the current literal graph and40 multi-source searches through radius4 saved their actual R3/R4 sets. There is no individually successful K1: R4 missing counts range from750 to51457. The union of their attachment ports has233 vertices, each appearing in at most two P_i.

## Exact route condition

For a selected nonempty index set I, preserve all old edges, attach y_i to P_i, and join every pair of helpers. For any old target t,

`d(y_i,t) = min(1+d_G(P_i,t), 2+min_(j in I, j != i) d_G(P_j,t))`.

The direct route proves the upper bound. For the reverse bound, take the last helper y_j on a shortest path to t. Its remaining route is one attachment followed by an old-G path. If j=i the prefix has length at least0; otherwise at least1, and the clique realizes that one-step prefix. Empty-set distances are infinity. Thus diameter at most5 requires every missing-R4 target of each selected i to have some selected R3 provider j.

## Complete witness chain

Start with all40 indices active. If i misses a target at R4 and no active candidate covers that target at R3, then i cannot occur in any feasible selected set. Previously excluded candidates cannot be providers, so this deletion rule is inductively sound.

- Round0 deletes39 indices: every index except28 has a missing-R4 target with **no R3 provider anywhere in the original40-pool**. For example, index0 (saved source-added vertex51417) misses target207, and the original provider list for207 is empty.
- Round1 deletes the sole survivor index28 (saved source-added vertex51445). It misses target265. Its complete original provider list is `[14,30,34,35,38]`, and all five were excluded in round0. With only28 active, its750 missing-R4 targets have no provider.

The fixed point is empty. By induction every feasible I would have to lie in that empty set, contradicting nonemptiness. This rejects all nonempty subsets of the frozen P40 clique family, including K1, without enumerating subsets. Degree and port constraints were not needed for this rejection; adding those required constraints cannot restore a solution. No conclusion about changed P_i, additional guards, new neighborhoods, or general cooperative constructions follows.

## Saved evidence and cost

`PREPARED.json` contains all40 literal S_i/P_i, R3/R4 sizes, conditional helper-degree bounds, and current old-port capacities. `prepared.R3.u64.bin` and `prepared.R4.u64.bin` store40 rows of805 little-endian uint64 words, bit t representing old label t. The provider files store each old target's exact40-bit provider sets. `PROVIDER_ELIMINATION.json` records every deleted index, concrete target, full original provider list, round, and remaining-support deficit. `RESULT.json` and `TERMINAL.json` are complete with no pending work.

The targeted old-scope check found no prior execution of this exact pool; full-neighborhood clones and whole saturated-component copies do not already cover deletion of saturated attachments plus a new helper clique. PRED was saved before the new route computations.

Worker CPU0.088320 seconds; preparation, compilation and execution0.739728 seconds, within25CPU. Exactly one current-source read and40 prescribed multi-source R4 computations;0 source-diameter all-root BFS,0 SAT/LP/MIP calls,0 new graphs,0 restarts,0 pool changes. Stop this exact family.
