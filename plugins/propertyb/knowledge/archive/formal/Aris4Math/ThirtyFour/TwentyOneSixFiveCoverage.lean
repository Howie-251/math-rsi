import Aris4Math.ThirtyFour.TwentyOneSixFive66888
import Aris4Math.ThirtyFour.TwentyOneSixFive67888
import Aris4Math.ThirtyFour.TwentyOneSixJoint0
import Aris4Math.ThirtyFour.TwentyOneSixJoint1
import Aris4Math.ThirtyFour.TwentyOneSixJoint2
import Aris4Math.ThirtyFour.TwentyOneSixJoint3
import Aris4Math.ThirtyFour.TwentyOneSixJoint4
namespace Aris4Math.ThirtyFour.TwentyOneSixFiveCoverage
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
set_option maxRecDepth 100000
set_option maxHeartbeats 0
abbrev Kind:=Fin 2
abbrev Case:=Fin 14

def μ (kind : Kind) (i : Case) (T : Finset (Fin 5)) : ℕ :=
  if kind=0 then TwentyOneSixFive66888Data.μ i T else
  if hi : i.val<9 then TwentyOneSixFive67888Data.μ ⟨i.val,hi⟩ T else
    (![TwentyOneSixJoint0Data.μ,TwentyOneSixJoint1Data.μ,TwentyOneSixJoint2Data.μ,
       TwentyOneSixJoint3Data.μ,TwentyOneSixJoint4Data.μ] : Fin 5→Finset (Fin 5)→ℕ)
        ⟨i.val-9,by omega⟩ T

def degree (kind : Kind) : Fin 5→ℕ := ![6,6+kind.val,8,8,8]
def pair (kind : Kind) (i j : Fin 5) : ℕ :=
  if i=j then degree kind i else
  if ({i,j} : Finset (Fin 5))={0,1} then 2-kind.val else
  if 2≤i.val ∧ 2≤j.val then 2 else 1

def low (kind : Kind) (T : Finset (Fin 5)) : ℕ :=
  if T=∅ then 34 else
  if T.card=1 then ∑i∈T,degree kind i else
  if T={0,1} then 2-kind.val else if T⊆{2,3,4} then 2 else 1

theorem low_empty (k : Kind) : low k ∅=34 := rfl
theorem low_singleton : ∀k i,low k {i}=degree k i := by decide +kernel
theorem low_pair : ∀k i j,i≠j→low k {i,j}=pair k i j := by decide +kernel

theorem recovered_eq : ∀k i T,μ k i T=recovered (low k) (μ k i) T := by decide +kernel

def highLabels : Fin 8→Finset (Fin 5) :=
  ![{0,2,3},{0,2,4},{0,3,4},{0,2,3,4},{1,2,3},{1,2,4},{1,3,4},{1,2,3,4}]
def high (h : Fin 8→Fin 2) (t : Fin 3) (T : Finset (Fin 5)) : ℕ :=
  if T={2,3,4} then t.val else ∑j,if T=highLabels j then (h j).val else 0

theorem high_at : ∀h t j,high h t (highLabels j)=(h j).val := by decide +kernel
theorem high_tail : ∀h t,high h t {2,3,4}=t.val := by decide +kernel
theorem high_xy_zero : ∀h t T,0∈T→1∈T→high h t T=0 := by decide +kernel

theorem high_types : ∀T : Finset (Fin 5),3≤T.card→
    (0∈T ∧ 1∈T) ∨ (∃j,T=highLabels j) ∨ T={2,3,4} := by decide +kernel

theorem xuv_sum : ∀h t,
    (∑U∈Finset.univ.filter (fun U=>({0,2,3} : Finset (Fin 5))⊆U),high h t U)=(h 0).val+(h 3).val := by decide +kernel

theorem coverage : ∀k : Kind,∀h : Fin 8→Fin 2,∀t : Fin 3,
    (h 0).val+(h 3).val=1→
    (∀i j : Fin 5,i≠j→(∑T∈supers {i,j} 3,high h t T)≤pair k i j)→
    ∃a : Case,∀T,3≤T.card→high h t T=μ k a T := by decide +kernel

theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 21)) (f : Fin 5↪Fin 21)
    (k : Kind) (i : Case) (counts : ∀T,count H f T=μ k i T) : PropertyB H := by
  by_cases k0 : k=0
  · apply TwentyOneSixFive66888.propertyB_of_counts H f i
    simpa only [μ,if_pos k0] using counts
  · by_cases small : i.val<9
    · apply TwentyOneSixFive67888.propertyB_of_counts H f ⟨i.val,small⟩
      simpa only [μ,if_neg k0,dif_pos small] using counts
    · have upper : i.val<14 := i.isLt
      have lower : 9≤i.val := by omega
      interval_cases hi : i.val <;>
        simp only [μ,if_neg k0,dif_neg small,hi] at counts
      · exact TwentyOneSixJoint0.propertyB_of_counts H f counts
      · exact TwentyOneSixJoint1.propertyB_of_counts H f counts
      · exact TwentyOneSixJoint2.propertyB_of_counts H f counts
      · exact TwentyOneSixJoint3.propertyB_of_counts H f counts
      · exact TwentyOneSixJoint4.propertyB_of_counts H f counts
end Aris4Math.ThirtyFour.TwentyOneSixFiveCoverage
