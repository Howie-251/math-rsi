# Two six-degree points and one nine-degree point: the single-K5 branch

Let H be a25-point,35-edge pair-covering simple five-uniform hypergraph of degree spectrum6²,9,7²². If five seven-degree points form a positive-weight K5, then H has Property B. Their weighted rows4 force internal weights1 and exterior weights0, so they form a group G with λ=2 internally and λ=1 to every exterior point.

The two six-degree points are globally unit, since their weighted row is4·6−24=0. The nine-degree point has weighted row12. For a seven/nine pair the codegree is at most5, using the seven-degree row; no nine/nine pair occurs.

## The actual group inventory and the ten direct exclusions

The G degrees and internal/external codegrees are exactly those of the existing single-K5 proof. Thus the complete27 inventories, their20-external-point partition marginals, and their reduction to22 surviving inventories remain valid. For every exterior point v, its nonempty G-traces form a partition Π_v of G and its empty-trace degree is d(v)−|Π_v|. These facts hold also at degrees6 and9.

A previous seven-degree external-star certificate applies whenever a genuine seven-degree external point is selected: individual degrees of unlocked vertices do not enter the raw permutation bound. For each of the ten directly excluded classes, the exact strict-trace lists in `MIXED_ONE_SIX_K5_SELECTION_CHECK.json` provide either at least two triple-trace edges, or at least two pair-trace edges. In the latter three classes the strict pair-edge counts are6,4,2 (identifiers14,20,22).

There are only three special exterior points (the two sixes and the nine). Two triple-trace edges with no seven-degree exterior point would need four different special exterior points: an exterior point cannot be in two G-triple edges, because any two three-subsets of the five-point G intersect. This is impossible. Two pair-trace edges with no seven-degree exterior point would both have the entire three-special-point set as their exterior part, repeating a pair containing a six-degree point; this contradicts its global unit codegree. Thus a true seven-degree external caller exists for each of the ten direct exclusions11,13,14,15,16,17,19,20,21,22.

The remaining inventory identifiers are1,5,7,8,9,10,12,18,23,24,25,26. They are treated explicitly below, including12 and25.

## Positive triple choices and the old seven/seven certificates

The exact selected triple-trace orbits from the existing single-K5 proof have edge counts2 for1,5,8,10,26;4 for7,9; and5 for18. Every exterior point belongs to at most one G-triple edge.

For1,5,8,10 a selected triple edge forces each of its two exterior endpoints into the same additional unique G-trace slot (two such slots in8). Hence the endpoints have codegree at least2, so neither endpoint can be six-degree. Avoid the single nine-degree point by choosing another edge in the orbit of size2; both endpoints are then seven-degree and the old seven/seven certificate applies.

For7,9,18 the orbit has at least4 edges, greater than the three special points, so choose a triple edge with both endpoints seven-degree and apply the old certificate.

For26 the orbit has two edges. Avoid the nine-degree point. The selected endpoints are6/6,6/7, or7/7; the latter two are already covered by the existing one-six or old seven/seven certificates. In the new6/6 case their nonempty stars are both forced to {1,8,22}, their only common edge has G-trace22, and the raw bound is3235/3366<1.

## The global partition arguments for23 and12

For23 all exterior partitions have zero, one or two pair blocks. If their numbers are n0,n1,n2, the unchanged group marginals give n0+n1+n2=20 and n1+2n2=30. Hence n2≥10. After removing three special points at least seven seven-degree B points (those with two pair blocks) remain. Their at least14 incidences with only ten pair-trace edges force a real seven/seven B–B pair on one edge. Its full local inventory is one of the already strict36 B–B inputs. No assumption on the degrees of the other exterior points is made by this caller.

For12 put D(Π)=number of non-singleton blocks−1−1_{6∈Π}, where6 here is the bitmask{1,2}, not a degree label. The actual group marginals give Σ_v D(Π_v)=2. Every seven-degree exterior star has D≤0 unless H is already colorable. Every partition allowed by the group inventory has D≤1, and D=1 only at V1={5,26} and V2={3,28}, all four blocks being unique slots. Therefore at least two of the three special points have D=1, and at least one is six-degree. Choose this six-degree point and another D=1 special point. They cannot have the same V-type, which would repeat two unique edges and violate the six-degree global unit condition. Opposite V-types have no common nonempty block, so their sole common edge has empty G-trace.

The selected pair has degrees6/6 or6/9. Its two directions for V1,V2 give exactly four new forced inputs, all raw strict, maximum67409/72930. This argument uses the actual20-point marginal, not a single-star black box.

## The unique four-trace point25 and unique triple24

For25 the positive four-trace30 edge has one exterior point with forced Π={1,30}. Degrees6 and7 were already strictly covered. Degree9 supplies one new six-lock input, empty-trace degree7, raw bound3094931/3325608<1.

For24 the unique triple28 edge has two exterior points with nonempty stars A={1,2,28} or B={3,28}. The possible unordered degree pairs are6/6,6/7,6/9,7/7,7/9; a nine/nine pair is impossible. Existing certificates cover6/7 and7/7. With a six-degree endpoint, the codegree is1, q28=1, every other common-slot count is0, and only AA,AB,BA are feasible. Thus6/6 and6/9 each give three new inputs.

For7/9 the codegree is1,…,5. In AA the singleton shared-slot counts q1,q2 lie in{0,1} and q0=0,…,4−q1−q2, giving16 inputs. AB and BA each have q0=0,…,4, giving ten combined. BB forces q3=1 and q0=0,…,3, giving four. These36 new mixed inputs have maximum raw bound37491/38896<1.

All pair inventories use the actual degrees to obtain p0=d(x)−|Π_x| and r0=d(y)−|Π_y|, and then the exact four cells μ−p−r+q,p−q,r−q,q. Nonnegative slot capacities,35 total edges and all low-point unit conditions are checked.

## Finite certificates and scope

Only42 new forced inputs are needed: four for12,36 for24, one for25 and one for26. `MIXED_TWO_SIX_K5_A_PILOT.py/json` gives their concrete layouts and raw bounds; all are strict, maximum37491/38896, in3.29 seconds. `MIXED_TWO_SIX_K5_A_REPLAY.py/json` independently hand-lists this exact domain, restores every trace, checks all degrees and codegrees and recomputes all25 rows of A/B/C using direct binomial coefficients. It imports no generator, DP, probability or quota implementation and passed in0.37 seconds.

The old22-class selection interfaces and their precise strict-trace/orbit lists remain explicit dependencies, independently checked in `MIXED_ONE_SIX_K5_SELECTION_CHECK.py/json`. All22 group inventories have now been covered for spectrum6²,9,7²². Combined with the no-K5 Brooks caller and two-low eight-unit gate in `MIXED_TWO_SIX_UNIT8.md`, this proves Property B for the complete spectrum6²,9,7²². Spectrum6²,8²,7²¹ is separate.
