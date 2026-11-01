import Aris4Math.ThirtyFour.TwentyFiveUnitConditional

/-! A failed degree budget needs only a short list of distinct incident blocks.
The list checker never constructs the full pair completion. -/
namespace Aris4Math.ThirtyFour.TwentyFiveDegreeObstruction
open Aris4Math.K6Classification TwentyFiveUnitCounts
variable {n : ℕ}

def blockCheck (listed : List (Finset (Fin n))) (T : Finset (Fin n)) : Bool :=
  listed.contains T || (decide (T.card=2) && listed.all (fun B => decide (¬ T⊆B)))

theorem block_mem (listed : List (Finset (Fin n))) (T : Finset (Fin n))
    (checked : blockCheck listed T=true) : T∈pairCompletion listed.toFinset := by
  simp only [blockCheck,Bool.or_eq_true,Bool.and_eq_true,List.contains_iff,
    decide_eq_true_eq] at checked
  rcases checked with mem | ⟨size,none⟩
  · exact Finset.mem_union_left _ (List.mem_toFinset.mpr mem)
  · apply Finset.mem_union_right
    apply Finset.mem_filter.mpr
    refine ⟨Finset.mem_powersetCard.mpr ⟨Finset.subset_univ _,size⟩,?_⟩
    intro B mem
    exact of_decide_eq_true (List.all_eq_true.mp none B (List.mem_toFinset.mp mem))

theorem not_feasible (degree : Fin n → ℕ) (listed bad : List (Finset (Fin n)))
    (i : Fin n) (nodup : bad.Nodup) (enough : degree i<bad.length)
    (checked : bad.all (fun T => decide (i∈T) && blockCheck listed T)=true) :
    ¬ Feasible 34 degree (pairCompletion listed.toFinset) := by
  intro feasible
  have subset : bad.toFinset⊆(pairCompletion listed.toFinset).filter (fun T => i∈T) := by
    intro T mem
    have h := List.all_eq_true.mp checked T (List.mem_toFinset.mp mem)
    simp only [Bool.and_eq_true] at h
    rcases h with ⟨through,valid⟩
    exact Finset.mem_filter.mpr ⟨block_mem listed T valid,of_decide_eq_true through⟩
  have lower := Finset.card_le_card subset
  rw [List.toFinset_card_of_nodup nodup] at lower
  exact (not_lt_of_ge (le_trans lower (feasible.1 i))) enough

end Aris4Math.ThirtyFour.TwentyFiveDegreeObstruction

namespace Aris4Math.ThirtyFour.TwentyFiveNineLowTenthInventory
open TwentyFiveUnitCounts Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
def big : Fin 25 → Finset (Finset (Fin 10)) := ![{{6,7,8},{0,1,6},{0,2,7},{0,5,8},{1,4,7},{2,4,8},{4,5,6},{1,3,8},{2,3,6},{3,5,7},{0,3,4,9},{1,2,5,9}},
{{0,1,2},{1,3,5},{1,6,8},{2,5,7},{3,6,7},{0,7,8},{2,4,6},{0,3,4},{4,5,8},{0,5,6,9},{1,4,7,9},{2,3,8,9}},
{{3,7,8},{0,3,4},{1,4,7},{2,4,8},{0,6,7},{1,6,8},{2,3,6},{0,5,8},{1,3,5},{2,5,7},{4,5,6},{0,1,2,9}},
{{6,7,8},{0,1,6},{0,2,7},{0,5,8},{1,4,7},{2,4,8},{4,5,6},{1,3,8},{2,3,6},{3,5,7},{0,3,4,9},{1,2,5,9}},
{{0,1,2},{1,3,5},{1,6,8},{2,5,7},{3,6,7},{0,7,8},{2,4,6},{0,3,4},{4,5,8},{0,5,6,9},{1,4,7,9},{2,3,8,9}},
{{6,7,8},{0,1,6},{0,4,7},{1,5,8},{3,4,8},{2,5,7},{2,3,6},{0,3,5,9},{1,2,4,9}},
{{0,1,2},{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{4,5,8},{1,6,8},{0,7,8},{3,8,9},{4,7,9},{5,6,9}},
{{0,1,3},{0,7,8},{1,6,8},{3,5,7},{3,4,6},{4,5,8},{2,6,7},{1,2,5},{0,2,4},{3,8,9},{4,7,9},{5,6,9}},
{{3,5,8},{1,3,7},{2,5,7},{1,6,8},{2,4,8},{4,6,7},{0,5,6},{0,3,4},{7,8,9},{0,1,2,9}},
{{0,3,5},{3,7,8},{2,5,8},{0,4,7},{1,4,8},{2,6,7},{4,5,6},{1,3,6},{5,7,9},{0,1,2,9},{6,8,9}},
{{0,1,2},{1,5,6},{2,7,8},{3,5,7},{4,6,8},{0,3,4},{0,6,7,9},{1,3,8,9},{2,4,5,9}},
{{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{4,5,8},{1,6,8},{0,7,8},{0,1,2,9},{3,8,9},{4,7,9},{5,6,9}},
{{0,1,2},{0,3,5},{1,3,6},{2,5,8},{2,6,7},{3,7,8},{4,5,6},{1,4,8},{0,4,7},{5,7,9},{6,8,9}},
{{3,6,7},{0,7,8},{1,6,8},{0,3,4},{1,3,5},{4,5,8},{2,4,6},{2,5,7},{0,1,2,9}},
{{6,7,8},{0,1,6},{0,4,7},{1,5,8},{3,4,8},{2,5,7},{2,3,6},{0,3,5,9},{1,2,4,9}},
{{0,1,2},{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{4,5,8},{1,6,8},{0,7,8},{3,8,9},{4,7,9},{5,6,9}},
{{0,1,3},{0,7,8},{1,6,8},{3,5,7},{3,4,6},{4,5,8},{2,6,7},{1,2,5},{0,2,4},{3,8,9},{4,7,9},{5,6,9}},
{{3,5,8},{1,3,7},{2,5,7},{1,6,8},{2,4,8},{4,6,7},{0,5,6},{0,3,4},{7,8,9},{0,1,2,9}},
{{0,3,5},{3,7,8},{2,5,8},{0,4,7},{1,4,8},{2,6,7},{4,5,6},{1,3,6},{5,7,9},{0,1,2,9},{6,8,9}},
{{0,1,2},{1,5,6},{2,7,8},{3,5,7},{4,6,8},{0,3,4},{0,6,7,9},{1,3,8,9},{2,4,5,9}},
{{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{4,5,8},{1,6,8},{0,7,8},{0,1,2,9},{3,8,9},{4,7,9},{5,6,9}},
{{0,3,4},{1,5,6},{4,6,8},{3,5,7},{2,7,8},{0,1,2,9},{4,5,9},{3,8,9},{6,7,9}},
{{0,1,2},{3,4,5},{6,7,8},{0,3,6,9},{1,4,7,9},{2,5,8,9}},
{{0,3,4},{1,5,6},{4,6,8},{3,5,7},{2,7,8},{0,1,2,9},{4,5,9},{3,8,9},{6,7,9}},
{{0,1,2},{3,4,5},{6,7,8},{0,3,6,9},{1,4,7,9},{2,5,8,9}}]

def lastDegree : Fin 25 → ℕ := ![6,6,7,7,7,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,6,6,7,7]
def degrees (c : Fin 25) (i : Fin 10) : ℕ := if i.val<9 then 6 else lastDegree c
end Aris4Math.ThirtyFour.TwentyFiveNineLowTenthInventory

namespace TenthShortProbe
open Aris4Math Aris4Math.ThirtyFour Aris4Math.K6Classification
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue
set_option maxRecDepth 100000
set_option maxHeartbeats 0
def oldBig : Finset (Finset (Fin 9)) := {{0,1,2},{0,3,4},{1,3,5},{2,3,6},{4,5,6},{1,4,7},{2,5,7},{0,6,7},{2,4,8},{0,5,8},{1,6,8},{3,7,8}}
def candidates : List (Finset (Fin 9)) := [{0,1,2},{0,3,4},{1,3,5},{2,3,6},{4,5,6},{1,4,7},{2,5,7},{0,6,7},{2,4,8},{0,5,8},{1,6,8},{3,7,8}]
def chosen0 : Finset (Finset (Fin 9)) := ∅
def witness0 : Witness 10 25 := ⟨0,![0,1,2,3,4,5,6,7,8,9]⟩
set_option profiler true in
theorem test0 : TwentyFiveUnitConditional.Checks (fun _ => 6) TwentyFiveNineLowTenthInventory.big TwentyFiveNineLowTenthInventory.degrees oldBig chosen0 witness0 := by
  intro feasible
  let listed : List (Finset (Fin 10)) := [{0,1,2},{0,3,4},{1,3,5},{2,3,6},{4,5,6},{1,4,7},{2,5,7},{0,6,7},{2,4,8},{0,5,8},{1,6,8},{3,7,8}]
  let bad : List (Finset (Fin 10)) := [{0,9},{1,9},{2,9},{3,9},{4,9},{5,9},{6,9}]
  have same : extend oldBig chosen0=listed.toFinset := by decide +kernel
  rw [same] at feasible
  exact False.elim (TwentyFiveDegreeObstruction.not_feasible (fun _ => 6) listed bad 9
    (by decide +kernel) (by decide +kernel) (by decide +kernel) feasible)
def chosen6 : Finset (Finset (Fin 9)) := {{0,6,7},{2,4,8}}
def witness6 : Witness 10 25 := ⟨0,![0,6,1,7,2,8,4,3,5,9]⟩
set_option profiler true in
theorem test6 : TwentyFiveUnitConditional.Checks (fun _ => 6) TwentyFiveNineLowTenthInventory.big TwentyFiveNineLowTenthInventory.degrees oldBig chosen6 witness6 := by
  intro _
  decide +kernel

end TenthShortProbe
