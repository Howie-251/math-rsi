import Aris4Math.ThirtyFour.TwentyOneSixTwo
import Aris4Math.ThirtyFour.TwentyOneSixNoSeven
import Aris4Math.ThirtyFour.TwentyOneSixOneSeven
import Aris4Math.ThirtyFour.TwentyOneSixTwoSevens
import Aris4Math.ThirtyFour.TwentyOneSixManySevens
namespace Aris4Math.ThirtyFour.TwentyOneSix

/-- Every actual pair-covering 34-edge hypergraph on 21 vertices with minimum
six and an attained degree six has Property B. All local inputs are constructed
inside the proof. -/
theorem propertyB_of_degree_six (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀v,6≤H.degree v)
    (x : Fin 21) (dx : H.degree x=6) : PropertyB H := by
  classical
  by_cases second : ∃y,y≠x ∧ H.degree y=6
  · obtain ⟨y,yx,dy⟩:=second
    exact TwentyOneSixTwo.propertyB_of_two_sixes H cover size minimum x y yx.symm dx dy
  have others7 (u : Fin 21) (ux : u≠x) : 7≤H.degree u := by
    have low:=minimum u
    have ne : H.degree u≠6 := fun du=>second ⟨u,ux,du⟩
    omega
  by_cases firstSeven : ∃y,H.degree y=7
  · obtain ⟨y,dy⟩:=firstSeven
    have xy : x≠y := by intro eq;rw [eq,dy] at dx;omega
    by_cases secondSeven : ∃z,z≠y ∧ H.degree z=7
    · obtain ⟨z,zy,dz⟩:=secondSeven
      have xz : x≠z := by intro eq;rw [eq,dz] at dx;omega
      by_cases thirdSeven : ∃w,w≠y ∧ w≠z ∧ H.degree w=7
      · obtain ⟨w,wy,wz,dw⟩:=thirdSeven
        have xw : x≠w := by intro eq;rw [eq,dw] at dx;omega
        exact TwentyOneSixManySevens.propertyB_of_six_three_sevens H cover size
          x y z w xy xz xw zy.symm wy.symm wz.symm dx dy dz dw
      · apply TwentyOneSixTwoSevens.propertyB_of_two_sevens H cover size x y z xy xz zy.symm dx dy dz
        intro u ux uy uz
        have low:=others7 u ux
        have ne : H.degree u≠7 := fun du=>thirdSeven ⟨u,uy,uz,du⟩
        omega
    · apply TwentyOneSixOneSeven.propertyB_of_one_seven H cover size x y xy dx dy
      intro u ux uy
      have low:=others7 u ux
      have ne : H.degree u≠7 := fun du=>secondSeven ⟨u,uy,du⟩
      omega
  · apply TwentyOneSixNoSeven.propertyB_of_six_no_seven H cover size x dx
    intro u ux
    have low:=others7 u ux
    have ne : H.degree u≠7 := fun du=>firstSeven ⟨u,du⟩
    omega
end Aris4Math.ThirtyFour.TwentyOneSix
#print axioms Aris4Math.ThirtyFour.TwentyOneSix.propertyB_of_degree_six
