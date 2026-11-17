# Independent review of the rigidity encodings and history checker

This is a local computational-dependency audit. It does not certify the entire
Q7 theorem and does not substitute solver `UNSAT` output for a checked proof.

## Exact graph statements represented

The R0 family searches for a C4-free Q6 graph with every degree in {3,4,5},
158 full three-stars rooted in each parity, and at least four even degree-3
vertices. The R1 family instead requires 158 even stars, 155 odd stars, and
at least eight even degree-3 vertices. A full star is a root together with
three present edges in three specified coordinate directions.

The variables consist of 192 edge variables, one degree-3 indicator at each
of the 64 vertices, all 1,280 star indicators, 160 odd-hole indicators, and
fresh cardinality auxiliaries. All six incident edge literals at a vertex
are constrained by the fifteen positive four-literal clauses and the single
all-negative six-literal clause. These are equivalent to degree 3 through 5.
For the degree indicator z, the fifteen clauses `not z or not e1 or ... or
not e4` prohibit degree at least four when z is true; the twenty clauses
`z or e1 or e2 or e3` prohibit degree at most three when z is false.
Together with the degree restriction, z is equivalent to degree exactly three.
All 128 assignments to six edges and z were independently checked.

A star indicator is equivalent to the conjunction of its three edges, with
three forward binary implications and one reverse implication. The 240
negative four-edge clauses are exactly the 240 squares of Q6.

In a C4-free Q3, any two distinct roots of the same parity differ in precisely
two coordinates. Their full stars would contain the square on those two
coordinates. Thus at most one star of each parity is possible per Q3.
There are 160 Q3 faces. On the even side the two normalized faces have all
four star variables false, while the other 158 faces have a positive
four-star clause; pairwise negative clauses impose at most one. This is
exactly two even holes, or even star sum 158. On each odd face, the clause
`s1 or s2 or s3 or s4 or h` and the four clauses `not h or not si` make h
equivalent to having no odd star. Together with pairwise star exclusion,
the cardinality of h equal to 2 or 5 is exactly odd star sum 158 or 155.
The hole equivalence was checked on all 32 assignments to its five variables.

Every graph with the stated properties extends to all definition variables
uniquely. The counter-extension argument below then provides the fresh
auxiliary variables. Conversely every CNF model gives precisely such a graph.
There is no exact edge count or odd degree-3 cardinality in the new
`--min-even3` mode.

## Independent sequential-counter reconstruction and proof

For signed literals x1,...,xn and 0<k<n-1, introduce q(i,j), where
1<=i<=n-k and 1<=j<=k. Its intended meaning is: at least j of the first
i+j-1 input literals are true. The encoding consists of:

1. `not xi or q(i,1)` for every i.
2. `not q(i,j) or q(i+1,j)` when i<n-k.
3. `not x(i+j) or not q(i,j) or q(i,j+1)` when j<k.
4. `not x(i+k) or not q(i,k)` for every i.

The first three groups force q(i,j) whenever at least j inputs in its prefix
are true. This follows by induction on prefix length: either the last input
is false and the previous prefix already has j true inputs (use group 2),
or the last input is true and the shorter prefix has j-1 (use group 3).
For j=1 use group 1 and its monotonicity; for i=1 and j>1 use group 3
recursively. If at least k+1 inputs are true, let p be the position of the
(k+1)st true input and set i=p-k. The first p-1 inputs force q(i,k), which
conflicts with the last group at the true input xp. Thus every CNF model
has at most k true inputs.

Conversely, if at most k input literals are true, set q(i,j) according to its
intended prefix-count meaning. Groups 1 through 3 are satisfied by elementary
prefix counting. Group 4 is satisfied because q(i,k) together with a true
x(i+k) would give at least k+1 true inputs. This explicitly provides a
satisfying auxiliary extension. The special cases are a negative input unit
per literal for k=0, no clauses for k=n, and a single all-negative clause for
k=n-1. Lower bounds apply this construction to the negated inputs; equality
uses independent fresh lower- and upper-bound auxiliaries.

The independent script allocates each q when its pair is first encountered
in the row order of these four groups. It does not import PySAT, invoke a SAT
solver, or compare a second call to the original encoder. It reconstructs
all integer identifiers, all clauses, and the auxiliary allocation order
directly. The complete ordered clause list matches each audited concrete
CNF, including both large cardinality blocks. It also exhaustively checks
12,288 input assignments across all three bound types, all n from 1 through
8, and all k. It computes Horn closure and explicitly verifies each accepted
auxiliary extension; it rejects exactly the assignments violating the bound.

The R0 instances have 2,440 variables and 12,974 clauses: 8,384 degree/star
definition clauses, 240 square clauses, 1,126 even-face clauses, 200 even
lower-bound clauses, 1,760 odd-hole definition clauses, and 1,264 odd-hole
cardinality clauses. The R1 instances have 3,438 variables and 14,978 clauses;
only the two cardinality counts change to 368 and 3,100. File-specific hashes
and reconstruction outcomes are in `star_rigidity_encoding_audit.json`.

## Normalization and mathematical threshold

Any even hole can be sent to free coordinates {0,1,2}, base 0, by a coordinate
permutation and an even translation. For a face whose external fixed bits
have odd parity, choose one internal coordinate in the translation as well;
its internal component does not change the image face. Thus the translation
can always preserve even parity. The complete stabilizer consists of the
36 coordinate permutations preserving the free-coordinate triple, and the
four even translations supported on that triple. Acting with all 144
elements partitions the other 159 faces into ten orbits of sizes
3,3,1,18,36,18,36,36,4,4. This action and partition were independently
enumerated in `six_profiles_independent_audit.py`. Therefore checking all ten
representatives loses no graph with exactly two even holes.

For either parity of a degree-3-through-5 Q6 graph with M edges and b degree-3
vertices, the identity binomial(d,3)=6d-20+3*1[d=3] gives

    S = 6M-640+3b.

When S=158, it follows that b=266-2M, so b is even. Consequently b>=4 is
equivalent to M<=131, and b>=8 is equivalent to M<=129. All ten R0 and all
ten R1 certificates have now been independently checked, establishing
M>=132 for the two-star-sums-158 statement and M>=130 for the 158/155
statement. Final byte-level audit details are in
`local_rigidity_checked_review.md` and `local_rigidity_final_audit.json`.

## History-checker soundness and regression tests

`check_drup_history.ps1` preserves the original checker in its separate
file. Each proposed addition is first checked against the active watched
formula. If that propagation does not conflict, a history engine is lazily
constructed from original axioms and proof additions with line number
strictly smaller than the current line. Sequential control guarantees every
such prior addition was already accepted; failure aborts immediately. The
current addition is never present in this reconstruction. Subsequent
history additions occur only after acceptance, and deletions do not remove
anything from history. Clause arrays are cloned between engines because
each watched engine permutes its own literal positions.

Inductively, every available clause in either engine follows from the
original CNF. Reverse unit propagation derives conflict from the negation
of a candidate, so acceptance preserves that implication invariant.
Restoring a deleted consequence cannot invalidate it. A successfully
verified empty addition therefore proves the original CNF inconsistent.
This is a sound RUP implication certificate with recoverable deletions;
it need not satisfy a proof format that requires every addition to be RUP
against only the current deletion-respecting active database.

The 15 synthetic checks in `history_checker_audit.json` include the original
ten positive and negative cases, a nonempty addition requiring recovery,
multiple nonempty recoveries, a forbidden future-clause dependency, a
forbidden current-clause dependency, and a forbidden invalid prior addition.
All outcomes match expectations. Small tests support the code review; they
are not a machine-checked metatheorem about the implementation.

The separate `check_drup_history_fast.ps1` adds C# compiler `/optimize+` and
changes the class name; its propagation algorithm is identical. It passes
the same 15 regressions. Its watched core was also extracted without changes
and exposed through a static testing wrapper. On 2,400 randomly generated
input formulas and 24,000 candidate RUP clauses, every answer matched an
independent naive Python unit-propagation implementation. The cases include
unit clauses, empty clauses, tautologies, and successive calls after watch
permutations. The seed, source hash, and outcomes are recorded in
`rup_differential_audit.json`. The full R0 case1 proof produced precisely the
same 115 historical recovery positions and certificate hashes under both
compiler modes.

The earlier m131 case0 proof is now independently accepted in full: 32,441
additions, 25,231 deletions, 73 historical recoveries, beginning at line
48,319. The first failed active step was also independently checked by naive
Python propagation against the strictly earlier history in
`audit_rup_failure.json`. Batch results for the new families are recorded in
their separate `*_checked_batch.json` and per-certificate reports. A generated
proof without a successful report remains unchecked.
