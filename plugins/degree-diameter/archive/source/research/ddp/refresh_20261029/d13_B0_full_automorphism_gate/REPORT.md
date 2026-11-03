# Stop before verification: only the core involution is bound

The bounded read does **not** supply a nontrivial literal automorphism of the entire original51417-vertex graph. No full-source automorphism check was run, because the corresponding permutation of its863 peripheral vertices is not provided. This does not prove that the full graph has no nontrivial automorphism.

## What is explicit

The saved construction binding uses a50554-vertex partial-fold core over33397 classes. The raw involution is `phi[p]=tau[tau[p]]`. On each saved two-vertex split class `{u,v}`, the candidate core permutation swaps u and v; singleton classes are fixed. The existing binder builds this `swap` array only through `core_n` and checks

`{swap[v] : v in core[u]} == core[swap[u]]`

only on core-to-core adjacency. This is the simultaneous split-class swap; its validity for the core does not address edges incident with labels50554,…,51416.

## Missing whole-source binding

The cached primary description of the current51417 source says that colors and copies of H(3) were chosen jointly, pencil vertices have extra anchors with reserved slots, and twin-vertex packing fills remaining slots. Thus these peripherals are actual graph attachments, not an automatically identified geometric orbit whose Frobenius action can be assumed.

`SOURCE_FACTS.json` explicitly records that the current source's split/color/copies witness was not included in the saved complete deposit file table. The local binder recovers exact core-class data, but its peripheral output only records core-pin counts, extra-neighbor counts, and possible H3 core-star signature parents. It supplies no full peripheral-image permutation and performs no full-graph involution check. A core-star signature alone also does not determine preservation of peripheral-to-peripheral edges.

The accepted40 records and fixed extension generator attach new vertices to literal source labels while retaining old edges. They do not define an automorphism of original B0 or identify the original peripheral labels under Frobenius. Hence they cannot resolve this gap.

No arbitrary rule “fix all863 peripherals” was substituted for a recovered extension. Likewise no inference from core degree, Galois-stable geometric neighborhoods, or the old fullstar tests was used as a full-source automorphism certificate.

## Exact read scope and terminal result

Five source files, all under `research/ddp/more_graphs_20261027/d13_D5_h9_transfer/`:

1. `public_desc_g5.html`: cached primary construction description, specifically the current51417 section.
2. `SOURCE_FACTS.json`: current source receipt and missing deposit-witness notice.
3. `bind_source.py`: actual scope of the core permutation and peripheral profiling.
4. `singlefault_star_probe/accepted_family40.json`: original base binding and40 literal accepted extensions.
5. `singlefault_star_probe/generate.py`: existing fixed extension generator, which copies the literal base and appends prescribed edges.

Only matching D13/Frobenius/core-binding entries of `research-wiki/DDP_METHOD_LEDGER.md` were consulted; no general table or automorphism-class search was performed. The old Baer/Galois neighborhood pools and fullstar domains were not rerun.

Terminal: **PERIPHERAL_BINDING_MISSING_IN_BOUNDED_READ_SCOPE**. No original graph/edge list read, no full permutation produced, no edge verification, no D5/BFS, no transported neighborhood pool, no optimizer, and no installation. Parent decision is required before any broader source recovery or different specified permutation. This is not a proof of nonexistence of full-source automorphisms.
