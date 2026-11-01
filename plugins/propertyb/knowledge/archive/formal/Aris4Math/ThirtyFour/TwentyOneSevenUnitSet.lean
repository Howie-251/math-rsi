import Aris4Math.ThirtyFour.TwentyOneSevenUnitQuad

/-! Actual unit neighbors of a degree-seven vertex. The four-lock classifier
is applied to arbitrary real triples, so no local residue premise is exposed. -/

namespace Aris4Math.ThirtyFour.TwentyOneSevenUnitSet

open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.QuadProfiles (count highLabels)
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (fourVertices)

theorem unit_set_structure_of_not_propertyB (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (size : H.edges.card=34) (noB : ¬PropertyB H)
    (x : Fin 21) (dx : H.degree x=7) (U : Finset (Fin 21)) (large : 3≤U.card)
    (degrees : ∀u∈U,H.degree u=8) (unit : ∀u∈U,H.codegree x u=1) :
    (∀a∈U,∀b∈U,a≠b→H.codegree a b=2) ∧
    (∀e∈H.edges,x∈e→(U∩e).card≤2) := by
  have apart (u : Fin 21) (hu : u∈U) : x≠u := by
    intro eq
    have du := degrees u hu
    rw [eq] at dx
    omega
  have triple (a : Fin 21) (ha : a∈U) (b : Fin 21) (hb : b∈U)
      (c : Fin 21) (hc : c∈U) (ab : a≠b) (ac : a≠c) (bc : b≠c) :
      H.codegree a b=2 ∧
      ∀e∈H.edges,x∈e→a∈e→b∈e→c∈e→False := by
    let f := fourVertices x a b c (apart a ha) (apart b hb) (apart c hc) ab ac bc
    have da := degrees a ha
    have db := degrees b hb
    have dc := degrees c hc
    have xa := unit a ha
    have xb := unit b hb
    have xc := unit c hc
    have hd : ∀j,H.degree (f j)=![7,8,8,8] j := by
      intro j;fin_cases j <;> assumption
    have hu : ∀j : Fin 4,j≠0→H.codegree (f 0) (f j)=1 := by
      intro j ne
      fin_cases j <;> simp +decide [f,fourVertices,xa,xb,xc] at ne ⊢
    have res := TwentyOneSevenUnitQuad.residual H cover size noB f hd hu
    refine ⟨res.1,?_⟩
    have zero : count H f (highLabels 4)=0 := res.2.2.2
    intro e he xe ae be ce
    have sig : lockSignature f e=highLabels 4 := by
      ext j
      fin_cases j <;> simp [f,fourVertices,highLabels,xe,ae,be,ce]
    have positive : 1≤count H f (highLabels 4) :=
      Finset.one_le_card.mpr ⟨e,Finset.mem_filter.mpr ⟨he,sig⟩⟩
    omega
  constructor
  · intro a ha b hb ab
    have small : ({a,b} : Finset (Fin 21)).card<U.card :=
      lt_of_le_of_lt Finset.card_le_two (by omega)
    obtain ⟨c,hc,apart⟩ := Finset.exists_mem_notMem_of_card_lt_card small
    simp only [Finset.mem_insert,Finset.mem_singleton,not_or] at apart
    exact (triple a ha b hb c hc ab (Ne.symm apart.1) (Ne.symm apart.2)).1
  · intro e he xe
    by_contra high
    obtain ⟨a,b,c,ha,hb,hc,ab,ac,bc⟩ := Finset.two_lt_card_iff.mp
      (show 2<(U∩e).card by omega)
    obtain ⟨ha,ae⟩ := Finset.mem_inter.mp ha
    obtain ⟨hb,be⟩ := Finset.mem_inter.mp hb
    obtain ⟨hc,ce⟩ := Finset.mem_inter.mp hc
    exact (triple a ha b hb c hc ab ac bc).2 e he xe ae be ce

end Aris4Math.ThirtyFour.TwentyOneSevenUnitSet

#print axioms Aris4Math.ThirtyFour.TwentyOneSevenUnitSet.unit_set_structure_of_not_propertyB
