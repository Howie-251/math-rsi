# Independent audit of the A4 spanning cycle-factor lemma

Date: 2026-11-01. Reviewer: GPT-6.1sol, high (explicit user setting).
Review independence: same-family. Semantic acceptance: provisional.

**Verdict: PASS for the cycle-factor claim and CF1, relative to imported N14.**
The deterministic GF5 check is independently reproduced. No open fatal,
critical, major, or minor issue was found in the factor reduction. This audit
does not prove connectedness, A4 Hamiltonicity, or full P6. The introductory
"independent review pending" in the hashed input is superseded by this report.

## Input and exact statement

Primary input: `A4_SPANNING_FACTOR.md`, SHA256
`08b78af7f4388089c6e3329b2f95dc3d538551447af17aa97baf9fa85207edc9`.

For every matching F of the complete graph on V(Q5), whose four uncovered
vertices have parity split 1+3, and for every choice v among the three
majority-parity holes, there exists a simple 2-regular spanning graph on
V(Q5) minus v containing F, with every added edge a cube edge.
F has 14 edges. Arbitrary long and same-parity edges of F are permitted.

N14 is an explicit imported theorem for the adjacent branch. Its local
statement and application were checked in `TWO_ODD_HOLES_TRANSFER.md`; this
audit does not independently re-prove the external Fink–Mütze Theorem 8 on
which N14 rests. The final bibliographical source-comparison paragraph of the
factor document is not part of the audited theorem or its dependency chain.

## Obligation ledger

| ID | Obligation and independent verification | Result |
|---|---|---|
| O1 | XOR by the minority hole maps that hole to 0 and the other three to odd vertices; preserves every short edge and matching incidence. | Closed |
| O2 | If ab or at is short, adjoining it gives a matching with exactly two odd holes, including v. N14 at dimension 5 produces the required cycle; the adjoined edge is short relative to original F. | Closed modulo N14 |
| O3 | Otherwise r(a)=r(b)=r(t)=2 and r=1 elsewhere; even demand 15+2=17, odd demand 13+2+2=17. | Closed |
| O4 | A lost odd neighbor other than v must have exactly one neighbor in S because F contains at most one edge incident to it. Its partner cannot be a. Distinct lost neighbors have distinct partners. Thus losses are bounded by R(S), including when some F edges are long. | Closed |
| O5 | Both b and t retain all incident cube edges, and at most 16-n(S) of them are outside the full neighborhood. Their extra demand contributes at least max(0,n(S)-14). Removing v costs at most one. | Closed |
| O6 | GF5 holds for all 65,535 nonempty subsets of the 16 even vertices, by independent exhaustive integer computation. Empty clone subsets satisfy 0<=0 directly. | Closed by finite computation |
| O7 | For any subset U of even clones, its represented original set S has exactly the same clone neighborhood as the full set of clones of S, and size(U)<=size(S)+1[a in S]. Weighted Hall therefore covers partial-clone subsets as well. Equal sides of size 17 turn the saturating matching into a perfect matching. | Closed |
| O8 | A repeated projected edge requires both endpoints to be doubled. The only doubled vertices are a,b,t; b,t have equal parity, and ab,at are absent in this branch. No duplicate can occur. | Closed |
| O9 | H avoids every short F edge by definition of G; long F edges cannot equal a short H edge. Thus F union H is simple and degree two at all 31 allowed vertices. No F edge meets v because v is a hole. | Closed |
| O10 | Every finite simple graph of degree two is a disjoint union of cycles; this yields exactly the claimed scope and does not imply connectivity. | Closed |
| O11 | CF1: for nonempty proper clone subsets, proper original support has at least one unit of excess by GF5's table; full support has all 17 odd neighbors and at most 16 clones. Thus strict Hall holds. Removing endpoints of any chosen clone edge leaves Hall, so that edge lies in a perfect matching and its original edge lies in a spanning factor. | Closed |

Dependency graph is acyclic: normalization and the adjacent-case import are
independent of GF5; GF5 plus the loss estimate yields clone Hall, then simple
projection, then the cycle factor. A4 or P6 is not used anywhere.

CF1 uses the strict version of the same Hall bound and the same projection
argument. It permits prescribing one allowed new edge in the nonadjacent
branch. Removing two selected endpoints costs at most one neighbor for any
subset of the remaining even part; that subset was a proper subset of the
original 17-vertex part. Equal remaining sides of size 16 allow Hall again.
There is no inference to simultaneous prescription of several edges or to
keeping a previously chosen component while joining another one.

## Independent computational verification

The submitted checker `verify_a4_factor_geometry.py` was read and rerun.
Its 65,535 nonempty masks cover every relevant S, and its leaf-parent bitset
counts distinct parents rather than leaf edges. It returns PASS with the
stated minima.

An independent checker, `a4_factor_gray_audit.py`, instead visits all subsets
in Gray-code order, updates the five affected odd degrees, and tracks the XOR
of selected original vertex labels at each odd vertex. At degree one this XOR
is the unique parent. It does not reuse the submitted neighbor-mask loop.
The empty case is handled separately and is included only to give 65,536
total Hall cases. Results are in `a4_factor_gray_audit_results.json`.

For sizes 0 through 16 both independent and submitted checks agree on:

`[0,2,3,3,2,2,1,1,1,3,4,3,3,3,2,1,0]`.

The submitted result uses null at size zero because GF5 is only asserted for
nonempty S. This is a presentation difference: Hall itself has slack zero
for the empty subset. The independent histogram has exactly two zero-slack
sets, the empty set and the entire even part. No negative slack exists.
Each nonempty cardinality has a concrete minimizing witness in both results.

The larger C++ checker was also inspected: its eligible b,t values are the
11 odd nonneighbors of 0, chosen unordered in 55 ways, and v is any of the
remaining 14 odd vertices. This gives 770 configurations. It loops all 65,536
subsets and correctly counts protected leaf parents. Its 50,462,720-case
reported result agrees with the stronger, hole-independent GF5 check. This
review did not independently rerun those 50 million cases because GF5 alone
already suffices and was independently verified.

## Counterexample pass and boundaries

The following failure mechanisms were explicitly tested against the proof:

- Long or same-parity F edges: they remove no extra short edges, so they
  cannot invalidate the loss bound.
- Several leaf neighbors of one parent: F removes at most one of them;
  counting distinct parents is the correct upper bound.
- A subset containing only one clone of a: identical clone neighborhoods
  make Hall valid without requiring such subsets to be unions of clone pairs.
- Projecting a generic demand-clone matching can create parallel edges if
  an edge joins two doubled endpoints. The proof explicitly excludes exactly
  those a-b and a-t edges before using this projection; the adjacent branch
  is handled by N14 instead.
- S empty or all even vertices: both have Hall equality and are handled.
- A disconnected factor: this remains possible. No merging procedure or
  connected-factor claim is inferred from the Hall calculation.

No non-enumerative derivation of GF5 was obtained in this audit. GF5 remains
a complete finite computer-assisted lemma rather than an asymptotic or
experimental assertion. The universal conclusion quantifies over all F by
the analytic loss estimate; it does not enumerate only sampled matchings.

No proof text or root state file was modified by this audit. Deterministic
verification closes GF5; same-family reviewer agreement alone is not a
cross-family semantic acceptance overlay.
