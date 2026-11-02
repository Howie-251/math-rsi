# Quadric-line transversals give a uniform old-to-new D5 guarantee in H9

The key geometric claim is proved for the actual classical coordinate model: for singular points p,x of H(q),

    incidence_distance_H(p,x)<=4  iff  B(p,x)=0.

Consequently every complete projective singular line of the ambient Q(6,9), whether or not it is an H9 incidence line, gives an old-to-new distance-at-most5 certificate after the partial fold. This explains the actual675 recovered source vertices at the uniform geometric level. It does not yet prove that an arbitrary family of these new vertices has all new-new distances at most5.

This report contains a paper derivation only. It does not construct H9 incidence, regenerate coordinates, run BFS, search new candidates, or recheck the675 signatures. Those signatures are evidence from the assigned source agent and are attributed below. The source's existing P3 test already certifies the actual986-point sequence; its success is distinct from a universal theorem for arbitrary new quadric lines.

## Actual coordinates and the required polar condition

Write a vector of F_q^7 as x=(u,s,v), with u=(x0,x1,x2), s=x3, v=(x4,x5,x6). The local primary source and verify_witness.py use

    Q(x)=u dot v-s^2,
    B(x,y)=Q(x+y)-Q(x)-Q(y)
          =u dot b+v dot a-2*s*t,  for y=(a,t,b).

In coordinates, the polar row for fixed x and unknown y is

    [x4,x5,x6,-2*x3,x0,x1,x2].

For F9, characteristic3 gives -2=1, so its fourth entry is simply x3 in the actual field encoding. The source's six Pluecker equations are

    p12=p34, p54=p32, p20=p35,
    p65=p30, p01=p36, p46=p31,
    pij=x_i*y_j-x_j*y_i.

Equivalently, using the ordinary three-dimensional cross product,

    u cross a = s*b-t*v,
    v cross b = t*u-s*a.                       (E)

A line through singular x must additionally be wholly singular. For its second generator y, this includes B(x,y)=0. It is essential not to discard that polar equation merely because the six Pluecker equations were read from code.

For example, at x=e0, the six equations alone leave the4-dimensional space y1=y2=y3=0. It contains directions not perpendicular to x and is not a totally singular plane. The polar condition adds y4=0, leaving the correct3-dimensional flat plane. The analogous pure-v case behaves the same way. The local builder skips six-equation kernels whose dimension is not3; this report does not misidentify those skipped4-dimensional kernels as flat planes or execute the builder.

## Flatness proved from these equations, including the exceptional cases

For a nonzero singular x, define W_x by (E) and B(x,y)=0. We prove that W_x is a3-dimensional vector space containing x and wholly contained in Q=0. Its projectivization is the totally singular plane Pi_x.

**Case s!=0.** Since u dot v=s^2, both u and v are nonzero. The first equation gives

    b=(u cross a+t*v)/s.

Insert this in the second equation and use v cross (u cross a)=u*(v dot a)-a*(v dot u). It gives v dot a=s*t, hence t=(v dot a)/s. Thus a is arbitrary, and it determines t,b uniquely: dim W_x=3. Also u dot b=s*t, so B=0. Finally

    a dot b = t*(a dot v)/s = t^2,

because a dot (u cross a)=0. Therefore Q(y)=0 for every y in this space.

**Case s=0, u!=0, v=0.** The second equation forces t=0, the first gives a=alpha*u, and the polar equation gives u dot b=0. There is one free alpha and a2-dimensional choice of b, so dim W_x=3 and Q(y)=alpha*(u dot b)=0. The case u=0,v!=0 is dual: t=0, b=beta*v, v dot a=0, again a totally singular3-space.

**Case s=0, u!=0, v!=0.** Here u dot v=0. Choose a0,b0 with

    u cross a0=-v,    v cross b0=u.

They exist because the image of the cross-product map by a nonzero vector is its dot-perpendicular plane. Every solution of (E) has the form

    a=t*a0+alpha*u,   b=t*b0+beta*v.

The cross-product identities give v dot a0=0, u dot b0=0, and a0 dot b0=1. For the last identity, expand (u cross a0) cross b0 in two ways. Hence B(x,y)=0 automatically and a dot b=t^2. The parameters t,alpha,beta are independent, so dim W_x=3 and Q(y)=0.

These cases exhaust nonzero Q-singular x. They apply to the source's equations, including the pure-u and pure-v points. Every H-line through x is contained in Pi_x. Conversely, if y is in W_x but not on the vector span of x, then the projective line <x,y> is wholly singular (Qx=Qy=Bxy=0) and satisfies all six Pluecker equations, so it is an H-line by the coordinate definition. Therefore the H-lines through x are exactly all q+1 projective lines through x inside Pi_x. This is the required classical flatness, derived rather than assumed from memory.

## The polar distance criterion by shell and tangent counts

First prove inclusion. If H-incidence point distance is0 or2, perpendicularity follows from Q(p)=0 or from their common singular H-line. If the distance is4, write a path

    p, Hline1, y, Hline2, x.

Both p and x lie in the wholly singular plane Pi_y proved above, so B(p,x)=0. Thus every point at incidence distance at most4 from p lies in Q intersect p-perp.

The generalized hexagon has degree q+1 and girth12. Its point shells at distances0,2,4 from p have sizes

    1,  q(q+1),  q^3(q+1).

There are no collisions in the last shell: two distinct paths of length4 to the same point, or a return into an earlier point shell, would give a cycle shorter than12. Their sum is

    q^4+q^3+q^2+q+1.                           (1)

The tangent hyperplane section Q intersect p-perp is a cone with vertex p over a parabolic Q(4,q). A hyperbolic-pair decomposition gives this directly: p-perp has the form <p> plus a5-dimensional residual parabolic quadratic space. The base has

    |Q(4,q)|=(q+1)(q^2+1)=q^3+q^2+q+1

projective points. For completeness its vector form ab+cd-t^2 has q^4 zeros: if (a,c)!=0, each t leaves q choices of (b,d), giving (q^2-1)q^2; if (a,c)=0, t=0 and (b,d) have q^2 choices. Remove the zero vector and divide by q-1. Each base point contributes q nonvertex points of the cone, so the tangent section has

    1+q*|Q(4,q)|=q^4+q^3+q^2+q+1.             (2)

The inclusion and equal finite counts (1),(2) prove the claimed equivalence. At q=9 the shells are1+90+7290=7381, precisely the tangent-section size; the remaining59049 of66430 points have incidence distance6 and nonzero polar product.

This is the actual ambient polar geometry of the classical model. It does not say that every singular line of Q is an H incidence line; the six additional Pluecker equations select the latter.

## Uniform old-core to a new ambient singular line

Let L be any projective singular line of Q(6,q), with all q+1 of its points. For any singular point p, the linear functional x->B(p,x) on the2-dimensional vector space underlying L has a nonzero kernel vector. That vector is a singular point x of L, because all of L lies on Q. Hence B(p,x)=0 and the preceding theorem gives H-incidence distance(p,x)<=4.

Now use the actual sigma point-line bijection from the partial fold. An H-incidence path of length4

    p, M1, y, M2, x

becomes the G_sigma walk

    p, sigma^-1(M1), y, sigma^-1(M2), x.

**It has four graph steps, not two.** Shorter even paths are handled the same way. Apply the partial-fold map pi; it cannot increase the walk length. If a new vertex z_L has every point image pi(x), x in L, as a core neighbor, then

    d(pi(p),z_L)<=4+1=5

for every core vertex pi(p). Extra anchors and new-new edges are irrelevant to this guarantee and cannot spoil it. Maximum-degree budgets remain separate.

This works when L is not an H9 incidence line. That is the distinction which the earlier incidence-line interpretation missed. No complete single core star is required; the intersection with each tangent hyperplane supplies the relevant pin globally.

## Every non-H singular line has a unique flat-plane center

This direct corollary explains a geometric pencil parameter without a new search. Let x,z be two distinct points of a singular line L which is not an H-line. They satisfy B(x,z)=0, so their H-incidence distance is at most4. It is not2, because then their unique projective line would itself be an H-line. Therefore the distance is exactly4. Girth12 makes this path unique; let y be its middle point.

Then x,z lie in Pi_y, so all of L=<x,z> lies in Pi_y. The point y is not on L, since every projective line through y inside Pi_y is an H-line. Thus L is a transversal of the q+1 H-lines through y: it meets each once. If another center existed it would give another length4 H-incidence path between x and z, contradicting girth12. The center is unique.

For coordinates, solve the six Pluecker equations plus the polar row for unknown y against each of fixed x,z. Since the equations are alternating in x,y and B is symmetric, their common kernel is W_x intersect W_z and has vector dimension1 for a non-H singular L. The polar rows must be included, particularly in the pure-u/v cases above. This proves the dimension1 prediction for each chosen line; it does not claim that a source object's recovered line witness is unique after folding. Anchor membership in the center's phi-fiber is a separate empirical claim. The assigned coordinate agent has now confirmed all675 center kernels have dimension1, are singular, and give centers outside the chosen lines. Its further657-image10 anchor prediction was refuted:25 empty-anchor cases pass vacuously, while all632 cases with anchors fail containment in the center's phi-fiber. The first is subject41505, whose center folds to518 but has anchor12. Thus the source's extra anchors cannot be identified with this canonical center rule; this does not affect the old-new theorem, which needs none of them. These are attributed results from ../h9_quadric_center/RESULT.json, not additional computations by this report.

## Actual source evidence and the remaining new-new obligation

The source agent's h9_quadric_line_signature/RESULT.json reports675/675 selected source objects matched to ambient singular lines, with all mandatory folded line images contained in their actual core pins. All675 chosen lines fail the H9 Pluecker-line condition. It used the actual point-label order, calibrated by all66430 Frobenius images matching tau^2; it did not generate H9 incidence lines or run BFS. This report reuses that evidence rather than repeating it.

The matched line images have sizes10 for657 objects and7 for18; anchor counts0/1/2/3/4 are25/230/412/7/1. Multiple image sizes are consistent with folding; the proof only requires inclusion of every folded image. The source scan stopped at a matching witness for each object and did not prove uniqueness of that witness.

For example, source vertex41502 has the exact10-pin folded image of its chosen singular line and no anchors, while that line is not an H9 incidence line. The theorem above supplies a uniform <=5 route from every point of K to this vertex and likewise to all675 objects. It does not identify the remaining135 non-star tail points as quadric-line vertices.

For two new line vertices z_L,z_M, choose x in L and then y in M with B(x,y)=0. The proved point distance is at most4, so the resulting bound is only

    d(z_L,z_M)<=1+4+1=6.

No fifth step has been removed. Source P3 already proves the actual986-point insertion sequence succeeds; this does not prove arbitrary Q-line batches succeed, or that the675 chosen Q-lines work independently of helpers.

## A concrete, falsifiable new-new bridge condition

Here are sufficient geometric witnesses for a pair, with no new computation performed in this report:

1. **Shared folded pin.** If pi(L) intersects pi(M), the two new vertices share a core neighbor and have distance2.
2. **Short sigma-incidence bridge.** If some x in L and y in M satisfy H-incidence distance(x,sigma(y))<=3 (or the reverse oriented condition), Lemma3.1's odd-path conversion gives a core route from pi(x) to pi(y) of length at most3. The new pair then has distance at most1+3+1=5.

The second condition has an exact flat-plane interpretation:

    distance_H(x,sigma(y))<=3  iff  sigma(y) meets Pi_x.

The forward implication follows from an incidence path x--N--w--sigma(y), with w H-collinear to x; the reverse uses that intersection point and its H-line to x. An incidence1 route is included. This is stronger than merely B(x,y)=0, which gave a point-to-point four-step bound.

The proposed claim, now refuted by the existing P8 test below, was that every pair of the675 selected Q-line witnesses has either a shared folded pin or such an oriented short sigma bridge. If true, it gives an independent-batch D5 certificate for K plus those675 vertices (with their degree budgets already inherited from the source). If false, the first uncovered pair identifies the gap in that certificate: it may still have another core three-step route, a route using anchors, or a helper route, so failure does not refute the actual source graph. This proposal is now REFUTED_BY_EXISTING_P8_STRONGER_TEST. The P8 evidence is inherited below; no additional pair scan or incidence check is run by this report.

## Scope and terminal state

The obtained result is a uniform geometric old-new theorem, plus a unique-center corollary for non-H singular lines and an explicit new-new witness condition. The primary hypotheses are the actual classical Q embedding, the source sigma pairing and valid partial fold, and inclusion of all folded points of each chosen singular line as pins. It does not establish D5 for arbitrary collections of Q-lines, supply missing degree slots, or generate a record.

The paper round is complete. No new template, coordinate/line enumeration, H9-incidence reconstruction, candidate graph, local search, BFS, or solver was started by this report. Existing source P3 and the675 coordinate classification are attributed as prior/parallel evidence; they are not rerun here.

Sources: local primary H9 partial-fold paper Section2.1, Lemma3.1, Lemma4.1, Theorem5.1; its verify_witness.py coordinates at lines187-193, Pluecker rows228-242 and plane generation243-258. The original duality paper Section2.3 gives the same Q and six Pluecker equations. Existing675 witnesses are in ../h9_quadric_line_signature/RESULT.json and first41502.json. No unprovided secondary-source flatness assertion is used.


## P8 evidence update: the universal short-bridge proposal is refuted

Status of PAIR_PREDICTION.json: **REFUTED_BY_EXISTING_P8_STRONGER_TEST**. Reuse ../quadric_batch/raw_result.json; there is no additional pair scan, incidence check, or BFS in this update.

The existing P8 test checked all227475 unordered pairs among the675 selected attachment sets in the fixed41356-point core K, separately for mandatory folded Q-line images and for the actual core attachments including anchors:

| attachments used | set pairs with core distance>3 |
|---|---:|
| mandatory Q-line images | 15639 |
| actual core attachments A_i | 1752 |

A shared folded pin gives core set distance0. An oriented short sigma bridge as defined above gives core set distance at most3. Consequently the15639 mandatory set pairs at distance>3 violate a weaker necessary condition for that proposed witness; no incidence-level refinement can make the original universal bridge claim true. The further1752 failures with actual anchors show that those anchors do not make all675 points an independent batch certified through old K alone.

These numbers count pairs of attachment sets in the static core. They are not final-graph bad vertex pairs, not a new measured graph diameter, and not a failure of the actual source. Helpers, other new vertices and new-new edges can change those distances. The existing P3 certificate for the complete986-point source sequence remains successful. The uniform single-Q-line old-new theorem and its unique-center corollary are also unchanged.

This loop closes the universal static short-bridge hypothesis. The next authorized work stays on constructing single Q-line vertices with legal degree load in the fixed bounded source-derived pool; it does not pursue local repairs of these failed pairs. Source coordinates are being used for the one already assigned finite center-line variant pool, and root owns its coverage check. This report starts no larger candidate family, no new pair analysis, and no additional search.
