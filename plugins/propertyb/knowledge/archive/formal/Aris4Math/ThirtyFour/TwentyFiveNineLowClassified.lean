import Aris4Math.ThirtyFour.TwentyFiveUnit9Actual
import Aris4Math.ThirtyFour.TwentyFiveNineLowClassifiedBatch0
import Aris4Math.ThirtyFour.TwentyFiveNineLowClassifiedBatch1
import Aris4Math.ThirtyFour.TwentyFiveNineLowClassifiedBatch2
import Aris4Math.ThirtyFour.TwentyFiveNineLowClassifiedBatch3
import Aris4Math.ThirtyFour.TwentyFiveNineLowClassifiedBatch4
import Aris4Math.ThirtyFour.TwentyFiveNineLowClassifiedBatch5
namespace Aris4Math.ThirtyFour.TwentyFiveNineLowClassified
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitCounts TwentyFiveConditionalRows TwentyFiveNineLowClassifiedData
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem sources : rows.map FamilyRow.source=List.ofFn TwentyFiveUnit9Data.catalogue := by decide +kernel

theorem checked : rows.all (fun r => decide (FamilyCheck (fun _ => 6) TwentyFiveNineLowInventory.big r))=true := by
  simp only [rows,List.all_append,TwentyFiveNineLowClassifiedBatch0.checked,TwentyFiveNineLowClassifiedBatch1.checked,TwentyFiveNineLowClassifiedBatch2.checked,TwentyFiveNineLowClassifiedBatch3.checked,TwentyFiveNineLowClassifiedBatch4.checked,TwentyFiveNineLowClassifiedBatch5.checked,Bool.true_and]

theorem feasible_case (c : Fin 374)
    (feasible : Feasible 34 (fun _ => 6) (pairCompletion (TwentyFiveUnit9Data.catalogue c))) :
    ∃ d : Fin 147, TwentyFiveUnit9Data.catalogue c=TwentyFiveNineLowInventory.big d := by
  have mem : TwentyFiveUnit9Data.catalogue c∈rows.map FamilyRow.source := by
    rw [sources]
    exact List.mem_ofFn.mpr ⟨c,rfl⟩
  obtain ⟨r,mem,same⟩ := List.mem_map.mp mem
  have quick := of_decide_eq_true (List.all_eq_true.mp checked r mem)
  refine ⟨r.target,?_⟩
  rw [← same] at feasible ⊢
  exact family_sound (fun _ => 6) TwentyFiveNineLowInventory.big r quick feasible

/-- Every actual nine-low unit choice is represented with its true counts. -/
theorem actual (H : Simple5Hypergraph (Fin 25)) (edges : H.edges.card=34)
    (f : Fin 9 ↪ Fin 25) (unit : Unit H f) (degrees : ∀ i, H.degree (f i)=6) :
    ∃ c : Fin 147, ∃ σ : Equiv.Perm (Fin 9),
      large H (σ.toEmbedding.trans f)=TwentyFiveNineLowInventory.big c ∧
      (∀ T, count H (σ.toEmbedding.trans f) T=TwentyFiveNineLow.μ c T) := by
  obtain ⟨c,σ,same⟩ := TwentyFiveUnit9Actual.actual H f unit
  let g := σ.toEmbedding.trans f
  have gUnit : Unit H g := unit_relabel H f unit σ
  obtain ⟨counts,feasible⟩ := actual_inventory H g gUnit (fun _ => 6) (fun i => degrees (σ i))
  rw [edges,show large H g=TwentyFiveUnit9Data.catalogue c from same] at counts feasible
  obtain ⟨d,normal⟩ := feasible_case c feasible
  refine ⟨d,σ,same.trans normal,?_⟩
  intro T
  rw [counts T,normal]
  exact TwentyFiveNineLowInventory.recovered d T
end Aris4Math.ThirtyFour.TwentyFiveNineLowClassified
