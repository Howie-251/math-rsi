# Central double lift: exact projection, connectivity, and route gate

The bound source recipe is `../AUTHOR_construction.json`, with LEFT law

`(v,j)(w,k)=(v+316^j*w,j+k)`.

The source normal modulus is 6941=11*631 and its phase modulus is 90. Its five positive generators `(normal,phase)` are `(35,35),(509,5),(4285,37),(6911,49),(3639,34)`. The published source is a connected Cayley graph of diameter 7; that source fact is inherited, with no source BFS in this analysis.

Change only the phase modulus to 180. Since `316^90=1 mod6941`, the same law defines a group of order 1249380. The projection `pi(v,j)=(v,j mod90)` is a surjective group homomorphism with kernel `{(0,0),(0,90)}`. Its nonidentity kernel element kappa is central and has order two. No faithful action of C180 on the normal factor is required.

The true inverse of `(v,j)` is `(-316^(-j)*v,-j mod180)`. Thus the five new inverses are

`(1058,145),(4535,175),(5926,143),(4266,131),(4593,146)`.

Their normal coordinates agree with the old inverses because `316^90=1`; their phases equal the old inverse phases plus 90. Directly copying the source's inverse phases would be incorrect. The ten target generators project bijectively onto the ten distinct source generators, so the target is a simple 10-regular ordinary two-sheet graph cover, with 6246900 edges.

## Connectivity is provable before BFS

Let `g=(35,35)` in the target. The scalar `316^35` has residues 10 modulo 11 and 393 modulo 631, of respective orders 2 and 9. Both residues differ from 1. Consequently its geometric sum of length 18 vanishes in both fields, hence modulo 6941. It follows that

`g^18=(0,18*35 mod180)=(0,90)=kappa`.

The lifted generators project onto the published source's generating set, so their subgroup projects onto all of the source group. It also contains the full projection kernel, by the displayed power. A subgroup that projects onto the quotient and contains the kernel is the entire target group. Thus this lift is connected. The length-18 word proves generation; it says nothing about reachability of kappa within seven steps.

## The necessary gate and the diameter inference

If the target graph has diameter at most 7, a word of length at most 7 must reach kappa from the identity. Immediate generator/inverse backtracks cancel, so enumeration of all nonbacktracking words of lengths zero through seven is complete for this necessary question. In particular the implementation must use the specific true inverse dart IDs, not a condition based only on phase signs.

If no such word reaches `(normal0,phase90)`, this fixed central double lift is rigorously rejected without constructing a graph or running BFS. This is a route obstruction for this fixed choice of lifted generators, not for all two-sheet covers or all degree-10 constructions. Conversely, finding such a word passes only a necessary gate; it does not prove radius 7 covers the whole target.

For the right-generator Cayley adjacency `z -- z*s`, every LEFT translation is an automorphism, acting transitively on all vertices. Therefore a complete identity-root BFS of the target gives the exact global diameter. A radius-7 miss alone rejects diameter 7; an exact larger diameter requires the completed distance data or a separate upper bound. This reduction does not require a source BFS.

This note performed only small modular arithmetic and the displayed group argument. It enumerated no words and generated no graph, parameter batch, or BFS. The sole producer owns the seven-step gate and any graph run; no higher central modulus or altered generator set is requested.
