# Reused-reviewer delta: two internal-path exclusions

Date: 2026-10-13. **PASS modulo the explicitly inherited imports and the
reviewed local template.** Both new deductions are sound as stated.
No mathematical issue or required proof correction was found.

This is an **explicitly reused**, same-family, provisional review by
`/root/internal_path_proof_check`, following that agent's completed fresh
review of the original two internal-path notes. It is not a new fresh
review, external acceptance, solver result or formal theorem. The parent
confirmed the requested agent configuration as `gpt-6-astra` / `ultra`;
there is no independent backend attestation. The original `PROOF_AUDIT`
and `PROOF_CHECK_STATE` retain exactly their original two-input scope.

## Input, assumptions and provenance

New primary input, read directly in full after author stability was
communicated by the delegated author:
`proofs/dd82/n61/INTERNAL_DOUBLE_ENDPOINT_ADJACENCY_EXCLUSION.md`,
lines 1–156. No manuscript was edited by this reviewer.

The hypotheses are the same actual simple 8-regular order61 graph,
diameter at most two, actual `B=A^2+A-7I-J`, and consecutive `u,v,w`
in the inherited double-defect path forest. The new manuscript imports
the exact local partition, complete middle row, actual commutation,
`B[T]=K_3[U]+K_3[W]`, parent sizes and ordinary-vertex rule from
`INTERNAL_DOUBLE_PATH_LOCAL.md`. Each application below discharges
those hypotheses within that same original A.

The local note's 24-obligation fresh review, the precise sources
`CONNECTED_TRIPLE_EXCLUSION.md` and `DOUBLE_DEFECT_CYCLE_OBSTRUCTION.md`,
and the previously saved local/Gemini import-status records are recorded
in `PROOF_AUDIT.md` and `PROOF_AUDIT.json`. All remain inherited;
no previous proof, solver, enumeration or certificate was rerun. No new
external call, graph search, formalization, rendering or digest was made.

The draft's lines 25–26 and 155 refer to a pending fresh checker. The
actual receipt here is only the expressly authorized reused-reviewer
delta. That pending-status wording does not supply fresh acceptance.

## Frozen delta obligations

| ID | Required conclusion | Hypotheses and justification |
|---|---|---|
| D01 | If `A_uw=1`, then `B_uw=B[u,Z]=B[w,Z]=0` | Local commutation supplies two units in T; existing double to v supplies two more; disjoint sets and nonnegative row-four budget |
| D02 | Under that assumption, `U intersect W=P intersect Q=empty` and `|P|=|Q|=4` | Actual `mu(u,w)=1+B_uw-A_uw=0`; endpoint degree eight and complete neighborhood partition |
| D03 | For every `z in Z_t`, both equations (3) hold | Partition actual common neighbors with u and w; use D01 and unique parent t |
| D04 | All P,Q attachments lie in the two neutral size-seven classes | For attached z, `p_z+q_z=1`; nonnegative D03 counts forbid parents in U or W |
| D05 | At least one ordinary neutral vertex exists and forces a contradiction | Exactly `14-8=6` such vertices; D03 needs one P and one Q neighbor while the ordinary rule allows only one neighbor in the two neutral classes |
| D06 | `A_uw=0` for every consecutive triple, hence `a_2=0` | D05 contradicts the only other binary adjacency value; the triple was arbitrary |
| D07 | `r>0` and `h>0` are incompatible | For t in U intersection W, `B[T]` already exhausts all four row units; a z in P intersection Q has the two distinct common neighbors u,w, forcing `B_tz>=1` |
| D08 | Exactly four earlier necessary types remain unexcluded by these deductions | Set epsilon zero and apply `rh=0` to the complete six-row table and `r+h=1+beta` |

All eight obligations are discharged. Their acyclic dependencies are
`local template -> D01 -> D02 -> D03 -> D04 -> D05 -> D06`, and
`local template -> D07`; `D06+D07+six-type table -> D08`.
There are no new analytic limits, probability modes or asymptotic claims.

## Counterexample-first probes

- **Uncounted defect port:** The two T units are distinct from the
  double entry at v. They exhaust the full endpoint row, so there is
  no residual port at w or any z. This is an actual budget identity,
  not a guessed zero block.
- **Overlapping attachment sets:** In the epsilon-one branch, any
  member of P intersection Q is a common neighbor of u,w, contradicting
  their derived zero common-neighbor count. Disjointness precedes its
  use in every later equation.
- **No ordinary neutral vertex, or all such vertices in one class:**
  The neutral union has 14 vertices and P union Q has exactly eight,
  so six remain. It is unnecessary for both neutral classes to contain
  one: the two equations are symmetric under naming a and b.
- **Self-incidence in an attachment count:** `d_P(z)` counts actual
  neighbors in P. If z belongs to P, its own diagonal contribution is
  zero by simplicity, and the common-neighbor decomposition still holds.
- **An A edge between t and the common attachment z:** The second proof
  does not assume `A_tz=0`; the lower bound is `B_tz=mu+A_tz-1>=1`.
  If they are adjacent the contradiction is only stronger.
- **Overlapping U,W clique edges:** The local identity is a weighted
  sum. A vertex in both sets receives two row units from each triangle,
  even if an edge is counted twice, so its T-row weight is still four.
- **Dropping a remaining beta-one type:** `r=0,h=2` and `r=2,h=0`
  obey `rh=0` and remain. No other new exclusion follows from D07.

These are exact analytic probes. No valid counterexample to a stated
claim was found; the positive judgment rests on the deductions below.

## Complete delta derivation check

Assume epsilon is one. The local `(v,u)` and `(v,w)` commutation
equations give defect sums two into T from each endpoint. Together
with their respective double edges to v, this accounts for all four
units. Nonnegativity and the disjoint partition give equation (1).
Consequently `mu(u,w)=0`, so U,W and P,Q are pairwise disjoint in the
stated manner. Each endpoint has the other endpoint, three T neighbors
and four Z neighbors. This proves D01–D02.

For z in `Z_t`, all common neighbors with u lie in the disjoint pieces
`{w}`, U, P of the actual endpoint neighborhood. Their contributions
are respectively `q_z`, `1[t in U]` and `d_P(z)`. Since `B_uz=0`,
their sum is `1-p_z`. The w equation is symmetric. Solving gives
the two identities in (3), proving D03 without any independent
incidence-array assumption.

For z in the union of attachment sets, `p_z+q_z=1`. If its parent
were in U or W, one count in (3) would be negative. Thus attachments
all lie over neutral parents. Since U,W are disjoint triples in an
eight-element T, there are exactly two neutral parents; each parent
class has size seven. Hence their union has 14 vertices, containing
exactly eight attachments and six ordinary vertices. This proves D04
and the existence part of D05.

Take any ordinary neutral vertex z, naming its parent a and the other
neutral parent b. Equation (3) gives one P neighbor and one Q neighbor.
They are distinct because P and Q are disjoint. Both lie in the union
of the two neutral classes. But the previously proved ordinary rule
allows no neighbor in `Z_a` and exactly one in `Z_b`. Thus two is at
most one, a contradiction. No uniform rule was applied to an attachment
vertex. This closes D05, excludes epsilon one, and proves D06 globally
for every internal triple. The Toeplitz interpretation `a_2=0` follows
for every path with at least three vertices.

For D07, take `t in U intersect W` and `z in P intersect Q` if both
exist. They are distinct because T and Z are disjoint. The weighted
triangle identity contributes two plus two units to row t within T,
so its row-four budget forces `B_tz=0`. However, u and w are two
distinct original common neighbors of t,z; the actual defect identity
therefore gives `B_tz>=2+0-1=1`. This contradiction establishes `rh=0`
without requiring the first exclusion or deciding the parent of z.

Finally with epsilon zero, beta zero requires `r+h=1`, allowing
`(r,h)=(0,1),(1,0)`. Beta one requires `r+h=2`; `rh=0` allows
`(0,2),(2,0)` and excludes `(1,1)`. Thus exactly the two specified
rows of the earlier necessary list are removed. The word "exactly"
refers to rows excluded by these deductions, not to realizability of
the remaining rows. This proves D08.

## Verdict boundary

The two new conclusions are `A_uw=0` for every consecutive D triple
and `rh=0`. Equivalently, `a_2=0` on every sufficiently long D path,
and the surviving tuples are
`(r,h,beta)=(0,1,0),(1,0,0),(0,2,1),(2,0,1)`.
Combining with the earlier followup confines the beta-one tuples to
three-vertex components; that implication reuses the already reviewed
component confinement lemma.

No theorem here excludes all internal D vertices, isolated adjacent
double edges, the four surviving local types, or order61. The shared
actual A remains essential. There are zero open mathematical issues,
zero fixes, and no change to the inherited global existence range.
This is a separate reused provisional delta, not part of the original
fresh verdict and not a fresh or external acceptance receipt.

## Second reused increment: one common attachment at most

The initial two-claim receipt above is preserved as historical scope.
After a further author-stability message, the revised same manuscript
was read directly in full, now lines 1–176 and titled "Three exclusions
for an internal double-path vertex". Its earlier two proofs have no
mathematical change. The new substantive content is section5, lines
146–164, adding `h<=1` and updating the final list to three types.
This is another **explicitly reused, same-family, provisional** increment;
it does not change the freshness status of either receipt.

Two further obligations are frozen for this increment:

- **D09:** A shared attachment z has `sum_{t in T} B_tz=4`, so the
  entire symmetric nonnegative row-four defect row is supported in T.
  If a second distinct shared attachment z' exists, `B_zz'=0` and
  `B_zz'>=1` follow simultaneously. Therefore `h<=1`.
- **D10:** Combining D09 with D06–D08 removes the prior remaining
  tuple `(r,h,beta)=(0,2,1)` and leaves exactly
  `(0,1,0),(1,0,0),(2,0,1)` as necessary types.

Counterexample probes: taking `z=z'` would invalidate a distinct-pair
identity, but `h>=2` explicitly supplies two distinct elements. A
possibly adjacent z,z' pair is retained: `A_zz'>=0` suffices and an
edge only strengthens the defect lower bound. The symmetry conversion
from the column sum over T to the complete row sum is explicit. The
defect saturation argument also explicitly uses `z' in Z`, disjoint
from T, so no possible shared-parent location is silently fixed.

The derivation is complete. A shared attachment satisfies
`A_uz=A_wz=1`; the already checked local commutation formula therefore
gives the stated sum four. Symmetry, nonnegativity and total row sum
four force every defect entry from z to Z to be zero. A second shared
attachment z' has the distinct common original neighbors u and w,
so the actual identity instead gives
`B_zz'=mu(z,z')+A_zz'-1>=2+0-1=1`. This is a contradiction independent
of whether the first two exclusions were applied. Hence D09 holds.
Applying `h<=1` to the four-row intermediate list removes only
`(0,2,1)`, establishing D10 and the final three-row list.

**Second-increment verdict: PASS**, with two of two added obligations
discharged and no issue. Cumulatively this delta covers three new
claims through ten discharged obligations. The first two-claim receipt
remains recorded above; only its four-survivor list is superseded for
the revised manuscript. The beta-one tuple `(2,0,1)` remains allowed
by these deductions and is confined to three-vertex D components by
the original followup. No internal-double or order61 exclusion follows.
The draft still describes a pending fresh checker; these actual
increment receipts are reused and provisional, not fresh or external.
