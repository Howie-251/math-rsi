import Aris4Math.ThirtyThree.TwentyTwo
import Aris4Math.ThirtyThree.TwentyTwoHighPair
import Aris4Math.ThirtyThree.TwentyTwoTriple
import Aris4Math.ThirtyThree.TwentyTwoQuadAssembly

/-! Complete 22-point Property B proof: actual structural selection feeds every
pair, induced-path, and four-lock case into its proved probability caller. -/
namespace Aris4Math.ThirtyThree

theorem twenty_two_propertyB (H : Simple5Hypergraph (Fin 22))
    (cover : H.PairCovering) (edges33 : H.edges.card = 33) : PropertyB H := by
  obtain pair | triple | quad := TwentyTwoSelection.exists_locks_of_twenty_two H
    cover edges33 (by simp)
  · obtain ⟨x,y,xy,hcase⟩ := pair
    rcases hcase with ⟨dx,dy,cxy⟩ | ⟨dx,dy,high⟩
    · rcases dy with dy | dy
      · exact TwentyTwo.six_six_propertyB H cover edges33 x y xy cxy dx dy
      · exact TwentyTwo.six_seven_propertyB H cover edges33 x y xy cxy dx dy
    · exact TwentyTwoHighPair.propertyB_of_high_pair H edges33 x y xy dx dy high
  · obtain ⟨x,y,z,xy,xz,yz,dx,dy,dz,cxy,cxz,cyz⟩ := triple
    apply TwentyTwoTriple.propertyB_of_path H cover edges33
      (TripleProfiles.threeVertices x y z xy xz yz)
    · intro j
      fin_cases j
      · exact dx
      · exact dy
      · exact dz
    · exact cxy
    · exact cxz
    · exact cyz
  · obtain ⟨x,y,z,w,xy,xz,xw,yz,yw,zw,hcase⟩ := quad
    exact TwentyTwoQuadAssembly.propertyB_of_quadCase H cover edges33
      x y z w xy xz xw yz yw zw hcase

end Aris4Math.ThirtyThree

#print axioms Aris4Math.ThirtyThree.twenty_two_propertyB
