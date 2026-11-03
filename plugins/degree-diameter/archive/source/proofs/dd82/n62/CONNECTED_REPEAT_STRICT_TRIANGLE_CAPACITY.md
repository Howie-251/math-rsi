# Strict capacity for nongenerated triangles and external centers

## Claim and assumptions

Use the actual connected-repeat order-62 setting and notation of
CONNECTED_REPEAT_TRIANGLE_WITNESS_REFINEMENT.md: there are d double
repeats, D is their 2d endpoints, U is the union of all unit repeat
triangles, and C1 is the set of type-one centers. Write
|U|=3d+v_extra and c_out=|C1\U|. Then

    17d + 3v_extra + 3c_out < 186.

In particular, at d=9,

    v_extra + c_out <= 10.

This eliminates the formerly considered boundary v_extra=11 entirely.
It does not exclude d=9 or assert that a type-zero triangle exists.

## Proof

Every heavy endpoint has one unit repeat neighbor outside D, U, and C1,
by the imported D1 light-mate and type-one center results. Put
R=V\(D union U union C1). These sets give

    |R| = 62 - 5d - v_extra - c_out.

Let ell(w) count heavy repeat neighbors of w. All heavy unit incidences
terminate in R, so

    sum_(w in R) ell(w) = 2d,    0 <= ell(w) <= 3.

If 2d=3|R|, every vertex of R would have ell(w)=3. In that event
Z=D union R is closed in the positive repeat support: a heavy vertex
has only its heavy mate in D and its unit mate in R; a vertex of R has
all three repeat neighbors in D. The set Z is nonempty, since d>=1,
and proper, since the 3d vertices of generated triangles are in U and
outside Z. This contradicts connectedness. Hence 2d<3|R|, giving the
claimed strict inequality. Equivalently, equality is ruled out by
CONNECTED_REPEAT_HEAVY_PORT_CLOSURE.md, which proves 3L3<2d.

For d=9, substituting gives 153+3(v_extra+c_out)<186. Integrality yields
v_extra+c_out<=10.

## Exact scope and remaining boundary

For the possible d values 1,3,5,7,9, the corresponding upper bounds on
v_extra+c_out are 56,44,33,22,10. These are capacity bounds, not claims
that every numerical boundary is attainable; overlap-cluster
restrictions may reduce them further.

The old implication "d=9 and v_extra=11 implies some type-zero
triangle" remains logically correct, but its antecedent is now
excluded by the strict capacity bound. It should not be used to infer
a type-zero triangle for an arbitrary d=9 candidate.

If d=9 and v_extra=10, then c_out=0. Since nongenerated triangle
clusters are isolated triangles and diamonds, 3s+4k=10 forces s=2,
k=1. There are four nongenerated unit triangles, comprising two
isolated triangles and one diamond. No contradiction to this remaining
boundary is claimed.

This is a paper consequence of the previously established actual-graph
reductions and is not yet a Lean theorem. Review pending.

