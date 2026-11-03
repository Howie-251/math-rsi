# No order65 graph: a finite-field trace proof

Status: complete paper derivation, fresh proof-checker and Gemini B5 accepted.
The actual original-graph caller is compiled in formal/DegreeDiameter/Moore65.lean;
formal/logs/review-moore65-audit.log records only standard axioms. This replaces
the implementation route without changing the original graph domain.

Suppose G is a finite simple undirected graph on65 vertices, with maximum
degree at most8 and every pair of distinct vertices joined by a path of length
one or two. The root ball bound makes G 8-regular. Let A be its integer adjacency
matrix, J the all-ones matrix, and B=A²+A-7I-J its actual defect matrix.

B is entrywise nonnegative and has every row sum65-65=0. Each of its entries is
therefore0. Consequently

    A² + A = 7I + J,   AJ=JA=8J,   tr A=0,   J²=65J.

Reduce entries modulo29, and put M=2A+I. All subsequent equations are in the
matrix ring over the field F_29. Direct expansion gives

    M²=4J,   MJ=JM=17J,   tr M=65=7.

For every matrix X over F_29, tr(X^29)=(tr X)^29=tr X. One elementary proof
expands tr(X^29) as the sum over cyclic sequences of29 indices of products of
entries. Cyclic rotation preserves each product. Every nonconstant sequence
has an orbit of size29, so those contributions vanish in characteristic29.
The constant sequences contribute sum_i X_ii^29=sum_i X_ii. This also follows
from the fixed Mathlib theorem `Matrix.ZMod.trace_pow_card`.

On the other hand, J^k=65^(k-1)J for k>=1, by induction. Hence

    tr(M^29)
      = tr(M (M²)^14)
      = 4^14 · 65^13 · tr(MJ)
      = 17 · (4·65)^14
      = 17 · (-1)^14
      = 17.

The penultimate equality uses4·65=260=-1 in F_29. Thus the same trace equals
both7 and17, a contradiction. No order65 graph exists.

All matrices were built from the original graph. The only finite computation
is arithmetic modulo29; there is no graph enumeration, no imported spectral
classification, no floating-point step, and no unproved field extension premise.

The relevant Lean bridge consists of: the already compiled original-graph
defect identities; nonnegative sum-zero rows imply B=0; matrix reduction to
ZMod29; the displayed power identity; and the library trace Frobenius theorem.
The compiled caller is no_original_graph_card_65; its actual build and audit logs
are recorded above. The paper argument and the Lean proof have the same original scope.
