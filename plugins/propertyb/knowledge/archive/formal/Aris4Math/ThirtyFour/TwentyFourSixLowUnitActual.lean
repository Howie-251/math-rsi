import Aris4Math.ThirtyFour.TwentyFourSixLowUnitData

namespace Aris4Math.ThirtyFour.TwentyFourSixLowUnitActual
open Aris4Math.ThirtyThree.MultiLockRecovery
open TwentyFourSixLowUnitData
open TwentyFourNoLowCoverage (entries pair cap catalogue vector perm)
set_option maxRecDepth 100000
set_option maxHeartbeats 1000000
private theorem entries_nodup : (entries.map Prod.fst).Nodup := by decide +kernel
private theorem entry_large : ∀e∈entries,2≤e.1.card ∧ e.2=1 := by decide +kernel
private theorem pair_two : ∀j,(pair j).card=2 := by decide +kernel
private theorem cap_one : ∀j,cap false j=1 := by decide +kernel
private theorem high_support : ∀T : Finset (Fin 6),3≤T.card→
    T∉entries.map Prod.fst→5<T.card := by decide +kernel

/-- Reuse the already complete 352-input six-lock catalogue. Changing the
ordinary degrees from seven to six changes only singleton and empty counts. -/
theorem actual_classification (H : Simple5Hypergraph (Fin 24)) (size : H.edges.card=34)
    (f : Fin 6↪Fin 24) (degrees : ∀i,H.degree (f i)=6)
    (unit : ∀i j,i≠j→H.codegree (f i) (f j)=1) :
    ∃i : Case,∃σ : Equiv.Perm (Fin 6),∀T,count H (σ.toEmbedding.trans f) T=μ i T := by
  classical
  have lowActual : ∀T,T.card≤2→upperCount H f T=upper T := by
    apply upper_eq_of_low_data H f upper
    · simp [upper,size]
    · intro i;simp [upper,degrees]
    · intro i j ij;simp [upper,unit i j ij,ij]
  let values := entries.map (fun e=>count H f e.1)
  have member : values∈catalogue false := by
    apply ActualAllocations.mem_enumerate H f entries entries_nodup pair (cap false)
    · intro e he
      obtain ⟨large,one⟩ := entry_large e he
      rw [one]
      apply ActualAllocations.count_le_of_pairs H f 1
      · intro i j ij;rw [unit i j ij]
      · exact large
    · intro j
      rw [lowActual (pair j) (by rw [pair_two]),cap_one]
      have card := pair_two j
      have nonempty : pair j≠∅ := by intro eq;rw [eq] at card;simp at card
      simp [upper,card,nonempty]
  have highActual (T : Finset (Fin 6)) (large : 3≤T.card) : count H f T=vector values T := by
    dsimp only [vector,values]
    rw [BoundedAllocations.decode_map]
    by_cases mem : T∈entries.map Prod.fst
    · simp [mem]
    · simp [mem,count_eq_zero_of_large H f T (high_support T large mem)]
  obtain ⟨selected,matched⟩ := TwentyFourNoLowCoverage.coverage false values member
  let σ := perm selected.2
  have small : selected.1.val<9 := by
    apply small_case selected.1
    have equality := matched.1 ({0,1} : Finset (Fin 6)) (by decide)
    have card : (({0,1} : Finset (Fin 6)).map (perm selected.2).toEmbedding).card=2 := by simp
    have nonempty : (({0,1} : Finset (Fin 6)).map (perm selected.2).toEmbedding)≠∅ := by
      intro eq;rw [eq] at card;simp at card
    simpa [TwentyFourNoLowCoverage.low,card,nonempty] using equality.symm
  let i : Case := ⟨selected.1.val,small⟩
  have cast : largeCase i=selected.1 := Fin.ext rfl
  refine ⟨i,σ,?_⟩
  intro T
  rw [μ_eq_recovered]
  apply actual_recovered H (σ.toEmbedding.trans f) upper (μ i)
  · apply upper_eq_of_low_data H (σ.toEmbedding.trans f) upper
    · simp [upper,size]
    · intro j;simp [upper,degrees]
    · intro j k jk;simp [upper,unit (σ j) (σ k) (σ.injective.ne jk),jk]
  · intro U large
    rw [LockRelabel.count_comp_perm,highActual _ (by simpa using large),high_eq i U large,cast]
    exact matched.2 U large
end Aris4Math.ThirtyFour.TwentyFourSixLowUnitActual
#print axioms Aris4Math.ThirtyFour.TwentyFourSixLowUnitActual.actual_classification
