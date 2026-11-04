# First actual T17 orbit without a triangle obstruction: rank certificate

2026-11-01. ARIS proof-writer producer package. Fresh independent review
of the forest/rank certificate and actual Q6 application is required.

## Exact claim and status

Let $F$ be any matching of $K(Q_5)$ with hole set

$$H=\{0,1,2,7,11,13,21,31\}.$$

Its minority hole is $0$, its majority holes are
$\{1,2,7,11,13,21,31\}$, and the prescribed omissions are
$U=\{1,2,13\}$. Then a simple cycle on exactly $Q_5\setminus U$, of
length $29$, contains $F$ and has only short edges outside $F$. All twelve
required matching edges may be long or join equal parities. Any common
cube automorphism transports this marked theorem, including the opposite
parity orientation. This is one marked T17 theorem, not full T17.

**PROVABLE AS STATED relative to the generic primary rank bound and
verification of the supplied finite certificate.** The producer reached
rank $2048$ after $8397$ valid short forests. Its separate producer-side
check recomputed every selected forest, all $2048^2$ matrix bits, and all
saved pivot combinations. Independent acceptance remains pending.

## 1. Positive forest interface

Put $K=Q_5\setminus H$, so $|K|=24$. An admissible forest $S$ has short
edges, omitted-vertex degree zero, degree one at all $K$ vertices, degree
two at the five included holes $H\setminus U$, and no cyclic component.
It has seventeen edges, twelve path components and endpoint set exactly
$K$. Compress each path to its endpoint pair $P(S)$.

For any required matching $F$ on $K$, take $F+P(S)$ as a labeled
multigraph. If it is connected, it is one alternating $24$-cycle.
Expanding its path edges gives a single $29$-cycle retaining every edge
of $F$. The path interiors are disjoint and cover exactly the included
holes. All new edges are short. A common pair of $F$ and $P(S)$ would be
an isolated two-edge component and is excluded by connectedness; a direct
short path therefore cannot duplicate an original edge in a successful
union. The expanded cycle is simple.

Here the five included holes are pairwise nonadjacent, so every supplied
forest has five two-edge hole paths and seven direct terminal edges.
The generator and verifier nevertheless enforce degrees and forest
acyclicity directly; completeness of a cherry enumeration is unnecessary.
Only the selected $2048$ legal positive witnesses are needed.

## 2. Universal rank implication

Use the generic matching-connectivity rank bound over $\mathbb F_2$:
for the complete matrix $\mathcal H_{24}$ on all perfect matchings of
twenty-four endpoints,

$$\operatorname{rank}_{\mathbb F_2}(\mathcal H_{24})
\le 2^{24/2-1}=2048.$$

The exact primary import is Corollary3.5, following Theorem3.4, in Cygan,
Kratsch and Nederlof, *Fast Hamiltonicity checking via bases of perfect
matchings*. Its source alignment is recorded in the frozen
`A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md`; the accepted T26 rank package
uses this identical bound at twenty-four endpoints. No rank claim is
inferred from matching samples, and no bipartite restriction is imposed.

The selected forest pairings $P_1,\ldots,P_{2048}$ and arbitrary matching
columns $X_1,\ldots,X_{2048}$ have connectivity submatrix of rank $2048$.
Thus these complete rows are independent and, by the upper bound, span
the whole row space of $\mathcal H_{24}$.

Every column indexed by an original matching $F$ is nonzero: enumerate
its edges $(a_i,b_i)$ and form the matching $(b_i,a_{i+1})$ with cyclic
indexing. Its union with $F$ is one alternating cycle. If all selected
rows vanished at $F$, every row in their span would vanish there, a
contradiction. Some selected $P_i$ therefore connects with $F$, and its
positive short forest expands to the asserted $29$-cycle. The arbitrary
matching used to prove the column is nonzero need not be a realizable
short forest; only the selected row witnesses have that requirement.

## 3. Finite certificate and source changes

`Q5_T17_RANK_search.cpp` is a new-prefix copy of the existing T26 rank
producer. The input changes are exactly three omitted vertices, seventeen
forest edges and thirty-four bytes per selected forest. Endpoint count
$24$, basis-column count $2048$, field arithmetic and connectivity
convention remain the same. The original T26 source was not modified.

The producer reads eight distinct hole labels and then three omitted
labels from `Q5_T17_RANK_candidate_first_config.txt`. It fills exact degrees
using short edges, rejects cycles with a disjoint-set test, computes the
actual path pairing, and selects a row only when binary elimination raises
rank. Generator completeness and generation order are not premises.

All certificate files have prefix `Q5_T17_RANK_candidate_first`:

| Suffix | Format |
|---|---|
| `_forests.bin` | $2048$ records of $34$ bytes: seventeen canonically sorted short edges |
| `_pairs.bin` | $2048$ records of $24$ bytes: twelve endpoint pairs using original Q5 labels |
| `_columns.bin` | $2048$ records of $24$ bytes: arbitrary perfect matching columns on $K$ |
| `_matrix.bin` | $2048$ records of $256$ bytes, least significant bit first |
| `_pivots.bin` | $2048$ records of $256$ bytes; row $j$ has highest set bit $j$ |
| `_combos.bin` | $2048$ records of $256$ bytes; original-row coefficients for each pivot |

The producer-side author checker decodes every selected forest, checks all
short edges, exact degrees, omissions, path traversal and endpoint-pair
association, and verifies every column is a matching of exactly $K$.
It recomputes all $4194304$ connectivity bits by labeled alternating walks.
It then verifies every saved pivot is exactly its recorded XOR combination
of original rows, with the required highest bit. These checks give an exact
rank lower bound over $\mathbb F_2$. Its PASS is producer evidence, not
substitute independent acceptance.

## 4. Actual Q6 rows and conditional candidate coverage

For the Q6 ten-hole domain let the root be $u=0$, the odd target $v$ be
covered, and original nonroot holes be even $Z$ of size four and odd $W$
of size five, with $Z\cup W$ independent. Take the outer face $A$ containing
$v$ and its complementary face $B$.

* For $(a,b)=(3,1)$, select all three even holes $Z\cap A$ as bridge
  sources. The final B minority hole is the sole member of $Z\cap B$;
  the majority set is $(W\cap B)$ plus the three bridge mirrors. Omit
  exactly those three mirrors.
* For $(a,b)=(0,4)$, select any three odd sources in $W\cap A$ excluding
  the mirror of $u$. Four candidates and at most one exclusion guarantee
  existence. The B minority hole is the sole member of $W\cap B$; its
  majority set is $(Z\cap B)$ plus the three mirrors, again omitted.

In either row the original uniform-transfer theorem needs only its already
accepted balanced-two-hole A endpoint theorem. Its tagged forest,
simultaneous same-parity bridge suppression and expansion give the exact
original endpoints. The new local full-rank input applies to every arbitrary
compressed B matching; it requires no unproved exclusion of a newly created
same-parity edge. Covered targets exclude no odd hole source.

Translate the actual B minority to zero and delete the outer coordinate.
Apply a common five-coordinate permutation to the majority set and all
three marked omissions. A projection is accepted only when it equals the
exact marked orbit proved here. The retained producer witness for each
record includes the outer cut, source triple, original minority, local
marked sets and an actual normalizing permutation. Nonadjacency of minority
to the four included majority holes follows from the original $Z,W$.

The complete profile of the accepted $41236$-record residual contains
$100$ actual marked T17 orbits; $64$ do not have the forced cherry at the
minority, and $36$ do. The forced case alone cannot have full rank at
twenty-four endpoints and must be treated conditionally.

For priority the selected first orbit was ranked using the newer
$4096$-record **candidate** remainder after all T26 producer rank inputs.
That T26 batch's independent acceptance is a separate import gate.
In that candidate domain there are $17$ actual T17 orbits, of which ten
have no minority forced cherry. This first orbit has the greatest available
net coverage without that obstruction, tied with three other candidates:

| Target | Candidate input | New marked-orbit records | Candidate remainder |
|---:|---:|---:|---:|
| $1$ | $910$ | $180$ | $730$ |
| $7$ | $1476$ | $342$ | $1134$ |
| $31$ | $1710$ | $360$ | $1350$ |
| Total | $4096$ | $882$ | $3214$ |

All $882$ actual projections were replayed by the producer application
checker from original Q6 labels, including the chosen source triple and
normalizing permutation. Exact remaining records are saved. These are
candidate coverage counts, not an accepted ledger decrement; the local
rank theorem, its transfer application and the T26-batch input gate all
require independent acceptance.

## 5. Triangle limitations and dependency map

If all three omitted vertices neighbor the included minority hole, its
two remaining short neighbors $p,q$ are covered and every short forest
must contain the two-edge path $p-0-q$. A required $pq$ edge would force
an isolated triangle. Those marked inputs are not claimed by this local
theorem, and no search limit or deficient rank is treated as a counterexample.
The separate forced-cherry rank reduction could cover matchings avoiding
$pq$, but a Q6 completion must still be proved not to create that edge.

The first marked orbit has only two omitted minority neighbors, so that
particular obstruction does not arise. Full rank certifies the whole
arbitrary matching statement rather than silently assuming nonbipartite
compressed edges absent.

Dependencies are generic primary rank upper bound + legal positive forests
+ exact full-rank submatrix -> this T17 orbit; separately accepted uniform
transfer + accepted candidate input chain -> its Q6 application. No A8,
A10, other T17 orbit, T26 theorem or Q6 theorem is used to prove the local
rank input itself. Full T17, full ten-hole P6 and full P6 remain outside
this package.
