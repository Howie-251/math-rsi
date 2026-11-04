# Independent final eight-hole proof review

Date: 2026-11-01. Reviewer task `/root/eight_full_closure_audit`, fresh context,
user-directed GPT-6.1-sol / high ARIS proof-checker route. This overrides the
skill's default model/effort. Semantic assurance is **same-family / provisional**;
there is no formalization or cross-family acceptance claim.

**Verdict: PASS, relative to the explicit published and previously audited
imports.** The complete statement in `EIGHT_HOLE_FULL_CLOSURE.md` is justified:
for every short 28-edge matching M in Q6, every free root u, and every vertex v
of opposite parity, there is a Hamilton u–v path containing every edge of M.
The target may be covered or free. There are no open mathematical obligations
within that exact eight-hole statement. Full P6 and the 10–18-hole layers are
outside this verdict, as is complete T15.

## Evidence and independence

Read the complete assembly, complete Q5 neighbor-abundance/EP0 argument, old
two-bridge transfer, free-target/A6 closure scopes, six-hole closure, all 24
imported marked-core review scopes and the historical geometry-chain reports.
The finite certificates underlying the imported core theorems are not all
re-enumerated here. Their whole-matching scope, exact marked omissions, proof
inputs, and fixed SHA256 bindings are checked. This boundary is explicit:
imported semantic theorems, rather than certificate counts, supply the
universal matching quantifier.

New standalone `EIGHT_HOLE_FULL_REVIEW_check.py` imports no producer/checker
module and reads no dynamic current-core ledger. It constructs all coordinate
projections and marked orbit maps directly. It checks the frozen input hashes
of 23 review reports and the finite A6 status report, with shared files hashed
once in this process. All declared `audited_input_hashes`,
`protected_core_hashes`, and `audit_artifact_hashes` in those reports match.
Context snapshots are historical metadata, not theorem premises, and are not
used as proof inputs. The complete fixed dictionary of actually checked inputs
is in `EIGHT_HOLE_FULL_REVIEW_check.json` and the final review JSON.

The final EP0 and Q4 abundance reports were already frozen and PASS before
this final verdict was emitted. In particular the final core1, core4 and core24
reviews, not preliminary versions, are bound. Review inputs do not include any
future eight-hole verdict, dynamic ledger, or global state.

## Explicit proof-obligation ledger

| ID | Obligation and discharge |
|---|---|
| F01 | Translation by u and coordinate permutation are cube automorphisms and transport every required edge, free root and specified target. Parity may reverse globally. Short M leaves exactly four holes of each parity. The normalized target has weight 1,3 or5, hence can be 1,7 or31. |
| F02 | The free-target theorem imports the full A6-discharge audit and includes every short matching and both prescribed free endpoints. It is not a sample result. |
| F03 | An edge from Z to W can be added without covering root0. Its endpoints were free; the new matching has29 edges. The complete six-hole theorem includes covered targets and produces the same prescribed0–v endpoints while retaining the augmented matching. Forgetting its extra requirement preserves M. |
| F04 | After that preprocessing, Z union W is independent; root-to-W adjacency is allowed. A covered target is excluded from all eight holes. No extra realizability or direction-use restriction is imposed. |
| F05 | All nine good rows are the previously audited covered-target transfers with A6 now discharged. A fresh independent C++ enumeration of all eligible covered geometries reproduces the entire residual set, rather than assuming saved counts establish completeness. |
| F06 | The old (1,4) theorem, eight singleton-avoided-face cores, and four balanced-bridge cores apply to every realizing matching. Direct recomputation from all66127 raw residual records reproduces their exact elimination and the fixed21350 base set. |
| F07 | All21350 base rows are unique. Every actual (2,1) cut is reconstructed from the original six coordinates; translate by the unique B member of Z, delete the cut coordinate, and retain the two mirrored Z holes as the marked avoided pair. The calculated core-choice set equals the saved set in every row. |
| F08 | For each21300 nonempty-choice row the checker supplies an actual cut, translation, projected marked holes, five-coordinate permutation and accepted complete-core review. No core26 theorem is assumed: rows with alternatives18,21,25 are assigned to their complete theorems. Arbitrary intermediate long/same-parity edges and all crossing bijections lie within the core theorem quantifiers. |
| F09 | For every remaining original matching, a sufficient (2,0) cut and covered odd crossing port q distinct from v exist. Independently regenerate every sufficient deleted crossing edge, and find a covered even vertex isolated after all deletions in each representative. The original matching must cover that vertex, so must use a deleted edge. The cut may depend on M. |
| F10 | For the selected q, any admissible D completes M_A to a matching L with precisely holes r,q. The covered v differs from q and from even r; with t=L(v), the vertices r,q,v,t are distinct. Replacing vt by rt gives exactly equal-parity holes v,q in an arbitrary K(Q5) matching. |
| F11 | The imported Q5 abundance theorem concerns the union of realizable short neighbors over31-cycles omitting v, not simultaneous degree3 on one cycle. Both that union and N(q) intersect S have size at least3 inside the same five-element neighborhood. Their intersection is nonempty, yielding some valid C and qs. This choice may depend on D and M. |
| F12 | C contains required rt. Replace rt by r–v–t and delete rv: the surviving object is a Hamilton r–v path containing L; vt is restored, rt removed, and every surviving new edge is short. Edge qs survives because q differs from r,v,t, including when s=r or s=t. Thus the exact existential EP0, with q distinct from v, is established. |
| F13 | Every possible s in N(q) intersect S, rather than one favorable s, gives an accepted marked core. Fresh reconstruction compares all234 projected cases exactly with the saved rows:174 core4,60 core1. No exchange of existential choices with a prescribed optional edge occurs. |
| F14 | The audited (2,0) transfer consumes t_B=s xor e_i, preserves all real crossings, attaches the two distinct short bridges and records the endpoint tag. Its final minority hole and two marked avoided majority holes agree with the projection witness. Both root-face cases, crossing targets, and s=root are allowed. |
| F15 | Simultaneous suppression of the two covered B bridge mirrors removes degree conflicts without cycles. Required compressed edges represent paths with disjoint interiors; applying the exact marked30-cycle theorem and expanding them restores all64 vertices and all original matching edges. Deleting the unique tagged0v edge leaves exactly the requested Hamilton0–v path. Auxiliary edges disappear or expand into the recorded paths, whose surviving new edges are short. |
| F16 | The seven target-preserving permutation orbits have sizes10,1,9,9,1,10,10; they are pairwise disjoint and equal exactly to both the50 no-choice base rows and the50 `closed_geometries` entries of the final EP0 review. No normalized geometry is omitted or counted as a matching. |

## Deterministic final accounting

The new C++ census enumerates the whole domain directly: for every nonzero
even triple Z it enumerates all odd quadruples W excluding the covered target
and adjacent Z vertices. It tests the nine rows and erases each retained tuple
from an independently read set of saved records. Every required erase succeeds
and the set is empty at the end. This proves exact set equality and absence of
omissions in addition to the totals.

| Target | Eligible geometries | Exact residual after nine rows |
|---:|---:|---:|
|1|9168375|19530|
|7|9334641|22472|
|31|9347625|24125|
|Total|27850641|66127|

Direct coordinate reconstruction from those66127 records gives:

| Discharged branch | Geometries |
|---|---:|
|(1,4) theorem|24669|
|Eight singleton-avoided-face cores|7820|
|Four balanced-bridge cores|12288|
|Fixed base with complete-core (2,1) witnesses|21300|
|Exact50 EP0 exceptions|50|
|Unaccounted|0|

The final fixed base SHA256 is
`787d22bb2d427c385428580fa1aa237069e3654e4761209782754254872060eb`.
`EIGHT_HOLE_FULL_REVIEW_witness.json` records one concrete discharging witness
for every base row, together with the complete marked24-core registry.

The new12 core choices selected in those21300 rows have multiplicities:
0:1989;1:150;4:2163;5:1326;8:2826;15:3252;18:984;21:1968;
23:3936;24:492;25:1968;27:246. Each multiplicity refers to marked hole
geometries and is backed by a theorem for all realizing arbitrary matchings.

## Dependency direction and adversarial checks

The dependency order is Q4 endpoint/avoidance and published perfect-matching
inputs, then N10/N14/A4/A6 and individual marked Q5 core theorems, then the
eight-hole local transfers and their coordinate geometry consequences, then
this final theorem. Q5 abundance uses its Q4 spectra and exact star-pair check;
it does not use any eight-hole conclusion or complete T15. Its EP0 consequence
then combines with the independently proved core1/core4 theorems. The final
accounting depends only on these lower nodes. The historical occurrence of an
OPEN eight-hole statement in an immutable source is not used as a hypothesis.
No circular use of this assembly, any higher-hole P6 layer, or full T15 occurs.

Counterexample checks specifically targeted a covered target that is a crossing
port, root in either face, root adjacent to an odd hole, a q equal to v, an s
equal to r or t, arbitrary auxiliary long and same-parity edges, two bridge
mirrors in one compressed component, both orientations of local parity, and
all possible returned optional neighbors rather than a prescribed one.
The sufficient-port reconstruction explicitly excludes q=v, and its deletion
certificates remain valid. The old fixed-cut exposure counterexamples do not
contradict the proved matching-dependent cut selection. These checks found no
counterexample or unresolved gap in a used implication.

Validation: compiled the new census with assertions enabled using
`D:/mingw64/bin/g++.exe -O3 -std=c++17`, ran it freshly, and ran the complete
new Python accounting/hash verifier successfully. The checker writes only its
own census result, witness and check JSON. No main research state, dynamic
ledger, goal, earlier proof, certificate or review was modified.

The accepted theorem remains relative to the explicitly imported mathematical
results and checked finite evidence, with same-family/provisional semantic
assurance. It closes the complete eight-hole layer only.
