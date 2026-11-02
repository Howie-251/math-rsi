# Derivation Package

## Target

Replace the fixed K4 edge multiplicities `(4,2,1)` by `(3,2,2)`, and derive the exact short-word capacities and voltage-lift distance score used in the new finite construction profile.

## Status

COHERENT AS STATED. Capacity is a necessary condition, not a diameter guarantee. The graph identities and four-root score are exact.

## Invariant Object

A simple 172-vertex graph with four 43-vertex cyclic orbits. The objective is its exact unordered count of vertex pairs farther than three steps.

## Assumptions

- Every voltage lies in F43, added along an oriented base edge and negated on reversal.
- The base endpoints 01 and 23 have multiplicity a=3; 02 and 13 have b=2; 03 and 12 have c=2.
- Parallel edges on one endpoint pair have distinct voltages; no base loop is allowed.
- Tree edges 01#0,02#0,03#0 are fixed at zero. No common scalar normalization is used.

## Notation

Vertices `(v,x)` have label `43*v+x`, v=0,1,2,3. Edge-array groups are 0..2=01, 3..5=23, 6..7=02, 8..9=13, 10..11=03, 12..13=12. Tree indices are 0,6,10; the other eleven coordinates are independent. A coefficient vector records signed uses of the fourteen oriented edge variables in a base walk.

## Derivation Strategy and Map

1. Enumerate all nonbacktracking base walks of lengths zero through three; these include representatives of every possible lifted distance at most three.
2. Deduplicate their field-linear voltage forms separately for each ordered pair of base endpoints.
3. Compare these exact finite counts with the analytic formulas and with tree-gauge projection.
4. Use four complete orbit-root BFS traversals for every actual candidate, independently of the capacity test.

## Main Derivation

### Exact form counts

For a root and target joined by the a-matching, the number of distinct forms is

`F_a = a + 2bc + a²(a−1)/2 + a*(3b²+3c²−2b−2c)`.

The first two terms count one-edge and two-edge routes. Three-edge routes staying on the same endpoint pair have forms `e_i−e_j+e_k`, with j different from i and k. When i=k they contribute a(a−1); when i and k differ their interchangeable order contributes `a*C(a−1,2)`. Their sum is `a²(a−1)/2`. Routes using an a edge and two b edges contribute `a*(2b(b−1)+b²)`, and the analogous c routes complete the formula. The supports of these classes distinguish the forms. Over F43 the small signed coefficients introduce no additional modular collision.

At the same base vertex, the distinct forms comprise the empty walk, all nontrivial two-edge parallel returns, and all directed triangle routes:

`F_diag = 1 + sum_m m(m−1) + 6abc`.

Substituting (3,2,2) gives diagonal 83, a-target 68, b-target 74 and c-target 74. The actual independent symbolic enumeration in `run.py` produces exactly

`[[83,68,74,74],[68,83,74,74],[74,74,83,68],[74,74,68,83]]`.

Each root has exactly 302 raw nonbacktracking words including the empty word. All coefficient-form sets were built directly, not inferred from the formula. `CAPACITY_CHECK.json` saves the raw counts, distinct counts and analytic values. Every target fiber needs 43 different voltages. The minimum capacity improves from 63 for the old (4,2,1) base to 68; same-orbit capacity rises from 63 to 83. This does not establish coverage for any field assignment.

### Exact tree normalization

Under the vertex relabel `(v,x)->(v,x+c_v)`, a voltage on u→v changes by `z'=z+c_v−c_u`. Setting c0=0 makes the three chosen tree voltages zero uniquely. Fourteen raw voltages therefore leave eleven free coordinates.

The symbolic counts are unchanged after dropping the three tree coordinates. Two forms with the same endpoints have coefficient difference of zero incidence boundary. If that difference is supported only on a tree, it is zero, since a tree has no nonzero circulation. The actual enumeration also checks this injectivity for all sixteen endpoint pairs.

### Exact graph and four-root score

Every base vertex has incident multiplicity 3+2+2=7. Distinct voltages within each parallel class prevent duplicate lifted edges, and different endpoint orbits prevent loops. Each legal state gives a simple graph with 172 vertices and 602 edges. Simultaneous translation of x by any element of F43 preserves all edges and is transitive in each orbit.

Four complete BFS traversals at labels 0,43,86,129 therefore give the full distance information up to this proven symmetry. If their radius-three deficits are m0,m1,m2,m3, the exact bad unordered pair count is `43*(m0+m1+m2+m3)/2`. No equalities between different root deficits are assumed.

## Remarks and Interpretation

Changing from (4,2,1) to (3,2,2) changes the actual base incidence multiplicities and increases the triangle-route term from 6*4*2*1 to 6*3*2*2. This batch uses no old graph or old random start. It does not merely add seeds to the previous family.

The first formal random state is independently expanded into a Python edge set and checked by four complete Python BFS traversals. All four 172-entry distance arrays are compared with the first C++ score, and that score is reused as the first production evaluation. No extra all-source preflight is run.

## Boundaries and Non-Claims

The finite scope is exactly 64 legal random starts, at most nine descent segments each, at most thirty strict full-coordinate moves per segment, and legal two-coordinate kicks between segments. No necessary-capacity filter omits an actual coordinate neighbor. Completing this batch is not a complete family exclusion; no other base or modulus is searched.

## Open Risks

The exact capacity and graph-label checks show no mismatch. Existence of a diameter-three graph in the full balanced voltage family remains unresolved after this finite experiment.
