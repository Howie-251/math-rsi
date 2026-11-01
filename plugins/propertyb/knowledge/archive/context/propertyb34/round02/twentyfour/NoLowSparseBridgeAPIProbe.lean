import Aris4Math.ThirtyFour.TwentyFourNoLowCoverageData

namespace Aris4Math.ThirtyFour.TwentyFourSparseDecode
variable {α : Type*} [DecidableEq α]

def support : List (α×ℕ)→List ℕ→Finset α
  | (a,_)::es,k::ks => if k=0 then support es ks else insert a (support es ks)
  | _,_ => ∅

theorem support_subset (es : List (α×ℕ)) (ks : List ℕ) :
    ∀a∈support es ks,a∈es.map Prod.fst := by
  induction es generalizing ks with
  | nil => simp [support]
  | cons e es ih =>
    cases ks with
    | nil => simp [support]
    | cons k ks =>
      intro a ha
      simp only [support] at ha
      split_ifs at ha with hk
      · exact List.mem_cons_of_mem _ (ih ks a ha)
      · rcases Finset.mem_insert.mp ha with rfl|ha
        · exact List.mem_cons_self
        · exact List.mem_cons_of_mem _ (ih ks a ha)

/-- A binary allocation on distinct types is exactly its sparse support.
The two lists need not have equal lengths: both decoders stop at either end. -/
theorem decode_indicator (es : List (α×ℕ)) (ks : List ℕ)
    (nodup : (es.map Prod.fst).Nodup) (binary : ∀k∈ks,k≤1) (a : α) :
    BoundedAllocations.decode es ks a=if a∈support es ks then 1 else 0 := by
  induction es generalizing ks with
  | nil => simp [BoundedAllocations.decode,support]
  | cons e es ih =>
    cases ks with
    | nil => simp [BoundedAllocations.decode,support]
    | cons k ks =>
      obtain ⟨absent,nd⟩ := List.nodup_cons.mp nodup
      have small : k≤1 := binary k List.mem_cons_self
      have rest : ∀k∈ks,k≤1 := fun k hk=>binary k (List.mem_cons_of_mem _ hk)
      have tail := ih ks nd rest
      by_cases eq : a=e.1
      · subst a
        have outside : e.1∉support es ks := fun h=>absent (support_subset es ks e.1 h)
        rcases Nat.le_one_iff_eq_zero_or_eq_one.mp small with rfl|rfl
        · simp [BoundedAllocations.decode,support,outside]
        · simp [BoundedAllocations.decode,support]
      · rw [BoundedAllocations.decode,if_neg eq]
        by_cases zero : k=0
        · simp only [support,if_pos zero]
          exact tail
        · simp only [support,if_neg zero,Finset.mem_insert,eq,false_or]
          exact tail
end Aris4Math.ThirtyFour.TwentyFourSparseDecode
#print axioms Aris4Math.ThirtyFour.TwentyFourSparseDecode.decode_indicator
namespace Aris4Math.ThirtyFour.TwentyFourNoLowCoverage
open TwentyFourNoLowSixData
open TwentyFourSparseDecode
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def profileHigh : Case→Finset (Finset (Fin 6)) := ![∅,{{3,4,5}},{{2,3,4,5}},{{2,3,5},{1,4,5}},{{1,3,5},{0,4,5},{2,3,4}},{{1,2,3},{0,4,5}},{{1,2,3,4,5}},{{1,2,3,5},{0,4,5}},{{1,2,5},{0,3,5},{0,2,4},{1,3,4}},∅,{{3,4,5}},{{1,4,5}},{{2,3,4,5}},{{2,3,5},{1,4,5}},{{1,3,4,5}},{{1,3,5},{0,4,5}},{{1,3,5},{0,4,5},{2,3,4}},{{1,2,5},{1,3,4}},{{1,2,5},{0,4,5},{1,3,4}},{{1,2,3},{0,4,5}},{{1,2,3,4,5}},{{1,2,3,5},{0,4,5}},{{1,2,5},{0,3,5},{0,2,4},{1,3,4}},{{0,1,5}},{{0,1,5},{3,4,5}},{{0,1,4,5}},{{0,1,5},{2,3,4}},{{0,1,5},{2,3,4,5}},{{2,3,5},{0,1,4,5}},{{0,1,5},{1,3,4}},{{0,1,5},{2,4,5},{1,3,4}},{{0,1,3,4,5}},{{1,2,3},{0,1,4,5}},{{0,1,5},{1,2,3,4}},{{1,2,5},{0,3,5},{0,1,4}},{{1,2,5},{0,3,5},{0,1,4},{2,3,4}},{{0,1,5},{0,1,4}},{{0,1,5},{0,1,4},{3,4,5}},{{0,1,5},{2,3,5},{0,1,4}},{{0,1,5},{0,1,4},{2,3,4,5}},{{0,1,3},{0,1,4,5}},{{0,1,3},{2,3,5},{0,1,4,5}},{{0,1,5},{1,2,3},{0,1,4}},{{0,1,5},{1,2,3},{0,1,4},{3,4,5}},{{0,1,2},{0,1,3,4,5}},{{0,1,2,5},{0,1,3,4}}]
def CheapMatch (b : Bool) (values : List ℕ) (selected : Case×Perm) : Prop :=
  (∀k∈values,k≤1) ∧ extraPair selected.1=b ∧
  (b=true→({0,1} : Finset (Fin 6)).map (perm selected.2).toEmbedding={0,1}) ∧
  support entries values=(profileHigh selected.1).image (fun T=>T.map (perm selected.2).toEmbedding)
instance (b : Bool) (values : List ℕ) (selected : Case×Perm) : Decidable (CheapMatch b values selected) := by unfold CheapMatch;infer_instance
def sparseValues0 : List ℕ := [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
theorem cheap0 : CheapMatch true sparseValues0 (39,60) := by decide +kernel
def sparseValues1 : List ℕ := [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
theorem cheap1 : CheapMatch true sparseValues1 (39,120) := by decide +kernel
def sparseValues2 : List ℕ := [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
theorem cheap2 : CheapMatch true sparseValues2 (39,0) := by decide +kernel
def sparseValues3 : List ℕ := [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
theorem cheap3 : CheapMatch true sparseValues3 (20,1) := by decide +kernel
def sparseValues4 : List ℕ := [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
theorem cheap4 : CheapMatch true sparseValues4 (20,0) := by decide +kernel
private theorem entries_nodup_sparse : (entries.map Prod.fst).Nodup := by decide +kernel
variable (profile_high_correct : ∀i T,3≤T.card→
    μ i T=if T∈profileHigh i then 1 else 0)
include profile_high_correct in

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
