import Aris4Math.ThirtyFour.TwentyFourNoLowSparseData
namespace Aris4Math.ThirtyFour.TwentyFourNoLowCoverage
open TwentyFourNoLowSixData
open TwentyFourSparseDecode
set_option maxHeartbeats 0
set_option maxRecDepth 100000
private theorem entries_nodup_sparse : (entries.map Prod.fst).Nodup := by decide +kernel
private theorem profile_high_correct : ∀i T,3≤T.card→
    μ i T=if T∈profileHigh i then 1 else 0 := by
  intro i
  fin_cases i <;> decide +kernel

theorem cheap_correct (b : Bool) (values : List ℕ) (selected : Case×Perm)
    (cheap : CheapMatch b values selected) :
    (∀T,T.card≤2→low b (T.map (perm selected.2).toEmbedding)=upper selected.1 T) ∧
    (∀T,3≤T.card→vector values (T.map (perm selected.2).toEmbedding)=μ selected.1 T) := by
  obtain ⟨binary,extra,pairfixed,supporteq⟩ := cheap
  constructor
  · intro T _
    cases b with
    | false => simp [low,upper,extra]
    | true =>
      have fixed := pairfixed rfl
      have eq : T.map (perm selected.2).toEmbedding=({0,1} : Finset (Fin 6)) ↔ T={0,1} := by
        conv_lhs => rw [← fixed]
        exact (Finset.map_injective (perm selected.2).toEmbedding).eq_iff
      simp [low,upper,extra,eq]
  · intro T large
    rw [profile_high_correct selected.1 T large]
    change BoundedAllocations.decode entries values (T.map (perm selected.2).toEmbedding)=_
    rw [TwentyFourSparseDecode.decode_indicator entries values entries_nodup_sparse binary,supporteq]
    have eq : T.map (perm selected.2).toEmbedding ∈
        (profileHigh selected.1).image (fun U=>U.map (perm selected.2).toEmbedding) ↔
        T∈profileHigh selected.1 := by
      constructor
      · intro h
        obtain ⟨U,hu,eq⟩ := Finset.mem_image.mp h
        have same : U=T := Finset.map_injective (perm selected.2).toEmbedding eq
        simpa only [same] using hu
      · intro h
        exact Finset.mem_image.mpr ⟨T,h,rfl⟩
    simp only [eq]
#print axioms cheap_correct

end Aris4Math.ThirtyFour.TwentyFourNoLowCoverage
