# Pure twelve-by-twelve component exclusion delta audit

**PASS12 — zero open issues.** The stated 12×12 component pair is excluded by the actual moment/type argument. Combined with the accepted minimum-size paper, every D1 generated-triangle component K therefore has **|K|≥14**. This does not exclude a twelve-vertex heavy component paired with a larger K, or the whole D1 branch.

Reviewed all165 lines of `proofs/dd82/n62/D1_TWELVE_COMPONENT_EXTERIOR_EXCLUSION.md`. Main reviewer: `/root/proof_review_n62_d1_reduction`; an independent bounded shard `/root/proof_review_n62_d1_reduction/signed_spectral_delta` checked the entire note and returned six discharged obligations with no concrete errors. Requested model/effort is `gpt-6-astra` / `ultra`; actual backend identity is unattested. Acceptance is same-family provisional. No source was edited.

## Hypotheses and ledger

The proof uses actual A,B, component equitability, the accepted exterior moments, and the explicit established exclusion B_xy=3. The last import is essential for ruling out size-two repeat components. No finite separator table or floating LP claim is a dependency of this pure proof.

| ID | Checked obligation | Result |
|---|---|---|
| P01 | Orient the two hypothesized components by internal degree. | Equal sizes12 and cross degrees4 permit naming C as internal degree0 and D as degree1, regardless of which was the D1 heavy component. |
| P02 | Specialized moments and inequalities. | Substitution gives N=38, Sx=48,Sy=36,Qx=72,Qy=48,Qxy=48, hence factorial moments24,12. Pointwise bounds become x+4y≤12 and 4x+2y≤12. |
| P03 | Every B-component has size at least four. | Weighted degree counting gives even size. A size-two component with row sum3 and zero diagonal would have its sole off-diagonal entry3, excluded by the stated import. |
| P04 | Each nonempty type count is at least four, including n00. | Equitability makes (x,y) constant on every exterior B-component. Each type is a union of whole components, not an arbitrary subset; thus its count is zero or at least4 and even. This includes (0,0). |
| P05 | y cannot equal3. | The pointwise bound then forces x=0. At least4 points of type(0,3) would contribute24 to a factorial y-moment totaling12. |
| P06 | x cannot equal3. | It forces y=0. The minimum type size and factorial x-moment24 force exactly4 such points and leave x≤1 elsewhere. Then xy≤y everywhere, contradicting48>36. |
| P07 | The two factorial moments give the row/column totals (5). | With x,y≤2, each point at coordinate2 contributes exactly2. Thus n20+n21+n22=12 and n02+n12+n22=6. |
| P08 | Exactly one y=2 type has count6. | Two positive counts would sum to at least8 by P04. This uses the minimum4, not evenness alone. |
| P09 | Case n22=6. | With u=n21, all moments give n20=6−u,n11=24−2u,n01=u,n10=2u,n00=2−u. Hence n21+n00=2, impossible when each is zero or at least4. |
| P10 | Case n12=6. | n20=12−u,n11=36−2u,n01=u−12 force u=12. Then n11=12,n10=6 and the specified positive types total36, so n00=2, contradicting P04. |
| P11 | Case n02=6. | n20=12−u and n01=u−24 simultaneously require u≤12 and u≥24. All three placements of the six y=2 points are exhausted. |
| P12 | D1 generated-component corollary. | The minimum paper gives K≥12 and K12⇒distinct H12 with cross degrees4 and internal degrees{0,1}. P01–P11 exclude exactly that case. Evenness gives K≥14. |

Every displayed case formula was recalculated directly from the six moments. All nine types in {0,1,2}² are accounted for, including zero-coordinate types. No vertex assignment is assumed distinct unless it is an actual counted vertex, and no original-edge preservation of individual B-components is assumed.

The decisive possible failure mode would be replacing the minimum nonempty type size4 by mere evenness: the counts2 appearing in the contradictions would then be permitted. The source does not make that replacement; its no-triple import supplies the stronger bound. Type(0,0) is not an exception because it too consists of whole exterior B-components. The coordinate-cap argument also handles type(3,0) explicitly before reducing to nine types.

No computational table, solver, or LP infeasibility result was used. The source's global no-triple result is a prior paper import; its finite checker was not rerun. The conclusion is sound modulo the stated imports and remains separate from any full order-62 exclusion or Lean connection. No hashes, TeX/PDF/HTML, or order63–65 work was performed.
