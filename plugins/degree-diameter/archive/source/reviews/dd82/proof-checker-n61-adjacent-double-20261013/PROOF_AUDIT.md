# Order61 adjacent-double and double-cycle proof audit

Date: 2026-10-13. One bounded fresh Codex review, with a fresh read-only
cycle-lemma shard. Review independence: **same-family**. Acceptance status:
**provisional**. This is neither Gemini review nor Lean verification.

**Finding:** no substantive mathematical defect found in the stated necessary
template, seven-type normalization, or double-cycle obstruction, conditional
on the expressly accepted imports. The initial minor wording error about a
five-point transversal was corrected by the parent and the correction read.
The adjacent-double exclusion and general
order61 exclusion remain open; neither is established by these notes.

## Scope and method

Reviewed completely:

- `proofs/dd82/n61/ADJACENT_DOUBLE_REPEAT_LOCAL.md`, lines 1–260.
- `proofs/dd82/n61/DOUBLE_DEFECT_CYCLE_OBSTRUCTION.md`, lines 1–129.
- `proofs/dd82/n61/ADJACENT_DOUBLE_DIRECTION.md`, especially lines 50–73.

At the parent's request, a small same-round coverage addendum also reads
`proofs/dd82/n61/ADJACENT_DOUBLE_FULL_GRAPH_MODEL.md` in full, including
the subsequently added group-matching consequence. This reviews a
mathematical specification, not implementation or execution.

The connected, nonnegative, zero-diagonal, row-four defect matrix with
entries in `{0,1,2}` is an **accepted import** from
`CONNECTED_TRIPLE_EXCLUSION.md`; its computation was not re-audited. Every
new use of that import was checked. The original adjacency matrix is simple,
undirected, 8-regular, on 61 vertices, and has diameter at most two.

Applied project `.agents/skills/proof-checker/SKILL.md` under the V3
mathematical adaptation. No experiments, old solver reruns, external calls,
Lean work, rendering, paper scores, or hashes were performed. This reviewer
did not edit manuscripts. Wiki mutation is left to the parent because this task owns only
this review directory.

Reviewer: `/root/n61_adjacent_double_proof_check`. Independent bounded shard:
`/root/n61_adjacent_double_proof_check/cycle_lemma_readonly` (requested
`gpt-6-astra`, reasoning `ultra`). The shard reviewed only the cycle note and
returned its mathematical derivation, not acceptance of the wider proof.

## Local template: concrete derivation checks

**Core and parity, local lines 41–62.** For adjacent pairs, `B_xy=mu(x,y)`.
Thus `B_uv=2` gives exactly two common neighbors `s,t`, and their triangles
spend the remaining two units in each of the `u,v` defect rows. If `st` were
an edge, `mu(u,s)` would be at least two, contradicting `B_us=1`.
For the nonedge `st`, its two known common neighbors give `B_st>=1`.
The alternative `B_st=2` saturates all four core rows, contradicting
connected positive support on 61 vertices. Each of `s,t` consequently has
one external unit port, initially allowing coincident endpoints.

The parity step at `s` is exact: the sum of `B_sx` over actual neighbors of
`s` is `2+A_sp`, and also equals twice the number of triangles through
`s`. Since `A_sp` is binary, it must be zero. There is exactly one triangle
at `s`; the same holds at `t`. At `u,v`, the sums are four, accounting for
exactly the two displayed triangles.

**Partition and same-A identities, local lines 66–109.** Independence of
each layer follows from the exact triangle counts. Disjointness follows
from `mu(u,v)=mu(s,t)=2` and exclusion of additional core triangles.
For `f=e_u-e_v`, `g=1_U-1_V`, the identities are

`Bf=-2f`, `Af=-f+g`, `(A^2+A)f=5f`, `Ag=5f`, `Bg=-2g`.

Here `Jf=0`, and `AB=BA` follows from regularity, so all steps use the
same original `A`. The `U,V` coordinates of `Ag=5f` force `A[U,V]=0`.
For the neighborhood block at `u`, every distinct pair of neighbors has
the common neighbor `u`; its defect equals adjacency plus the number of
additional common neighbors. From the complete `u` row, only `v` has two
neighbors inside `N(u)`, namely `s,t`. Together with the two induced edges
`vs,vt`, this proves exactly the three unit edges in (5).

In particular distinct `U` points have only `u` as a common neighbor.
Their seven other neighbors therefore give 35 distinct vertices, each
with one `U` neighbor and, by `Ag=5f`, one `V` neighbor. Points in `S,T`
cannot be among them: their parent `s` or `t` already accounts for their
unique common neighbor with both `u` and `v`. The sizes total
`4+5+5+6+6+35=61`; no unassigned vertices remain.

**Port location and layer degrees, local lines 111–146.** At `(u,z)`, with
`z` in `S union T union Z`, commutation gives exactly

`1[z=p]+1[z=q]+sum_{i in U} B_iz = A_sz+A_tz`.

For `z` in `Z`, the right side vanishes. Together with `A_sp=A_tq=0`
and the neighborhood-block zeros, this proves `p in T`, `q in S`, and
only then their distinctness. Nonnegativity makes all ordinary `S/T`
ports to `U` and `V` units and excludes every `U/V` defect port into `Z`.
At `x in S`, common-neighbor counting against `t` gives
`d_T(x)=1+1[x=q]`; its remaining degree is `6-1[x=q]` in `Z`.
The symmetric formula holds in `T`. At a `Z` vertex, counting against
`s,t` gives one neighbor in each layer; the four `U,V,S,T` neighbors
leave exactly four neighbors in `Z`.

Taking `U,V` coordinates in `Bg=-2g`, using `B[U]=B[V]=0`, proves both
row and column sums of `C=B[U,V]` are two. The common neighbors of
`u_i,v_j` are precisely their shared `Z` cell, so its size is
`1+C_ij`. These are actual incidence cells, not independently chosen
common-neighbor witnesses.

**S/T interface and remaining ports, local lines 148–203.** At `(s,y)`
for `y in T`, the `AB` side is `sum_{x in S}B_xy`; the `BA` side is
`A_uy+A_vy+A_ty+A_py=1`, including when `y=p`. The symmetric equation
gives all row sums. Thus the integer matrix `P=B[S,T]` really is a
permutation matrix. The only common neighbors of an `S,T` pair lie in
`Z`, proving `L=J-K+P` without requiring `K` and `P` disjoint.

For (13), the only induced edge of `N(s)` is `uv`. Apart from `s`, the
only vertices with two neighbors in this neighborhood are `t` (neighbors
`u,v`) and `p` (the two-element set `E`). All others have at most one
by the complete `s` defect row. This proves the doubled `uv` edge and
single edge on `E`, with no omitted defect edges. The `t` argument is
identical with `q,F`.

At `(s,z)` and `(t,z)`, commutation gives exactly the two column sums
in (14). Removing them from the defect row gives (15), whose total is
`35*4-5-5=130`, or unordered weight 65. This does not conflict with
the 70 actual edges in `A[Z]`. For an `S` row, the other defect
contributions total

`1[x=q]+2(1-1[x=q])+1[x in E]+1`,

so the remaining sum is exactly (16). The five-point sets `N_Z(p)` and
`N_Z(q)` each meet every `U` class and every `V` class once, since the
relevant original pair is nonadjacent and has defect zero. Finally the
only common neighbors of `p,q` lie in `Z`, giving
`|N_Z(p) intersect N_Z(q)|=1+eta-epsilon`. All four binary combinations
are retained; realizability of them is not asserted.

## Normalization and coverage

Every connected component of a degree-two bipartite multigraph is an even
cycle, allowing a double edge as the size-two cycle. Alternating around
each component produces two perfect matchings; independent `U,V` labels
make one identity. The other becomes a permutation whose cycle sizes are
the component half-sizes, a partition of five. Conversely those component
sizes are invariant under independent row/column relabeling. This proves
exactly the seven listed types, including the all-double type `C=2I`.
Changing alternating colors within a component merely reverses the
associated cycle orientation and introduces no additional type.

The four claimed port bijections have both sides checked. Equation (7)
gives one unit from each ordinary `S/T` vertex into each of `U,V`.
For `u_i in U`, `(s,u_i)` commutation gives

`sum_{x in S}B_x,u_i = A_u,u_i+A_v,u_i+A_t,u_i+A_p,u_i = 1`.

The three other versions give one endpoint per `U/V` vertex as well.
Thus each is a perfect matching. After normalizing `C`, labels of the
five ordinary `S` vertices and the five ordinary `T` vertices can be
chosen independently by their `U` endpoints. Their `V` matchings remain
variable, as do `K`, `P`, and their incidences to the already cell-labeled
`Z`. No same-A relationship has been silently fixed twice. In particular
the `q` transversal cannot also be fixed to the identity by the exhausted
independent `V` relabeling argument.

This is a lossless necessary representation: every actual graph in this
branch has such labels. It is not a sufficiency proof or verification of
any later CNF encoding. All original same-A degree/path constraints still
need to be enforced by such an implementation.

## Cycle note and counterexample probes

For `E_ij=H_{i+1,j+1}-H_ij`, the entry `(i,j+1)` of `HC=CH` gives
`E_ij=E_{i-1,j+1}`. Oddness permits `t=(i-j)/2` modulo `n`; iteration
reaches `E_{(i+j)/2,(i+j)/2}=0` by constant diagonal. The proof works
also at `n=3` and nowhere uses symmetry of `H`.

Under `B=2A(C_61)`, commutation and the zero diagonal of the actual `A`
therefore make `A` circulant. Its eight shifts are four opposite pairs.
Two-step sums are cancellation, doubled shifts, or sums from distinct
opposite pairs; hence the ball has size at most `1+8+8+24=41<61`.
Coincidences only reduce this bound. A cycle of double defects saturates
every row on that cycle, so nonnegativity removes all outgoing defect
edges; connectedness forces a spanning cycle. This proves the path-forest
corollary. It does not exclude paths.

Analytically verified probes, without experiments:

- Dropping constant diagonal: for odd `n>=3`, the reflection
  `R_ij=1[i+j=0 mod n]` commutes with the cycle and is symmetric, but
  `R_00=1`, `R_11=0`; it is not circulant.
- Dropping oddness: for even `n>=4`, the reflection
  `R_ij=1[i+j=1 mod n]` is symmetric and zero-diagonal and commutes
  with the cycle, but `R_01=1`, `R_12=0`; it is not circulant.
- Nonsymmetric probe: the directed cyclic-shift permutation has constant
  zero diagonal, commutes with `C=P+P^{-1}`, and is circulant, consistent
  with the absence of a symmetry hypothesis in the lemma.
- Local degeneracies retained: the initial possibility `p=q` is excluded
  by proved port locations, not by a naming convention. Double entries
  of `C`, all seven component partitions, overlap of `K,P`, and all four
  `(epsilon,eta)` cases remain in the representation.
- Connectedness probe: without the import, saturation would isolate a
  double cycle but would not force it to span all 61 vertices. This is
  exactly where the corollary needs connected positive support.

## Issue and disposition

**MINOR-1 — UNCLEAR / COSMETIC / notation.** Local manuscript lines
191–192 initially said “Each of the five Z neighbors of p or q forms a transversal.”
An individual vertex cannot form a five-class transversal. The surrounding
proof establishes the intended set statement. Minimal fix:
“Each of the sets `N_Z(p)` and `N_Z(q)` is a transversal of the five U
classes and also of the five V classes.” No theorem, hypothesis, or
downstream mathematical conclusion changes. The parent applied exactly this
correction during the review; the reviewer reread lines 188–197 and closed
the issue. No manuscript edit was made by this reviewer.

There are zero open fatal, critical, or major issues in this bounded
review, and the sole minor issue is closed. The machine verdict is
`PASS/all_proofs_complete` for the claims in scope; the mathematical finding
is sound modulo the explicit accepted imports,
with same-family provisional status. Subsequent encoding, solving, external
review, and any order61 exclusion are outside this completed review.

## Same-round addendum: full original-graph model specification

The model uses 61 distinct original labels and all `61*60/2=1830`
unordered adjacency variables. For a distinct pair there are exactly 59
possible intermediate vertices; its direct edge together with those
59 actual conjunctions supplies the correct diameter-two disjunction.
Exact degree eight and the declared simple undirected adjacency variables
therefore preserve the original graph semantics. For each pair,
`c_xy=A_xy+sum_w(A_xw AND A_wy)=1+B_xy`, so the inherited range is
exactly `1<=c_xy<=3`.

The three label choices are compatible. Each row of `H=J+C` sums to
`5+2=7`, permitting five fixed groups of seven `Z` vertices with one
unconditional `U` parent each. Within a group, the type-dependent cell
sizes permit consecutive labels for the `V` parents. Every actual graph
admits this relabeling of its 35 actual vertices. Choosing ordinary `S`
and `T` labels afterward uses only their independent permutations and
does not change `C` or either `Z` parent. Leaving their `V` defect maps,
the `S/T` adjacency pattern and the `q` transversal variable avoids an
additional unproved normalization.

Thus every actual adjacent-double graph has a satisfying assignment of
the specified full model. Omitting optional, proved necessary identities
can only enlarge its solution set; this does not weaken the coverage
implication needed for an UNSAT exclusion. Conversely any decoded model
satisfying all original degree/path constraints is an actual target;
the fixed core neighborhoods already give adjacent `u,v` exactly the
two common neighbors `s,t`.

No substantive issue was found in this specification. Correct auxiliary
conjunction definitions, selector guards, cardinality encodings and
actual solve/certificate evidence remain implementation obligations.
This addendum does not claim those obligations have been checked.

The parent then added one redundant propagation consequence, also checked
within this round. Let `Z_i` be the seven vertices whose `U` parent is
`U_i`. For every `z in Z`,

`mu(U_i,z)=A_uz+sum_{w in Z_i}A_wz=d_Z_i(z)=1-A_U_i,z`,

because `A_uz=0` and the proved interface has `B_U_i,z=0`. Thus there
are no `A[Z]` edges within a `U` group and every vertex has one neighbor
in each of the other four groups. For any two groups this is degree one
on both sides, hence a perfect matching. The identical proof applies to
the selected `V` groups, which also have size seven by the column margins
of `H`. Encoding these counts does not choose a particular matching or
impose an automorphism; it is a valid consequence for every actual graph
covered by the model.

## Same-mechanism delta: S/T port propagation

Read the complete stable `ADJACENT_DOUBLE_PORT_PROPAGATION.md` after its
author confirmed that editing had stopped. This deliberately reuses the
reviewed local equations; it is an incremental same-family provisional
check, not a new independent review of the original imports. No computation,
external call, old proof rerun, or new review directory was used.

**Exact same-A color counts, equations (1)–(5).** For `z in Z`, the
unique parents `x(z),y(z)` are actual neighbors in `S,T`. The previously
checked port column sums become `sum_x beta_xz=1[y(z)=p]` and
`sum_y gamma_yz=1[x(z)=q]`; their row sums remain local (16).
For `x in S`, its complete neighborhood is `{s}`, its actual `K`
neighbors, and its `Z` color class. Since `A_sz=0`, its common-neighbor
count with `z` is exactly `K_x,y(z)+d_Z^S_x(z)`. Thus

`d_Z^S_x(z)=1+beta_xz-1[x=x(z)]-K_x,y(z)`.

The symmetric `T` formula follows identically. No common neighbor from
another layer is omitted. Summing over all six `S` colors gives four,
because the `K` column degree is `1+1[y(z)=p]`, consistently with the
actual degree four inside `Z`.

**Only possible K/P overlap, equation (6).** A point in an `S,T` cell
with `K_xy=1` forms the actual triangle `x,y,z`. The two defect ports
to `z` are therefore positive. Their respective column sums force
`y=p` and `x=q`. On a `K` edge, cell size `1-K_xy+P_xy` is `P_xy`,
so `K_xy P_xy=0` outside `(q,p)`. At `(q,p)`, a triangle occurs exactly
when `epsilon=eta=1`, when the cell contains one point. No other original
triangle containing an `S/T` edge is possible.

**Shared-parent Z edge, equations (7)–(8).** If `zz'` is an actual edge
with common `S` parent `x`, its triangle supplies two distinct positive
entries in row `beta_x,*`. The port column sums force both `T` parents
to be `p`. The row formula `1+1[x=q]-1[x in E]` can be at least two
only for `x=q` with `epsilon=0`. The cell then has size `1+eta`, so
`eta=1` and `z,z'` are its two points. The argument with common `T`
parent reaches the same case.

There are now four unit entries `B_qz=B_qz'=B_pz=B_pz'=1`. The adjacent
pair `z,z'` has distinct common neighbors `q,p`, so `B_zz'>=2`.
Each of these two rows already has the two unit ports, and the nonnegative
row-four budget forces `B_zz'=2` and every other entry to be zero.
The `q` row has its known unit at `t`, its unit at `p` from `eta=1`,
and its two units at `z,z'`; the `p` row similarly has only `s,q,z,z'`.
Together with the four inherited core rows, all eight rows in displayed
(7) are therefore exact and saturated inside
`{u,v,s,t,p,q,z,z'}`. The layers prove that these eight vertices are
distinct. This nonempty proper set has no outgoing positive defect entry,
contradicting connected support on 61 vertices.

Thus every actual `S` and `T` parent class in `A[Z]` is independent.
The argument excludes the proposed edge, not the `epsilon=0,eta=1`
parameter choice: that choice retains two nonadjacent points in its
`(q,p)` cell. Without connected support, the displayed symmetric eight
rows form a consistent closed row-four weighted block; this explains
the precise indispensable use of the import and is not presented as an
actual 61-vertex counterexample.

**Consequences in Section 4.** Setting the own-parent count to zero in
the exact color formula proves (9). Triangles through an `S` vertex can
only come from edges between its `K` neighbors and its `Z` class: its
core parent has no neighbors in those two parts, the `T` layer is
independent, and its `Z` class has just been proved independent. Hence
ordinary `S/T` points have no triangles; `q,p` have exactly one each
only in the `epsilon=eta=1` case.

For `y(z)!=p`, the port column is zero and the unique `K` column
neighbor `kappa` differs from `x(z)` by the overlap result. The four
neighbor colors are exactly the four colors outside those two. For
`y(z)=p`, let `phi(z)` be its unique port endpoint. Ordinary members
of `E` have zero port row. If `epsilon=0`, both members of `E` are
ordinary, the own parent is outside `E`, and (9) forces the port endpoint
to differ from that parent. Formula (10) therefore gives `2,1,1`.
If `epsilon=1`, exactly one port has endpoint `q in E`, because that
row sum is one. It has four distinct colors, including the case where
the own parent is `q`; the other four ports have pattern `2,1,1`.
Consequently exactly `5-epsilon` vertices have a repeated `S` neighbor
color. The symmetric reasoning gives the same number for `T` colors.

**Encoding boundary.** The new overlap restriction, zero edges within
every `S/T` parent class, and formulas (1)–(6),(8)–(10) are valid
necessary constraints in the existing seven-type model. All four
`(epsilon,eta)` cases remain. Port variables must still be tied to the
same actual path counts by `c_xz=1+beta_xz`, `c_yz=1+gamma_yz`; isolated
port/count feasibility would not establish a graph. No automorphism,
preferred matching, or restriction on triangles entirely in `Z` was
introduced. This review does not inspect the ensuing implementation or
any new solver result. No substantive mathematical issue was found.

The author also corrected the opening terminology from “adjacency and
defect matchings” to “adjacency interface K and defect matching P”; the
reviewer reread the corrected sentence. This avoids calling K a matching
despite its degree-two row and column. There is no remaining wording issue
or mathematical change from this correction.

## Final coverage delta: selected cases and within-cell order

Read the new final section of `ADJACENT_DOUBLE_FULL_GRAPH_MODEL.md`,
lines 86–122. This is a final mathematical coverage check in the same
reused context, without source-code inspection or execution.

The revised port threshold interpretation is correct on the proved binary
interfaces `S/T`, `S/Z`, and `T/Z`: with `1<=c_xy<=2`, the Boolean
threshold `c_xy>=2` equals `B_xy=c_xy-1`. This is not a replacement of
the global upper bound three; the original core double entries remain.
A positive selector unit picks one of the seven exactly-one cases.
For an exclusion all seven cases must be closed by appropriate actual
evidence; an UNKNOWN case remains open.

Inside a fixed actual `(U,V)` cell, any finite collection of vertices can
be sorted by its pair `(S-parent index,T-parent index)`, with arbitrary
ties. This permutation fixes all non-Z vertices and both parents of every
Z vertex. Relabeling all incident A edges together preserves every proved
constraint, K, and the earlier U-to-S/T defect matchings. Auxiliary values
are assigned from the relabeled actual graph. No S/T relabeling or new
transversal identity is used. Thus every actual graph has a sorted
representative in its selected C type, although not every prior labeled
assignment is retained.

With exactly one S and one T parent per vertex, the proposed clauses are
precisely the lexicographic comparison: 15 binary clauses forbid a decrease
in S index, and `6*15=90` four-literal clauses forbid a decrease in T index
when the S indices agree. These 105 clauses per consecutive cell pair
impose no restriction when S increases, and allow exact ties. Consecutive
nondecrease suffices for the whole cell. All 25 cells are nonempty and
total 35 vertices, hence there are `sum_cells(|cell|-1)=35-25=10`
consecutive pairs. Therefore each selected case correctly adds 1,050
ordering clauses and one positive selector unit.

No mathematical coverage issue was found. This supports the specified
revision; implementation, actual clause emission, preparation and solve
evidence remain outside this review. The review stops after this delta.
