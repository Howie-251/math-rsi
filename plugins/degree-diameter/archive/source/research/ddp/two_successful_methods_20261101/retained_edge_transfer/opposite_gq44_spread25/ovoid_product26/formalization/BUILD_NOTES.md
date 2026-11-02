# Build notes

Use the existing formal project, pinned Lean4.24/cache and saved explicit
LEAN_PATH through compile.py/directLean-j1. New order:
OvoidSpreadCloneCapacity→OvoidProduct26Definitions→Inputs→Exact→independentAudit.
The original FullNeighborhoodClones, source7242 and its generic geometry proofs
are imported unchanged; no old module/cache rebuild or lake resolution occurs.

Each new module first-attempt PASS; each115CPU hard limit,300CPU total, one
worker. Measured Lean child CPU19.021851. The first generic import took61wall
seconds but only2.162CPU while cache data loaded; it was not restarted.

The graph stores a fixed source constant, not mutable current adjacency.
check_binding.py reads the ORIGINAL7242 edge table once, checks each of289
ordered owners and its25 immutable pins against all3 actual recipe tables,
then binds the full97750edge final graph. It reuses the source's already-complete
formula binding and runs no BFS. Product index17*i+j is formalized by the actual
Fin289 equivalence and total label; adjacent centers remain allowed.

Finite hO uses only17 owner checks plus425 positive line positions with an85-line
index certificate. It proves at-most-one ovoid INDEX per original line. There
is no Q-algebra formalization, exactregularity proof, or source-capacity-optimality
claim in this scope. All actual degree/Walk/lower-bound caller hypotheses are
closed before the final unconditional theorem and separate Audit.
