import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueChecked0
import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueChecked1
import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueChecked2
import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueChecked3
import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueChecked4
import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueChecked5
import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueChecked6
import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueChecked7
import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueChecked8
namespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
open TwentyOneSevenQuadCoverage (Residue)
open TwentyOneSevenFourActualCore (catalogue Valid)
open TwentyOneSevenFourCertificates (Choice)
theorem coverage (r : Residue) (values : List ℕ) (member : values∈catalogue r)
    (valid : Valid r values) : ∃ c : Choice, ∃ p : Perm, Matched r values c p := by
  fin_cases r
  · change values ∈ catalogue (0 : Residue) at member
    rw [← rows_eq0] at member
    obtain ⟨row,mem,eq⟩ := List.mem_map.mp member
    refine ⟨row.2.1,row.2.2,?_⟩
    have h := of_decide_eq_true (List.all_eq_true.mp rows_checked0 row mem)
    simpa only [eq] using h (by simpa only [eq] using valid)
  · change values ∈ catalogue (1 : Residue) at member
    rw [← rows_eq1] at member
    obtain ⟨row,mem,eq⟩ := List.mem_map.mp member
    refine ⟨row.2.1,row.2.2,?_⟩
    have h := of_decide_eq_true (List.all_eq_true.mp rows_checked1 row mem)
    simpa only [eq] using h (by simpa only [eq] using valid)
  · change values ∈ catalogue (2 : Residue) at member
    rw [← rows_eq2] at member
    obtain ⟨row,mem,eq⟩ := List.mem_map.mp member
    refine ⟨row.2.1,row.2.2,?_⟩
    have h := of_decide_eq_true (List.all_eq_true.mp rows_checked2 row mem)
    simpa only [eq] using h (by simpa only [eq] using valid)
  · change values ∈ catalogue (3 : Residue) at member
    rw [← rows_eq3] at member
    obtain ⟨row,mem,eq⟩ := List.mem_map.mp member
    refine ⟨row.2.1,row.2.2,?_⟩
    have h := of_decide_eq_true (List.all_eq_true.mp rows_checked3 row mem)
    simpa only [eq] using h (by simpa only [eq] using valid)
  · change values ∈ catalogue (4 : Residue) at member
    rw [← rows_eq4] at member
    obtain ⟨row,mem,eq⟩ := List.mem_map.mp member
    refine ⟨row.2.1,row.2.2,?_⟩
    have h := of_decide_eq_true (List.all_eq_true.mp rows_checked4 row mem)
    simpa only [eq] using h (by simpa only [eq] using valid)
  · change values ∈ catalogue (5 : Residue) at member
    rw [← rows_eq5] at member
    obtain ⟨row,mem,eq⟩ := List.mem_map.mp member
    refine ⟨row.2.1,row.2.2,?_⟩
    have h := of_decide_eq_true (List.all_eq_true.mp rows_checked5 row mem)
    simpa only [eq] using h (by simpa only [eq] using valid)
  · change values ∈ catalogue (6 : Residue) at member
    rw [← rows_eq6] at member
    obtain ⟨row,mem,eq⟩ := List.mem_map.mp member
    refine ⟨row.2.1,row.2.2,?_⟩
    have h := of_decide_eq_true (List.all_eq_true.mp rows_checked6 row mem)
    simpa only [eq] using h (by simpa only [eq] using valid)
  · change values ∈ catalogue (7 : Residue) at member
    rw [← rows_eq7] at member
    obtain ⟨row,mem,eq⟩ := List.mem_map.mp member
    refine ⟨row.2.1,row.2.2,?_⟩
    have h := of_decide_eq_true (List.all_eq_true.mp rows_checked7 row mem)
    simpa only [eq] using h (by simpa only [eq] using valid)
  · change values ∈ catalogue (8 : Residue) at member
    rw [← rows_eq8] at member
    obtain ⟨row,mem,eq⟩ := List.mem_map.mp member
    refine ⟨row.2.1,row.2.2,?_⟩
    have h := of_decide_eq_true (List.all_eq_true.mp rows_checked8 row mem)
    simpa only [eq] using h (by simpa only [eq] using valid)
end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue
