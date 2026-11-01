import Aris4Math.ThirtyThree.TwentyFourFullFiveData
import Aris4Math.ThirtyThree.TwentyFourQuadRedirect
import Aris4Math.K4Profiles
import Aris4Math.ProfileApplication

/-! A genuine edge of five degree-six vertices, with at most one internal
codegree-two pair, realizes one of the two strictly subunit bare profiles. -/
namespace Aris4Math.ThirtyThree.TwentyFourFullFive
open Aris4Math.TypeCounting Aris4Math.TraceRecovery
open TwentyFourFullFiveData MultiLockRecovery

/-- A large trace contains a pair other than the possible exceptional pair.
The selected full edge already uses that pair, so no other edge has this trace. -/
theorem actual_high (H : Simple5Hypergraph (Fin 24))
    (vertices : Fin 5 ↪ Fin 24) (E : Finset (Fin 24)) (edge : E ∈ H.edges)
    (inside : ∀ i, vertices i ∈ E) (k : Fin 2)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = low k {i,j}) :
    ∀ T, 3 ≤ T.card → count H vertices T = high T := by
  have full : lockSignature vertices E = Finset.univ := by
    ext i
    simp only [Finset.mem_univ,iff_true,mem_lockSignature]
    exact inside i
  have unique (e : Finset (Fin 24)) (he : e ∈ H.edges)
      (T : Finset (Fin 5)) (hsig : lockSignature vertices e = T) (large : 3 ≤ T.card) :
      e = E := by
    obtain ⟨i,hi,outside⟩ := Finset.exists_mem_notMem_of_card_lt_card
      (s := ({0,1} : Finset (Fin 5))) (t := T) (by norm_num; omega)
    obtain ⟨j,hj,ji⟩ := Finset.exists_mem_ne (show 1 < T.card by omega) i
    have ij := Ne.symm ji
    have ne : ({i,j} : Finset (Fin 5)) ≠ {0,1} := by
      intro eq
      exact outside (eq ▸ Finset.mem_insert_self i {j})
    have hone : H.codegree (vertices i) (vertices j) = 1 := by
      rw [pairs i j ij]
      simp [low,ij,ne]
    exact H.edge_unique_of_codegree_one hone he edge
      ((mem_lockSignature vertices e i).mp (hsig ▸ hi))
      ((mem_lockSignature vertices e j).mp (hsig ▸ hj)) (inside i) (inside j)
  intro T large
  by_cases eq : T = Finset.univ
  · subst T
    have fiber : H.edges.filter (fun e => lockSignature vertices e = Finset.univ) = {E} := by
      ext e
      simp only [Finset.mem_filter,Finset.mem_singleton]
      constructor
      · rintro ⟨he,hs⟩
        exact unique e he Finset.univ hs large
      · rintro rfl
        exact ⟨edge,full⟩
    change (H.edges.filter _).card = high Finset.univ
    rw [fiber]
    simp [high]
  · have fiber : H.edges.filter (fun e => lockSignature vertices e = T) = ∅ := by
      apply Finset.eq_empty_iff_forall_notMem.mpr
      intro e he
      obtain ⟨he,hs⟩ := Finset.mem_filter.mp he
      have ee := unique e he T hs large
      subst e
      exact eq (hs.symm.trans full)
    change (H.edges.filter _).card = high T
    rw [fiber]
    simp [high,eq]

/-- A labeled actual full-edge configuration has Property B. -/
theorem propertyB_of_labeled (H : Simple5Hypergraph (Fin 24))
    (edges33 : H.edges.card = 33) (vertices : Fin 5 ↪ Fin 24)
    (E : Finset (Fin 24)) (edge : E ∈ H.edges) (inside : ∀ i, vertices i ∈ E)
    (degrees : ∀ i, H.degree (vertices i) = 6) (k : Fin 2)
    (pairs : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = low k {i,j}) :
    PropertyB H := by
  have hlow : ∀ T, T.card ≤ 2 → upperCount H vertices T = low k T := by
    apply upper_eq_of_low_data H vertices (low k)
    · simp [low,edges33]
    · intro i
      simp [low,degrees]
    · intro i j ij
      exact (pairs i j ij).symm
  have actual (T : Finset (Fin 5)) : count H vertices T = counts k T :=
    (actual_recovered H vertices (low k) high hlow
      (actual_high H vertices E edge inside k pairs) T).trans (recovered_eq k T)
  obtain ⟨valid,strict,noCap,noCorrection⟩ := certificates k
  have real := FiveProfiles.realizes_profile H vertices (positions k) (counts k) actual []
    (by simpa only [← p_eq] using valid)
  rw [← p_eq] at real
  exact ProfileApplication.propertyB_of_uncorrected_profile H vertices (positions k)
    (p k) real noCap noCorrection strict

open BlockClassification K6Classification
open K6Traces (onGround onGround_card)

/-- Label a specified pair in a five-set by 0 and 1. -/
theorem label_pair (E B : Finset (Fin 24)) (five : E.card = 5)
    (sub : B ⊆ E) (two : B.card = 2) :
    ∃ label : ↥E ≃ Fin 5, labelBlock E label B = {0,1} := by
  let actual : Unit → Finset ↥E := fun _ => onGround E B
  let model : Unit → Finset (Fin 5) := fun _ => {0,1}
  have smallA (x : E) : (signature actual x).card ≤ 2 :=
    (Finset.card_le_univ _).trans (by decide)
  have smallB (x : Fin 5) : (signature model x).card ≤ 2 :=
    (Finset.card_le_univ _).trans (by decide)
  have single : ∀ i, (actual i).card = (model i).card := by
    intro i
    simp [actual,model,onGround_card E B sub,two]
  obtain ⟨label,hl⟩ := exists_equiv_map_blocks actual model smallA smallB
    (by simpa using five) single
    (fun i j h => False.elim (h (Subsingleton.elim i j)))
  exact ⟨label,hl ()⟩

/-- Both cases selected by the analytic quad redirection imply a real coloring. -/
theorem propertyB_of_full_five (H : Simple5Hypergraph (Fin 24))
    (edges33 : H.edges.card = 33) (selected : TwentyFourQuadRedirect.FullFiveLocks H) :
    PropertyB H := by
  obtain ⟨E,edge,degrees,cases⟩ := selected
  have five := H.five_uniform E edge
  rcases cases with unit | ⟨a,ha,b,hb,ab,bad,others⟩
  · let label : ↥E ≃ Fin 5 := Fintype.equivOfCardEq (by simpa using five)
    let vertices := lockVertices E label
    have inside (i : Fin 5) : vertices i ∈ E := (label.symm i).property
    apply propertyB_of_labeled H edges33 vertices E edge inside
      (fun i => degrees _ (inside i)) 0
    intro i j ij
    rw [unit _ (inside i) _ (inside j) (vertices.injective.ne ij)]
    simp [low,ij]
  · have sub : ({a,b} : Finset (Fin 24)) ⊆ E := by
      intro x hx
      simp only [Finset.mem_insert,Finset.mem_singleton] at hx
      rcases hx with rfl | rfl <;> assumption
    obtain ⟨label,labeled⟩ := label_pair E {a,b} five sub (by simp [ab])
    let vertices := lockVertices E label
    have inside (i : Fin 5) : vertices i ∈ E := (label.symm i).property
    have inverse : unlabel E label {0,1} = {a,b} :=
      labelBlock_injective E label (unlabel_subset E label _) sub
        ((label_unlabel E label _).trans labeled.symm)
    have pairEq (i j : Fin 5) :
        ({vertices i,vertices j} : Finset (Fin 24)) = {a,b} ↔
          ({i,j} : Finset (Fin 5)) = {0,1} := by
      have eq : unlabel E label {i,j} = unlabel E label {0,1} ↔
          ({i,j} : Finset (Fin 5)) = {0,1} :=
        (Finset.map_injective (lockVertices E label)).eq_iff
      rw [inverse] at eq
      simpa only [unlabel,Finset.map_insert,Finset.map_singleton] using eq
    apply propertyB_of_labeled H edges33 vertices E edge inside
      (fun i => degrees _ (inside i)) 1
    intro i j ij
    by_cases eq : ({i,j} : Finset (Fin 5)) = {0,1}
    · have actualEq := (pairEq i j).mpr eq
      have ordered : (vertices i = a ∧ vertices j = b) ∨
          (vertices i = b ∧ vertices j = a) := by
        have hi : vertices i = a ∨ vertices i = b := by
          have h := actualEq ▸ Finset.mem_insert_self (vertices i) {vertices j}
          simpa only [Finset.mem_insert,Finset.mem_singleton] using h
        have hj : vertices j = a ∨ vertices j = b := by
          have h := actualEq ▸ Finset.mem_insert_of_mem (Finset.mem_singleton_self (vertices j))
          simpa only [Finset.mem_insert,Finset.mem_singleton] using h
        have vne := vertices.injective.ne ij
        rcases hi with hi | hi <;> rcases hj with hj | hj
        · exact False.elim (vne (hi.trans hj.symm))
        · exact Or.inl ⟨hi,hj⟩
        · exact Or.inr ⟨hi,hj⟩
        · exact False.elim (vne (hi.trans hj.symm))
      have co : H.codegree (vertices i) (vertices j) = 2 := by
        rcases ordered with ⟨hi,hj⟩ | ⟨hi,hj⟩
        · simpa only [hi,hj] using bad
        · simpa only [hi,hj,H.codegree_comm b a] using bad
      rw [co]
      simp [low,eq]
    · rw [others _ (inside i) _ (inside j) (vertices.injective.ne ij)
        (fun heq => eq ((pairEq i j).mp heq))]
      simp [low,ij,eq]

end Aris4Math.ThirtyThree.TwentyFourFullFive
#print axioms Aris4Math.ThirtyThree.TwentyFourFullFive.propertyB_of_full_five
