# Full Q5 local inputs: near-balanced cuts for the 12--18-hole layers

2026-11-01. ARIS proof-writer producer package. The row proof is relative
to accepted local imports; the new exact census is producer evidence
pending independent review. Full 12--18-hole Q6 and full P6 remain OPEN.

## Exact row theorem

Let M be a short matching of Q6 with 2k holes, 6<=k<=9. Fix a free root
u and any opposite-parity target v, free or covered. Normalize u=0 even,
write its other even holes as Z (size k-1) and odd holes as W (size k),
and assume Z union W is independent. Choose a coordinate face A containing
v, let B be the other face, and put a=|Z intersect A|, b=|W intersect A|.

The following cut rows suffice for a Hamilton u--v path through M with
all new edges short, relative to the stated accepted local inputs:

1. b=a with b>=1;
2. b=a+1;
3. b=a+2, provided an odd source in W intersect A exists that is neither
   the free target v nor the mirror of u across the cut.

For a covered target row3 always has a source because b>=2 and only the
root mirror can be excluded. For a free target it always has a source if
the entire hole set {u} union Z union W is independent; the root mirror
then is not a hole and only v must be excluded. Without that stronger
independence assumption one must check the source condition explicitly:
a=0,b=2 can have two different forbidden sources and is not automatic.
The row a=b=0 is deliberately excluded: its even bridge source does not
exist. No matching feasibility assumption or sampled matching is used.

## Accepted imports and their ranges

`Q5_A10_FULL_REVIEW` accepts every arbitrary K(Q5) matching with balanced
m:m holes, m=1,...,16, from any free root to any opposite-parity target,
covered or free, with only short new edges. It accepts full cycles for
m=0,...,16. It also accepts every feasible imbalance-two avoid-one input
with holes (t-1,t+1), t=1,...,15, for every marked majority hole and both
parity orientations. Required local matching edges may be long or join
equal parities. All these ranges are part of the reviewed consequence
statement, not an extrapolation from small cases.

Use the accepted uniform-transfer construction and its explicit
five-direction free-root endpoint input for zero original crossings.
Its old numerical restrictions b<=3 or a<=2 served the former limited
A endpoint imports. The construction is replayed below with the new full
balanced-hole theorem. No complete higher-hole Q6 theorem is used to
obtain these local Q5 inputs.

## Completion, endpoint and hole-count proof

Let C be the actual original crossing matching, c=|C|, and X_A,X_B its
distinct endpoint sets. If c=0, apply the accepted five-direction theorem.
For c>0 write delta=1 if u belongs to A, and 0 otherwise.

In row1, select one even source z from Z intersect A; in row2 select no
source. Equivalently s=a+1-b is one or zero. If delta=1, take r=u and pair
X_A plus the s sources into a matching D. If delta=0 and s=1, let r be
the source and pair X_A. If delta=0 and s=0, shortness of the original
internal matching gives one more even than odd crossing port; choose an
even port r and pair all other A ports. The endpoint pairing sets are
even by 2|M_A|+c=32-|H_A|. The completed A matching M_A union D has
exactly b holes of each parity, and r is free. In row1 b>=1, and in row2
b=a+1>=1, so the full local endpoint theorem applies. Its odd target v
is legal whether covered or free; even consumption never consumes v.

After the accepted transfer and tagging, the B matching has hole counts
(k-a-1,k-b+s). In row1 these are (k-a-1,k-a+1), and exactly the source
mirror is omitted; it lies in the majority class. The full Q5 imbalance-
two avoid-one theorem applies. In row2 both counts equal k-a-1; the full
balanced-cycle theorem applies, including zero holes/perfect matching.

In row3 choose the one legal odd source w specified in the theorem.
If delta=1 take r=u and pair X_A union {w}. If delta=0, shortness gives
two more even than odd crossing ports; choose an even port r and pair
(X_A minus {r}) union {w}. The completed A matching has a+1 holes of
each parity, includes the free even r, and still permits target v.
Use its full local endpoint theorem. The transferred B holes are
(k-a,k-a-2), with the even source mirror as the sole prescribed majority
omission. The reversed imbalance-two theorem applies. All declared B
counts are nonnegative and feasible for an actually constructed matching.
The A balanced parameter is at least one in every branch.

## Forest, conflict and artificial-edge bookkeeping

Every selected source is originally free. Its mirror cannot be a crossing
port, because a crossing edge at that B vertex would have to use its
actual short mirror as partner in the original short M. Independence
excludes its being an original hole of the opposite parity. Even-source
mirrors have odd parity and cannot be u; the odd-source hypothesis
excludes u explicitly. Thus every mirror is internally B-covered.

Apply the local A path, delete D, attach all original crossings and the
one bridge if present. Distinct physical attachments preserve a path
forest, including a temporarily isolated crossing target. The artificial
tag uv joins the true endpoint segments when u is in A, or extends the
v segment to the previously unattached u in B. For u in A the parity
identities and c>0 make D nonempty; for u in B the D-empty boundary is
already included in the accepted tagged construction. Compress A paths.

The only B conflict is the single internally covered bridge mirror y.
Its original mate is outside every transferred endpoint: it is internally
covered, not a crossing port or free root, and has opposite parity to y.
It is a pendant endpoint in the conflict path, so no cycle is formed.
Suppress y, retaining its path and any tag. The resulting B matching has
the exact hole counts stated above, namely (H_B minus {u}) union {y} when
a bridge is present, or H_B minus {u} otherwise. Its marked y is omitted
by the B cycle theorem and restored once on expansion.

Expand every suppressed edge and transferred path and delete the unique
tag. The global graph is one Hamilton u--v path preserving every original
edge. All completion edges D were deleted, all compression edges expanded,
and the tag removed; every surviving newly introduced physical edge is
short. This proves the row theorem without the old local endpoint bounds.

## Conditional predecessor reduction, especially free targets

Let P(k-1) be the COMPLETE preceding 2k-2-hole endpoint theorem for every
short matching, every free root of either parity and every opposite-
parity target, free or covered. The following reductions require P(k-1).

For a covered target, any short Z--W hole edge can be added without
covering u or v, and P(k-1) applies. Thus the remaining reduced domain
may assume Z union W independent; root--W adjacency is still allowed.

For a free target, suppose ANY two original holes x,y form a short edge.
If xy differs from uv, adding xy leaves at least one of u,v free. Apply
P(k-1) using that remaining free endpoint as root and the other as target,
reversing the resulting path if needed. It contains M union {xy}; the
extra xy edge is short relative to M. If xy=uv, add uv, choose a different
remaining free root r (there are at least 2k-2 free holes), and any short
neighbor s of r. P(k-1) gives a Hamilton r--s path containing the added
uv. Its endpoints are opposite-parity, and r was free in the augmented
matching. Add the short rs edge to obtain a Hamilton cycle; a path with
64 vertices cannot already contain an edge joining its two endpoints.
Delete the added uv to obtain the required Hamilton u--v path through M.
The artificial uv is not an original edge because both endpoints were
originally free. No original required edge was deleted.

Consequently the free-target reduced domain may assume the ENTIRE hole
set independent. In particular mirror(u) is never an odd source hole,
so the source exception in row3 is automatically discharged there.

The complete preceding ten-hole theorem is now final PASS in
`TEN_HOLE_FULL_REVIEW.json`, fixed SHA-256
`72c6f693b4f8bee6376edcbd132235d7985436f6ebbad8a19dade0d5326f643d`.
Thus these predecessor reductions are available unconditionally relative
to accepted imports for the twelve-hole layer. For fourteen, sixteen and
eighteen holes they remain CONDITIONAL on the corresponding preceding
complete layer. Neither the census nor the row proof proves that missing
predecessor. The cut theorem itself holds for its explicitly independent
input geometries regardless of predecessor status.

## Exact new producer census and raw remaining domains

`HIGHER_Q5_FULL_census.cpp` is a new source, leaving the old census frozen.
It enumerates every nonzero even Z of size k-1 and every odd W of size k
nonadjacent to Z, retaining root adjacency. For each normalized odd target
v=1,7,31 it separates free/covered status. Coordinate permutations fixing
root0 normalize all opposite-parity targets to these weights1,3,5.
For free targets, any unit vertex in W is recorded as the conditional
root-adjacent-to-predecessor branch BEFORE cut tests; all remaining free
records have fully independent holes. Then all SIX actual target-oriented
cuts are tested for b-a in {0,1,2}, excluding a=b=0. Only genuinely unhit
records are written as raw original labels, with sorted Z followed by W.

The old k>=7 eligible-only shortcut is removed. Every k=6,...,9 runs the
actual cut tests and writes all six residual files, including empty files.
The program performs no matching-realizability exclusion. Each record
has 2k-1 bytes. These are hole-geometry counts, not matching counts or
automorphism-orbit counts. A hole geometry need not be realizable by a
short original matching; no such restriction is used in this exhaustive
over-domain.

| Holes | Covered residual v1/v7/v31 | Covered total | Free residual v1/v7/v31 | Free total |
|---:|---|---:|---|---:|
|12|2364029 /2632038 /2824049|7820116|0 /80622 /107984|188606|
|14|2760900 /3125851 /3365650|9252401|0 /94182 /137860|232042|
|16|725370 /834303 /912495|2472168|0 /15786 /27060|42846|
|18|22260 /27735 /30810|80805|0 /0 /0|0|

Each output JSON records the eligible count, cut-covered count,
free-root-adjacency reduction count and residual count. Their sum is
checked. All eligible counts agree exactly with the old independent-domain
census, while the k>=7 cut filtering is new. All raw file lengths equal
the stated residual count times 2k-1. These are producer consistency
checks, not a substitute for an independent census/domain audit.

The eighteen-hole free residual being empty is a conditional statement
about this reduced domain; it is NOT a full eighteen-hole theorem while
the sixteen-hole predecessor is unproved. All four layers remain open.

## Next shared inputs and limits

The frozen raw file naming is
`HIGHER_Q5_FULL_residual_h{12,14,16,18}_v{1,7,31}_{covered,free}.bin`.
Their SHA-256 pins, source, proof and accepted import/review hashes are
recorded in the new manifest. Counts are only the initial near-balanced
filter, before lookup of existing marked rank registries, accepted T63
split, T44 and other local inputs. They must not be described as the final
number of difficult or unproved matching cases.

For example twelve-hole rows(2,1),(0,3) require marked Q5 T37 inputs:
three minority plus seven majority holes, omitting two majority holes.
Their complement has22 endpoints, so the same matching-connectivity
rank method would require1024 legal short forests rather than2048.
Actual included holes come from original Z union W and are independent.
First reuse already accepted actual marked T26/T15/T17/T63 registries
where applicable; new T37 geometries must have their own profile and
positive certificates. No unprofiled universal local input is assumed.

All new computational evidence here is producer-only pending fresh
independent review. No full12--18-hole layer or full P6 conclusion is
asserted, and no failed search is a negative certificate.
