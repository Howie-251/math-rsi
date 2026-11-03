# Center-cycle exclusion: delta proof audit

**Verdict: PASS within the source's explicit connected-repeat assumptions; same-family, provisional.** No proof gap or required source change was found in `proofs/dd82/n62/CONNECTED_REPEAT_CENTER_CYCLE_EXCLUSION.md` (all 196 lines).

Reviewer: `/root/proof_review_n62_triangle_witnesses`; 2026-10-11. This is a delta review by the same reviewer in the context of the preceding triangle-witness review, not a fresh-context or cross-family review. The reviewer did not author the delta. The prior source dependencies and their mathematical checks are reused; no prior audit verdict was used to replace the new derivations. The original four review artifacts are unchanged. Only this Markdown file and its JSON counterpart are added.

## Checked obligations

| ID | Obligation | Discharge |
|---|---|---|
| CC01 | Normalize a center-graph `C4` as two disjoint repeat diamonds with centers `(a,b,x,y)`. | The earlier overlap-cluster theorem puts alternating triangles in the same diamond and the two diamonds in distinct clusters. Center-relation symmetry puts each opposite pair of centers in the other diamond's shared edge. Injectivity supplies its two different endpoints. Swapping the two shared-edge labels in either diamond does not alter any triangle set, so the two choices are independent. Lines 54–82. |
| CC02 | The opposite center rows force both diamond tips `z,w` adjacent in the original graph to both `u,v`. | `N(x)∩N(y)={a,b}` is exact because these are two distinct common neighbors of a unit-repeat pair. Since `u~x` and `v~y`, this forces `u` nonadjacent to `y` and `v` nonadjacent to `x`. At center `a`, row `{b,u,v}` has extra `xy` witness `b`; the other witnesses therefore have forced assignments `u` to `xz` and `v` to `yz`. At center `b`, row `{a,u,v}` forces `u` to `xw` and `v` to `yw`. Lines 86–105. |
| CC03 | These forced incidences exclude the center-graph `C4`. | The distinct `u,v` are two common neighbors of `z,w`; hence `B_zw≥1` from the actual common-neighbor identity, regardless of `A_zw`. The two tips have `B_zw=0`: a positive value would be one by the row budget and close a unit `K4` component, forbidden by connected support on 62 vertices. Lines 107–113. |
| CC04 | Normalize a `P4` as centers `(u,a,x,w)` for path `T_z,T_u,T_w,T_v`. | Endpoint centers belong to their single neighboring triangle and not the other triangle of that diamond, hence are its tips `u,w`. Internal centers lie in the respective shared edges; the shared labels can be chosen independently. This uses the component's missing edges explicitly, and makes no extra symmetry assumption. Lines 117–135. |
| CC05 | Equation (9) gives the entire original induced graph on the eight vertices, with eleven edges. | Four center incidences force nine of the eleven cross edges. Center row `a` adds `yv`; center row `x` adds `zb`. The five cross zeros are `yb` by the exact `xy` common-neighbor pair; `xv,za,wu` by uniqueness of the respective centers; and `zv` because otherwise `u,v` acquire the two common neighbors `y,z` despite `B_uv=0`. The positive repeat pairs are original nonedges; the two tip pairs are also original nonedges because they share `b` and `y`, respectively, and the original graph is triangle-free. Thus there are no omitted within-set edges. Lines 137–167. |
| CC06 | There are two witnesses `p,q` outside all eight vertices, and `p≠q`. | In center `u`'s row, `a,b` are the additional `xy,xz` witnesses, so the third repeat neighbor `p` witnesses `yz`. The matrix gives only center `u` as a common neighbor of `y,z` among the eight vertices, so the additional witness is outside. Similarly `x,y` are the additional `ab,av` witnesses for center `w`, and `q` witnesses `bv`; only `w` already witnesses that pair within the eight vertices. If `p=q`, the established edges `pz,pb,zb` give a forbidden original triangle. Lines 169–181. |
| CC07 | The scope retains possible cross-diamond repeat ports and does not exclude `P4`. | Neither CC05 nor CC06 assumes all cross-diamond repeat entries are zero. In particular `B_zv` may still be zero or one at the level proved here; the other ports at `z,v` were not silently forced outside the eight vertices. The new proof excludes `C4` only and records a necessary `P4` pattern, not a realization or contradiction. Lines 183–196. |

## Boundary and consistency checks

The `C4` witness assignments were checked with the opposite pair of labels swapped; the assignments simply swap and the same duplicated tip witnesses result. No external-port distinctness is needed for the `C4` proof. For `P4`, the two displayed external witnesses are proved distinct by triangle-freeness, rather than being assumed distinct. Possible cross repeats between the remaining tips were retained throughout. The exact common-neighbor assertions use two vertices already proved distinct; they do not repeat the earlier invalid pattern of inferring a two-element set from membership of possibly coincident ports.

A direct arithmetic check of the stated `4×4` matrix returned eleven entries equal to one and these common-neighbor sets *within the eight-vertex pattern*:

```text
T_z: {u};  T_w: {a};  T_u: {x};  T_v: {w}
(x,y): {a,u};  (a,b): {x,w}
(z,w): {b};    (u,v): {y}
(y,z): {u};    (b,v): {w}
```

These finite matrix checks corroborate the derivation and, for the last two pairs, the need for outside witnesses. They are not an actual order-62 graph search or a global realizability test. No solver was run. No counterexample or unresolved delta obligation was found.

The retained necessary center-component list is now `K1,K2,P3,P4`. The `P4` case, the other listed components, and type-zero triangles remain unresolved. No full order-62 exclusion or known-order-63-plus result is claimed. Cross-family acceptance remains for the parent workflow.
