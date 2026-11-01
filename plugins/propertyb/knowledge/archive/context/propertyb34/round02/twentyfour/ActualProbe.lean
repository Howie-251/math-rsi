import Aris4Math.ThirtyFour.TwentyFourNoLowCoverageData

namespace Aris4Math.ThirtyFour.TwentyFourNoLowActualProbe
open Aris4Math.ThirtyThree.MultiLockRecovery
open TwentyFourNoLowCoverage
set_option maxRecDepth 100000
set_option maxHeartbeats 1000000
attribute [local irreducible] Matched

private theorem entries_nodup : (entries.map Prod.fst).Nodup := by decide +kernel
private theorem pair_card : ∀j,(pair j).card=2 := by decide +kernel
private theorem pair_cap : ∀b j,low b (pair j)=cap b j := by decide +kernel
private theorem high_support : ∀T : Finset (Fin 6),3≤T.card→
    T∉entries.map Prod.fst→5<T.card := by decide +kernel
private theorem entry_unit_pair : ∀b : Bool,∀e∈entries,
    ∃i∈e.1,∃j∈e.1,i≠j ∧ low b {i,j}=1 ∧ e.2=1 := by decide +kernel

/-- Every actual six-lock configuration with degrees seven and all pair
codegrees one except the optional distinguished pair has a coloring. -/
theorem propertyB_of_six_labeled
    (coverageOracle : ∀b values,values∈catalogue b→Matched b values) (H : Simple5Hypergraph (Fin 24))
    (size : H.edges.card=34) (f : Fin 6↪Fin 24) (b : Bool)
    (degrees : ∀i,H.degree (f i)=7)
    (pairs : ∀i j,i≠j→H.codegree (f i) (f j)=low b {i,j}) : PropertyB H := by
  classical
  have lowActual : ∀T,T.card≤2→upperCount H f T=low b T := by
    apply upper_eq_of_low_data H f (low b)
    · simp [low,size]
    · intro i
      simp [low,degrees]
    · intro i j ij
      exact (pairs i j ij).symm
  let values := entries.map (fun e=>count H f e.1)
  have member : values∈catalogue b := by
    apply ActualAllocations.mem_enumerate H f entries entries_nodup pair (cap b)
    · intro e he
      obtain ⟨i,hi,j,hj,ij,unit,one⟩ := entry_unit_pair b e he
      have bound := count_le_codegree H f e.1 i j hi hj
      simpa only [pairs i j ij,unit,one] using bound
    · intro j
      rw [lowActual (pair j) (by rw [pair_card]),pair_cap]
  have highActual (T : Finset (Fin 6)) (large : 3≤T.card) :
      count H f T=vector values T := by
    dsimp only [vector,values]
    rw [BoundedAllocations.decode_map]
    by_cases mem : T∈entries.map Prod.fst
    · simp [mem]
    · simp [mem,count_eq_zero_of_large H f T (high_support T large mem)]
  have matched := coverageOracle b values member
  unfold Matched at matched
  let selected := choose b values
  let σ := perm selected.2
  let g := σ.toEmbedding.trans f
  apply TwentyFourNoLowSix.propertyB_of_low_high H g selected.1
  · apply upper_eq_of_low_data H g (TwentyFourNoLowSixData.upper selected.1)
    · have m := matched.1 (∅ : Finset (Fin 6)) (by simp)
      simpa only [selected,Finset.map_empty,low,if_pos rfl,size] using m.symm
    · intro i
      have m := matched.1 ({i} : Finset (Fin 6)) (by simp)
      have degree : H.degree (g i)=7 := degrees (σ i)
      rw [degree]
      simpa [selected,low] using m.symm
    · intro i j ij
      have m := matched.1 ({i,j} : Finset (Fin 6)) (by simp [ij])
      have pairActual : H.codegree (g i) (g j)=low b {σ i,σ j} :=
        pairs (σ i) (σ j) (σ.injective.ne ij)
      rw [pairActual]
      simpa only [Finset.map_insert,Finset.map_singleton,selected,σ] using m.symm
  · intro T large
    change count H (σ.toEmbedding.trans f) T=TwentyFourNoLowSixData.μ selected.1 T
    rw [LockRelabel.count_comp_perm,highActual _ (by simpa using large)]
    exact matched.2 T large

end Aris4Math.ThirtyFour.TwentyFourNoLowActualProbe
#print axioms Aris4Math.ThirtyFour.TwentyFourNoLowActualProbe.propertyB_of_six_labeled
