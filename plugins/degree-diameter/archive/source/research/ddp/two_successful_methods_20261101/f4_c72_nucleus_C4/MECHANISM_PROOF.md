# Semilinear conic charts with an internal nucleus C4

This is a conditional mechanism theorem, not a constructed4608-vertex graph.
The four distance cases below are valid with true semilinear inverse darts and
projective port compatibility. No load-bearing gap was found in that rule.
The distance-three condition is stronger than originally needed for a one-way
certificate: in this homogeneous rule it is necessary as well as sufficient,
regardless of how many three-cross words join a controller pair.

## 1. Exact hypotheses and graph

Let K=F4=F2[w]/(w²+w+1), so w²=w+1 and w³=1. Addition is characteristic two;
integer codes0,1,2,3 mean0,1,w,w², not ZMod4. Write F_s(c)=c^(2^s), s∈{0,1}.
Coordinatewise F_s is additive, bijective, and its own inverse.

In K³ put

    L_∞=(0,0,1), L_t=(1,t,t²) for t∈K, N=(0,1,0).

A “conic direction” means the one-dimensional K-space [L_p]. Let C be a simple
undirected5-regular controller. Its five neighbors at each vertex have distinct
local port labels p∈{∞}∪K. For a dart e:u→v, let p(e) be its port at u and r(e)
its reverse port at v. Reverse ports can depend on the actual edge; no fixed
inverse-port permutation is assumed.

For each dart choose an invertible F_s-semilinear additive map T_e:K³→K³:

    T_e(c x)=F_s(c) T_e(x),     T_e(x+y)=T_e(x)+T_e(y).

Assume:

1. T_bar(e)=T_e^(-1) exactly as functions, not merely projectively.
2. T_e permutes the five conic directions; call the permutation π_e.
3. T_e(L_p(e))=β_e L_r(e) for some β_e≠0. β_e is arbitrary; β_e=1 is NOT used.
4. T_e(N)=α_e N, α_e≠0, and every directed dart satisfies

       {1,w} ∪ {α_e, α_e F_s(w)} = K* .                 (E)

Define the fiber graph on V(C)×K³. Internal edges add N or wN in one fiber.
Cross edges for e:u→v are

       (u,x) ~ (v,T_e(x)+t L_r(e)),       t∈K.

There are no additional constant edge offsets. This homogeneity matters for
the necessity statement in Section7.

These edges are undirected: T_e^(-1)(t L_r(e))=F_s(t/β_e)L_p(e), so the reverse
dart's free noise cancels it. No scalar is silently dropped. Each cross dart
has4 distinct endpoints in a different controller fiber; the5 neighbor fibers
are distinct. The two internal generators are different nonzero involutions.
Thus the graph is simple and22-regular. Internal components are C4: they are
cosets of K N, generated additively by N,wN, with w²N=N+wN in two internal steps.
For |C|=72 its order is4608, cross-edge count180×256=46080, internal-edge
count4608, total50688.

## 2. Conic and nucleus facts

Two different conic directions span a2-space S which does not contain N.
For finite a≠b, if λL_a+μL_b=N, the first coordinate gives λ=μ, and the third
then gives λ(a+b)²=0, hence λ=μ=0, contradicting the middle coordinate1.
For L_∞ and a finite L_a, the first coordinate immediately makes the finite
coefficient zero and the middle coordinate cannot equal1. Scalar multiples
of N are excluded for the same reason.

Any three different conic directions are independent. For three finite
parameters the determinant is, up to the irrelevant sign,
(a+b)(a+c)(b+c)≠0. With L_∞ and two finite parameters the determinant is a+b≠0.

The planes Q_p=span_K(N,L_p) are therefore five different planes through [N].
There are exactly |P¹(K)|=5 planes through any fixed line in K³; consequently
these are the entire pencil and their union is K³. Each has16 points and their
common intersection is the4-point line K N, giving4+5(16−4)=64 points.

For a fixed conic direction L_r, the four secant planes span(L_r,L_q), q≠r,
and the tangent plane span(L_r,N) are the five different planes through L_r.
Their union is K³. The four secants alone have52 points; the tangent supplies
the remaining12. This uses projective directions, so nonzero rescaling of any
L does not change any conclusion.

## 3. Forward/reverse nucleus coefficients

If T=A F_s and T(N)=αN, then

    T^(-1)=F_s(A^(-1)) F_s,
    α_reverse=F_s(α^(-1)).

For the prescribed smaller-controller-label→larger-label darts, take α=w when
s=0 and α=w² when s=1. Their exact reverses have respectively α_reverse=w²
and w². All directed cases satisfy(E):

| s | α | α F_s(w) | α_reverse |
|---|---|----------|-----------|
|0|w|w²|w²|
|0|w²|1|w|
|1|w²|w|w²|

Adding the coefficient0, corresponding to no internal step, therefore gives
all of K. The exponent is F_s(w)=w^(2^s), not w^s.

The normalized conic-matrix construction is compatible with this calculation.
For h=[[a,b],[c,d]], δ=ad+bc≠0, in the coordinates used here,

    M(h) = [[a²,0,b²], [ac,δ,bd], [c²,0,d²]].

It maps N to δN, has determinant δ³, and sends the conic to itself. Hence
A=(α/δ)M(h) gives T=A F_s with the required nucleus coefficient. Changing h
by a scalar changes both M and δ by that scalar squared, so A is well defined
on the projective h-class. The60 PGL2(4) classes, with the two Frobenius choices,
induce120 different permutations of the five conic directions: a nontrivial
Frobenius fixes∞,0,1 but swaps w,w² and cannot be a projectivity fixing all
three. Thus the induced permutations are all S5; each p→r constraint leaves24.
This counts normalized forward choices; reverse operators must be their actual
inverses, with the reverse coefficients in the table, not an independently
chosen forward-normalized matrix.

The theorem itself only needs hypotheses1–4 and does not depend on that domain
enumeration or on any particular controller search.

## 4. Controller distance0: all tangent planes in≤3 steps

Fix a source(u,x) and its dart e at port p. A cross followed by its reverse
has endpoint

    T_e^(-1)(T_e x+tL_r)+zL_p
      = x + (F_s(t/β_e)+z)L_p.

Thus its endpoints are exactly x+K L_p. A single internal step N or wN before
or after this backtrack adds respectively N or wN while keeping the same
basepoint x. A single internal step cN, c∈{1,w}, between the two crosses adds

    T_e^(-1)(cN)=α_reverse F_s(c)N.

By(E) for the reverse dart, these routes give every coefficient in K N, so
within length≤3 they cover the whole affine tangent plane x+Q_p. All five
ports' tangent planes cover x+K³. Every route here has basepoint exactly x;
no unrelated affine origins are being combined.

## 5. Controller distance1: four secants plus the tangent in≤3

For e:u→v write b=T_e x and r=r(e). The direct edge covers b+K L_r. Append
at v a backtrack f followed by its true inverse, where f's source port q≠r.
The resulting three-cross endpoints are

    b + t L_r + T_f^(-1)(s L_reverse(f)) + z L_q,

so exactly b+span(L_r,L_q). The β_f factors merely reparameterize the free
coefficient of L_q. All four q≠r produce the four secants through L_r.
Their common affine origin is b, since T_f^(-1)T_f is the identity on the
ENTIRE direct endpoint, including its first noise.

The missing tangent b+span(L_r,N) is covered by a direct edge followed by
at most two internal moves: the possible added nucleus coefficients are
0,1,w,1+w=w². By the pencil fact these routes cover the whole target fiber.
This case does not require(E), beyond the assumptions used elsewhere.

## 6. Controller distance2: four cosets of a secant plane in≤3

Take a shortest controller path u→v→z with darts e,f. Let r be e's incoming
port at v, p=f's outgoing port at v, q=f's reverse port at z. Then r≠p.
Two-cross endpoints have the fixed basepoint b=T_f T_e x and free noise span

    S=span(T_f L_r,L_q).

Because T_f L_p is proportional to L_q and its conic permutation is injective,
T_f L_r and L_q are two DIFFERENT conic directions. Thus dim_K S=2 and N∉S.
The first noise coefficient is transformed by F_s, which is a bijection of K;
its parameter remains independent of the second noise.

With exactly one extra internal move, putting cN at the middle fiber adds
α_f F_s(c)N, while putting it at the target adds cN, c∈{1,w}. Together with no
internal move, (E) supplies all four coefficients of K N. Therefore the endpoint
sets are precisely the four cosets b+S+aN, a∈K, covering the whole target fiber.
All these routes use≤3 edges and the SAME b=T_f T_e x. Internal moves at the
source are unnecessary for this argument.

## 7. Controller distance3: exact rank criterion, both directions

For a three-cross word e1,e2,e3 write r1 for the incoming port after e1, p2 for
e2's source port, r2 for e2's target port, p3 for e3's source port and r3 for
e3's target port. A shortest length-three word is nonbacktracking, so
r1≠p2 and r2≠p3. Write s2,s3 for the latter two semilinear exponents. Its
endpoint from x is

    T3 T2 T1 x
    + F_(s2+s3 mod2)(t1) a + F_s3(t2) b + t3 c,
    a=T3 T2 L_r1, b=T3 L_r2, c=L_r3.

All three coefficients range independently over K. This formula includes the
suffix Frobenius actions; treating T2/T3 as K-linear without reparameterizing
would be incorrect. Their projective conic directions satisfy [a]≠[b] and
[b]≠[c] by the two nonbacktracking conditions and port compatibility.
Consequently they have rank3 exactly when [a]≠[c]. Applying T3^(-1) gives the
pure middle-permutation criterion

    GOOD(e1,e2,e3)  iff  π_e2(r1) ≠ p3.

The reversed word has criterion π_e2^(-1)(p3)≠r1, equivalent to the same
condition, so the GOOD test is independent of which orientation is chosen for
an unordered controller pair. No equality T_e L_p=L_r, as opposed to nonzero
proportionality, is used.
When good, the endpoint image is T3T2T1 x+K³, so one such word covers every
source x and target fiber coordinate, regardless of its basepoint.

Necessity is stronger than a bound on the number of bad words. When a word is
bad, [a]=[c] and [b] is different, so its noise image is a conic SECANT plane,
which excludes every nonzero nucleus vector. From source x=0 its basepoint
T3T2T1(0) is exactly0. If EVERY three-cross word for a controller-distance3
pair is bad, NONE reaches target coordinate N (or wN or w²N). Any graph walk
of length≤3 projecting between that pair must have exactly3 cross steps;
there is no time for an internal move. Hence the fiber graph cannot have D≤3.
This argument does not require at most4 words. Even the union of all10 conic
secant planes omits the3 nonzero nucleus vectors (the small check finds size61).
The absence of extra edge offsets is essential to this common-zero argument.

## 8. Conditional theorem and scope

Under hypotheses1–4 the fiber graph has diameter≤3 if and only if:

- the controller has diameter≤3; and
- every controller-distance3 pair has at least one GOOD three-cross word.

Sufficiency follows from Sections4–7; necessity of the controller diameter
follows by projection and necessity of GOOD from the x=0 argument above.
For any72-controller instance meeting these conditions the graph is simple,
22-regular, has4608 vertices and50688 edges, and has diameter exactly3, since
4608>1+22+22·21=485, the simple-undirected degree22 diameter-two bound.

The new internal C4 edges are part of the hypotheses. Therefore a controller
bound proved for the old degree20 cross-only rule, including any old≤68 bound,
does not rule out this new rule. In particular, Section4 uses no controller
triangles and does repair that self-layer coverage obstruction conditionally.
It does NOT prove that a72-controller assignment with GOOD words exists.

Producer-owned Exoo72/Michel72 domain/route/empty-edge artifacts are separate
from this proof. They may close their specific chart-assignment domains without
invalidating the conditional theorem or excluding every72-controller. No new
fiber graph, all-root/source BFS, solver, Lean theorem or public-novelty result
is asserted here. Known-controller feasibility and public comparisons remain
root/producer-owned.

## 9. Proof-only finite corroboration

MECHANISM_CHECK.py is independent of controller/producer inputs. It checks the
10 conic pairs,10 distinct triples, tangent pencils and adjacent secant union,
all3 directed coefficient cases,30 two-cross shifted-plane cases, and all80
nonbacktracking conic triples. Every asserted mask identity passed. Its result
is MECHANISM_CHECK_RESULT.json, measured CPU0.032770784<30, one process. It
constructs only K³ vector-space masks, no controller or fiber graph, and runs
zero BFS/solver/Lean/install/hash operations. The algebraic proof above supplies
the quantifiers and common-basepoint interpretation rather than treating these
small checks as a constructed graph or a novelty certificate.

The separate GENERAL_QUOTIENT_INTERFACE.md states the non-conic sufficient
interfaces and the unique-controller-word Hall obstruction, with its own scope.
It does not extend the all-bad-conic/nucleus necessity to general matrices.
