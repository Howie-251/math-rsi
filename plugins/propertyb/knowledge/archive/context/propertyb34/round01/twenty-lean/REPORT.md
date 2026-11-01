# T34 round 1: complete twenty-vertex Lean branches

The original T34 target remains unchanged. This continuation first closes the actual 20-point branch with minimum degree seven and exactly two degree-seven vertices. Old T32/T33 sources and delivered artifacts are unchanged.

## Exactly two seven-degree vertices

`Aris4Math.ThirtyFour.TwentySevenTwo.propertyB_of_two_sevens` proves `PropertyB H` for an actual simple five-uniform H on `Fin 20`, given pair coverage, exactly 34 edges, all degrees at least seven, and exactly two degree-seven points. No supplied type table, probability bound, bad-pair certificate, or residual classification is a theorem premise.

The proof connects the following actual objects:

1. `TwentyStructure.eights_budget` obtains at least six actual degree-eight points from incidence sum 170 and the two seven-points.
2. Existing unit/strong double-lock bounds restrict the seven-seven codegree to two or three; the new 41-case triple module leaves only codegree two. For each eight-point its two cross-codegrees are both one with common triple count zero, or both two.
3. On every pair of eight-points, strong eight-eight doubles first bound their codegree by three. The four-lock type domain has exactly 169 labelled inputs: 168 have strict bounds, while one residue has all high traces zero, all four seven-eight codegrees one, and the eight-eight codegree two. The coverage theorem is kernel checked and its assumptions are derived from the actual pair inventories and bounds on actual traces.
4. The residue applies simultaneously to all choices of two eight-points. Thus each seven-point is a unit neighbor of every eight-point, and an edge through the first seven-point contains at most one eight-point. The two edges containing both seven-points contain no eight-point. `Incidence.neighbor_capacity` double-counts actual edges and proves `|L|+2≤7`, contradicting `|L|≥6`.

The 168 strict four-lock inputs use one uniform exact dual interface. Nested total/pure quotas are converted to a two-multiplier nonnegative dual; the five already supplied avoided-lock certificates also fit two terms per center. The generator independently recomputes the rational quota, capacity and weight inequality. Lean then checks the actual numeric inequality and calls the existing proved `realized_refined_deduction`, whose input is the same actual H. Overlapping quotas are not added as independent deductions. Seven inputs would fail with the weaker maximum of separate total/pure bounds, so this stronger interface is mathematically necessary for this recorded table.

## Executed builds

- `lake build Aris4Math.ThirtyFour.TwentySevenTwoTriples`: 1004 jobs, exit zero, `build-two-triples-r2.log`.
- `lake build Aris4Math.ThirtyFour.TwentySevenTwoQuad`: 1011 jobs, exit zero, `build-two-quad.log`; Data 51 seconds, Numeric 441 seconds, actual coverage/caller 21 seconds.
- `lake build Aris4Math.ThirtyFour.TwentySevenTwo Aris4Math.ThirtyFour.QuadTransport`: 1025 jobs, exit zero, `build-two-complete.log`. The final two-seven theorem has only `propext`, `Classical.choice`, `Quot.sound` as transitive axioms.

`QuadTransport` proves actual trace transport under lock permutations for the next unique-seven branch. This checked helper is not a proof of that next branch.

The updated Assembly removes the two-seven regime from its remaining proposition. The current twenty-point obligations are exactly one seven-point or minimum degree exactly eight. Vertex counts 21–25 remain global remaining obligations; no complete T34 theorem or new global lower bound has been established.

## Next actual obligation

Continue the unique-seven branch from `SEVEN_ONE.md`. Its 384 saved strict four-lock witnesses occupy 99 orbits under the three degree-eight labels; the checked trace transport permits using representative witnesses. Complete local coverage, triple redirects and the six residuals' universal incidence contradiction still need Lean connections. The degree-eight branch follows after this one.

The updated `lake build Aris4Math.ThirtyFour.Assembly` completed 1040 jobs, exit zero (`build-assembly-two.log`). `TwoAudit.lean` independently imports it, restates the two-seven branch using only a bare edge set and filtered-edge degrees, and obtains an actual Bool coloring. It also restates the arbitrary `[Finite V]` original target conditionally on the newly smaller remaining goal. `two-audit.log` records both successful elaborations and only the standard three axioms. The original twenty-point `r=2` obligation is now internally discharged in Assembly.

For the next branches, `TwentyRemainingTriples` now contains 88 labelled strict triple witnesses: fifty for (7,8,8), and all thirty-eight labelled permutations of the fourteen (8,8,8) representatives. The actual caller reconstructs the real type multiplicities and supplies total/pure deletion. Its explicit build completed 1004 jobs, exit zero, in `build-remaining-triples.log` (98 seconds). This helper alone does not close the unique-seven or minimum-eight branch.

## Unique seven-degree point: complete actual branch (13:53 UTC)

`TwentySevenOne.propertyB_of_one_seven` proves Property B for the actual pair-covering 20-point hypergraph with exactly34 edges, minimum degree at least7, and exactly one point of degree7. `build-one-complete.log` finishes 1030 jobs successfully; its transitive axioms are precisely `propext`, `Classical.choice`, and `Quot.sound`.

The actual four-lock classification uses99 permutation representatives and the related88 labelled strict triple profiles (50 of degrees7,8,8 and38 of degrees8,8,8). Exact common triples are connected to exact triple-plus-quadruple traces in `QuadIncidence`; `QuadTransport` proves relabelling of actual traces. `TwentySevenOneClassification.coverage` checks the complete bounded local input domain in the Lean kernel and maps every strict alternative back to the actual input.

The remaining predicates are deliberately weaker than listing the six original residual orbits. They say: no four-point common edge; the three codegrees from the seven-degree point never sum to4; and if all three are1, all high exact traces vanish. These properties alone suffice. If every low neighbor is unit, each of the seven incident edges meets at most one of the at least eight degree-eight points. Otherwise there is a double neighbor; at most one degree-eight point is a unit neighbor, giving at least15 incidences, whereas each of the seven incident edges meets at most two degree-eight points, giving at most14. Both contradictions are formalized for actual edges.

The independent Python `ONE_COVERAGE_CHECK.json` covers674 inventory-consistent local inputs:343 satisfy the weaker residual,201 take a strict triple, and130 take a strict quad. This is supporting arithmetic inspection; Lean's finite classification and actual callers supply the formal proof.

`Assembly.lean` now leaves exactly the minimum-degree-eight 20-point regime plus all21–25-point cases. Explicit Assembly build completes1048 jobs (`build-assembly-one.log`). `OneAudit.lean` independently reconstructs the original Bool coloring conclusion from a raw five-uniform Finset edge family and the unique-seven hypotheses, and separately reconstructs the original arbitrary-`[Finite V]` conditional theorem from the new `RemainingGoal`. `one-audit.log` exits0 and all three audited declarations use only the standard three axioms. This is not a proof of `RemainingGoal` or of the full T34 target.

Next: the minimum-degree-eight branch.79 exact four-lock certificates are generated in `EIGHT_QUAD_DATA.json`; their Lean build and the general graph/incidence argument are in progress.

## Complete twenty-point branch (2026-10-13 14:23 UTC)

The whole twenty-point obligation is now proved:

```lean
Aris4Math.ThirtyFour.twenty_propertyB :
  ∀ H : Simple5Hypergraph (Fin 20),
    H.PairCovering → H.edges.card = 34 → PropertyB H
```

`Twenty.lean` dispatches actual degrees to the already proved degree≤6 branch, at least three sevens, exactly two sevens, exactly one seven, and minimum degree eight. It has no local profile, graph, probability, or certificate premise. The minimum-eight caller is `TwentyEight.propertyB_of_minimum_eight`; its only assumptions are actual pair coverage,34 edges, and minimum degree at least8.

The eight-degree branch includes the79 strict four-lock representatives and all relevant triple/double witnesses. It first proves that every six-pair vector in `{1,2,3}^6` has one of66 representatives under an actual permutation of the four selected vertices. The explicit representative choice is checked in the kernel. High traces are then classified with their true pair inventories. The final actual caller transports both codegrees and exact traces, including conversion of common triple counts to exact triple-plus-quadruple counts. This closes the whole local classification without assuming a residual list.

The general remainder is the shorter argument in `EIGHT_SIMPLIFICATION.md`. `TwentyEightLocal` rules out actual codegree3. `TwentyEightGraph` derives the graph constraints and uses actual codegree-one edges to identify the two C4 witnesses. `UnitGraph` proves the universal-vertex/maximum-unit-degree-one dichotomy without graph enumeration. `TwentyEight` closes both cases by actual per-edge incidence capacities. `Incidence.extra_capacity` accounts for the lost capacity of edges containing a distinguished extra point. No whole-hypergraph enumeration is used.

Validation:

- `build-twenty-complete.log`: explicit `lake build Aris4Math.ThirtyFour.Twenty`,1045 jobs, successful; the complete branch and minimum-eight theorem have exactly the standard three transitive axioms.
- `TwentyAudit.lean` / `twenty-audit.log`: independent import, raw five-uniform Finset edge family, original Bool coloring, and both colors explicitly occurring in each edge; all4 audited declarations use only `propext`, `Classical.choice`, `Quot.sound`. Exit0.
- `build-assembly-twenty.log`: explicit `lake build Aris4Math.ThirtyFour.Assembly`,1059 jobs, successful.
- `AssemblyAudit.lean` / `assembly-audit.log`: bare `[Finite V]`, arbitrary five-uniform Finset edge family and≤34 edges, conditional on exactly the new remaining21–25-point obligations; independent import succeeds, both audited declarations use only the standard three axioms. Exit0.
- Source scan of all `ThirtyFour/*.lean` finds no `sorry`, `admit`, new axiom, or `native_decide`.

`Assembly.RemainingGoal` now means only actual pair-covering34-edge hypergraphs on21–25 points. `target_iff_remaining_goal` proves this is equivalent to unrestricted `Target34`; the remaining proposition itself has not been proved. T34 and the new global lower bound are not yet claimed.

The numeric79-representative build took219 seconds for the numeric module plus19 seconds for its data; the final66-pair canonical classification took175 seconds and its actual caller8 seconds. Two larger direct classification attempts were intentionally interrupted while replacing redundant kernel searches with explicit kernel-checked representatives; those development logs are not acceptance records. The authoritative finished records are the clean complete-twenty and Assembly logs listed above.

Reproduction from the project root:

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
cd formal
lake build Aris4Math.ThirtyFour.Assembly
lake env lean ../context/propertyb34/round01/twenty-lean/TwentyAudit.lean
lake env lean ../context/propertyb34/round01/twenty-lean/AssemblyAudit.lean
```

Next formal obligation, as assigned:21-point minimum degree5, then minimum degree6; afterward a reusable shared-bad-vector weak-dual interface where the new mathematical branches require it. Source and evidence for all three twenty-point residual branches are preserved here; no T32/T33 file was changed.
