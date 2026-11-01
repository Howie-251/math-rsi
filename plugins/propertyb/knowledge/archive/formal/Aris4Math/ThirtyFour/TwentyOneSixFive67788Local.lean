import Aris4Math.ThirtyFour.TwentyOneSixFive67788
import Aris4Math.ThirtyThree.TwentyOnePairAssembly
namespace Aris4Math.ThirtyFour.TwentyOneSixFive67788Local
open scoped BigOperators
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TripleProfiles (tripleCodegree)
open TwentyOneSixFive67788Data (degree μ Case)
set_option maxRecDepth 100000
set_option maxHeartbeats 0

def root (j : Fin 3) : Fin 5:=j.castLE (by decide)
def tail (j : Fin 2) : Fin 5:=⟨j.val+3,by omega⟩
def pair (b : Fin 2) (i j : Fin 5) : ℕ:=
  if i=j then degree i else if ({i,j}:Finset (Fin 5))={1,2} then 2 else
  if ({i,j}:Finset (Fin 5))={3,4} then b.val+1 else 1

def low (b : Fin 2) (T : Finset (Fin 5)) : ℕ:=
  if T=∅ then 34 else if T.card=1 then ∑i∈T,degree i else
  if T={1,2} then 2 else if T={3,4} then b.val+1 else 1

def high (h : Fin 3→Fin 2) (q : Fin 2) (T : Finset (Fin 5)) : ℕ:=
  if T={0,1,2} then q.val else ∑i,if T={root i,3,4} then (h i).val else 0

theorem low_empty (b) : low b ∅=34 := rfl
theorem low_single : ∀b i,low b {i}=degree i := by decide +kernel
theorem low_pair : ∀b i j,i≠j→low b {i,j}=pair b i j := by decide +kernel
theorem high_root : ∀h q,high h q {0,1,2}=q.val := by decide +kernel
theorem high_at : ∀h q i,high h q {root i,3,4}=(h i).val := by decide +kernel
theorem high_zero : ∀h q i j t,i≠j→∀T,root i∈T→ root j∈T→ tail t∈T→high h q T=0 := by decide +kernel
theorem high_types : ∀T : Finset (Fin 5),3≤T.card→
  T={0,1,2} ∨ (∃i,T={root i,3,4}) ∨
  (∃i j : Fin 3,∃t : Fin 2,i≠j ∧ root i∈T ∧ root j∈T ∧ tail t∈T) := by decide +kernel
theorem root_sum : ∀h q,(∑U∈Finset.univ.filter (fun U=>({0,1,2}:Finset (Fin 5))⊆U),high h q U)=q.val := by decide +kernel
theorem coverage : ∀b : Fin 2,∀h : Fin 3→Fin 2,
    (∀i j : Fin 5,i≠j→(∑T∈supers {i,j} 3,high h 1 T)≤pair b i j)→
    ∃c : Case,(∀T,T.card≤2→low b T=TwentyOneSixFive67788Data.upper c T) ∧
      (∀T,3≤T.card→high h 1 T=μ c T) := by decide +kernel

/-- The eleven complete local profiles, derived from actual five-lock data. -/
theorem propertyB_of_five (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (f : Fin 5↪Fin 21) (b : Fin 2)
    (hd : ∀j,H.degree (f j)=degree j)
    (hc : ∀i j,i≠j→H.codegree (f i) (f j)=pair b i j)
    (xyz : tripleCodegree H (f 0) (f 1) (f 2)=1)
    (clean : ∀i j : Fin 3,i≠j→∀t : Fin 2,
      tripleCodegree H (f (root i)) (f (root j)) (f (tail t))=0) : PropertyB H := by
  have hlow : ∀T,T.card≤2→upperCount H f T=low b T := by
    apply upper_eq_of_low_data
    · exact (low_empty b).trans size.symm
    · intro j;exact (low_single b j).trans (hd j).symm
    · intro i j ne;exact (low_pair b i j ne).trans (hc i j ne).symm
  have unitRoot (i : Fin 3) : pair b (root i) 3=1 := by fin_cases b <;> fin_cases i <;> decide
  have small (i : Fin 3) : count H f {root i,3,4}≤1 := by
    have ne : root i≠3 := by fin_cases i <;> decide
    exact (count_le_codegree H f {root i,3,4} (root i) 3 (by simp) (by simp)).trans_eq
      ((hc _ _ ne).trans (unitRoot i))
  have qsmall : count H f {0,1,2}≤1 := by
    have bound:=count_le_codegree H f {0,1,2} 0 1 (by decide) (by decide)
    rw [hc 0 1 (by decide)] at bound
    exact bound
  let h : Fin 3→Fin 2:=fun i=>⟨count H f {root i,3,4},by have:=small i;omega⟩
  let q : Fin 2:=⟨count H f {0,1,2},by omega⟩
  have forbidden (T : Finset (Fin 5)) (i j : Fin 3) (t : Fin 2) (ne : i≠j)
      (hi : root i∈T) (hj : root j∈T) (ht : tail t∈T) : count H f T=0 := by
    by_contra nz
    obtain ⟨e,he⟩:=Finset.card_pos.mp (by omega : 0<count H f T)
    obtain ⟨he,sig⟩:=Finset.mem_filter.mp he
    have member (k : Fin 5) (hk : k∈T) : f k∈e := (mem_lockSignature f e k).mp (sig ▸ hk)
    have pos : 1≤tripleCodegree H (f (root i)) (f (root j)) (f (tail t)) :=
      Finset.one_le_card.mpr ⟨e,Finset.mem_filter.mpr ⟨he,member _ hi,member _ hj,member _ ht⟩⟩
    rw [clean i j ne t] at pos
    omega
  have hhigh (T : Finset (Fin 5)) (large : 3≤T.card) : count H f T=high h q T := by
    rcases high_types T large with rfl | ⟨i,rfl⟩ | ⟨i,j,t,ne,hi,hj,ht⟩
    · rw [high_root]
    · rw [high_at]
    · rw [forbidden T i j t ne hi hj ht,high_zero h q i j t ne T hi hj ht]
  have qone : q=1 := by
    have sums:=sum_supers H f ({0,1,2}:Finset (Fin 5))
    have eq : (∑U∈Finset.univ.filter (fun U=>({0,1,2}:Finset (Fin 5))⊆U),count H f U)=
        ∑U∈Finset.univ.filter (fun U=>({0,1,2}:Finset (Fin 5))⊆U),high h q U := by
      apply Finset.sum_congr rfl
      intro U hu
      apply hhigh
      have bound:=Finset.card_le_card (Finset.mem_filter.mp hu).2
      have card : ({0,1,2}:Finset (Fin 5)).card=3 := by decide
      omega
    rw [eq,root_sum] at sums
    have upperEq : upperCount H f ({0,1,2}:Finset (Fin 5))=tripleCodegree H (f 0) (f 1) (f 2) := by
      simp [upperCount,tripleCodegree,Finset.insert_subset_iff]
    rw [upperEq,xyz] at sums
    exact Fin.ext sums
  have inventory (i j : Fin 5) (ne : i≠j) : (∑T∈supers {i,j} 3,high h 1 T)≤pair b i j := by
    have bound:=high_pair_budget H f i j ne
    have eq : (∑T∈supers {i,j} 3,count H f T)=(∑T∈supers {i,j} 3,high h q T) :=
      Finset.sum_congr rfl (fun T hT=>hhigh T (Finset.mem_filter.mp hT).2.2)
    rw [eq,qone,hc i j ne] at bound
    exact bound
  obtain ⟨c,lmatch,hmatch⟩:=coverage b h inventory
  apply TwentyOneSixFive67788.propertyB_of_low_high H f c
  · intro T ht;exact (hlow T ht).trans (lmatch T ht)
  · intro T ht;rw [hhigh T ht,qone];exact hmatch T ht
end Aris4Math.ThirtyFour.TwentyOneSixFive67788Local
#print axioms Aris4Math.ThirtyFour.TwentyOneSixFive67788Local.propertyB_of_five
