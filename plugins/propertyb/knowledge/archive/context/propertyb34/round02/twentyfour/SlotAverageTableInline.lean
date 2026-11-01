import Aris4Math.ThirtyFour.MixedLayoutApplication
import Aris4Math.ThirtyThree.ActualBadSlot
import Aris4Math.ThirtyThree.TwentyFourUniqueBadPair

/-! A real bad edge pair is selected before a layout is chosen. Exact
centerwise bounds on its convexly averaged contribution imply a coloring. -/
namespace Aris4Math.ThirtyFour.TwentyFourActualSlotAverage
open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.LinkDeletion Aris4Math.LinkWeightCertificates
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.ActualBadSlot
open MixedLayoutApplication
variable {n edgeCount : ℕ} {L : Type*} [Fintype L]

def slotWeight (positions : L→Fin n↪Fin 24) (p : L→Numeric.Profile)
    (l : L) (j : Fin n) (T U : Finset (Fin n)) : ℚ :=
  weights positions p l j T U+weights positions p l j U T

/-- The finite slot bounds refer to one fixed actual pair at each center,
independently of the later positions. No independence between centers is assumed. -/
theorem propertyB_of_slot_averages (H : Simple5Hypergraph (Fin 24))
    (cover : H.PairCovering) (vertices : Fin n↪Fin 24) (μ : Finset (Fin n)→ℕ)
    (counts : ∀T,count H vertices T=μ T)
    (degrees : ∀j,H.degree (vertices j)=6)
    (unit : ∀i j,i≠j→H.codegree (vertices i) (vertices j)=1)
    (positions : L→Fin n↪Fin 24) (p : L→Numeric.Profile)
    (real : ∀l,RealizesProfile H vertices (positions l) (p l) edgeCount)
    (nocap : ∀l,(p l).emptyPairCap=none)
    (centers : ∀l j,(positions l j).val+1∈(p l).correctionCenters)
    (gamma : L→ℚ) (gn : ∀l,0≤gamma l) (mass : ∑l,gamma l=1)
    (centerBound : Fin n→ℚ)
    (bounds : ∀j T U,Admissible μ j T U→
      (∑l,gamma l*min (a positions p l j)
        (c positions p l j-slotWeight positions p l j T U))≤centerBound j)
    (strict : (∑l,gamma l*free (positions l) (p l))+(∑j,centerBound j)<1) :
    PropertyB H := by
  classical
  have existsSlot (j : Fin n) : ∃T U E F,
      ({E,F} : Finset (Finset (Fin 24)))∈H.badLinkPairs (vertices j) ∧
      lockSignature vertices E=T ∧ lockSignature vertices F=U ∧ Admissible μ j T U := by
    have lower := H.link_bad_pair_lower_bound cover (vertices j)
    rw [Fintype.card_fin,degrees j] at lower
    have nonempty : (H.badLinkPairs (vertices j)).Nonempty := Finset.card_pos.mp (by omega)
    obtain ⟨T,U,E,F,bad,hE,hF,adm⟩ := exists_actual_slot H vertices j
      (fun i ij=>unit j i ij.symm) nonempty
    refine ⟨T,U,E,F,bad,hE,hF,?_⟩
    simpa only [Admissible,counts] using adm
  choose T U E F bad hE hF admissible using existsSlot
  let D (l : L) (j : Fin n) := ∑z∈directedBadPairs H (vertices j),
    typeWeight (p l) (positionType vertices (positions l)) ((positions l j).val+1) z
  have weightLower (l : L) (j : Fin n) : slotWeight positions p l j (T j) (U j)≤D l j := by
    exact slot_weight_lower H vertices (positions l) (p l) j (E j) (F j) (T j) (U j)
      (bad j) (hE j) (hF j)
  have center (j : Fin n) :
      (∑l,gamma l*min (a positions p l j) (c positions p l j-D l j))≤centerBound j := by
    calc
      _ ≤ ∑l,gamma l*min (a positions p l j)
          (c positions p l j-slotWeight positions p l j (T j) (U j)) := by
        apply Finset.sum_le_sum
        intro l _
        exact mul_le_mul_of_nonneg_left (min_le_min le_rfl (sub_le_sub_left (weightLower l j) _)) (gn l)
      _ ≤ _ := bounds j (T j) (U j) (admissible j)
  have total : (∑l,gamma l*(free (positions l) (p l)+
      ∑j,min (a positions p l j) (c positions p l j-D l j)))<1 := by
    have sum := Finset.sum_le_sum (s:=Finset.univ) (fun j _=>center j)
    rw [Finset.sum_comm] at sum
    simp_rw [mul_add,Finset.mul_sum,Finset.sum_add_distrib]
    exact lt_of_le_of_lt (add_le_add_left sum _) strict
  obtain ⟨l,success⟩ := MixedLayoutDual.exists_strict_of_average gamma
    (fun l=>free (positions l) (p l)+∑j,min (a positions p l j) (c positions p l j-D l j))
    gn mass total
  exact propertyB_of_layout_bound H vertices (positions l) (p l) (real l) (nocap l) (centers l) success
end Aris4Math.ThirtyFour.TwentyFourActualSlotAverage
#print axioms Aris4Math.ThirtyFour.TwentyFourActualSlotAverage.propertyB_of_slot_averages
namespace Aris4Math.ThirtyFour.TwentyFourSlotAverageTable
open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.ActualBadSlot
open MixedLayoutApplication TwentyFourActualSlotAverage
variable {n edgeCount : ℕ} {L S : Type*} [Fintype L] [Fintype S]

structure Slot (n : ℕ) where
  center : Fin n
  left : Finset (Fin n)
  right : Finset (Fin n)

def contribution (positions : L→Fin n↪Fin 24) (p : L→Numeric.Profile)
    (l : L) (s : Slot n) : ℚ :=
  min (a positions p l s.center)
    (c positions p l s.center-slotWeight positions p l s.center s.left s.right)

/-- The table enumerates actual admissible slots up to exchanging the edges.
Each entry keeps the same actual pair while averaging the layouts. -/
theorem propertyB_of_table (H : Simple5Hypergraph (Fin 24))
    (cover : H.PairCovering) (vertices : Fin n↪Fin 24) (μ : Finset (Fin n)→ℕ)
    (counts : ∀T,count H vertices T=μ T)
    (degrees : ∀j,H.degree (vertices j)=6)
    (unit : ∀i j,i≠j→H.codegree (vertices i) (vertices j)=1)
    (positions : L→Fin n↪Fin 24) (p : L→Numeric.Profile)
    (real : ∀l,RealizesProfile H vertices (positions l) (p l) edgeCount)
    (nocap : ∀l,(p l).emptyPairCap=none)
    (centers : ∀l j,(positions l j).val+1∈(p l).correctionCenters)
    (gamma : L→ℚ) (gn : ∀l,0≤gamma l) (mass : ∑l,gamma l=1)
    (slot : S→Slot n)
    (complete : ∀j T U,Admissible μ j T U→∃s,
      (slot s).center=j ∧
      (((slot s).left=T ∧ (slot s).right=U) ∨
       ((slot s).left=U ∧ (slot s).right=T)))
    (value : L→S→ℚ)
    (entry : ∀l s,contribution positions p l (slot s)=value l s)
    (centerBound : Fin n→ℚ)
    (bounds : ∀s,(∑l,gamma l*value l s)≤centerBound (slot s).center)
    (strict : (∑l,gamma l*free (positions l) (p l))+(∑j,centerBound j)<1) :
    PropertyB H := by
  apply propertyB_of_slot_averages H cover vertices μ counts degrees unit
    positions p real nocap centers gamma gn mass centerBound _ strict
  intro j T U adm
  obtain ⟨s,hj,hpair⟩ := complete j T U adm
  have eq (l : L) : min (a positions p l j)
      (c positions p l j-slotWeight positions p l j T U)=value l s := by
    rw [←entry l s]
    rcases hpair with ⟨hT,hU⟩ | ⟨hU,hT⟩
    · simp only [contribution,hj,hT,hU]
    · simp only [contribution,hj,hT,hU,slotWeight,add_comm]
  simpa only [eq,hj] using bounds s
end Aris4Math.ThirtyFour.TwentyFourSlotAverageTable