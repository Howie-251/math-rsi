# Lean proof: every 33-edge simple 5-uniform hypergraph has Property B

Import `Aris4Math.ThirtyThree.Main`. The theorem
`Aris4Math.propertyB_of_at_most_thirty_three : Target33`
quantifies over arbitrary finite vertex types and assumes only a simple
five-uniform edge set with at most 33 edges. It proves **m(5) ≥ 34**.

`ReviewAudit33.lean` independently spells the original statement using a bare
finite edge set and derives both colors in every edge, then prints the actual
definitions, theorem types, and eight transitive-axiom audits. The dependencies
are only `propext`, `Classical.choice`, and `Quot.sound`.

From this directory, using the pinned Lean 4.24.0 and `lake-manifest.json`:

```sh
lake build Aris4Math.ThirtyThree.Main
lake env lean ReviewAudit33.lean
```

On a new machine with elan, run `lake exe cache get` first to fetch dependency
caches. Keep the manifest; do not run `lake update` as a reproduction step.
The default `lake build` still builds the separately retained 32-edge result.

On the original Mac, the project-local toolchain can be selected with:

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
```

See `../context/propertyb33/FORMAL_VERIFICATION.md` for recorded execution scope,
`../context/propertyb33/round02/final-assembly/` for the actual outputs, and
`../PROOF_PACKAGE_33.html` for the complete mathematical reading edition.
The named build completed successfully with 1138 jobs on 2026-10-13; the
post-build original-statement audit also exited 0. These were local incremental
checks with the locked cache retained. Human reproduction instructions are in
`../HANDOFF_FOR_REVIEW_33.md`.
The proof uses general counting and proved local classifications with exact
kernel arithmetic; it does not enumerate all hypergraphs.
