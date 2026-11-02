# Free-C5 order60: coupled difference constraints within vertex orbits

## Target and status

**COHERENT AS STATED.** This is one pure derivation for the complete
free-C5 order60 mechanism. It gives a small shared-variable constraint
and a quotient obstruction, without fixing the quotient or running any
enumeration, solver, profile, BFS or Lean task. No full-family exclusion
is claimed. Local mathematical status is same-family/provisional;
this note has not itself received Gemini review.

The organizing object is the actual defect
`B = A^2 + A - 7I - J60`, entrywise nonnegative, with diagonal zero and
row sum five. We use the existing necessary quotient identity and row
types in [CYCLIC5_ORBIT_SWITCH_AND_QUOTIENT.md](CYCLIC5_ORBIT_SWITCH_AND_QUOTIENT.md).
The derivation is: quotient parity removes one row type; actual
same-orbit common neighbors give two shared difference-presence
conditions; these become an edge-coloring obligation for double
interfaces. All steps below are exact identities or proved necessary
conditions, with no approximation.

## Assumptions and notation

Let G be a simple degree-eight graph on `(a,t)`, `0 <= a < 12`, `t in Z5`,
invariant under `(a,t) -> (a,t+1)`. For necessity assume diameter at most
two. Let `S_ab` be the directed set of shifts on interface a to b,
so `S_ba = -S_ab`, and let `q_ab = |S_ab|`. The quotient is M, with
`r_a = M_aa` its internal degree. Existing arguments give `r_a in {0,2}`
and the seven listed row types. Its actual defect quotient is

`D = M^2 + M - 7I12 - 5J12 >= 0`, with row sums five.

## 1. The all-even row is impossible

If row a of M is all even, then `(M^2+M)_ab` is even for every b.
For each of the eleven `b != a`, the nonnegative integer
`D_ab = (M^2+M)_ab - 5` is therefore odd and at least one. This
contradicts the row sum five.

Among the previously retained seven row types, the only all-even row
is `r_a=0`, external multiplicities `2,2,2,2`. It is excluded. The six
remaining types are

| Internal degree | Nonzero external multiplicities |
|---|---|
| 2 | `1^6` |
| 2 | `2,1^4` |
| 0 | `2,2,1^4` |
| 0 | `2,2,2,1,1` |
| 0 | `3,1^5` |
| 0 | `3,2,1^3` |

This is a cheap consequence of the **full** quotient nonnegativity;
it is not asserted to be logically independent of that condition.

## 2. Exact within-orbit coverage

For nonzero delta in Z5, the number of common neighbors of `(a,0)`
and `(a,delta)` in orbit b is

`c_ab(delta) = |S_ab intersect (S_ab+delta)|`.

This count is unchanged by delta negation or interface reversal.
An independent orbit a has no direct edge or internal intermediate,
so its same-orbit coverage is exactly

`sum_(b != a) c_ab(1) >= 1` and
`sum_(b != a) c_ab(2) >= 1`.                                      (1)

The negative shifts follow by symmetry. An orbit with `r_a=2` is
already a C5, which itself covers all its pairs in at most two steps.

An interface of size at most one contributes zero to both counts.
For a double interface `S_ab={x,y}`, precisely one of the two counts
is one: the class of `y-x` is either `{+1,-1}` or `{+2,-2}`. This is a
single two-valued label shared by both endpoints. For a triple
interface, **both** counts are positive: for every nonzero delta,

`|S_ab intersect (S_ab+delta)| >= 3+3-5 = 1`.

Thus an independent orbit incident to a triple interface automatically
satisfies (1). Every other independent orbit must see both difference
classes among its double interfaces. For its remaining row types there
are respectively two or three double interfaces. When there are two,
their classes must be opposite; when there are three, they must not all
be equal. This is a coupled condition on actual shifts, not merely on
the number of routes in the quotient.

## 3. A quotient obstruction and a constructive scope

Form the simple graph H on the twelve orbit labels by placing edge ab
exactly when `q_ab=2`. Call an orbit constrained when it is independent
and has no triple interface. By the six row types, constrained vertices
have H-degree two or three, and all unconstrained vertices have degree
zero or one.

**Necessary obstruction.** H cannot have an odd-cycle connected
component. Every vertex in that component is constrained of degree two,
so the shared edge labels would have to alternate around an odd cycle.
Equivalently, a cycle of double interfaces whose vertices all have
`r=0` and row type `2,2,1^4`, with no other double interface at those
vertices, must have even length. Unit interfaces outside the cycle do
not repair this same-orbit obstruction.

In fact this is the only obstruction to satisfying all the same-orbit
conditions for a quotient obeying the six row types. To see this,
consider each component of H. An all-even, nontrivial component is a
cycle because the maximum degree is three; alternate colors if it is
even. Otherwise adjoin one auxiliary vertex z and connect it once to
each odd-degree vertex. The enlarged connected graph has all degrees
even. Take an Euler circuit beginning at z and alternate two colors
along it. At each original vertex, incoming/outgoing edges form
oppositely colored pairs, even if the circuit has odd length (the sole
wrap-around exception is at z). Original degree-two vertices therefore
see both colors. Original degree-three vertices acquire degree four;
after removal of their one auxiliary edge they still see both colors.
Degree-one vertices are unconstrained. Isolated vertices need no color.

For each colored double interface choose the shift set `{0,1}` or
`{0,2}` according to its color. Choose any triple shift set, any single
shift, and the permitted internal circle. Reverse interfaces use the
negative shift set. This realizes the quotient as a complete invariant
60-vertex degree-eight graph and covers every pair in the same orbit.
**Cross-orbit coverage remains a separate, unresolved obligation.**
This construction is not a diameter-two witness.

No complete numerical quotient passing all earlier D conditions but
violating the odd-cycle rule was produced in this pure task. Therefore
we do not claim a demonstrated strict separation from the full
quotient feasibility domain; the proved coupled shift condition and
its cheap quotient consequence are the actual results.

## 4. Encoding without fixing the quotient

Let `x_ab,t` be the existing directed-shift edge variable, interpreting
it as `x_ba,-t` when reversing the canonical interface. For each
unordered pair `{a,b}`, introduce or reuse shared flags

`e_ab,delta <-> OR_(t in Z5) (x_ab,t AND x_ab,t+delta)`, delta=1,2. (2)

These flags are identical from either endpoint: reversal only reindexes
the five terms. They mean presence of a difference class. A triple
interface has both flags true; a double interface has exactly one.
With `l_a,1,l_a,2` the two internal-step variables, add for each a

`l_a,1 OR l_a,2 OR OR_(b != a) e_ab,1`,
`l_a,1 OR l_a,2 OR OR_(b != a) e_ab,2`.                            (3)

Equations (2) must be equivalences, not free auxiliary certificates.
There are 132 shared flags and 24 guarded existence clauses. Their
660 underlying unordered shift-pair products are already represented
among the actual-middle Tseitin variables of the prepared CNF, so one
existing equivalent product variable can be reused per product. The
OR equivalences need five forward clauses and one reverse clause each.

The original complete coverage CNF already logically implies (3):
these are compressed same-orbit obligations, not a newly missing
distance condition. The implementation value is sharing the same
class flag across two endpoint rows and exposing the degree-two
alternation/odd-cycle obstruction to propagation. No speedup is claimed
without an actual comparison. The current checked CNF was not changed.

At a quotient stage, simply build H and reject odd-cycle components.
In a full orbit-variable model, (2)--(3) retain arbitrary quotients;
one need not enumerate cycle cuts or fix a proposed quotient first.

## 5. Character blocks: precise identities, no further exclusion

For a primitive fifth root zeta and k=1,2, define the Hermitian matrix
`T_k[a,b] = sum_(d in S_ab) zeta^(kd)`, with the analogous internal
entry. The nontrivial-character defect block is

`B_k = T_k^2 + T_k - 7I`.

Because the actual symmetric nonnegative B has row sum five, its
operator norm is at most five. Each eigenvalue lambda of T_k therefore
satisfies `-5 <= lambda^2+lambda-7 <= 5`, equivalently

`lambda in [-4,-2] union [1,3]`.

This is a necessary spectral interval, not a contradiction. Also
`p_k(x)=det(xI-T_k)` has coefficients in the integers of Q(sqrt5):
complex conjugation preserves the determinant, and the entries are
algebraic integers. The two polynomials are Galois conjugates and

`det(xI-A) = det(xI-M) * (p_1(x)*p_2(x))^2`,

where `p_1*p_2` is an integer polynomial. This factorization holds for
every graph with the free C5 action, including failed candidates; it
does not alone give an additional target-only cut. No further Galois
or trace obstruction was obtained in this task.

## Boundaries and workflow

The actual results are the all-even-row consequence, shared difference
conditions, and the exact same-orbit feasibility characterization for
the six retained row types. They neither exclude the entire C5 family
nor imply cross-orbit coverage, and they are not constraints on an
arbitrary graph lacking the specified free action. No new computation
was performed and no numerical performance claim is made.

The project-local `formula-derivation` skill was read in this task;
`proof-writer` was read earlier and reused. This is their V3 DD82
adaptation: one invariant object, exact assumptions, complete local
proof and explicit remaining obligation; no new review agents,
solver run, shared-state update or formalization.
