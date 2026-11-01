import Aris4Math.ThirtyFour.TwentySevenTwoQuad
import Aris4Math.ThirtyFour.TwentySevenTwoTriples
import Aris4Math.ThirtyFour.TwentyEightPairs
import Aris4Math.ThirtyFour.TwentyStructure
import Aris4Math.ThirtyFour.Incidence

namespace Aris4Math.ThirtyFour.TwentySevenTwo
open scoped BigOperators
open Aris4Math.ThirtyThree.TripleProfiles (tripleCodegree)
open Aris4Math.ThirtyThree.QuadProfiles (first second)
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (fourVertices)
open Aris4Math.ThirtyFour.TwentyStructure

/-- The complete actual-input branch with exactly two seven-degree points. -/
theorem propertyB_of_two_sevens (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀ x, 7 ≤ H.degree x)
    (two : (TwentySevenMany.sevens H).card=2) : PropertyB H := by
  classical
  by_contra noB
  obtain ⟨x,y,xy,pair⟩ := Finset.card_eq_two.mp two
  have dx : H.degree x=7 := (TwentySevenMany.mem_sevens H x).mp (by simp [pair])
  have dy : H.degree y=7 := (TwentySevenMany.mem_sevens H y).mp (by simp [pair])
  let L := eights H
  have six : 6 ≤ L.card := by
    have budget := eights_budget H size minimum
    rw [two] at budget
    change 6 ≤ (eights H).card
    omega
  have degree (z : Fin 20) (hz : z ∈ L) : H.degree z=8 := (mem_eights H z).mp hz
  have xne (z : Fin 20) (hz : z ∈ L) : x ≠ z := by
    intro eq; have dd := degree z hz; rw [← eq,dx] at dd; omega
  have yne (z : Fin 20) (hz : z ∈ L) : y ≠ z := by
    intro eq; have dd := degree z hz; rw [← eq,dy] at dd; omega
  have lowxy := TwentySevenMany.seven_pair_bounds H cover size noB x y xy dx dy
  have crossBound (a : Fin 20) (da : H.degree a=7) (z : Fin 20) (hz : z ∈ L) : H.codegree a z ≤ 3 := by
    have az : a ≠ z := by intro eq; have dd := degree z hz; rw [← eq,da] at dd; omega
    have hn : ¬ 4 ≤ H.codegree a z := fun h => noB
      (TwentySevenMany.propertyB_of_high H cover size a z az da (Or.inr (degree z hz)) h)
    omega
  have triple (z : Fin 20) (hz : z ∈ L) :=
    TwentySevenTwoTriples.residual_of_not_propertyB H cover size noB x y z xy (xne z hz) (yne z hz)
      dx dy (degree z hz) (by omega) (crossBound x dx z hz) (crossBound y dy z hz)
  obtain ⟨z0,hz0⟩ := Finset.card_pos.mp (show 0 < L.card by omega)
  have cxy : H.codegree x y=2 := (triple z0 hz0).1
  have kind (z : Fin 20) (hz : z ∈ L) : H.codegree x z=1 ∨ H.codegree x z=2 := by
    rcases (triple z hz).2 with h | h
    · exact Or.inl h.1
    · exact Or.inr h.1
  have matched (z : Fin 20) (hz : z ∈ L) : H.codegree y z=H.codegree x z := by
    rcases (triple z hz).2 with h | h
    · omega
    · omega
  have quad (z w : Fin 20) (hz : z ∈ L) (hw : w ∈ L) (zw : z ≠ w) :
      H.codegree x z=1 ∧
      ∀ e ∈ H.edges, x ∈ e → z ∈ e → w ∈ e → False := by
    have czwLow := H.one_le_codegree cover zw
    have czw : H.codegree z w ≤ 3 := by
      have hn : ¬ 4 ≤ H.codegree z w := fun h => noB
        (TwentyEightPairs.propertyB_of_high H cover size z w zw (degree z hz) (degree w hw) h)
      omega
    let vertices := fourVertices x y z w xy (xne z hz) (xne w hw) (yne z hz) (yne w hw) zw
    have hd : ∀ j, H.degree (vertices j)=TwentySevenTwoQuadData.degree j := by
      intro j; fin_cases j <;> simp [vertices,fourVertices,TwentySevenTwoQuadData.degree,dx,dy,degree z hz,degree w hw]
    have hc : ∀ j, H.codegree (vertices (first j)) (vertices (second j))=
        TwentySevenTwoQuad.co (H.codegree x z) (H.codegree x w) (H.codegree z w) j := by
      intro j; fin_cases j <;> simp [vertices,fourVertices,first,second,TwentySevenTwoQuad.co,cxy,matched z hz,matched w hw]
    obtain ⟨one,_,_,zero⟩ := TwentySevenTwoQuad.residual_of_not_propertyB H size noB vertices
      (H.codegree x z) (H.codegree x w) (H.codegree z w) (kind z hz) (kind w hw) ⟨czwLow,czw⟩ hd hc
    refine ⟨one,?_⟩
    intro e he hx hz hw
    exact TwentySevenTwoQuad.no_common_023 H vertices zero e he hx hz hw
  have unit (z : Fin 20) (hz : z ∈ L) : H.codegree x z=1 := by
    have pos : 0 < (L.erase z).card := by rw [Finset.card_erase_of_mem hz]; omega
    obtain ⟨w,hw⟩ := Finset.card_pos.mp pos
    obtain ⟨wz,hw⟩ := Finset.mem_erase.mp hw
    exact (quad z w hz hw (Ne.symm wz)).1
  have atMost (e : Finset (Fin 20)) (he : e ∈ H.edges) (hx : x ∈ e) : (L ∩ e).card ≤ 1 := by
    apply Finset.card_le_one.mpr
    intro z hz w hw
    obtain ⟨hz,hze⟩ := Finset.mem_inter.mp hz
    obtain ⟨hw,hwe⟩ := Finset.mem_inter.mp hw
    by_contra zw
    exact (quad z w hz hw zw).2 e he hx hze hwe
  have separate (e : Finset (Fin 20)) (he : e ∈ H.edges) (hx : x ∈ e) (hy : y ∈ e)
      (z : Fin 20) (hz : z ∈ L) : z ∉ e := by
    have tau : tripleCodegree H x y z=0 := by
      have u := unit z hz
      rcases (triple z hz).2 with h | h
      · exact h.2.2
      · omega
    intro hze
    have pos : 1 ≤ tripleCodegree H x y z :=
      Finset.one_le_card.mpr ⟨e,Finset.mem_filter.mpr ⟨he,hx,hy,hze⟩⟩
    omega
  have sum : (∑ z ∈ L, H.codegree x z)=L.card := by
    calc
      _ = ∑ _z ∈ L, 1 := Finset.sum_congr rfl (fun z hz => unit z hz)
      _ = _ := by simp
  have cap := Incidence.neighbor_capacity H x y L atMost separate
  rw [sum,cxy,dx] at cap
  omega
end Aris4Math.ThirtyFour.TwentySevenTwo
#print axioms Aris4Math.ThirtyFour.TwentySevenTwo.propertyB_of_two_sevens
