# Final direct port consequences for the two open internal-double cases

Status: pure consequences of the reviewed h=0 theorem and reviewed r2 port classification. Root check and explicit reused local delta PASS are saved in DELTA_COMMON_ATTACHMENT_INTEGRATION.md/.json. Both refined inputs were actually prepared and solved once; both UNKNOWN. Actual Gemini round4 accepted the corollary, source and outcomes; raw record reviews/dd82/20261013_V3_n61_internal_final_results_review.json.

## Double endpoint ports must have a parent adjacent to that endpoint

Use the full internal-double template, T=N(v), U=T intersect N(u), W=T intersect N(w), and each z in Z has exactly one T-neighbor t(z). The computation-assisted h=0 theorem applies to EVERY consecutive D triple in every target graph.

If B_uz=2, u has precisely the two double neighbors v,z, because B_uv=2 and its B row sum is four. Thus v,u,z is a consecutive D-path triple. Its h=0 inclusion says N(v) intersect N(z) subset N(u). The left side is exactly {t(z)}, so t(z) belongs to U. Likewise B_wz=2 implies t(z) belongs to W.

Therefore force [B_uz>=2]=false for each z whose parent is not in U, and the analogous W constraint. This is a necessary condition for every actual target, not an assumed endpoint choice or selected D-path length. In the r1_h0_b0 type each endpoint excludes33 parent positions, giving66 pre-simplification negative literals on existing exact second-threshold bits. Bool-false bits contribute no clause. The r2 endpoint residual row budget is only one, so the same condition is already automatic there.

This consequence depends on the checked r0 input through universal h=0. It is not justified by the previously encoded h=0 condition for the selected u,v,w triple alone.

## Couple the two unit endpoint ports in r2

For r2_h0_b1, write U={a,b,c}, W={a,b,d}, q0 in Q intersect Z_c and p0 in P intersect Z_d. The already proved INTERNAL_DOUBLE_SHARED_TWO_PORTS.md gives exactly these ordered allowed pairs (x,y):
- (q0,p0);
- O_c times O_d;
- O_d times O_c.

Each endpoint domain already has eleven members and each has exactly one unit port. There are51 allowed pairs and70 forbidden pairs out of121. For each forbidden pair add the binary clause not[B_ux>=1] or not[B_wy>=1]. All bits already equal the actual same-A entry thresholds. No new free variable, independently chosen matching or port subcase is introduced. All3 necessary configurations remain represented.

## Execution scope

These are explicit new clauses on the previous complete r1/r2 inputs. Preserve those bodies and all source/input/result records; use a separate refined directory. Neither old UNKNOWN is an exclusion or a reason for an unchanged cold start. One new bounded profile of each changed input would test these actual consequences. No h1 recomputation is needed; its complete checked contradiction is inherited. The main internal-D branch and whole61 remain open until appropriate actual evidence.



Actual refined results: r1 has33296variables103669clauses and returned UNKNOWN after57.788672CPU seconds; r2 has27886variables86661clauses and returned UNKNOWN after56.218533CPU seconds. All old body lines and added Boolean conditions checked during preparation, no newvariables. These outcomes do not exclude either remaining type. See internal_double_full61_run/all_results.json for allfive terminal profiles.
