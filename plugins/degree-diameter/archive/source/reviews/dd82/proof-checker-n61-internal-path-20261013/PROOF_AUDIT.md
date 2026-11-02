# Internal double-path proof audit

Date: 2026-10-13. **PASS for the stated necessary conclusions, modulo the
explicit inherited imports.** No mathematical gap or false statement was
found in either declared manuscript. There are zero open issues.

This is one **fresh, same-family, provisional** Codex review by
`/root/internal_path_proof_check`, spawned with no inherited conversation
and requested `gpt-6-astra` / `ultra`, as confirmed by the parent. That
configuration is not independent backend attestation. This review does
not confer external acceptance or Lean verification.

## Exact scope and method

The complete primary inputs were read directly:

- `proofs/dd82/n61/INTERNAL_DOUBLE_PATH_LOCAL.md`, lines 1–190.
- `proofs/dd82/n61/INTERNAL_DOUBLE_PATH_FOLLOWUP.md`, lines 1–114.

The frozen 24-obligation inventory is `PROOF_SKELETON.md`. Every local
parent count, endpoint type, commutation use, recurrence boundary,
rectangle alternative and path-size inequality was checked analytically.
The documents were not edited. No solver, graph search, enumeration,
external call, old order62–65 review, formalization, rendering, paper
score or artifact digest was performed. No mathematical claim from a
separately pending followup is included in this verdict.

The project-local `proof-checker` skill was applied with the user's V3
adaptation. Its report, state and obligation outputs are retained here;
paper/rendering machinery is inapplicable to this bounded Markdown proof
review. The parent owns any wiki integration, external review and later
model implementation.

## Imports: source and review provenance

`CONNECTED_TRIPLE_EXCLUSION.md` supplies actual order61 regularity,
nonnegative integral symmetric zero-diagonal defect, row sum four,
entries in `{0,1,2}`, and connected positive support. Its stated
finite-enumeration and exact-CNF certificate dependencies are inherited,
not rechecked. The saved Gemini round4 result
`reviews/dd82/20261013_V3_n61_triples_final_review.json` explicitly accepts
that structural theorem while leaving order61 open. Its stored thread
is `a26ad33b-931a-46cd-a72e-a6cbf6d4ee2a`.

`DOUBLE_DEFECT_CYCLE_OBSTRUCTION.md` supplies the path-forest conclusion.
Its introductory writer-checked sentence predates the following records:

- `reviews/dd82/proof-checker-n61-adjacent-double-20261013/PROOF_AUDIT.md`
  and `.json`: prior fresh same-family provisional cycle review, with a
  fresh read-only cycle shard; later adjacent-model deltas are explicitly
  reused and are not dependencies of this new audit.
- `reviews/dd82/20261013_V3_n61_adjacent_direction.json`: Gemini round1
  explicitly accepts the cycle proof and path-forest corollary.
- `reviews/dd82/20261013_V3_n61_adjacent_ports_final_review.json`: the same
  external thread's round3 final inventory retains that structural result.
- `prompts/26101313-1/final.md`: assembled handoff states the exact
  inherited scope and distinguishes local provisional review from Gemini.

The saved external thread is `c486e575-cfca-490a-a2c8-aea4fba5fdb5`.
All three external status records inspected report requested and returned
`gemini-3.8-flash-high`, effort `high`, status `SUCCESS`, and selected
label `Gemini 3.8 Flash (High)`. These are historical saved CLI metadata,
not independent backend attestation and not new external review of the
two current manuscripts. Only import/status alignment was reviewed;
their old proofs, computations and certificates were not rerun.

## Counterexample-first checks

These probes were resolved by exact reasoning, before the positive
closure decision. They are not unsuccessful numerical searches offered
in place of proofs.

1. **A-adjacent double incident to an internal vertex.** Its two distinct
   common neighbors would both need to be the sole remaining allowed
   positive endpoint in the saturated middle row. This is impossible.
   An isolated A-adjacent double edge remains allowed; it is never
   silently removed.
2. **Full overlap `U=W`, or a lost beta-one case.** The relation
   `r+h=1+beta-epsilon` and `beta<=1` imply `r<=2`; overlap three is
   impossible. The beta-one possibilities `(r,h)=(0,2),(1,1),(2,0)`
   are all retained. Their later confinement to three-vertex components
   does not exclude them globally.
3. **Endpoint adjacency `epsilon=1`.** The common neighbor `w` of
   `u,t` must be counted exactly when `t in W`. Formula (9) includes
   it. Setting the residual vectors to zero would lose two row units;
   the manuscript instead leaves their nonnegative entries variable.
4. **Exceptional attachments or overlapping P,Q.** A vertex in both
   P and Q has `e(z)=2`, so the nonexceptional rule cannot be applied
   to it. The proof uses (10) on all exceptions and (11) only outside
   their union, with the correct inclusion–exclusion cardinality.
5. **Smallest Toeplitz paths and extreme indices.** For `m=2`, all
   offdiagonal shift differences compare consecutive nonedges and
   vanish. For the furthest index `(i,j)=(0,m-1)`, the recurrence
   uses the valid internal pair `(1,m-1)`. Gap one is a direct base
   case, not a recursive invocation crossing the diagonal.
6. **Equal offsets and the boundary rectangle.** If `p=q`, the proposed
   four vertices collapse; the theorem expressly excludes that case.
   If `p+q=m` and `|p-q|=1`, the middle pair has defect two, so two
   endpoint common neighbors give no contradiction. That alternative
   is retained, then handled in the odd-center count.
7. **First forbidden component sizes.** For `k=53`, `m=52`, the two
   chosen centers are internal and have path degree at most two. For
   `k=54`, `m=53`, the exceptional offsets 26 and 27 give the two
   endpoints as common neighbors of the centers; outside overlap is
   at most one. Both cases require at least nine exterior vertices,
   and the same inequalities hold at all larger sizes.
8. **Unjustified global symmetry/independence.** Only T is proved
   independent here; triangles elsewhere remain possible. Toeplitz
   structure is confined to the path principal block. Unequal parent
   classes and exceptions prevent interpreting (11) as a complete
   matching cover or an equitable global partition.

No counterexample to a stated claim was found; all obligations below
are discharged by derivation, not by the absence of a counterexample.

## Local template: full derivation checks

**Actual identities and nonedges (L01–L04; local lines 12–58).** For
distinct x,y, the actual matrix definition gives `mu=1+B-A`. Since
`AJ=JA=8J`, the same definition gives `AB=BA`; B is not an independently
chosen weighted graph. If `A_uv=1`, its two common neighbors each give
a positive defect in row v. They are distinct from u,v, but only w is
available. Thus `A_uv=A_vw=0`. Every edge in T would similarly force
a forbidden positive entry in row v, so T is independent.

The two double pairs have three common neighbors each, giving
`|U|=|W|=3`. Every z outside `T union {u,v,w}` has `A_vz=B_vz=0`, so
exactly one T neighbor. For a pair x,y in T, v supplies the baseline
common neighbor; u and w supply the two possible extras. No vertex
of T can be common, and no z can meet two T vertices. This proves
the exact weighted sum of the two triangles in `B[T]`, including
the possible doubled intersection edge.

**Six cases (L05–L07; lines 62–90).** The two sides of commutation
at `(v,x)` are exactly `sum_{t in T}B_tx` and `2(A_ux+A_wx)`.
For x=u,w this gives sum `2epsilon`. If epsilon is one, each endpoint
already spends two units at v and the other two in T. Therefore its
defect at the other endpoint is zero, and `mu(u,w)=0`. The possible
common-neighbor locations are precisely T and Z, proving (6).
For epsilon zero, beta zero gives `r+h=1` and beta one gives `r+h=2`;
nonnegative integral solutions give the other five rows of the table.
No listed type is asserted realizable.

**Parent and endpoint counts (L08–L11; lines 94–127).** At t, the
original neighbors already assigned are v and `k_t` endpoints. The
other `7-k_t` are exactly `Z_t`. Membership in both U,W, in exactly
one, and in neither has cardinality `r`, `6-2r`, and `2+r`.
Their weighted class-size sum is `5r+6(6-2r)+7(2+r)=50`.
The endpoint neighborhoods give `|P|=|Q|=8-3-epsilon=5-epsilon`.

For epsilon zero, a zero nonnegative defect sum gives `B[T,u]=0`.
The only common neighbors of u and t are the members of `P intersect
Z_t`, so their number is `1-1[t in U]`; the w equation is symmetric.
For epsilon one, the vanishing u,w common-neighbor count proves both
disjointness statements. The actual common neighbors of u,t are those
in `P intersect Z_t`, plus w exactly when `t in W`. Solving the
identity for the former gives (9), including the two residual-vector
sums. These sums also give four endpoint attachments, consistent with
the degree count.

**All remaining vertex counts (L12–L13; lines 129–148).** For z in
`Z_t`, its known neighbors are its parent and the `e(z)` attached
endpoints, so `d_Z(z)=7-e(z)`. Against x in T, its common neighbors
are exactly its neighbors in `Z_x` and the attached endpoint terms
displayed in (10); v is not adjacent to z and T is independent.
Adding `A_xz=1[x=t]` and subtracting one gives the claimed B entry.
The column sum is the already proved commutation identity.
For `e(z)=0`, nonnegativity forces all these defect entries to vanish,
so (11) follows. Finally `50-|P union Q|=40+2epsilon+h`, which is
`40+h` for epsilon zero and 42 for epsilon one. There are at most
ten exceptions. No unproved uniform rule is used on them.

## Toeplitz proof: recurrence and bounds

**L14–L16; local lines 150–173.** If an A-adjacent double edge had an
additional D neighbor at either end, L02 applied there would contradict
that adjacency. Therefore every edge of a path with at least two
edges is an A nonedge.

For internal r,s, both entire defect rows are saturated by the two
path neighbors. Thus external vertices contribute zero to both sides
of `(AB)_{r,s}=(BA)_{r,s}`, giving (12) after division by two.
For `0<=i<j<=m-1`, substituting `r=i+1,s=j` is valid: i is at most
`m-2`, and j is at least one. Rearrangement yields

`a_(i+1,j+1)-a_(i,j)=a_(i+2,j)-a_(i+1,j-1)=E_(i+1,j-1)`.

If the gap is at least two, both new indices stay in range and the
gap decreases by two. On the diagonal E is zero because both original
diagonal entries are zero. At gap one it is zero because both entries
are consecutive-path nonedges. Symmetry handles i>j. Therefore the
entire shift-difference matrix vanishes. No endpoint defect row is
assumed saturated and no cyclic continuation or automorphism is used.

## Followup: all three conclusions

**Beta-one confinement (F01; followup lines 31–44).** At u the double
edge uv and unit uw already have weight three. A second double edge
would bring this to at least five, contrary to row sum four. The
same applies at w. With v already of D degree two, this is exactly
the three-vertex component. Components of size at least four therefore
have beta zero at every internal triple, with all three beta-zero
local types still admitted by the current manuscripts.

**Distinct offsets (F02–F04; lines 46–66).** An internal row has no
defect to a nonconsecutive path vertex, giving `mu+A=1`. Distinct
positive p,q with sum at most m make four distinct vertices. If their
sum is less than m, vertices 0 and p+q are a nonconsecutive pair with
an internal endpoint and have common neighbors p and q, impossible.
If the sum equals m, p and q are both internal and have common
neighbors 0 and m. Their distance can therefore only be one. This
does not assume adjacency between either opposite pair. The vacuous
short-path cases do not require applying Toeplitz below m=2.

**Size bound (F05–F08; lines 68–104).** For two consecutive internal
vertices, `A_xy=0`, `B_xy=2`, hence exactly three common neighbors.
The exterior-neighborhood union is precisely
`16-d_P(x)-d_P(y)-c_out` by inclusion–exclusion.

If `m=2r`, selected distinct offsets always sum above 2r, since an
even sum cannot have difference one. At x=r only one offset at most
r can occur, contributing two neighbors. At y=r-1 a small offset
at most r-1 excludes both r and r+1; without one, those two large
offsets contribute at most one each. Thus both degrees are at most
two, and `c_out<=3` yields an exterior union of size at least nine.

If `m=2r+1`, the center degrees are equal. At most one selected
offset at most r can occur, contributing two neighbors; offset r+1
contributes one. Coexistence forces the pair r,r+1, by the exact
boundary alternative. Unless both occur, degrees are at most two.
If both occur, the degrees are three and both path endpoints are
common neighbors of the centers, so `c_out<=1`. The exterior union
still has at least `16-3-3-1=9` vertices. For k>=53 all selected
centers are indeed distinct internal vertices. The remaining graph
has `61-k<=8` vertices, yielding the stated contradiction. Components
of sizes one and two already obey the conclusion, and no claim of
sharpness or near-bound realizability is made.

## Closure and remaining scope

All 24 frozen micro-claims are discharged under the stated imports.
There are no new assumptions, fixes, theorem weakenings, unresolved
issues, exchanges of limits, stochastic modes or hidden constants.
The dependency graph is acyclic, and each case split is exhaustive.

The original graph on Z, its exceptional incidences and all simultaneous
common-neighbor counts remain unresolved. The manuscripts do not
eliminate internal double vertices, beta-one triples, isolated adjacent
doubles, all triangles, or order61. Their conclusions neither impose
global Toeplitz symmetry/equitability nor replace the shared actual A
by independently chosen defect data. General58–61 and the inherited
range `57<=N(8,2)<=61` remain unchanged by this bounded review.
