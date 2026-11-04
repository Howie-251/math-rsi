# First actual T26 marked orbit: 2048 short-forest rank certificate

2026-11-01. ARIS proof-writer producer package. Complete candidate proof
relative to the primary matching-connectivity rank theorem and explicit
finite certificates; fresh independent acceptance is pending. No main
ledger or previously frozen T63 input was changed.

## Exact claim and status

Let F be any matching of K(Q5) with minority holes {0,3}, majority holes
{1,4,14,22,28,31}, and prescribed omitted holes U={1,4}. There is a simple
30-cycle on exactly Q5-U containing F, with all edges outside F short.
All twelve original required edges may be arbitrary, long, or join equal
parities. Every common Q5 automorphism transports this assertion to the
corresponding actual marked geometry, including the opposite parity
orientation. This theorem concerns this marked orbit only, not all T26.

**Status: PROVABLE AS STATED conditional on independent verification of
the supplied rank/forest certificate and the stated primary rank import.**
The producer obtained full GF(2) rank 2048 after only 9605 valid forests.
A separate Python producer check verifies all selected forests, all
4194304 connectivity bits, and every saved elimination combination.

## 1. Forest-to-cycle interface

Put H={0,1,3,4,14,22,28,31}, K=Q5-H, and U={1,4}. An admissible S is a
simple graph of short edges on Q5-U, with degree one at all 24 vertices
of K and degree two at the six included holes H-U, and with no cycle.
Its components are twelve paths, its edge count is eighteen, and its
endpoint set is exactly K. Let P(S) pair the endpoints of these paths.

For any required matching F on K, regard F and P(S) as separately labelled
matchings. If their union is one alternating 24-cycle, expand every P(S)
edge into its S path. The resulting graph is a single 30-cycle. Its path
interiors are disjoint and comprise precisely H-U. It retains every F
edge, and all introduced edges are short. A common F/P pair would form
an isolated labelled 2-cycle, impossible in a connected 24-cycle; thus
a length-one S path cannot duplicate an original F edge in a successful
pair. The expanded cycle is simple.

This interface allows adjacent included holes. The generator does not
assume an independent-cherry representation: it enforces exact degrees
and rejects every cycle with a disjoint-set forest test. The selected
forests are independently checked as actual graphs, so generator
completeness or generation order is not a premise.

## 2. Exact rank implication

Let H_24 be the binary matching-connectivity matrix indexed by every
perfect matching of the complete graph on K. Its entry h(F,P) is one
exactly when the labelled union F+P is one alternating cycle. The imported
upper bound is rank_GF(2)(H_24)<=2^(24/2-1)=2048.

The primary theorem is Corollary 3.5, from Theorem 3.4, of Cygan, Kratsch
and Nederlof, *Fast Hamiltonicity checking via bases of perfect matchings*,
JACM 2018. The generic theorem applies to all even endpoint counts and
arbitrary complete-graph matchings. The version and primary-source
alignment are recorded in `A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md`; this
proof uses that theorem at 24 rather than 22 endpoints. Its bound is the
only external algebraic premise. It does not assume bipartite required
matchings or rank properties inferred from small experiments.

Take the supplied admissible forests S_1,...,S_2048 and supplied arbitrary
perfect-matching columns X_1,...,X_2048. Their connectivity submatrix
A[i,j]=h(P(S_i),X_j) has GF(2) rank 2048, by the finite certificate.
Therefore their complete rows in H_24 are independent and span its entire
row space by the imported rank upper bound.

Every column F of H_24 is nonzero. To see this, order its twelve disjoint
edges as (a_i,b_i) and let R consist of (b_i,a_(i+1)), cyclically in i.
These pairs form a perfect matching and F+R is one alternating cycle.
If all 2048 selected rows were zero at column F, their entire span, and
hence every row of H_24, would be zero there. This contradicts h(R,F)=1.
Some selected P(S_i) thus connects with F, and Section 1 gives its positive
30-cycle. This proves the exact universal matching statement. R is used
only to establish a nonzero matrix column, not asserted to be a short
forest. A deficient rank would leave the method OPEN rather than provide
a counterexample.

## 3. Finite positive certificate and checks

The search is `Q5_T26_RANK_search.cpp`, using the configuration in
`Q5_T26_RANK_first_config.txt`. It assigns covered degrees one, included
hole degrees two, and omitted degrees zero. It repeatedly fills the most
constrained unfilled vertex with distinct short neighbors, rejecting every
edge addition whose endpoints are already connected. At a full legal
forest it derives the actual path pairing, evaluates connectivity against
2048 valid matching columns, and selects a new row only when GF(2)
elimination increases rank. It stops at rank 2048. All of these generation
details may be replaced by checking just the saved finite witnesses.

| Artifact prefix `Q5_T26_RANK_first` | Exact format |
|---|---|
| `_forests.bin` | 2048 records of 36 bytes: eighteen sorted unordered short edges |
| `_pairs.bin` | 2048 records of 24 bytes: twelve sorted unordered endpoint pairs on K |
| `_columns.bin` | 2048 records of 24 bytes: arbitrary complete-graph matching columns on K |
| `_matrix.bin` | 2048 records of 256 bytes: matrix bits, low bit first per byte |
| `_pivots.bin` | 2048 records of 256 bytes, pivot j has highest set bit j |
| `_combos.bin` | 2048 records of 256 bytes selecting original rows whose XOR is pivot j |
| `.json` | Producer search count, rank, and selected source indices |

The producer-side `Q5_T26_RANK_first_author_check.py` independently parses
every selected forest and verifies shortness, edge uniqueness, omission,
all exact vertex degrees, absence of cycles via full path traversal,
and equality with the supplied endpoint matching. It checks every column
is a matching on exactly K. It recomputes all 2048^2 connectivity bits by
an alternating walk on the two labelled matchings and compares every bit
with the saved matrix. For each pivot it verifies that its saved row
combination equals the pivot and that its highest set bit is precisely
the declared index. These triangular rows prove rank 2048 over GF(2),
without floating-point arithmetic or assumptions about the chosen basis.
Its output is producer evidence; fresh independent review remains required.

## 4. Actual Q6 marked projections and conditional coverage

For a covered-target Q6 ten-hole residual, use the accepted uniform cut
notation: root u=0, target v odd and covered, other even holes Z of size
four, odd holes W of size five, and Z union W independent. For each
outer cut A containing v, the two relevant rows are:

* (a,b)=(2,1): bridge both even holes in Z intersect A. After transfer
  the B minority holes are Z intersect B (two), its majority holes are
  (W intersect B) union the two bridge mirrors (six), and exactly the two
  mirrors are omitted.
* (a,b)=(0,3): bridge any two odd holes in W intersect A whose mirrors
  differ from u. Three sources and at most one exclusion leave a legal
  pair. B minority holes are W intersect B (two), majority holes are
  (Z intersect B) union the two mirrors (six), with the mirrors omitted.

In both rows the A endpoint input has balanced two holes and is already
accepted. The arbitrary long matching produced by transfer is allowed by
the exact T26 theorem. The accepted simultaneous bridge-conflict forest,
tag, suppression and expansion proof applies; no new global endpoint is
chosen. Whether the actual B geometry is in this marked orbit depends
only on Z,W,v and the selected cut/source pair. Common automorphisms must
map the minority set, majority set and marked omissions together.

`Q5_T26_RANK_profile.py` generates those actual projections from the
accepted 54222-record residual, normalizing a minority hole to 0 and the
other to 3 or 15 under a common coordinate permutation. It records each
geometry only once per original record even if several projections work.
This first marked orbit has 11340 actual records in that fixed domain:
3600 for v=1, 3780 for v=7, and 3960 for v=31. Every chosen outer cut,
row, source pair and actual local marked geometry is retained in
`Q5_T26_RANK_first_coverage.json`. Exact remaining bytes are saved under
the first-prefix residual binaries. Counts and overlap with the separate
conditional T63 reduction are producer coverage claims requiring fresh
application review; no decrement is entered into any accepted ledger.

## Dependencies and limits

The local theorem depends only on the generic primary rank bound and
the 2048 selected finite forests/matching columns/full-rank matrix.
Its proof uses no full A8, A10, T63, ten-hole Q6 statement or P6 result.
The optional Q6 application additionally imports the accepted uniform
transfer, its balanced-two-hole endpoint input, and the accepted residual
domain. These form an acyclic dependency graph.

The theorem has exactly the specified marked orbit scope. No full T26,
full ten-hole theorem, higher Q6 layer or full P6 conclusion is asserted.
No failed search or capped run is interpreted as nonexistence. This file
and its finite certificates are frozen for fresh independent audit.
