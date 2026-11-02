# PSL2(F11)/C2 on330 cosets: complete degree5 batch

**All1132 orbital-union candidates completed:118 disconnected,1014 connected and every complete identity-radius4 check failed.** There are zero hits and zero untested candidates. The existence prediction is refuted for the fixed action. Negative exact global diameter and ordinary unordered bad-pair counts remain null; no new lower bound or graph was claimed.

The actual new stabilizer binding matches the proposed structure: H has order2, N(H) has order12, the330 vertices are cosets xH, and inversion orbits of the complete doublecoset list give three degree1 atoms,25 degree2 atoms and69 degree4 atoms. All atoms are actual nonloop symmetric adjacency relations, their representative independence was checked over all660 group representatives, and together they partition every nonloop neighbor set. The original660 group matrices/table were read-only reused, without rebuilding or re-auditing the old group.

|Atom-degree pattern|Candidates|Disconnected|Connected R4 failures|
|---|---:|---:|---:|
|1+2+2|900|96|804|
|1+4|207|21|186|
|1+1+1+2|25|1|24|

Every candidate is a simple5regular330-vertex graph with825 edges. The producer performed1132 connectivity closures and1014 complete one-root radius4 traversals, zero all-root BFS and zero old-source BFS. The worker process used0.561771 CPU seconds, the driver0.000765586 seconds; compilation was zero. The process exited0 in the initial call and has no live handle. Its hard limit was18 CPU seconds within the20-second aggregate allowance.

[MODEL_SCOPE.md](MODEL_SCOPE.md) proves that the atom enumeration covers every simple undirected valency5 graph invariant under this fixed G/H action. Degree at most4 cannot have diameter4 at330 points by Moore161. Therefore the complete negative result closes this fixed-action maximumdegree5 family, while general330-point graphs and other actions remain open. The saved public threshold252 was a proposed improvement threshold, not a new result.

The changed stabilizer replaces the earlier132-point five-orbital-plus-matching restriction with multiple smaller adjacency atoms; it is a controlled variant of the same PSL2 coset mechanism. The extra orbital freedom was real but did not produce complete four-step coverage. This batch stops without another subgroup, generator seed, graph score optimization or whole-graph distance study.

Authoritative inputs and receipts are INPUT_BINDING.json, ATOMS.json, CANDIDATE_INPUT.json, CASES.jsonl, RESULT.json, terminal.json and the self-contained search.py/run.py. The original group data remain in the completed132 directory. The sole ledger had no matching330/C2 scope before this run.
