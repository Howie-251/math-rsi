# A 23-vertex pair-covering hypergraph with 34 edges and minimum degree at least 7 is two-colorable

**Status:** complete paper candidate, with independent exact replay of every retained probability certificate. It is not yet a Lean theorem. The argument uses the existing conditional greedy-coloring lemma and its genuine link bad-pair quotas. Its only finite classifications are local traces on at most seven selected vertices.

Let H be a simple 5-uniform hypergraph on 23 vertices, with 34 edges, covering every pair, and with minimum degree at least 7. Write d(x) for degree and lambda(x,y) for codegree. We show that H has Property B.

## 1. The degree-seven weighted graph

The total degree is 170. If L denotes the degree-seven vertices and r=|L|, then

    170 >= 7r + 8(23-r),    so r >= 14.

Set w(x,y)=lambda(x,y)-1. Pair coverage makes these nonnegative integers. For every x in L,

    sum_{y != x} w(x,y) = 4d(x)-22 = 6.                 (1)

The strong-codegree branch from the independently verified first-hour package handles all pairs in L with lambda>=4: lambda>=5 by a two-lock bound; when the maximum is4, an arbitrary third vertex of L gives one of26 complete three-lock profiles, all strict, with maximum82689/83980. Thus henceforth 0<=w(x,y)<=2 on L. The source is `context/propertyb34-hour1-20261013/MIDDLE_PROGRESS.md`, with the49 double/triple witnesses in `MIDDLE_THRESHOLDS_VERIFIED.json` in that directory.

## 2. Selecting six vertices by minimum total weight

Choose S subset L with |S|=6 minimizing

    W = sum_{{x,z} subset S} w(x,z).

For x in S put d_S(x)=sum_{z in S-x}w(x,z); for y outside S put d_S(y)=sum_{z in S}w(y,z). A swap of x for y cannot reduce W, hence

    d_S(y) >= d_S(x)+w(x,y).                            (2)

Let b be the total weight between S and L-S. Sum (2) over y in L-S. The five vertices of S other than x have total weighted degree at most6 by (1). Subtracting twice the internal weight yields

    (r-6)d_S(x)+sum_{y in L-S}w(x,y) <= b
      <= 30+d_S(x)+sum_{y in L-S}w(x,y)-2W.

Therefore

    (r-7)d_S(x)+2W <= 30.                              (3)

The weighted graph induced by L has total weight at most3r. Average W over all six-subsets to obtain

    W <= floor(90/(r-1)) <= 6.                         (4)

Since W>=d_S(x) and r>=14, (3) excludes d_S(x)>=4. If any d_S(x)=3, it forces W<=4. Thus our actual selected S belongs to one of two complete local domains:

- maximum internal weighted degree at most2, total weight at most6;
- maximum internal weighted degree3, total weight at most4.

No assumption about a three-color class size is needed.

## 3. The local six-vertex classification

For selected vertices s_1,...,s_k, let n_T be the number of actual edges whose intersection with the selected set is exactly T. These are nonnegative integers, vanish for |T|>5, and obey

    sum_T n_T=34,
    sum_{T contains i} n_T=7,
    sum_{T contains i,j} n_T=1+w(i,j).

The standard conditional greedy bound and genuine bad-pair deductions give a rigorous upper bound U on the probability that the resulting coloring fails. Every certificate used below has U<1; consequently it proves a coloring exists. An integral type profile is a relaxation of the actual hypergraph data, so allowing unrealizable profiles only enlarges the verification domain.

For completeness, the profile enumeration fixes all multiplicities n_T with |T|>=3. Each choice is bounded above by every remaining pair multiplicity. Exact two-point counts are then determined by the pair equalities, singleton counts by the degree equalities, and n_empty by the edge count. Negative results are rejected. This is exhaustive because the actual n_T is one of these nonnegative choices. Relabeling the selected vertices transports all lock positions and inequalities; it does not identify distinct actual inputs without transporting the certificate.

A larger profile can be discarded when any smaller projection has a strict certificate. When adjoining a vertex v, let a_T count old edges of trace T which contain v. The complete extension range is

    0<=a_T<=n_T, a_T=0 if |T|=5, sum_T a_T=d(v).

The new counts are n'_T=n_T-a_T and n'_{T union {v}}=a_T. The new pair constraints are sum_{T contains i}a_T=lambda(s_i,v). These exact splits are the sole extension mechanism in the tables.

The maximum-degree3/W<=4 domain has9 weighted graph shapes. Complete generation, after discarding already-strict four- and five-point projections, leaves66 trace profiles. All66 are strict, with maximum4809/4862. See `SIX_DEGREE_THREE.json` and its independent `SIX_DEGREE_THREE_VERIFIED.json`.

For maximum weighted degree at most2, each component is an ordinary path or cycle, an isolated vertex, or an isolated edge of weight2. The complete five-to-six extension leaves725 trace orbits after discarding strict lower projections. Pure quotas prove530; shared-bad-count joint-layout certificates prove117 more. The78 remaining profiles have only the following weighted graphs (all nonzero weights equal1):

| Weighted graph on S | W | Remaining trace profiles |
|---|---:|---:|
| 2K2 + 2K1 | 2 | 8 |
| K3 + 3K1 | 3 | 4 |
| 3K2 | 3 | 28 |
| K3 + K2 + K1 | 4 | 21 |
| 2K3 | 6 | 17 |

The sources are `SIX_DEGREE_TWO_CANON.json`, `SIX_DEGREE_TWO_CANON_STRICT_JOINT.json`, and `SIX_RESIDUES_STRICT_JOINT.json`. The lower projection tables are `FOUR_LOW.json` (699 profiles;617 pure plus11 joint strict,71 residual) and `FIVE_DEGREE_TWO.json` (246 profiles after four-projection pruning;110 pure plus47 joint strict,89 residual).

## 4. The equality branch W=6

Every x in S has internal weighted degree2. From (2), each y in L-S has d_S(y)>=3: the inequality first forces d_S(y)>=2, but any positive weight w(x,y) then raises its lower bound to at least3. On the other hand, (1) gives total cut weight at most36-12=24. As r>=14, equality is forced throughout:

- r=14;
- every y in L-S has d_S(y)=3;
- all six vertices of S have total weighted degree6 within L;
- every positive weight across the cut equals1 (by (2));
- every pair from S to a vertex outside L has weight0.

For a positive cut edge xy, swapping x for y preserves W=6. The replacement set is still a global minimizer. Equation (3) again forces all its internal degrees to equal2. If z is another S-neighbor of y, its new degree is 2-w(x,z)+1, so w(x,z)=1. Therefore every outside vertex's three S-neighbors form an ordinary triangle. Every selected vertex has four cut neighbors, so S consists of two disjoint triangles A,B. The outside vertices split into sets Y_A,Y_B of size4 according to which triangle they meet.

If y,z are distinct members of Y_A, swap a in A with y. In the resulting minimizing set, z is adjacent to both vertices of A-a; its three neighbors must again form a triangle, so its third neighbor is y. Thus w(y,z)=1. The same holds inside Y_B. Consequently the weighted graph on L is exactly the disjoint union of two K7 components. Every vertex of L now spends its full weighted degree6 within its component. By (1), every pair from L to a vertex outside L has lambda1.

Since r=14 and the total ordinary degree is170, the nine remaining vertices all have degree8. Append any one of them to S. Its codegree with all six selected vertices is exactly1. The complete extensions of the17 residual six-point profiles, modulo the displayed symmetries, give209 seven-point profiles; every one has a strict pure-quota certificate, with maximum2245/2288. This proves the W=6 branch. See `EQUALITY_SEVEN.json`; all209 rows occur in `STRICT_WITNESSES_VERIFIED.json`.

## 5. The branches W=2,3,4

The cut from S to L-S has total weight at most36-2W. Choose y in L-S minimizing its weight to S. Since r-6>=8,

    T=d_S(y) <= floor((36-2W)/(r-6))
             <= 4 if W=2, and <=3 if W=3 or4.          (5)

Let a_i=w(s_i,y). Then a_i is an integer in{0,1,2}, sum_i a_i=T, and by (2), T>=d_S(s_i)+a_i for every i. For each of the six sets obtained from S union {y} by deleting an old vertex:

- its total weight must be at least W, by minimality;
- if its maximum weighted degree is3 and its weight is at most4, Section3 already gives a coloring;
- if its maximum weighted degree is at most2, its exact trace must belong to the78 residual profiles in Section3.

For transparency, the complete surviving neighbor vectors after the graph-level conditions are below. The labels are specified by the edge sets of the old graph; omitted old edges have weight0. These vectors do not assume that y can be chosen separately for different projections: the same actual y from (5) is used throughout.

| Old graph, labels 1,...,6 | Remaining vectors (a_1,...,a_6) |
|---|---|
| edges12,34 | (0,0,0,0,0,1), (0,0,0,0,1,0), (0,0,1,1,0,0), (1,1,0,0,0,0) |
| triangle123 | (1,1,1,0,0,0) |
| edges12,34,56 | (0,0,0,0,1,1), (0,0,1,1,0,0), (1,1,0,0,0,0) |
| triangle123 and edge45 | (0,0,0,0,2,1), (0,0,0,1,1,0), (0,0,0,2,0,1), (0,0,1,1,1,0), (0,1,0,1,1,0), (1,0,0,1,1,0), (1,1,1,0,0,0) |

The complete trace splitting checks20949 candidate extensions and retains1125 labelled seven-point profiles after all strict projections. Of these,1124 have strict pure-quota bounds, with maximum2843/2860. The sole remaining profile initially gives1002/1001. Its genuine bad-count vector is shared across several layouts; an exact repaired dual certificate gives

    U_average <= 904545552/910000091 < 1.

The different layouts have different conditional probability spaces. What is fixed is H and its actual bad-count vector. The strict weighted average of valid upper bounds implies that at least one layout's own upper bound is below1; that layout supplies a valid coloring. No assertion is made that the average is an upper bound on one common failure probability.

Sources are `SEVEN_SELECTED.json` and `SEVEN_SELECTED_JOINT.json`. All1124 pure rows and the one repaired dual have passed independent exact replay, in `SEVEN_SELECTED_STRICT_VERIFIED.json` and `SEVEN_SELECTED_JOINT_VERIFIED.json`.

This exhausts the possibilities for the actual minimizing S, and proves the stated 23-vertex branch as a paper candidate.

## 6. Validation and remaining formal work

The independent checker recomputes labelled-injection A,B,C rows, genuine avoided-lock quotas, complete bad-slot capacities, pair weights, nonnegative dual multipliers, the sum-one layout weights, and exact capacity-repair penalties. It reads actual saved type counts and degree vectors; it does not accept solver success as a certificate. In total,2668 pure certificates and176 joint certificates in this directory have passed exact replay. The lower-dimensional strong-codegree49-record package is separately frozen.

For Lean, the needed new ingredients are the finite weighted-six-set minimum and exchange lemma (3), the W=6 two-K7 reduction, the complete local trace classifications and split coverage, the exact probability witnesses, and the actual-H caller assembling these cases. The arithmetic evidence does not by itself constitute this future formalization.
