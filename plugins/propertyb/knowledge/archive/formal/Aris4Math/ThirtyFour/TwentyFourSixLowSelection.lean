import Aris4Math.ThirtyFour.TwentyFourSixLowPairPatterns
namespace Aris4Math.ThirtyFour.TwentyFourSixLowSelection
open TwentyFourSixLowPairPatterns
open Aris4Math.ThirtyThree.TwentyFourSelection
set_option maxHeartbeats 2000000
variable (H : Simple5Hypergraph (Fin 24))

/-- Select six genuine low vertices, retaining the prescribed nonunit pair,
then normalize the disjoint nonunit pairs on the other four vertices. -/
theorem exists_labeled (cover : H.PairCovering) (many : 6≤H.sixVertices.card)
    (bad : ∃x∈H.sixVertices,∃y∈H.sixVertices,x≠y ∧ H.codegree x y≠1) :
    ∃f : Fin 6↪Fin 24,∃b : Pattern,(∀i,H.degree (f i)=6) ∧
      (∀i j,i≠j→H.codegree (f i) (f j)=
        if ({i,j} : Finset (Fin 6))={0,1} ∨
          (1≤b.val ∧ ({i,j} : Finset (Fin 6))={2,3}) ∨
          (2≤b.val ∧ ({i,j} : Finset (Fin 6))={4,5}) then 2 else 1) := by
  classical
  obtain ⟨x,hx,y,hy,xy,nonunit⟩ := bad
  have dx : H.degree x=6 := (Finset.mem_filter.mp hx).2
  have dy : H.degree y=6 := (Finset.mem_filter.mp hy).2
  have two : H.codegree x y=2 := by
    have lo := H.one_le_codegree cover xy
    have hi := six_codegree_le_two H cover (by simp) dx xy
    omega
  have rem : 4≤(H.sixVertices\{x,y}).card := by
    have sub : ({x,y} : Finset (Fin 24))⊆H.sixVertices := by
      intro z hz
      rcases Finset.mem_insert.mp hz with rfl|hz
      · exact hx
      · exact (Finset.mem_singleton.mp hz) ▸ hy
    have eq := Finset.card_sdiff_add_card_eq_card sub
    have card : ({x,y} : Finset (Fin 24)).card=2 := by simp [xy]
    omega
  obtain ⟨S,sub,card⟩ := Finset.exists_subset_card_eq rem
  let e : ↥S≃Fin 4 := Fintype.equivFinOfCardEq (by simpa using card)
  let g : Fin 4↪Fin 24 := ⟨fun i=>(e.symm i).val,Subtype.val_injective.comp e.symm.injective⟩
  have mem (i : Fin 4) := Finset.mem_sdiff.mp (sub (e.symm i).property)
  have gd (i : Fin 4) : H.degree (g i)=6 := (Finset.mem_filter.mp (mem i).1).2
  have gx (i : Fin 4) : g i≠x := by simpa [g] using (not_or.mp (by simpa using (mem i).2)).1
  have gy (i : Fin 4) : g i≠y := by simpa [g] using (not_or.mp (by simpa using (mem i).2)).2
  have xg (i : Fin 4) : H.codegree x (g i)=1 :=
    unit_of_other_bad H cover (by simp) dx xy (by omega) (gx i).symm (gy i).symm
  have yg (i : Fin 4) : H.codegree y (g i)=1 :=
    unit_of_other_bad H cover (by simp) dy xy.symm
      (by simpa only [H.codegree_comm y x] using (show 2≤H.codegree x y by omega))
      (gy i).symm (gx i).symm
  let r : Fin 6→Bool := fun k=>decide (H.codegree (g (first k)) (g (second k))=2)
  have actual (i j : Fin 4) (ij : i≠j) : adj r i j=decide (H.codegree (g i) (g j)=2) := by
    fin_cases i <;> fin_cases j <;> first
      | exact (ij rfl).elim
      | rfl
      | exact congrArg (fun n=>decide (n=2)) (H.codegree_comm _ _)
  have matching : IsMatching r := by
    intro i j k ij ik a b
    have aa : H.codegree (g i) (g j)=2 := by simpa only [actual i j ij,decide_eq_true_eq] using a
    have bb : H.codegree (g i) (g k)=2 := by simpa only [actual i k ik,decide_eq_true_eq] using b
    by_contra jk
    have one := unit_of_other_bad H cover (by simp) (gd i) (g.injective.ne ij)
      (by omega) (g.injective.ne ik) (g.injective.ne jk)
    omega
  obtain ⟨b,p,normalized⟩ := normalize r matching
  let σ := perm p
  let h := σ.toEmbedding.trans g
  have hd (i : Fin 4) : H.degree (h i)=6 := gd (σ i)
  have hx' (i : Fin 4) : h i≠x := gx (σ i)
  have hy' (i : Fin 4) : h i≠y := gy (σ i)
  have xh (i : Fin 4) : H.codegree x (h i)=1 := xg (σ i)
  have yh (i : Fin 4) : H.codegree y (h i)=1 := yg (σ i)
  have hh (i j : Fin 4) (ij : i≠j) : H.codegree (h i) (h j)=
      if canonical b i j then 2 else 1 := by
    have eq := normalized i j ij
    rw [actual _ _ (σ.injective.ne ij)] at eq
    have lo := H.one_le_codegree cover (h.injective.ne ij)
    have hi := six_codegree_le_two H cover (by simp) (hd i) (h.injective.ne ij)
    change decide (H.codegree (h i) (h j)=2)=canonical b i j at eq
    cases value : canonical b i j
    · rw [value] at eq
      have ne : H.codegree (h i) (h j)≠2 := by simpa only [decide_eq_false_iff_not] using eq
      simp only [Bool.false_eq_true,↓reduceIte]
      omega
    · rw [value] at eq
      have yes : H.codegree (h i) (h j)=2 := by simpa only [decide_eq_true_eq] using eq
      exact yes
  let f0 : Fin 6→Fin 24 := ![x,y,h 0,h 1,h 2,h 3]
  have distinct : ∀i j : Fin 4,i≠j→h i≠h j := fun i j ne=>h.injective.ne ne
  have injective : Function.Injective f0 := by
    intro i j eq
    fin_cases i <;> fin_cases j <;> simp only [f0,Matrix.cons_val_zero,Matrix.cons_val_one,Matrix.cons_val_succ] at eq <;> first
      | rfl
      | exact (xy eq).elim
      | exact (xy eq.symm).elim
      | exact (hx' _ eq).elim
      | exact (hx' _ eq.symm).elim
      | exact (hy' _ eq).elim
      | exact (hy' _ eq.symm).elim
      | (have impossible := h.injective eq; contradiction)
  let f : Fin 6↪Fin 24 := ⟨f0,injective⟩
  refine ⟨f,b,?_,?_⟩
  · intro i
    fin_cases i <;> simp [f,f0,dx,dy,hd]
  · intro i j ij
    have yx := (H.codegree_comm y x).trans two
    have hxUnit (i : Fin 4) := (H.codegree_comm (h i) x).trans (xh i)
    have hyUnit (i : Fin 4) := (H.codegree_comm (h i) y).trans (yh i)
    fin_cases i <;> fin_cases j <;> first
      | exact (ij rfl).elim
      | (simp [f,f0,two,yx,xh,yh,hxUnit,hyUnit,hh,canonical] <;> fin_cases b <;> decide)
end Aris4Math.ThirtyFour.TwentyFourSixLowSelection
#print axioms Aris4Math.ThirtyFour.TwentyFourSixLowSelection.exists_labeled
