import Aris4Math.ThirtyFour.WeightedSubsetSelection

/-! Minimum-degree deletion proves the sparse-graph independent-set bound.
The graph is arbitrary; there is no enumeration of graphs. -/
namespace Aris4Math.ThirtyFour.TwentyFourSparseGraph
open scoped BigOperators
open WeightedSubsetSelection
variable {V : Type*} [DecidableEq V]
variable (R : V → V → Prop) [DecidableRel R]

def weight (x y : V) : ℕ := if R x y then 1 else 0
def Independent (S : Finset V) : Prop := ∀ x∈S, ∀ y∈S, ¬ R x y
def NoIndependent (S : Finset V) (k : ℕ) : Prop :=
  ¬ ∃ T⊆S, T.card=k ∧ Independent R T

theorem neighbors_card (S : Finset V) (x : V) :
    (S.filter (R x)).card=degree (weight R) S x := by
  simp [degree,weight]

theorem energy_remove (S C : Finset V) (sub : C⊆S) (d : ℕ)
    (minimum : ∀ x∈C,d≤degree (weight R) S x) :
    d*C.card+energy (weight R) (S\C)≤energy (weight R) S := by
  have parts : (∑ x∈C,degree (weight R) S x)+
      (∑ x∈S\C,degree (weight R) S x)=energy (weight R) S := by
    rw [←Finset.sum_union Finset.sdiff_disjoint.symm,Finset.union_sdiff_of_subset sub]
    rfl
  have low : d*C.card≤∑ x∈C,degree (weight R) S x := by
    calc
      _ = ∑ _x∈C,d := by simp [Nat.mul_comm]
      _ ≤ _ := Finset.sum_le_sum minimum
  have remain : energy (weight R) (S\C)≤∑ x∈S\C,degree (weight R) S x := by
    apply Finset.sum_le_sum
    intro x _
    exact Finset.sum_le_sum_of_subset Finset.sdiff_subset
  exact (Nat.add_le_add low remain).trans_eq parts

/-- If no independent (k+1)-subset exists, n²≤k(n+2e). -/
theorem no_independent_bound (symm : Symmetric R) (irrefl : Irreflexive R)
    (k : ℕ) (S : Finset V) (absent : NoIndependent R S (k+1)) :
    S.card^2≤k*(S.card+energy (weight R) S) := by
  classical
  induction k generalizing S with
  | zero =>
    have empty : S=∅ := by
      by_contra h
      obtain ⟨x,hx⟩ := Finset.nonempty_iff_ne_empty.mpr h
      apply absent
      refine ⟨{x},Finset.singleton_subset_iff.mpr hx,by simp,?_⟩
      intro a ha b hb
      have ax := Finset.mem_singleton.mp ha
      have bx := Finset.mem_singleton.mp hb
      subst a;subst b
      exact irrefl x
    simp [empty]
  | succ k ih =>
    by_cases empty : S=∅
    · simp [empty]
    obtain ⟨x,hx,minimal⟩ := Finset.exists_min_image S (degree (weight R) S)
      (Finset.nonempty_iff_ne_empty.mpr empty)
    let d := degree (weight R) S x
    let C := insert x (S.filter (R x))
    let A := S\C
    have sub : C⊆S := Finset.insert_subset hx (Finset.filter_subset _ _)
    have xnot : x∉S.filter (R x) := by simp [irrefl x]
    have ccard : C.card=d+1 := by
      simp only [C,Finset.card_insert_of_notMem xnot,neighbors_card,d]
    have cards : A.card+(d+1)=S.card := by
      simpa only [A,←ccard] using Finset.card_sdiff_add_card_eq_card sub
    have smaller : NoIndependent R A (k+1) := by
      rintro ⟨T,tSub,tCard,indep⟩
      have noNeighbor (y : V) (hy : y∈T) : y≠x ∧ ¬R x y := by
        have h := Finset.mem_sdiff.mp (tSub hy)
        have yc : y∉C := h.2
        have yn : y≠x ∧ y∉S.filter (R x) := by simpa only [C,Finset.mem_insert,not_or] using yc
        exact ⟨yn.1,fun edge=>yn.2 (Finset.mem_filter.mpr ⟨h.1,edge⟩)⟩
      have notmem : x∉T := fun h=>(noNeighbor x h).1 rfl
      apply absent
      refine ⟨insert x T,Finset.insert_subset hx (tSub.trans Finset.sdiff_subset),?_,?_⟩
      · simp [notmem,tCard,Nat.add_assoc]
      · intro a ha b hb
        by_cases ax : a=x
        · subst a
          by_cases bx : b=x
          · subst b; exact irrefl _
          · exact (noNeighbor b (Finset.mem_of_mem_insert_of_ne hb bx)).2
        · have haT : a∈T := Finset.mem_of_mem_insert_of_ne ha ax
          by_cases bx : b=x
          · subst b
            exact fun h=>(noNeighbor a haT).2 (symm h)
          · exact indep a haT b (Finset.mem_of_mem_insert_of_ne hb bx)
    have bound := ih A smaller
    have removed := energy_remove R S C sub d (fun y hy=>minimal y (sub hy))
    rw [ccard] at removed
    change d*(d+1)+energy (weight R) A≤energy (weight R) S at removed
    by_cases kz : k=0
    · subst k
      have zero : A.card=0 := by nlinarith [bound]
      rw [zero] at cards
      nlinarith
    · have kp : 0<k := Nat.pos_of_ne_zero kz
      have square : 0≤((k:ℤ)*(d+1)-(A.card:ℤ))^2 := sq_nonneg _
      have c : (S.card:ℤ)=(A.card:ℤ)+(d+1) := by exact_mod_cast cards.symm
      have rem : (d:ℤ)*(d+1)+(energy (weight R) A:ℤ)≤energy (weight R) S := by
        exact_mod_cast removed
      have b : (k:ℤ)*(A.card+(energy (weight R) A))≥(A.card:ℤ)^2 := by
        exact_mod_cast bound
      have kpz : (0:ℤ)<k := by exact_mod_cast kp
      have mulb := mul_nonneg (by omega : (0:ℤ)≤k+1) (sub_nonneg.mpr b)
      have mulrem := mul_nonneg (by positivity : (0:ℤ)≤k*(k+1)) (sub_nonneg.mpr rem)
      have desired : (S.card:ℤ)^2≤((k:ℤ)+1)*(S.card+(energy (weight R) S)) := by
        by_contra h
        have positive : 0<(k:ℤ)*((S.card:ℤ)^2-((k:ℤ)+1)*(S.card+(energy (weight R) S))) :=
          mul_pos kpz (by omega)
        rw [c] at positive
        nlinarith only [mulb,mulrem,square,positive]
      exact_mod_cast desired

end Aris4Math.ThirtyFour.TwentyFourSparseGraph
#print axioms Aris4Math.ThirtyFour.TwentyFourSparseGraph.no_independent_bound
