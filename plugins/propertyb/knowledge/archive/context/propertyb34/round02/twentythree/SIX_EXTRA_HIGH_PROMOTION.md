# Exact-six-low promotion reduction

This is a local continuation of the T34 proof, not a new bound or a completed branch.
The new actual modules are `TwentyThreeHighPromotion`, `TwentyThreeSparsePromotion`,
`TwentyThreeSixLowExtraCatalogue`, and `TwentyThreeExactlySixLowComplete`.

After the six-low classification, a noncolorable H has a normalized six-lock
inventory: empty multiplicity 11, six singleton multiplicities 2, nine pair
multiplicities 1, and two disjoint triple multiplicities 1. Its total is 34.
The six low vertices are the entire six-vertex set in this branch.

The actual degree sum gives at least ten degree-7/8 vertices. Each low vertex
has total excess codegree at most 2 over any outside subset; summed over six
lows this is at most 12. Thus an actual degree-7/8 vertex z outside the six can
be selected with total excess at most 1. Every codegree to a low is positive,
so their six-vector is either all ones or has exactly one 2.

Write p(T) for the number of actual old-T edges containing z and lambda_i for
the codegree from old lock i to z. Partitioning that same incidence gives

    p({i}) + sum_{T containing i, |T|>=2} p(T) = lambda_i.

Hence only the nine pair and two triple promotions are independent variables.
Each lies between zero and the old multiplicity (here 1). Their sum around
an old vertex is at most lambda_i. The existing BoundedAllocations enumerator
contains every actual such vector. There are 49 vectors for each of the six
possible positions of the double codegree, and 37 for the all-unit case:
331 vectors for each new degree, with no singleton or empty free variables.

For the production proof, an additional lossless reduction removes five of
those seven patterns. The residual old inventory is invariant under the
six explicit permutations with factoradic codes [0,301,260,111,4,5]. They
send old label 0 to any requested old label i. Their invariance on all old
trace counts and the identity transforming oneDouble(some i) to
oneDouble(some 0) are kernel checked. Lift the permutation while fixing
the seventh label. This preserves the actual new vertex, its degree and
the exact old trace counts, and moves the possible double-codegree to
label 0. The final representative permutation is composed with this
normalization to return to the original actual input.

Consequently only some 0 (49 vectors) and none (37 vectors), a total of
86 vectors per degree, enter the new coverage proof. The other five
pattern files are historical generated sources and are not dependencies
of the production Numeric module. This reduction is an actual-input
relabeling theorem, not an unproved symmetry restriction.

Each singleton is recovered by the preceding equality. The remaining empty
promotion is recovered from degree(z) minus the sum of nonempty promotions.
These operations count actual edges, not distinct projected trace labels.
No independent-event hypothesis is introduced.

`complete_actual` and `extend_actual_of_high` prove the reconstruction for
arbitrary lock number. `extendSparse_eq` proves that summing high promotions
over their finite support and summing the nonempty completions over that
support plus singletons equals the original complete Boolean-algebra formula.
The numeric domain is unchanged by this implementation optimization.

The 86 normalized capacity vectors are bound to the 18 saved seven-lock representatives
for each degree. Their strict bounds are the previously exported 17 pure
seven-degree certificates, one 31-layout joint seven-degree certificate, and
18 pure eight-degree certificates. The 31-layout certificate has genuinely
nonzero capacity penalties at three centers; the cached implementation checks
those exact rational values and does not copy the zero-penalty special case
from the earlier five-low certificate.

Status: general reconstruction and sparse equality have passed light Lean
checks; the complete actual caller has passed with the exact classifier,
coverage and probability APIs explicit as parameters. The production caller
has no such premises. Full new catalogue and strict-certificate builds are
still pending. The final normalized actual chain probe passed in 7.31 seconds
with only the standard three axioms; its exact coverage and numerical APIs
remain explicit probe parameters until the official modules are built. Review should focus on the actual selection/reconstruction,
capacity-domain completeness and representative bindings; agreement is not
being recorded as a completed branch.
