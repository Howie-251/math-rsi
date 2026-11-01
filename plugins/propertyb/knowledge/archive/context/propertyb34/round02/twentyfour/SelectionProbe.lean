import Aris4Math.ThirtyFour.WeightedSubsetSelection
import Aris4Math.ThirtyFour.TwentyFourStrongCodegree
import Aris4Math.ThirtyFour.TwentyFourMatchingSelection

/-! Minimum-degree deletion proves the sparse-graph independent-set bound.
The graph is arbitrary; there is no enumeration of graphs. -/
namespace Aris4Math.ThirtyFour.TwentyFourSparseGraph
open scoped BigOperators
open WeightedSubsetSelection
variable {V : Type*} [DecidableEq V]
variable (R : V → V → Prop) [DecidableRel R]

def weight (x y : V) : ℕ := if R x y then 1 else 0
def Independent (S : Finset V) : Prop := ∀ x∈S, ∀ y∈S, ¬ R x y
def NoIndependent (S : Finset V) (k : ℕ) : Prop :=
  ¬ ∃ T⊆S, T.card=k ∧ Independent R T

theorem neighbors_card (S : Finset V) (x : V) :
    (S.filter (R x)).card=degree (weight R) S x := by
  simp [degree,weight]

theorem energy_remove (S C : Finset V) (sub : C⊆S) (d : ℕ)
    (minimum : ∀ x∈C,d≤degree (weight R) S x) :
    d*C.card+energy (weight R) (S\C)≤energy (weight R) S := by
  have parts : (∑ x∈C,degree (weight R) S x)+
      (∑ x∈S\C,degree (weight R) S x)=energy (weight R) S := by
    rw [←Finset.sum_union Finset.sdiff_disjoint.symm,Finset.union_sdiff_of_subset sub]
    rfl
  have low : d*C.card≤∑ x∈C,degree (weight R) S x := by
    calc
      _ = ∑ _x∈C,d := by simp [Nat.mul_comm]
      _ ≤ _ := Finset.sum_le_sum minimum
  have remain : energy (weight R) (S\C)≤∑ x∈S\C,degree (weight R) S x := by
    apply Finset.sum_le_sum
    intro x _
    exact Finset.sum_le_sum_of_subset Finset.sdiff_subset
  exact (Nat.add_le_add low remain).trans_eq parts

/-- If no independent (k+1)-subset exists, n²≤k(n+2e). -/
theorem no_independent_bound (symm : Symmetric R) (irrefl : Irreflexive R)
    (k : ℕ) (S : Finset V) (absent : NoIndependent R S (k+1)) :
    S.card^2≤k*(S.card+energy (weight R) S) := by
  classical
  induction k generalizing S with
  | zero =>
    have empty : S=∅ := by
      by_contra h
      obtain ⟨x,hx⟩ := Finset.nonempty_iff_ne_empty.mpr h
      apply absent
      refine ⟨{x},Finset.singleton_subset_iff.mpr hx,by simp,?_⟩
      intro a ha b hb
      have ax := Finset.mem_singleton.mp ha
      have bx := Finset.mem_singleton.mp hb
      subst a;subst b
      exact irrefl x
    simp [empty]
  | succ k ih =>
    by_cases empty : S=∅
    · simp [empty]
    obtain ⟨x,hx,minimal⟩ := Finset.exists_min_image S (degree (weight R) S)
      (Finset.nonempty_iff_ne_empty.mpr empty)
    let d := degree (weight R) S x
    let C := insert x (S.filter (R x))
    let A := S\C
    have sub : C⊆S := Finset.insert_subset hx (Finset.filter_subset _ _)
    have xnot : x∉S.filter (R x) := by simp [irrefl x]
    have ccard : C.card=d+1 := by
      simp only [C,Finset.card_insert_of_notMem xnot,neighbors_card,d]
    have cards : A.card+(d+1)=S.card := by
      simpa only [A,←ccard] using Finset.card_sdiff_add_card_eq_card sub
    have smaller : NoIndependent R A (k+1) := by
      rintro ⟨T,tSub,tCard,indep⟩
      have noNeighbor (y : V) (hy : y∈T) : y≠x ∧ ¬R x y := by
        have h := Finset.mem_sdiff.mp (tSub hy)
        have yc : y∉C := h.2
        have yn : y≠x ∧ y∉S.filter (R x) := by simpa only [C,Finset.mem_insert,not_or] using yc
        exact ⟨yn.1,fun edge=>yn.2 (Finset.mem_filter.mpr ⟨h.1,edge⟩)⟩
      have notmem : x∉T := fun h=>(noNeighbor x h).1 rfl
      apply absent
      refine ⟨insert x T,Finset.insert_subset hx (tSub.trans Finset.sdiff_subset),?_,?_⟩
      · simp [notmem,tCard,Nat.add_assoc]
      · intro a ha b hb
        by_cases ax : a=x
        · subst a
          by_cases bx : b=x
          · subst b; exact irrefl _
          · exact (noNeighbor b (Finset.mem_of_mem_insert_of_ne hb bx)).2
        · have haT : a∈T := Finset.mem_of_mem_insert_of_ne ha ax
          by_cases bx : b=x
          · subst b
            exact fun h=>(noNeighbor a haT).2 (symm h)
          · exact indep a haT b (Finset.mem_of_mem_insert_of_ne hb bx)
    have bound := ih A smaller
    have removed := energy_remove R S C sub d (fun y hy=>minimal y (sub hy))
    rw [ccard] at removed
    change d*(d+1)+energy (weight R) A≤energy (weight R) S at removed
    by_cases kz : k=0
    · subst k
      have zero : A.card=0 := by nlinarith [bound]
      rw [zero] at cards
      nlinarith
    · have kp : 0<k := Nat.pos_of_ne_zero kz
      have square : 0≤((k:ℤ)*(d+1)-(A.card:ℤ))^2 := sq_nonneg _
      have c : (S.card:ℤ)=(A.card:ℤ)+(d+1) := by exact_mod_cast cards.symm
      have rem : (d:ℤ)*(d+1)+(energy (weight R) A:ℤ)≤energy (weight R) S := by
        exact_mod_cast removed
      have b : (k:ℤ)*(A.card+(energy (weight R) A))≥(A.card:ℤ)^2 := by
        exact_mod_cast bound
      have kpz : (0:ℤ)<k := by exact_mod_cast kp
      have mulb := mul_nonneg (by omega : (0:ℤ)≤k+1) (sub_nonneg.mpr b)
      have mulrem := mul_nonneg (by positivity : (0:ℤ)≤k*(k+1)) (sub_nonneg.mpr rem)
      have desired : (S.card:ℤ)^2≤((k:ℤ)+1)*(S.card+(energy (weight R) S)) := by
        by_contra h
        have positive : 0<(k:ℤ)*((S.card:ℤ)^2-((k:ℤ)+1)*(S.card+(energy (weight R) S))) :=
          mul_pos kpz (by omega)
        rw [c] at positive
        nlinarith only [mulb,mulrem,square,positive]
      exact_mod_cast desired

end Aris4Math.ThirtyFour.TwentyFourSparseGraph
#print axioms Aris4Math.ThirtyFour.TwentyFourSparseGraph.no_independent_bound

/-! Actual five unit seven-degree locks in the no-six-degree branch. -/
namespace Aris4Math.ThirtyFour.TwentyFourNoLowSelection
open scoped BigOperators
open WeightedSubsetSelection
open Aris4Math.ThirtyThree.TwentyFourSelection (sevenVertices)
variable (H : Simple5Hypergraph (Fin 24))

def excess (x y : Fin 24) : ℕ := if x=y then 0 else H.codegree x y-1
theorem excess_symm (x y : Fin 24) : excess H x y=excess H y x := by
  simp only [excess,eq_comm,H.codegree_comm x y]
@[simp] theorem excess_self (x : Fin 24) : excess H x x=0 := by simp [excess]

theorem full_degree (cover : H.PairCovering) (x : Fin 24) :
    degree (excess H) Finset.univ x=4*H.degree x-23 := by
  have split := Finset.sum_erase_add (s:=Finset.univ) (excess H x) (Finset.mem_univ x)
  rw [excess_self,Nat.add_zero] at split
  have eq : (∑ y∈(Finset.univ : Finset (Fin 24)).erase x,excess H x y)=
      ∑ y∈(Finset.univ : Finset (Fin 24)).erase x,H.codegree x y-1 := by
    apply Finset.sum_congr rfl
    intro y hy
    simp [excess,(Finset.mem_erase.mp hy).1.symm]
  rw [eq,H.sum_codegree_excess cover x] at split
  simpa only [Fintype.card_fin,degree] using split.symm

def outside := Finset.univ\sevenVertices H

theorem outside_cards : (sevenVertices H).card+(outside H).card=24 := by
  have h := Finset.card_sdiff_add_card_eq_card (Finset.subset_univ (sevenVertices H))
  simpa [outside,Nat.add_comm] using h

theorem sum_parts (f : Fin 24→ℕ) :
    (∑x∈sevenVertices H,f x)+(∑x∈outside H,f x)=∑x,f x := by
  rw [←Finset.sum_union Finset.sdiff_disjoint.symm,
    show sevenVertices H∪outside H=Finset.univ from
      Finset.union_sdiff_of_subset (Finset.subset_univ _)]

theorem minimum_seven (cover : H.PairCovering) (none : H.sixVertices.card=0)
    (x : Fin 24) : 7≤H.degree x := by
  have low := ThirtyThree.TwentyFourSelection.minimum_degree H cover (by simp) x
  have notSix : H.degree x≠6 := by
    intro dx
    have member : x∈H.sixVertices := Finset.mem_filter.mpr ⟨Finset.mem_univ _,dx⟩
    have positive := Finset.card_pos.mpr ⟨x,member⟩
    omega
  omega

theorem outside_degree (cover : H.PairCovering) (none : H.sixVertices.card=0)
    {x : Fin 24} (hx : x∈outside H) : 8≤H.degree x := by
  have low := minimum_seven H cover none x
  have absent := (Finset.mem_sdiff.mp hx).2
  have ne : H.degree x≠7 := by simpa [sevenVertices] using absent
  omega

theorem degree_budget (size : H.edges.card=34) :
    7*(sevenVertices H).card+(∑x∈outside H,H.degree x)=170 := by
  have eq := sum_parts H H.degree
  have sevens : (∑x∈sevenVertices H,H.degree x)=7*(sevenVertices H).card := by
    calc
      _ = ∑_x∈sevenVertices H,7 := Finset.sum_congr rfl (fun x hx=>(Finset.mem_filter.mp hx).2)
      _ = _ := by simp [Nat.mul_comm]
  rw [sevens,H.sum_degrees,size] at eq
  exact eq

theorem seven_card_cases (cover : H.PairCovering) (size : H.edges.card=34)
    (none : H.sixVertices.card=0) :
    (sevenVertices H).card=22 ∨ (sevenVertices H).card=23 := by
  have bound := TwentyFourMatchingSelection.six_seven_budget H cover size
  rw [none] at bound
  have cards := outside_cards H
  have budget := degree_budget H size
  have nonzero : 0<(outside H).card := by
    by_contra h
    have zero : (outside H).card=0 := by omega
    have empty := Finset.card_eq_zero.mp zero
    simp [empty] at budget
    omega
  omega

/-- The same cross term appears in the two parts of the actual excess graph. -/
theorem excess_balance (cover : H.PairCovering) :
    energy (excess H) (sevenVertices H)+
        (∑x∈outside H,degree (excess H) Finset.univ x)=
      5*(sevenVertices H).card+energy (excess H) (outside H) := by
  let cross := ∑x∈sevenVertices H,degree (excess H) (outside H) x
  have crossSwap : (∑y∈outside H,degree (excess H) (sevenVertices H) y)=cross := by
    dsimp [degree,cross]
    rw [Finset.sum_comm]
    exact Finset.sum_congr rfl (fun x _=>Finset.sum_congr rfl (fun y _=>excess_symm H y x))
  have left : energy (excess H) (sevenVertices H)+cross=5*(sevenVertices H).card := by
    change (∑x∈sevenVertices H,degree (excess H) (sevenVertices H) x)+
      (∑x∈sevenVertices H,degree (excess H) (outside H) x)=_
    rw [←Finset.sum_add_distrib]
    calc
      _ = ∑x∈sevenVertices H,degree (excess H) Finset.univ x :=
        Finset.sum_congr rfl (fun x _=>degree_split (excess H) Finset.univ
          (sevenVertices H) (Finset.subset_univ _) x)
      _ = ∑_x∈sevenVertices H,5 := by
        apply Finset.sum_congr rfl
        intro x hx
        rw [full_degree H cover,(Finset.mem_filter.mp hx).2]
      _ = _ := by simp [Nat.mul_comm]
  have right : cross+energy (excess H) (outside H)=
      ∑x∈outside H,degree (excess H) Finset.univ x := by
    rw [←crossSwap]
    unfold energy
    rw [←Finset.sum_add_distrib]
    exact Finset.sum_congr rfl (fun x _=>degree_split (excess H) Finset.univ
      (sevenVertices H) (Finset.subset_univ _) x)
  omega

theorem energy_bounds (cover : H.PairCovering) (size : H.edges.card=34)
    (none : H.sixVertices.card=0) (noB : ¬PropertyB H) :
    ((sevenVertices H).card=22 ∧ energy (excess H) (sevenVertices H)≤98) ∨
    ((sevenVertices H).card=23 ∧ energy (excess H) (sevenVertices H)≤102) := by
  have cards := outside_cards H
  have budget := degree_budget H size
  have balance := excess_balance H cover
  rcases seven_card_cases H cover size none with n22|n23
  · left
    refine ⟨n22,?_⟩
    have two : (outside H).card=2 := by omega
    obtain ⟨a,b,ab,set⟩ := Finset.card_eq_two.mp two
    have da := outside_degree H cover none (x:=a) (by simp [set])
    have db := outside_degree H cover none (x:=b) (by simp [set])
    simp only [set,Finset.sum_pair ab,n22] at budget
    have da8 : H.degree a=8 := by omega
    have db8 : H.degree b=8 := by omega
    have small := TwentyFourStrongCodegree.codegree_le_four H size noB a b ab
      (da8.trans db8.symm) (Or.inr da8)
    have outEnergy : energy (excess H) (outside H)=2*(H.codegree a b-1) := by
      simp [set,energy,degree,excess,ab,ab.symm,H.codegree_comm b a,Nat.two_mul]
    rw [n22,outEnergy,set,Finset.sum_pair ab,full_degree H cover,full_degree H cover,
      da8,db8] at balance
    omega
  · right
    refine ⟨n23,?_⟩
    have one : (outside H).card=1 := by omega
    obtain ⟨a,set⟩ := Finset.card_eq_one.mp one
    simp only [set,Finset.sum_singleton,n23] at budget
    have da9 : H.degree a=9 := by omega
    have outEnergy : energy (excess H) (outside H)=0 := by simp [set,energy,degree]
    rw [n23,outEnergy,set,Finset.sum_singleton,full_degree H cover,da9] at balance
    omega

def bad (x y : Fin 24) : Prop := x≠y ∧ 2≤H.codegree x y
instance : DecidableRel (bad H) := fun _ _=>inferInstanceAs (Decidable (_∧_))

theorem exists_five_unit (cover : H.PairCovering) (size : H.edges.card=34)
    (none : H.sixVertices.card=0) (noB : ¬PropertyB H) :
    ∃ S⊆sevenVertices H,S.card=5 ∧ H.UnitCodegrees S := by
  have pointwise (x y : Fin 24) : TwentyFourSparseGraph.weight (bad H) x y≤excess H x y := by
    unfold TwentyFourSparseGraph.weight bad excess
    split_ifs <;> omega
  have sumBound : energy (TwentyFourSparseGraph.weight (bad H)) (sevenVertices H)≤
      energy (excess H) (sevenVertices H) := by
    apply Finset.sum_le_sum
    intro x _
    exact Finset.sum_le_sum (fun y _=>pointwise x y)
  have symm : Symmetric (bad H) := by
    intro x y h
    exact ⟨h.1.symm,by simpa only [H.codegree_comm y x] using h.2⟩
  have irrefl : Irreflexive (bad H) := fun x h=>h.1 rfl
  have existsIndependent : ¬TwentyFourSparseGraph.NoIndependent (bad H) (sevenVertices H) 5 := by
    intro absent
    have bound := TwentyFourSparseGraph.no_independent_bound (bad H) symm irrefl 4
      (sevenVertices H) absent
    rcases energy_bounds H cover size none noB with ⟨n,upper⟩|⟨n,upper⟩ <;>
      rw [n] at bound <;> omega
  obtain ⟨S,sub,card,indep⟩ := Classical.not_not.mp existsIndependent
  refine ⟨S,sub,card,?_⟩
  intro x hx y hy xy
  have low := H.one_le_codegree cover xy
  have notBad := indep x hx y hy
  change ¬(x≠y ∧ 2≤H.codegree x y) at notBad
  omega

end Aris4Math.ThirtyFour.TwentyFourNoLowSelection
#print axioms Aris4Math.ThirtyFour.TwentyFourNoLowSelection.exists_five_unit