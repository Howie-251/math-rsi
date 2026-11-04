# Ten root-star B local classifications, with all fifty actual marked maps

2026-11-02. ARIS proof-writer producer package. All ten B cases are frozen
for fresh independent verification. Status: PROVABLE AS STATED relative
to the accepted generic reduced-rank criterion and verification of the
explicit finite certificates. No A mixed-opening theorem or Q6 star
closure is asserted. The producer has not triggered an independent checker.

## Exact local theorem

For each row below put H={0} union J, U={1,2,4}, K=Q5-H, p=8 and q=16.
For EVERY perfect matching F of the COMPLETE graph on K, there is a
simple cycle on exactly Q5-U containing every edge of F and introducing
only short edges IF AND ONLY IF pq is absent from F. Thus the cycle has
29 vertices. Original required edges may be long and may join equal
parities. The theorem transports under every common cube automorphism
of H,U and {p,q}, including parity reversal. No unlisted local geometry
or unrestricted T17 theorem is claimed.

| Class | Majority holes J | Certificate prefix |
|---:|---|---|
|0|1,2,4,7,11,13,19|TWELVE_STAR_B_orbit_00|
|1|1,2,4,7,11,13,25|TWELVE_STAR_B_orbit_01|
|2|1,2,4,7,11,19,25|TWELVE_STAR_B_orbit_02|
|3|1,2,4,7,11,21,25|TWELVE_STAR_B_orbit_03|
|4|1,2,4,11,13,14,25|TWELVE_STAR_B_orbit_04|
|5|1,2,4,11,13,19,21|TWELVE_STAR_B_orbit_05|
|6|1,2,4,11,13,19,25|TWELVE_STAR_B_orbit_06|
|7|1,2,4,11,13,25,26|TWELVE_STAR_B_orbit_07|
|8|1,2,4,11,13,26,28|TWELVE_STAR_B_orbit_08|
|9|1,2,4,11,25,26,28|TWELVE_STAR_B_orbit_09|

Every included hole of H-U other than0 is a weight-three odd vertex.
In particular the only remaining short neighbors of0 are p,q, and both
are COVERED rather than holes. These hypotheses are explicit; a degree
count alone would not establish that the forced endpoints lie in K.

## Analytic necessity and legal short forests

The included free hole0 has no required F edge. Its two cycle edges must
be short and must therefore be0p,0q. If pq belongs to F, the three vertices
0,p,q already have their full cycle degrees and form an isolated triangle.
They cannot be part of a simple spanning29-cycle. This proves necessity
without a search-failure premise.

For each class the finite certificate supplies1024 admissible forests S
of short edges on Q5-U. Each has degree0 on U, degree1 at all24 covered
terminals K, degree2 at the five included holes H-U, and no cycle.
It therefore has17 edges and12 terminal-to-terminal path components.
The component through0 is exactly p--0--q: the covered p,q have degree1,
so it cannot continue further. Its full endpoint matching P(S) contains
the forced pair pq. Remove that pair to obtain P'(S) on
K'=K minus {p,q}, a set of22 terminals.

## Reduced-rank sufficiency and arbitrary matching scope

Suppose pq is absent from F. Write a=F(p), b=F(q). The four vertices
p,q,a,b are distinct. Replace pa,qb by ab, obtaining an arbitrary
complete-graph perfect matching F' on K'. The compressed edge ab need
not be short. Suppression of the labelled path a--p--q--b gives the exact
component-preserving equivalence

    F + P(S) is one alternating cycle
        iff F' + P'(S) is one alternating cycle.

This is the single-pair case of the accepted reduced-rank criterion in
HIGHER_FORCED_CHERRY_TRANSFER.md Section5, accepted by
HIGHER_FORCED_CHERRY_REVIEW.json. The earlier structural explanation is
FORCED_CHERRY_RANK_REDUCTION.md. For a single pair R={pq}, acyclicity of
the labelled graph F+R is exactly pq not in F. No stronger matching
restriction is introduced.

The primary complete-graph matching-connectivity rank upper bound is
rank_GF2(H_22)<=2^(22/2-1)=1024, Corollary3.5 of Cygan--Kratsch--Nederlof,
*Fast Hamiltonicity checking via bases of perfect matchings*. The generic
source version and arbitrary-matching domain alignment are recorded in
A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md. Only this upper bound is imported;
no bipartite restriction or experimental rank extrapolation is used.

For each class, the supplied1024 P' rows restricted to the supplied1024
arbitrary matching columns have GF(2) rank1024. Their complete rows in
H_22 are therefore independent and span its full row space. Every matching
column is nonzero: order and orient the eleven edges of F' and cyclically
connect the end of each to the start of the next. If every selected row
vanished at F', so would their complete row space, contradicting this
nonzero column. Hence one selected P' connects with F'.

Undo suppression and expand P(S)'s disjoint paths through its stored S.
The result is one connected simple29-cycle on exactly Q5-U containing
all F edges. Its introduced edges are short. A common required/forest
endpoint pair would be an isolated labelled2-cycle and cannot occur
in a successful connected24-terminal union; thus no length-one forest
path duplicates a physical F edge. Combined with the isolated-triangle
necessity, this proves the exact iff once the finite data pass review.
No exhaustive enumeration of F or of all possible forests is needed.

## Frozen finite certificate interface

Every one of the ten prefixes has EXACTLY1024 selected forest, full-pair,
reduced-pair, column, matrix and rank-evidence records:

| Suffix | Bytes per record | Meaning |
|---|---:|---|
|_forests.bin|34|17 sorted unordered short edges of the FULL forest on Q5-U|
|_full_pairs.bin|24|12 endpoint pairs on the FULL24-terminal set K|
|_pairs.bin|22|11 reduced endpoint pairs on K'|
|_columns.bin|22|an arbitrary perfect matching column on K'|
|_matrix.bin|128|1024 connectivity bits, low-bit-first within each byte|
|_pivots.bin|128|highest pivot index j in row j|
|_combos.bin|128|original matrix rows whose XOR equals that pivot|

The local configuration supplies eight holes, three omissions and the two
forced endpoints. Metadata records the search selection indices. The
producer uses a general exact-degree/DSU forest generator and evaluates
the reduced connectivity rows directly; its completeness is not a premise.
All ten runs reached full reduced rank before their cap. The finite
theorem depends only on the saved witnesses and rank data.

A fresh checker must independently verify all10240 full forests, exact
support/degrees/shortness/acyclicity, forced physical cherry, full endpoint
pairing and reduced pairing. It must validate all10240 arbitrary matching
columns and recompute all10*1024^2=10485760 connectivity bits, retaining
matching-edge labels. It may recompute GF(2) rank or verify every pivot
as the supplied row-combination XOR, with distinct highest bits0..1023.
These obligations are not replaced by the producer full_rank fields.

## All fifty actual B choices and simultaneous transport

In the actual local labels set Z0={7,11,13,19,21}, E={1,2,4,8,16}.
Choose t in Z0 and an unordered pair {w,b} subset E. Put
S=E minus {w,b}, J=(Z0 minus {t}) union S and U=S. There are exactly
5*binomial(5,2)=50 choices. Their minority is0. The consumed original
hole t is NOW COVERED in this B matching: t is not in {0} union J and
belongs to the24-terminal arbitrary-matching domain. It is not silently
omitted or left free by the local theorem.

TWELVE_STAR_B_actual_choices_map.json records EVERY raw choice, its
canonical class, the complete32-vertex coordinate map, mapped consumed
t and simultaneous images of J,U and the pair. The map fixes0. The
coordinate-permutation array q has the convention that output bit d
reads input bit q[d]. The producer verifies all actual M/J/U/pair maps
and that the mapped consumed t is a covered canonical terminal.
It also compares the complete raw-choice set with all five t times all
ten unordered pairs, proving no choice was omitted or duplicated.

The local B geometry depends on the UNORDERED pair only. If the A proof
assigns distinct ordered roles w,b, either ordering has precisely the
same B statement. Thus the50 maps cover all100 ordered choices for B
purposes without imposing any A-side endpoint claim. Their canonical
normalization uses common coordinate permutations with minority0 fixed,
so required arbitrary edges, shortness and exact marked omissions are
preserved under inverse transport. All ten cases are retained to leave
the A-side choice unrestricted; the optional two-class selection in
TWELVE_STAR_B_OPTIONS.md is not a restriction on this frozen package.

## Strict scope and acceptance gates

The acyclic DAG is accepted generic primary rank bound/reduced criterion
+ the ten new finite positive certificates -> exact local iff statements
-> their50 actual marked transports. No Q6 root-star theorem, A mixed
opening result or desired P6 statement is a premise.

This package says nothing by itself about whether an A mixed cycle can
be opened at a suitable edge, whether the actual compressed B matching
avoids the pair, or how virtual auxiliary edges are eliminated in a
global construction. Those remain distinct proof obligations. Even a
final PASS of all ten local B inputs would NOT close a root-star Q6 case
without those interfaces. All new local data remain producer candidates
until the designated independent reviewer accepts them. No original
root-star agent file or accepted main ledger was modified.
