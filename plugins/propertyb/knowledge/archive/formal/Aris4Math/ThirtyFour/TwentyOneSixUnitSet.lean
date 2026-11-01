import Aris4Math.ThirtyFour.Incidence
import Aris4Math.ThirtyFour.TwentyOneFive

/-! The structural conclusion of the degree-six / three unit-neighbor
classification. The classifier is a caller obligation; this module proves the
finite-set implication for the actual hypergraph and actual edge incidences. -/

namespace Aris4Math.ThirtyFour.TwentyOneSixUnitSet

open scoped BigOperators
open Aris4Math.ThirtyThree.TripleProfiles (tripleCodegree)

private theorem exists_third (U : Finset (Fin 21)) (large : 3 ≤ U.card)
    (a b : Fin 21) : ∃ c ∈ U, c ≠ a ∧ c ≠ b := by
  have small : ({a,b} : Finset (Fin 21)).card ≤ 2 := Finset.card_le_two
  obtain ⟨c,hc,out⟩ := Finset.exists_mem_notMem_of_card_lt_card
    (s := {a,b}) (t := U) (by omega)
  refine ⟨c,hc,?_⟩
  simpa only [Finset.mem_insert,Finset.mem_singleton,not_or] using out

/-- The two possible residual patterns on three members of the unit-neighbor
set. The second branch is the sum-four pattern; the separate pair bounds make
this precisely a permutation of (1,1,2). Ordered quantification below supplies
the zero common-triple conclusion for each of the three pairs. -/
def TripleResidue (H : Simple5Hypergraph (Fin 21)) (x a b c : Fin 21) : Prop :=
  (H.codegree a b=2 ∧ H.codegree a c=2 ∧ H.codegree b c=2) ∨
  (H.codegree a b+H.codegree a c+H.codegree b c=4 ∧
    tripleCodegree H x a b=0)

/-- One unit pair would give every member of U a unit neighbor. Every pair
would then extend to a residual triple with zero common incidence with x.
The six actual x-edges cannot cover at least seven such members. -/
theorem no_unit_pair (H : Simple5Hypergraph (Fin 21)) (x : Fin 21)
    (U : Finset (Fin 21)) (dx : H.degree x=6) (large : 7 ≤ U.card)
    (unit : ∀ u ∈ U, H.codegree x u=1)
    (pairs : ∀ a ∈ U, ∀ b ∈ U, a ≠ b →
      H.codegree a b=1 ∨ H.codegree a b=2)
    (residue : ∀ a ∈ U, ∀ b ∈ U, ∀ c ∈ U,
      a ≠ b → a ≠ c → b ≠ c → TripleResidue H x a b c)
    (a b : Fin 21) (ha : a ∈ U) (hb : b ∈ U) (ab : a ≠ b) :
    H.codegree a b ≠ 1 := by
  intro one
  have neighbor : ∀ p ∈ U, ∃ q ∈ U, p ≠ q ∧ H.codegree p q=1 := by
    intro p hp
    by_cases pa : p=a
    · subst p
      exact ⟨b,hb,ab,one⟩
    by_cases pb : p=b
    · subst p
      exact ⟨a,ha,ab.symm,by rw [H.codegree_comm]; exact one⟩
    rcases residue p hp a ha b hb pa pb ab with allTwo | sumFour
    · have impossible := allTwo.2.2
      omega
    · have boundA := pairs p hp a ha pa
      have boundB := pairs p hp b hb pb
      by_cases unitA : H.codegree p a=1
      · exact ⟨a,ha,pa,unitA⟩
      · refine ⟨b,hb,pb,?_⟩
        have total := sumFour.1
        omega
  have zero : ∀ p ∈ U, ∀ q ∈ U, p ≠ q → tripleCodegree H x p q=0 := by
    intro p hp q hq pq
    by_cases unitPQ : H.codegree p q=1
    · obtain ⟨r,hr,rp,rq⟩ := exists_third U (by omega) p q
      rcases residue p hp q hq r hr pq rp.symm rq.symm with allTwo | sumFour
      · have impossible := allTwo.1
        omega
      · exact sumFour.2
    · obtain ⟨r,hr,pr,unitPR⟩ := neighbor p hp
      have rq : r ≠ q := by
        intro eq
        subst r
        exact unitPQ unitPR
      rcases residue p hp q hq r hr pq pr rq.symm with allTwo | sumFour
      · have impossible := allTwo.2.1
        omega
      · exact sumFour.2
  have capacity : ∀ e ∈ H.edges, x ∈ e → (U ∩ e).card ≤ 1 := by
    intro e he hxe
    apply Finset.card_le_one.mpr
    intro p hp q hq
    obtain ⟨hp,hpe⟩ := Finset.mem_inter.mp hp
    obtain ⟨hq,hqe⟩ := Finset.mem_inter.mp hq
    by_contra pq
    have absent := zero p hp q hq pq
    have positive : 1 ≤ tripleCodegree H x p q :=
      Finset.one_le_card.mpr ⟨e,Finset.mem_filter.mpr ⟨he,hxe,hpe,hqe⟩⟩
    omega
  have upper := Incidence.codegree_capacity H x U 1 capacity
  have total : (∑ u ∈ U, H.codegree x u)=U.card := by
    calc
      _ = ∑ _u ∈ U, (1 : ℕ) := Finset.sum_congr rfl unit
      _ = U.card := by simp
  rw [total,dx] at upper
  omega

/-- Under the local residual classification, every distinct U-pair has
codegree two, and each actual edge through x contains at most two U-points.
No degree-eight or x-not-in-U premise is needed for this finite-set implication. -/
theorem unit_set_structure (H : Simple5Hypergraph (Fin 21)) (x : Fin 21)
    (U : Finset (Fin 21)) (dx : H.degree x=6) (large : 7 ≤ U.card)
    (unit : ∀ u ∈ U, H.codegree x u=1)
    (pairs : ∀ a ∈ U, ∀ b ∈ U, a ≠ b →
      H.codegree a b=1 ∨ H.codegree a b=2)
    (residue : ∀ a ∈ U, ∀ b ∈ U, ∀ c ∈ U,
      a ≠ b → a ≠ c → b ≠ c → TripleResidue H x a b c)
    (noFour : ∀ a ∈ U, ∀ b ∈ U, ∀ c ∈ U,
      a ≠ b → a ≠ c → b ≠ c →
      ∀ e ∈ H.edges, x ∈ e → a ∈ e → b ∈ e → c ∈ e → False) :
    (∀ a ∈ U, ∀ b ∈ U, a ≠ b → H.codegree a b=2) ∧
    (∀ e ∈ H.edges, x ∈ e → (U ∩ e).card ≤ 2) := by
  constructor
  · intro a ha b hb ab
    exact (pairs a ha b hb ab).resolve_left
      (no_unit_pair H x U dx large unit pairs residue a b ha hb ab)
  · intro e he hxe
    by_contra high
    have three : 2 < (U ∩ e).card := by omega
    obtain ⟨a,b,c,ha,hb,hc,ab,ac,bc⟩ := Finset.two_lt_card_iff.mp three
    obtain ⟨ha,hae⟩ := Finset.mem_inter.mp ha
    obtain ⟨hb,hbe⟩ := Finset.mem_inter.mp hb
    obtain ⟨hc,hce⟩ := Finset.mem_inter.mp hc
    exact noFour a ha b hb c hc ab ac bc e he hxe hae hbe hce

end Aris4Math.ThirtyFour.TwentyOneSixUnitSet
