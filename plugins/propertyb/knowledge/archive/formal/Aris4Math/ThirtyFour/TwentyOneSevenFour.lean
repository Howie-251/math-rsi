import Aris4Math.ThirtyFour.TwentyOneSevenFourCertificates
import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueKernel
namespace Aris4Math.ThirtyFour.TwentyOneSevenFour
open Aris4Math.ThirtyThree.MultiLockRecovery

theorem propertyB_of_four_sevens (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (size : H.edges.card=34)
    (minimum : ∀ x, 7≤H.degree x)
    (four : (TwentyOneSevenSelection.sevens H).card=4) : PropertyB H := by
  apply TwentyOneSevenFourActualCore.propertyB_of_four_sevens H cover size minimum four
  intro r values member valid g actual
  obtain ⟨c,p,matched⟩ := TwentyOneSevenFourCatalogue.coverage r values member valid
  apply TwentyOneSevenFourCertificates.propertyB_of_counts H
    ((TwentyOneSevenFourCatalogue.perm p).toEmbedding.trans g) c
  intro T
  rw [LockRelabel.count_comp_perm,actual]
  exact matched T
end Aris4Math.ThirtyFour.TwentyOneSevenFour
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenFour.propertyB_of_four_sevens
