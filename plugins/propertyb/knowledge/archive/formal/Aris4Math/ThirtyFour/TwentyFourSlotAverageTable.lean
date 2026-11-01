import Aris4Math.ThirtyFour.TwentyFourActualSlotAverage
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
