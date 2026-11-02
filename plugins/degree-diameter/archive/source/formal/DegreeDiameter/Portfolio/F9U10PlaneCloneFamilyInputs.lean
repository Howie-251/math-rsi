import DegreeDiameter.Portfolio.F9U10PlaneCloneFamilyDefinitions
import DegreeDiameter.Portfolio.F9SixFiberDouble56Inputs
namespace DegreeDiameter.Portfolio.F9U10PlaneCloneFamily
open F9Graph56862
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
/-- A60-entry partial inverse certificate, avoiding a repeated60×60 target comparison. -/
def targetOwner : Fin 78 → Option (Fin 10 × Fin 6) := ![some (0,4), some (1,4), none, none, none, some (0,3), some (1,3), some (4,2), some (5,2), some (6,2), some (7,5), some (8,5), some (9,5), some (2,4), some (3,4), none, none, none, some (2,3), some (3,3), some (7,2), some (8,2), some (9,2), some (4,5), some (5,5), some (6,5), some (6,0), some (4,1), some (5,1), some (6,1), none, some (2,5), some (3,5), some (4,3), some (5,3), some (6,3), none, some (7,0), some (8,0), some (9,0), some (7,1), some (8,1), some (9,1), none, some (0,5), some (1,5), some (7,3), some (8,3), some (9,3), none, some (4,0), some (5,0), none, some (2,1), some (3,1), none, none, some (0,2), some (1,2), some (7,4), some (8,4), some (9,4), none, some (0,0), some (1,0), none, some (0,1), some (1,1), none, none, some (2,2), some (3,2), some (4,4), some (5,4), some (6,4), none, some (2,0), some (3,0)]
theorem target_owner : ∀ (u : Fin 10) (p : Fin 6),
    targetOwner (controller (chosenFiber u) p) = some (u,p) := by decide +kernel
theorem controller_targets_injective : Function.Injective
    (fun ip : Fin 10 × Fin 6 => controller (chosenFiber ip.1) ip.2) := by
  rintro ⟨u,p⟩ ⟨v,q⟩ h
  have ho := congrArg targetOwner h
  simp only [target_owner] at ho
  exact Option.some.inj ho
theorem common_base_pin_index_unique (w : Fin 56862) (i j : BaseIndex)
    (hi : F9Graph56862.graph.Adj w (baseCenter i))
    (hj : F9Graph56862.graph.Adj w (baseCenter j)) : i = j := by
  apply basePair.injective
  exact F9SixFiberDouble56.common_plane_pin_index_unique chosenFiber controller_targets_injective
    w (basePair i) (basePair j) hi hj
theorem base_load_le_one (w : Fin 56862) : FullNeighborhoodClones.load F9Graph56862.graph baseCenter w ≤ 1 := by
  apply Fintype.card_le_one_iff.mpr
  intro x y
  apply Subtype.ext
  exact common_base_pin_index_unique w x.val y.val x.property y.property
theorem copy_load_le (k : Nat) (w : Fin 56862) : FullNeighborhoodClones.load F9Graph56862.graph (center k) w ≤ k := by
  have hbase : ∀ x y : {b : BaseIndex // F9Graph56862.graph.Adj w (baseCenter b)}, x = y :=
    Fintype.card_le_one_iff.mp (base_load_le_one w)
  let copyIndex : {j : Fin k × BaseIndex // F9Graph56862.graph.Adj w (center k j)} → Fin k := fun j => j.val.1
  have hinj : Function.Injective copyIndex := by
    intro x y hcopy
    have hbaseval : x.val.2 = y.val.2 :=
      congrArg Subtype.val (hbase ⟨x.val.2,x.property⟩ ⟨y.val.2,y.property⟩)
    apply Subtype.ext
    exact Prod.ext hcopy hbaseval
  have h := Fintype.card_le_of_injective copyIndex hinj
  simpa only [Fintype.card_fin] using h
#print axioms target_owner
#print axioms base_load_le_one
#print axioms copy_load_le
end DegreeDiameter.Portfolio.F9U10PlaneCloneFamily
