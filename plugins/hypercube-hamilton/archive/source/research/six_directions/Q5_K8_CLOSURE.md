# Q5 balanced eight-hole cycle extension

2026-11-01. ARIS proof-writer. Complete proposed proof relative to the
listed imports and finite geometry witnesses; independent review pending.

## Exact claim

Every matching $F$ of $K(Q_5)$ with exactly four even and four odd holes
has a Hamilton cycle containing $F$, all of whose edges outside $F$ are
short. Required matching edges may be long or join equal parities.
Call this assertion K8. It is not the full balanced-eight-hole endpoint
theorem and not the full A8 avoid-one theorem.

## Dependencies

1. Full Q5 balanced-six-hole cycle extension K6, accepted with A6 in
   `A6_AND_EIGHT_FREE_CLOSED.md` and its cited independent reviews.
2. Only the delta-1/2/3 branches of Q5 A8 from
   `A8_PARTIAL_PROOF_PACKAGE.md`, which require independent acceptance.
   No unresolved A8 orbit, A10, or higher-hole P6 theorem is used.
3. The finite geometric assertion and positive witnesses below, generated
   by `q5_k8_geometry.py`; a separate independent check is required.

## Proof

If two holes are short-adjacent, add their edge. The new matching has
three holes of each parity and K6 supplies the full cycle. The added edge
was short, so this is also an allowed extension of F. Thus assume all
eight holes are independent. Write their parity classes as E and O.

The following finite assertion holds: for every independent set with four
holes of each parity, there is a free vertex r and a short neighbor y
such that, after replacing hole r by y, the new 3:5-hole geometry has a
coordinate cut containing y with majority-minus-minority count 1, 2, or 3.
Here y is necessarily covered by F, since the holes are independent.
The majority class is the parity of y, and y is its prescribed omitted hole.

Choose such r,y and write h=F(y). The four vertices r,y,h and the other
holes have the required distinctness: r is free and h,y are covered.
Set

$$F'=(F\setminus\{yh\})\cup\{hr\}.$$

This is an arbitrary complete-graph matching whose holes are precisely
the old holes minus r plus y. The selected delta-1/2/3 branch of A8 gives
a cycle on exactly $Q_5-y$ containing F', with short new edges. Replace
its required edge hr by the two-edge path h-y-r. The original edge hy
is restored and yr is short. This is a Hamilton cycle containing F;
the auxiliary edge hr disappears. Its construction works for every
matching on the specified covered support, independently of the value
of h. This proves K8, subject to acceptance of the finite assertion.

## Finite assertion: explicit complete universe

Enumerate each of the $\binom{16}{4}$ even hole sets E. List all odd
vertices nonadjacent to E, and enumerate all four-element subsets O.
This produces exactly 980 independent balanced-eight-hole geometries,
without symmetry reduction. For each, enumerate the eight choices of r
and its five coordinate neighbors y. For each pair compute the five cut
imbalances of the marked 3:5-hole set $(E\cup O\setminus\{r\})\cup\{y\}$,
always taking the face containing y. A pair is successful if some
imbalance is 1,2,3.

All 980 geometries have a successful pair. The exact histogram of
successful (r,y) pairs is 580 geometries with 40, 320 with 18, and 80
with 24. `q5_k8_geometry.json` records each input and one actual r,y,
coordinate, and imbalance witness. A verifier need only rebuild the
complete finite domain and check each witness with the stated formulas;
it need not search for Hamilton cycles or inspect matching instances.

## Limits

K8 supplies a cycle with freely selected construction endpoints. It does
not supply a path to an arbitrary prescribed covered endpoint: that would
require handling the corresponding fixed A8 geometry, which may be open.
No full ten-hole covered-target or other full P6 conclusion is asserted.
