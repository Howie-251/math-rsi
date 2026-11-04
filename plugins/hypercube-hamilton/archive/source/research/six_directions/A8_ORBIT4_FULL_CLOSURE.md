# A8: full closure of the fourth residual geometry orbit

2026-11-01. ARIS proof-writer. Complete proposed orbit proof relative to
explicit imports and positive finite certificates; fresh review pending.
Full A8 and full P6 remain open.

## Exact theorem

Let F be any matching of K(Q5) with holes exactly

$$H=\{0,1,2,4,15,23,27,29\}.$$

Then there is a cycle on exactly Q5 minus {0}, containing F, with every
edge outside F short. All twelve required matching edges may be arbitrary,
including long and same-parity edges. Coordinate permutations transport
this theorem to all30 marked geometries in the fourth row of
A8_PARTIAL_PROOF_PACKAGE.md (zero-based orbit index3). This statement is
about that exact orbit, not all A8 inputs.

## Imports

Use GQ4-avoid, the complete Q4 T15 and T63 classifications, and the two-
and three-bridge sufficient criteria, with accepted scopes in
A8_BRIDGE_INPUTS_REVIEW.md/.json. The proof below derives the needed
four-cut restrictions explicitly; the unreviewed diagnostic typed spectrum
is not a premise. No full A8, A10, or higher-hole P6 conclusion is imported.

## 1. Four valid cut templates

For bit b let A have coordinate zero and B coordinate one. A contains the
forbidden hole0. In each row choose the A bridge holes whose B mirrors are Y.

| b | Y in B | possible fixed obstruction edge pq | B local theorem |
|---:|---|---|---|
|2|3,6|10--18|T15|
|4|5,6|12--20|T15|
|8|9,10,12|8--24|T63|
|16|17,18,20|16--24|T63|

The first two A faces have two minority and two majority original holes;
consuming the two minority bridge sources leaves two majority holes.
The B compression has one minority and five majority holes, omitting Y.
The last two A faces have three minority and two majority holes; consuming
three minority bridge sources again leaves two majority holes. Their B
compression has six same-parity holes, omitting the three members of Y.
All bridge vertices are originally covered. Direct coordinate deletion
and minority translation give exactly the obstruction edges displayed.
These facts can also be verified directly from H and the cut bits.

## 2. A sufficient condition outside a restricted-edge family

Fix one row, put S=Y union {p,q}, and suppose pq is not an original edge
of F. The restricted-edge family for this row consists of matchings with:

1. every original crossing edge having its B endpoint in S;
2. every internally matched member of Y having its mate in S.

If a matching violates either condition, its audited bridge criterion
succeeds. Indeed form G=F_B union C union the bridges. Its A endpoints T
are the crossing ports and the bridge sources. Pair its T-to-T components
into P. Every other G component meeting T has one B terminal.
Violation of condition1 or2 gives a terminal outside {p,q}: respectively
a nonbridge crossing port outside S, or the outside mate of an internal
bridge. Let e=1 when both p,q are terminals rooted in T, and e=0 otherwise.
The total number of rooted terminals is even, and the outside terminal
ensures it is strictly greater than2e. Since that number is |T|-2|P|,

$$ |T|/2>|P|+e. $$

This is exactly the strict inequality in the accepted bridge criterion,
with pq absent as required. It gives the desired31-cycle. Thus an input
not covered by any of these four constructions must, for each row,
either contain its fixed edge pq or belong to its restricted-edge family.
This necessary condition for remaining inputs is all that is needed;
no assertion that a failed template disproves the original theorem is used.

## 3. Disjoint complete description of the remaining inputs

Partition by the four-bit mask recording which displayed fixed edges
belong to F, in table order. For a bit set to1 require that edge. For a
bit set to0 exclude that edge and impose its restricted-edge conditions.
The required edges must be pairwise disjoint. Each restricted condition
is precisely an allowed-edge graph on the24 covered vertices: crossing
edges may enter B only at S, and an internal B edge meeting Y may not
leave S. All other original edges are allowed.

Intersect these graphs for the unset bits, remove the vertices covered
by the required edges, and enumerate all perfect matchings of the remaining
graph. This is a disjoint, exhaustive partition of every input left by
Section2. It places no shortness restriction on the original matching.

The nonempty masks and exact counts are:

| mask | required fixed edges | matching count |
|---:|---|---:|
|3|10--18,12--20|2025|
|7|10--18,12--20,8--24|99225|
|11|10--18,12--20,16--24|99225|

The total is200475. Masks containing both final fixed edges are impossible
because these edges share24. Every other empty branch has an odd connected
component in its allowed graph, preventing a perfect matching; actual
components are recorded in the independent verification output.

The producer A8_orbit4_joint_bad_enumerate.py generates the full inputs
and branch graphs. The separate verify_A8_orbit4_joint_bad.py reconstructs
the graphs from the cut definitions, verifies odd-component obstructions,
and enumerates the remaining perfect matchings in reverse vertex order,
without importing producer code or using its memoized counts. It checks
exact set equality, uniqueness, all required fixed edges, and all unset
fixed-edge absences against the24-byte input records.

## 4. Complete positive certificates for the finite remainder

A8_orbit4_joint_bad_certificates.bin contains exactly200475 records of55
bytes: the twelve original matching edges (24 bytes), followed by a31-
vertex cycle. The independent verifier checks each input is precisely the
corresponding member of the complete input domain; all31 listed vertices
are distinct and equal to {1,...,31}; every original edge appears; and
every other cycle edge, including the closing edge, has Hamming distance1.
The vertex sequence itself proves connectedness and excludes extra cycles.

All200475 records pass. The search producer reports no unknown or exhausted
input, but search exhaustiveness is not a proof premise: the complete
positive certificates and independently checked domain are sufficient.
There are no unchecked residual inputs in this finite remainder.

## 5. Conclusion and remaining scope

Every matching with holes H either satisfies one audited cut construction
or is one of the completely verified positive finite inputs. This proves
the exact theorem. Coordinate permutations preserve the omitted vertex0,
short edges, and the arbitrary matching domain, so the30-member orbit is
covered. The other A8 residual orbits and full P6 remain separate obligations.
Semantic acceptance remains same-family/provisional relative to explicit
imports, pending fresh review of this complete assembly.
