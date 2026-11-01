import Aris4Math.ThirtyFour.TwentyOneSixFiveSelection
import Aris4Math.ThirtyFour.TwentyOneSixTwoUnit
namespace Aris4Math.ThirtyFour.TwentyOneSixTwo
open scoped BigOperators
open Aris4Math.ThirtyThree.TripleProfiles (tripleCodegree)
open TwentyOneSixStructure

/-- Complete actual branch with two degree-six vertices. -/
theorem propertyB_of_two_sixes (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀v,6≤H.degree v)
    (x y : Fin 21) (xy : x≠y) (dx : H.degree x=6) (dy : H.degree y=6) : PropertyB H := by
  classical
  by_contra noB
  let L:=TwentyOneFiveStructure.eights H
  have many : 13≤L.card := eights_two_six_budget H cover size minimum noB x y xy dx dy
  have degree (z) (hz : z∈L) : H.degree z=8 := (TwentyOneFiveStructure.mem_eights H z).mp hz
  have apart (z) (hz : z∈L) : x≠z ∧ y≠z := by
    have dz:=degree z hz
    constructor <;> intro eq
    · rw [←eq,dx] at dz;omega
    · rw [←eq,dy] at dz;omega
  have cxy : H.codegree x y=2 := by
    obtain ⟨z,hz⟩:=Finset.card_pos.mp (by omega : 0<L.card)
    have res:=residual_668 H cover size noB x y z xy (apart z hz).1 (apart z hz).2 dx dy (degree z hz)
    have notOne : H.codegree x y≠1 := fun one=>noB
      (TwentyOneSixTwoUnit.propertyB_of_two_sixes_unit H cover size minimum x y xy dx dy one)
    omega
  let A:=H.badPartners x\{y}
  let B:=H.badPartners y\{x}
  have boundA : A.card≤3 := by
    have bd:=TwentyOneSixIncidence.outside_bad_budget H cover x dx {y} (by simpa using xy)
    simpa [A,cxy] using bd
  have boundB : B.card≤3 := by
    have bd:=TwentyOneSixIncidence.outside_bad_budget H cover y dy {x} (by simpa using xy.symm)
    simp only [Finset.sum_singleton,H.codegree_comm y x,cxy] at bd
    simpa [B] using bd
  let S:=L\(A∪B)
  have large : 7≤S.card := by
    have split:=Finset.card_sdiff_add_card_inter L (A∪B)
    have inter:=Finset.card_le_card (Finset.inter_subset_right : L∩(A∪B)⊆A∪B)
    have union:=Finset.card_union_le A B
    change 7≤(L\(A∪B)).card
    omega
  have sub : S⊆L := Finset.sdiff_subset
  have degrees (u) (hu : u∈S) : H.degree u=8 := degree u (sub hu)
  have units (u) (hu : u∈S) : H.codegree x u=1 ∧ H.codegree y u=1 := by
    have ne:=apart u (sub hu)
    obtain ⟨_,out⟩:=Finset.mem_sdiff.mp hu
    have lowerX:=H.one_le_codegree cover ne.1
    have lowerY:=H.one_le_codegree cover ne.2
    constructor
    · by_contra hn
      apply out
      apply Finset.mem_union_left
      apply Finset.mem_sdiff.mpr
      refine ⟨Finset.mem_filter.mpr ⟨by simp [ne.1.symm],by omega⟩,?_⟩
      simpa using ne.2.symm
    · by_contra hn
      apply out
      apply Finset.mem_union_right
      apply Finset.mem_sdiff.mpr
      refine ⟨Finset.mem_filter.mpr ⟨by simp [ne.2.symm],by omega⟩,?_⟩
      simpa using ne.1.symm
  have clean (u) (hu : u∈S) : tripleCodegree H x y u=0 := by
    have res:=residual_668 H cover size noB x y u xy (apart u (sub hu)).1
      (apart u (sub hu)).2 dx dy (degrees u hu)
    have unit:=units u hu
    omega
  have structured:=TwentyOneSixUnitActual.unit_set_structure_of_not_propertyB H cover size noB
    x dx S large degrees (fun u hu=>(units u hu).1)
  exact noB (TwentyOneSixFiveSelection.propertyB_of_unit_set H size x y 0 xy dx dy cxy S
    large degrees units structured.1 clean)
end Aris4Math.ThirtyFour.TwentyOneSixTwo
#print axioms Aris4Math.ThirtyFour.TwentyOneSixTwo.propertyB_of_two_sixes
