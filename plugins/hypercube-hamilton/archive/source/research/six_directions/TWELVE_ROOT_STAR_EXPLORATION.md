# Root-star holes: exact reductions, a mixed-opening route, and remaining obligations

2026-11-02. Proof-writer exploration by `/root/higher_forced_cherry_review` (role switched from prior independent audits). This document is **not an independent acceptance** of its new arguments. No ledger or accepted producer file is changed.

**Status of the requested root-star endpoint claim: NOT CURRENTLY JUSTIFIED by the accepted inputs alone.** There is no counterexample here. The document supplies exact reductions, two short structural obstructions to naive transfers, a new Q5 endpoint consequence and root-mirror transfer candidate, and a concrete conditional multi-bridge construction. The main missing input is now an explicit *bipartite mixed-omission cycle with an opening edge*, not an unspecified higher-layer theorem. A deficient rank probe does not refute that input.

## 1. Exact claim and diagnostic domain

Let M be any original short matching in Q6 with holes H={u} union Z union W, u=0, |Z|=5 even vertices, and W=N(u)={1,2,4,8,16,32}. Let v=31 be a covered odd target. The desired claim is a Hamilton u--v path containing M, with all new edges short, for every realizing M.

The diagnostic `TWELVE_NO_EXTRA_profile.json` lists 235 residual geometries in six target-stabilizer orbits. It is producer diagnostic evidence, not an independently accepted exhaustion gate. The six representatives are:

| Z | Diagnostic records |
|---|---:|
| 39,43,45,51,53 | 30 |
| 39,43,45,51,63 | 60 |
| 39,43,45,54,63 | 60 |
| 39,43,51,60,63 | 10 |
| 39,43,53,57,63 | 15 |
| 39,43,53,58,63 | 60 |

Every listed Z vertex has bit32 set. Let A be the bit32=0 face and B bit32=1. Then u,v belong to A, A has holes {u,1,2,4,8,16}, B has holes Z union {32}, and the original A port surplus is exactly four even ports. Thus if X_A is the original port set,

$$|X_A\cap E|-|X_A\cap O|=4,$$

so there are at least four even ports and c=|X_A| is positive even. These port facts hold for **every** realizing short matching, with no realizability filtering.

A later raw diagnostic also contains 297 root-star records among the 1281 residuals (12 at target7 and 285 at target31). The present special cut argument assumes the six listed representatives with Z wholly in B and is not asserted for all 297.

Accepted imports available here include complete ten-hole Q6 for original short matchings, Q5 all-balanced endpoints/cycles and all feasible imbalance-two avoid-one inputs, accepted uniform source transfer, and the seven older forced T17 classifications. New 15 forced T17 certificates mentioned below are producer candidates until their separate acceptance gate passes.

## 2. Two exact reformulations of the endpoint task

### 2.1 Delete the root

For a root-star input, any sought path has first edge u--w for some w in W, because all physical neighbors of u are those six free holes. Deleting u gives a spanning w--v path in Q6 minus u, containing M and using only short new edges. Conversely prefixing u--w to any such path solves the original task. Thus the root-star task is exactly equivalent to existence of this punctured-cube path for at least one w in W.

Both endpoints w,v are odd, while Q6 minus u has 31 even and 32 odd vertices. There is no parity contradiction. The accepted *full-cube balanced* endpoint theorem does not assert this punctured-cube statement. Replacing it by an ordinary opposite-parity endpoint theorem would lose the required domain and parity hypotheses.

### 2.2 A mixed-omission cycle, with one removable auxiliary edge

Write h=M(v). For any w in W define

$$F_w=(M\setminus\{vh\})\cup\{wh\}.$$

This is a matching: w was free, and h differs from u,w,v. Its holes replace w by v and retain u. The following are equivalent:

1. The original root-star Hamilton u--v extension exists.
2. For some w in W, F_w has a simple cycle C on exactly Q6 minus {u,v}, with every edge outside F_w short.

**Proof, 2 to 1.** Delete the required auxiliary edge wh from C. This leaves a spanning w--h path on 62 vertices. Add the short edge uw and original required edge hv. The result is a Hamilton u--v path through M; wh has disappeared, so every new surviving edge is short.

**Proof, 1 to 2.** The first neighbor w is free because W=N(u); the final edge is hv because v is an endpoint covered by M. Delete u and v from the path and add wh between its two distinct endpoints. This is a simple 62-cycle containing F_w. Its other new edges were short. The auxiliary edge cannot already occur internally on the resulting 62-vertex endpoint path.

Only this particular almost-short F_w is needed: all edges except possibly wh are original short edges. A theorem for every arbitrary matching in the mixed-omission domain would be stronger than required. It is not currently imported.

## 3. Why two naive fixes do not resolve the star

### 3.1 Preferred-cut standard T19 is a genuine degree trap

At the bit32 cut, the old odd-consumption row is (a,b)=(0,5), with four sources selected from the five A unit holes. Their B mirrors are four of the five short neighbors of the included B minority hole 32. The standard local cycle omits those four mirrors. Only **one** short neighbor of the included minority remains. Since that minority is not covered by the required B matching, its complement degree must be two, which is impossible.

This proves failure of that specific cycle template for every F on its local covered set. It is a degree obstruction to the template, not a nonexistence proof for the original Q6 path. It must not be presented merely as a search/rank failure.

### 3.2 Root-in-obstruction is not the direct star difficulty

In any target-facing coordinate cut with u in B, W=N(u) has exactly one hole in A. Thus b=1; the positive odd-consumption branch is unavailable, while the even-consumption mirrors Y are odd. Any ordinary same-parity forced obstruction has Y's odd parity, whereas u is even. The root is automatically outside it. In cuts with u in A it is outside the local B face entirely. Hence the familiar root-in-OB failure is not the direct explanation for these root-star leftovers in the usual templates.

The new root-mirror transfer below may help nonstar residuals, but it does not bypass the root-star degree trap by itself.

## 4. A derived Q5 endpoint interface and a new conditional transfer

The complete proof candidate is saved separately as `TWELVE_ROOT_MIRROR_MAJORITY_TRANSFER.md`, pending a fresh independent review.

**Derived Q5 interface.** An arbitrary K(Q5) matching with hole counts (a,a+2) has a Hamilton path from any free majority-parity r to any distinct same-majority-parity target v, covered or free, with only short new edges.

For covered v with mate h, replace vh by rh. The holes retain counts (a,a+2) but v becomes a majority hole. Apply the accepted avoid-v theorem, delete the auxiliary rh edge from its 31-cycle and add original hv. For free v, add rv, apply the accepted balanced cycle theorem to hole counts (a,a), and delete rv. Both arguments remove their only new auxiliary edge.

This permits a new root-mirror construction when u is in B, r=bar(u) is an A odd hole, r differs from v, and b-a>=2. Take only s=b-a-2 other odd sources, pair all X_A union S into D, and use the new same-majority r--v path. Add the short bridge ru and tag uv: this is a cycle on A union {u}; delete D and compress A **and u**. The final local B holes are H_B union Y and omissions are Y union {u}. The root is now omitted rather than a matching terminal. Hole counts and omission count match the old odd template, but the actual marked set changes. For s>=1 the usual both-port prescribed-gap argument works for one or several same-parity forced pairs because d=(c+s)/2>floor(c/2).

This is a complete conditional transfer proof in the separate candidate file, not a verified application. It cannot apply to root-star cuts with u in B: there b=1 and b-a>=2 fails. Its prospective use is the nonstar root-in-obstruction residual. The special s=0 case has an unconditional-local-input transfer but no automatic forced-pair gap assertion.

## 5. A concrete multi-bridge mixed-opening construction

This is the most specific star route found here. It uses one extra bridge at an A vertex which was originally covered, made legal by deleting a chosen short edge from a mixed-omission cycle. It avoids the four-omitted-neighbors trap by **consuming an original B hole**.

### 5.1 Required choices and the precise new local input

Work at the bit32 cut. Let q be an original **even A port**. Let t be an A short neighbor of q with

$$t\in T:=\{z\mathbin{\oplus}32:z\in Z\}\setminus\{v\}.$$

Then t is originally internally A-covered: its B mirror is an original Z hole, so it cannot be a crossing port, and t is neither an A hole nor v. Let w,b be distinct A unit holes from {1,2,4,8,16}. Put

$$S=\{1,2,4,8,16\}\setminus\{w,b\},\qquad |S|=3.$$

The new local obligation is:

> **Bipartite mixed-opening Q5 interface.** For H_A={0,q,31,b}, U_A={0,31}, and every *bipartite* perfect matching F of K(Q5) minus H_A, there exists a simple cycle on Q5 minus U_A containing F, with all edges outside F short, and containing the specified short edge q--t.

Here q and b are included holes, q is even, b odd, and t is a covered terminal. A still weaker interface may suffice: F need only be the structured matching M'_A+D below, and D is ours to choose. The quantifiers could be weakened to existence of a bipartite D for each original M. The universal interface is a convenient separable sufficient input, not something proved by existing balanced endpoints.

A short-forest rank certificate for this stronger interface must retain only forests containing q--t. The generic format is N=28, R=8192, 16 short forest edges, omitted degrees zero at 0,31, included-hole degrees two at q,b, terminal degrees one. A rank deficiency of this family would not alone refute coverage of all bipartite columns.

### 5.2 Local matching preparation, including the target-crossing case

Fix the actual original M and h=M(v). Form the auxiliary global matching F_w from Section 2.2, choosing w in A.

If h is in A, F'_A=(M_A minus vh) union wh. If h is in B, replace the original crossing v--h by the one **virtual auxiliary crossing** w--h. In that case the A port set X'_A replaces the odd port v by odd port w; the B port set is unchanged. This is the only possibly nonshort crossing, and it disappears when wh is deleted at the end. No general short-original-matching theorem is applied to F_w.

In both cases the number c and all even A ports are unchanged, and their even-port surplus is four. The A internal matching is bipartite; a possibly long internal wh still joins odd w to even h. The genuine A holes of F_w are {u,v} plus the four unit holes other than w, with counts (1,5).

Choose q as above and pair

$$(X'_A\setminus\{q\})\cup S$$

into D. This set has equal even and odd cardinalities: port surplus 4, minus even q gives surplus 3, and the three odd sources cancel it. Choose D entirely **bipartite**. The completion is disjoint from q,b,u,v, and the completed A matching has exactly H_A={u,q,v,b} as holes. Thus its required edges form a bipartite matching on K14+14. There is no need to assume a theorem for arbitrary nonbipartite F here.

Apply the unproved mixed-opening interface to this F'_A+D, obtaining C_A on A minus {u,v}, with q--t present. Because q is a hole, q--t is not a required matching edge. The vertex t is neither a port nor a selected source, so no D edge touches it.

### 5.3 Opening the cycle and making the covered bridge legal

Delete every D edge and also q--t from C_A. There are d=(c+2)/2>=3 D edges, so the result is a path forest. Attach:

1. every actual or virtual crossing of F_w, including the q crossing;
2. the three short bridges from S to their B mirrors Y;
3. the new short bridge t--t_B, where t_B=t xor32 is the original Z hole.

Deleting D gives one missing incidence at each ordinary port or selected source. Deleting q--t gives one missing incidence at q and at t. Those are restored by the q crossing and the new t bridge. All A vertices outside {u,v} now have degree two. The B attachment endpoints are X_B union Y union {t_B}, all distinct; t_B was an original hole and cannot be a port or one of the unit-mirror Y vertices. The graph stays a forest. This is why the new bridge from an **originally covered** t is legitimate; blindly adding such a bridge without deleting q--t would give degree three at t.

Compress the A paths. At the three Y vertices, suppress the usual distinct opposite-parity original B mates. The new attachment at t_B consumes that B hole rather than creating an omission there. The resulting local matching L has holes

$$\{32\}\cup(Z\setminus\{t_B\})\cup Y,$$

with singleton minority 32, seven even majority holes, and marked omissions Y. It is an actual **forced T17** input: three of the five neighbors of 32 are omitted, so the remaining two neighbors are

$$p=w\mathbin{\oplus}32,\qquad q_0=b\mathbin{\oplus}32.$$

The covered endpoints p,q_0 are not B ports in the original matching, since their original A mirrors w,b were free. The virtual w--h crossing does not change this: its B endpoint is the original port h, not the physical mirror of w. Both p,q_0 have the same even parity as Y, and their original short internal mates have the opposite parity, outside Y. Thus both retain their original M_B edges under compression/suppression. In particular **p q_0 is absent from the actual L**, independently of the choice of original matching and D.

If this actual marked B geometry is an accepted forced T17 classification, its local cycle therefore exists. Expand all compressed paths to a simple cycle on Q6 minus {u,v} containing F_w. All bridge edges are short except the possible wh auxiliary crossing; that required auxiliary survives until Section 2.2 deletes it. Delete wh and add uw and hv. This gives the original Hamilton u--v path, with all original M edges and only short new edges.

This proves the *conditional construction*. It does not prove the mixed-opening interface or that all choices yield an accepted B input.

### 5.4 Six canonical stronger local inputs

Under coordinate permutations of A fixing its antipodes 0,31, the geometric opening configurations (q,b,t), where q is even of weight2 or4, b a unit hole and t a weight3 neighbor of q, have six cases:

$$(3,1,7),\ (3,4,7),\ (3,4,11),\ (15,1,14),\ (15,1,7),\ (15,16,7).$$

For weight2 q, distinguish whether b belongs to q, and when it does not, whether t adds b. For weight4 q, distinguish whether b belongs to q, and when it does, whether t removes b. The six listed cases partition those possibilities. The required H is {0,q,31,b}, U={0,31}; each case additionally requires the edge q--t. Matching F only needs to be bipartite. No rank certificate for these enhanced cases is supplied here.

### 5.5 Existence of useful ports and the current B classification boundary

For the six representatives, T consists of their bit32-deleted weight3 vertices (delete 31 if 63 belongs to Z). Among the fifteen nonroot even A vertices, the numbers outside N(T) are 2,3,2,0,3,1. Since there are at least four even ports, **some** even port is adjacent to T in every case. This small fact was directly enumerated in the author diagnostics; a future application review should independently reconstruct it.

Not every t gives one of the seven older accepted forced T17 inputs. Enumerating all choices {w,b} and simultaneous marked permutations gives the following counts of nonroot even vertices which have no adjacent t leading to such an accepted older B input:

| Z orbit, in Section 1 order | Bad even q using old accepted7 | Bad even q after adding15 producer forced-T17 candidates |
|---|---:|---:|
| 1 | 15 | 15 |
| 2 | 5 | 3 |
| 3 | 2 | 2 |
| 4 | 5 | 0 |
| 5 | 3 | 3 |
| 6 | 1 | 1 |

Thus the old accepted seven provide a useful-port existence implication for the third, fifth and sixth orbits (diagnostically 135 records), conditional on the missing mixed-opening input. If the 15 new local forced inputs pass their separate gate, the same port-count implication extends to orbits 2 through6 (diagnostically 205 records). The first 30-record orbit has no such t with the currently listed old+new15 B registry. This is failure of this sufficient registry choice, not a local or global nonexistence result.

The exact author-side (t,{w,b},B-row) options are stored in `TWELVE_ROOT_STAR_OPEN_EDGE_OPTIONS.json`, marked diagnostic and not independently reviewed. No claim of coverage is promoted on the basis of those numbers.

### 5.6 Reported probe and why it does not close the obligation

The parent reports a probe for ordinary mixed H={0,1,3,31}, U={0,31} reaching rank8128 after85452 forests, below the generic8192 bound, without hitting its100000 cap. This report has not been independently checked here. Even if exhaustive, it only shows that this chosen full-row-rank sufficiency criterion does not close the unrestricted interface. It is not a counterexample.

In particular, this construction needs only **bipartite required columns**, and D can be chosen by us. A deficiency against the full arbitrary-matching column domain does not identify a bad bipartite column, does not establish an uncovered structured F'_A+D, and does not disprove a cycle through q--t. Future work should test restricted column coverage, identify the annihilator/obstruction family, or show a selectable bipartite D avoids it. Merely filtering the same forests to force q--t cannot increase their unrestricted full-matrix rank.

### 5.7 Late B-side producer update: ten further candidates

After the previous option table was generated, `a8_bridge_inputs_audit` supplied `TWELVE_STAR_B_profile.json` and `TWELVE_STAR_B_summary.json`. The profile lists the first orbit's 50 raw choices (five t values times ten unordered unit pairs) in ten marked T17 classes. The producer summary reports reduced rank1024 for all ten, with explicit fields `star_Q6_closed=false` and `A_mixed_opening_interface_proved=false`. Those finite certificates are **not independently accepted by this author document**.

If they pass their own fresh audit, they provide the missing first-orbit B classifications. In fact two marked classes suffice for a fixed unconsumed unit pair {8,16}: t=7 uses its class5, while t=11,13,19,21 use class0. All five t values then become available and only two nonroot even vertices lack a neighbor in that T set; the four-even-port argument supplies a usable q. Together with independently accepted new15 classifications for the other orbits, this would make the conditional B route available for all235 diagnostic records. It would **still not prove the A bipartite mixed-opening interface** or any root-star Q6 theorem. The earlier table intentionally records only old7 and pending15 and has not silently been reinterpreted as an acceptance of these ten new candidates.

### 5.8 A rank-deficient mixed input can still have an exact classification

The parent proposed a more informative interpretation of the reported8128 rank. The following implication has a complete algebraic derivation, conditional on independently verifying the claimed8128 positive forest certificate for the ordinary mixed geometry. It does not assert that the edge-forced interface has been certified.

Let H={0,1,3,31}, U={0,31}, K=Q5 minus H. Cut by bit2 (the coordinate value2), and let R be the seven **covered-terminal** crossing pairs from the odd parity side of the bit2=0 face to the even parity side of the bit2=1 face. This is the corresponding eight-edge half-layer minus its edge1--3, whose two endpoints are included holes. R is a matching of seven pairs inside K.

**Necessary obstruction.** A legal short complement has total odd degree9 and even degree7 in the bit2=0 face: omitted even0 contributes zero, included odd1 contributes two, and other covered terminals contribute one. Consequently its odd-to-even crossings minus reverse crossings equal2. If an original required F contains R, the complement cannot use any of those seven physical edges (a simple local cycle cannot reuse a required edge). The only remaining odd-half-layer crossing is1--3. Its odd-to-even crossing count is at most1, contradiction. Thus no local cycle exists for F containing every pair of R.

**Exact64-dimensional bad-column constraint.** In the full28-terminal connectivity matrix V, consider all columns G containing R. Such G are R union G^- with G^- an arbitrary matching on the fourteen residual labels K minus V(R). For any full row P, a cycle in P+R makes the row zero on all these columns. Otherwise suppress the internal R labels along the P/R paths, obtaining a residual matching P^-; the restriction of the P row to those columns is exactly the corresponding row of H14. Every residual P^- can arise: insert the seven R pairs consecutively into one edge of P^- using alternating P and R edges, and leave other residual edges unchanged. Thus this restricted full matrix has **exact rank64**, the rank of H14. This proves the codimension, rather than assuming the number of bad columns equals a dimension.

The full row space V has dimension8192. Evaluation on all G containing R has rank64, so its kernel W has dimension8128. Every legal forest row lies in W by the necessary obstruction. If an independently checked legal family spans8128 rows, it spans W exactly.

For any F not containing all of R, choose e in R minus F. Its endpoints belong to different F edges. Arrange these two F edges consecutively in a cyclic ordering of the F edges with appropriate orientations, use e to join them, and connect the other endpoints around the circle. This gives a perfect matching P containing e with P+F a single alternating cycle. For every bad G containing R, P and G share e, so the corresponding full row vanishes at G (a proper labeled two-edge component). Hence P lies in W. Since the certified forest rows span W and P has entry1 at F, at least one forest row connects F. Therefore the independently checked8128 certificate, together with the explicit obstruction, would prove:

> Ordinary mixed cycle exists iff F does **not** contain all seven pairs R.

No full8192 row rank is needed. This argument also works for arbitrary F, not only bipartite F. The reported rank8128 alone does not supply the hypothesis; its actual positive forests, reconstructed connectivity matrix and exact independent rank still need review. The classification is a fresh candidate mathematical input until that review occurs.

**Structured D avoids this ordinary trap.** In the star construction with canonical q=3,b=1, R includes4--6,8--10,16--18. The three-source set S=units minus {w,b} contains at least two of the odd unit vertices4,8,16. Choose one such source x. It is covered only by D in the completed A matching. If its R mate x xor2 is outside D's endpoint set, that R edge is already absent. If it is inside, choose x's D partner to be a different even D endpoint; at least three even endpoints are available because d>=3. The remaining balanced endpoint sets pair bipartitely. Thus some selectable bipartite D always makes F miss at least one R edge. This resolves the ordinary trap for the actual structured columns if the8128 classification is independently accepted, but still does not force a usable q--t opening edge.

An enhanced forest family constrained to contain q--t may have additional trap families. It needs its own row-space/obstruction analysis. Restricting the existing8128 family cannot increase its unrestricted rank, so repeating the8192-fullrank test would not answer the sharper question.

## 6. Target-forced-mate dual route

The later 1281 residual diagnostic includes many nonstar inputs with Z=N(v) minus one even neighbor h. Because the original matching is short and v is covered, **M must contain vh**. Delete v and that matching edge. The desired path is then equivalent to a spanning u--h path in Q6 minus v through M minus vh, with only short new edges; append hv in the reverse direction. Both endpoints are even and the punctured cube has one extra even vertex, so parity is correct.

This is a useful restriction of the original matching class and may help classify root-in-OB cases or choose D. It is not an application of the accepted full-cube balanced endpoint theorem. The mixed-omission reformulation of Section 2.2 applies for any chosen free short neighbor w of u, and only that particular mate h must be considered. A separate punctured-cube or mixed-opening input is still needed.

## 7. Concrete remaining obligations and next actions

1. Independently review the derived same-majority Q5 endpoint lemma and the separate root-mirror-omitted transfer. Their proofs use only accepted inputs, but this author file is not a fresh review.
2. For the star route, settle the six **bipartite mixed-opening** inputs, or the weaker structured version with selectable bipartite D. Ordinary mixed-cycle existence without a usable q--t edge does not authorize the covered bridge.
3. Independently check the new15 forced T17 inputs and the finite good-port lookup if using the conditional205 route. Existing old7 alone support only the conditional135 count stated above.
4. Independently review the newly supplied ten B forced-T17 candidates for the first 30-record orbit, or permit a t with t_B not in Z. The latter produces a T19 B geometry with three neighbor omissions plus one higher-weight mirror omission and needs its own classification and careful suppression; it is not proved here.
5. Extend any successful star proof to the additional root-star records outside the six235 diagnostic orbits; do not silently reuse the assumption Z wholly in B.
6. Only after the mathematical inputs pass fresh review should any actual-M/source census, scope assembly or ledger promotion occur.

There is no counterexample claim and no complete root-star, twelve-hole or P6 theorem in this exploration. The exact reductions and conditional interfaces distinguish the proved algebraic constructions from the still missing endpoint/marked-cycle inputs.
