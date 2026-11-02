# A70 actual load assembly checkpoint

`GQ77Cubic22Clone70Inputs` actual compilation exited0, measured1.992804CPU/3.302wall, one worker,60CPU per-module limit. `load_le_six` is closed and its printed axioms are exactly propext, Classical.choice, Quot.sound.

The proof reuses the actual already-closed65base load≤1 on the original160050source. For an arbitrary source vertex w, its adjacent base-center subtype has at most one element. The adjacent6600clone-index subtype maps to `Fin6` by the copy coordinate. Equal copy coordinates plus base-index uniqueness imply equal `(copy,base)` pairs, hence equal clone indices by `clonePair.injective`. `Fintype.card_le_of_injective` gives load≤6. No source-vertex/clone-index enumeration, center independence, or center injectivity assumption occurs. This is the elementary multiplicity argument specialized to this concrete instance.

The underlying graph is the immutable original `OppositeGQ77Spread.graph`, not the current161150graph. All clone neighbors remain original160050source endpoints, and new-new adjacency is False by the imported generic graph definition. The degree bound is source≤64 plus new load≤6. Source no-isolates, true bounded WalkD3, and nonD2 are imported from completed source/65proofs; the old Walk collapse theorem supplies the lower diameter bound for arbitrary clone multiplicity.

Typed order and recipe binding has checked all6600rows against producer `PREFIX_LOADS.csv`, and exports `FORMAL_ORDERED_CLONE_RECIPE.csv`. Fresh independent `SUMMARY.json` is now actualPASS: all5544000edges bound, all6600immutable64-neighborhoods exact, all6copies checked individually, all5121600source edges retained, and0new-new edges. Its separately generated O22/spread/index recipe matches the typed recipe. Formalization only reads that summary and recipe; no repeated large-edge validation or BFS is performed here.

Exact is running, followed by separate import/type/body/axiom Audit. Accepted counts and external reviews remain root owned.
