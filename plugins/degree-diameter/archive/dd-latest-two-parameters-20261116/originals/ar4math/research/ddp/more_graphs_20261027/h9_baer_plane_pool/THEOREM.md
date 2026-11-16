# Baer subplane neighbors: a new core-cover mechanism

Let K be the existing partial-fold core with its point map pi, and retain the established classical H(9) embedding and polar-distance lemma from `research/ddp/global_coverage_20261027/h9_quadric_line_rule/REPORT.md`. This note changes the set of proposed pins, not the old source graph or the accepted projection lemma.

## Uniform coverage

Choose a totally singular projective plane Pi=PG(W), dim_F9(W)=3, and an F9-basis w1,w2,w3. Let

    B = { [a*w1+b*w2+c*w3] : (a,b,c) in F3^3 minus0 }.

There are13 projective points: F9-proportional vectors with F3 coordinates are already F3-proportional, because any nonzero coordinate determines the scalar. For any ambient singular point p, the restriction of the polar linear form x -> polar(p,x) to these three F3 coordinates is an F3-linear map F3^3 -> F9. Its codomain has dimension2 over F3. Therefore its kernel has a nonzero vector. The resulting x in B satisfies polar(p,x)=0 and is singular, since Pi is totally singular.

By the inherited polar-distance lemma, the H-incidence point distance from p to x is at most4. The established sigma point-line projection and partial-fold map pi turn that path into an old-core graph walk of length at most4. Thus

    R4_K(pi(B)) = V(K).

A new vertex joined to every distinct pin in pi(B) is within5 steps of every old-core vertex. This argument uses a plane's13-point subgeometry, rather than all10 points of a line. It does not assert that degree budgets or coverage of previously appended extra vertices are automatic.

## Why folding can make13 raw pins affordable

For a plane defined overF3, take an F3-line L and an F3-center C outside L. A basis of L together with t*C, where t^2=-1 in F9, defines a Baer subplane. Under coordinate Frobenius, t maps to -t; on the13-point subplane this fixes the4 points of L and the center, and exchanges the remaining8 points in4 pairs. If these pairs are identified by the actual partial-fold map and not split, the13 raw points have9 distinct images. Each split pair increases that image count by1. The actual saved maps and degrees determine which instances are usable; no folding pattern is assumed as a substitute for checking them.

## Finite first search scope

Only the364 H(3)-coordinate centers y in Q(6,3) are selected. Their existing flat planes Pi_y are defined overF3. On a single plane, begin with PG2(F3) inside the91 points of PG2(F9) and take its projectivity orbit. A coordinate3-cycle, a unit shear, and a diagonal primitive-F9 multiplier generate PGL3(F9): conjugation supplies every field shear and the elementary matrices, with the diagonal supplying all determinants. The orbit has

    |PGL3(9)| / |PGL3(3)| = 42456960 / 5616 = 7560

Baer subplanes. Equivalently each subplane is determined by a projective frame, and the stabilizer of the prime-field subplane consists of projectivities represented overF3.

The total initial scope is364*7560=2751840 plane/subplane pairs. Candidate degree screening uses the actual current37631 and42397 sources. A91-bit mask makes full13-point allowed-degree testing cheap; only surviving masks need explicit folded-pin deduplication. This scope does not cover all66430 ambient flat planes.

## Predictions and acceptance

P1: at least one candidate in this finite scope has a degree-legal folded neighbor set of size at most the degree cap11 or12. P2: each actually generated Baer neighbor set covers the complete corresponding old core at radius4, as above. These are separate predictions; P1 may fail even though the conditional theorem is valid.

A complete new graph is accepted only after its full selected-neighbor R4 covers every vertex of the actual previous graph, including all existing extra vertices, and every old degree remains legal. No old edges are deleted. Existing source validation is inherited; no old all-source BFS is requested. A degree pool or this lemma alone is not a new graph or a finished Goal.
