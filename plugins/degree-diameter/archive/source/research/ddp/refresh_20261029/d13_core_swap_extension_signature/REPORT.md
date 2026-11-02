# The fixed core involution cannot extend; four literal new capacity-legal sets remain

Two different questions were tested with one read of original B0. The full-automorphism extension has a strict negative answer. The separately authorized rule “swap core labels but keep peripheral guard IDs” produces four new individually capacity-legal sets, whose coverage was not numerically tested.

## Necessary signature obstruction to any full extension

The saved core partition recovers17157 split-pair swaps on50554 labels; its core-automorphism property was inherited, not rechecked. The863 peripherals have843 distinct core-neighbor signatures:826 singleton groups,14 groups of size2, and3 groups of size3.

The first mismatch, at the68th signature group in increasing least-peripheral-label order, is peripheral vertex50629. Its exact core-neighbor signature is

`[61,5156,10143,15136,21698,28257,34765,38196,41629,44965]`.

Applying the fixed core swap yields

`[64,5159,10146,15130,21692,28251,34768,38199,41632,44965]`.

The original signature occurs once. The transformed signature occurs **zero** times among all863 peripheral vertices. Comparison stopped at this witness.

Any full-graph automorphism restricting to this core swap maps the entire core onto itself, and therefore permutes the remaining peripherals. Adjacency to the core then forces each peripheral signature to map to its swapped signature, with equal multiplicity. The displayed1-versus0 mismatch is impossible. Thus **this specified core swap has no extension to an automorphism of original51417**, even allowing an arbitrary peripheral permutation. No assumption that peripherals are fixed was used. This does not exclude other full-graph automorphisms.

`PERIPHERAL_SIGNATURES.json` contains every original signature and its complete vertex group. `RESULT.json` contains the obstruction. No full-edge automorphism test or duplicate-group assignment was needed.

## Different candidate rule: peripheral guard IDs kept fixed

Apply the saved core swap to the core members of each cached successful S_i, and retain the literal IDs of its peripheral members. This is an explicit candidate rule, not a claimed full-source automorphism.

All40 sets differ from their own original S_i. There are38 distinct sets outside the original40 pool. Six rows individually satisfy B0's degree13 spare-port and size bounds, but two are already in the original pool (indices15 and23). The four genuinely new individually capacity-legal sets are:

| Original index | Literal candidate S | Size |
|---|---|---:|
| 0 | 4639,7030,19110,22466,33064,34736,41546,43286,49935,50577 | 10 |
| 8 | 4981,12230,18124,26290,30226,34924,40363,44218,48486,51337 | 10 |
| 17 | 10255,10846,11409,11947,12659,13395,14068,14418,14782,50591 | 10 |
| 37 | 2813,9214,15101,25662,33884,38121,38574,42842,48533,50577,50578 | 11 |

Index37 equals original S_0 together with50578. Its original-B0 R4 coverage therefore follows immediately from the already saved S_0 certificate, without BFS. However it consumes a superset of S_0's ports and cannot improve the static unit-benefit packing objective; S_0 dominates it. No coverage claim is made for indices0,8,17. In particular, preservation of core-only paths does not establish preservation of routes using peripherals.

`CORE_SWAP_FIXED_PERIPHERAL_CANDIDATES.json` stores all40 originals, images, pool-membership flags, individual capacity results and specific blocked ports. These are candidates for parent review, not actual additional accepted graphs or a jointly feasible packing.

## Scope and cost

The PRED was saved before the signature and candidate calculations. One original source edge read; existing core Aut evidence reused. CPU0.304361371 seconds, within5CPU. No source diameter/BFS, neighborhood ball, SAT, packing, full-edge Aut check, new graph generation, altered guard, or additional seed. Both authorized diagnostics are terminal; no subsequent candidate verification was started.
