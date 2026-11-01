import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthNumeric0
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthNumeric1
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthNumeric2
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthCoverage
namespace Aris4Math.ThirtyFour.TwentyFiveNineLowTenthComplete
open Aris4Math.ThirtyThree.MultiLockRecovery
open TwentyFiveUnitExtension TwentyFiveUnitCounts TwentyFiveNineLowTenthCoverage

theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 10 ↪ Fin 25)
    (c : Fin 25) (counts : ∀ T,count H f T=TwentyFiveNineLowTenth.μ c T) : PropertyB H := by
  fin_cases c
  · exact TwentyFiveNineLowTenth.Case0.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case1.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case2.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case3.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case4.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case5.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case6.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case7.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case8.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case9.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case10.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case11.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case12.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case13.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case14.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case15.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case16.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case17.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case18.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case19.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case20.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case21.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case22.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case23.propertyB_of_counts H f counts
  · exact TwentyFiveNineLowTenth.Case24.propertyB_of_counts H f counts

theorem propertyB_of_group (H : Simple5Hypergraph (Fin 25)) (edges : H.edges.card=34)
    (f : Fin 10 ↪ Fin 25) (unit : Unit H f) (g : Fin 6)
    (deg : ∀ i,H.degree (f i)=degrees g i)
    (old : large H (LockExtension.restrict f)=oldBig g) : PropertyB H := by
  obtain ⟨c,σ,counts⟩ := TwentyFiveUnitConditional.actual H edges f unit (degrees g) deg
    (oldBig g) old (candidates g) (candidates_complete g)
    TwentyFiveNineLowTenthInventory.big TwentyFiveNineLowTenthInventory.degrees
    (witnesses g) (checked g)
  apply propertyB_of_counts H (σ.toEmbedding.trans f) c
  intro T
  rw [counts T]
  exact TwentyFiveNineLowTenthInventory.recovered c T
end Aris4Math.ThirtyFour.TwentyFiveNineLowTenthComplete
#print axioms Aris4Math.ThirtyFour.TwentyFiveNineLowTenthComplete.propertyB_of_group
