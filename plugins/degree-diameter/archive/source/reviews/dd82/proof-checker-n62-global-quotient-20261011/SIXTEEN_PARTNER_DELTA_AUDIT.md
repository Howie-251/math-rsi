# Size-sixteen partner exclusion: bounded delta audit

**Verdict: PASS28, modulo the named actual-graph imports.** All 313 lines of `proofs/dd82/n62/D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md` were checked. No mathematical gap or source repair was found. The paper excludes all seven displayed size-sixteen cases, including the necessary eight-vertex mixed type (3,2). Together with the previously reviewed reductions, it establishes that both D1-associated components have at least fourteen vertices. It does not exclude D1 or arbitrary order-62 graphs.

Reviewer: `/root/proof_review_n62_d1_reduction`; requested `gpt-6-astra` / `ultra`, actual backend unattested. This is a same-family, provisional semantic review. The author is a different agent. No author paper was modified. The audit is incremental; prior accepted component and moment derivations are reused, rather than represented as freshly recertified imports.

## Scope, symbols, and dependency ledger

For every actual legal simple undirected graph G on 62 vertices, let A be its original adjacency matrix and B=A²+A−7I−J. Let H,K be distinct components of the positive support of B, with sizes 12,16, original cross degrees r_HK=4,r_KH=3, and (s,t) in {(0,0),(0,1),(0,2),(1,1),(1,2),(2,0),(2,1)}. The local theorem states that no such component pair exists. It is stronger in scope than the D1-specific use: no extra local D1 structure is used within the seven-case argument.

A and B are 62×62 symmetric matrices; A is a zero-diagonal 0–1 matrix. R is the nonnegative integer component quotient with r_CD counting neighbors in D of a vertex in C. The vectors d_L=A1_L count original neighbors in L. Scalars x_v=d_H(v), y_v=d_K(v) are nonnegative integers; N_ij is the integer size of a joint exterior type. The factorial moments Fx,Fy and the cross moment C are finite sums. P and M denote entire joint types, whereas X is first a type and then proved to be a single component. No symbol reverses the directed quotient convention.

Dependency DAG: actual graph identities → component equitability and quotient → exterior moments / pointwise bounds / type divisibility → complete mixed-type reduction → seven explicit contradictions. The combined H,K≥14 consequence separately imports the minimum-size list and its other exclusions. No circularity occurs. There are no asymptotic claims, limits, probability modes, or analytic interchanges.

Accepted imports used locally: `GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`, Section 3, and `D1_COMPONENT_MINIMUM_SIZES.md`, Section 8. Their actual-graph hypotheses and quotient orientation match this paper. The main seven-case exclusion uses evenness but does not use B≤2, a minimum nonempty type size of four, or individual-component invariance under A. In particular it allows potential two-vertex components until its own divisibilities exclude or constrain them.

For the combined consequence, the five partner-size triples and H=K≥14 are the reviewed minimum-size results; the seven size-sixteen cases agree exactly with the reviewed exact-moment paper. The reviewed twelve-by-twelve, two-large-partner and twenty-zero-two results remove sizes 12,24,20, while the exact separators remove 28. These imports retain their own explicit dependencies, including the no-triple premise where used by the earlier proofs. The old two-partner post-fix workflow was closed only after inspecting the actual separate fresh-blind PASS receipt, cited below.

## Proof-obligation inventory

Each row records a checked implication under the preceding actual-graph hypotheses. All 28 obligations are discharged.

| ID | Obligation | Check |
|---|---|---|
| S01 | Actual graph scope and orientation | A is the original symmetric adjacency matrix; r_CD counts neighbors in D from C. The imported actual quotient R²+R=10I+1nᵀ has nonnegative integer entries and satisfies component edge balance. |
| S02 | Whole-component types | Equitability makes (d_H,d_K) constant on each exterior B-component, so every joint type is a union of whole components; it need not be a single component. |
| S03 | Even component and type sizes | B has integer weights and row sum three, so 3\|E\| is twice the total unordered B-weight. Each component and each type has even size, without using B≤2. |
| S04 | Joint and individual divisibilities | For a type T_ij, each vertex of H has an integer common number of neighbors in T_ij; edge balance gives 12\|iN_ij. Similarly 16\|jN_ij. The same argument applies to a single component within a type, including zero-coordinate cases. |
| S05 | Exact moment specialization | Substituting h=12,k=16,a=4,b=3 into the accepted formulas gives N=34, Sx=48−12s, Fx=72−12s², Sy=80−16t, Fy=144−16t², C=48(3−s−t). |
| S06 | Pointwise domain | The distinct components and degree eight give x+y≤8. Keeping H and K terms in the actual neighbor identities gives (s+1)x+3y≤12 and 4x+(t+1)y≤16; all omitted contributions are nonnegative. |
| S07 | Actual component-vector identity | B1_L=3·1_L implies (A²+A)1_L=10·1_L+\|L\|·1. At every vertex outside L, (A d_L)+d_L=\|L\|. No invariance of an individual component under A is assumed. |
| S08 | Complete mixed-coordinate domain | With s,t≥0 and x,y positive, x+3y≤12 and 4x+y≤16 give 1≤x,y≤3. Thus the nine displayed types exhaust mixed possibilities. |
| S09 | Divisor table | The values lcm(2,12/gcd(12,x),16/gcd(16,y)) are exactly 48,24,48,48,24,48,16,8,16 in the displayed row-major order. |
| S10 | First mixed exclusions | A positive divisor-48 type exceeds the total 34. Types (3,1),(3,3) require at least 16 vertices and factorial x contribution 96>Fx≤72. |
| S11 | Type (2,2) exclusion | Its size would be exactly 24. It contributes Sx=48, impossible for s>0. For s=0 it exhausts Sx but contributes only Fx=48<72, so no other vertex can repair the deficit. |
| S12 | Both surviving mixed sizes | The only candidates are P=(1,2) with 24 vertices and M=(3,2) with eight. A second multiple for M contributes at least 96 to Fx. This explicitly retains the formerly omitted M possibility. |
| S13 | No coexistence and cross moment | P and M together contribute Sx=48,Fx=48. This exceeds Sx when s>0 and exhausts it with an Fx deficit when s=0. Each alone contributes C=48, so C is zero or 48. |
| S14 | Cases (0,0),(0,1) | Their required cross moments are 144 and 96, respectively, contradicting the preceding complete possibilities. |
| S15 | Case (0,2) | M violates 4x+3y≤16. P therefore occurs, exhausts Sy=48, and contributes only Fy=48 rather than the required 80. |
| S16 | Case (2,0) | M violates 3x+3y≤12. P exhausts Sx=24 but contributes Fx=0 rather than the required 24. |
| S17 | Case (1,1), P branch | After P, the residual x moments are Sx=12,Fx=60. The pointwise bound x≤4 gives x(x−1)≤3x, hence Fx≤36, contradiction. |
| S18 | Case (1,1), M residual | After the eight M vertices, residual positive x types are pure with Sx=Fx=12. Divisibility makes nonempty x=3 contribute at least 24 and x=4 at least 72 to Fx. Therefore precisely six vertices have type (2,0), with no type (1,0). |
| S19 | Individual M and X components | Every component inside M has size divisible by eight, so the eight-vertex M is one component. Every component inside X=T20 has size divisible by six, so the six-vertex X is one component. |
| S20 | Actual (1,1) neighbor equations | d_H is 1 on H, 3 on K and M, 2 on X, and zero elsewhere. At v∈M the identity is 12=3+6+3d_M(v)+2d_X(v)+3, forcing no M−X edges. At v∈X it is 12=2+2d_X(v)+2, forcing d_X(v)=4. |
| S21 | Quotient diagonal contradiction | For the actual six-vertex component X, R_XX=4. Its diagonal quotient equation has nonnegative other terms and gives R_XX²+R_XX≤\|X\|+10=16, contradicting 20. |
| S22 | Case (2,1), positive x support | C=0 makes positive x and y supports disjoint. Summing x−1≤x(x−1)/2 over positive x gives \|U\|≥24−24/2=12. |
| S23 | Case (2,1), pure y counts | Writing N01=16a,N02=8b,N03=16c,N04=4d gives a+b+3c+d=4 and b+6c+3d=8. Nonnegative integer solutions force c=0,d=2,b=2,a=0. Thus \|V\|=24 and \|U\|+\|V\|≥36>34. |
| S24 | Case (1,2), pure x counts | x≤4 and six-point minimum for x=4 exclude that type by Fx≥72>60. The remaining equations give u=3w−24,v=30−3w,8≤w≤10 and 4\|w; hence N30=8,N20=6,N10=0. |
| S25 | Case (1,2), pure y counts and exhaustion | A y=3 type contributes at least 96>80. For counts a=N01,b=N02,d=N04, a=8d−32,b=40−6d and 4≤d≤6 with 4\|d force d=4,b=16,a=0. The four nonzero types total 34, leaving no zero type. |
| S26 | Case (1,2), neighbors of type (0,4) | Such a vertex z exists. Its four K neighbors each have d_H=3 and exhaust the right side 12 in the H identity. Thus z has no neighbor in either positive x exterior type and no neighbor in H. |
| S27 | Final original-graph contradiction | Degree eight and the exhausted exterior list force the other four neighbors of z into T04∪T02. All eight neighbors have d_K≥2, while d_K(z)=4. The K identity gives 16=(A d_K)(z)+4≥20. |
| S28 | Coverage and combined consequence | All seven listed cases are excluded. The reviewed minimum-size and exact-separator results restrict H12 to five partner sizes; the reviewed pure twelve, two-large-partner, and twenty-zero-two exclusions remove all other options. Hence H≠12 and H≥14 by evenness. The previously reviewed K12 reduction and exclusion give K≥14. H=K was already ≥14 in the minimum-size source. |

## Counterexample and boundary pass

The mixed-type divisor table was regenerated independently. It includes (3,2), whose minimum count eight is essential: omitting it would leave the (1,1) argument incomplete. Its possible larger multiples fail the factorial budget. The (2,2) and simultaneous P/M possibilities were checked at s=0, where equality in the first moment requires an explicit second-moment contradiction.

The six-vertex type X is not assumed connected in B: divisibility is applied separately to every component inside it before connectivity is concluded. The original-neighbor equations then use all possible nonzero d_H values. Symmetry of the original graph, rather than component invariance, transfers absence of M−X edges. The final quotient diagonal estimate drops only nonnegative terms.

For the pure cases, zero-coordinate and (0,0) types are allowed initially. In (2,1), disjoint positive supports alone exceed 34; no condition on the zero type is needed. In (1,2), the exact four positive-type counts exhaust 34 before the final neighborhood argument rules out hidden zero-type neighbors. Both applications of the component identity are at vertices outside the selected component. No counterexample under the stated hypotheses was found, and failure to find one is not used as proof.

## Independent arithmetic evidence

A primary standard-library Python check exited 0. It regenerated all nine mixed divisors, checked the mixed domain bounds in every listed case, and substituted all seven parameter pairs into the general exact moment formulas. It obtained the following vectors in order (N,Sx,Fx,Sy,Fy,C):

    (0,0): (34,48,72,80,144,144)
    (0,1): (34,48,72,64,128,96)
    (0,2): (34,48,72,48,80,48)
    (1,1): (34,36,60,64,128,48)
    (1,2): (34,36,60,48,80,0)
    (2,0): (34,24,24,80,144,48)
    (2,1): (34,24,24,64,128,0)

Fresh bounded shard `/root/proof_review_n62_d1_reduction/sixteen_pure_arithmetic`, requested `gpt-6-astra` / `ultra` with no inherited conversation, checked Sections 4–5 independently. It returned six obligation keys: pure domain; (2,1) integer contradiction; (1,2) x counts; (1,2) y counts; full exterior exhaustion; final actual-graph contradiction. Its reported exact enumeration of divisible pure counts up to 34 found no combined distribution for (2,1), and the single displayed distribution for (1,2). The shard found no local gap and did not issue a whole-paper verdict. The proof above is explicit arithmetic and does not depend on enumeration, solver status, or an LP result.

## Prior post-fix workflow closure

The separate [fresh blind audit](../proof-checker-n62-two-partners-blind-20261011/PROOF_AUDIT.md) and its JSON receipt were read. They explicitly check the corrected first-case coefficient d_K|H=5 and the equation 20=5x+3d_Y, record no prior target audits read, and return PASS for both large-partner exclusions and the separate twenty-zero-two exclusion. This discharges the earlier two-partner post-fix review requirement. Its original CRITICAL coefficient error and author repair remain preserved in `TWO_LARGE_PARTNER_DELTA_AUDIT.md/.json`; the workflow verdict is now PASS. This closure is based on the actual receipt, not solely on the parent's report.

No solver, LP, Lean compilation, source modification, or order63–65 work was performed. Only Markdown and JSON review artifacts are emitted; no digests are generated. Cross-family acceptance and the full D1/order-62 problem remain outside this audit.
