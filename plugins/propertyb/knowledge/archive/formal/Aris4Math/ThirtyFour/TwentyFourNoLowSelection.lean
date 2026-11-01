import Aris4Math.ThirtyFour.TwentyFourSparseGraph
import Aris4Math.ThirtyFour.TwentyFourStrongCodegree
import Aris4Math.ThirtyFour.TwentyFourMatchingSelection

/-! Actual five unit seven-degree locks in the no-six-degree branch. -/
namespace Aris4Math.ThirtyFour.TwentyFourNoLowSelection
open scoped BigOperators
set_option maxHeartbeats 1000000
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
      ∑ y∈(Finset.univ : Finset (Fin 24)).erase x,(H.codegree x y-1) := by
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
  change (∑x∈sevenVertices H,f x)+(∑x∈Finset.univ\sevenVertices H,f x)=∑x,f x
  rw [←Finset.sum_union Finset.sdiff_disjoint.symm,
    show sevenVertices H∪(Finset.univ\sevenVertices H)=Finset.univ from
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

/-- A genuine seventh-degree point meets the five unit locks with at most
one unit of excess. The same actual five row budgets are summed. -/
theorem exists_sixth (cover : H.PairCovering) (size : H.edges.card=34)
    (none : H.sixVertices.card=0) (S : Finset (Fin 24))
    (sub : S⊆sevenVertices H) (card : S.card=5) :
    ∃ y∈sevenVertices H\S,degree (excess H) S y≤1 := by
  have many := seven_card_cases H cover size none
  have cards := Finset.card_sdiff_add_card_eq_card sub
  have lower : 17≤(sevenVertices H\S).card := by omega
  have upper : (∑y∈sevenVertices H\S,degree (excess H) S y)≤25 := by
    calc
      _ ≤ ∑y : Fin 24,degree (excess H) S y :=
        Finset.sum_le_sum_of_subset (Finset.subset_univ _)
      _ = ∑x∈S,degree (excess H) Finset.univ x := by
        simp only [degree]
        rw [Finset.sum_comm]
        exact Finset.sum_congr rfl (fun x _=>Finset.sum_congr rfl (fun y _=>excess_symm H y x))
      _ = ∑_x∈S,5 := by
        apply Finset.sum_congr rfl
        intro x hx
        rw [full_degree H cover,(Finset.mem_filter.mp (sub hx)).2]
      _ = 25 := by simp [card]
  by_contra! absent
  have each (y : Fin 24) (hy : y∈sevenVertices H\S) : 2≤degree (excess H) S y := by
    have h := absent y hy
    omega
  have sum := Finset.sum_le_sum (s:=sevenVertices H\S) each
  have low : 2*(sevenVertices H\S).card≤∑y∈sevenVertices H\S,degree (excess H) S y := by
    simpa [Nat.mul_comm] using sum
  omega

/-- Choose the exceptional old lock (an arbitrary lock if no exception
exists). Every other old lock is unit with the new actual vertex. -/
theorem exists_anchor (cover : H.PairCovering) (S : Finset (Fin 24))
    (card : S.card=5) (y : Fin 24) (outside : y∉S)
    (bound : degree (excess H) S y≤1) :
    ∃x∈S,(H.codegree x y=1 ∨ H.codegree x y=2) ∧
      ∀z∈S,z≠x→H.codegree z y=1 := by
  have pairBound (x : Fin 24) (hx : x∈S) : H.codegree x y=1 ∨ H.codegree x y=2 := by
    have xy : x≠y := by intro eq;subst x;exact outside hx
    have low := H.one_le_codegree cover xy
    have one := Finset.single_le_sum (f:=excess H y) (fun _ _=>Nat.zero_le _) hx
    have ex : excess H y x=H.codegree x y-1 := by simp [excess,xy.symm,H.codegree_comm y x]
    change excess H y x≤degree (excess H) S y at one
    rw [ex] at one
    omega
  by_cases some : ∃x∈S,H.codegree x y=2
  · obtain ⟨x,hx,bad⟩ := some
    refine ⟨x,hx,Or.inr bad,?_⟩
    intro z hz zx
    have xy : x≠y := by intro eq;subst x;exact outside hx
    have zy : z≠y := by intro eq;subst z;exact outside hz
    have pairSub : ({x,z} : Finset (Fin 24))⊆S := by simp [Finset.insert_subset_iff,Finset.singleton_subset_iff,hx,hz]
    have two := Finset.sum_le_sum_of_subset pairSub (f:=excess H y)
    change (∑a∈({x,z} : Finset (Fin 24)),excess H y a)≤degree (excess H) S y at two
    simp [excess,zx.symm,xy.symm,zy.symm,H.codegree_comm y x,H.codegree_comm y z,bad] at two
    have low := H.one_le_codegree cover zy
    omega
  · obtain ⟨x,hx⟩ := Finset.card_pos.mp (by omega : 0<S.card)
    refine ⟨x,hx,pairBound x hx,?_⟩
    intro z hz _
    rcases pairBound z hz with one|two
    · exact one
    · exact (some ⟨z,hz,two⟩).elim

/-- Six selected vertices in fixed labels, with the only possible nonunit
pair labeled {0,1}. Selection depends solely on the original hypergraph. -/
theorem exists_labeled_six (cover : H.PairCovering) (size : H.edges.card=34)
    (none : H.sixVertices.card=0) (noB : ¬PropertyB H) :
    ∃f : Fin 6↪Fin 24,∃b : Bool,(∀i,H.degree (f i)=7) ∧
      (∀i j,i≠j→H.codegree (f i) (f j)=
        if b && ({i,j} : Finset (Fin 6))=={0,1} then 2 else 1) := by
  obtain ⟨S,sub,card,unit⟩ := exists_five_unit H cover size none noB
  obtain ⟨y,hy,bound⟩ := exists_sixth H cover size none S sub card
  have yout := (Finset.mem_sdiff.mp hy).2
  obtain ⟨x,hx,pair,others⟩ := exists_anchor H cover S card y yout bound
  let A := S.erase x
  have acard : A.card=4 := by simp [A,Finset.card_erase_of_mem hx,card]
  let e : ↥A ≃ Fin 4 := Fintype.equivFinOfCardEq (by simpa using acard)
  let g : Fin 4↪Fin 24 := ⟨fun i=>(e.symm i).val,Subtype.val_injective.comp e.symm.injective⟩
  have gin (i : Fin 4) : g i∈S := Finset.mem_of_mem_erase (e.symm i).property
  have gx (i : Fin 4) : g i≠x := (Finset.mem_erase.mp (e.symm i).property).1
  have gy (i : Fin 4) : g i≠y := by intro eq;exact yout (eq ▸ gin i)
  have xy : x≠y := by intro eq;exact yout (eq ▸ hx)
  let f0 : Fin 6→Fin 24 := ![x,y,g 0,g 1,g 2,g 3]
  have distinct : ∀i j : Fin 4,i≠j→g i≠g j := fun i j h=>g.injective.ne h
  have inj : Function.Injective f0 := by
    intro i j eq
    fin_cases i <;> fin_cases j <;> simp_all [f0,Ne.symm]
  let f : Fin 6↪Fin 24 := ⟨f0,inj⟩
  let b : Bool := decide (H.codegree x y=2)
  have xdeg : H.degree x=7 := (Finset.mem_filter.mp (sub hx)).2
  have ydeg : H.degree y=7 := (Finset.mem_filter.mp (Finset.mem_sdiff.mp hy).1).2
  have gdeg (i : Fin 4) : H.degree (g i)=7 := (Finset.mem_filter.mp (sub (gin i))).2
  have xg (i : Fin 4) : H.codegree x (g i)=1 := unit x hx (g i) (gin i) (gx i).symm
  have yg (i : Fin 4) : H.codegree y (g i)=1 := (H.codegree_comm y (g i)).trans (others (g i) (gin i) (gx i))
  have gg (i j : Fin 4) (ij : i≠j) : H.codegree (g i) (g j)=1 := unit _ (gin i) _ (gin j) (g.injective.ne ij)
  refine ⟨f,b,?_,?_⟩
  · intro i
    fin_cases i <;> simp [f,f0,xdeg,ydeg,gdeg]
  · intro i j ij
    have yx := H.codegree_comm y x
    have gxUnit (i : Fin 4) := (H.codegree_comm (g i) x).trans (xg i)
    have gyUnit (i : Fin 4) := (H.codegree_comm (g i) y).trans (yg i)
    rcases pair with one|two
    · fin_cases i <;> fin_cases j <;> first
        | exact (ij rfl).elim
        | (simp [f,f0,b,one,xg,yg,gxUnit,gyUnit,gg,H.codegree_comm y x] <;> decide)
    · fin_cases i <;> fin_cases j <;> first
        | exact (ij rfl).elim
        | (simp [f,f0,b,two,xg,yg,gxUnit,gyUnit,gg,H.codegree_comm y x] <;> decide)


end Aris4Math.ThirtyFour.TwentyFourNoLowSelection
#print axioms Aris4Math.ThirtyFour.TwentyFourNoLowSelection.exists_labeled_six
