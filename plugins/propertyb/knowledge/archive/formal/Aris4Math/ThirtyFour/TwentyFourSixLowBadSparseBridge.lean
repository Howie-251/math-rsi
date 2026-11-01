import Aris4Math.ThirtyFour.TwentyFourSixLowBadSparseData
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadCoverage
open TwentyFourSixLowBadData
open TwentyFourSparseDecode
set_option maxHeartbeats 0
set_option maxRecDepth 100000
private theorem entries_nodup_sparse : (entries.map Prod.fst).Nodup := by decide +kernel
private theorem profile_high_correct : ∀i T,3≤T.card→
    μ i T=if T∈profileHigh i then 1 else 0 := by
  intro i
  fin_cases i <;> decide +kernel

private theorem low_support (b : Pattern) (T : Finset (Fin 6)) :
    low b T=if T=∅ then 34 else if T.card=1 then 6 else if T∈inputBad b then 2 else 1 := by
  by_cases h1 : 1≤b.val <;> by_cases h2 : 2≤b.val <;> simp [low,inputBad,h1,h2,or_assoc,or_comm,or_left_comm]
private theorem upper_support (i : Case) (T : Finset (Fin 6)) :
    upper i T=if T=∅ then 34 else if T.card=1 then 6 else if T∈profileBad i then 2 else 1 := by
  by_cases h1 : 2≤badCount i <;> by_cases h2 : 3≤badCount i <;> simp [upper,profileBad,h1,h2,or_assoc,or_comm,or_left_comm]

private theorem map_member_iff (σ : Equiv.Perm (Fin 6)) (S : Finset (Finset (Fin 6)))
    (T : Finset (Fin 6)) :
    T.map σ.toEmbedding ∈ S.image (fun U=>U.map σ.toEmbedding) ↔ T∈S := by
  constructor
  · intro h
    obtain ⟨U,hu,eq⟩ := Finset.mem_image.mp h
    have same : U=T := Finset.map_injective σ.toEmbedding eq
    simpa only [same] using hu
  · intro h
    exact Finset.mem_image.mpr ⟨T,h,rfl⟩

/-- Sparse support equalities for both the nonunit pairs and the high
traces recover all original low upper counts and high exact counts. -/
theorem cheap_correct (b : Pattern) (values : List ℕ) (selected : Case×Perm)
    (cheap : CheapMatch b values selected) :
    (∀T,T.card≤2→low b (T.map (perm selected.2).toEmbedding)=upper selected.1 T) ∧
    (∀T,3≤T.card→vector values (T.map (perm selected.2).toEmbedding)=μ selected.1 T) := by
  obtain ⟨binary,pairs,supporteq⟩ := cheap
  constructor
  · intro T _
    rw [low_support,upper_support]
    simp only [Finset.map_eq_empty,Finset.card_map,pairs,map_member_iff]
  · intro T large
    rw [profile_high_correct selected.1 T large]
    change BoundedAllocations.decode entries values (T.map (perm selected.2).toEmbedding)=_
    rw [TwentyFourSparseDecode.decode_indicator entries values entries_nodup_sparse binary,supporteq]
    simp only [map_member_iff]
end Aris4Math.ThirtyFour.TwentyFourSixLowBadCoverage
#print axioms Aris4Math.ThirtyFour.TwentyFourSixLowBadCoverage.cheap_correct
