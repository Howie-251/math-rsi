# Canonical source gauge and the cyclotomic transfer boundary

The actual `AUTHOR_construction.json` and `AUTHOR_README.md` bind a two-base regular voltage graph. Group coordinates `(v,j)` have LEFT law `(v,j)(w,k)=(v+4^j*w,j+k)` over `F4051 semidirect C25`. Directed links act by right multiplication of the group label; reverse darts use the true group inverse. Source loops are `(0,3)` on base 0 and `(178,8)` on base 1; the three links from base 0 to 1 are identity, `(1,2)`, and `(2122,15)`. The published source diameter 10 is inherited, with no source graph generation or BFS here.

## A source-compatible gauge, not an arbitrary field lift

For right-voltage edges `(i,g)--(j,g*s)`, a base coordinate change `g'=g*h_i` replaces the voltage by `h_i^-1*s*h_j`. In general this can make one chosen link the identity. Once that link is identity, the remaining changes preserving it require `h_0=h_1`, so the loop voltages may only be conjugated together, not independently translated.

For a LEFT semidirect law, conjugation by `(c,0)` sends `(v,j)` to `(v+(1-r^j)*c,j)`. Kill the base-0 loop's normal coordinate by this common conjugation, then normalize the first nonzero nonidentity cross normal coordinate to one by a common field scaling. Only if all those cross normal coordinates vanish would the prescribed fallback inspect the base-1 loop normal coordinate. These operations keep every loop/link incidence and reverse pairing unchanged.

The actual source is already in this cross-first gauge: identity link, pure base-0 loop, and first other cross normal equal to one. Thus no normal conjugation or scaling is needed. Phase renumbering is the exact source isomorphism

`F(v,j)=(v,17j mod25)`, with new action `beta=4^3=64`.

Indeed `3*17=1 mod25`, so `beta^(17j)=4^j`, proving the homomorphism identity. The normalized recipe becomes

- base-0 loop `(0,1)`;
- base-1 loop `(178,11)`;
- links `identity`, `(1,9)`, `(-1929,5)`.

Here `-1929=2122 mod4051`. Also `beta^25=1` and `beta^5=4019!=1`, so beta has exact order 25. The source geometry is unchanged by this phase renumbering.

For a transfer, the literal integer coefficients 178 and -1929 must be frozen explicitly. Replacing -1929 by its old representative 2122 would give the same source but generally a different target recipe. Likewise, choosing the base-1 loop as normalizer defines the same target family only if every target field scales by its own inverse of 178, producing coefficients `1/178` and `-1929/178`. Copying the old field inverse `178^-1=660 mod4051` as a new integer coefficient would instead change the transfer family. The existing cross-normal-one gauge avoids this ambiguity.

## Why the fixed integer action 4 cannot be retained

`Phi25(t)=t^20+t^15+t^10+t^5+1`, and small exact arithmetic gives

`Phi25(4)=1100586419201=251*601*1801*4051`.

Each displayed factor is prime, and 4 has exact order 25 modulo each. If a different prime q admits literal action 4 of exact order 25, then q divides `Phi25(4)`. There is therefore no such prime q greater than 4051. In particular an enlarged prime-field candidate must change the action embedding; it is not a literal-4 enlargement.

The parent-selected q4201 is prime and is the next prime above 4051 congruent to 1 modulo 25. The intervening eligible odd numbers 4101 and 4151 are composite, and the others are even. Since 25 divides 4200, F4201 has exactly phi(25)=20 actions of exact order 25. No one of those actions was enumerated or tested by this analysis. The hypothetical order is `2*25*4201=210050`; no candidate graph or diameter is claimed here.

## Inverse, connectivity, and the correct representative-root scope

For any compatible target action beta the inverse is `(-beta^(-j)*v,-j)`. Keeping these inverse darts makes every internal loop an inverse pair. Both loop phases are nonzero in the odd phase group, and the cross phases 0,9,5 are distinct. Hence the normalized template defines a simple 5-regular graph for every exact-order-25 action.

Connectivity also holds without a source BFS. The base-0 loop supplies y, the identity link moves between bases without changing the group coordinate, and traversing the `(1,9)` link and returning by the identity link supplies `x*y^9` on base 0. Following by `y^-9` supplies x. Thus all of the target group is generated on base 0, and the identity link reaches every vertex of base 1.

Left multiplication by any group element preserves all right-voltage edges and acts transitively on each base fibre. Therefore complete coverage from `(base0,e)` and `(base1,e)` proves the global diameter bound. One root alone is not sufficient: this is a two-orbit voltage lift, not a one-orbit Cayley graph. The source README's exact automorphism-group claim is inherited only for the old graph; the target reduction needs only the explicit two-orbit deck action, not an assertion about its full automorphism group.

For an actual word with current phase j, the endpoint-polynomial recurrence is `P_new=P_old+t^j*c_dart`, with inverse polynomial `-t^(-k)*c_dart` for a forward dart of phase k. Identities modulo Phi25 transfer between compatible fields. Extra equalities occurring only after reduction in F4051, and complete field coverage of the source, do not transfer automatically. Thus the authorized target test must evaluate actual endpoint images for both base roots and each target-base/phase slot; raw word counts or distinct formal polynomials are only necessary prefilters. The source's voltage directions and valid base-word transitions must be retained.

This analysis performed only the displayed small arithmetic and group/gauge arguments. It enumerated no short words, target roots, parameters, graphs, or BFS, and it does not select or evaluate a target action. Any finite all-20-embedding gate remains the sole producer's separate task.
