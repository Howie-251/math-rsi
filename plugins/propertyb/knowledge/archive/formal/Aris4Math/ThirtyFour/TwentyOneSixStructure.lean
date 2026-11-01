import Aris4Math.ThirtyFour.TwentyOneSixLocalTriples
namespace Aris4Math.ThirtyFour.TwentyOneSixStructure
open Aris4Math.ThirtyThree.TripleProfiles
open TwentyOneSixLocalTriples TwentyOneSixIncidence
set_option maxHeartbeats 0

theorem codegree_le_four (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (noB : ¬PropertyB H) (x y : Fin 21) (xy : x≠y)
    (dx6 : 6≤H.degree x) (dx7 : H.degree x≤7) (dxy : H.degree x≤H.degree y) (dy8 : H.degree y≤8) :
    H.codegree x y≤4 := by
  by_contra hn
  exact noB (TwentyOneSixPairs.propertyB_of_high H size x y xy dx6 dx7 dxy dy8 (by omega))

theorem propertyB_of_666 (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering) (size : H.edges.card=34)
    (x y z : Fin 21) (xy : x≠y) (xz : x≠z) (yz : y≠z)
    (dx : H.degree x=6) (dy : H.degree y=6) (dz : H.degree z=6) :
    PropertyB H := by
  by_contra noB
  have a4 := codegree_le_four H size noB x y xy (by omega) (by omega) (by omega) (by omega)
  have b4 := codegree_le_four H size noB x z xz (by omega) (by omega) (by omega) (by omega)
  have c4 := codegree_le_four H size noB y z yz (by omega) (by omega) (by omega) (by omega)
  have a1 := H.one_le_codegree cover xy
  have b1 := H.one_le_codegree cover xz
  have c1 := H.one_le_codegree cover yz
  obtain ⟨ta,tb,tc⟩ := ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H x y z
  have ab := pair_excess H cover x y z xy xz yz dx
  obtain ⟨ixa,iya,iza⟩ := inventories H x y z xy xz yz
  rw [dx] at ixa
  rw [dy] at iya
  rw [dz] at iza
  have ac := pair_excess H cover y x z xy.symm yz xz dy
  rw [H.codegree_comm y x] at ac
  have bc := pair_excess H cover z x y xz.symm yz.symm xy dz
  rw [H.codegree_comm z x,H.codegree_comm z y] at bc
  have cov := coverage666 ⟨H.codegree x y,by omega⟩ ⟨H.codegree x z,by omega⟩
    ⟨H.codegree y z,by omega⟩ ⟨tripleCodegree H x y z,by omega⟩ a1 b1 c1 ta tb tc ab ac bc
  exact noB (apply666 H size x y z xy xz yz dx dy dz cov)

theorem propertyB_of_667 (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering) (size : H.edges.card=34)
    (x y z : Fin 21) (xy : x≠y) (xz : x≠z) (yz : y≠z)
    (dx : H.degree x=6) (dy : H.degree y=6) (dz : H.degree z=7) :
    PropertyB H := by
  by_contra noB
  have a4 := codegree_le_four H size noB x y xy (by omega) (by omega) (by omega) (by omega)
  have b4 := codegree_le_four H size noB x z xz (by omega) (by omega) (by omega) (by omega)
  have c4 := codegree_le_four H size noB y z yz (by omega) (by omega) (by omega) (by omega)
  have a1 := H.one_le_codegree cover xy
  have b1 := H.one_le_codegree cover xz
  have c1 := H.one_le_codegree cover yz
  obtain ⟨ta,tb,tc⟩ := ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H x y z
  have ab := pair_excess H cover x y z xy xz yz dx
  obtain ⟨ixa,iya,iza⟩ := inventories H x y z xy xz yz
  rw [dx] at ixa
  rw [dy] at iya
  rw [dz] at iza
  have ac := pair_excess H cover y x z xy.symm yz xz dy
  rw [H.codegree_comm y x] at ac
  have cov := coverage667 ⟨H.codegree x y,by omega⟩ ⟨H.codegree x z,by omega⟩
    ⟨H.codegree y z,by omega⟩ ⟨tripleCodegree H x y z,by omega⟩ a1 b1 c1 ta tb tc ab ac iza
  exact noB (apply667 H size x y z xy xz yz dx dy dz cov)

theorem residual_668 (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering) (size : H.edges.card=34)
    (noB : ¬PropertyB H)
    (x y z : Fin 21) (xy : x≠y) (xz : x≠z) (yz : y≠z)
    (dx : H.degree x=6) (dy : H.degree y=6) (dz : H.degree z=8) :
    (H.codegree x y=1 ∧ H.codegree x z=1 ∧ H.codegree y z=1 ∧ tripleCodegree H x y z=0) ∨
    (H.codegree x y=2 ∧ ((H.codegree x z=1 ∧ H.codegree y z=1 ∧ tripleCodegree H x y z=0) ∨
      (H.codegree x z=1 ∧ H.codegree y z=2 ∧ tripleCodegree H x y z=1) ∨
      (H.codegree x z=2 ∧ H.codegree y z=1 ∧ tripleCodegree H x y z=1))) := by
  have a4 := codegree_le_four H size noB x y xy (by omega) (by omega) (by omega) (by omega)
  have b4 := codegree_le_four H size noB x z xz (by omega) (by omega) (by omega) (by omega)
  have c4 := codegree_le_four H size noB y z yz (by omega) (by omega) (by omega) (by omega)
  have a1 := H.one_le_codegree cover xy
  have b1 := H.one_le_codegree cover xz
  have c1 := H.one_le_codegree cover yz
  obtain ⟨ta,tb,tc⟩ := ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H x y z
  have ab := pair_excess H cover x y z xy xz yz dx
  obtain ⟨ixa,iya,iza⟩ := inventories H x y z xy xz yz
  rw [dx] at ixa
  rw [dy] at iya
  rw [dz] at iza
  have ac := pair_excess H cover y x z xy.symm yz xz dy
  rw [H.codegree_comm y x] at ac
  have cov := coverage668 ⟨H.codegree x y,by omega⟩ ⟨H.codegree x z,by omega⟩
    ⟨H.codegree y z,by omega⟩ ⟨tripleCodegree H x y z,by omega⟩ a1 b1 c1 ta tb tc ab ac iza
  rcases cov with left | right | strict
  · exact Or.inl left
  · exact Or.inr right
  · exact False.elim (noB (apply668 H size x y z xy xz yz dx dy dz strict))

theorem residual_677 (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering) (size : H.edges.card=34)
    (noB : ¬PropertyB H)
    (x y z : Fin 21) (xy : x≠y) (xz : x≠z) (yz : y≠z)
    (dx : H.degree x=6) (dy : H.degree y=7) (dz : H.degree z=7) :
    (H.codegree x y=1 ∧ H.codegree x z=1 ∧ H.codegree y z=2 ∧ tripleCodegree H x y z=1) ∨
    (H.codegree x y=2 ∧ H.codegree x z=2 ∧ H.codegree y z=1 ∧ tripleCodegree H x y z=0) := by
  have a4 := codegree_le_four H size noB x y xy (by omega) (by omega) (by omega) (by omega)
  have b4 := codegree_le_four H size noB x z xz (by omega) (by omega) (by omega) (by omega)
  have c4 := codegree_le_four H size noB y z yz (by omega) (by omega) (by omega) (by omega)
  have a1 := H.one_le_codegree cover xy
  have b1 := H.one_le_codegree cover xz
  have c1 := H.one_le_codegree cover yz
  obtain ⟨ta,tb,tc⟩ := ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H x y z
  have ab := pair_excess H cover x y z xy xz yz dx
  obtain ⟨ixa,iya,iza⟩ := inventories H x y z xy xz yz
  rw [dx] at ixa
  rw [dy] at iya
  rw [dz] at iza
  have cov := coverage677 ⟨H.codegree x y,by omega⟩ ⟨H.codegree x z,by omega⟩
    ⟨H.codegree y z,by omega⟩ ⟨tripleCodegree H x y z,by omega⟩ a1 b1 c1 ta tb tc ab iya iza
  rcases cov with left | right | strict
  · exact Or.inl left
  · exact Or.inr right
  · exact False.elim (noB (apply677 H size x y z xy xz yz dx dy dz strict))

theorem residual_678 (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering) (size : H.edges.card=34)
    (noB : ¬PropertyB H)
    (x y z : Fin 21) (xy : x≠y) (xz : x≠z) (yz : y≠z)
    (dx : H.degree x=6) (dy : H.degree y=7) (dz : H.degree z=8) :
    H.codegree x y≤2 ∧ H.codegree x z≤2 ∧ H.codegree y z≤2 := by
  have a4 := codegree_le_four H size noB x y xy (by omega) (by omega) (by omega) (by omega)
  have b4 := codegree_le_four H size noB x z xz (by omega) (by omega) (by omega) (by omega)
  have c4 := codegree_le_four H size noB y z yz (by omega) (by omega) (by omega) (by omega)
  have a1 := H.one_le_codegree cover xy
  have b1 := H.one_le_codegree cover xz
  have c1 := H.one_le_codegree cover yz
  obtain ⟨ta,tb,tc⟩ := ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H x y z
  have ab := pair_excess H cover x y z xy xz yz dx
  obtain ⟨ixa,iya,iza⟩ := inventories H x y z xy xz yz
  rw [dx] at ixa
  rw [dy] at iya
  rw [dz] at iza
  have cov := coverage678 ⟨H.codegree x y,by omega⟩ ⟨H.codegree x z,by omega⟩
    ⟨H.codegree y z,by omega⟩ ⟨tripleCodegree H x y z,by omega⟩ a1 b1 c1 ta tb tc ab iya iza
  rcases cov with residual | strict
  · exact residual
  · exact False.elim (noB (apply678 H size x y z xy xz yz dx dy dz strict))

theorem unit_eight_pair (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering) (size : H.edges.card=34)
    (noB : ¬PropertyB H) (x y z : Fin 21) (xy : x≠y) (xz : x≠z) (yz : y≠z)
    (dx : H.degree x=6) (dy : H.degree y=8) (dz : H.degree z=8)
    (unitY : H.codegree x y=1) (unitZ : H.codegree x z=1) : H.codegree y z≤2 := by
  have upper := ThirtyThree.TwentyOnePairAssembly.codegree_le_degree H y z
  rw [dy] at upper
  obtain ⟨ta,tb,tc⟩ := ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H x y z
  rw [unitY] at ta
  have inv := TwentyOneFiveStructure.pair_inventory H x y z xy xz yz
  rw [unitY,dy] at inv
  by_contra hn
  have high : 3≤H.codegree y z := by omega
  apply noB
  apply apply688 H size x y z xy xz yz dx dy dz
  rw [unitY,unitZ]
  exact coverage688 ⟨H.codegree y z,by omega⟩ ⟨tripleCodegree H x y z,by omega⟩ high inv

theorem two_six_others_eight (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀v,6≤H.degree v) (noB : ¬PropertyB H)
    (x y : Fin 21) (xy : x≠y) (dx : H.degree x=6) (dy : H.degree y=6) :
    ∀z,z≠x→z≠y→8≤H.degree z := by
  intro z zx zy
  have low := minimum z
  by_contra hn
  have cases : H.degree z=6 ∨ H.degree z=7 := by omega
  rcases cases with dz | dz
  · exact noB (propertyB_of_666 H cover size x y z xy zx.symm zy.symm dx dy dz)
  · exact noB (propertyB_of_667 H cover size x y z xy zx.symm zy.symm dx dy dz)
open scoped BigOperators

theorem eights_two_six_budget (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀v,6≤H.degree v) (noB : ¬PropertyB H)
    (x y : Fin 21) (xy : x≠y) (dx : H.degree x=6) (dy : H.degree y=6) :
    13≤(TwentyOneFiveStructure.eights H).card := by
  have others := two_six_others_eight H cover size minimum noB x y xy dx dy
  have each (z : Fin 21) : 9≤H.degree z+(if z=x then 3 else 0)+
      (if z=y then 3 else 0)+(if H.degree z=8 then 1 else 0) := by
    by_cases zx : z=x
    · subst z; simp [dx,xy]
    by_cases zy : z=y
    · subst z; simp [dy,xy.symm]
    have lower := others z zx zy
    by_cases dz : H.degree z=8
    · simp [zx,zy,dz]
    · simp only [zx,zy,dz,if_false,add_zero]; omega
  have sum := Finset.sum_le_sum (s:=Finset.univ) (fun z _=>each z)
  have bound : 189≤170+3+3+(TwentyOneFiveStructure.eights H).card := by
    simpa [Finset.sum_add_distrib,H.sum_degrees,size,TwentyOneFiveStructure.eights] using sum
  omega

end Aris4Math.ThirtyFour.TwentyOneSixStructure
#print axioms Aris4Math.ThirtyFour.TwentyOneSixStructure.propertyB_of_666
#print axioms Aris4Math.ThirtyFour.TwentyOneSixStructure.two_six_others_eight
