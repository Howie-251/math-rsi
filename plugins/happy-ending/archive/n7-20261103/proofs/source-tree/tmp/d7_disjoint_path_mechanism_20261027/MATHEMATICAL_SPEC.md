# D7 disjoint R6 finite decision specification

Written before implementation or scientific execution, 2026-10-27. Main-selected single candidate: every two actual R6 paths in a complete D7 signotope intersect. No claim of packing=transversal or numerical capacity improvement is included. Requested executor is native gpt-6.1-sol/high; this role record is distinct from independently reported backend/effort evidence. All new work remains unreviewed/unaccepted.

## Exact finite entry and hereditary domain

Vertices are totally ordered, paths have vertex-count length, and R is true/B is false. A complete rank-3 signotope has packet order (abc,abd,acd,bcd) with at most one colour change. A consecutive monochromatic path has every subsequence monochromatic: on four consecutive retained points, equal first and last packet terms force every term equal; deletion of interior points, inductively, preserves the path colour.

D7 means complete packets, no B5, no weak7, and EndR5 intersect SrcB4 empty. No R7 follows from weak7 using the two-point opposite-colour path, but is explicitly encoded. All these properties are inherited by restriction; terminal attainment itself need not be inherited. If two disjoint R6 exist in any D7, restrict to their union of exactly twelve vertices, retaining both actual paths and every domain prohibition. Conversely a twelve-point witness refutes the all-class candidate. Thus this is a complete finite decision, not arbitrary small-order evidence.

## Formula and projection proof

N=12, zero-based sorted vertices. Colour variables 1..220 enumerate sorted triples lexicographically. For each quadruple exclude each of the eight four-bit words with more than one change (one clause per forbidden word). For every five-subset add the OR of its three consecutive colour variables (no B5). For every seven-subset add the OR of the negatives of its five consecutive colour variables (no R7).

For every seven-subset, use its extreme points as common endpoints, and all 32 assignments of the five interior points to a red path or a blue path. Forbid the conjunction of all correct consecutive colours. A length-two path imposes no triples. This exhausts weak7: different-colour paths with the same endpoints cannot share an internal point, because their subsequences would give the endpoint/internal-point triple both colours. Length sum nine therefore has union exactly seven. Longer witnesses can be shortened preserving endpoints to length sum nine.

For each eight-subset forbid red on consecutive triples of its first five points together with blue on consecutive triples of its last four points. These paths share the fifth point. This is exactly every junction witness because four predecessors of the common point and three successors are strictly separated. There are no omitted interleavings in a junction.

Enumerate all 462 six-subsets A containing vertex 0, with B the complement. Variables 221..682 are selectors. For each selector add eight implications requiring the four consecutive triples of each of A and B red. Add one OR of all selectors. Every disjoint R6 pair in N=12 partitions all vertices and has a unique member containing 0, so it supplies a selector; any true selector supplies the two actual paths. In the forward direction a true colouring of D7 with two disjoint paths extends to the formula by setting its selector true and the others false. In the reverse direction packets and the exhaustive forbidden conjunction clauses give exactly D7, and a selected partition gives disjoint red paths. This proves equality of semantic projections for every colouring.

Expected clause counts without deduplication: packet 3960; noB5 792; noR7 792; weak7 25344; junction 495; selector implications 3696; selector existence 1; total 35080, variables 682. Group/full hashes and full variable ledger will be saved before the solve. This direct-colour structural formula is not a C_r campaign and imports no state/F3 builder.

## Validation and controls

Independently read all colours and inspect packets, every B5/R7 subset, all 32 weak partitions per seven-subset, all junctions. Enumerate all 924 six-subsets, all actual R6, and an actual disjoint pair. Recompute terminal pair ranks and actual source/end sets. If SAT, enumerate at most 4096 vertex subsets for exact minimum transversals and alpha=N-tau; save all colours, all red6 and all minimum transversals. Clause-check the full SAT assignment independently of this semantic audit.

Positive domain/negative packing controls are established D11 tmp/d7_global_critical_20261027/canonical_R11_assignment.json with its exact canonical_R11_counterreceipt.json, and established D15 tmp/d7_critical_full_core_20261027/minor15/sat_colors.json with its semantic receipt. The source report is .trellis/tasks/10-19-nr7-structure-capacity/research/D7_CRITICAL_FULL_CORE_EQUALITY_AND_ENDPOINT_CALIBRATION_20261027.md. Input byte hashes are sealed in INPUT_MANIFEST.json before implementation. Test all sixteen packet words against the hard-coded eight valid words. All-red12 and all-blue12 must fail the expected domain prohibitions. Any CNF/semantic mismatch stops before the one science solve.

## Hard resource and evidence gate

Only authoritative Linux executes generation/checking/solving. One AE kissat proof-producing controlled external run: executable /data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat; wall and CPU 60 s; AS 4 GiB; outer supervisor 90 s; TERM then KILL after 2 s; proof <=256 MiB enforced by RLIMIT_FSIZE plus polling. No retry or extension. Read proof syntax and checker route before invocation. On UNSAT, one exact-CNF proof check under wall/CPU 60 s and AS 4 GiB; unavailable checker means raw UNSAT only. On SAT, colour validator and exact hypergraph characterization run under wall/CPU30 s and AS2 GiB. UNKNOWN stops. No PySAT/CaDiCaL, independent reviewer, model acceptance change, or old run restart.

Owned writes are only this fresh local directory and the corresponding fresh authoritative /data/ktqiu_hdd/math_agent/tmp/d7_disjoint_path_mechanism_20261027. Existing files, jobs, proofs, CNFs, task state, acceptance and session pointers are protected. Exact input and protected-file observations are saved as manifests, never used for restoration.
