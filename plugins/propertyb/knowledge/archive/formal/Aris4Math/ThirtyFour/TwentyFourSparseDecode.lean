import Aris4Math.ThirtyFour.BoundedAllocations

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
