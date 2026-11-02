# A saturated-row contradiction excludes S_TOUCH at order 62

## Theorem and status

No original degree-at-most-eight, diameter-at-most-two graph on 62 vertices
can realize the S_TOUCH template with simple repeat matrix B. This is a
paper proof from the actual adjacency matrix, with no SAT result or finite
enumeration needed inside this branch. Fresh proof-checker delta review passed eight obligations; Gemini B13 also accepted the full argument. Reviews are in reviews/dd82/proof-checker-s-touch-three-20261011/ and reviews/dd82/20261011_B13_s_touch_exclusion.json.
It excludes one of the seven recovered templates, not every order-62 graph.

## Original graph premises

The standard degree count makes G eight-regular. Set B=A²+A−7I−J.
Then B is symmetric, integral, nonnegative, has zero diagonal and row sum 3,
and AB=BA. For distinct vertices c(u,v)+Auv=1+Buv. The triangle identity
sum_{v~u} Buv=2t(u) implies t(u)≤1.

In S_TOUCH, B has only entries 0 and 1. The root 0 has neighborhood
X={1,...,8}; the only original edge inside X is 12. Thus 012 is a triangle.
The exceptional vertex w=9 lies outside the closed root neighborhood and
has parents {1,3}. Every other vertex y outside it has exactly one parent
i∈X; denote its class by Ci. The sizes of these classes are irrelevant.
These are precisely the S_TOUCH premises of RECOVERED_REDUCTION.md.

## Three fixed repeat rows

The triangle edges give B01=B02=B12=1. The exceptional parent set gives
B0w=1. Hence the repeat row of 0 is exactly {1,2,w}.

Vertices 1 and 3 are nonadjacent. Their common neighbors are exactly 0,w:
there is no common neighbor in X, and w is the only vertex outside X∪{0}
with two parents. Thus B13=1. The repeat row of 1 is exactly {0,2,3}.

Vertex 2 has repeat neighbors 0,1, and exactly one further vertex b.
Every x∈X\{1,2} has exactly one common neighbor with 2, namely 0.
Indeed X has only edge12 and no exceptional parent set contains 2.
These pairs are nonadjacent, so B2x=0. Therefore b lies in Y, outside
the closed root neighborhood. We have B2b=1.

Since 2 already lies on triangle012, its incident original edges already
contribute B20+B21=2=2t(2). Nonnegativity forces b not adjacent to 2.
In particular b is not in C2.

## Locate b using the first saturated row

First b cannot equal w. The (1,w) entry of AB has contributions
A10 B0w=1 and A12 B2w=1 if b=w. All other terms are nonnegative.
But the (1,w) entry of BA, using the complete repeat row of 1, is

    A0w + A2w + A3w = 0+0+1 = 1,

contradicting AB=BA. Thus b is an ordinary singleton-parent vertex.

Evaluate the (1,b) entry. The left side is at least A12 B2b=1.
The complete repeat row of 1 gives the right side

    A0b + A2b + A3b = A2b + A3b.

Since b has one parent and is not adjacent to 2, this forces b∈C3.

## The second saturated row gives the contradiction

Now the (0,b) entry of AB is at least A02 B2b=1. The complete repeat
row of 0 gives

    (BA)0b = A1b + A2b + Awb = Awb,

because b∈C3. Equality forces Awb=1.

We also have A3b=1 and A3w=1. Therefore w,3,b form a triangle, so
B3b=c(3,b)≥1. Returning to the same (0,b) entry, its left side is at least

    A02 B2b + A03 B3b ≥ 1+1 = 2,

whereas its right side is Awb=1. This contradiction proves the theorem.

## Scope and connection

The proof uses only exact graph identities and the displayed S_TOUCH parent
structure. It supersedes the need to solve the three canonical cases of
S_TOUCH_THREE_CASE_REDUCTION.md for this mathematical branch. Those fresh
30-second runs returned UNKNOWN and supply no proof evidence.

Together with the recovered seven-template coverage, the remaining order-62
templates are D0_MATCH, D0_EDGE_BIN, D0_EDGE_BOUT, D1_MATCH, D2_MATCH and
S_DISJOINT. They are not excluded here. The broader triple-repeat elimination
still has its own finite-check dependency. A Lean caller for this new branch
has not yet been implemented.
