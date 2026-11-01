import Aris4Math.ThirtyFour.TwentyOneSevenSelection
import Aris4Math.ThirtyFour.Incidence
import Aris4Math.ThirtyThree.MultiLockRecovery
import Aris4Math.ThirtyFour.LockExtension
import Aris4Math.ThirtyFour.LockRelabel

/-! Actual six-lock selection in the unique-seven branch. Two real root
edges provide two disjoint pairs; a fifth unit neighbor supplies a third edge. -/

namespace Aris4Math.ThirtyFour.TwentyOneSevenOneSelection

open scoped BigOperators
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.MultiLockRecovery

def rootCount (T : Finset (Fin 6)) : ℕ :=
  if T={0} then 4 else if T={0,1,2} ∨ T={0,3,4} ∨ T={0,5} then 1 else 0

def pair (i j : Fin 6) : ℕ := if i=0 ∨ j=0 then 1 else 2

theorem root_counts_of_edges (H : Simple5Hypergraph (Fin 21)) (f : Fin 6↪Fin 21)
    (degree : H.degree (f 0)=7) (units : ∀j,j≠0→H.codegree (f 0) (f j)=1)
    (e g h : Finset (Fin 21)) (he : e∈H.edges) (hg : g∈H.edges) (hh : h∈H.edges)
    (se : lockSignature f e={0,1,2}) (sg : lockSignature f g={0,3,4})
    (sh : lockSignature f h={0,5}) :
    ∀T,0∈T→count H f T=rootCount T := by
  have exact_one (T : Finset (Fin 6)) (j : Fin 6) (j0 : j≠0)
      (zero : 0∈T) (hj : j∈T) (a : Finset (Fin 21)) (ha : a∈H.edges)
      (sig : lockSignature f a=T) : count H f T=1 := by
    have lower : 1≤count H f T := Finset.one_le_card.mpr ⟨a,Finset.mem_filter.mpr ⟨ha,sig⟩⟩
    have upper := count_le_codegree H f T 0 j zero hj
    rw [units j j0] at upper
    omega
  have anchor (j : Fin 6) (j0 : j≠0) : ∃a∈H.edges,
      f 0∈a ∧ f j∈a ∧
      (lockSignature f a={0,1,2} ∨ lockSignature f a={0,3,4} ∨ lockSignature f a={0,5}) := by
    fin_cases j
    · exact (j0 rfl).elim
    · refine ⟨e,he,?_,?_,Or.inl se⟩ <;> rw [←mem_lockSignature,se] <;> decide
    · refine ⟨e,he,?_,?_,Or.inl se⟩ <;> rw [←mem_lockSignature,se] <;> decide
    · refine ⟨g,hg,?_,?_,Or.inr (Or.inl sg)⟩ <;> rw [←mem_lockSignature,sg] <;> decide
    · refine ⟨g,hg,?_,?_,Or.inr (Or.inl sg)⟩ <;> rw [←mem_lockSignature,sg] <;> decide
    · refine ⟨h,hh,?_,?_,Or.inr (Or.inr sh)⟩ <;> rw [←mem_lockSignature,sh] <;> decide
  have largeCounts (T : Finset (Fin 6)) (zero : 0∈T) (large : 2≤T.card) :
      count H f T=(if T={0,1,2} ∨ T={0,3,4} ∨ T={0,5} then 1 else 0) := by
    by_cases a : T={0,1,2}
    · subst T
      simpa using exact_one _ 1 (by decide) (by decide) (by decide) e he se
    by_cases b : T={0,3,4}
    · subst T
      simpa using exact_one _ 3 (by decide) (by decide) (by decide) g hg sg
    by_cases c : T={0,5}
    · subst T
      simpa using exact_one _ 5 (by decide) (by decide) (by decide) h hh sh
    rw [if_neg (not_or.mpr ⟨a,not_or.mpr ⟨b,c⟩⟩)]
    apply Finset.card_eq_zero.mpr
    apply Finset.eq_empty_iff_forall_notMem.mpr
    intro z hz
    obtain ⟨hz,sig⟩ := Finset.mem_filter.mp hz
    obtain ⟨j,hj,j0⟩ := Finset.exists_mem_ne (by omega : 1<T.card) 0
    obtain ⟨v,hv,root,tail,shape⟩ := anchor j j0
    have rootZ : f 0∈z := (mem_lockSignature f z 0).mp (sig.symm ▸ zero)
    have tailZ : f j∈z := (mem_lockSignature f z j).mp (sig.symm ▸ hj)
    have zv := H.edge_unique_of_codegree_one (units j j0) hz hv rootZ tailZ root tail
    have sv : lockSignature f v=T := zv ▸ sig
    rcases shape with sa | sb | sc
    · exact a (sv.symm.trans sa)
    · exact b (sv.symm.trans sb)
    · exact c (sv.symm.trans sc)
  have sum : (∑T∈supers ({0} : Finset (Fin 6)) 2,count H f T)=3 := by
    calc
      _ = ∑T∈supers ({0} : Finset (Fin 6)) 2,
          if T={0,1,2} ∨ T={0,3,4} ∨ T={0,5} then 1 else 0 := by
        apply Finset.sum_congr rfl
        intro T ht
        obtain ⟨sub,large⟩ := (Finset.mem_filter.mp ht).2
        exact largeCounts T (sub (by simp)) large
      _ = 3 := by decide +kernel
  have singleton : count H f {0}=4 := by
    have total := count_add_larger H f {0}
    simp only [Finset.card_singleton,Nat.reduceAdd,upper_singleton,degree] at total
    rw [sum] at total
    omega
  intro T zero
  by_cases one : T={0}
  · subst T
    simpa [rootCount] using singleton
  · have large : 2≤T.card := by
      by_contra small
      have sub : ({0} : Finset (Fin 6))⊆T := Finset.singleton_subset_iff.mpr zero
      exact one (Finset.eq_of_subset_of_card_le sub (by simpa using (show T.card≤1 by omega))).symm
    simpa only [rootCount,if_neg one] using largeCounts T zero large

theorem two_double_edges (H : Simple5Hypergraph (Fin 21)) (x : Fin 21)
    (dx : H.degree x=7) (U : Finset (Fin 21)) (large : 9≤U.card)
    (units : ∀u∈U,H.codegree x u=1)
    (capacity : ∀e∈H.edges,x∈e→(U∩e).card≤2) :
    ∃e∈H.edges,∃g∈H.edges,e≠g ∧ x∈e ∧ x∈g ∧ (U∩e).card=2 ∧ (U∩g).card=2 := by
  let E := H.edges.filter fun e => x∈e
  let D := E.filter fun e => (U∩e).card=2
  have each (e : Finset (Fin 21)) (he : e∈E) :
      (U∩e).card≤1+(if (U∩e).card=2 then 1 else 0) := by
    obtain ⟨he,xe⟩ := Finset.mem_filter.mp he
    have cap := capacity e he xe
    split_ifs <;> omega
  have total := Incidence.sum_codegrees_subset H x U
  have unitSum : (∑u∈U,H.codegree x u)=U.card := by
    calc
      _ = ∑_u∈U,(1 : ℕ) := Finset.sum_congr rfl units
      _ = _ := by simp
  rw [unitSum] at total
  have sum := Finset.sum_le_sum each
  have bound : U.card≤7+D.card := by
    have doubles : (∑e∈E,if (U∩e).card=2 then 1 else 0)=D.card := by
      simp only [D,Finset.card_eq_sum_ones,Finset.sum_filter]
    have ecard : E.card=7 := dx
    calc
      U.card = ∑e∈E,(U∩e).card := total
      _ ≤ ∑e∈E,(1+(if (U∩e).card=2 then 1 else 0)) := sum
      _ = 7+D.card := by rw [Finset.sum_add_distrib,doubles];simp [ecard]
  obtain ⟨e,he,g,hg,eg⟩ := Finset.one_lt_card.mp (show 1<D.card by omega)
  obtain ⟨he,ec⟩ := Finset.mem_filter.mp he
  obtain ⟨hg,gc⟩ := Finset.mem_filter.mp hg
  obtain ⟨he,xe⟩ := Finset.mem_filter.mp he
  obtain ⟨hg,xg⟩ := Finset.mem_filter.mp hg
  exact ⟨e,he,g,hg,eg,xe,xg,ec,gc⟩

theorem exists_locks_from_unit_set (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (x : Fin 21) (dx : H.degree x=7) (U : Finset (Fin 21)) (large : 9≤U.card)
    (degrees : ∀u∈U,H.degree u=8) (units : ∀u∈U,H.codegree x u=1)
    (pairs : ∀a∈U,∀b∈U,a≠b→H.codegree a b=2)
    (capacity : ∀e∈H.edges,x∈e→(U∩e).card≤2) :
    ∃f : Fin 6↪Fin 21,f 0=x ∧
      (∀i,H.degree (f i)=if i=0 then 7 else 8) ∧
      (∀i j,i≠j→H.codegree (f i) (f j)=pair i j) ∧
      (∀T,0∈T→count H f T=rootCount T) := by
  obtain ⟨e,he,g,hg,eg,xe,xg,ec,gc⟩ := two_double_edges H x dx U large units capacity
  obtain ⟨a,b,ab,pe⟩ := Finset.card_eq_two.mp ec
  obtain ⟨c,d,cd,pg⟩ := Finset.card_eq_two.mp gc
  obtain ⟨ha,ae⟩ := Finset.mem_inter.mp (show a∈U∩e by rw [pe];simp)
  obtain ⟨hb,be⟩ := Finset.mem_inter.mp (show b∈U∩e by rw [pe];simp)
  obtain ⟨hc,cg⟩ := Finset.mem_inter.mp (show c∈U∩g by rw [pg];simp)
  obtain ⟨hd,dg⟩ := Finset.mem_inter.mp (show d∈U∩g by rw [pg];simp)
  have notG (u : Fin 21) (hu : u∈U) (ue : u∈e) : u∉g := by
    intro ug
    exact eg (H.edge_unique_of_codegree_one (units u hu) he hg xe ue xg ug)
  have notE (u : Fin 21) (hu : u∈U) (ug : u∈g) : u∉e := by
    intro ue
    exact eg (H.edge_unique_of_codegree_one (units u hu) he hg xe ue xg ug)
  have ag := notG a ha ae
  have bg := notG b hb be
  have ce := notE c hc cg
  have de := notE d hd dg
  have ac : a≠c := fun eq => ce (eq ▸ ae)
  have ad : a≠d := fun eq => de (eq ▸ ae)
  have bc : b≠c := fun eq => ce (eq ▸ be)
  have bd : b≠d := fun eq => de (eq ▸ be)
  have small : ((U∩e)∪(U∩g)).card<U.card := by
    have bound := Finset.card_union_le (U∩e) (U∩g)
    omega
  obtain ⟨w,hw,notOld⟩ := Finset.exists_mem_notMem_of_card_lt_card small
  have we : w∉e := fun h => notOld (Finset.mem_union_left _ (Finset.mem_inter.mpr ⟨hw,h⟩))
  have wg : w∉g := fun h => notOld (Finset.mem_union_right _ (Finset.mem_inter.mpr ⟨hw,h⟩))
  have aw : a≠w := fun eq => we (eq ▸ ae)
  have bw : b≠w := fun eq => we (eq ▸ be)
  have cw : c≠w := fun eq => wg (eq ▸ cg)
  have dw : d≠w := fun eq => wg (eq ▸ dg)
  have apart (u : Fin 21) (hu : u∈U) : x≠u := by
    intro eq
    have du := degrees u hu
    rw [eq] at dx
    omega
  have xa := apart a ha
  have xb := apart b hb
  have xc := apart c hc
  have xd := apart d hd
  have xw := apart w hw
  obtain ⟨h,hh,xh,wh⟩ := cover x w xw
  have hne : h≠e := fun eq => we (eq ▸ wh)
  have hng : h≠g := fun eq => wg (eq ▸ wh)
  have ah : a∉h := fun ah => hne
    (H.edge_unique_of_codegree_one (units a ha) hh he xh ah xe ae)
  have bh : b∉h := fun bh => hne
    (H.edge_unique_of_codegree_one (units b hb) hh he xh bh xe be)
  have ch : c∉h := fun ch => hng
    (H.edge_unique_of_codegree_one (units c hc) hh hg xh ch xg cg)
  have dh : d∉h := fun dh => hng
    (H.edge_unique_of_codegree_one (units d hd) hh hg xh dh xg dg)
  let f : Fin 6↪Fin 21 := ⟨![x,a,b,c,d,w],by
    intro i j eq
    fin_cases i <;> fin_cases j <;>
      simp [xa,xb,xc,xd,xw,ab,ac,ad,aw,bc,bd,bw,cd,cw,dw,
        Ne.symm xa,Ne.symm xb,Ne.symm xc,Ne.symm xd,Ne.symm xw,
        Ne.symm ab,Ne.symm ac,Ne.symm ad,Ne.symm aw,Ne.symm bc,
        Ne.symm bd,Ne.symm bw,Ne.symm cd,Ne.symm cw,Ne.symm dw] at eq ⊢⟩
  have inside (i : Fin 6) (ne : i≠0) : f i∈U := by
    fin_cases i <;> simp +decide [f] at ne ⊢ <;> assumption
  have funit (i : Fin 6) (ne : i≠0) : H.codegree (f 0) (f i)=1 := units _ (inside i ne)
  have se : lockSignature f e={0,1,2} := by
    ext i;fin_cases i <;> simp [f,xe,ae,be,ce,de,we]
  have sg : lockSignature f g={0,3,4} := by
    ext i;fin_cases i <;> simp [f,xg,ag,bg,cg,dg,wg]
  have sh : lockSignature f h={0,5} := by
    ext i;fin_cases i <;> simp [f,xh,ah,bh,ch,dh,wh]
  refine ⟨f,rfl,?_,?_,root_counts_of_edges H f dx funit e g h he hg hh se sg sh⟩
  · intro i
    by_cases eq : i=0
    · subst i
      simpa [f] using dx
    · rw [if_neg eq]
      exact degrees _ (inside i eq)
  · intro i j ne
    by_cases iz : i=0
    · subst i
      simpa [pair] using funit j (Ne.symm ne)
    by_cases jz : j=0
    · subst j
      rw [H.codegree_comm]
      simpa [pair] using funit i ne
    · simp only [pair,if_neg (not_or.mpr ⟨iz,jz⟩)]
      exact pairs _ (inside i iz) _ (inside j jz) (f.injective.ne ne)

/-- No selected-set or local-profile premise remains in this actual caller. -/
theorem exists_locks (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀v,7≤H.degree v) (noB : ¬PropertyB H)
    (one : (TwentyOneSevenSelection.sevens H).card=1) (x : Fin 21) (dx : H.degree x=7) :
    ∃f : Fin 6↪Fin 21,f 0=x ∧
      (∀i,H.degree (f i)=if i=0 then 7 else 8) ∧
      (∀i j,i≠j→H.codegree (f i) (f j)=pair i j) ∧
      (∀T,0∈T→count H f T=rootCount T) := by
  obtain ⟨_,large,pairs,capacity⟩ := TwentyOneSevenSelection.one_seven H cover size minimum noB one x dx
  apply exists_locks_from_unit_set H cover x dx (TwentyOneSevenSelection.unitEights H x)
    large ?_ ?_ pairs capacity
  · intro u hu
    exact (Finset.mem_filter.mp (Finset.mem_filter.mp hu).1).2
  · intro u hu
    exact (Finset.mem_filter.mp hu).2

def rootLast : Equiv.Perm (Fin 6) where
  toFun := ![1,2,3,4,5,0]
  invFun := ![5,0,1,2,3,4]
  left_inv := by decide +kernel
  right_inv := by decide +kernel

theorem rootLast_zero : ∀i,rootLast i=0 ↔ i=5 := by decide +kernel

theorem zero_mem_promoted : ∀T : Finset (Fin 5),
    0∈(LockExtension.promoted T).map rootLast.toEmbedding := by decide +kernel

theorem rotated_root_count : ∀T : Finset (Fin 5),
    rootCount ((LockExtension.promoted T).map rootLast.toEmbedding)=
      if T=∅ then 4 else if T={0,1} ∨ T={2,3} ∨ T={4} then 1 else 0 := by decide +kernel

/-- The same actual locks with the degree-seven root last, so the old five
eight-degree locks and their promotion vector can be used directly. -/
theorem exists_last_locks (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀v,7≤H.degree v) (noB : ¬PropertyB H)
    (one : (TwentyOneSevenSelection.sevens H).card=1) (x : Fin 21) (dx : H.degree x=7) :
    ∃g : Fin 6↪Fin 21,
      (∀i,H.degree (g i)=if i=5 then 7 else 8) ∧
      (∀i j,i≠j→H.codegree (g i) (g j)=if i=5 ∨ j=5 then 1 else 2) ∧
      (∀T : Finset (Fin 5),LockExtension.promotion H g T=
        if T=∅ then 4 else if T={0,1} ∨ T={2,3} ∨ T={4} then 1 else 0) := by
  obtain ⟨f,_,degrees,pairs,counts⟩ := exists_locks H cover size minimum noB one x dx
  let g := rootLast.toEmbedding.trans f
  refine ⟨g,?_,?_,?_⟩
  · intro i
    change H.degree (f (rootLast i))=_
    rw [degrees]
    simp only [rootLast_zero]
  · intro i j ne
    change H.codegree (f (rootLast i)) (f (rootLast j))=_
    rw [pairs _ _ (rootLast.injective.ne ne)]
    simp only [pair,rootLast_zero]
  · intro T
    change count H (rootLast.toEmbedding.trans f) (LockExtension.promoted T)=_
    rw [LockRelabel.count_comp_perm,counts _ (zero_mem_promoted T)]
    exact rotated_root_count T

end Aris4Math.ThirtyFour.TwentyOneSevenOneSelection

#print axioms Aris4Math.ThirtyFour.TwentyOneSevenOneSelection.exists_locks
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenOneSelection.exists_last_locks
