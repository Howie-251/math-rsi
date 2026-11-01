import Aris4Math.ThirtyFour.TwentyOneSixUnitActual
import Aris4Math.ThirtyFour.TwentyOneSixQuadCoverage
import Aris4Math.ThirtyFour.QuadIncidence

set_option simprocs false
namespace Aris4Math.ThirtyFour.TwentyOneSixTwoUnit
open scoped BigOperators
open Aris4Math.ThirtyThree.TripleProfiles (tripleCodegree)
open Aris4Math.ThirtyThree.QuadProfiles (count first second highLabels)
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (fourVertices)
open TwentyOneSixStructure TwentyOneSixQuadCoverage

theorem propertyB_of_two_sixes_unit (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀v,6≤H.degree v)
    (x y : Fin 21) (xy : x≠y) (dx : H.degree x=6) (dy : H.degree y=6)
    (unit : H.codegree x y=1) : PropertyB H := by
  classical
  by_contra noB
  let L:=TwentyOneFiveStructure.eights H
  have many : 13≤L.card := eights_two_six_budget H cover size minimum noB x y xy dx dy
  have degree (z) (hz : z∈L) : H.degree z=8 := (TwentyOneFiveStructure.mem_eights H z).mp hz
  have apart (z) (hz : z∈L) : x≠z ∧ y≠z := by
    have dz:=degree z hz
    constructor <;> intro eq
    · rw [←eq,dx] at dz; omega
    · rw [←eq,dy] at dz; omega
  have triple (z) (hz : z∈L) : H.codegree x z=1 ∧ H.codegree y z=1 ∧ tripleCodegree H x y z=0 := by
    rcases residual_668 H cover size noB x y z xy (apart z hz).1 (apart z hz).2 dx dy (degree z hz) with a | b
    · exact a.2
    · omega
  have structured:= TwentyOneSixUnitActual.unit_set_structure_of_not_propertyB H cover size noB x dx L
    (by omega) degree (fun z hz=>(triple z hz).1)
  have capacity:=structured.2
  have sum : (∑z∈L,H.codegree x z)=L.card := by
    calc
      _=∑_z∈L,1 := Finset.sum_congr rfl (fun z hz=>(triple z hz).1)
      _=_ := by simp
  have cap:=Incidence.codegree_capacity H x L 2 capacity
  rw [sum,dx] at cap
  omega
end Aris4Math.ThirtyFour.TwentyOneSixTwoUnit
#print axioms Aris4Math.ThirtyFour.TwentyOneSixTwoUnit.propertyB_of_two_sixes_unit
