import Aris4Math.ThirtyFour.TwentyFiveEightLowTenthNumeric0
import Aris4Math.ThirtyFour.TwentyFiveEightLowTenthNumeric1
import Aris4Math.ThirtyFour.TwentyFiveEightLowTenthCoverage
import Aris4Math.ThirtyFour.TwentyFiveEightLowTenthInventory
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowTenthComplete
open Aris4Math.ThirtyThree.MultiLockRecovery TwentyFiveUnitExtension TwentyFiveColoredActual
open TwentyFiveEightLowTenthCoverage
set_option maxHeartbeats 0
set_option maxRecDepth 100000
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 10↪Fin 25)
    (c : Fin 20) (counts : ∀ T,count H f T=TwentyFiveEightLowTenth.μ c T) : PropertyB H := by
  fin_cases c
  · exact TwentyFiveEightLowTenth.Case0.propertyB_of_counts H f counts
  · exact TwentyFiveEightLowTenth.Case1.propertyB_of_counts H f counts
  · exact TwentyFiveEightLowTenth.Case2.propertyB_of_counts H f counts
  · exact TwentyFiveEightLowTenth.Case3.propertyB_of_counts H f counts
  · exact TwentyFiveEightLowTenth.Case4.propertyB_of_counts H f counts
  · exact TwentyFiveEightLowTenth.Case5.propertyB_of_counts H f counts
  · exact TwentyFiveEightLowTenth.Case6.propertyB_of_counts H f counts
  · exact TwentyFiveEightLowTenth.Case7.propertyB_of_counts H f counts
  · exact TwentyFiveEightLowTenth.Case8.propertyB_of_counts H f counts
  · exact TwentyFiveEightLowTenth.Case9.propertyB_of_counts H f counts
  · exact TwentyFiveEightLowTenth.Case10.propertyB_of_counts H f counts
  · exact TwentyFiveEightLowTenth.Case11.propertyB_of_counts H f counts
  · exact TwentyFiveEightLowTenth.Case12.propertyB_of_counts H f counts
  · exact TwentyFiveEightLowTenth.Case13.propertyB_of_counts H f counts
  · exact TwentyFiveEightLowTenth.Case14.propertyB_of_counts H f counts
  · exact TwentyFiveEightLowTenth.Case15.propertyB_of_counts H f counts
  · exact TwentyFiveEightLowTenth.Case16.propertyB_of_counts H f counts
  · exact TwentyFiveEightLowTenth.Case17.propertyB_of_counts H f counts
  · exact TwentyFiveEightLowTenth.Case18.propertyB_of_counts H f counts
  · exact TwentyFiveEightLowTenth.Case19.propertyB_of_counts H f counts

theorem propertyB_of_group (H : Simple5Hypergraph (Fin 25)) (edges : H.edges.card=34)
    (f : Fin 10↪Fin 25) (unit : Unit H f) (g : Fin 2)
    (degrees : ∀ i,H.degree (f i)=standard 8 i)
    (old : large H (LockExtension.restrict f)=oldBig g) : PropertyB H := by
  obtain ⟨c,σ,counts⟩ := TwentyFiveUnitConditional.actual H edges f unit (standard 8) degrees
    (oldBig g) old (candidates g) (candidates_complete g)
    TwentyFiveEightLowTenthInventoryData.big (fun _ => standard 8) (witnesses g) (checked g)
  apply propertyB_of_counts H (σ.toEmbedding.trans f) c
  intro T
  rw [counts T]
  exact TwentyFiveEightLowTenthInventory.recovered c T
end Aris4Math.ThirtyFour.TwentyFiveEightLowTenthComplete
