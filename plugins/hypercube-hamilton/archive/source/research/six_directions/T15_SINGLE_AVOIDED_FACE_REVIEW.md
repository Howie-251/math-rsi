# T15 singleton avoided face: independent proof audit

Date: 2026-11-01. **PASS relative to the explicit Q4 imports.**
Review independence: **same-family**. Semantic acceptance: **provisional**.
Reviewer invocation: `model=gpt-6.1-sol`, `reasoning_effort=high`,
`fork_turns=none`, explicitly selected by the user (not inherited).
No FATAL, CRITICAL, MAJOR, or MINOR issue found in the stated eight-orbit
claim. Full Q5 T15 and full P6 remain unproved by this package.

The reviewer received the complete candidate as a fresh audit task and read
the ARIS proof-checker skill. The independent checker imports no producer
module and does not read the producer accounting JSON or verification JSON.
Reading producer source was used to understand file formats, not as a
verification oracle. The proof and declared input hashes are recorded in the
companion JSON and independent-check JSON. No main state file was edited.

## Exact scope and imports

The quantified conclusion is: for every one of the eight marked geometries
13,14,19,31,32,35,37,38, for every complete-graph matching whose holes are
exactly that geometry, there exists a simple cycle with support exactly the
30 vertices outside the specified two omitted majority holes, containing
every prescribed edge and using only cube edges elsewhere. Prescribed
edges may cross the chosen cut arbitrarily, have any length, or have equal
endpoint parity. Cube automorphisms transport this conclusion to each whole
marked orbit; the omitted pair remains the omitted pair.

Explicitly imported, rather than reproved in this invocation:

1. The exact, previously audited Q4 two-opposite-hole negative tables for
   holes 0,1 and 0,7, including the positive complement of their 51 and 53
   exceptions. The actual exception edge sets, not status/count fields,
   are used as input. Coordinate permutations give all eight odd targets.
2. Q4 A4_4 for any arbitrary matching with four holes of parity type 1:3,
   omitting a specified majority hole; only this finite Q4 result from
   `Q4_CORE_AND_A4_SPLIT.md` is used.
3. The exact finite Q4 T15 classification in `Q4_T15_CLASSIFICATION.md`:
   failure requires both omitted majority holes adjacent to the minority
   and a prescribed edge between the two other neighbors. Only its
   sufficient consequence when one omitted hole is nonadjacent is used.

Prior audit verdicts were not substituted for new checks on the candidate.
This audit does not newly revalidate the original Q4 binary tables or
certificates; that is the declared boundary of the imported results.

## Obligation ledger and dependency DAG

Symbols: A,B are disjoint 16-vertex faces; local vertex labels lie in
0,...,15; 0 is the omitted A vertex; a is the even B minority; x is the
omitted odd B vertex; I is its three included odd holes. F_A,F_B are
matchings; C is a crossing matching of size c; X_A,X_B its distinct port
sets; d is a free A root; D pairs all A ports except d; L=F_A union D;
S is the eligible odd target set; good roots refer to existence of an
individual completion for that fixed root and target. R denotes a formal
matching of pairwise interior-disjoint paths, not actual new long edges.

The acyclic proof chain is Q4 exact tables -> exact A path test -> failure
states -> stalled partials -> good-root sets and Hall obstruction. Separately,
Q4 A4/T15 -> safe and occupied transfer. The previous two chains close every
case except four c=1 families. Independent A input coverage + exhaustive B
pairings + positive witnesses -> optional spectra -> pairwise intersection
-> two-cycle switch closes those final families. No node invokes Q5 T15,
P6, or a consequence requiring the candidate conclusion.

| ID | Obligation and hypothesis discharge | Result |
|---|---|---|
| MC01 | Chosen cut has exactly one original hole in A, and it is omitted; local table agrees with the geometry file | checked all 8 rows |
| MC02 | Common coordinate deletion/translation preserves internal short edges and corresponding bridges | cube automorphism argument |
| MC03 | A has 15 and B has 11 covered original vertices, so c is odd and 1<=c<=11 | matching degree count |
| MC04 | For every port root d and D pairing the other ports, L has holes exactly 0,d | endpoint disjointness |
| MC05 | z odd, z!=d gives covered z, distinct d,k,z,0, and T_z has holes exactly 0,z | matching swap |
| MC06 | The cycle/path transformation is an equivalence preserving all prescribed edges and shortness of added edges | checked below |
| MC07 | Every negative root-state inverse is valid and every possible root-state failure occurs in the inverse set | full forward audit |
| MC08 | A state failing all fixed targets occurs in their inverse union despite the d=z exclusion | at most one of three targets equals d |
| MC09 | Exactly c(c-2)!! completions extend each partial F_A | distinct root and perfect pairing choices |
| MC10 | Submatching multiplicities characterize all stalled partials, including unvisited inputs | exact double-count, no search-failure assumption |
| MC11 | Every stalled partial's completions and eligible-target good roots | direct completion enumeration |
| MC12 | Failure of safe/occupied transfers induces a bad-root injection | actual C is injective on ports |
| MC13 | All c>=3 stalled cases have a deficient Hall subset | fresh maximum matching plus explicit Hall certificates |
| MC14 | Safe z gives a forest with distinct B leaves, even when z_A is temporarily isolated | degree and component proof below |
| MC15 | z in I yields exactly A4 hole set {a,x} union (I minus {z}) | omitted x is majority; all matching hypotheses hold |
| MC16 | Internally covered safe z allows kz,zq -> kq without repeated endpoints | internal endpoints disjoint from crossing ports |
| MC17 | This suppression gives T15 holes {a,x} union I union {z}, and x or z nonadjacent to a | definition of S |
| MC18 | Occupied root fixed to C inverse(z_B), d!=z and c>=3 prevents a closed A component | proof below |
| MC19 | Occupied contraction gives the same T15 holes and valid omission x,z | exact forest endpoint set X_B minus {z_B} |
| MC20 | Expansions preserve one simple cycle, all original matching edges, and only short new edges | disjoint path interiors; artificial edges disappear |
| MC21 | Orbit 37 at c=1 has a safe target; remaining four families have the stated unique h | direct good-root recomputation |
| MC22 | Every residual A input and every B matching occurs once among spectrum inputs | set equality to independent enumeration |
| MC23 | Every witness and union spectrum is valid, and every A/B pair has a common optional edge | all 34,514 witnesses and 396,900 pairs |
| MC24 | The edge switch forms one simple 30-cycle retaining the sole crossing | all 396,900 actual joined cycles checked |
| MC25 | All crossing counts, partials, B matching choices, and crossing bijections are covered | MC03, MC09-13, MC21-24 |

No limit interchanges, probability-mode upgrades, asymptotic constants, or
uniformity assumptions arise: all quantifiers range over explicit finite sets.

## Sensitive boundary arguments

**Exact path test (candidate lines 69-83).** In a d--z path containing L,
the z endpoint must use its sole prescribed incident edge zk. Removing z
therefore leaves a spanning d--k path on 14 vertices. Its endpoint edge dk
cannot already occur: a path with more than two vertices cannot contain its
endpoint-to-endpoint edge. Adding dk closes it. Conversely remove the
required dk from a 14-cycle and append the original kz. Even if dk is long,
it is removed in expansion; kz is prescribed. There is no unverified
shortness assumption. The impossible z=d case is handled explicitly.

**Safe forest (lines 93-115).** D is a matching contained in a simple path.
Its removal makes a path forest. Every nonendpoint port loses its D edge
and regains degree one after its original crossing is attached; d gains
its crossing; z gains its bridge. If z_A is a port, it loses its final D
edge and becomes isolated, then gains two distinct incident edges: its
original crossing and the new bridge to the safe B vertex. The B endpoints
are distinct because the bridge endpoint is outside X_B. This is still a
path, not a lost vertex or a closed component. All resulting interiors are
disjoint, which licenses compression and expansion.

**Occupied forest (lines 117-132).** Here the root is chosen *after the
actual crossing C is fixed*: d=C inverse(z_B). It is required to be good for
this z, which means existence of some D for this fixed root. Since c>=3,
D is nonempty. Removing even one D edge from the d--z path separates d
and z, including the case that the final D edge isolates z. The crossing
at d attaches z_B to the d component. The bridge then connects that
component to the different z component. It cannot close a cycle. If z_A
is another port, its original crossing has a B endpoint different from
z_B by injectivity of C. The final forest endpoints are exactly
X_B minus {z_B}, with interiors A minus {0} together with z_B. The excluded
c=1 case would lack this separation and is not incorrectly passed here.

**Hall quantifiers (lines 134-178).** If all available z are occupied and no
occupied transfer works, actual C gives an injection from available z into
A ports, assigning each z a bad root. Rejecting every such injection is
stronger than needed and covers every B port set and crossing bijection.
A good root need not use one globally common D: after selecting z and its
actual root, its own witnessing D can be chosen. Thus no forall/exists
exchange is hidden in the good-root argument.

**One-crossing cycle switch (lines 180-220).** Each individual pair may
choose a different common edge and different witnessing path/cycle.
Membership in both *unions* is sufficient: it supplies a witness on each
side for that selected edge; spectra need not be maximal. C_A uses
A minus {0} and h_B, while C_B uses B minus {x,h}, so their supports are
disjoint and total 30. A common optional edge avoids 0,x,h. Deleting one
edge from each cycle produces two paths; the two corresponding bridges
connect their four distinct endpoints into a single cycle. Neither deleted
edge is prescribed, and the sole prescribed crossing d_A h_B survives.
The independent checker checks degree two, connectedness, exact support,
prescribed-edge containment and new-edge shortness for every pair.

## Deterministic results

The standalone checker is `t15_single_avoided_face_independent_check.py`;
its recorded output is `t15_single_avoided_face_independent_check.json`.
Run with Python 3.10 or later from any working directory. Runtime in this
run was about 72 seconds.

- 2,027,025 near-perfect rooted states, forward checked at every applicable
  odd target: 15,135,120 exact comparisons to Q4 source exception sets.
- Complete fixed-target failure sets: 105 each for 13,14,31,35,37; zero
  for 19,32,38. No producer-provided count used in deriving these sets.
- For each nonempty row, exact stalled partial counts at c=1,3,5,7,9,11:
  105,105,21,1,0,0. Every stalled completion was regenerated and rechecked.
- All 635 c>=3 stalled partials have an independently derived deficient
  Hall subset; all 105 c=1 stalls for orbit 37 have more usable targets
  than ports. The other 420 c=1 stalls have exactly their claimed h.
- 4200 distinct inputs: exactly 105 A and 945 B matchings for each of the
  four remaining rows. B coverage was checked against all pairings of the
  exact ten covered vertices; A coverage against fresh failure enumeration.
- All 34,514 stored positive path/cycle witnesses checked; every stored
  spectrum equals the reconstructed optional-edge union. Search node and
  solution-count metadata were not used.

| Orbit | A inputs | B inputs | Pairs | Minimum optional intersection |
|---|---:|---:|---:|---:|
|13|105|945|99,225|7|
|14|105|945|99,225|5|
|31|105|945|99,225|9|
|35|105|945|99,225|6|

All 396,900 intersections are nonempty. For each pair, a selected witness
pair was actually joined and verified as a valid simple 30-cycle. This is
an exhaustive deterministic certificate check within the finite claimed
domain, not sample evidence for additional T15 geometries.

## Counterexample pass and verdict boundary

Adversarial cases examined: d=z; endpoint z carried by D rather than F_A;
temporary isolated z_A; the smallest occupied crossing count c=3;
the forbidden occupied c=1 closure; a safe target internally covered in B;
same-parity/long required edges; repeated/artificial compressed edges;
overlap of the two cycles through h_B; optional edge incident to an omitted
vertex; a union edge witnessed by different choices on the two sides; and
a matching input missing from or duplicated in positive files. The first
and occupied c=1 cases are excluded exactly where needed, overlap is avoided
by excluding h_B from C_B, and all other boundaries are discharged above.
No verified counterexample or open proof obligation remains for the stated
claim relative to the explicit Q4 inputs.

This PASS is same-family/provisional semantic review, with deterministic
finite verification accepted for the stated input files. It closes the
specified eight marked Q5 T15 orbits relative to the imported finite Q4
results. It neither proves full T15/P6 nor changes a Q6 parent count; such
coverage must be recomputed over all allowed cuts separately.
