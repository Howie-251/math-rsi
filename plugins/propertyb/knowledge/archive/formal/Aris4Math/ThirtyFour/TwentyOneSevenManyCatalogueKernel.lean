import Aris4Math.ThirtyFour.TwentyOneSevenManyCatalogueCertificates
namespace Aris4Math.ThirtyFour.TwentyOneSevenManyCatalogue
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyFour.LockExtension
open Aris4Math.ThirtyFour.PromotionCatalog
open Aris4Math.ThirtyFour.PromotionReconstruction
open TwentyOneSevenQuadCoverage (Residue residueμ)
set_option maxHeartbeats 0
set_option maxRecDepth 100000
set_option synthInstance.maxSize 1000
theorem coverage (r : Residue) (values : List ℕ) (member : values∈catalogue r) (valid : Valid r values) : Matched r values := by
  have all : (catalogue r).all (fun values=>decide (Valid r values→Matched r values))=true := by
    fin_cases r
    · change (catalogue 0).all (fun values=>decide (Valid 0 values→Matched 0 values))=true
      rw [catalogue_eq0]
      simp only [List.all_append,certificate_chunk0_0,certificate_chunk0_1,certificate_chunk0_2,certificate_chunk0_3,certificate_chunk0_4,certificate_chunk0_5,certificate_chunk0_6,certificate_chunk0_7,Bool.and_self]
    · change (catalogue 1).all (fun values=>decide (Valid 1 values→Matched 1 values))=true
      rw [catalogue_eq1]
      simp only [List.all_append,certificate_chunk1_0,certificate_chunk1_1,certificate_chunk1_2,certificate_chunk1_3,Bool.and_self]
    · change (catalogue 2).all (fun values=>decide (Valid 2 values→Matched 2 values))=true
      rw [catalogue_eq2]
      simp only [List.all_append,certificate_chunk2_0,certificate_chunk2_1,Bool.and_self]
    · change (catalogue 3).all (fun values=>decide (Valid 3 values→Matched 3 values))=true
      rw [catalogue_eq3]
      simp only [List.all_append,certificate_chunk3_0,certificate_chunk3_1,certificate_chunk3_2,certificate_chunk3_3,certificate_chunk3_4,certificate_chunk3_5,certificate_chunk3_6,certificate_chunk3_7,certificate_chunk3_8,Bool.and_self]
    · change (catalogue 4).all (fun values=>decide (Valid 4 values→Matched 4 values))=true
      rw [catalogue_eq4]
      simp only [List.all_append,certificate_chunk4_0,certificate_chunk4_1,certificate_chunk4_2,certificate_chunk4_3,certificate_chunk4_4,certificate_chunk4_5,certificate_chunk4_6,certificate_chunk4_7,certificate_chunk4_8,Bool.and_self]
    · change (catalogue 5).all (fun values=>decide (Valid 5 values→Matched 5 values))=true
      rw [catalogue_eq5]
      simp only [List.all_append,certificate_chunk5_0,certificate_chunk5_1,certificate_chunk5_2,certificate_chunk5_3,certificate_chunk5_4,certificate_chunk5_5,Bool.and_self]
    · change (catalogue 6).all (fun values=>decide (Valid 6 values→Matched 6 values))=true
      rw [catalogue_eq6]
      simp only [List.all_append,certificate_chunk6_0,certificate_chunk6_1,certificate_chunk6_2,Bool.and_self]
    · change (catalogue 7).all (fun values=>decide (Valid 7 values→Matched 7 values))=true
      rw [catalogue_eq7]
      simp only [List.all_append,certificate_chunk7_0,certificate_chunk7_1,certificate_chunk7_2,certificate_chunk7_3,certificate_chunk7_4,certificate_chunk7_5,Bool.and_self]
    · change (catalogue 8).all (fun values=>decide (Valid 8 values→Matched 8 values))=true
      rw [catalogue_eq8]
      simp only [List.all_append,certificate_chunk8_0,certificate_chunk8_1,certificate_chunk8_2,certificate_chunk8_3,certificate_chunk8_4,certificate_chunk8_5,certificate_chunk8_6,certificate_chunk8_7,certificate_chunk8_8,Bool.and_self]
  exact (of_decide_eq_true (List.all_eq_true.mp all values member)) valid
end Aris4Math.ThirtyFour.TwentyOneSevenManyCatalogue
