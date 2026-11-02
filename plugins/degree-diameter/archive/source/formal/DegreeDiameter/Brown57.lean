import DegreeDiameter.Brown57Verified

namespace DegreeDiameter

/-- Transport from a computational neighbor enumeration to the canonical specification. -/
theorem brown57_degree : degreeAtMostEight brown57 := by
  classical
  intro v
  have h := brown57_computable_degree v
  unfold SimpleGraph.degree SimpleGraph.neighborFinset at h ⊢
  convert h using 1
  apply congrArg Finset.card
  ext w
  simp

/-- The explicit construction supplies the original lower-bound existential. -/
theorem exists82_57 : Exists82 57 := by
  exact ⟨Fin 57, inferInstance, brown57, Fintype.card_fin 57,
    brown57_degree, brown57_diameter⟩

end DegreeDiameter
