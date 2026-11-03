# A70 typed encoding checkpoint

`GQ77Cubic22Clone70Definitions` actual compilation exited0 with pinned Lean4.24.0, explicit existing `LEAN_PATH`, one compiler worker. Measured2.100205CPU;59.809wall included observed import I/O progress. No old module or compiled cache was changed or rebuilt.

The carrier is literally `(Fin160000⊕Fin50)⊕Fin6600`. `clonePair : Fin6600 ≃ Fin6×Fin1100`; `center k = GQ77Cubic22Clone65.center (clonePair k).2`. The graph's printed body is exactly `FullNeighborhoodClones.graph OppositeGQ77Spread.graph center`, so the source is the original closed160050graph, not the161150graph. The new `label : Vertex ≃ Fin166650` preserves all old source labels, and the closed `label_new_copy` gives160050+1100*copy+50*i+j.

The lightweight binding actualPASS compares the typed decomposition and all6600exported center/label rows with the producer's actual `PREFIX_LOADS.csv`, including the copy/base indices, source owner, new label, and stated degree-prefix recipe. Export: `FORMAL_ORDERED_CLONE_RECIPE.csv`. It also compares all1100base centers and exact O22/spread order with the frozen accepted base definitions. Measured0.054900CPU,0large edgefile reads,0BFS. The immutable1100source neighborhoods reuse the existing accepted base binding; whole new edgefile correctness is delegated to fresh independent acceptance and remains pending here.

Next: use the already proved base load≤1. On adjacent clone indices, projection to the copy coordinate `Fin6` is injective: equal copy and the existing uniqueness of adjacent base indices force equal pairs. This bounds the new load by6 without enumerating source-vertex/clone pairs or assuming center independence/injectivity. Exact will use the unchanged source≤64 and the existing arbitrary-index clone Walk/nonD2 theorems.

This is one fixed degree70instance; target166650, degree≤70, true bounded WalkD3 and nonD2, no remaining certificate premises. Root best-located guarantee164500 is2150smaller in the bounded comparison; global record and priority remain unconfirmed. A/B/C reviews are root coordinated.
