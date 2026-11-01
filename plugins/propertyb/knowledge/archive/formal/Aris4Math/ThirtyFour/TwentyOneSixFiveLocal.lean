import Aris4Math.ThirtyFour.TwentyOneSixFiveCoverage
import Aris4Math.ThirtyThree.TwentyOnePairAssembly
namespace Aris4Math.ThirtyFour.TwentyOneSixFiveLocal
open scoped BigOperators
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TripleProfiles (tripleCodegree)
open TwentyOneSixFiveCoverage
set_option maxRecDepth 100000
set_option maxHeartbeats 0

def tail (j : Fin 3) : Fin 5:=⟨j.val+2,by omega⟩
def first : Fin 8→Fin 5:=![0,0,0,0,1,1,1,1]
def second : Fin 8→Fin 5:=![2,2,3,2,2,2,3,2]
theorem label_pair : ∀k j,
    first j∈highLabels j ∧ second j∈highLabels j ∧ first j≠second j ∧ pair k (first j) (second j)=1 := by decide +kernel
theorem xy_third : ∀T : Finset (Fin 5),3≤T.card→0∈T→1∈T→∃j:Fin 3,tail j∈T := by decide +kernel

theorem propertyB_of_five (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (f : Fin 5↪Fin 21) (kind : Kind)
    (hd : ∀j,H.degree (f j)=degree kind j)
    (hc : ∀i j,i≠j→H.codegree (f i) (f j)=pair kind i j)
    (noXY : ∀j:Fin 3,tripleCodegree H (f 0) (f 1) (f (tail j))=0)
    (xuv : tripleCodegree H (f 0) (f 2) (f 3)=1) : PropertyB H := by
  have hlow : ∀T,T.card≤2→upperCount H f T=low kind T := by
    apply upper_eq_of_low_data
    · exact (low_empty kind).trans size.symm
    · intro j; exact (low_singleton kind j).trans (hd j).symm
    · intro i j ne; exact (low_pair kind i j ne).trans (hc i j ne).symm
  have small (j : Fin 8) : count H f (highLabels j)≤1 := by
    obtain ⟨hi,hj,ne,unit⟩:=label_pair kind j
    exact (count_le_codegree H f (highLabels j) (first j) (second j) hi hj).trans_eq
      ((hc _ _ ne).trans unit)
  have tailSmall : count H f {2,3,4}≤2 := by
    have bound:=count_le_codegree H f {2,3,4} 2 3 (by decide) (by decide)
    rw [hc 2 3 (by decide)] at bound
    exact bound
  let h : Fin 8→Fin 2:=fun j=>⟨count H f (highLabels j),by have:=small j;omega⟩
  let t : Fin 3:=⟨count H f {2,3,4},by omega⟩
  have highXY (T : Finset (Fin 5)) (large : 3≤T.card) (h0 : 0∈T) (h1 : 1∈T) : count H f T=0 := by
    by_contra nonzero
    obtain ⟨j,hj⟩:=xy_third T large h0 h1
    obtain ⟨e,he⟩:=Finset.card_pos.mp (by omega : 0<count H f T)
    obtain ⟨he,sig⟩:=Finset.mem_filter.mp he
    have member (i : Fin 5) (hi : i∈T) : f i∈e :=
      (mem_lockSignature f e i).mp (sig ▸ hi)
    have positive : 1≤tripleCodegree H (f 0) (f 1) (f (tail j)) :=
      Finset.one_le_card.mpr ⟨e,Finset.mem_filter.mpr ⟨he,member 0 h0,member 1 h1,member _ hj⟩⟩
    rw [noXY j] at positive
    omega
  have hhigh (T : Finset (Fin 5)) (large : 3≤T.card) : count H f T=high h t T := by
    rcases high_types T large with ⟨h0,h1⟩ | ⟨j,rfl⟩ | rfl
    · rw [highXY T large h0 h1,high_xy_zero h t T h0 h1]
    · rw [high_at]
    · rw [high_tail]
  have hx : (h 0).val+(h 3).val=1 := by
    have sums:=sum_supers H f ({0,2,3}:Finset (Fin 5))
    have supEq : (∑U∈Finset.univ.filter (fun U=>({0,2,3}:Finset (Fin 5))⊆U),count H f U)=
        ∑U∈Finset.univ.filter (fun U=>({0,2,3}:Finset (Fin 5))⊆U),high h t U := by
      apply Finset.sum_congr rfl
      intro U hU
      apply hhigh
      have cu:=Finset.card_le_card (Finset.mem_filter.mp hU).2
      have c3 : ({0,2,3}:Finset (Fin 5)).card=3 := by decide
      omega
    rw [supEq,xuv_sum] at sums
    have upperEq : upperCount H f ({0,2,3}:Finset (Fin 5))=tripleCodegree H (f 0) (f 2) (f 3) := by
      simp [upperCount,tripleCodegree,Finset.insert_subset_iff]
    rw [upperEq,xuv] at sums
    exact sums
  have inventory (i j : Fin 5) (ne : i≠j) : (∑T∈supers {i,j} 3,high h t T)≤pair kind i j := by
    have bound:=high_pair_budget H f i j ne
    have eq : (∑T∈supers {i,j} 3,count H f T)=(∑T∈supers {i,j} 3,high h t T) :=
      Finset.sum_congr rfl (fun T hT=>hhigh T (Finset.mem_filter.mp hT).2.2)
    rw [eq,hc i j ne] at bound
    exact bound
  obtain ⟨i,matchHigh⟩:=coverage kind h t hx inventory
  apply propertyB_of_counts H f kind i
  intro T
  rw [recovered_eq]
  exact actual_recovered H f (low kind) (μ kind i) hlow
    (fun U hU=>(hhigh U hU).trans (matchHigh U hU)) T
end Aris4Math.ThirtyFour.TwentyOneSixFiveLocal
#print axioms Aris4Math.ThirtyFour.TwentyOneSixFiveLocal.propertyB_of_five
