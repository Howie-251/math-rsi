import Aris4Math.ThirtyFour.NineteenSingle
import Aris4Math.ThirtyFour.NineteenPairs
import Aris4Math.ThirtyFour.NineteenTriples
import Aris4Math.ThirtyFour.NineteenSelection
import Aris4Math.ThirtyThree.Nineteen

/-! The complete actual nineteen-vertex branch at the new bound of 34 edges. -/
namespace Aris4Math.ThirtyFour

private theorem nineteen_pair_propertyB (H : Simple5Hypergraph (Fin 19))
    (edges34 : H.edges.card = 34) (x y : Fin 19) (ne : x ≠ y)
    (hcase : NineteenSelection.PairCase H x y) : PropertyB H := by
  obtain ⟨dx,unit | high⟩ := hcase
  · obtain ⟨lower,upper,codeg⟩ := unit
    have mem : (⟨8,H.degree y,1,7,8⟩ : NineteenPairs.PairCase) ∈ NineteenPairs.highCases := by
      interval_cases h : H.degree y <;> decide
    exact NineteenPairs.propertyB_of_high_pair H edges34 x y ne _ mem dx rfl codeg
  · obtain ⟨dy,lower⟩ := high
    have upper := ThirtyThree.TwentyOnePairAssembly.codegree_le_degree H x y
    rw [dx] at upper
    have mem : (⟨8,8,H.codegree x y,1,11⟩ : NineteenPairs.PairCase) ∈ NineteenPairs.highCases := by
      interval_cases h : H.codegree x y <;> decide
    exact NineteenPairs.propertyB_of_high_pair H edges34 x y ne _ mem dx dy rfl

/-- Every pair-covering actual hypergraph on nineteen vertices with exactly
34 edges has a Boolean two-coloring. No numeric certificate is a premise. -/
theorem nineteen_propertyB_of_eq (H : Simple5Hypergraph (Fin 19))
    (cover : H.PairCovering) (edges34 : H.edges.card = 34) : PropertyB H := by
  obtain single | pair | triple := NineteenSelection.exists_selected H cover edges34
  · obtain ⟨x,lower,upper⟩ := single
    exact NineteenSingle.propertyB_of_degree_five_to_seven H cover edges34 x lower upper
  · obtain ⟨x,y,ne,hcase⟩ := pair
    exact nineteen_pair_propertyB H edges34 x y ne hcase
  · obtain ⟨x,y,z,xy,xz,yz,dx,dy,dz,ca,cb,cc⟩ := triple
    exact NineteenTriples.propertyB_of_three_eights H cover edges34 x y z xy xz yz dx dy dz ca cb cc

/-- The corresponding at-most-34 branch; the old at-most-33 theorem is reused
only below the new boundary. Pair covering is the reduction's internal input. -/
theorem nineteen_propertyB (H : Simple5Hypergraph (Fin 19))
    (cover : H.PairCovering) (edges34 : H.edges.card ≤ 34) : PropertyB H := by
  by_cases heq : H.edges.card = 34
  · exact nineteen_propertyB_of_eq H cover heq
  · exact ThirtyThree.Nineteen.nineteen_propertyB H (by omega)

end Aris4Math.ThirtyFour
#print axioms Aris4Math.ThirtyFour.nineteen_propertyB_of_eq
#print axioms Aris4Math.ThirtyFour.nineteen_propertyB
