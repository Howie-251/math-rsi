# T44 same-face zero-crossing gluing — proof draft

Date: 2026-11-01. ARIS proof-writer package. This closes one specified
transfer branch relative to the imported Q4 perfect-endpoint classification;
it does not claim the full T44_5 or T15 target.

## Claim

Let $F$ be an arbitrary matching of $K(Q_5)$ with precisely four holes,
all of one parity. Let $x,y$ be two prescribed holes. Suppose some
coordinate cut $Q_5=A\cup B$ has all four holes in $A$ and no required
edge of $F$ crossing the cut. Then there is a cycle on exactly
$Q_5\setminus\{x,y\}$ containing every edge of $F$ and adding only
short edges.

The original required edges may be long or same-parity. No shortness
assumption is imposed on $F_A$ or $F_B$.

## Status

PROVABLE AS STATED, relative to the explicitly imported finite Q4
perfect-endpoint classification and the positive path certificates
checked below. Independent review of this new proof package is requested.

The dedicated verifier completed with **PASS**: $311850$ matching
records, $2486610$ explicit positive paths, and all $216$ low-endpoint
rows passed. The endpoint-count histogram is
$\{3:180,4:36,5:10,6:1040,7:5036,8:305548\}$.

## Notation and dependencies

Identify both coordinate faces with the same Q4, so corresponding
vertices differ by the deleted coordinate. Write $\bar v$ for the
corresponding vertex in the other face. The map $v\mapsto\bar v$
preserves Q4 distances; as a Q5 map it reverses global parity.

For a perfect matching $P$ of $K(Q_4)$ and a root $r$, let $G(P,r)$
be the set of opposite-parity endpoints of Hamilton paths starting at
$r$, containing all of $P$ and adding only short edges.

Imported input: `Q4_PERFECT_ENDPOINT_ABUNDANCE.md` proves that
$|G(P,r)|\ge4$. Its complete bad-endpoint classification, in
`q4_perfect_endpoint_abundance_check.json`, has 4708 exceptional
perfect matchings at root $0$, with their exact bad odd endpoint sets.
Every nonexceptional matching has at most one bad odd endpoint.

This proof uses two finite statements:

1. The exceptional bad sets contain none of the endpoint triples in
   Section 1 below.
2. The 30 normalized T44 inputs have complete positive path witnesses
   satisfying the endpoint alternative in Section 2 below.

The dedicated independent checker is
`verify_t44_sameface_path_gluing.py`; it imports no producer or older
checker. It relies on the separate proof of exhaustiveness of the
perfect-endpoint exceptional universe, rather than assuming the 4708
JSON rows alone establish that exhaustiveness.

## 1. Endpoint hitting triples

Let $e_i,e_j,e_k$ be three distinct coordinate unit vectors of Q4.
For every perfect matching $P$, each of the sets

$$\{e_i,e_j,e_k\},\qquad
  \{e_i,e_j,e_i\mathbin\oplus e_j\mathbin\oplus e_k\}$$

intersects $G(P,0)$.

There are four triples of the first form and twelve of the second.
The checker generates all sixteen directly. None is contained in any
of the 4708 exact exceptional bad sets. A nonexceptional matching has
at most one bad endpoint, so it cannot contain any three-element set
of bad endpoints either. This proves the assertion for every perfect
matching, using the imported classification. Translation through a
root $r$ gives the corresponding statement for $G(P,r)$.

## 2. Q4 T44 positive path cover

Let $L$ be a matching of $K(Q_4)$ whose four holes $x,y,b,t$ all have
one parity, where $x,y$ are to be omitted. Normalize by translating
$x$ to $0$ and permuting coordinates so $y=p\in\{3,15\}$. All four
holes are then even. Order the included holes so $b<t$.

For each $p$, the included pair ranges over
$\binom{6}{2}=15$ choices. For each such hole set, the other twelve
vertices have $11!!=10395$ perfect matchings. Thus the thirty files
`q4_t44_path_abundance_p_b_t.bin` cover all normalized inputs.

Every row consists of sixteen mate bytes, one path-count byte, and
that many explicit 14-vertex paths. Each listed path starts at $b$,
ends at a different odd vertex, visits exactly $Q_4\setminus\{0,p\}$,
contains $L$, and has only short edges outside $L$.

Let $S$ be the set of endpoints appearing in the positive witnesses
for a row. The checked alternative is

$$|S|\ge5\quad\text{or}\quad
  S\mathbin\oplus b\text{ contains one of the sixteen triples in Section 1}.$$

Here $S\mathbin\oplus b=\{s\mathbin\oplus b:s\in S\}$ normalizes
the path root to $0$. The checker validates all positive paths, all
mate involutions, exact hole sets, distinct endpoint witnesses, and
bijective recursive matching-rank coverage of $0,\ldots,10394$ in
each file. No claim that the listed endpoints are all possible
endpoints is necessary: positive witnesses and their endpoint lower
sets suffice.

There are only 216 rows with at most four listed endpoints. Their
translated endpoint sets have thirteen possible values. Each contains
one of the sixteen hitting triples. The checker also checks directly
that none of those thirteen endpoint sets is contained in any of the
4708 exceptional bad sets. This direct comparison is redundant but
provides a second implementation of the finite intersection step.

## 3. Q4 path compatibility consequence

For any $L$ as in Section 2 and any perfect matching $P$ on another
copy of Q4 identified vertex-for-vertex with the first, there is a
common endpoint $q$ such that:

* the first copy has a path from $b$ to $q$ on exactly its fourteen
  nonomitted vertices, extending $L$ with short new edges;
* the second copy has a Hamilton path from $b$ to $q$, extending $P$
  with short new edges.

To prove this, take the positive-witness endpoint set $S$ from Section 2.
If $|S|\ge5$, then $|G(P,b)|\ge4$ and both are subsets of the same
eight opposite-parity vertices, so $S\cap G(P,b)\ne\varnothing$.
If $S\oplus b$ contains a hitting triple, Section 1 again gives a
member of $S\cap G(P,b)$. Choose such a member $q$ and the two paths
that witness its membership. Since $q$ is opposite in parity to $b$,
the endpoints are distinct.

The normalization is a proof device only: translate and permute both
copies by the same Q4 automorphism, apply the conclusion, then undo
that automorphism. The actual matching $P$ remains an arbitrary
complete-graph perfect matching under this automorphism.

## 4. Q5 gluing proof

Since $F$ has no crossing edge, $F_A$ has exactly the four original
holes and $F_B$ is a perfect matching on $B$. Normalize the two faces
as in Section 2, applying the same identification to both.

By Section 3 choose an A path $R_A$ from the included hole $b$ to $q$
on exactly $A\setminus\{x,y\}$, and a B Hamilton path $R_B$ from
$\bar b$ to $\bar q$. Add the two short cube edges

$$b\bar b,\qquad q\bar q.$$

The A and B paths have disjoint supports, and their two pairs of
endpoints are distinct. Their union with these two edges is one
cycle: start at $b$, traverse $R_A$ to $q$, cross to $\bar q$,
traverse $R_B$ backwards to $\bar b$, and cross back to $b$.
It contains fourteen A vertices and sixteen B vertices, exactly
$Q_5\setminus\{x,y\}$. Every internal required edge belongs to its
corresponding path, and there are no original crossing edges to
restore. Every added edge is either a short path edge or one of the
two displayed short bridges. This proves the claim. $\square$

## Consequence and limits

Together with the positive-crossing same-face lemma in
`T15_ANALYTIC_NOTES.md`, this closes the T44_5 branch in which all
four holes lie in a common coordinate face, regardless of crossing
count. In particular it handles the previously exceptional
same-face orbit with avoided pair $\{0,3\}$ and included pair
$\{5,9\}$ in Q5.

It does not supply a coordinate face for hole geometries that have
none, and it does not resolve the remaining T44_5 geometric orbits.
The original T44_5 and T15 statements are unchanged.
No remaining R8-covered input is claimed closed by this file.

## Reproduction and open risks

Run:

```powershell
python research\six_directions\verify_t44_sameface_path_gluing.py
```

The output is `t44_sameface_path_gluing_verification.json`, including
all thirty file hashes, complete record/path counts, low endpoint sets,
the sixteen hitting triples, and imported-classification hash.

The main external proof dependency is the correctness and complete
scope of `Q4_PERFECT_ENDPOINT_ABUNDANCE.md`. This file explicitly uses
its exceptional-set classification, not merely its two endpoint-count
bounds. An independent reviewer should check this dependency as well
as the new path verifier and the two-bridge gluing.
