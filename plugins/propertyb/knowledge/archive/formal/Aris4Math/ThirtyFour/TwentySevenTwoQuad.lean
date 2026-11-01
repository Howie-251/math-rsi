import Aris4Math.ThirtyFour.TwentySevenTwoQuadNumeric
import Aris4Math.ThirtyThree.TwentyTwoQuadAssembly

namespace Aris4Math.ThirtyFour.TwentySevenTwoQuad
set_option maxRecDepth 100000
open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.ThirtyThree.QuadProfiles
open Aris4Math.ThirtyThree.TripleProfiles (table_pruneZero pruneZero)
open Aris4Math.ThirtyThree.RefinedDeletion
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (highPairSum high_inventory count_le_codegree)
open Aris4Math.ThirtyFour.TwentySevenTwoQuadData

theorem realizes34 (H : Simple5Hypergraph (Fin 20)) (vertices : Fin 4 ↪ Fin 20)
    (i : Case) (hμ : ∀ T, count H vertices T = μ i T)
    (valid : Numeric.validProfile (p i) 34) :
    RealizesProfile H vertices (positions i) (p i) 34 := by
  rw [p_eq] at valid ⊢
  refine ⟨rfl,valid,?_,table_pruneZero _ _ _ (raw_table H vertices (positions i) (μ i) hμ _)⟩
  simp [profile,pruneZero,rawProfile,canonicalType]

theorem propertyB_of_data (H : Simple5Hypergraph (Fin 20))
    (edges34 : H.edges.card=34) (vertices : Fin 4 ↪ Fin 20) (i : Case)
    (hd : ∀ j, H.degree (vertices j) = degree j)
    (hc : ∀ j, H.codegree (vertices (first j)) (vertices (second j)) = coData i j)
    (ht : ∀ a, count H vertices (highLabels a) = highData i a) : PropertyB H := by
  obtain ⟨valid,strict,bounds⟩ := TwentySevenTwoQuadNumeric.certificates i
  have hm : ∀ T, count H vertices T = μ i T := by
    intro T
    rw [actual_recovered,edges34]
    rw [show (fun j => H.degree (vertices j)) = degree from funext hd,
      show (fun j => H.codegree (vertices (first j)) (vertices (second j))) = coData i from funext hc,
      show (fun j => count H vertices (highLabels j)) = highData i from funext ht]
    rfl
  have real := realizes34 H vertices i hm valid
  apply ThirtyThree.CustomDeletion.propertyB_of_custom_deletion H vertices (positions i) (p i) real rfl (loss i)
  · intro j _
    obtain ⟨lossEq,nonneg,avoids,quotas,bound⟩ := bounds j
    rw [lossEq]
    exact realized_refined_deduction H vertices (positions i) (p i) real j
      (avoid i j) (alpha i j) (quota i j) (lossAt i j) nonneg avoids quotas bound
  · intro k hk
    have absent : ∀ j : Fin 4, k ≠ (positions i j).val+1 := by
      intro j he
      apply hk
      simp only [p,pruneZero]
      exact List.mem_ofFn.mpr ⟨j,he.symm⟩
    simp [loss,absent 0,absent 1,absent 2,absent 3]
  · exact strict

def co (a b c : ℕ) : Fin 6 → ℕ := ![2,a,b,a,b,c]

set_option maxHeartbeats 0 in
theorem coverage : ∀ a b : Fin 2, ∀ c : Fin 3, ∀ h : Fin 5 → Fin 3,
    (∀ j, highPairSum (fun z => (h z).val) j ≤ co (a.val+1) (b.val+1) (c.val+1) j) →
    (a.val=0 ∧ b.val=0 ∧ c.val=1 ∧ ∀ z, (h z).val=0) ∨
    ∃ i : Case, (∀ j, co (a.val+1) (b.val+1) (c.val+1) j=coData i j) ∧
      ∀ z, (h z).val=highData i z := by
  intro a b c
  fin_cases a <;> fin_cases b <;> fin_cases c <;> decide +kernel

theorem residual_of_not_propertyB (H : Simple5Hypergraph (Fin 20))
    (edges34 : H.edges.card=34) (noB : ¬ PropertyB H) (vertices : Fin 4 ↪ Fin 20)
    (a b c : ℕ) (ha : a=1 ∨ a=2) (hb : b=1 ∨ b=2) (hc : 1 ≤ c ∧ c ≤ 3)
    (degrees : ∀ j, H.degree (vertices j)=degree j)
    (codegrees : ∀ j, H.codegree (vertices (first j)) (vertices (second j))=co a b c j) :
    a=1 ∧ b=1 ∧ c=2 ∧ ∀ z, count H vertices (highLabels z)=0 := by
  have choose : ∀ i : Fin 5, ∃ j : Fin 6,
      first j ∈ highLabels i ∧ second j ∈ highLabels i ∧ j ≠ 5 := by decide
  have bounded (i : Fin 5) : count H vertices (highLabels i) ≤ 2 := by
    obtain ⟨j,hj1,hj2,hj⟩ := choose i
    have bound := count_le_codegree H vertices (highLabels i) (first j) (second j) hj1 hj2
    rw [codegrees] at bound
    have small : co a b c j ≤ 2 := by
      fin_cases j <;> simp_all [co] <;> omega
    exact bound.trans small
  let h : Fin 5 → Fin 3 := fun z => ⟨count H vertices (highLabels z),by have := bounded z; omega⟩
  let ai : Fin 2 := ⟨a-1,by omega⟩
  let bi : Fin 2 := ⟨b-1,by omega⟩
  let ci : Fin 3 := ⟨c-1,by omega⟩
  have ae : ai.val+1=a := by dsimp [ai]; omega
  have be : bi.val+1=b := by dsimp [bi]; omega
  have ce : ci.val+1=c := by dsimp [ci]; omega
  have inv : ∀ j, highPairSum (fun z => (h z).val) j ≤ co (ai.val+1) (bi.val+1) (ci.val+1) j := by
    intro j
    rw [ae,be,ce,← codegrees j]
    exact high_inventory H vertices j
  rcases coverage ai bi ci h inv with ⟨a0,b0,c1,zero⟩ | ⟨i,coeq,higheq⟩
  · exact ⟨by omega,by omega,by omega,zero⟩
  · exfalso
    apply noB
    apply propertyB_of_data H edges34 vertices i degrees
    · intro j
      rw [codegrees,← ae,← be,← ce]
      exact coeq j
    · exact higheq

/-- The zero-high-trace residue excludes every common edge through locks 0,2,3. -/
theorem no_common_023 {v : ℕ} (H : Simple5Hypergraph (Fin v))
    (vertices : Fin 4 ↪ Fin v) (zero : ∀ z, count H vertices (highLabels z)=0)
    (e : Finset (Fin v)) (he : e ∈ H.edges)
    (h0 : vertices 0 ∈ e) (h2 : vertices 2 ∈ e) (h3 : vertices 3 ∈ e) : False := by
  classical
  by_cases h1 : vertices 1 ∈ e
  · have sig : lockSignature vertices e=highLabels 4 := by
      ext j; fin_cases j <;> simp [lockSignature,highLabels,h0,h1,h2,h3]
    have pos : 1 ≤ count H vertices (highLabels 4) := Finset.one_le_card.mpr
      ⟨e,Finset.mem_filter.mpr ⟨he,sig⟩⟩
    rw [zero] at pos
    omega
  · have sig : lockSignature vertices e=highLabels 2 := by
      ext j; fin_cases j <;> simp [lockSignature,highLabels,h0,h1,h2,h3]
    have pos : 1 ≤ count H vertices (highLabels 2) := Finset.one_le_card.mpr
      ⟨e,Finset.mem_filter.mpr ⟨he,sig⟩⟩
    rw [zero] at pos
    omega
end Aris4Math.ThirtyFour.TwentySevenTwoQuad
#print axioms Aris4Math.ThirtyFour.TwentySevenTwoQuad.residual_of_not_propertyB
