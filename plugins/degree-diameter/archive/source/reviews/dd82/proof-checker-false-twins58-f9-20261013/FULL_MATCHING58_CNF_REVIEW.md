# Independent check of the full false-twin58 CNF

Run: `dd82-v3-f9-c7-20261013-0749`. Local verdict: **PASS** for the
mathematical representation, preparation source and actual seed/CNF
consistency. This is a same-family provisional review, not a solver
decision or an external Gemini acceptance. No solver or new BFS was run
by this check.

## Candidate preservation

The previously reviewed exact false-twin representation gives eight
independent six-point fibres and an arbitrary perfect matching between
every pair. Choose coordinates on the root fibre G0. Give a point in Gj
the coordinate of its unique neighbour in G0. This independently changes
the coordinates of each of the other seven fibres and sets all seven
root matchings to identity. The remaining 21 matchings are arbitrary;
no automorphism, translation relation, triangle restriction or seed edge
is imposed.

For points in distinct fibres Gi and Gj, a common neighbour cannot be a
twin, a parent, or a point in Gi or Gj. It must lie in one of the other
six fibres. Consequently direct adjacency or one of the 36 explicitly
listed two-edge paths is the complete coverage condition. Row and column
exactly-one constraints make each interface a perfect matching. Reverse
references transpose the same variables. The three clauses
`(-z,p), (-z,q), (z,-p,-q)` are equivalent to `z = (p AND q)`.
All other point pairs are automatically covered by the fixed scaffold.
The resulting CNF is therefore satisfiable exactly when some graph in
the full order-58 false-twin family satisfies the target requirements.

I read the complete preparation source, its decode function, the actual
encoding metadata, and the only reused archive functions `CNFEmitter`
and `add_iff_and`. They implement these conditions without additional
cuts. Importing their definitions does not execute the archive's old
searches or mathematical restrictions.

## Actual independent check

The standalone checker
[`full_matching58_independent_cnf_check.py`](../../../computations/dd82/construction/full_matching58_independent_cnf_check.py)
imports only the Python standard library and does not import the generator,
matrix routines, distance routines or CNF helper. It reads the actual
seed edge table and reconstructs all 28 permutations. Their union with
the 64 scaffold edges is exactly the 232-edge seed; every vertex has
degree eight and the seven root permutations are identity.

Using the recorded variable names only as identifiers, it independently
checks every primary variable's endpoints, all 36,288 path gates' two
geometric edges, and the complete 36-route set for each of the 1,008
cross-fibre point pairs. It then reads the actual DIMACS and verifies
every one of its 115,500 clauses against the complete required clause
sequence. The 37,296-variable assignment reconstructed from the edge
table agrees exactly with the saved seed assignment.

Exactly 105 clauses are false, all of them coverage clauses. The seed
has exactly the same labelled edges as the previously independently
BFS-checked f9 candidate, and the 105 failed pairs agree individually
with that existing BFS result. This comparison runs no new distance
computation. The full evidence, including all 28 reconstructed matchings,
false clause numbers and pairs, is
[`independent_cnf_check.json`](../../../computations/dd82/construction/full_matching58_run/independent_cnf_check.json).
The single check used 0.241846989 process CPU seconds and 0.349581100
wall seconds, excluding interpreter startup and final result writing.

## Exact conclusion

The saved input faithfully encodes the full false-twin58 family, rather
than only the already excluded f9 symmetry subfamily. The seed is still
a failed graph with 105 bad pairs. Only a subsequent satisfying model
with a complete independent graph check, or a verified UNSAT certificate
for this input, could decide this family. Even a full family exclusion
would not exclude arbitrary order-58 graphs without false twins.
