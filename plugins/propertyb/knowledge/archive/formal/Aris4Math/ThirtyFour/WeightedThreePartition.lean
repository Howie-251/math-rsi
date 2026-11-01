import Mathlib.Data.Finset.Max
import Mathlib.Data.Fintype.Pi
import Mathlib.Data.Fintype.Card
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Group.Finset.Piecewise
import Lean.Elab.Tactic.Omega

/-! A three-part partition of a symmetric loop-free natural-weight graph of
weighted degree at most five. Minimizing the sum of internal edge weights
forces internal weighted degree at most one at every vertex. -/

namespace Aris4Math.ThirtyFour.WeightedThreePartition

open scoped BigOperators

variable {V : Type*} [Fintype V] [DecidableEq V]

def colorWeight (w : V → V → ℕ) (color : V → Fin 3) (x : V) (k : Fin 3) : ℕ :=
  ∑ y : V, if color y=k then w x y else 0

def monoWeight (w : V → V → ℕ) (color : V → Fin 3) (x y : V) : ℕ :=
  if color x=color y then w x y else 0

def energy (w : V → V → ℕ) (color : V → Fin 3) : ℕ :=
  ∑ x : V, ∑ y : V, monoWeight w color x y

def restEnergy (w : V → V → ℕ) (color : V → Fin 3) (x : V) : ℕ :=
  ∑ u ∈ Finset.univ.erase x, ∑ v ∈ Finset.univ.erase x, monoWeight w color u v

omit [Fintype V] [DecidableEq V] in
theorem monoWeight_symm (w : V → V → ℕ) (symmetric : ∀ x y, w x y=w y x)
    (color : V → Fin 3) (x y : V) :
    monoWeight w color x y=monoWeight w color y x := by
  by_cases same : color x=color y
  · simp only [monoWeight,if_pos same,if_pos same.symm]
    exact symmetric x y
  · simp only [monoWeight,if_neg same,if_neg (Ne.symm same)]

omit [DecidableEq V] in
theorem row_sum (w : V → V → ℕ) (color : V → Fin 3) (x : V) :
    (∑ y : V, monoWeight w color x y)=colorWeight w color x (color x) := by
  simp only [monoWeight,colorWeight,eq_comm]

/-- The total energy contains each incident monochromatic weight in both
orientations; everything else lies in the complement of x. -/
theorem energy_at_vertex (w : V → V → ℕ) (symmetric : ∀ x y, w x y=w y x)
    (zero : ∀ x, w x x=0) (color : V → Fin 3) (x : V) :
    energy w color=restEnergy w color x+2*colorWeight w color x (color x) := by
  have diagonal : monoWeight w color x x=0 := by simp [monoWeight,zero x]
  have rowErase := Finset.sum_erase_add (s := Finset.univ)
    (fun y => monoWeight w color x y) (Finset.mem_univ x)
  dsimp only at rowErase
  rw [diagonal,Nat.add_zero,row_sum] at rowErase
  have column : (∑ u ∈ Finset.univ.erase x, monoWeight w color u x)=
      colorWeight w color x (color x) := by
    calc
      _ = ∑ u ∈ Finset.univ.erase x, monoWeight w color x u :=
        Finset.sum_congr rfl (fun u _ => monoWeight_symm w symmetric color u x)
      _ = _ := rowErase
  have outer := Finset.sum_erase_add (s := Finset.univ)
    (fun u => ∑ v : V, monoWeight w color u v) (Finset.mem_univ x)
  dsimp only at outer
  have inner : (∑ u ∈ Finset.univ.erase x, ∑ v : V, monoWeight w color u v)=
      restEnergy w color x+∑ u ∈ Finset.univ.erase x, monoWeight w color u x := by
    calc
      _ = ∑ u ∈ Finset.univ.erase x,
          ((∑ v ∈ Finset.univ.erase x, monoWeight w color u v)+monoWeight w color u x) := by
        apply Finset.sum_congr rfl
        intro u _
        exact (Finset.sum_erase_add (s := Finset.univ)
          (fun v => monoWeight w color u v) (Finset.mem_univ x)).symm
      _ = _ := Finset.sum_add_distrib
  rw [inner,column,row_sum] at outer
  change restEnergy w color x+colorWeight w color x (color x)+
    colorWeight w color x (color x)=energy w color at outer
  omega

theorem restEnergy_update (w : V → V → ℕ) (color : V → Fin 3) (x : V) (k : Fin 3) :
    restEnergy w (Function.update color x k) x=restEnergy w color x := by
  apply Finset.sum_congr rfl
  intro u hu
  apply Finset.sum_congr rfl
  intro v hv
  have ux := (Finset.mem_erase.mp hu).1
  have vx := (Finset.mem_erase.mp hv).1
  simp [monoWeight,Function.update_of_ne ux,Function.update_of_ne vx]

theorem colorWeight_update (w : V → V → ℕ) (zero : ∀ x, w x x=0)
    (color : V → Fin 3) (x : V) (k : Fin 3) :
    colorWeight w (Function.update color x k) x k=colorWeight w color x k := by
  apply Finset.sum_congr rfl
  intro y _
  by_cases same : y=x
  · subst y
    simp [zero]
  · simp [Function.update_of_ne same]

/-- Moving x changes only its incident weights. The two color-class weights
on the right are evaluated in the original coloring. -/
theorem energy_update_balance (w : V → V → ℕ) (symmetric : ∀ x y, w x y=w y x)
    (zero : ∀ x, w x x=0) (color : V → Fin 3) (x : V) (k : Fin 3) :
    energy w (Function.update color x k)+2*colorWeight w color x (color x)=
      energy w color+2*colorWeight w color x k := by
  rw [energy_at_vertex w symmetric zero (Function.update color x k) x,
    energy_at_vertex w symmetric zero color x,Function.update_self,
    restEnergy_update,colorWeight_update w zero]
  omega

omit [DecidableEq V] in
theorem colorWeight_sum (w : V → V → ℕ) (color : V → Fin 3) (x : V) :
    (∑ k : Fin 3, colorWeight w color x k)=∑ y : V, w x y := by
  unfold colorWeight
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro y _
  simp

/-- A minimum-energy three-class partition has internal weighted degree at
most one whenever the total weighted degree at each vertex is at most five. -/
theorem exists_three_part_defect_one (w : V → V → ℕ)
    (symmetric : ∀ x y, w x y=w y x) (zero : ∀ x, w x x=0)
    (maximum : ∀ x, (∑ y : V, w x y) ≤ 5) :
    ∃ color : V → Fin 3, ∀ x, colorWeight w color x (color x) ≤ 1 := by
  classical
  obtain ⟨color,_,minimal⟩ := Finset.exists_min_image (Finset.univ : Finset (V → Fin 3))
    (energy w) ⟨fun _ => 0,Finset.mem_univ _⟩
  refine ⟨color,?_⟩
  intro x
  have each (k : Fin 3) : colorWeight w color x (color x) ≤ colorWeight w color x k := by
    have compare := minimal (Function.update color x k) (Finset.mem_univ _)
    have balance := energy_update_balance w symmetric zero color x k
    omega
  have hsum := Finset.sum_le_sum (s := Finset.univ) (fun k _ => each k)
  rw [colorWeight_sum w color x] at hsum
  have hmax := maximum x
  simp only [Finset.sum_const,Finset.card_univ,Fintype.card_fin,Nat.nsmul_eq_mul] at hsum
  omega

end Aris4Math.ThirtyFour.WeightedThreePartition

#print axioms Aris4Math.ThirtyFour.WeightedThreePartition.energy_update_balance
#print axioms Aris4Math.ThirtyFour.WeightedThreePartition.exists_three_part_defect_one
