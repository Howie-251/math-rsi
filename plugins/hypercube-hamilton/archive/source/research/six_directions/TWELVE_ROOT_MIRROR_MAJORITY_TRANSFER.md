# Root-mirror majority-endpoint transfer (new proof-writer candidate)

2026-11-01. Author: `/root/higher_forced_cherry_review` now acting as proof-writer, not as reviewer of this new result. Status: **PROVABLE AS STATED relative to the accepted Q5 inputs, pending a fresh independent proof review.** No application census or Q6 layer closure is asserted. This file is not an acceptance gate and changes no ledger.

## 1. Imported inputs

Use the accepted all-feasible Q5 imbalance-two avoid-one theorem A_(2t): for arbitrary complete-graph matching F with hole counts (t-1,t+1), every specified majority hole may be omitted from a cycle containing F, with only short new edges. Use the accepted all-balanced Q5 cycle theorem for arbitrary complete-graph matchings. Their exact accepted package is `Q5_A10_FULL_REVIEW.json` and the consequences of `Q5_HIGHER_HOLE_REDUCTION.md`. Parity may be reversed under face coordinates.

## 2. New derived Q5 endpoint interface

**Lemma.** Let F be any matching of K(Q5), with a holes of parity E and a+2 holes of parity O. Let r be a free O vertex and v a distinct O target, covered or free. Then F has a Hamilton r--v path on all 32 vertices, and every path edge outside F is short.

**Proof, covered target.** Put h=F(v) and F'=(F minus {vh}) union {rh}. Because r is free and distinct from v, h differs from both, and F' is a matching. Its holes replace r by v, which have the same parity; hence its hole counts are still (a,a+2), and v is a majority hole. The accepted avoid-v theorem gives a simple cycle on Q5 minus v through F', with all edges outside F' short. Delete its required edge rh, producing a spanning h--r path on Q5 minus v, and add the original required edge hv. The result is a Hamilton v--r path through all original F edges. The auxiliary rh disappears, so every new surviving edge is short. No restriction on h or the parity/length of rh was required.

**Proof, free target.** Add the possibly long same-parity edge rv to F. Both majority holes disappear; the new matching has balanced hole counts (a,a). Apply the accepted balanced cycle theorem and delete rv. This gives the claimed Hamilton path and removes the only added nonshort auxiliary edge. Feasibility is inherited from the actual matching; a may be zero, in which case the cycle import is its accepted perfect-matching case. The lemma does not address r=v.

## 3. General root-mirror-omitted transfer

Let M be an original short matching of Q6 with holes H={u} union Z union W, where u is even/free, Z consists of k-1 even holes and W of k odd holes. Assume Z union W independent. Fix an odd target v, free or covered. Choose a coordinate cut A,B with v in A and u in B. Suppose the mirror r=bar(u) belongs to W intersect A and differs from v. Put a=|Z intersect A| and b=|W intersect A|, and assume b-a>=2. Set s=b-a-2. Choose s sources S from (W intersect A) minus {r,v}, and Y={bar(x):x in S}.

The source set exists automatically under these hypotheses: at most two of b vertices are excluded and s=b-a-2<=b-2. For a covered target v, only r can be excluded from W. The theorem is also valid with any explicitly chosen legal S.

Let the actual B hole set be H_*=(H intersect B) union Y, and let U={u} union Y. All members of U have global even parity. Assume the actual marked local geometry has a universal cycle-extension theorem on exactly B minus U for every arbitrary perfect matching L on B minus H_*, with only short new edges outside L. Then M has a Hamilton u--v extension with only short new edges.

Its B hole counts, in global (even,odd) order, are (k-a+s,k-b), and it omits exactly s+1 even majority holes U. This has the same hole counts and omission count as the old odd-consumption row using s+1 sources, but a **different marked omission set**: the global root is now one of the omissions, not a covered terminal.

**Proof.** Let C be the original crossing matching, c=|C|, and X_A,X_B its ports. Internal shortness gives |X_A intersect E|-|X_A intersect O|=b-a=s+2, since u is in B. Thus c>=s+2>0. Also c is congruent to a+b modulo 2, and c+s is even. The source vertices are originally free and disjoint from X_A, and r is neither a port nor a source.

Pair all vertices of X_A union S arbitrarily into an artificial matching D. Its size is d=(c+s)/2>=s+1>=1. All its endpoints are free for M_A and exclude r and a free v. The completed matching M_A+D has exactly a even and a+2 odd holes: the ports are covered, precisely the s chosen odd holes are covered, and r stays an odd free hole. Apply the lemma of Section 2 to obtain a simple Hamilton r--v path P_A through M_A+D. Required D edges may be arbitrary, as allowed by the lemma. All other new local edges are short.

Add the short bridge ru and tagged edge uv. The two endpoints r,v of P_A are distinct, and u is outside A, so Q=P_A+ru+uv is a simple cycle on A union {u}. Delete all D edges. Since d>=1, Q-D is a forest. Attach every original crossing edge and every selected source bridge x--bar(x). Their B endpoints lie in X_B union Y and are distinct from each other and u. They merely attach distinct B leaves, so the graph remains a forest.

Every A vertex now has degree two. At a port or source the deleted D incidence is restored by its attachment; at r the bridge ru restores the endpoint degree; at v the tag restores it. If a covered target v is a port and D deletion isolates it in the A path, the crossing plus tag restore degree two, so the degree calculation includes that boundary. The root u has degree two, supplied by ru and uv. Every vertex in X_B union Y has degree one. Thus all components are paths with B leaf endpoints. Compress all A vertices **and u** as internal vertices of these paths, retaining path data and the tag. This gives a perfect matching T on X_B union Y; one path contains u and the tag. This differs from the old transfer, in which u was a terminal of T.

Every y in Y is originally internally covered in B. Its free mirror excludes a crossing port; nonroot independence excludes an original nonroot hole; y differs from u because r was excluded from S. Its distinct original short mate h_y is odd, outside Y, ports and the originally free root. Hence T+M_B has only the usual pendant path conflicts at Y, and no conflict cycle. Suppress Y and keep all physical path data. The resulting perfect matching L has hole set precisely H_*=(H intersect B) union Y; u is still a hole of this local matching because it was compressed as an interior vertex and had no original M_B edge.

Apply the assumed marked B theorem to the actual L, obtaining a simple cycle on B minus U. Its interiors omit both Y and u. Expanding recorded paths restores all A vertices, u and Y exactly once. The result is a tagged spanning Q6 cycle containing every original edge of M. Delete uv. D and auxiliary compressed edges have disappeared; all surviving new edges are short local edges, crossings, selected bridges, or ru. The prescribed endpoints are u and v. This proves the conditional transfer for every realizing original M.

## 4. Forced-pair version (positive s)

Under Section 3's hypotheses additionally let s>=1. Suppose the actual local marked B geometry has a classification through arbitrary L iff the labeled union L+R is acyclic, where R is a matching of covered vertices all having parity U (even). Then the Hamilton u--v extension exists. In particular this applies to a single forced cherry if its actual obstruction is among covered B terminals.

**Proof.** Root u is omitted, so no R endpoint is u. Let J_B be all R pairs whose two endpoints are original B ports, with j=|J_B|, and J_A their actual original crossing partners. Every J_A endpoint lies in X_A and thus in the completion domain X_A union S; the local root r is a free hole and cannot be a port. Prescribe J_A subset D and pair the rest arbitrarily. Since R is a matching, j<=floor(c/2). Since c+s is even and s>=1, d=(c+s)/2>floor(c/2)>=j.

As in Section 3, suppressing Y moves a T endpoint to its opposite-parity original mate h_y. Original internal matching edges are short and join opposite parities. Therefore any L edge wholly within V(R) must be an unchanged T edge between two ports. Any cycle of L+R lies in T+J_B. Lifting its T paths and restoring the corresponding J_A pairs gives a cycle in Q minus (D minus J_A), where Q=P_A+ru+uv is the simple cycle on A union {u}. Lifted paths have disjoint interiors; u is one such possible interior vertex, not a junction or terminal. The strict gap d>j leaves at least one deleted Q edge, so that graph is a forest, contradiction. Thus L+R is acyclic and the local classification applies. Expansion is the same as in Section 3.

The case s=0 is covered by the unconditional Section 3 theorem but is not included in this forced-pair argument: d=c/2 and j=d could remove the spare gap. No unstated gap assumption is hidden.

## 5. New obligations and scope

This file proves a conditional construction, not that any remaining actual geometry has a useful cut or an accepted local marked input. The B omissions must be looked up as Y union {u}, never as the old all-mirror omission set. A new application scan should try cuts with u in B, bar(u) an A hole, b-a>=2 and bar(u) not v; choose s=b-a-2 sources; then test only actually accepted local geometries with the transformed U including u. For forced classifications, use s>=1 and preserve the actual R under the same map.

The new result needs fresh independent proof review before any application/state promotion. It does not solve root-star inputs W=N(u): when u is in B and A contains v, exactly one W vertex lies in A, hence b=1 and b-a>=2 is impossible. Its prospective use is the nonstar root-in-obstruction boundary, where turning u from a terminal into an omission may expose a different accepted marked local input. No full twelve-hole or P6 conclusion is asserted.
