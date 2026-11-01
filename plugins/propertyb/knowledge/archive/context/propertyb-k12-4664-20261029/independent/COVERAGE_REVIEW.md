# Independent coverage review: k=12, M=4663

Date: 2026-10-29. Verdict: **PASS_MODULO_IMPORTS** at the scope stated below.
`review_independence: same-family`; `acceptance_status: provisional`.

The statement reviewed is: every finite simple 12-uniform hypergraph with at most
4663 edges has Property B, hence m(12) ≥ 4664. No pair-cover, degree, vertex-count
or preselected-lock premise is imposed on the original input.

## Files and actual verification scope

The final accepted route is `conditional.py` with `CONDITIONAL.json` for
v=91…693, followed by `tail.py` with `TAIL.json` for v=694…782. Their exact row
concatenation is `COMPLETE.json`. Earlier `scan.py`, `hybrid_fast.py` and their
incomplete outputs are exploratory and are not needed for this route.

The review read these sources, the existing M4660 derivation package, the
conditional-extension lemma, and both original certificate implementations.
The new independent `check.py` imports neither the scanner nor a certificate
implementation. It reconstructs the full chosen parameter domain, checks every
trace vector, and separately evaluates selected probabilities with Python
`Fraction`. The Fraction formula code is reused from the independently written
M4660 audit, not imported from the certificate implementation.

Actual execution: `python3 context/propertyb-k12-4664-20261029/independent/check.py`,
exit 0, 2.926374 CPU seconds. Machine results are `DOMAIN_CHECK.json`,
`RESULTS.json`, and `check.log`. An earlier 16-case run also passed; the final
results include 20 cases. These runs together used less than 6 CPU seconds.

## 1. Original objects reach the new complete vertex domain

Suppose an original counterexample has at most M=4663 edges. Choose one with
the fewest vertices. Two vertices which do not lie on a common edge can be
identified: no edge loses its cardinality, repeated quotient edges can be
removed, and any quotient coloring pulls back. Minimality therefore forces
pair-cover in this same counterexample.

For v vertices its degrees satisfy 11d(x)≥v−1. Thus
v ceil((v−1)/11)≤12M=55956. If v≤22, both color classes can have size≤11,
giving a proper coloring directly. For other v, a uniformly balanced coloring
has per-edge monochromatic probability

    p_v = (C(floor(v/2),12)+C(ceil(v/2),12))/C(v,12).

If M p_v<1 the union bound gives a coloring. Independent integer reconstruction
over every 23≤v≤12M retained precisely **91…782**, all 692 values. It also
checked C(v,12)≥M at every retained value, allowing padding with distinct edges
to exactly M edges on the same vertex set. Padding preserves non-colorability
and pair-cover. At the upper endpoint,
783 ceil(782/11)=56376>55956; this constraint is monotone thereafter.

Consequently all subsequent degrees and traces belong to one actual padded
hypergraph with 4663 edges. The old lower endpoint 93 for M4660 would omit
91,92 and is not used. Both new endpoint cases passed an independent Fraction
probability replay.

## 2. The adaptive prefix covers every actual minimum degree

Fix v in 498…693 and let x be an actual global minimum-degree vertex, d=d(x).
Its complete possible range is

    ceil((v−1)/11) ≤ d ≤ floor(55956/v).

Each record contains precisely one branch for every integer d in this range.
If its one-lock bound is strict, x is sufficient. Otherwise set

    s_d = 2(v−1)−11d,
    B = d + floor((55956−vd)/s_d).

The driver does not silently discard s_d≤0: it would report failure. All
accepted branches needing a second lock have s_d>0. Pair-cover implies at
least s_d vertices have codegree exactly 1 with x. Their degrees are all≥d;
the total-degree budget supplies such a vertex y with d≤e=d(y)≤B.
The independent reconstruction obtains B by searching for the first integer
b with vd+s_d(b+1−d)>55956, and agrees with every recorded B.

Crucially, the accepted records cover **every** e in d…B for this actual
minimum-degree branch. Each e either has a strict two-lock certificate or
receives the conditional third-lock treatment below. This does not infer a
worst degree profile by monotonicity, and does not use a second vertex from a
different hypothetical hypergraph.

For v=91…497, a zero-lock bound is sufficient without selecting d; this covers
all those actual inputs immediately.

## 3. Conditional third locks remain in the same actual hypergraph

Consider an actual branch with x,y of degrees d,e and λ(x,y)=1. Put

    E_x=11d−(v−1), E_y=11e−(v−1),
    t=v−2−E_x−E_y,
    R=55956−vd−(e−d).

The number of neighbors with codegree≥2 with x is at most E_x, and likewise
for y. Among the v−2 remaining vertices there are therefore at least t
vertices with codegree 1 to both. All degrees are≥d. After reserving the
excess degree e−d at y, their total excess over d is at most R. For t>0 this
gives a vertex z with

    d ≤ f=d(z) ≤ F=d+floor(R/t).

Every accepted conditional branch has t>0 and R≥0. The independent checker
reconstructed F by the first strict violation t(f+1−d)>R, compared all t,R,F
records, and enumerated **every** f=d…F. There are 9869 such degree-pair
branches. No nonpositive-pool branch is treated as eliminated.

All three selected vertices are distinct and mutually have codegree 1. Their
actual trace is either one triple edge or three separate pair edges; no
third configuration is possible because each lock pair is used exactly once.
Both possibilities are checked for every f. Sorting (d,e,f) merely relabels
the three actual vertices before assigning their fixed positions. The two
trace formulas are invariant under that simultaneous relabeling. In particular
f<e is allowed and is not lost.

The reviewer independently generated every accepted one-, two-, and three-lock
trace vector and checked nonnegativity, total edge count 4663, its specified
degrees, and all pair codegrees exactly 1. Counts below are parameter instances;
different conditional branches can lead to the same sorted triple, so these
are not counts of nonisomorphic hypergraphs or distinct triple profiles.

## 4. The global tail covers its complete independent-lock domain

For each v=694…782, the driver finds the least integer D≥ceil((v−1)/11) with

    Z=(D+1)v−55956>0,
    22Z>[11(D+1)−v+2]^2.

The imported general selection lemma gives three actual vertices of degrees
at most D, mutually of codegree 1. Its auxiliary graph joins pairs of
codegree≥2 among degree≤D vertices. The degree-sum excess bounds its edges;
Caro–Wei and Cauchy–Schwarz force an independent set of size≥3 under precisely
this inequality. No minimum-degree vertex has to belong to these locks.

The independent checker searches D from the lower bound through M, agrees
with every chosen least D, and enumerates every sorted degree triple between
the pair-cover lower bound and D with both trace types. The 693/694 switch
has no gap, and does not require the prefix's selected locks to extend into
the tail's selected locks.

## 5. Full parameter reconstruction and independent arithmetic

| Accepted calculation | Vertex domain | Parameter instances |
|---|---|---:|
| Zero locks | 91…497 | 407 |
| One lock, within adaptive prefix | subset of 498…693 | 3914 |
| Two locks, within adaptive prefix | subset of 498…693 | 94640 |
| Conditional three locks | subset of 621…693 | 489700 |
| General-selection three locks | 694…782 | 75694 |
| Total | every v=91…782 | **664355** |

All row counts and subbranch counts were reconstructed independently, including
the complete d/e/f ranges and both trace types. Every saved accepted branch
upper numerator is nonnegative and strictly below S=2^52. Each row's saved
maximum equals the maximum of its accepted branch summaries.

Twenty selected cases were recomputed with unrounded exact rational endpoint
and ordered-pair probabilities, including minimum-weight bad-pair deductions.
Each exact bound is at most its saved outward-rounded upper bound and is
strictly below 1. Cases include the worst accepted instance of each lock count,
91/92, 497/498, 620/621, 693/694, the final v=782 and both three-lock traces.
They also include the conditional pool's narrowest branch endpoint at
v=684, sorted degrees (81,82,83), and the largest conditional F endpoint at
v=657, sorted degrees (60,84,103), both trace types.

The complete table's tightest reported numerator is

    4503599103886333 / 4503599627370496 < 1

at v=659 and the two-lock instance (d,e)=(63,82), leaving integer gap
523484163. This instance passed the exact Fraction replay independently.

## 6. Rounding and return to an original coloring

The existing certificate source computes endpoint and ordered-pair upper
coefficients as ceil(S p), while each directional deletion coefficient is
floor(S w). The downward-rounded deletion slots are sorted afresh, including
zero-weight slots. For any actual bad-pair set, its true weight is at least
its rounded weight and hence at least the least-q rounded-slot sum. Subtracting
this sum therefore preserves the upper-bound direction. The one-, two-, and
three-lock trace counts are used unchanged by the new drivers.

At each position, the minimum is taken among three bounds on the same actual
failure event; these position bounds are then summed for one fixed conditional
permutation distribution. No incompatible layouts are combined. An adaptive
choice of lock number or relabeling depending on the actual degree/trace is
legitimate: one strict certificate for that actual hypergraph suffices.

`FastExact.table` checks M² max(WH)<2^63−1 and M max(A,B)<2^63−1 for every
used table, before the nonnegative integer contractions. Their intermediate
partial sums are bounded by the same complete nonnegative sum. Deletions are
Python integer sums; the code checks the resulting pair-bound entries remain
nonnegative; the final position sum uses Python integers. These safety and
rounding mechanisms were read in source. This review does not claim an
independent complete recomputation of all NumPy table coefficients.

For any actual padded minimal counterexample, the preceding domain/selection
argument supplies an accepted local instance. The imported permutation
certificate theorem and its strict numerator supply a successful greedy
coloring with positive probability. Restriction to the original edge set
and pullback through any minimal-counterexample quotient return the original
Property B statement. Thus the hybrid driver introduces no extra premise into
the theorem.

## Imported facts and remaining verification scope

The mathematical imports are the established permutation bad-witness theorem,
its weighted link/global pair deductions, and the general low-degree lock
selection lemma, as restated in
`context/propertyb-general/k12-lock-pilot-20261021/DERIVATION_PACKAGE.md`
and the collaborator's general-k source. The conditional extension itself was
checked above against its source
`context/propertyb-general/locks-vs-uniform-20261021/conditional-extension/DERIVATION.md`.

No mathematical coverage defect or rounding-direction defect was found in the
new accepted path. This review is a full parameter-domain/trace reconstruction
and a 20-case independent exact probability replay. It is **not** a complete
second arithmetic replay of all 664355 instances, a new Lean proof, a
cross-family review, or an independent-machine reproduction. Cross-family
review and any required whole-result acceptance remain the root executor's
separate obligations.
