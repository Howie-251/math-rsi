import Aris4Math.ThirtyFour.TwentyEightFacts
import Aris4Math.ThirtyFour.TwentyEightPairs
import Aris4Math.ThirtyFour.TwentySevenTwoQuad
import Aris4Math.ThirtyFour.TwentyStructure
import Aris4Math.ThirtyFour.Incidence

namespace Aris4Math.ThirtyFour.TwentyEightLocal
open scoped BigOperators
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.QuadProfiles (first second count highLabels)
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (fourVertices)
open Aris4Math.ThirtyFour.TwentyStructure

variable (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
  (size : H.edges.card=34) (noB : ¬ PropertyB H)
include cover size noB

theorem codegree_le_three (x y : Fin 20) (xy : x ≠ y)
    (dx : H.degree x=8) (dy : H.degree y=8) : H.codegree x y ≤ 3 := by
  have hn : ¬ 4 ≤ H.codegree x y := fun h => noB
    (TwentyEightPairs.propertyB_of_high H cover size x y xy dx dy h)
  omega

theorem residue (f : Fin 4 ↪ Fin 20) (degrees : ∀ j, H.degree (f j)=8) :
    TwentyEightClassification.Residue
      (fun j => H.codegree (f (first j)) (f (second j)))
      (fun j => count H f (highLabels j)) := by
  apply TwentyEightClassification.residual_of_not_propertyB H cover size noB f
  · intro j; fin_cases j <;> exact degrees _
  intro j
  have ne : f (first j) ≠ f (second j) := f.injective.ne (by fin_cases j <;> decide)
  exact ⟨H.one_le_codegree cover ne,codegree_le_three H cover size noB _ _ ne (degrees _) (degrees _)⟩

theorem no_common_of_three (p q z w : Fin 20)
    (dp : H.degree p=8) (dq : H.degree q=8) (dz : H.degree z=8) (dw : H.degree w=8)
    (pq : p ≠ q) (pz : p ≠ z) (pw : p ≠ w) (qz : q ≠ z) (qw : q ≠ w) (zw : z ≠ w)
    (three : H.codegree p q=3) : ∀ e ∈ H.edges, p ∈ e → z ∈ e → w ∈ e → False := by
  let f := fourVertices p q z w pq pz pw qz qw zw
  have ds : ∀ j, H.degree (f j)=8 := by
    intro j; fin_cases j <;> simp [f,fourVertices,dp,dq,dz,dw]
  have r := residue H cover size noB f ds
  have zeros := TwentyEightFacts.all_high_zero_of_three _ _ r ⟨0,three⟩
  exact TwentySevenTwoQuad.no_common_023 H f zeros

theorem all_codegrees_le_two (minimum : ∀ x, 8 ≤ H.degree x)
    (p q : Fin 20) (hp : p ∈ eights H) (hq : q ∈ eights H) (pq : p ≠ q) :
    H.codegree p q ≤ 2 := by
  have dp := (mem_eights H p).mp hp
  have dq := (mem_eights H q).mp hq
  have upper := codegree_le_three H cover size noB p q pq dp dq
  by_contra hn
  have three : H.codegree p q=3 := by omega
  let S := (eights H).erase p
  have large := eights_at_least_ten H size minimum
  have scard : 9 ≤ S.card := by simp only [S,Finset.card_erase_of_mem hp]; omega
  have cap (e : Finset (Fin 20)) (he : e ∈ H.edges) (hpe : p ∈ e) : (S ∩ e).card ≤ 1 := by
    apply Finset.card_le_one.mpr
    intro z hz w hw
    obtain ⟨hz,hze⟩ := Finset.mem_inter.mp hz
    obtain ⟨hw,hwe⟩ := Finset.mem_inter.mp hw
    obtain ⟨zp,hz⟩ := Finset.mem_erase.mp hz
    obtain ⟨wp,hw⟩ := Finset.mem_erase.mp hw
    have dz := (mem_eights H z).mp hz
    have dw := (mem_eights H w).mp hw
    by_contra zw
    by_cases qz : q=z
    · subst z
      obtain ⟨t,ht,tp,tq,tw⟩ := exists_fourth (eights H) (by omega) p q w
      have dt := (mem_eights H t).mp ht
      let f := fourVertices p t q w tp.symm pq wp.symm tq tw (by exact zw)
      have ds : ∀ j, H.degree (f j)=8 := by
        intro j; fin_cases j <;> simp [f,fourVertices,dp,dq,dt,dw]
      have r := residue H cover size noB f ds
      have zeros := TwentyEightFacts.all_high_zero_of_three _ _ r ⟨1,three⟩
      exact TwentySevenTwoQuad.no_common_023 H f zeros e he hpe hze hwe
    by_cases qw : q=w
    · subst w
      obtain ⟨t,ht,tp,tq,tz⟩ := exists_fourth (eights H) (by omega) p q z
      have dt := (mem_eights H t).mp ht
      let f := fourVertices p t z q tp.symm zp.symm pq tz tq zw
      have ds : ∀ j, H.degree (f j)=8 := by
        intro j; fin_cases j <;> simp [f,fourVertices,dp,dq,dt,dz]
      have r := residue H cover size noB f ds
      have zeros := TwentyEightFacts.all_high_zero_of_three _ _ r ⟨2,three⟩
      exact TwentySevenTwoQuad.no_common_023 H f zeros e he hpe hze hwe
    exact no_common_of_three H cover size noB p q z w dp dq dz dw pq zp.symm wp.symm qz qw zw three e he hpe hze hwe
  have lower : S.card ≤ ∑ z ∈ S, H.codegree p z := by
    calc
      _ = ∑ _z ∈ S, 1 := by simp
      _ ≤ _ := Finset.sum_le_sum (fun z hz => H.one_le_codegree cover (Finset.mem_erase.mp hz).1.symm)
  have upper := Incidence.codegree_capacity H p S 1 cap
  rw [dp] at upper
  omega

theorem graph_facts (minimum : ∀ x, 8 ≤ H.degree x)
    (f : Fin 4 ↪ Fin 20) (low : ∀ j, f j ∈ eights H) :
    TwentyEightFacts.GraphFacts (fun j => H.codegree (f (first j)) (f (second j)))
      (count H f (highLabels 4)) := by
  have ds (j) : H.degree (f j)=8 := (mem_eights H _).mp (low j)
  have r := residue H cover size noB f ds
  have bounded (j) : H.codegree (f (first j)) (f (second j)) ≤ 2 :=
    all_codegrees_le_two H cover size noB minimum _ _ (low _) (low _) (f.injective.ne (by fin_cases j <;> decide))
  exact TwentyEightFacts.graph_facts _ _ (TwentyEightFacts.small_of_bounded _ _ r bounded)

omit cover size noB in
theorem common_quad_iff (f : Fin 4 ↪ Fin 20) :
    (∃ e ∈ H.edges, ∀ j, f j ∈ e) ↔ 1 ≤ count H f (highLabels 4) := by
  constructor
  · rintro ⟨e,he,all⟩
    have sig : lockSignature f e=highLabels 4 := by
      ext j; fin_cases j <;> simp [lockSignature,highLabels,all]
    exact Finset.one_le_card.mpr ⟨e,Finset.mem_filter.mpr ⟨he,sig⟩⟩
  · intro positive
    obtain ⟨e,he⟩ := Finset.one_le_card.mp positive
    obtain ⟨he,sig⟩ := Finset.mem_filter.mp he
    refine ⟨e,he,?_⟩
    intro j
    have hj : j ∈ highLabels 4 := by fin_cases j <;> decide
    exact (mem_lockSignature f e j).mp (sig ▸ hj)

omit cover size noB in
theorem edge_eq_of_unit (x y : Fin 20) (unit : H.codegree x y=1)
    (e f : Finset (Fin 20)) (he : e ∈ H.edges) (hf : f ∈ H.edges)
    (xe : x ∈ e) (ye : y ∈ e) (xf : x ∈ f) (yf : y ∈ f) : e=f := by
  have bound : (H.edges.filter fun e => x ∈ e ∧ y ∈ e).card ≤ 1 := by
    change H.codegree x y ≤ 1
    omega
  apply Finset.card_le_one.mp bound
  · exact Finset.mem_filter.mpr ⟨he,xe,ye⟩
  · exact Finset.mem_filter.mpr ⟨hf,xf,yf⟩

end Aris4Math.ThirtyFour.TwentyEightLocal
#print axioms Aris4Math.ThirtyFour.TwentyEightLocal.all_codegrees_le_two
