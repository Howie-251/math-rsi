# 35 vertices, minimum degree nine: a complete candidate

Let H be the same simple six-uniform pair-covering hypergraph, with v=35, M=66, degree sum396 and actual minimum degree9. The existing adaptive certificate closes the case where a minimum-degree vertex x has a unit-codegree neighbor of degree at most11. Thus fix x of degree9 and assume every member of A={z:lambda(x,z)=1} has degree at least12. Put u=|A|. The x row gives u≥23, while the total excess above degree9 is81, so3u≤81 and u≤27.

## Lemma: a low nonunit partner of codegree two exists

There are n=34−u nonunit partners of x. Their total sum of lambda(x,z)−1 is11. Let l be the number with lambda exactly two. The other n−l partners each contribute at least two, so11≥l+2(n−l), or l≥57−2u.

If all these l partners had degree at least11, their degree excess above9, together with A, would be at least

    3u+2l ≥114−u ≥87 >81,

contradiction. Hence an actual y outside A∪{x} has degree e∈{9,10} and lambda(x,y)=2.

## Lemma: an actual low common unit neighbor exists

The number of nonunit partners of y is at most5e−34. One of them is x, which does not belong to A. Thus the common unit pool C=A∩{z:lambda(y,z)=1} has size

    |C|≥u−(5e−35)=u+35−5e.

All A vertices have degree at least12. After charging3u excess units to A and e−9 units to y, the remaining degree excess is at most81−3u−(e−9). Therefore C contains z of degree at most

    12+floor((81−3u−(e−9))/(u+35−5e)).

If e=9, u≥23 makes the numerator at most12 and denominator at least13; hence d(z)=12. If e=10, numerator at most11 and denominator at least8, so d(z)≤13 (and at least12). The denominator is positive in both cases. The three selected vertices are distinct; their codegrees are lambda(z,x)=lambda(z,y)=1, lambda(x,y)=2.

## Complete actual traces and arithmetic

Label z as0, x as1, y as2. The only degree triples are (12,9,9), (12,9,10), (13,9,10). Let tau∈{0,1} be the actual triple intersection multiplicity. Their complete trace counts are

    ell_7=tau, ell_3=ell_5=1−tau, ell_6=2−tau,
    ell_1=d(z)−2+tau, ell_2=6+tau, ell_4=e−3+tau,
    ell_0=66−sum_{T≠0}ell_T.

All six complete local types have a strict conditional failure bound using the proven component quota separately for each avoided pool, taking the maximum valid deduction against the same actual bad-pair vector. The submitted exact values and layouts are in LOW_PAIR_CENTER35.json, produced by low_pair_center35.py using component_kernel.py. The largest submitted value is14882237/14887440<1. Together with the imported adaptive cases e≤11 this covers the entire v35, minimum-degree9 branch.

Status: primary-agent paper derivation and exact arithmetic; independent replay and cross-family review pending. This is one internal branch, not the whole m(6)≥67 theorem.
