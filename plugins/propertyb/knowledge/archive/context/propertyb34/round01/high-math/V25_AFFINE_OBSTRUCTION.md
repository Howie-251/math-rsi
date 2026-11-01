# The affine nine-lock obstruction at 25 vertices is removable

## Target and scope

Let H be a pair-covering simple five-uniform hypergraph on 25 vertices with 34
edges, and let r be the number of degree-six vertices. A degree-six vertex has
codegree one with every other vertex. The earlier selection lemma supplies nine
pairwise-unit locks of degrees 6^q 7^(9-q), where q=min(r,9).

This note handles the particular case where their large traces are exactly the
twelve lines of AG(2,3), each a triple. It does not classify all nine-lock inputs.
The exact formulas and all retained witnesses have independent injection ABC
checks; the new actual-selection argument remains a paper candidate.

## The original obstruction

All 36 pairs of the nine locks lie in the affine triples, so there are no pair
traces. Every lock belongs to four triples. Its singleton multiplicity is two
at degree six and three at degree seven. The empty trace multiplicity is q-5.

For q=5,6,7 the existing direct bounds are respectively 0, 393/1040, and
8243/10920. A new exact dynamic program over all lock orders and positions still
leaves q=8 and q=9 above one: 11601/11440 and 6476/6435. These are limitations of
this local bound, not counterexamples.

## A tenth actual lock exists

Write t for the number of degree-seven vertices. The degree sum gives

    170 >= 6r + 7t + 8(25-r-t), hence t >= 30-2r.

For r=8, at least fourteen degree-seven vertices exist. The one already selected
degree-seven lock has total codegree excess four, so at most four other vertices
have nonunit codegree with it. After discarding these and itself, a new
degree-seven vertex remains. It is automatically unit with the eight low locks.

For r=9, at least twelve degree-seven vertices exist, and any one is unit with
all nine low locks. For r>=10, choose an additional degree-six vertex instead.

## Complete local extension

Let x be the new unit lock, of degree d=7 or d=6 as above. Every old lock meets x
in exactly one edge. The old traces of those edges therefore partition the nine
old labels. Their only positive possibilities are affine triples and singleton
traces. Distinct affine triples chosen for this partition must be disjoint,
hence belong to one parallel class.

If a is the number of chosen affine triples, the partition has 9-2a parts, so
9-2a<=d and a<=3. Promote each selected old trace T to T union {x}; its old
multiplicity drops by one. The singleton trace {x} has multiplicity
d-(9-2a), subtracted from the old empty multiplicity. Negative multiplicities
are impossible and discarded. This recovers every actual extension exactly.

The possibilities and independently replayed worst bounds are:

| Old profile | New degree | Complete labelled extensions | Maximum bound |
|---|---:|---:|---|
| q=8 | 7 | 24 | 4618/5005 |
| q=9 | 7 | 28 | 6014/6435 |
| q=9 | 6 | 16 | 5671/6435 |

All bounds are strict. Each extension records its actual ten-lock counts,
positions, total/pure quota certificate and every row in
`V25_AFFINE_EXTENSION.json` or `V25_AFFINE_TENTH_LOW.json`. The script checks
the usual Fraction formula against a separately expanded 34-stub injection
count; `independent_ABC: true` is stored per witness. The full-order position
optimization is only a way of finding these finite witnesses.

## Remaining obstacle

The affine family, previously a concrete failure of the nine-lock template, now
has a complete actual tenth-lock resolution. General nine-lock families,
including other linear triple families and four/five-point traces, remain
unclassified. A proof of the full 25-vertex branch still requires a universal
selection/coverage argument or a smaller family of forced good substructures.
