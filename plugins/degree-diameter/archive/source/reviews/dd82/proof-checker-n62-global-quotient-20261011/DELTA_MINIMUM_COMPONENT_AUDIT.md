# D1 component minimum-size and exterior-moment delta audit

**PASS24 — zero open issues.** Reviewed all 290 lines and all eight sections of `proofs/dd82/n62/D1_COMPONENT_MINIMUM_SIZES.md`. The necessary minimum sizes, the five size/incidence triples, and the exterior moment restrictions are supported. No remaining component pair is asserted realizable or excluded by this verdict.

This is a same-family provisional delta review by `/root/proof_review_n62_d1_reduction`. Requested model/effort: `gpt-6-astra` / `ultra`; actual backend identity is unattested. The independent bounded shard `/root/proof_review_n62_d1_reduction/signed_spectral_delta` checked sections 6 and 8 and returned seven discharged obligations with no concrete error. No author source was edited.

## Assumptions and scope

The proof concerns an actual finite simple order-62 graph with degree eight, diameter at most two, and actual B=A²+A−7I−J. A particular heavy edge has the accepted D1 structure. H is its positive-support B-component and K the component containing its generated triangle. If they differ, a=r_HK≥4, b=r_KH≥3, ha=kb. The complete local rows and B_pq=0 come from the accepted hard-D1/C4 notes. Component equitability, even sizes, and the quotient identities come from the previously reviewed global paper.

Only the elementary actual identities and equitability portion of that quotient proof is needed here; its global classification and signed-eigenspace conclusions are not needed for these deductions. No new finite enumeration, LP separation, solver result, or formal axiom is used. The reported exterior-moment computation and its separating quadratics are outside this paper audit.

The symbol a in the local rows of section 2 is a vertex; the lower-case a in size/incidence inequalities is the integer quotient entry r_HK. The section-local meanings are recoverable and do not enter one equation together. Analogous t notation denotes the local repeat endpoint only in section 2, and the internal K-degree in section 4.2. No type mismatch was found.

The dependency chain is acyclic: common-neighbor budget → elementary h≥8 → exclusions h=8,10 → h≥12 → k≥12 → k=12 refinement and h=12 list. The general exterior moments use only the actual graph identity, so they can also independently verify the specialized moments used earlier.

## Obligation ledger

All obligations below are discharged; locations refer to the reviewed source.

| ID | Lines | Checked assertion and justification |
|---|---:|---|
| M01 | 21–40 | The inherited equitability, balance, row sum, even component sizes and D1 incidence bounds apply to the same actual graph. Cross-component B entries are exactly zero. |
| M02 | 51–57 | Counting common neighbors of unordered pairs inside C_i gives Σ_j n_j binom(r_ji,2). Summing c=1+B−A gives n_i(n_i+2−r_ii)/2, including weighted double entries. |
| M03 | 59–65 | Balance n_jr_ji=n_ir_ij gives (3). Every term is nonnegative: positive off-diagonal r_ij has positive integral r_ji; diagonal t(t−1) is nonnegative for integer t≥0. |
| M04 | 67–75 | Keeping the diagonal term gives n_i≥t²−2; keeping the HK term gives (5). If H=K, internal degree ≥4 gives h≥14. |
| M05 | 81–92 | The six vertices 0,w,a,r,p,q are distinct and in H. If they exhausted H, the two remaining unit repeats of r would be p,q; then the last repeat of p would have to be q, contradicting B_pq=0. Evenness yields h≥8. |
| M06 | 96–102 | At h=8 the budget allows only b=3,a=4 or5. Balance k=8a/3 is nonintegral in either case. H=K is already excluded by M04. |
| M07 | 106–110 | At h=10, a(b−1)≤12 gives b=3,a=4,5,6 or a=b=4. Integral balance retains exactly (k,a,b)=(10,4,4),(20,6,3). |
| M08 | 112–115 | Both retained cases saturate the budget with a(b−1)=12, forcing r_HH=0. Their K vertices exhaust all pair-common-neighbor contributions in H; every vertex outside K therefore has H-degree ≤1. |
| M09 | 119–128 | In the 10×10 case the reverse argument gives K independent and exterior K-degree ≤1. The 100 cross pairs have 60 common neighbors in total, all exterior; 42 exterior vertices contribute at most one each. Contradiction. |
| M10 | 132–140 | In the 10×20 case H has 20 remaining original incidences outside H∪K. Exterior H-degree ≤1 makes their targets exactly 20 distinct X vertices; the remaining Y has size 12. The displayed d_H profile follows. |
| M11 | 142–152 | Cross common-neighbor total 200−60=140 gives e(X,K)=140−60t. Subtracting H, internal K, and X incidences from K's degree total 160 gives e(Y,K)=40(t−1). Internal degree contributes 20t, with the correct multiplicity. |
| M12 | 154–165 | For y∈Y, summing CN(u,y)=1 over u∈H gives 3d_K(y)+d_X(y)=10. Degree eight and nonnegativity give 1≤d_K(y)≤3. Therefore 12≤e(Y,K)≤36, contradicting its multiple-of-40 value. |
| M13 | 167–186 | Evenness gives h≥12. If k≤10, balance and (5) give h(a²−k)≤k(a+2). For a≥4, a²−k≥a+2>0, forcing h≤k≤10. Thus k≥12. |
| M14 | 190–197 | For k=12, b(a−1)≤14 leaves (a,b)=(4,3),(4,4),(5,3). Balance and h≥12 leave only h=k=12,a=b=4. |
| M15 | 199–201 | Keeping both the diagonal and cross terms of (3) gives α(α−1)+12≤14−α and similarly for β; thus α²,β²≤2 and α,β∈{0,1}. |
| M16 | 203–217 | All five specialized moments (12) are exact. First moments remove hα and ha from total 8h; square moments remove hα² and kb² from h(h+10−α); the cross moment removes ha(α+β) from hk−ha. |
| M17 | 219–221 | If α=β=0, cross sum 96 violates 2Σxy≤Σx²+Σy²=144. |
| M18 | 223–229 | If α=β=1, each coordinate has sum36 and binomial sum6, hence positive support size ≥30. Two such supports in 38 vertices intersect, contradicting the required zero cross sum. Thus {α,β}={0,1}. |
| M19 | 233–241 | At h=12, a(b−1)≤14 gives b=3,a=4,…,7 or a=b=4. Balance gives exactly the five listed necessary triples. No claim of realization or sufficiency is made. |
| M20 | 245–257 | The general first, square and cross exterior moments (15) follow from actual degree/common-neighbor identities and balance. They allow arbitrary nonnegative a,b and internal degrees consistent with the graph. |
| M21 | 259–266 | The Gram matrix is Σ_v (1,x_v,y_v)^T(1,x_v,y_v), hence PSD. Disjointness of C,D and degree eight give nonnegative integral x_v,y_v with x_v+y_v≤8. The empty exterior is covered. |
| M22 | 267–276 | For exterior v, sum over u∈C of c(u,v)=1−A_uv gives Σ_{w∈N(v)}d_C(w)=h−x_v. The C,D-neighbor contributions are αx_v+by_v; discarding only nonnegative terms gives the first bound in (16), and swapping components gives the second. |
| M23 | 278–281 | Equitability makes (x_v,y_v) constant on each entire exterior B-component. Each has even size, so every type multiplicity is even. This does not assume A preserves components individually. |
| M24 | 5–17,283–290 | The paper proves necessary bounds and explicitly leaves the five h=12 cases, larger pairs, H=K, and double-edge parity unresolved. No computational separation is silently imported. |

## Independent moment derivation

For a B-component C of size h and internal original degree α,

    ||A1_C||² = 1_C^T(7I+J+B−A)1_C = h(h+10−α).

Removing contributions hα² from C and kb² from D yields Q_x in (15). The full cross product for distinct components is

    (A1_C)^T(A1_D) = hk−ha,

because both the identity and B cross blocks vanish. Removing hαa+kbβ=ha(α+β) gives the stated Q_xy. These calculations agree with the unordered-pair derivation and confirm all constants and signs in (12),(15).

## Exceptional-case and counterexample pass

No counterexample was found. The h=6 saturation argument accounts for every possible repeat target and uses the exact, already exhausted rows. Both h=8 nonintegral candidates and every h=10 candidate were checked. The 10×20 contradiction permits all integer t; no unstated bound on t is needed. Exterior vertices need not be original-independent, and their repeat components need not be preserved individually by A. Neither condition is used.

The k=12 equal-diagonal contradictions use actual nonnegative integral degrees, not arbitrary real moment variables. In particular, the support argument for α=β=1 requires integrality and uses it correctly. The mixed diagonal cases are necessary possibilities only. The five h=12 triples are an exhaustive output of the displayed necessary inequalities and balance, not five constructed graphs.

The pointwise inequalities remain valid for exterior vertices adjacent to either or both components, and zero cross incidence does not invalidate (15). Type parity follows from unions of whole even B-components, so it is stronger than mere evenness of the total exterior size and is justified.

## Result and boundary

No source repair was needed. This delta accepts h,k≥12, H=K⇒h≥14, the k=12 structure with opposite internal degrees, the h=12 five-case list, and the exact exterior moment/type restrictions. The script `component_exterior_moments.py`, its case counts, and any LP or separating-polynomial claims were not audited or used here. No solver, finite graph enumeration, hashes, TeX/PDF/HTML, or order63–65 work was performed.
