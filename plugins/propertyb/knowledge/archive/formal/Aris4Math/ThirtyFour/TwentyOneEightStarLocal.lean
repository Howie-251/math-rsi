import Aris4Math.ThirtyFour.TwentyOneEightFive88888
import Aris4Math.ThirtyFour.TwentyOneEightJointStar0
namespace Aris4Math.ThirtyFour.TwentyOneEightStarLocal
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery
set_option maxHeartbeats 0
set_option maxRecDepth 100000

def pair (i j : Fin 5) : ℕ:=if i=0 ∨ j=0 then 1 else 2
def high (q : Fin 2) (T : Finset (Fin 5)) : ℕ:=
  if T={0,1,2,3} then 1 else if T={1,2,3} then 1-q.val else if T={1,2,3,4} then q.val else 0
def low (T : Finset (Fin 5)) : ℕ:=
  if T=∅ then 34 else if T.card=1 then 8 else if 0∈T then 1 else 2
def μ (q : Fin 2) (T : Finset (Fin 5)) : ℕ:=
  if q=0 then TwentyOneEightJointStar0Data.μ T else TwentyOneEightFive88888Data.μ 0 T

theorem low_empty : low ∅=34 := rfl
theorem low_single : ∀i,low {i}=8 := by decide +kernel
theorem low_pair : ∀i j,i≠j→low {i,j}=pair i j := by decide +kernel
theorem recovered_eq : ∀q T,μ q T=recovered low (high q) T := by decide +kernel

/-- The two star extensions, including the genuinely mixed three-layout one. -/
theorem propertyB_of_high (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (f : Fin 5↪Fin 21) (degrees : ∀j,H.degree (f j)=8)
    (pairs : ∀i j,i≠j→H.codegree (f i) (f j)=pair i j)
    (q : Fin 2) (hhigh : ∀T,3≤T.card→count H f T=high q T) : PropertyB H := by
  have hlow : ∀T,T.card≤2→upperCount H f T=low T := by
    apply upper_eq_of_low_data
    · exact low_empty.trans size.symm
    · intro i;exact (low_single i).trans (degrees i).symm
    · intro i j ne;exact (low_pair i j ne).trans (pairs i j ne).symm
  have counts (T) : count H f T=μ q T := by
    rw [recovered_eq]
    exact actual_recovered H f low (high q) hlow hhigh T
  by_cases qzero : q=0
  · apply TwentyOneEightJointStar0.propertyB_of_counts H f
    simpa only [μ,if_pos qzero] using counts
  · apply TwentyOneEightFive88888.propertyB_of_counts H f 0
    simpa only [μ,if_neg qzero] using counts
end Aris4Math.ThirtyFour.TwentyOneEightStarLocal
#print axioms Aris4Math.ThirtyFour.TwentyOneEightStarLocal.propertyB_of_high
