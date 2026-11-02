# Prepared model, no solver invocation

`run_once.py --prepare-only` completed with21722 variables and74336 clauses, encoding CPU0.122005083 seconds. The380 primary variables include every noninternal edge between the29 degree2 motif vertices, including eligible edges within the seven-vertex chain. Centers2/4 have no such variable. Each free vertex has exactly2 selected extra edges, so a decoded graph has33 fixed plus29 variable edges, hence62 total.

R2 uses exact bidirectional AND/OR definitions. Every distinct pair requires adjacency or a length3 walk; nonadjacent3-walks are automatically nonbacktracking. Self routes are provided by the fixed triangles. The model contains no C33 capacity cuts or fixed external root edges.

Only the eight disjoint new K3 blocks are canonically relabeled; the first parent is not fixed. `LABEL_SCOPE.md` proves preservation, and the degree5 agent independently confirmed that argument in a read-only message. No solver was used for this confirmation.

`--solve` reads this saved CNF and variable map without regenerating them. It rejects an existing HANDLE/TERMINAL, uses one90-second solver call, and reports total CPU including the saved preparation cost. Root review is pending; neither mode defaults to solving.

On SAT, the script rebuilds the31-point graph and checks all961 ordered adjacent-or-NB3 conditions, including self. It exports literal edges/adjacency and witnesses only. Because the fixed triangles overlap, it intentionally does not reuse the triangle-factor port decoder; general2-factorization and F5 generation are left to root.
