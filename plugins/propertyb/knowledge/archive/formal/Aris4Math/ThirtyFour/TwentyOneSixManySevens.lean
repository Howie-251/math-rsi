import Aris4Math.ThirtyFour.TwentyOneSixStructure
import Aris4Math.ThirtyFour.TwentyOneSixQuadCoverage
import Aris4Math.ThirtyFour.TwentyOneFive

/-! Actual degree-(6,7,7,7) vertices cannot occur in a non-Property-B
21-vertex, pair-covering hypergraph with 34 edges. The triple residuals,
common-edge implications, and quadruple classification are connected here. -/

namespace Aris4Math.ThirtyFour.TwentyOneSixManySevens

open Aris4Math.ThirtyThree.TripleProfiles (tripleCodegree)
open Aris4Math.ThirtyThree.QuadProfiles (count first second highLabels)
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (fourVertices high_inventory)
open Aris4Math.ThirtyFour.TwentyOneSixStructure (residual_677)
open Aris4Math.ThirtyFour.TwentyOneSixQuadCoverage
  (co6777 Assumptions6777 actual6777)
open Aris4Math.ThirtyFour.TwentyOneFiveLocal (triple_common common_quad)

theorem propertyB_of_six_three_sevens (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (size : H.edges.card=34)
    (x y z w : Fin 21) (xy : x ≠ y) (xz : x ≠ z) (xw : x ≠ w)
    (yz : y ≠ z) (yw : y ≠ w) (zw : z ≠ w)
    (dx : H.degree x=6) (dy : H.degree y=7)
    (dz : H.degree z=7) (dw : H.degree w=7) : PropertyB H := by
  by_contra noB
  have rxy := residual_677 H cover size noB x y z xy xz yz dx dy dz
  have rxw := residual_677 H cover size noB x y w xy xw yw dx dy dw
  have rzw := residual_677 H cover size noB x z w xz xw zw dx dz dw
  let f := fourVertices x y z w xy xz xw yz yw zw
  have hd : ∀ j, H.degree (f j)=TwentyOneSixQuad6777Data.degree j := by
    intro j
    fin_cases j <;> simp [f,fourVertices,TwentyOneSixQuad6777Data.degree,dx,dy,dz,dw]
  rcases rxy with one | two
  · obtain ⟨xy1,xz1,yz2,xyz1⟩ := one
    have xw1 : H.codegree x w=1 := by omega
    have yw2 : H.codegree y w=2 := by omega
    have zw2 : H.codegree z w=2 := by omega
    have xyw1 : tripleCodegree H x y w=1 := by omega
    obtain ⟨e,he,xe,ye,ze⟩ := triple_common H x y z (by omega)
    obtain ⟨e',he',xe',ye',we'⟩ := triple_common H x y w (by omega)
    have eq := H.edge_unique_of_codegree_one xy1 he' he xe' ye' xe ye
    have we : w ∈ e := eq ▸ we'
    have positive : 1 ≤ count H f (highLabels 4) := common_quad H f e he (by
      intro j; fin_cases j <;> simp [f,fourVertices,xe,ye,ze,we])
    have bound := high_inventory H f 0
    change count H f (highLabels 0)+count H f (highLabels 1)+count H f (highLabels 4)
      ≤ H.codegree x y at bound
    have quad : count H f (highLabels 4)=1 := by omega
    have hc : ∀ j, H.codegree (f (first j)) (f (second j))=co6777 1 1 1 j := by
      intro j
      fin_cases j <;> simp [f,fourVertices,first,second,co6777,xy1,xz1,xw1,yz2,yw2,zw2]
    have ass : Assumptions6777 1 (fun j => count H f (highLabels j)) := by
      constructor
      · intro _; exact quad
      · intro impossible; norm_num at impossible
    exact actual6777 H size noB f 0 0 0 hd hc ass
  · obtain ⟨xy2,xz2,yz1,xyz0⟩ := two
    have xw2 : H.codegree x w=2 := by omega
    have yw1 : H.codegree y w=1 := by omega
    have zw1 : H.codegree z w=1 := by omega
    have xyw0 : tripleCodegree H x y w=0 := by omega
    have xzw0 : tripleCodegree H x z w=0 := by omega
    have t0 := QuadIncidence.triple_count H f 0
    have t1 := QuadIncidence.triple_count H f 1
    have t2 := QuadIncidence.triple_count H f 2
    change tripleCodegree H x y z=count H f (highLabels 0)+count H f (highLabels 4) at t0
    change tripleCodegree H x y w=count H f (highLabels 1)+count H f (highLabels 4) at t1
    change tripleCodegree H x z w=count H f (highLabels 2)+count H f (highLabels 4) at t2
    have hc : ∀ j, H.codegree (f (first j)) (f (second j))=co6777 2 1 1 j := by
      intro j
      fin_cases j <;> simp [f,fourVertices,first,second,co6777,xy2,xz2,xw2,yz1,yw1,zw1]
    have ass : Assumptions6777 2 (fun j => count H f (highLabels j)) := by
      constructor
      · intro impossible; norm_num at impossible
      · intro _
        exact ⟨t0.symm.trans xyz0,t1.symm.trans xyw0,t2.symm.trans xzw0⟩
    exact actual6777 H size noB f 1 0 0 hd hc ass

/-- Select the actual three seven-degree vertices from the existing degree set. -/
theorem propertyB_of_many_sevens (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (size : H.edges.card=34)
    (x : Fin 21) (dx : H.degree x=6)
    (many : 3 ≤ (TwentyOneFiveStructure.sevens H).card) : PropertyB H := by
  obtain ⟨g,hg⟩ := TwentyOneFive.indexed_subset (TwentyOneFiveStructure.sevens H) many
  have dg (i : Fin 3) : H.degree (g i)=7 :=
    (TwentyOneFiveStructure.mem_sevens H _).mp (hg i)
  have xn (i : Fin 3) : x ≠ g i := by
    intro eq
    rw [eq,dg] at dx
    omega
  exact propertyB_of_six_three_sevens H cover size x (g 0) (g 1) (g 2)
    (xn 0) (xn 1) (xn 2) (g.injective.ne (by decide))
    (g.injective.ne (by decide)) (g.injective.ne (by decide)) dx (dg 0) (dg 1) (dg 2)

end Aris4Math.ThirtyFour.TwentyOneSixManySevens

#print axioms Aris4Math.ThirtyFour.TwentyOneSixManySevens.propertyB_of_six_three_sevens
#print axioms Aris4Math.ThirtyFour.TwentyOneSixManySevens.propertyB_of_many_sevens
