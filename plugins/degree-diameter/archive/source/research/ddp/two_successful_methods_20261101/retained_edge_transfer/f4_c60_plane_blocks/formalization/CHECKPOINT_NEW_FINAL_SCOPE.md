# Actual final clone encoding and two recipe witnesses

Kernel status: both concrete results and separate import/type/axiom audit PASS. New-scope external A/B/C review is pending root coordination. Earlier paper A or fixed3840 review does not review this new encoding. This packet contains final actual source/types and is not a plan review.

Original objects: ../PROOF.md, ../RECIPE_d21.json, ../RECIPE_d22.json and ../../TRANSVERSE_BLOCK_LEMMA.md. Each new vertex copies its owner's full original source open neighborhood; all3840-source edges remain, and no two new vertices are adjacent. The144/352 ordered owners are exactly the selected9/22controller layers times the16 listed GF4 plane codes, in actual recipe generation order. The required conclusions are order3984/4192, degree≤21/22, genuine-walk diameter≤3 and not≤2.

Actual final source and paths under formal/DegreeDiameter/Portfolio/:

1. FullNeighborhoodClones.lean defines `graph G center : SimpleGraph (V ⊕ J)` by old-old=G, old-new=G.Adj old(centerj), new-new=False. Read the actual bodies of graph, collapse, oldHom and collapseHom. `old_walk_bound_iff` proves all old-old walk bounds in both directions by same-length maps; `diameterAtMost` proves D≥3 inheritance from no-isolated source; degree_old/new are exact finite-neighborhood cardinality formulas. The general theorem is not counted as a concrete graph instance.
2. F4PlaneBlockClonesDefinitions.lean fixes actual planeCode, layers21/layers22, form, center, V21/V22 and graph21/graph22. The carrier types are explicitly `Fin3840 ⊕ Fin144` and `Fin3840 ⊕ Fin352`. `label21` and `label22` are explicit equivalences to Fin3984/Fin4192. Theorems label21_old/new and label22_old/new in Exact prove that old labels remain v and new labels are3840+j.
3. F4PlaneBlockClonesPlane.lean proves the normal `(1,1,w)` is nonzero on every source direction and its16listed plane codes are zero and distinct. Using the existing actual-source adjacency equivalence, two neighbors of v in the same plane block use the same source port; normal(step)=normal(base)+t*normal(direction), finite4-element cancellation gives equal noise, and thus equal plane index. No Field/NoZeroDivisors instance or huge adjacency sweep is assumed.
4. F4PlaneBlockClonesCapacity.lean kernel-checks the actual60controller rows: at most1 or2 selected block indices, respectively, can be neighbors of each controller. F4PlaneBlockClonesLoad.lean maps every actual adjacent clone index into this allowed-block subtype; plane_neighbor_unique proves this map injective. Therefore the old load≤1 for graph21 and≤2 for graph22 is a proved consequence of the actual recipes, not a theorem input left for the user.
5. F4PlaneBlockClonesExact.lean supplies all caller premises from those proved capacities and the unchanged, already-compiled source theorems in F4Graph3840Exact.lean. Old degrees≤20 plus actual load≤1/2 give the respective degree bounds; no-isolated source comes from an actual forward edge; generic clone D3 applies; collapse would turn any old-old extension walk≤2 into a source walk≤2, contradicting the fixed3840 lower bound.

Actual exported theorems in namespace DegreeDiameter.Portfolio.F4PlaneBlockClones:

```
concrete_d21_n3984 :
  Fintype.card V21 = 3984 ∧ (∀ v, graph21.degree v ≤ 21) ∧
  DiameterAtMost graph21 3 ∧ ¬DiameterAtMost graph21 2

concrete_d22_n4192 :
  Fintype.card V22 = 4192 ∧ (∀ v, graph22.degree v ≤ 22) ∧
  DiameterAtMost graph22 3 ∧ ¬DiameterAtMost graph22 2
```

There are no certificate, capacity, source-degree or source-diameter premises on these final theorems. DiameterAtMost is the existing SingleExtension definition `∀u v, ∃w:G.Walk u v,w.length≤D`.

Executed evidence in this folder:

- INPUT_BINDING_CHECK.json: reads back the current Lean plane/layer literals, compares ordered144/352 owner arrays against every actual RECIPE step, compares ordered new labels at every index to3840+j, and checks controller/plane/copy metadata. Comparison is list equality, not set equality. The permutation is the identity. This is exact formula/recipe labeling, with no Lean ASCII parser claim.
- FINAL_COMPILE_RESULT.json: all new module receipts and exact scope; total new build including failed API attempts33.522509CPU, one worker, every module≤115CPU. Old3840 modules were unchanged and not recompiled.
- F4PlaneBlockClonesExact.log and _RESULT.json: actual unconditional target compilation, exit0.
- F4PlaneBlockClonesAudit.log and _RESULT.json: separate import of formal/F4PlaneBlockClonesAudit.lean printed definitions, label equalities, final types and axioms, exit0.
- Both final results have exactly `[propext, Classical.choice, Quot.sound]` as transitive axioms. No sorryAx, unproved extra axiom or native_decide lies on either dependency chain.

Scope boundaries: concrete graphs are on the stated Sum carriers with proved explicit Fin label equivalences. No separate transported Fin-graph theorem, ASCII parsing theorem, exact degree histogram or edge-count Lean theorem is claimed. Independent graph acceptance is inherited; no graph BFS/solver/source distance check was rerun. Public novelty is separate.

Reviewer task: independently back-translate the actual new definition bodies and final printed types, then trace the arbitrary source/clone cases and actual degree-load injection to the two unconditional callers. Identify the smallest concrete semantic or mathematical gap, or state none found in the inspected source. State exactly which files/logs were read and whether any code was actually run. Avoid dumping numeric tables; preserve the distinction between a checked theorem and incomplete external checkpoints.
