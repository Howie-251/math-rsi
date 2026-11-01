import Aris4Math.ThirtyFour.TwentyOneSevenUniqueCatalogueData
namespace Aris4Math.ThirtyFour.TwentyOneSevenUniqueLocal
open Aris4Math.ThirtyThree.MultiLockRecovery
open TwentyOneSevenUniqueCatalogue

theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 21)) (f : Fin 6↪Fin 21)
    (c : Case) (counts : ∀T,count H f T=targetμ c T) : PropertyB H := by
  by_cases a:c.val<16
  · apply TwentyOneSevenSix788888Batch000.propertyB_of_counts H f ⟨c.val,a⟩
    simpa only [targetμ,dif_pos a] using counts
  · by_cases b:c.val<32
    · apply TwentyOneSevenSix788888Batch001.propertyB_of_counts H f ⟨c.val-16,by omega⟩
      simpa only [targetμ,dif_neg a,dif_pos b] using counts
    · by_cases d:c.val<39
      · apply TwentyOneSevenSix788888Batch002.propertyB_of_counts H f ⟨c.val-32,by omega⟩
        simpa only [targetμ,dif_neg a,dif_neg b,dif_pos d] using counts
      · apply TwentyOneSevenJointUniqueSix0.propertyB_of_counts H f
        simpa only [targetμ,dif_neg a,dif_neg b,dif_neg d] using counts

theorem propertyB_of_five_counts (H : Simple5Hypergraph (Fin 21)) (f : Fin 5↪Fin 21)
    (c : Fin 2) (counts : ∀T,count H f T=targetFive c T) : PropertyB H := by
  by_cases h:c=0
  · apply TwentyOneSevenJointUnitFive0.propertyB_of_counts H f
    simpa only [targetFive,if_pos h] using counts
  · apply TwentyOneSevenJointUnitFive2.propertyB_of_counts H f
    simpa only [targetFive,if_neg h] using counts
end Aris4Math.ThirtyFour.TwentyOneSevenUniqueLocal
