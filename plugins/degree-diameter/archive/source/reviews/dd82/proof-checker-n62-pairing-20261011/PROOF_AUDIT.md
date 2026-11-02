# Order-62 triangle pairing: independent bounded proof audit

Verdict: **PASS — all audited mathematical obligations are discharged.**
This fresh Codex review is **same-family / provisional**. The requested reviewer
configuration was `gpt-6-astra` with `ultra` reasoning; the actual backend model
and reasoning level are not independently attested in this reviewer session.
The verdict concerns the paper proof, not a Lean theorem or a cross-family
semantic acceptance.

## Inputs and bounded scope

The complete following proofs were read and audited:

- `proofs/dd82/n62/TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md`, lines 1–142.
- `proofs/dd82/n62/S_TOUCH_SATURATED_ROW_EXCLUSION.md`, lines 1–88.

`proofs/dd82/n62/RECOVERED_REDUCTION.md` was also read. Its original-graph
premises at lines 42–52 and the elementary parent/parity definitions at lines
197–235 were checked where needed. The triple-repeat finite enumeration,
seven-template classification as a whole, and historical solver statements
were not accepted as inputs to the triangle-pairing proof and were not audited
in this review. The new proof's final statement about five remaining templates
is explicitly conditional on that separate recovered reduction.

No source proof was edited. No solver, finite model agreement, prior review
verdict, formal compilation, or unsuccessful graph search supplies an argument
in this audit. Only Markdown and JSON review artifacts were written, following
the task override of the skill's usual report and wiki workflow.

## Canonical conclusions

For every finite simple undirected graph G with 62 vertices, maximum degree at
most 8, and diameter at most 2, define A to be its actual adjacency matrix and
B=A²+A−7I−J. The finite set of actual triangles of G has a fixed-point-free
involution. Consequently its cardinality T is even.

There is no such G for which every entry of B is 0 or 1. This second conclusion
uses the simple-B assumption only in the final four-cycle count.

The proof does not establish nonexistence of every order-62 candidate, and it
does not use triple-repeat elimination to establish either conclusion above.

## Dependency audit and the main attack

The dependency graph is acyclic:

actual graph → regularity and exact B identities → one triangle per vertex →
local S_TOUCH contradiction without global B simplicity → mates avoid the
whole triangle neighborhood → distinct mates → indicator identities and
commutation → mate triangle → fixed-point-free involution → T even.

The additional simple-B premise gives the independent count T odd, which
contradicts this last conclusion. There is no use of T odd to prove pairing.

The existing S_TOUCH theorem is stated with globally simple B, but **its proof
does not use that hypothesis**. The new pairing proof explicitly claims this
strengthening by inspecting its derivation, and that inspection is correct.
The strengthening is fully discharged below; the audit does not merely apply
a theorem with an unmet hypothesis.

## Re-derivation of the S_TOUCH dependency without simple B

Use labels 0,1,2,3,w, where N(0)=X, the only induced edge in X is 12,
P(w)={1,3}, and every other vertex outside {0}∪X has exactly one parent in X.
Assume only the actual graph identities, nonnegative integral B with row sum
3, and at most one triangle through each vertex.

1. The triangle 012 forces B01=B02=B12=1. The two parents of w give B0w=1.
   Thus row 0 is exactly {1,2,w}, with unit entries.
2. The nonadjacent vertices 1 and 3 have exactly common neighbors 0,w.
   No common neighbor lies in X because its only induced edge is 12, and no
   other outside vertex has two parents. Thus B13=1, and row 1 is exactly
   {0,2,3}, with unit entries.
3. Row 2 already has B20=B21=1. Its remaining nonnegative integer weight is
   exactly 1, so it has one further unit neighbor b, without requiring a
   global entry bound. Every x∈X\{1,2} has exactly common neighbor 0 with 2,
   giving B2x=0. The zero diagonal and existing entries therefore place b
   outside the closed neighborhood of 0.
4. Since 2 already lies in 012, the incident-edge repeat sum is exactly 2.
   Hence A2b=0. If b=w, then (AB)1w≥B0w+B2w=2 but
   (BA)1w=A0w+A2w+A3w=1, impossible. Thus b is an ordinary singleton-parent
   vertex. From (AB)1b≥B2b=1 and (BA)1b=A2b+A3b=A3b, its parent is 3.
5. Now (AB)0b≥B2b=1 and (BA)0b=A1b+A2b+Awb=Awb imply Awb=1.
   The edges 3b,3w,wb give a triangle and hence B3b≥1. The same entry now has
   (AB)0b≥B2b+B3b≥2, while (BA)0b=Awb=1, a contradiction.

All inequalities use nonnegative entries. Every complete repeat row used here
was forced by unit lower bounds and row sum 3. Unknown entries elsewhere may
have weight 2 or 3; this does not change a step.

## Applying that local contradiction to an arbitrary triangle

For a triangle T0={r,a,b}, each vertex v has exactly two unit repeat entries
to its triangle partners. Nonnegative integrality and row sum 3 leave one
unique additional unit repeat neighbor f(v). The identity
sum_{x∼v}Bvx=2t(v)=2 excludes adjacency v∼f(v).

If w=f(r) were adjacent to a, the pair r,w would have precisely two common
neighbors, a and c. The second cannot be b: that would make wab a second
triangle through a and b. The only induced edge in N(r) is ab. The complete
repeat row at r is {a,b,w}, so every other vertex outside its closed
neighborhood has precisely one parent in N(r), while w has exactly parents
{a,c}. Relabeling (r,a,b,c) as (0,1,2,3) supplies every premise of the local
contradiction just proved. This is relabeling an arbitrary triangle, not an
assumption that an automorphism exists. Applying the same argument at all
three triangle vertices gives F∩(T0∪N(T0))=∅.

If f(r)=f(a)=w, then (AB)rw≥Ara·Baw=1, whereas the complete repeat row of r
gives (BA)rw=Aaw+Abw+Aww=0. Thus the three mates are distinct.

## Indicator identities, mate triangle, and involution

Symmetry of B and the three complete repeat rows give

    B 1_T0 = 2 1_T0 + 1_F.

The coefficient on F is exactly one because its three vertices are distinct.
Every vertex outside T0 has at most one neighbor in T0: two such neighbors
would make a second triangle through a vertex of T0. For C=N(T0)\T0,

    A 1_T0 = 2 1_T0 + 1_C.

The three sets T0,C,F are pairwise disjoint. Therefore AB=BA gives exactly

    B 1_C = 2 1_C − 2 1_F + A 1_F.

At each v∈F the left side is nonnegative and the right side is
−2+|N(v)∩F|. Simplicity of G and |F|=3 bound this neighbor count by two,
so it is exactly two. F is a triangle.

For u=f(v)∈F, the two triangle edges of F have unit B weight, and Buv=1 by
symmetry. These three entries exhaust row u. Its unique extra mate is
therefore v. The intrinsic mate construction returns T0 when applied to F,
and F≠T0. It is a fixed-point-free involution of the entire finite triangle
set. The empty triangle set is included and has even cardinality.

## Simple-B parity

If B is simple, its 62 rows of sum 3 give 93 unordered repeat edges. Exactly
3T of them are original edges: an original edge has positive B weight exactly
when it belongs to a triangle, and triangle edges have weight one. Adjacent
pairs have at most one common neighbor. Nonadjacent pairs have one common
neighbor when Bxy=0, and two when Bxy=1. Hence

    sum_{unordered {x,y}} choose(c(x,y),2) = 93−3T = 2C4.

Here C4 counts all four-cycles, not only induced four-cycles. Choosing a pair
of distinct common neighbors gives four distinct vertices and a four-cycle;
each such cycle has two opposite pairs. Thus the last equality is exact,
including graphs with extra edges on those vertices. It makes T odd,
contradicting the pairing theorem.

## Counterexample attempts

| Attack | Outcome and decisive reason |
|---|---|
| Permit repeat weights 2 or 3 elsewhere during S_TOUCH | No counterexample: only forced unit rows are used. |
| Let the second parent c be the third triangle vertex | Creates a second triangle at a and b, contrary to t≤1. |
| Give another outside vertex multiple root parents | Its root repeat entry would be positive, contradicting the saturated root row. |
| Identify two extra mates | Forces (AB)rw≥1 and (BA)rw=0. |
| Allow an outside vertex two neighbors in T0 | Creates a second triangle through triangle vertices. |
| Make F a path, an edge, or an independent set | A vertex of F has internal degree below 2 and hence a negative coordinate of B1_C. |
| Make the triangle map fixed, noninjective, or a longer cycle | Disjointness excludes fixed points; saturated mate rows force its square to be the identity. |
| Use the empty triangle set | Pairing still gives T=0 even; the simple-B count immediately contradicts it. |
| Apply the simple-B parity argument to weighted B | It would fail because weighted repeat edges contribute different four-cycle counts; the proof explicitly restricts this step to simple B. |

These are exact algebraic or graph-theoretic attacks; failure to find a model
was not used as evidence. No counterexample was found, and every candidate
above is excluded by a displayed argument.

## Findings and acceptance scope

No FATAL, CRITICAL, MAJOR, or MINOR issue was found. The referenced S_TOUCH
proof's stronger generality is justified by its complete derivation. No repair
or additional hypothesis is needed for the new theorem. The old dependency
document's global simplicity premise is stronger than necessary; its older
scope/status prose is historical and is not a premise of this audit.

All quantities and sums are finite. There are no asymptotic uniformity,
probability-mode, analytic interchange, or convergence obligations. The
formalization and cross-family acceptance remain separate work. This review
does not audit or certify the remaining double-repeat templates or a full
order-62 upper bound.
