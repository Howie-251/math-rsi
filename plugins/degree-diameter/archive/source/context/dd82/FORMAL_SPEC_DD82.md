# Original specification and proof obligations

The original mathematical specification below is unchanged. Current phase execution is N61_GLOBAL_CLOSURE_SPECTRAL_GOAL_20261019.md: decide order61 through global closure and full spectral arithmetic; orders58–60 are paused and62–65 remain inherited. Lean is final acceptance, not the discovery queue.
PROJECT_ROOT is /inspire/hdd/global_user/mahaitong-240108120090/ar4math (the user-facing project/global_user path is a symlink to this directory).

For an arbitrary finite vertex type V and a simple undirected graph G, require every degree at most 8 and, for every distinct u,v, either Adj(u,v) or an actual w with Adj(u,w) and Adj(w,v). The empty graph and the singleton are allowed. No connectedness, regularity, symmetry, root, partition or certificate premise is added to the definition.

Exists82(n) means a graph with exactly n vertices satisfying those conditions. The final assertion IsExact82(n*) must supply both Exists82(n*) and forall m, Exists82(m) -> m <= n*, for one concretely determined integer n*. The intended arbitrary-finite-type upper-bound theorem is universe polymorphic; the small-universe existential representation in the initial draft requires a finite relabelling bridge when connecting larger universes.

Current definition source: formal/DegreeDiameter/Definitions.lean. Definitions, Moore/regularity, actual defect, and several further modules have since compiled; current build evidence is indexed by STATUS_AND_DEPENDENCIES.md. No exact theorem is claimed. Full Lean closure remains a later acceptance stage.

Required connections:
1. Arbitrary original graph -> Moore bound, then regularity above 57.
2. Actual adjacency matrix -> integer defect B=A^2+A-7I-J, exact row sums and root/triangle budgets.
3. Complete explicit witness -> original graph predicates and Exists82(n*).
4. Every remaining possible order -> full-scope exclusion; old conditional and RAW results retain their precise premises until discharged.
5. Lower and global upper bounds -> actual exact-order theorem; print definitions, theorem type and transitive axioms, compile the actual new main module and independently import it.

No sorry, new unproved axioms or native_decide. External checks and reviewer agreement are not Lean proofs. Gemini A/B/C reviews are tracked separately from kernel verification. No exact value is presumed.
