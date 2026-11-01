import Aris4Math.ThirtyFour.TwentyOneSevenUniqueCatalogueCertificates
namespace Aris4Math.ThirtyFour.TwentyOneSevenUniqueCatalogue
theorem coverage (values : List ℕ) (mem : values∈catalogue) (valid : Valid values) : Matched values := by
  have covered : ∀xs∈catalogue,Valid xs→Matched xs := by
    rw [catalogue_eq]
    exact List.forall_mem_append.mpr ⟨List.forall_mem_append.mpr ⟨List.forall_mem_append.mpr ⟨List.forall_mem_append.mpr ⟨List.forall_mem_append.mpr ⟨List.forall_mem_append.mpr ⟨List.forall_mem_append.mpr ⟨List.forall_mem_append.mpr ⟨List.forall_mem_append.mpr ⟨certificate0, certificate1⟩, certificate2⟩, certificate3⟩, certificate4⟩, certificate5⟩, certificate6⟩, certificate7⟩, certificate8⟩, certificate9⟩
  exact covered values mem valid
end Aris4Math.ThirtyFour.TwentyOneSevenUniqueCatalogue
