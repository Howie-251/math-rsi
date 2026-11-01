import Aris4Math.ThirtyThree.TwentyThreeLowUnitSixCatalogData
import Aris4Math.ThirtyThree.TwentyThreeLowUnitSixHighCatalog
namespace Aris4Math.ThirtyThree.TwentyThreeLowUnitSixCatalog
open scoped BigOperators
open TwentyThreeLowUnitSixCatalogData
open TwentyThreeLowUnitSixHighCatalog
set_option maxHeartbeats 0
set_option maxRecDepth 100000
def capacity (e : Fin 3) (p : Fin 15) : ℕ := pairDegree e (first p) (second p)
def Admissible (e : Fin 3) (F : Finset (Fin 41)) : Prop :=
  ∀ p, ∑ a ∈ F, cost a p ≤ capacity e p
theorem capacity_le : ∀ e p, capacity e p ≤ maximum p := by decide +kernel
def Choice (e : Fin 3) (s : Fin 611) : Prop :=
  Admissible e (catalog s) →
    let c := winner e s
    let σ := permutation (perm e s)
    extra c = e ∧ (∀ i, degreeData (σ i) = degreeData i) ∧
      (∀ i j, pairDegree e (σ i) (σ j) = pairDegree e i j) ∧
      (largeFamily c).image (fun T => T.image σ) = (catalog s).image largeType

def blockIndex (b : Fin 10) (t : Fin 64) : Fin 611 :=
  ⟨(64*b.val+t.val)%611, Nat.mod_lt _ (by decide)⟩

theorem choice_0_0 : ∀ t : Fin 64, Choice 0 (blockIndex 0 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_0_1 : ∀ t : Fin 64, Choice 0 (blockIndex 1 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_0_2 : ∀ t : Fin 64, Choice 0 (blockIndex 2 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_0_3 : ∀ t : Fin 64, Choice 0 (blockIndex 3 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_0_4 : ∀ t : Fin 64, Choice 0 (blockIndex 4 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_0_5 : ∀ t : Fin 64, Choice 0 (blockIndex 5 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_0_6 : ∀ t : Fin 64, Choice 0 (blockIndex 6 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_0_7 : ∀ t : Fin 64, Choice 0 (blockIndex 7 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_0_8 : ∀ t : Fin 64, Choice 0 (blockIndex 8 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_0_9 : ∀ t : Fin 64, Choice 0 (blockIndex 9 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_1_0 : ∀ t : Fin 64, Choice 1 (blockIndex 0 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_1_1 : ∀ t : Fin 64, Choice 1 (blockIndex 1 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_1_2 : ∀ t : Fin 64, Choice 1 (blockIndex 2 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_1_3 : ∀ t : Fin 64, Choice 1 (blockIndex 3 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_1_4 : ∀ t : Fin 64, Choice 1 (blockIndex 4 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_1_5 : ∀ t : Fin 64, Choice 1 (blockIndex 5 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_1_6 : ∀ t : Fin 64, Choice 1 (blockIndex 6 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_1_7 : ∀ t : Fin 64, Choice 1 (blockIndex 7 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_1_8 : ∀ t : Fin 64, Choice 1 (blockIndex 8 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_1_9 : ∀ t : Fin 64, Choice 1 (blockIndex 9 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_2_0 : ∀ t : Fin 64, Choice 2 (blockIndex 0 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_2_1 : ∀ t : Fin 64, Choice 2 (blockIndex 1 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_2_2 : ∀ t : Fin 64, Choice 2 (blockIndex 2 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_2_3 : ∀ t : Fin 64, Choice 2 (blockIndex 3 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_2_4 : ∀ t : Fin 64, Choice 2 (blockIndex 4 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_2_5 : ∀ t : Fin 64, Choice 2 (blockIndex 5 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_2_6 : ∀ t : Fin 64, Choice 2 (blockIndex 6 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_2_7 : ∀ t : Fin 64, Choice 2 (blockIndex 7 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_2_8 : ∀ t : Fin 64, Choice 2 (blockIndex 8 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_2_9 : ∀ t : Fin 64, Choice 2 (blockIndex 9 t) := by
  unfold Choice Admissible
  decide +kernel

theorem choice_block (e : Fin 3) (b : Fin 10) : ∀ t : Fin 64, Choice e (blockIndex b t) := by
  fin_cases e <;> fin_cases b <;> first
  | exact choice_0_0
  | exact choice_0_1
  | exact choice_0_2
  | exact choice_0_3
  | exact choice_0_4
  | exact choice_0_5
  | exact choice_0_6
  | exact choice_0_7
  | exact choice_0_8
  | exact choice_0_9
  | exact choice_1_0
  | exact choice_1_1
  | exact choice_1_2
  | exact choice_1_3
  | exact choice_1_4
  | exact choice_1_5
  | exact choice_1_6
  | exact choice_1_7
  | exact choice_1_8
  | exact choice_1_9
  | exact choice_2_0
  | exact choice_2_1
  | exact choice_2_2
  | exact choice_2_3
  | exact choice_2_4
  | exact choice_2_5
  | exact choice_2_6
  | exact choice_2_7
  | exact choice_2_8
  | exact choice_2_9

theorem choice_exact (e : Fin 3) (s : Fin 611) : Choice e s := by
  let b : Fin 10 := ⟨s.val / 64, by omega⟩
  let t : Fin 64 := ⟨s.val % 64, Nat.mod_lt _ (by decide)⟩
  have eq : blockIndex b t = s := by
    apply Fin.ext
    dsimp [blockIndex,b,t]
    omega
  simpa only [eq] using choice_block e b t


theorem classify (e : Fin 3) (F : Finset (Fin 41)) (budget : Admissible e F) :
    ∃ c : Case, ∃ σ : Fin 6 ≃ Fin 6,
      extra c = e ∧ (∀ i, degreeData (σ i) = degreeData i) ∧
        (∀ i j, pairDegree e (σ i) (σ j) = pairDegree e i j) ∧
        (largeFamily c).image (fun T => T.image σ) = F.image largeType := by
  obtain ⟨s,rfl⟩ := covers F (fun p => (budget p).trans (capacity_le e p))
  exact ⟨winner e s,permutation (perm e s),choice_exact e s budget⟩

end Aris4Math.ThirtyThree.TwentyThreeLowUnitSixCatalog
#print axioms Aris4Math.ThirtyThree.TwentyThreeLowUnitSixCatalog.classify
