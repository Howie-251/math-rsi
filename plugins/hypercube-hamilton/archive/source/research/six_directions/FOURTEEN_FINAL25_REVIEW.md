# Independent review of the frozen final25 package

Verdict: **PASS**, for the exact final25 representative theorems and their application to the accepted source residual. Reviewer `/root/final25_audit_resume`, 2026-11-02, using the ARIS proof-checker skill at `F:/c4free-hypercube-main/ARIS/skills/skills-codex/proof-checker/SKILL.md`. Review independence is **same-family** and semantic acceptance is **provisional**. This is a complete finite-certificate and mathematical review of the stated scope; it is not Lean verification or cross-family acceptance. No mathematical issues remain open.

The frozen producer proof and application are `FOURTEEN_FINAL25_PROOF.md` and `FOURTEEN_FINAL25_APPLICATION.md`. All 132 input hashes of `FOURTEEN_FINAL25_MANIFEST.json` were freshly verified. Neither producer code nor producer replay output served as an acceptance oracle. Only new `FOURTEEN_FINAL25_REVIEW*` artifacts were written. No applicable workspace AGENTS.md was found in the ancestor paths checked.

## Exact dependencies and quantified conclusion

The source gate is the final PASS `FOURTEEN_MID_SELECTED_REVIEW.json`, SHA256 `e3a1867319318a41197835aa260e02b184bbe354dca2c1f88faa328ccf1ed0b6`. Its direct audited, imported and checker bindings were rehashed. Its covered residual is exactly 0/0/25 at targets 1/7/31. Its free-target closure is inherited by that source gate; this review's new work is exactly the covered final25 subset.

The local theorem import is `HIGHER_FORCED_CHERRY_REVIEW.json`, SHA256 `14a097a78df2708f03edaf5284e78e7c1178b2332c800830b23bb16f14463231`, together with Section 5 of `HIGHER_FORCED_CHERRY_TRANSFER.md`. Its recorded direct bindings were rehashed. The accepted general complete-graph GF(2) matching-connectivity upper bound applies at every even size, hence at 20 terminals with upper bound 512. This imports the complete mathematical theorem, not a small-size experiment, a bipartite restriction, or merely the older 22-terminal numerical instance. The argument uses selected rank-512 rows plus that upper bound to span the full connectivity row space. Every arbitrary perfect-matching column is nonzero by cyclic joining of its matching edges, so some selected row connects it. There is no sampling inference.

For each of the two stated uncovered sets, **every original short matching M** with that exact uncovered set extends to a Hamilton path from 0 to 31. Realizability of every possible uncovered geometry is unnecessary: this is an implication quantified over all realizing matchings. The exact source records have 20 and 5 simultaneous-coordinate images of these representatives. No full fourteen-hole assembly, predecessor chain, or full P6 is concluded in this package.

Dependency DAG: frozen accepted residual -> exact source record/maps; new B positive forests + general connectivity rank upper bound -> universal exact B criterion; complete maximal-A positive domain -> forest for any maximal extension; monotone actual-submatching lift -> actual A transfer; actual B suppression and obstruction avoidance -> B criterion -> expanded 62-cycle -> Hamilton endpoint splice. There is no edge from a full14/P6 conclusion back into any premise.

## Complete independent finite verification

`FOURTEEN_FINAL25_REVIEW_local.py` reuses the already independent STAR local checker's graph/rank algorithm, inspected before reuse. Its configuration comparison was adapted to this package's minority-then-majority serialization. It does not execute a producer module. For all five exact rows, it checks every physical short forest edge, no duplicate edges, no labelled cycles, every vertex degree, every path component, the full and reduced endpoint pairings, the unique forced cherry from its two available cube neighbors, and every supplied complete-matching column. It recomputes all connectivity entries by graph connectivity and independently eliminates the resulting rows over GF(2). Supplied pivot/combo equations are checked additionally; they are not used as a rank oracle.

| row | full/reduced endpoints | forests | recomputed bits | independent rank |
|---|---:|---:|---:|---:|
|0|22/20|512|262144|512|
|1|22/20|512|262144|512|
|7|22/20|512|262144|512|
|100|22/20|512|262144|512|
|101|22/20|512|262144|512|

Total: **2560 forests and 1310720 connectivity bits**, all checked, with all pivot equations verified. Universal cherry forcing follows because its internal hole has degree two and only those two available short neighbors; selected-forest occurrence alone was not substituted for universal forcing. For a single forced pair, the contraction criterion is exactly absence of that pair in the actual arbitrary complete matching.

`FOURTEEN_FINAL25_REVIEW_A.cpp` implements the independent maximal-domain method used by earlier STAR/MAXIMAL_A reviewers, with fresh domain definitions for these two orbits. It partitions by the exact unmatched odd subset disjoint from T, counts injective short mates by a 15-bit even-used-mask DP, and requires every neighbor of every unmatched odd vertex to be used. This last condition is equivalent to inclusion maximality. Orbit1 additionally requires bit30 in the used-even mask. Thus the count includes every legal maximal matching, without a cardinality cutoff or producer DFS dependence.

| orbit | size8 | size9 | size10 | size11 | total |
|---|---:|---:|---:|---:|---:|
|0|12|17040|274691|0|291743|
|1|0|804|100020|412439|513263|

All **805006** supplied records were checked: framing/padding, sorted legal short edges, disjointness, exact bipartition, mandatory T coverage, mandatory internal30 in orbit1, maximality, free even q, t in T, distinct unit w/b, the actual physical transformed positive opening forest and qt edge, and labelled acyclicity of P+Lstarprime. Common physical edges cause a failed DSU insertion and are rejected. Every exact endpoint set and its parity balance was verified, including target-unmatched maximal records. The chosen B geometry and protected pair were checked against a common-map registry generated from the five independently checked B inputs. Matching partner codes are unique. Equality of the legal unique certificate histograms with the independent DP histograms proves exhaustion, not merely the advertised count.

Maximal target flags are unmatched/matched = **10938/280805** in orbit0 and **45396/467867** in orbit1. These flags describe Lstar only, and never decide whether the actual original target is internally matched. Certified B uses counted by the checker are 291065/549/129 for rows0/1/7, and 510611/2652 for rows100/101.

`FOURTEEN_FINAL25_REVIEW_prepare.py` verifies all **456** supplied simultaneous options, including both the A permutation convention and the one common B permutation acting on minority holes, majority holes, omissions and the actual forced pair. The canonical orbit1 minority pair is {0,15}; its actual source pair {0,30} is mapped along with all other data. No cardinality-only identification is used. It checks all25 source indices and supplied actual-to-representative maps, fixing 0,31 and bit32. It also reconstructs membership independently across all120 coordinate maps and verifies exact ordered byte complements.

| target | accepted source | positive | remaining |
|---|---:|---:|---:|
|1|0|0|0|
|7|0|0|0|
|31|25|25|0|

The source hit counts are **20+5**. All three final remaining streams are literally empty. Their common SHA256 is `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

## Mathematical obligations and adversarial checks

1. **Actual internal restrictions.** The mirrors of T are original holes Z, so actual short matching edges at T must be internal A. In orbit1, the mirror of30 is the original hole62, so actual30 is internally covered as well. Extending the actual L by only new disjoint short edges preserves these mandatory coverages and terminates at an inclusion-maximal matching in exactly the counted graph. No maximum-cardinality assumption is made.

2. **Three target cases and inclusion.** If the actual target edge31h is internal, it belongs to L and therefore Lstar, with the same mate h; replacing it by wh in both gives Lprime subset Lstarprime. If actual31 is crossing and Lstar leaves31 unmatched, Lprime=L subset Lstar=Lstarprime. If actual31 is crossing and the maximal extension adds31hstar, that edge was not in L; deleting it and inserting whstar preserves every edge of L, so again Lprime subset Lstarprime. In both crossing cases the actual auxiliary edge is w63. In the third case whstar is a new completion edge, not the original target edge. Attempting to substitute the maximal target mate for actual63 is exactly the forbidden incorrect variant and is absent from this proof.

3. **Domain and endpoint accounting.** The new covered domain is Gprime=(E union O) minus31 plus w. The positive A forest has degree2 at q,b and degree1 at every other vertex of A minus{0,31}. After adding Lstarprime, q and b are internal. The endpoints are exactly (Xstarprime minus q) union S; there are 14-mstar of each parity and at least three components. The independent physical checker confirms this identity for every record, including the maximal-target-unmatched boundary.

4. **Completion existence.** Equal even/odd endpoint counts imply that the number of same-even paths equals that of same-odd paths. If nonzero, alternate these path types in a ring; each connection joins opposite parities. Insert any mixed paths into ring connections, orienting their endpoints to match. If all paths are mixed, orient them consistently and join cyclically. There are at least three components, excluding a degeneracy involving a single doubled component. These complete endpoint edges may be long, which is permitted because all will be deleted.

5. **Monotone lift.** Put D=Dstar union(Lstarprime minus Lprime). New maximal matching edges have distinct endpoints unmatched by Lprime; Dstar uses only unmatched vertices of Lstarprime and S, disjoint from those added matching endpoints. Thus D is a matching with precisely (Xprime minus q) union S as its domain. The equality P+Lprime+D=P+Lstarprime+Dstar is an equality of labelled edge multisets, yielding the same simple30-cycle. Its size is 14-|L|. Actual t is covered by L, hence D avoids t; q is also excluded. In the actualcross/maxmatched case whstar lies in D and is deleted. This proves the lift for every actual submatching, not only the enumerated maximal representatives.

6. **Cutting and attachments.** Deleting all D edges and qt from the30-cycle makes paths. Each unmatched-domain port except q loses its D edge and receives its original/virtual cross attachment. The free q loses qt and opens its actual crossing. The covered t loses qt and gets the new bridge to its original B hole. Sources S lose D and get source bridges. If cutting adjacent edges isolates t, its actual internal L edge would have been deleted, which cannot happen because t is outside D; no unaccounted degree-zero A component arises. Original matching crossings, source bridges, and t bridge have distinct B endpoints. In crossing-target cases w is an actual virtual port and w63 is kept. Local label31 for63 is distinct from units, T, S and minority holes.

7. **Actual B suppression.** Only Y=bar(S) has degree2 when transferred path-pairing edges are combined with original internal-B matching. Each y has an actual internal mate because its mirror was an A hole; y is originally covered since S avoids T and minority mirrors. All Y have the same parity and their original short edges leave Y. A cycle would need every vertex to lie in Y, but no original matching edge can stay within Y. Equivalently, these are paths with pendant original mates. Suppression gives a genuine complete matching on exactly the22 vertices outside the claimed new hole set. Its edges may be long or same-parity; the local criterion expressly admits all complete matchings.

8. **Actual forbidden-pair safety.** The unit mirrors of w,b were originally internally B-covered because w,b were original A holes. They are not transferred boundary endpoints, Y, original holes, or63. Each retains its original short matching edge; the opposite-parity other endpoint is outside Y, so suppression cannot alter it. Therefore their same-parity pair is absent from the actual compressed matching for every original M. This checks the actual F_B, not merely the original internal-B restriction. The proposed counterexample of a virtual target port colliding with a unit mirror fails because63 has local label31, not a unit.

9. **Expansion and final splice.** The universal B criterion now applies. Its short forest and actual compressed matching form one cycle. Suppressed Y interiors and transferred A interiors are disjoint, so expansion gives a single62-cycle on Q6 minus{0,31}, containing all modified original edges and the actual auxiliary edge. In the internal case that edge is wh; in the crossing case it is w63. Delete it, add the short0w, and restore the actual original h31. Endpoints are precisely0 and31, every original M edge is restored, and all remaining nonoriginal edges are short. Maximal-extension and completion edges were already deleted.

10. **Boundary and scope checks.** The largest maximal size11 gives exactly three balanced path components, still sufficient for completion. Empty source streams at1 and7 and both maximal target flags are included. Shared physical P/L edges are rejected as labelled two-cycles, not silently deduplicated. A B matching containing the forced pair is properly excluded, rather than inferred safe from parity of arbitrary compressed edges. No analytic interchange, asymptotic estimate, limit, probability mode or uniformity premise occurs.

All theorem applications discharge their explicit hypotheses in these obligations. The rank theorem is the sole nonfinite mathematical rank import; all new geometric positive premises are exhaustively checked rather than inherited by size or type. The accepted final25 application is complete conditional on the bound source gate. Full fourteen-hole assembly must independently bind its entire upstream chain and free branches. Full P6 remains outside this review.
