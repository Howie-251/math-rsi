# Hexagon126 plus a matching: complete coverage model and route budget

Status: **VALID paper model review; no joint feasibility conclusion**. This analysis performed no source construction, distance computation, matching enumeration, solver call or BFS. Source facts and the producer's radius cache are inherited, not recomputed.

## Exact radius-two / radius-four encoding

Let G be the fixed cubic generalized-hexagon incidence graph, and let M be a legal complement perfect matching selected by the model. Write H=G union M. The same selector may represent seven concrete matching edges in a C7 orbit.

For an unordered vertex pair {p,q}, its actual H-distance is at most two exactly when either its G-distance is at most two, or at least one of the following matching literals is true:

    M(p,x) for x in the closed old ball B1_G(q),
    M(q,x) for x in the closed old ball B1_G(p).

The balls must be **closed**, including q or p, so this includes the direct matching edge M(p,q). If an implementation instead uses open neighbour sets, it must add the direct matching literal separately. A two-step path using two matching edges returns to its start, because M is a matching; it creates no omitted non-diagonal pair.

Thus a variable Y2(p,q) may safely use only the implication

    Y2(p,q) => OR(the displayed matching support),

when the old distance is greater than two; old distance at most two is the constant True. Empty support forces Y2 false. These are sound positive reachability witnesses. They are existentially complete because any valid chosen matching permits assigning every Y2 its actual radius-two truth value. Reverse implications are not needed for the existential diameter model.

For an old far pair, impose

    OR over all w of [Y2(p,w) AND Y2(w,q)].

An auxiliary z for a conjunct needs only z=>Y2(p,w) and z=>Y2(w,q), together with the displayed OR over z. A selected witness gives an actual walk of length at most four. Conversely every actual path of length at most four can be split into two pieces of length at most two, so assigning actual reachability gives a satisfying extension. Include diagonal pairs as constant True, or handle their simplifications equivalently. All old pairs at distance at most four remain covered because no old edges are deleted.

Canonical unordered Y2 variables under the verified C7 action are sound: the selected matching and G are invariant under that action, so actual reachability is invariant as well. Memoizing a z by its two canonical input literals is also sound. Concrete matching edges in a two-edge route may have the **same selector alias**; they must not be required to use distinct model variables. The Y2 split automatically includes these routes and all routes using one or two new matching edges.

There are C(126,2)/7=1125 unordered pair orbits. No nontrivial element of odd-order C7 can fix a two-element set. Each root has 48+32=80 old far targets, giving 126*80/(2*7)=720 far pair orbits. Therefore the proposed 720 final coverage conditions, with Y2 available on all pair orbits, are complete for diameter at most four in this matching family. This is not a claim that they are jointly satisfiable.

## Perfect matching and mixed old bipartition

A degree-three root in a maximum-degree-four graph has radius-four ball at most

    1+3*(1+3+9+27)=121 < 126.

Every successful candidate must consequently be four-regular, so all 126 old vertices must receive a new edge: the added matching is perfect. Each old part has 63 vertices. If there are a point-point edges, b line-line edges and c cross edges in M, then 2a+c=2b+c=63. Hence a=b and c is odd. An all-cross matching preserves bipartiteness and cannot work: a root can reach at most 4+4*3^2=40 of the 63 opposite-part vertices in odd lengths at most three. This is the standard bipartite Moore obstruction, not a new general theorem.

For C7-invariant perfect matchings, the 18 length-seven orbits must be paired with distinct orbits; an invariant involution cannot match within an odd seven-cycle. The orbit base has nine point and nine line vertices. Its cross-pair count is odd. The all-nine-cross case is excluded by the preceding bound; the mixed counts one, three, five and seven remain possible at this necessary stage.

## Exact girth-six restriction

Restrict every matching edge to old distance five or six. A cycle with one matching edge then has length at least six. A cycle with two matching edges has two nonempty old connectors. It has length below six exactly when the connector lengths are 1+1, 1+2 or 2+1. For each pair of concrete matching edges both endpoint pairings must be considered.

These connector tests do not falsely exclude a graph under the stated domain. For a 1+2 test, if the middle vertex of the two-step old connector were an endpoint of the one-step connector, one of the matching edges would itself be an old edge, contrary to old distance at least five. Thus the forbidden short closed walk is a genuine cycle. A cycle with three matching edges has length at least six, since matching edges cannot be consecutive. Old cycles already have girth twelve.

Accordingly the domain plus the binary incompatibilities is exactly the girth-at-least-six subfamily of the fixed matching model. If two incompatible concrete edges are represented by the same orbit selector, that selector is forbidden; if they have different selectors, use a negative binary clause. This restriction is not the family of all matchings. It protects B2_H(root)=1+4+12=17 but does not guarantee the third or fourth layer or full diameter four.

## Why two matching steps are mathematically essential

The old sphere sizes are 1,3,6,12,24,48,32. Thus the 46 vertices at old distance at most four need no repair; the old distance-five and distance-six layers contain 80 targets. The source is bipartite and has intersection array

    b0=3; b1=...=b5=2; c1=...=c5=1; c6=3.

This follows from cubic degree, girth twelve and diameter six; it does not require vertex transitivity. The old balls of radius at most three are trees. For Far(r)=S5_G(r) union S6_G(r), the needed ball intersections are:

| Old distance d_G(r,x) | Far targets in B1_G(x) | Far targets in B2_G(x) | Far targets in B3_G(x) |
| --- | ---: | ---: | ---: |
| 3 | 0 | not needed | not needed |
| 4 | 2 | 6 | not needed |
| 5 | 3 | 8 | 14 |
| 6 | 4 | 7 | 16 |

These values follow by expanding at most three steps using the displayed intersection array. For example a centre at distance five has, within its B3, six targets in S5(r) and eight in S6(r). For a centre at distance six, its own layers have old-root distances: layer0 contains one distance-six vertex; layer1 three distance-five vertices; layer2 three distance-four and three distance-six vertices; layer3 three distance-three and nine distance-five vertices. Hence its B2 has seven far targets and its B3 sixteen. The distance-five vertex after the first step has one remaining lower neighbour and one remaining distance-six neighbour; returning to the centre consumes only one of its two distance-six neighbours.

Let c=1 if the matching edge at r is cross-part (old distance five), and c=0 if same-part (old distance six). Let n1 be the number of old neighbours of r whose matching edges are same-part, and n2 the corresponding number among its six old distance-two vertices. Consider all paths of length at most four with exactly one matching edge:

* M first: its suffix lies in B3_G(Mr), adding at most 16-2c far targets.
* G-M followed by at most two old steps: for each of the three old neighbours, a same-part matching centre is at old distance five from r and contributes at most eight far targets; a cross-part centre is at distance four or six and contributes at most seven. The total is at most 21+n1.
* G-G-M followed by at most one old step: for each old S2 vertex, a same-part matching centre is at old distance four or six and contributes at most four; a cross-part centre is at distance three or five and contributes at most three. The total is at most 18+n2.
* G-G-G-M: its old prefix has twelve endpoints, hence contributes at most twelve far targets.

Overlaps can only decrease the resulting union. All one-matching routes together therefore cover at most

    67-2c+n1+n2

of the 80 old far targets. Since n1<=3 and n2<=6, this is at most 76 for a same-part root mate and at most 74 for a cross-part root mate. A successful graph would need at least four or six distinct far targets, respectively, with no one-matching witness and with a genuine two-matching route.

The complete reduced two-matching patterns are M-G-M, M-G-M-G, M-G-G-M and G-M-G-M, with raw endpoint bounds 3,9,6,9. This extra capacity is not uniformly insufficient: the bounds do **not** exclude the full model. They instead explain why a model checking only one new-edge route would reject the entire intended family incorrectly. The Y2/R4 construction above includes all four types.

An earlier unfinalized paper message incorrectly used four instead of sixteen for the first-M distance-six centre, producing a 64/74 bound. Its middle-M cross-part estimate also needs seven rather than six when the centre has old distance six. The corrected values above are 76/74; no 64-bound constraint was added to the exact model. The Y2/R4 completeness argument is independent of this counting estimate.

As an auxiliary inherited observation, an involutive source-automorphism matching is uniformly too weak: matching steps commute with old steps, so any radius-four endpoint lies in B4_G(r) union B3_G(rho(r)), of size at most 46+22=68. The proposed matching is not assumed to be a source automorphism. C7 invariance alone does not imply that its mate map is an automorphism.

## Source and execution scope

The producer now uses the primary LCF description directly, with shift+18 checked as an edge permutation. The earlier local-triad-to-LCF isomorphism attempt remains UNKNOWN; none of this proof requires an unproved vertex-number correspondence. The source has two point/line orbits rather than a presumed vertex-transitive action. All 18 C7 representative roots, or equivalently all 720 far unordered pair orbits, must be covered.

Inherited local evidence: `SOURCE_LCF_PRIMARY.json`, `AUTOMORPHISM.json`, `RADIUS_CACHE.json`, `OLD_FAR_PAIRS.json`, and the separately retained `BINDING_RESULT.json`. Primary source facts were supplied by the source scout from the author cage table and official Sage LCF recipe. This paper adds no numerical test, graph, SAT call or new experimental row. Any negative exact solve would apply only to the frozen C7/girth/domain model and according to its actual proof status; a positive assignment still requires complete graph decoding and actual diameter acceptance.
