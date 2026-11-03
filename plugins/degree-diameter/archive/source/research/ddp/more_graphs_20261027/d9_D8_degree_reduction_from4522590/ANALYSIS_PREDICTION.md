# A source-specific degree10 to degree9 tradeoff

This is a paper analysis of the one frozen source-derived family, with no source or candidate BFS, word enumeration, parameter evaluation, or solver. The related ledger had no exact entry for source4522590 or this five-deletion family when checked. The earlier C90/source624690 work concerns a different source and target diameter.

The source is the author's LEFT metacyclic construction in [AUTHOR_construction.json](../d10_D8_current4522590_source/AUTHOR_construction.json), with provenance in [PRIMARY_DOWNLOADS.json](../d10_D8_current4522590_source/PRIMARY_DOWNLOADS.json). Its normal modulus is50251=31*1621, phase modulus90, and actor3. The five positive normal/phase pairs are (12329,24),(3077,35),(39374,34),(25424,39),(28529,26). Source D8 is inherited; it is not reverified here.

The actual [GAUGE_ARITHMETIC.json](../d10_D8_current4522590_source/GAUGE_ARITHMETIC.json) establishes actor orders90 overall,30 modulo31, and45 modulo1621. In particular, phase45 acts as (-1,+1) on the two CRT components. The source field conjugation c=361 and scale406 give field normals (0,1,-371,-187,-771), while the modulo31 normals remain (22,8,4,4,9). These are source receipts, not constants recomputed by this analysis.

## Frozen family and testable expectation

Replace only the field1621 by811. Keep the phase modulus90, modulo31 actor3 and the five phases (24,35,34,39,26). For each of the24 primitive45th roots beta in F811, use the fixed field normals (0,1,-371,-187,-771). Delete one of the five inverse pairs and add the zero-normal involution h=(45,0,0). This gives120 settings before the explicit connectivity check below.

The analytical expectation is that at least one connected setting has D<=8. Its mechanism is a genuine degree/order tradeoff: the field is approximately halved, and h provides an immediate phase45/control route in place of one ordinary inverse pair. This is a falsifiable expectation, not an inherited diameter theorem. This file records a source-informed expectation; global pre-experiment chronology is not asserted here. The producer's frozen PREDICTION is the authoritative experiment chronology.

The target order is90*31*811=2262690, and a simple9regular realization has10182105 edges. The parent owns the fresh (9,8) baseline comparison and the numerical experiment. No other actor order, phase set, field, normal vector, or nonzero-normal choice of h is covered by this family.

## Group law, simplicity, and gauge scope

Write an element as (j,z,t), with j modulo90, z modulo31, and t in F811. The LEFT law is

    (j,z,t)*(k,w,s) = (j+k, z+3^j*w, t+beta^j*s).

Its inverse is (-j,-3^(-j)z,-beta^(-j)t). The period conditions hold because30 and45 divide90. Each negative generator must be computed by this new law, rather than copied from the source modulus.

The ten original positive/negative phases are24,35,34,39,26,66,55,56,51,64. They are distinct and avoid0 and45. Removing one inverse pair and adding h therefore gives nine distinct nonidentity elements, with h=h^-1. The Cayley graph is consequently simple and9regular for every setting, whether connected or not.

For LEFT multiplication, conjugating by the pure field translation c changes a normal b at phase j to b+(1-beta^j)c. Scaling all field normals by a common nonzero scalar is another group automorphism. Such operations remain isomorphisms after deleting a pair. Here beta^45=1 also means that field conjugation preserves the chosen h field normal0. The modulo31 coordinate is unchanged by the source field gauge. The retained source-normalized integer vector defines a controlled transfer; it is not a completeness assertion for arbitrary target voltages. The primitive90 alternative would change this h/gauge relationship and is outside scope.

## Connectivity without old-source diameter assumptions

Use [x,y]=xyx^-1y^-1. Since h acts as (-1,+1), for every retained positive g_i,

    [h,g_i] = (0, -2*z_i, 0).

All z_i in (22,8,4,4,9) are nonzero modulo31. Thus the retained generators contain the whole pure C31 subgroup. The phase gcd with90 and45 is1 for each deletion frame, so projection onto Q=C31 semidirect C90, of order2790, is onto.

The field component of the commutator of g_i=(j,z_i,b_i) and g_k=(l,z_k,b_k) is

    (1-beta^l)*b_i + (beta^j-1)*b_k.

If it is nonzero, this phase-zero element raised to the31st power kills its C31 coordinate and keeps a nonzero F811 coordinate. Because811 is prime, the entire pure field subgroup follows. Together with the onto projection to Q, this proves connectivity.

For the four frames retaining g_0=(24,22,0), some other retained b_i is nonzero, and beta^24!=1. The displayed commutator then has field component (beta^24-1)b_i!=0. These four frames are connected for all24 actors.

For the frame deleting g_0, all remaining field actors are nontrivial. The four affine maps have a common fixed point precisely when the four values

    b_i/(1-beta^j_i),  i=1,2,3,4,

are equal. If they differ, a pair of maps fails to commute, giving the nonzero commutator above and connectivity. If they are all equal, every field map fixes that same point, as does h, so the field orbit cannot be all811 points: the full graph is disconnected. Thus this one frame needs the producer's explicit four-ratio arithmetic check for each actor. No connectedness assertion for these24 settings is made before that check.

## What the route change can and cannot preserve

The operation replaces a whole inverse pair, so it is not edge-monotone. Source D8 does not transfer. Even a word avoiding the deleted pair changes its field endpoint when1621 is replaced by811, so preserved word syntax is not preserved all-pairs coverage.

Inserting h changes a path phase by45. Its field action is identity and its field normal is zero, so it can supply phase/control alternatives without itself supplying a new field translation. In the modulo31 coordinate, its order-two action supplies the useful inversion above. Whether these new control routes compensate for the lost pair simultaneously in every field/control slot is exactly the full coverage question, not something settled by legality, connectivity, raw word counts, or a quotient pass.

For a connected Cayley setting, one complete identity-root distance computation gives the full graph diameter by left translations. A truncated R8 failure proves D>8 but is not an exact global diameter or an ordinary unordered bad-pair count. Only a complete passing numerical setting warrants exporting a new graph.

No numerical prediction verdict is supplied by this paper file. The producer owns the120-setting results and merges this evidence into its same-family row.
