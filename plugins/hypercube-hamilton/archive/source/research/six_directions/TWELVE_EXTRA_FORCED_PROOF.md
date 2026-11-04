# Fifteen new forced T17 marked classifications: reduced rank1024

2026-11-01. ARIS proof-writer producer proof. PROVABLE AS STATED relative
to the primary generic rank upper bound and explicit finite certificates,
pending independent verification. No old input or accepted state changed.

## Exact quantified local theorem

For EACH row below let H={0} union J, U={1,2,4}, K=Q5-H, and p=8,q=16.
For every arbitrary perfect matching F of the COMPLETE graph on K, there
is one simple29-cycle on exactly Q5-U containing F with only short new
edges IF AND ONLY IF pq is absent from F. Original required edges may be
long or equal-parity. All marked sets and the forced pair must be transported
together under cube automorphisms, including parity reversal. This proves
only the exact fifteen marked inputs, not unrestricted T17 or a Q6 layer.

| Original308 index | Majority J | Prefix suffix |
|---:|---|---|
| 97 | 1,2,4,11,13,26,31 | 097 |
| 113 | 1,2,4,11,21,26,31 | 113 |
| 177 | 1,2,4,7,11,21,26 | 177 |
| 178 | 1,2,4,7,11,25,28 | 178 |
| 179 | 1,2,4,11,13,19,22 | 179 |
| 180 | 1,2,4,11,13,19,28 | 180 |
| 181 | 1,2,4,11,13,22,26 | 181 |
| 182 | 1,2,4,11,21,26,28 | 182 |
| 234 | 1,2,4,11,25,28,31 | 234 |
| 239 | 1,2,4,7,11,19,28 | 239 |
| 240 | 1,2,4,7,25,26,28 | 240 |
| 241 | 1,2,4,11,13,22,25 | 241 |
| 281 | 1,2,4,7,11,19,31 | 281 |
| 282 | 1,2,4,11,13,25,31 | 282 |
| 283 | 1,2,4,25,26,28,31 | 283 |

Every included hole has its exact declared degree. The UNIQUE hole with
only two short neighbors outside U is0, with neighbors precisely8 and16,
both covered. These fifteen marked cases were compared with all120
coordinate permutations of the old seven accepted forced T17 inputs;
none belongs to those seven. They therefore need their own new reduced
certificates rather than an unsupported import of old classification.

## Necessity and reduced-rank sufficiency

Any permitted cycle has degree2 at the uncovered vertex0, whose only
remaining short neighbors are p,q. It must contain p--0--q. If F contains
pq, these three vertices form an isolated triangle, impossible in a
spanning29-cycle. This is a direct analytic negative certificate, not
a consequence of deficient rank or unsuccessful search.

The positive certificate supplies1024 short forests S on Q5-U. Every
covered vertex of K has degree1, each of the five included holes has
degree2, and no component is a cycle. There are17 short edges and12
path components, with endpoints precisely the24 vertices of K. The
component through0 is exactly p--0--q. Its full endpoint matching P
therefore contains pq. Delete that matching pair to obtain P' on
K'=K minus {p,q}, which has22 vertices.

If F lacks pq, put a=F(p),b=F(q). These four vertices are distinct.
Replace pa,qb by ab to give an arbitrary complete-graph perfect matching
F' on K'. Contracting the labelled path a--p--q--b proves connectedness
of F+P equivalent to connectedness of F'+P'. The compressed edge ab
need not be short; the local rank domain permits it.

The primary matching-connectivity theorem, Cygan--Kratsch--Nederlof,
Corollary3.5, bounds rank_GF2(H_22)<=2^(22/2-1)=1024 on ALL complete-graph
perfect matchings. Its generic source/domain alignment is recorded in
A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md. For each row the supplied1024
P' rows and1024 valid arbitrary-matching columns give rank1024. Their
complete rows consequently span H_22's row space. Every matching column
is nonzero: cyclically link consecutive oriented required edges. Hence
some P' connects the arbitrary F'. Undo contraction and expand P's paths
through S to obtain the required simple29-cycle, retaining all F edges.
A common required/forest endpoint pair would create an isolated labelled
2-cycle and cannot occur in the successful global connected union.
The only deliberately fixed pair pq is already absent from F.

## Independent-verification interface and finite formats

Each prefix is TWELVE_EXTRA_FORCED_orbit_XXX, with original308 indexXXX.
The1024 records per file have these exact formats:

- _forests.bin:34 bytes, seventeen sorted distinct short edges.
- _full_pairs.bin:24 bytes, twelve full endpoint pairs on K.
- _pairs.bin and _columns.bin:22 bytes on K'.
- _matrix.bin, _pivots.bin, _combos.bin:1024 rows of128 bytes, low-bit-first.
- _config.txt and .json: actual holes, omissions and extraction metadata.

Pivots have distinct highest set bits0,...,1023 and equal the XOR of
original rows selected by combos, certifying exact binary rank. A checker
may instead recompute rank from scratch. It must also independently
verify every forest's exact support, shortness, degrees, acyclicity,
full endpoint pairing and forced cherry; remove pq and compare P'; check
every column; and recompute all1024^2 matrix bits per row. The total is
15360 forests and15728640 connectivity bits. The separate producer author
checker performs these computations but is not a fresh acceptance review.

The producer extraction takes independent columns of each existing
1024-by2048 full-endpoint matrix and contracts its selected original
matching columns through p,q. Its source indices explain construction
only. The target reduced certificate stands independently; no forest
exhaustiveness, old full-row matrix or reported rank need be trusted.

## Scope and dependencies

The acyclic local DAG is primary generic rank bound + new selected finite
forests/columns/reduced matrices -> exact fifteen conditional statements.
It imports no full T17, Q6 twelve-hole theorem or P6 conclusion. The
necessary obstruction is proved analytically. An unsuccessful rank
criterion alone would remain OPEN, not disprove the local theorem.
Application requires the accepted general forced-cherry transfer and
actual root-not-obstruction/source/marked geometry conditions, proved
separately in TWELVE_EXTRA_FORCED_APPLICATION.md. No main ledger changed.
