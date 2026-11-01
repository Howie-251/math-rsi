import Aris4Math.SmallLockProfiles
import Aris4Math.ProfileApplication
import Aris4Math.LinkWeightCertificates

/-! The 21-vertex branch of the finite goal. -/

open scoped BigOperators

namespace Aris4Math.TwentyOne

open SmallLockProfiles TypeCounting LinkDeletion LinkWeightCertificates

/-- A degree-five lock already gives the required strict uncorrected bound. -/
theorem degree_five_propertyB (H : Simple5Hypergraph (Fin 21))
    (edges32 : H.edges.card = 32) (x : Fin 21) (degree : H.degree x = 5) : PropertyB H := by
  have real : RealizesProfile H (oneVertex x) onePosition Numeric.v21_d5 := by
    simpa only [degree, profile21_five] using realizes_profile21 H edges32 x
      (by omega) (by omega)
  exact ProfileApplication.propertyB_of_uncorrected_profile H (oneVertex x) onePosition
    Numeric.v21_d5 real rfl rfl Numeric.v21_d5_lt_one

/-- A degree-six lock also needs no link correction. -/
theorem degree_six_propertyB (H : Simple5Hypergraph (Fin 21))
    (edges32 : H.edges.card = 32) (x : Fin 21) (degree : H.degree x = 6) : PropertyB H := by
  have real : RealizesProfile H (oneVertex x) onePosition Numeric.v21_d6 := by
    simpa only [degree, profile21_six] using realizes_profile21 H edges32 x
      (by omega) (by omega)
  exact ProfileApplication.propertyB_of_uncorrected_profile H (oneVertex x) onePosition
    Numeric.v21_d6 real rfl rfl Numeric.v21_d6_lt_one

/-- The degree-seven profile's numerical deduction is supplied by distinct
actual bad link pairs at the actual locked vertex. -/
theorem degree_seven_deduction (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (edges32 : H.edges.card = 32)
    (x : Fin 21) (degree : H.degree x = 7) :
    ∀ j : Fin 1, (onePosition j).val + 1 ∈ Numeric.v21_d7.correctionCenters →
      Numeric.deduction Numeric.v21_d7 ((onePosition j).val + 1) ≤
        ∑ d ∈ directedBadPairs H (oneVertex x j),
          typeWeight Numeric.v21_d7 (positionType (oneVertex x) onePosition)
            ((onePosition j).val + 1) d := by
  have real : RealizesProfile H (oneVertex x) onePosition Numeric.v21_d7 := by
    simpa only [degree, profile21_seven] using realizes_profile21 H edges32 x
      (by omega) (by omega)
  intro j _
  exact v21_d7_deduction_11 H cover (oneVertex x) onePosition real j rfl degree

/-- The structural degree bound leaves only the corrected degree-seven case
after the other two alternatives have been proved colorable. -/
theorem propertyB_or_degree_seven (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (edges32 : H.edges.card = 32) :
    PropertyB H ∨ ∃ x : Fin 21, H.degree x = 7 := by
  obtain ⟨x, lower, upper, _⟩ := exists_realized_profile21 H cover edges32
  by_cases five : H.degree x = 5
  · exact Or.inl (degree_five_propertyB H edges32 x five)
  by_cases six : H.degree x = 6
  · exact Or.inl (degree_six_propertyB H edges32 x six)
  · exact Or.inr ⟨x, by omega⟩

/-- The actual bad-link deletion closes the degree-seven branch. -/
theorem degree_seven_propertyB (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (edges32 : H.edges.card = 32)
    (x : Fin 21) (degree : H.degree x = 7) : PropertyB H := by
  have real : RealizesProfile H (oneVertex x) onePosition Numeric.v21_d7 := by
    simpa only [degree, profile21_seven] using realizes_profile21 H edges32 x
      (by omega) (by omega)
  exact ProfileApplication.propertyB_of_corrected_profile H (oneVertex x) onePosition
    Numeric.v21_d7 real rfl (degree_seven_deduction H cover edges32 x degree)
    Numeric.v21_d7_lt_one

/-- Complete 21-vertex finite-goal branch. The conclusion is the original
PropertyB predicate, with no profile, counting or probability premise. -/
theorem twenty_one_propertyB (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (edges32 : H.edges.card = 32) : PropertyB H := by
  rcases propertyB_or_degree_seven H cover edges32 with colored | ⟨x, degree⟩
  · exact colored
  · exact degree_seven_propertyB H cover edges32 x degree

end Aris4Math.TwentyOne

#print axioms Aris4Math.TwentyOne.degree_five_propertyB
#print axioms Aris4Math.TwentyOne.degree_six_propertyB
#print axioms Aris4Math.TwentyOne.degree_seven_deduction
#print axioms Aris4Math.TwentyOne.propertyB_or_degree_seven
#print axioms Aris4Math.TwentyOne.degree_seven_propertyB
#print axioms Aris4Math.TwentyOne.twenty_one_propertyB
