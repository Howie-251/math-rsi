# Redei15 plane blockers give uniform old-core R4 coverage

This is a conditional paper derivation for the new B15 neighbor rule. It inherits the already established H9 polar-distance and partial-fold projection lemmas; it does not regenerate geometry, candidate pools or graph distances.

## The set and its different coverage mechanism

In PG2(F9), with homogeneous coordinates [Z,X,Y], let f(x)=x^5 and let D be its secant slopes. Put

    B = {[1,x,f(x)] : x in F9} union {[0,1,m] : m in D}.

For nonzero x, f(x)=x on the four squares and f(x)=-x on the four nonsquares. Same-branch slopes are +1 or -1. Mixed-branch slopes have the form (1+t)/(1-t), with t a nonsquare. The four nonsquares give four distinct slopes different from +/-1. Thus |D|=6 and |B|=15, as also recorded by the existing tiny SHAPE.json probe.

Here is a direct blocking proof, with no new enumeration. Every vertical line meets a graph point. A finite-slope line Y=mX+b with m in D meets B at its direction point. If m is not in D, the map x -> f(x)-mx is injective: equality at two different x would make m a secant slope. It is consequently bijective on F9, so every intercept b meets a graph point. The line at infinity meets D. Hence B meets all projective lines.

The coverage complementarity is a graph/direction division: omitted graph intercepts at a secant slope are supplied by its direction point; a nonsecant slope needs no direction point because its intercept map is already bijective. This is different from Baer13's F3^3 -> F9 kernel argument. Both mechanisms subsequently feed the same polar-distance lemma.

B is minimal blocking. Every affine graph point has its vertical line as a tangent, since the vertical direction [0,0,1] is absent. For each m in D, the map f(x)-mx has a collision and therefore misses an intercept b; Y=mX+b is tangent precisely at [0,1,m]. Thus no point of B can be removed while preserving blocking in the plane. This is minimality among raw blocking subsets, not a claim that every pin is needed for every particular folded graph.

## Conditional uniform-core theorem

Assume the following inherited interface.

1. The ambient singular points are the actual classical H(9) points, with polar form beta, and beta(p,x)=0 implies H-incidence point distance at most4.
2. The established sigma point-line conversion followed by the saved partial-fold map pi sends these even H-incidence walks to core walks of no greater length. Every core vertex has a raw point preimage.
3. Pi is any totally singular projective plane of Q(6,9), and B is embedded in Pi by an F9-projectivity. Every distinct image in P=pi(B) is retained as a mandatory neighbor of the proposed new point.

For a core vertex u=pi(p), restrict the linear functional x -> beta(p,x) to the three-dimensional vector space of Pi. Its projective zero set is a line, or the whole plane when the restriction is zero. Because B blocks every line, it contains some x with beta(p,x)=0. The inherited distance lemma and projection give

    d_K(u,pi(x)) <= 4.

Therefore R4_K(P)=V(K). Joining a distinct new vertex z to all mandatory pins P places every core vertex within5 of z. The four-step route is four graph steps; it is not shortened to two by the point-line conversion.

Nothing in this proof requires a G2 flat plane: total singularity and the inherited distance/projection interface suffice. It also does not require the special Baer13 structure, a complete Q-line, or a complete core star. This note inherits rather than reproves the actual coordinate interface in the earlier quadric-line and Baer reports.

If the current graph G contains K unchanged, its core vertices retain this coverage. Existing extras/copies outside pi's image still require full actual R4 coverage by the chosen mandatory pins plus anchors. For a complete single-vertex extension, check R4_G(P union anchors)=V(G) and actual degree legality; then the accepted single-extension induction applies. An arbitrary simultaneous batch does not receive an automatic new-new distance5 guarantee from this theorem.

## Frobenius folding and exact pin budgets

The polynomial and the chosen F3-projectivities commute with tau:x->x^3. With an F3 basis for an F3-defined ambient plane, the embedded B is tau-stable. Its graph has exactly three fixed points (x in F3), and its six direction points have exactly two fixed points (slopes +/-1). Thus B consists of five fixed singleton points and five nonfixed tau-pairs.

The existing PAIRING.json establishes that actual nontrivial pi-fibers are exactly unsplit tau-pairs; other fibers are singletons. If s of B's five pairs are split by the current saved map, then

    |pi(B)| = 5 + (5-s) + 2s = 10+s.

The mandatory images must be distinct when used as graph neighbors. For one appended point:

| degree cap | allowed split pairs s | mandatory pins | maximum additional distinct anchors |
|---|---:|---:|---:|
| 11 | 0 | 10 | 1 |
| 11 | 1 | 11 | 0 |
| 12 | 0 | 10 | 2 |
| 12 | 1 | 11 | 1 |
| 12 | 2 | 12 | 0 |

Larger s is unaffordable at these caps. Every mandatory pin and anchor must also have a free old degree slot. The formula is about actual saved pi, not merely the abstract Frobenius orbit count. It does not predict which candidates pass current degree/extras screening.

## Why the closed line/Baer pools do not already contain this rule

Raw B lies in the union of three projective lines: Y=X, Y=-X and Z=0. Each has six B points, so B contains no full F9 line. Any Baer PG2(F3) has at most four points on an ambient line: restricting its coordinates gives a nonzero F3-linear map F3^3 -> F9, with kernel of F3-dimension at most2. Three ambient lines can consequently contain at most12 of its13 points. B contains no Baer13 set.

There is also an exact folded-subset statement, so raw distinction is not lost after pi. Since B is tau-stable and every pi-fiber is a singleton or a tau-pair,

    pi^(-1)(pi(B)) = B.

Suppose an old complete Q-line or Baer13 set T had pi(T) contained in pi(B). Then every raw point of T would lie in B. A line or Baer subplane has a projective span inside Pi in that case, so it is a proper blocking subset of B in this same plane; this contradicts minimality. Equivalently the preceding three-line argument rules it out directly. Thus no old complete line/Baer mandatory image is hidden as a subset of the new mandatory image, including when some pairs are split.

This subset statement concerns the saved point-to-core pi and the mandatory pinset alone. Adding unrelated anchors can change subset containment, and a different graph rule could share the same R4 coverage without containing either raw object. It does not prove the existence of a degree-legal or complete new graph.

## Prediction disposition and scope

The root's existing SHAPE.json supports its exact15-point/6-direction, blocking/minimality, five-fixed-point and no-line/no-Baer predictions. Those tiny probe results are inherited, not rerun here. The uniform-core prediction is established conditionally by the proof above: every correctly embedded full folded B has R4 coverage of the corresponding bare core. A future core miss would therefore expose a violated embedding/map/full-pin premise; an extra-vertex miss does not refute this core theorem.

This round performs no new field probe, plane/projectivity enumeration, pin pool, candidate construction, BFS, solver or Lean work. It leaves actual degree screening and current-graph extras completion to the already assigned producer. No new graph or lower bound is claimed here.

Evidence: ../PREDICTION.json; ../SHAPE.json; ../../h9_baer_plane_pool/THEOREM.md; ../../h9_baer_galois_plane_filter/PAIRING.json; ../../../global_coverage_20261027/h9_quadric_line_rule/REPORT.md.
