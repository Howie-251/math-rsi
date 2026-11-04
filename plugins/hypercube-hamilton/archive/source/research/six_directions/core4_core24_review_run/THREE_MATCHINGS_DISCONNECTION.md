# Blocking three boundary pairings

Date: 2026-11-01. Proof-writer; independent review pending.

## Claim

Let V be a set of even cardinality N>=6. For any collection of at most
three perfect matchings R_i on the complete graph on V, there is a
perfect matching D such that the multigraph D union R_i is disconnected
for every i. Common edges count twice in this multigraph, but connectivity
is the same as in the ordinary edge-set union.

## Proof

The empty collection is immediate. Repeat a member if necessary so the
collection has three entries, with repetitions allowed.

If N>=10, choose an edge e1 of R1. At most two edges of R2 meet its two
vertices, so R2, having at least five edges, has a disjoint edge e2.
At most four edges of R3 meet the four chosen vertices, so R3 has an
edge e3 disjoint from both. Complete the three disjoint edges to a perfect
matching D on the remaining even number of vertices. For each i, the
shared edge ei is a two-vertex component of D union Ri: its endpoints
already have their only partner in both matchings. Since N>2, the union
is disconnected.

For N=6 or 8 relabel V so R1 is the canonical consecutive pairing.
This loses no generality: every perfect matching can be sent to that
pairing by a vertex bijection, which preserves connectivity and sends
the other two matchings to arbitrary perfect matchings on the same set.
There are respectively 15 and 105 perfect matchings. The certificate
`three_matchings_disconnection.json` lists every matching and, for every
ordered choice of R2,R3, supplies an index of a D whose union with each
of R1,R2,R3 is disconnected. There are 225 and 11025 pairs, including
equal matchings. `three_matchings_disconnection.py` checks each union
by graph traversal. A fresh checker must verify matching-list coverage,
the complete rectangular index set and every specified D; failed search
is never a certificate. Undo the relabeling to conclude. QED.

## Application principle

Suppose a construction, for every auxiliary boundary pairing D, supplies
a pairing R such that D union R is connected. If at most three specific
pairings are forbidden and N>=6, the construction has a permissible
choice: choose D from the claim to rule out all three forbidden outputs.
This respects the quantifiers; it does not assert that one can prescribe
R independently of D.
