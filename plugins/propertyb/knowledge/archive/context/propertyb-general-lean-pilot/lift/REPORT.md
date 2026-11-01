# Actual finite-vertex relabeling

Source: `formal/Aris4Math/General/RS/Lift.lean`.
Namespace: `Aris4Math.General.RS`.

`relabel f E` maps each actual edge of `E` using `f.finsetCongr`, and maps the actual family using that equivalence's embedding. It preserves the number of distinct edges; no deduplication or loss of simple edges occurs.

The compiled interfaces are:

- `edge_relabel_card`, `mem_relabel`, and `relabel_card`: exact edge and family transport.
- `uniform_relabel_iff`: exactly the same uniformity degree after transport.
- `edge_relabel_inter` and `edge_relabel_inter_card`: actual edge intersections and their cardinalities are preserved, including the singleton-intersection condition.
- `singlePairs_relabel`: equality of the actual directed single-intersection pair sets after applying the product equivalence to the original pair set.
- `gamma_relabel`: exact gamma equality, derived from that pair-set equality.
- `bichromatic_relabel_iff`: an actual coloring on the target pulls back along the given vertex equivalence.
- `propertyB_relabel_iff`: Property B is equivalent in both representations.
- `propertyB_of_fin_criterion k C hfin E hU hC`: transfers any proved `Fin n` criterion `C F.card (gamma F)` to arbitrary `[Finite V]`. This allows RS's real-parameter expression to be supplied by closing `C` over its numerical parameters. No probability theorem is assumed inside the transport itself.
- `pilotTarget_of_fin hfin`: supplies the exact `PilotTarget` from an actual finite-index 17-uniform theorem. It creates `Fintype.ofFinite V`, chooses `Fintype.equivFin V`, transports the real family, invokes the supplied theorem with the transported exact count, and pulls its coloring back.

The last two theorems are transport interfaces, not independent proofs of the RS criterion or the pilot. Their only theorem premise is the corresponding `Fin n` result, which the root assembly must actually prove and apply.

Verification: `BUILD.log` records source compilation and generation of `formal/.lake/build/lib/lean/Aris4Math/General/RS/Lift.olean`, exit 0, 7.82 s wall, 1.45 s user CPU, 1.79 s system CPU, max RSS 1,226,457,088 bytes. All audited declarations use only `propext`, `Classical.choice`, and `Quot.sound` (the direct Property B equivalence does not require choice). `CALLER.log` independently imports the module and restates both transport outputs using bare `[Finite V]`, literal edge uniformity, and explicit true/false witnesses. No `sorry`, new axiom, `native_decide`, full shared build, or change to Definitions is used.

Reproduce from `formal/`:

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
lake env lean -o .lake/build/lib/lean/Aris4Math/General/RS/Lift.olean Aris4Math/General/RS/Lift.lean
lake env lean ../context/propertyb-general-lean-pilot/lift/Caller.lean
```

Independent caller result: `CALLER.log` exit 0, 7.70 s wall, 1.20 s user CPU, 1.76 s system CPU, max RSS 1,196,523,520 bytes. Both bare original-form caller exports have exactly the three standard axioms. The delegated transport task has no remaining obligation; root integration into the actual probability criterion and pilot theorem remains necessary.
