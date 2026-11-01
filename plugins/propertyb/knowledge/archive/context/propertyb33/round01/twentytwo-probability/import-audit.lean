import Aris4Math.ThirtyThree.TwentyTwoComplete
import Aris4Math.Main

#check Aris4Math.ThirtyThree.twenty_two_propertyB
#print axioms Aris4Math.ThirtyThree.twenty_two_propertyB
#print axioms Aris4Math.ThirtyThree.QuadProfiles.actual_recovered
#print axioms Aris4Math.ThirtyThree.PureLink.pure_bad_pair_lower
#print axioms Aris4Math.ThirtyThree.TwentyTwoPureDeletion.realized_dual_deduction
#print axioms Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.data_complete
#print axioms Aris4Math.ThirtyThree.TwentyTwoQuad.propertyB_of_data
#print axioms Aris4Math.ThirtyThree.TwentyTwoTriple.propertyB_of_path
#print axioms Aris4Math.propertyB_of_at_most_thirty_two

/-- The entire 22-point reduced branch, with no type/profile, selected lock,
probability comparison, enumeration certificate or multiplicity premise. -/
theorem twenty_two_original_branch
    (E : Finset (Finset (Fin 22))) (hfive : ∀ e ∈ E,e.card=5)
    (hcard : E.card=33)
    (hcover : ∀ x y : Fin 22,x ≠ y → ∃ e ∈ E,x ∈ e ∧ y ∈ e) :
    ∃ c : Fin 22 → Bool,∀ e ∈ E,
      1 ≤ (e.filter (fun x => c x=true)).card ∧
      (e.filter (fun x => c x=true)).card ≤ 4 :=
  Aris4Math.ThirtyThree.twenty_two_propertyB ⟨E,hfive⟩ hcover hcard

#print axioms twenty_two_original_branch
example : Aris4Math.Target := Aris4Math.propertyB_of_at_most_thirty_two
