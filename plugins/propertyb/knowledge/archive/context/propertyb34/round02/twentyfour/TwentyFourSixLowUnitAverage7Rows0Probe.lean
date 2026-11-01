import Aris4Math.ThirtyFour.MixedLayoutApplication
import Aris4Math.ThirtyThree.ActualBadSlot
import Aris4Math.ThirtyThree.TwentyFourUniqueBadPair
import Aris4Math.ThirtyFour.CachedRows
import Aris4Math.ThirtyFour.TwentyFourNoLowCoverageKernel

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
namespace Aris4Math.ThirtyFour.TwentyFourSlotAverageCache
open scoped BigOperators
open MixedLayoutApplication TwentyFourSlotAverageTable
variable {n m : ℕ} {L : Type*} [Fintype L]

def cachedFree (positions : Fin n↪Fin 24) (p : Numeric.Profile) : ℚ :=
  ∑k∈Finset.univ.filter (fun k=>¬∃j,positions j=k),
    min (CachedRows.cachedA p (k.val+1) true)
      (min (CachedRows.cachedA p (k.val+1) false) (CachedRows.cachedC p (k.val+1)))
def cachedA (positions : Fin n↪Fin 24) (p : Numeric.Profile) (j : Fin n) : ℚ :=
  min (CachedRows.cachedA p ((positions j).val+1) true)
    (CachedRows.cachedA p ((positions j).val+1) false)
def cachedC (positions : Fin n↪Fin 24) (p : Numeric.Profile) (j : Fin n) : ℚ :=
  CachedRows.cachedC p ((positions j).val+1)

theorem free_eq (positions : Fin n↪Fin 24) (p : Numeric.Profile)
    (valid : Numeric.validProfile p m) (nocap : p.emptyPairCap=none) :
    free positions p=cachedFree positions p := by
  unfold free cachedFree
  apply Finset.sum_congr rfl
  intro k _
  obtain ⟨ha,hb,hc⟩ := CachedRows.rows_eq p m (k.val+1) valid nocap
  rw [ha,hb,hc]

theorem contribution_eq (positions : L→Fin n↪Fin 24) (p : L→Numeric.Profile)
    (l : L) (s : Slot n)
    (valid : Numeric.validProfile (p l) m) (nocap : (p l).emptyPairCap=none) :
    contribution positions p l s =
      min (cachedA (positions l) (p l) s.center)
        (cachedC (positions l) (p l) s.center-
          (LocalProfiles.executableWeights positions p l s.center s.left s.right+
           LocalProfiles.executableWeights positions p l s.center s.right s.left)) := by
  unfold contribution a c cachedA cachedC TwentyFourActualSlotAverage.slotWeight
  obtain ⟨ha,hb,hc⟩ := CachedRows.rows_eq (p l) m ((positions l s.center).val+1) valid nocap
  rw [ha,hb,hc,LocalProfiles.weights_eq]
end Aris4Math.ThirtyFour.TwentyFourSlotAverageCache
namespace Aris4Math.ThirtyFour.TwentyFourSixLowUnitData
open Aris4Math.ThirtyThree.MultiLockRecovery
set_option maxRecDepth 100000
set_option maxHeartbeats 0
abbrev Case := Fin 9
def μ : Case→Finset (Fin 6)→ℕ := ![fun T=>if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={4} then 1 else if T={5} then 1 else if T=∅ then 13 else 0,fun T=>if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={5} then 2 else if T=∅ then 12 else 0,fun T=>if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,3,4,5} then 1 else if T={0} then 1 else if T={1} then 1 else if T={2} then 3 else if T={3} then 3 else if T={4} then 3 else if T={5} then 3 else if T=∅ then 10 else 0,fun T=>if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={2,3,5} then 1 else if T={1,4,5} then 1 else if T={0} then 1 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={4} then 2 else if T={5} then 3 else if T=∅ then 11 else 0,fun T=>if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,4} then 1 else if T={2,3,4} then 1 else if T={2,5} then 1 else if T={1,3,5} then 1 else if T={0,4,5} then 1 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 3 else if T={4} then 3 else if T={5} then 3 else if T=∅ then 10 else 0,fun T=>if T={0,1} then 1 else if T={0,2} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={4} then 2 else if T={5} then 2 else if T=∅ then 11 else 0,fun T=>if T={0,1} then 1 else if T={0,2} then 1 else if T={0,3} then 1 else if T={0,4} then 1 else if T={0,5} then 1 else if T={1,2,3,4,5} then 1 else if T={0} then 1 else if T={1} then 4 else if T={2} then 4 else if T={3} then 4 else if T={4} then 4 else if T={5} then 4 else if T=∅ then 7 else 0,fun T=>if T={0,1} then 1 else if T={0,2} then 1 else if T={0,3} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={1,2,3,5} then 1 else if T={0,4,5} then 1 else if T={0} then 2 else if T={1} then 3 else if T={2} then 3 else if T={3} then 3 else if T={4} then 2 else if T={5} then 4 else if T=∅ then 9 else 0,fun T=>if T={0,1} then 1 else if T={2,3} then 1 else if T={0,2,4} then 1 else if T={1,3,4} then 1 else if T={1,2,5} then 1 else if T={0,3,5} then 1 else if T={4,5} then 1 else if T={0} then 3 else if T={1} then 3 else if T={2} then 3 else if T={3} then 3 else if T={4} then 3 else if T={5} then 3 else if T=∅ then 9 else 0]
def upper (T : Finset (Fin 6)) : ℕ := if T=∅ then 34 else if T.card=1 then 6 else 1
abbrev largeCase (i : Case) : TwentyFourNoLowSixData.Case := i.castLE (by omega)
end Aris4Math.ThirtyFour.TwentyFourSixLowUnitData
namespace Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
open Aris4Math.ThirtyThree.ActualBadSlot
open LocalProfiles MixedLayoutApplication TwentyFourSlotAverageTable
set_option maxRecDepth 100000
set_option maxHeartbeats 0
abbrev Layout := Fin 12
abbrev SlotIndex := Fin 47
def μ := TwentyFourSixLowUnitData.μ 7
def labels : List (Finset (Fin 6)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2},{3},{0,3},{1,3},{0,1,3},{2,3},{0,2,3},{1,2,3},{0,1,2,3},{4},{0,4},{1,4},{0,1,4},{2,4},{0,2,4},{1,2,4},{0,1,2,4},{3,4},{0,3,4},{1,3,4},{0,1,3,4},{2,3,4},{0,2,3,4},{1,2,3,4},{0,1,2,3,4},{5},{0,5},{1,5},{0,1,5},{2,5},{0,2,5},{1,2,5},{0,1,2,5},{3,5},{0,3,5},{1,3,5},{0,1,3,5},{2,3,5},{0,2,3,5},{1,2,3,5},{0,1,2,3,5},{4,5},{0,4,5},{1,4,5},{0,1,4,5},{2,4,5},{0,2,4,5},{1,2,4,5},{0,1,2,4,5},{3,4,5},{0,3,4,5},{1,3,4,5},{0,1,3,4,5},{2,3,4,5},{0,2,3,4,5},{1,2,3,4,5},{0,1,2,3,4,5}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem mem_labels : ∀T,T∈labels := by decide +kernel
def positionFn : Layout→Fin 6→Fin 24 := ![![10,9,11,12,13,14],![10,9,12,11,13,14],![10,11,9,12,13,14],![10,11,12,9,13,14],![10,12,9,11,13,14],![10,12,11,9,13,14],![13,9,11,12,10,14],![13,9,12,11,10,14],![13,11,9,12,10,14],![13,11,12,9,10,14],![13,12,9,11,10,14],![13,12,11,9,10,14]]
theorem positionFn_injective : ∀l,Function.Injective (positionFn l) := by
  intro l;fin_cases l <;> decide +kernel
def positions (l : Layout) : Fin 6↪Fin 24 := ⟨positionFn l,positionFn_injective l⟩
def p (l : Layout) : Numeric.Profile :=
  pruneZero ⟨24,executableType (positions l) Finset.univ,
    labels.map (fun T=>⟨executableType (positions l) T,μ T⟩),none,
    List.ofFn (fun j=>(positions l j).val+1)⟩
theorem p_eq (l : Layout) : p l=profile labels (positions l) μ (List.ofFn fun j=>(positions l j).val+1) := by
  simp only [p,executableType_eq,profile,rawProfile]
def computed : Layout→Numeric.Profile := ![⟨24,[10,11,12,13,14,15],[⟨[],9⟩,⟨[11],2⟩,⟨[10],3⟩,⟨[10,11],1⟩,⟨[12],3⟩,⟨[11,12],1⟩,⟨[13],3⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],4⟩,⟨[10,12,13,15],1⟩,⟨[11,14,15],1⟩],none,[11,10,12,13,14,15]⟩,⟨24,[10,11,12,13,14,15],[⟨[],9⟩,⟨[11],2⟩,⟨[10],3⟩,⟨[10,11],1⟩,⟨[13],3⟩,⟨[11,13],1⟩,⟨[12],3⟩,⟨[11,12],1⟩,⟨[14],2⟩,⟨[10,14],1⟩,⟨[13,14],1⟩,⟨[12,14],1⟩,⟨[15],4⟩,⟨[10,12,13,15],1⟩,⟨[11,14,15],1⟩],none,[11,10,13,12,14,15]⟩,⟨24,[10,11,12,13,14,15],[⟨[],9⟩,⟨[11],2⟩,⟨[12],3⟩,⟨[11,12],1⟩,⟨[10],3⟩,⟨[10,11],1⟩,⟨[13],3⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[12,14],1⟩,⟨[10,14],1⟩,⟨[13,14],1⟩,⟨[15],4⟩,⟨[10,12,13,15],1⟩,⟨[11,14,15],1⟩],none,[11,12,10,13,14,15]⟩,⟨24,[10,11,12,13,14,15],[⟨[],9⟩,⟨[11],2⟩,⟨[12],3⟩,⟨[11,12],1⟩,⟨[13],3⟩,⟨[11,13],1⟩,⟨[10],3⟩,⟨[10,11],1⟩,⟨[14],2⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[10,14],1⟩,⟨[15],4⟩,⟨[10,12,13,15],1⟩,⟨[11,14,15],1⟩],none,[11,12,13,10,14,15]⟩,⟨24,[10,11,12,13,14,15],[⟨[],9⟩,⟨[11],2⟩,⟨[13],3⟩,⟨[11,13],1⟩,⟨[10],3⟩,⟨[10,11],1⟩,⟨[12],3⟩,⟨[11,12],1⟩,⟨[14],2⟩,⟨[13,14],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[15],4⟩,⟨[10,12,13,15],1⟩,⟨[11,14,15],1⟩],none,[11,13,10,12,14,15]⟩,⟨24,[10,11,12,13,14,15],[⟨[],9⟩,⟨[11],2⟩,⟨[13],3⟩,⟨[11,13],1⟩,⟨[12],3⟩,⟨[11,12],1⟩,⟨[10],3⟩,⟨[10,11],1⟩,⟨[14],2⟩,⟨[13,14],1⟩,⟨[12,14],1⟩,⟨[10,14],1⟩,⟨[15],4⟩,⟨[10,12,13,15],1⟩,⟨[11,14,15],1⟩],none,[11,13,12,10,14,15]⟩,⟨24,[10,11,12,13,14,15],[⟨[],9⟩,⟨[14],2⟩,⟨[10],3⟩,⟨[10,14],1⟩,⟨[12],3⟩,⟨[12,14],1⟩,⟨[13],3⟩,⟨[13,14],1⟩,⟨[11],2⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[11,13],1⟩,⟨[15],4⟩,⟨[10,12,13,15],1⟩,⟨[11,14,15],1⟩],none,[14,10,12,13,11,15]⟩,⟨24,[10,11,12,13,14,15],[⟨[],9⟩,⟨[14],2⟩,⟨[10],3⟩,⟨[10,14],1⟩,⟨[13],3⟩,⟨[13,14],1⟩,⟨[12],3⟩,⟨[12,14],1⟩,⟨[11],2⟩,⟨[10,11],1⟩,⟨[11,13],1⟩,⟨[11,12],1⟩,⟨[15],4⟩,⟨[10,12,13,15],1⟩,⟨[11,14,15],1⟩],none,[14,10,13,12,11,15]⟩,⟨24,[10,11,12,13,14,15],[⟨[],9⟩,⟨[14],2⟩,⟨[12],3⟩,⟨[12,14],1⟩,⟨[10],3⟩,⟨[10,14],1⟩,⟨[13],3⟩,⟨[13,14],1⟩,⟨[11],2⟩,⟨[11,12],1⟩,⟨[10,11],1⟩,⟨[11,13],1⟩,⟨[15],4⟩,⟨[10,12,13,15],1⟩,⟨[11,14,15],1⟩],none,[14,12,10,13,11,15]⟩,⟨24,[10,11,12,13,14,15],[⟨[],9⟩,⟨[14],2⟩,⟨[12],3⟩,⟨[12,14],1⟩,⟨[13],3⟩,⟨[13,14],1⟩,⟨[10],3⟩,⟨[10,14],1⟩,⟨[11],2⟩,⟨[11,12],1⟩,⟨[11,13],1⟩,⟨[10,11],1⟩,⟨[15],4⟩,⟨[10,12,13,15],1⟩,⟨[11,14,15],1⟩],none,[14,12,13,10,11,15]⟩,⟨24,[10,11,12,13,14,15],[⟨[],9⟩,⟨[14],2⟩,⟨[13],3⟩,⟨[13,14],1⟩,⟨[10],3⟩,⟨[10,14],1⟩,⟨[12],3⟩,⟨[12,14],1⟩,⟨[11],2⟩,⟨[11,13],1⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[15],4⟩,⟨[10,12,13,15],1⟩,⟨[11,14,15],1⟩],none,[14,13,10,12,11,15]⟩,⟨24,[10,11,12,13,14,15],[⟨[],9⟩,⟨[14],2⟩,⟨[13],3⟩,⟨[13,14],1⟩,⟨[12],3⟩,⟨[12,14],1⟩,⟨[10],3⟩,⟨[10,14],1⟩,⟨[11],2⟩,⟨[11,13],1⟩,⟨[11,12],1⟩,⟨[10,11],1⟩,⟨[15],4⟩,⟨[10,12,13,15],1⟩,⟨[11,14,15],1⟩],none,[14,13,12,10,11,15]⟩]
theorem p_eq_computed (l : Layout) : p l=computed l := by fin_cases l <;> rfl
def gamma : Layout→ℚ := ![(1/12:ℚ),(1/12:ℚ),(1/12:ℚ),(1/12:ℚ),(1/12:ℚ),(1/12:ℚ),(1/12:ℚ),(1/12:ℚ),(1/12:ℚ),(1/12:ℚ),(1/12:ℚ),(1/12:ℚ)]
def centerBound : Fin 6→ℚ := ![(107/935:ℚ),(161/1430:ℚ),(161/1430:ℚ),(161/1430:ℚ),(107/935:ℚ),(14/85:ℚ)]
abbrev PositiveIndex := Fin 15
def positive : PositiveIndex→Finset (Fin 6) := ![∅,{0},{1},{0,1},{2},{0,2},{3},{0,3},{4},{1,4},{2,4},{3,4},{5},{1,2,3,5},{0,4,5}]
def slot : SlotIndex→Slot 6 := ![⟨0,{0},{0}⟩,⟨0,{0},{0,1}⟩,⟨0,{0},{0,2}⟩,⟨0,{0},{0,3}⟩,⟨0,{0},{0,4,5}⟩,⟨0,{0,1},{0,2}⟩,⟨0,{0,1},{0,3}⟩,⟨0,{0,1},{0,4,5}⟩,⟨0,{0,2},{0,3}⟩,⟨0,{0,2},{0,4,5}⟩,⟨0,{0,3},{0,4,5}⟩,⟨1,{1},{1}⟩,⟨1,{1},{0,1}⟩,⟨1,{1},{1,4}⟩,⟨1,{1},{1,2,3,5}⟩,⟨1,{0,1},{1,4}⟩,⟨1,{0,1},{1,2,3,5}⟩,⟨1,{1,4},{1,2,3,5}⟩,⟨2,{2},{2}⟩,⟨2,{2},{0,2}⟩,⟨2,{2},{2,4}⟩,⟨2,{2},{1,2,3,5}⟩,⟨2,{0,2},{2,4}⟩,⟨2,{0,2},{1,2,3,5}⟩,⟨2,{2,4},{1,2,3,5}⟩,⟨3,{3},{3}⟩,⟨3,{3},{0,3}⟩,⟨3,{3},{3,4}⟩,⟨3,{3},{1,2,3,5}⟩,⟨3,{0,3},{3,4}⟩,⟨3,{0,3},{1,2,3,5}⟩,⟨3,{3,4},{1,2,3,5}⟩,⟨4,{4},{4}⟩,⟨4,{4},{1,4}⟩,⟨4,{4},{2,4}⟩,⟨4,{4},{3,4}⟩,⟨4,{4},{0,4,5}⟩,⟨4,{1,4},{2,4}⟩,⟨4,{1,4},{3,4}⟩,⟨4,{1,4},{0,4,5}⟩,⟨4,{2,4},{3,4}⟩,⟨4,{2,4},{0,4,5}⟩,⟨4,{3,4},{0,4,5}⟩,⟨5,{5},{5}⟩,⟨5,{5},{1,2,3,5}⟩,⟨5,{5},{0,4,5}⟩,⟨5,{1,2,3,5},{0,4,5}⟩]
def freeValue : Layout→ℚ := ![(9/34:ℚ),(9/34:ℚ),(9/34:ℚ),(9/34:ℚ),(9/34:ℚ),(9/34:ℚ),(9/34:ℚ),(9/34:ℚ),(9/34:ℚ),(9/34:ℚ),(9/34:ℚ),(9/34:ℚ)]
def aValue : Layout→Fin 6→ℚ := ![![(63/340:ℚ),(21/170:ℚ),(77/340:ℚ),(77/340:ℚ),(7/85:ℚ),(14/85:ℚ)],![(63/340:ℚ),(21/170:ℚ),(77/340:ℚ),(77/340:ℚ),(7/85:ℚ),(14/85:ℚ)],![(63/340:ℚ),(77/340:ℚ),(21/170:ℚ),(77/340:ℚ),(7/85:ℚ),(14/85:ℚ)],![(63/340:ℚ),(77/340:ℚ),(77/340:ℚ),(21/170:ℚ),(7/85:ℚ),(14/85:ℚ)],![(63/340:ℚ),(77/340:ℚ),(21/170:ℚ),(77/340:ℚ),(7/85:ℚ),(14/85:ℚ)],![(63/340:ℚ),(77/340:ℚ),(77/340:ℚ),(21/170:ℚ),(7/85:ℚ),(14/85:ℚ)],![(7/85:ℚ),(21/170:ℚ),(77/340:ℚ),(77/340:ℚ),(63/340:ℚ),(14/85:ℚ)],![(7/85:ℚ),(21/170:ℚ),(77/340:ℚ),(77/340:ℚ),(63/340:ℚ),(14/85:ℚ)],![(7/85:ℚ),(77/340:ℚ),(21/170:ℚ),(77/340:ℚ),(63/340:ℚ),(14/85:ℚ)],![(7/85:ℚ),(77/340:ℚ),(77/340:ℚ),(21/170:ℚ),(63/340:ℚ),(14/85:ℚ)],![(7/85:ℚ),(77/340:ℚ),(21/170:ℚ),(77/340:ℚ),(63/340:ℚ),(14/85:ℚ)],![(7/85:ℚ),(77/340:ℚ),(77/340:ℚ),(21/170:ℚ),(63/340:ℚ),(14/85:ℚ)]]
def cValue : Layout→Fin 6→ℚ := ![![(162/935:ℚ),(1629/9724:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(63/935:ℚ),(567/2431:ℚ)],![(162/935:ℚ),(1629/9724:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(63/935:ℚ),(567/2431:ℚ)],![(162/935:ℚ),(1302/12155:ℚ),(1629/9724:ℚ),(1302/12155:ℚ),(63/935:ℚ),(567/2431:ℚ)],![(162/935:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(1629/9724:ℚ),(63/935:ℚ),(567/2431:ℚ)],![(162/935:ℚ),(1302/12155:ℚ),(1629/9724:ℚ),(1302/12155:ℚ),(63/935:ℚ),(567/2431:ℚ)],![(162/935:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(1629/9724:ℚ),(63/935:ℚ),(567/2431:ℚ)],![(63/935:ℚ),(1629/9724:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(162/935:ℚ),(567/2431:ℚ)],![(63/935:ℚ),(1629/9724:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(162/935:ℚ),(567/2431:ℚ)],![(63/935:ℚ),(1302/12155:ℚ),(1629/9724:ℚ),(1302/12155:ℚ),(162/935:ℚ),(567/2431:ℚ)],![(63/935:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(1629/9724:ℚ),(162/935:ℚ),(567/2431:ℚ)],![(63/935:ℚ),(1302/12155:ℚ),(1629/9724:ℚ),(1302/12155:ℚ),(162/935:ℚ),(567/2431:ℚ)],![(63/935:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(1629/9724:ℚ),(162/935:ℚ),(567/2431:ℚ)]]
def valueValue : Layout→SlotIndex→ℚ := ![![(36/221:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(1908/12155:ℚ),(375/2431:ℚ),(375/2431:ℚ),(129/935:ℚ),(162/935:ℚ),(162/935:ℚ),(162/935:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(63/1105:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ)],![(36/221:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(1908/12155:ℚ),(375/2431:ℚ),(375/2431:ℚ),(129/935:ℚ),(162/935:ℚ),(162/935:ℚ),(162/935:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(63/1105:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ)],![(36/221:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(1908/12155:ℚ),(375/2431:ℚ),(162/935:ℚ),(162/935:ℚ),(375/2431:ℚ),(129/935:ℚ),(162/935:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(63/1105:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ)],![(36/221:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(1908/12155:ℚ),(162/935:ℚ),(375/2431:ℚ),(162/935:ℚ),(375/2431:ℚ),(162/935:ℚ),(129/935:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(63/1105:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ)],![(36/221:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(1908/12155:ℚ),(375/2431:ℚ),(162/935:ℚ),(162/935:ℚ),(375/2431:ℚ),(129/935:ℚ),(162/935:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(63/1105:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ)],![(36/221:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(1908/12155:ℚ),(162/935:ℚ),(375/2431:ℚ),(162/935:ℚ),(375/2431:ℚ),(162/935:ℚ),(129/935:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(63/1105:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ)],![(63/1105:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(36/221:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(1908/12155:ℚ),(375/2431:ℚ),(375/2431:ℚ),(129/935:ℚ),(162/935:ℚ),(162/935:ℚ),(162/935:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ)],![(63/1105:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(36/221:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(1908/12155:ℚ),(375/2431:ℚ),(375/2431:ℚ),(129/935:ℚ),(162/935:ℚ),(162/935:ℚ),(162/935:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ)],![(63/1105:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(36/221:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(1908/12155:ℚ),(375/2431:ℚ),(162/935:ℚ),(162/935:ℚ),(375/2431:ℚ),(129/935:ℚ),(162/935:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ)],![(63/1105:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(36/221:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(1908/12155:ℚ),(162/935:ℚ),(375/2431:ℚ),(162/935:ℚ),(375/2431:ℚ),(162/935:ℚ),(129/935:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ)],![(63/1105:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(36/221:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(1908/12155:ℚ),(375/2431:ℚ),(162/935:ℚ),(162/935:ℚ),(375/2431:ℚ),(129/935:ℚ),(162/935:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ)],![(63/1105:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(1407/24310:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(63/935:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(1176/12155:ℚ),(2373/24310:ℚ),(2373/24310:ℚ),(1302/12155:ℚ),(63/715:ℚ),(1302/12155:ℚ),(1302/12155:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(21/170:ℚ),(36/221:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(3981/24310:ℚ),(1908/12155:ℚ),(162/935:ℚ),(375/2431:ℚ),(162/935:ℚ),(375/2431:ℚ),(162/935:ℚ),(129/935:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ),(14/85:ℚ)]]
end Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7
namespace Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7
open scoped BigOperators
open Aris4Math.ThirtyThree.ActualBadSlot
open MixedLayoutApplication TwentyFourSlotAverageTable
set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem rows_0 : TwentyFourSlotAverageCache.cachedFree (positions 0) (p 0)=freeValue 0 ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions 0) (p 0) j=aValue 0 j ∧
      TwentyFourSlotAverageCache.cachedC (positions 0) (p 0) j=cValue 0 j) := by
  simp only [TwentyFourSlotAverageCache.cachedFree,TwentyFourSlotAverageCache.cachedA,
    TwentyFourSlotAverageCache.cachedC,p_eq_computed]
  decide +kernel

theorem rows_1 : TwentyFourSlotAverageCache.cachedFree (positions 1) (p 1)=freeValue 1 ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions 1) (p 1) j=aValue 1 j ∧
      TwentyFourSlotAverageCache.cachedC (positions 1) (p 1) j=cValue 1 j) := by
  simp only [TwentyFourSlotAverageCache.cachedFree,TwentyFourSlotAverageCache.cachedA,
    TwentyFourSlotAverageCache.cachedC,p_eq_computed]
  decide +kernel

theorem rows_2 : TwentyFourSlotAverageCache.cachedFree (positions 2) (p 2)=freeValue 2 ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions 2) (p 2) j=aValue 2 j ∧
      TwentyFourSlotAverageCache.cachedC (positions 2) (p 2) j=cValue 2 j) := by
  simp only [TwentyFourSlotAverageCache.cachedFree,TwentyFourSlotAverageCache.cachedA,
    TwentyFourSlotAverageCache.cachedC,p_eq_computed]
  decide +kernel

theorem rows_3 : TwentyFourSlotAverageCache.cachedFree (positions 3) (p 3)=freeValue 3 ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions 3) (p 3) j=aValue 3 j ∧
      TwentyFourSlotAverageCache.cachedC (positions 3) (p 3) j=cValue 3 j) := by
  simp only [TwentyFourSlotAverageCache.cachedFree,TwentyFourSlotAverageCache.cachedA,
    TwentyFourSlotAverageCache.cachedC,p_eq_computed]
  decide +kernel

theorem rows_4 : TwentyFourSlotAverageCache.cachedFree (positions 4) (p 4)=freeValue 4 ∧
    (∀j,TwentyFourSlotAverageCache.cachedA (positions 4) (p 4) j=aValue 4 j ∧
      TwentyFourSlotAverageCache.cachedC (positions 4) (p 4) j=cValue 4 j) := by
  simp only [TwentyFourSlotAverageCache.cachedFree,TwentyFourSlotAverageCache.cachedA,
    TwentyFourSlotAverageCache.cachedC,p_eq_computed]
  decide +kernel
end Aris4Math.ThirtyFour.TwentyFourSixLowUnitAverage7