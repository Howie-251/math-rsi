import Aris4Math.ThirtyFour.TwentySevenOneClassification
import Aris4Math.ThirtyFour.TwentySevenTwoQuad
import Aris4Math.ThirtyFour.TwentyEightPairs
import Aris4Math.ThirtyFour.TwentyStructure
import Aris4Math.ThirtyFour.Incidence

namespace Aris4Math.ThirtyFour.TwentySevenOne
open scoped BigOperators
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.TripleProfiles (tripleCodegree)
open Aris4Math.ThirtyThree.QuadProfiles (first second highLabels count)
open Aris4Math.ThirtyThree.TwentyTwoQuadAssembly (fourVertices)
open Aris4Math.ThirtyFour.TwentyStructure

theorem propertyB_of_one_seven (H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀ x, 7 ≤ H.degree x)
    (one : (TwentySevenMany.sevens H).card=1) : PropertyB H := by
  classical
  by_contra noB
  obtain ⟨x,single⟩ := Finset.card_eq_one.mp one
  have dx : H.degree x=7 := (TwentySevenMany.mem_sevens H x).mp (by simp [single])
  let L := eights H
  have eight : 8 ≤ L.card := by
    have budget := eights_budget H size minimum
    rw [one] at budget
    change 8 ≤ (eights H).card
    omega
  have degree (z : Fin 20) (hz : z ∈ L) : H.degree z=8 := (mem_eights H z).mp hz
  have xne (z : Fin 20) (hz : z ∈ L) : x ≠ z := by
    intro eq; have dd := degree z hz; rw [← eq,dx] at dd; omega
  have crossBound (z : Fin 20) (hz : z ∈ L) : H.codegree x z ≤ 3 := by
    have hn : ¬ 4 ≤ H.codegree x z := fun h => noB
      (TwentySevenMany.propertyB_of_high H cover size x z (xne z hz) dx (Or.inr (degree z hz)) h)
    omega
  have pairBound (z w : Fin 20) (hz : z ∈ L) (hw : w ∈ L) (zw : z ≠ w) :
      H.codegree z w ≤ 3 := by
    have hn : ¬ 4 ≤ H.codegree z w := fun h => noB
      (TwentyEightPairs.propertyB_of_high H cover size z w zw (degree z hz) (degree w hw) h)
    omega
  have tripleBounds (z w : Fin 20) (hz : z ∈ L) (hw : w ∈ L) (zw : z ≠ w) :
      H.codegree x z ≤ 2 ∧ H.codegree x w ≤ 2 ∧ H.codegree z w ≤ 2 := by
    have a := crossBound z hz
    have b := crossBound w hw
    have c := pairBound z w hz hw zw
    have al := H.one_le_codegree cover (xne z hz)
    have bl := H.one_le_codegree cover (xne w hw)
    have cl := H.one_le_codegree cover zw
    obtain ⟨ta,tb,tc⟩ := ThirtyThree.TwentyOnePairAssembly.tripleCodegree_le_pairs H x z w
    by_contra hn
    have high : H.codegree x z=3 ∨ H.codegree x w=3 ∨ H.codegree z w=3 := by omega
    have suitable := TwentyRemainingTriples.seven_high_strict
      ⟨H.codegree x z,by omega⟩ ⟨H.codegree x w,by omega⟩ ⟨H.codegree z w,by omega⟩
      ⟨tripleCodegree H x z w,by omega⟩ al bl cl ta tb tc high
    exact noB (TwentyRemainingTriples.propertyB_of_suitable H cover size x z w
      (xne z hz) (xne w hw) zw true dx (degree z hz) (degree w hw) suitable)
  have crossKind (z : Fin 20) (hz : z ∈ L) : H.codegree x z=1 ∨ H.codegree x z=2 := by
    obtain ⟨w,hw,wz,_⟩ := exists_third L (by omega) z z
    have upper := (tripleBounds z w hz hw (Ne.symm wz)).1
    have lower := H.one_le_codegree cover (xne z hz)
    omega
  have fourFacts (a b c : Fin 20) (ha : a ∈ L) (hb : b ∈ L) (hc : c ∈ L)
      (ab : a ≠ b) (ac : a ≠ c) (bc : b ≠ c) :
      (∀ e ∈ H.edges, x ∈ e → a ∈ e → b ∈ e → c ∈ e → False) ∧
      H.codegree x a+H.codegree x b+H.codegree x c ≠ 4 ∧
      (H.codegree x a=1 → H.codegree x b=1 → H.codegree x c=1 →
        ∀ e ∈ H.edges, x ∈ e → b ∈ e → c ∈ e → False) := by
    let f := fourVertices x a b c (xne a ha) (xne b hb) (xne c hc) ab ac bc
    have hd : ∀ j, H.degree (f j)=TwentySevenOneQuadData.degree j := by
      intro j; fin_cases j <;> simp [f,fourVertices,TwentySevenOneQuadData.degree,dx,degree a ha,degree b hb,degree c hc]
    have hco : ∀ j, 1 ≤ H.codegree (f (first j)) (f (second j)) ∧
        H.codegree (f (first j)) (f (second j)) ≤ 2 := by
      intro j
      constructor
      · apply H.one_le_codegree cover
        exact f.injective.ne (by fin_cases j <;> decide)
      · have aa := tripleBounds a b ha hb ab
        have bb := tripleBounds a c ha hc ac
        have cc := tripleBounds b c hb hc bc
        fin_cases j <;> simp [f,fourVertices,first,second] <;> omega
    have residue := TwentySevenOneClassification.residual_of_not_propertyB H cover size noB f hd hco
    refine ⟨?_,residue.2.1,?_⟩
    · intro e he hx hae hbe hce
      have sig : lockSignature f e=highLabels 4 := by
        ext j; fin_cases j <;> simp [lockSignature,highLabels,f,fourVertices,hx,hae,hbe,hce]
      have pos : 1 ≤ count H f (highLabels 4) := Finset.one_le_card.mpr
        ⟨e,Finset.mem_filter.mpr ⟨he,sig⟩⟩
      have zero : count H f (highLabels 4)=0 := residue.1
      omega
    · intro ua ub uc e he hx hbe hce
      have zeros := residue.2.2 ua ub uc
      exact TwentySevenTwoQuad.no_common_023 H f zeros e he hx hbe hce
  have capacityTwo (e : Finset (Fin 20)) (he : e ∈ H.edges) (hx : x ∈ e) : (L ∩ e).card ≤ 2 := by
    by_contra hn
    obtain ⟨f,hf⟩ := TwentySevenMany.exists_indexed_subset (L ∩ e) (show 3 ≤ (L ∩ e).card by omega)
    have member (i : Fin 3) := Finset.mem_inter.mp (hf i)
    exact (fourFacts (f 0) (f 1) (f 2) (member 0).1 (member 1).1 (member 2).1
      (f.injective.ne (by decide)) (f.injective.ne (by decide)) (f.injective.ne (by decide))).1
      e he hx (member 0).2 (member 1).2 (member 2).2
  by_cases allUnit : ∀ z ∈ L, H.codegree x z=1
  · have capacityOne (e : Finset (Fin 20)) (he : e ∈ H.edges) (hx : x ∈ e) : (L ∩ e).card ≤ 1 := by
      apply Finset.card_le_one.mpr
      intro a ha b hb
      obtain ⟨ha,hae⟩ := Finset.mem_inter.mp ha
      obtain ⟨hb,hbe⟩ := Finset.mem_inter.mp hb
      by_contra ab
      obtain ⟨c,hc,ca,cb⟩ := exists_third L (by omega) a b
      exact (fourFacts c a b hc ha hb ca cb ab).2.2
        (allUnit c hc) (allUnit a ha) (allUnit b hb) e he hx hae hbe
    have sum : (∑ z ∈ L, H.codegree x z)=L.card := by
      calc
        _ = ∑ _z ∈ L, 1 := Finset.sum_congr rfl allUnit
        _ = _ := by simp
    have cap := Incidence.codegree_capacity H x L 1 capacityOne
    rw [sum,dx] at cap
    omega
  · push_neg at allUnit
    obtain ⟨b,hb,nonunit⟩ := allUnit
    have b2 : H.codegree x b=2 := by have := crossKind b hb; omega
    let A := L.filter (fun a => H.codegree x a=1)
    have smallA : A.card ≤ 1 := by
      apply Finset.card_le_one.mpr
      intro a ha c hc
      obtain ⟨ha,ua⟩ := Finset.mem_filter.mp ha
      obtain ⟨hc,uc⟩ := Finset.mem_filter.mp hc
      by_contra ac
      have ab : a ≠ b := by intro h; subst a; exact nonunit ua
      have cb : c ≠ b := by intro h; subst c; exact nonunit uc
      have impossible := (fourFacts a c b ha hc hb ac ab cb).2.1
      omega
    have each (z : Fin 20) (hz : z ∈ L) :
        H.codegree x z+(if H.codegree x z=1 then 1 else 0)=2 := by
      rcases crossKind z hz with h | h <;> simp [h]
    have sum : (∑ z ∈ L, H.codegree x z)+A.card=2*L.card := by
      have hs := Finset.sum_congr rfl (fun z hz => each z hz)
      simpa [Finset.sum_add_distrib,Finset.sum_boole,A,Nat.mul_comm] using hs
    have cap := Incidence.codegree_capacity H x L 2 capacityTwo
    rw [dx] at cap
    omega
end Aris4Math.ThirtyFour.TwentySevenOne
#print axioms Aris4Math.ThirtyFour.TwentySevenOne.propertyB_of_one_seven
