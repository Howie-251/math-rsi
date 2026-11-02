# Exact A-cubed translation

Let O denote old vertices, H helpers, and c(v) the unique helper attached
to old vertex v. Old-old length-three walks are inherited from the accepted
source. Within a K3 or K4, every ordered helper pair has a length-three
walk, including equal endpoints. Thus only cross-component helper pairs
and helper-old pairs need constraints.

For helpers in distinct H components, the only three-step type that can
cross components is H-O-O-H. Its middle edge must be an old source edge,
with endpoints colored by the two helpers. H-H-H-H stays in a component.
H-H-O-H and H-O-H-H would require a uniquely pinned old vertex to have two
different helper neighbors. This proves condition 2 in PRED.md exactly.

For helper i and old v, the possible type sequences are:

* H-H-H-O: the last helper is c(v). K3/K4 has every exact-two-step
  helper pair, so this is equivalent to c(v) in C_i.
* H-H-O-O: a neighbor w of v is pinned to a helper in C_i minus i.
* H-O-O-O: an old u at exactly two old steps from v is pinned to i.
* H-O-H-O: uniqueness of pins forces both helper visits to be i, and
  c(v)=i; this is already included in the first case.

Reversal gives old-helper walks. These cases prove necessity and
sufficiency of condition 3, with no reduction to a bad-pair surrogate.

## CNF

Variable x[v,i] means c(v)=i. Per vertex use an at-least-one clause plus
all pairwise at-most-one clauses. For each helper, prefix threshold
s[t,k] means at least k of the first t pins. Encode the equivalence

`s[t,k] <=> s[t-1,k] OR (x[t-1,i] AND s[t-1,k-1])`

with s[t,0]=true and s[0,k>0]=false. Assert the final threshold at load L
and negate threshold L+1. Four CNF clauses encode the recurrence, with
constant simplification.

For every cross-component pair and every directed orientation of each
old edge, use y <=> (x[u,i] AND x[v,j]) with all three equivalence clauses.
A clause over its 300 y variables requires a joining edge. Helper-old
conditions are direct positive clauses in x, with duplicate literals
removed.

For each required minimum-pin order i<j, every x[v,j] implies the
threshold s[v,1] for helper i (a pin strictly earlier than v). Orders are
0<1<2, 3<4<5, 0<3; 6<7<8<9, 10<11<12<13,
14<15<16<17, 6<10<14. These select a representative under helper
permutations within cliques and equal-size clique permutations. They do
not constrain the relative order of the two different clique sizes.

An independent paper review agreed that the graph walk conditions and
the threshold recurrence are exact. No graph-scale fiber verification
is used for this translation.
