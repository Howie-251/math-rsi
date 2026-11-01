# Shared-capacity refinement: independent audit

The shared \(C_1\) bound, the \(C_4\) codegree bound, their actual-A1 import, and the supplied coefficients are correct. They are now appended as §6 of `proofs/propertyb35/GLOBAL_TWO_FLIP_PATH_REPAIR.md` (the complete file is 287 lines).

## Exact mathematical scope

For outer edges intersecting exactly at \(w\), a valid middle edge must avoid \(w\), because the two attachment vertices must differ. With \(t_w\) counting those outer pairs,

\[
 C_1\le\sum_w(35-d_w)t_w.
\]

The missing quantities \(\binom{d_w}2-t_w\) are nonnegative and sum to \(W-n_1\). The actual A1 spectrum gives

\[
 W=648,\qquad\sum_wd_w\binom{d_w}2=5493,
\]

so \(\sum_wd_wt_w\ge9n_1-339\) and \(C_1\le26n_1+339\). No independent allocation to different outer pairs is assumed.

For a four-intersection outer pair with singleton differences \(u,v\), every middle edge contains both difference vertices. Thus \(c(G,J)\le\lambda_{uv}\). The bound \(C_4\le4n_4\) is proved under the explicit hypothesis \(\max\lambda\le4\).

For the actual reduced A1 role this hypothesis is a valid necessary non-B condition. I read `high_edge_intersection_repair_20261020/REPORT.md` §2 and the saved independent `VERIFY.json`/`RESULT.json`. The full strong-pair ranges are 78/codegree4–7, 79/5–7, 88/5–8, 89/5–8, 99/5–9. All twenty saved bounds are strictly below one. The actual six-degree \(x\) already has only codegree one or two, and the seven-degree \(p\) is unique; hence there is no missing 77 type. This justifies **global** \(\max\lambda\le4\), rather than merely a restriction on one selected kernel.

This import uses the full reduced-A1 roles, not solely its degree multiset. The canonical statement keeps the explicit maximum-codegree assumption on the standalone arithmetic corollary and states the actual-role bridge separately. The existing independent original-edge certificate replay was inspected, not rerun here.

## Resulting necessary structure

The resulting sufficient criterion is

\[
 L'=594n_0+4992n_1+3960n_2+6336n_3+3432n_4+20340<2722720.
\]

The constant 20340 is retained. With the A1 moment identities,

\[
 L'=2463474+8838n_3+17826n_4-5430\tau.
\]

Thus any non-B reduced-A1 input requires

\[
 8838n_3+17826n_4-5430\tau\ge259246,
\]

which is equivalent to \(\ge259248\) by divisibility by six. It forces \(n_3+n_4\ge15\); the pure cases give \(n_4=0\Rightarrow n_3\ge30\) and \(n_3=0\Rightarrow n_4\ge15\). The weighted condition retains all mixed cases.

The imported report's separate complete repair also shows that every remaining four-intersection kernel avoids \(x,p\). This extra fact is recorded as part of the genuine remaining structure, without asserting any corresponding exclusion for arbitrary three-intersection kernels.

## Evidence and stopping boundary

Run:

```sh
.tools/math-python/bin/python context/propertyb35-paper/round01/middle/global_private_pair_moments_20261020/two_flip_path_20261020/shared_capacity_20261020/CHECK.py
```

Actual result: PASS, approximately 0.0097 CPU seconds. The script checks all degree moments and coefficients, the twenty saved pair-gate ranges/strict bounds, and the already available rational maximum-\(n_1\) PSD witness. It does not repeat the older fixed-certificate calculation.

That old abstract witness \((17,1664/3,0,0,70/3)\) still gives \(L'=2879414\ge2722720\), with all six PSD forms nonnegative. Therefore the strengthened shared-capacity inequality has not contradicted the edge-intersection moment/PSD relaxation. It is not claimed to be realized by an H. No new LP or distribution search was performed.

Review scope is separate: the newly reported Gemini SUCCESS covered the earlier canonical §§1–5 (then lines1–186), including the original two-flip algorithm and coarse capacities, and did not execute code. The present §6/shared-capacity appendix was added afterwards and has no cross-family acceptance recorded in this task. Parent-agent review remains responsible for its promotion.

No H search, extra local inventory, Lean, MCP, wiki or navigation change was performed.
