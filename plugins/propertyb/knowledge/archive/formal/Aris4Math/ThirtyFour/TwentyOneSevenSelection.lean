import Aris4Math.ThirtyFour.TwentyOneSevenUnitSet
import Aris4Math.ThirtyFour.TwentyOneFiveStructure

/-! Actual degree and unit-neighbor budgets for the one- and two-seven cases.
The structural conclusions consume the actual four-lock classification. -/

namespace Aris4Math.ThirtyFour.TwentyOneSevenSelection

open scoped BigOperators

abbrev sevens := TwentyOneFiveStructure.sevens
abbrev eights := TwentyOneFiveStructure.eights

def unitEights (H : Simple5Hypergraph (Fin 21)) (x : Fin 21) : Finset (Fin 21) :=
  (eights H).filter fun y => H.codegree x y=1

theorem degree_count_budget (H : Simple5Hypergraph (Fin 21)) (size : H.edges.card=34)
    (minimum : ∀x,7≤H.degree x) : 19≤(eights H).card+2*(sevens H).card := by
  have each (x : Fin 21) : 9≤H.degree x+
      (if H.degree x=7 then 2 else 0)+(if H.degree x=8 then 1 else 0) := by
    have lower := minimum x
    split_ifs <;> omega
  have sumtwo : (∑x : Fin 21,if H.degree x=7 then 2 else 0)=2*(sevens H).card := by
    rw [←Finset.sum_filter]
    simp [sevens,TwentyOneFiveStructure.sevens,Nat.mul_comm]
  have sum := Finset.sum_le_sum (s := Finset.univ) (fun x _ => each x)
  have bound : 189≤170+2*(sevens H).card+(eights H).card := by
    simpa [Finset.sum_add_distrib,sumtwo,H.sum_degrees,size,eights,
      TwentyOneFiveStructure.eights] using sum
  omega

theorem eights_subset_erase (H : Simple5Hypergraph (Fin 21)) (x : Fin 21)
    (dx : H.degree x=7) : eights H⊆Finset.univ.erase x := by
  intro y hy
  have dy := (Finset.mem_filter.mp hy).2
  refine Finset.mem_erase.mpr ⟨?_,Finset.mem_univ _⟩
  intro eq
  rw [eq] at dy
  omega

theorem unit_eights_excess_budget (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (x : Fin 21) (dx : H.degree x=7) :
    (eights H).card≤(unitEights H x).card+
      ∑y∈eights H,(H.codegree x y-1) := by
  have each (y : Fin 21) (hy : y∈eights H) :
      1≤(if H.codegree x y=1 then 1 else 0)+(H.codegree x y-1) := by
    have yx := (Finset.mem_erase.mp (eights_subset_erase H x dx hy)).1
    have lower := H.one_le_codegree cover (Ne.symm yx)
    split_ifs <;> omega
  have sum := Finset.sum_le_sum each
  have singles : (∑y∈eights H,if H.codegree x y=1 then 1 else 0)=
      (unitEights H x).card := by
    simp only [unitEights,Finset.card_eq_sum_ones,Finset.sum_filter]
  simpa [Finset.sum_add_distrib,singles] using sum

theorem unit_eights_budget (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (x : Fin 21) (dx : H.degree x=7) :
    (eights H).card≤(unitEights H x).card+8 := by
  have bound := unit_eights_excess_budget H cover x dx
  have excess : (∑y∈eights H,(H.codegree x y-1))≤8 := by
    calc
      _ ≤ ∑y∈Finset.univ.erase x,(H.codegree x y-1) :=
        Finset.sum_le_sum_of_subset (eights_subset_erase H x dx)
      _ = 8 := by rw [H.sum_codegree_excess cover x,dx];norm_num
  omega

/-- A second seven-degree point spends its full excess outside the eight-degree
set, improving the neighbor budget by its codegree minus one. -/
theorem unit_eights_budget_with_seven (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (x y : Fin 21) (xy : x≠y)
    (dx : H.degree x=7) (dy : H.degree y=7) :
    (eights H).card+H.codegree x y≤(unitEights H x).card+9 := by
  have bound := unit_eights_excess_budget H cover x dx
  have lower := H.one_le_codegree cover xy
  have ynL : y∉eights H := by
    intro hy
    have de := (Finset.mem_filter.mp hy).2
    omega
  have sub : insert y (eights H)⊆Finset.univ.erase x :=
    Finset.insert_subset (Finset.mem_erase.mpr ⟨xy.symm,Finset.mem_univ _⟩)
      (eights_subset_erase H x dx)
  have excess : H.codegree x y-1+(∑z∈eights H,(H.codegree x z-1))≤8 := by
    calc
      _ = ∑z∈insert y (eights H),(H.codegree x z-1) :=
        (Finset.sum_insert ynL).symm
      _ ≤ ∑z∈Finset.univ.erase x,(H.codegree x z-1) :=
        Finset.sum_le_sum_of_subset sub
      _ = 8 := by rw [H.sum_codegree_excess cover x,dx];norm_num
  omega

theorem unit_eights_structure (H : Simple5Hypergraph (Fin 21))
    (cover : H.PairCovering) (size : H.edges.card=34) (noB : ¬PropertyB H)
    (x : Fin 21) (dx : H.degree x=7) (large : 3≤(unitEights H x).card) :
    (∀a∈unitEights H x,∀b∈unitEights H x,a≠b→H.codegree a b=2) ∧
    (∀e∈H.edges,x∈e→(unitEights H x∩e).card≤2) := by
  apply TwentyOneSevenUnitSet.unit_set_structure_of_not_propertyB H cover size noB x dx
    (unitEights H x) large
  · intro u hu
    exact (Finset.mem_filter.mp (Finset.mem_filter.mp hu).1).2
  · intro u hu
    exact (Finset.mem_filter.mp hu).2

theorem one_seven (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀v,7≤H.degree v) (noB : ¬PropertyB H)
    (one : (sevens H).card=1) (x : Fin 21) (dx : H.degree x=7) :
    17≤(eights H).card ∧ 9≤(unitEights H x).card ∧
    (∀a∈unitEights H x,∀b∈unitEights H x,a≠b→H.codegree a b=2) ∧
    (∀e∈H.edges,x∈e→(unitEights H x∩e).card≤2) := by
  have budget := degree_count_budget H size minimum
  have units := unit_eights_budget H cover x dx
  have large : 9≤(unitEights H x).card := by omega
  exact ⟨by omega,large,unit_eights_structure H cover size noB x dx (by omega)⟩

theorem two_sevens (H : Simple5Hypergraph (Fin 21)) (cover : H.PairCovering)
    (size : H.edges.card=34) (minimum : ∀v,7≤H.degree v) (noB : ¬PropertyB H)
    (two : (sevens H).card=2) (x y : Fin 21) (xy : x≠y)
    (dx : H.degree x=7) (dy : H.degree y=7) :
    15≤(eights H).card ∧ 7≤(unitEights H x).card ∧
    6+H.codegree x y≤(unitEights H x).card ∧
    (∀a∈unitEights H x,∀b∈unitEights H x,a≠b→H.codegree a b=2) ∧
    (∀e∈H.edges,x∈e→(unitEights H x∩e).card≤2) := by
  have budget := degree_count_budget H size minimum
  have units := unit_eights_budget_with_seven H cover x y xy dx dy
  have lower := H.one_le_codegree cover xy
  have large : 7≤(unitEights H x).card := by omega
  exact ⟨by omega,large,by omega,unit_eights_structure H cover size noB x dx (by omega)⟩

end Aris4Math.ThirtyFour.TwentyOneSevenSelection

#print axioms Aris4Math.ThirtyFour.TwentyOneSevenSelection.one_seven
#print axioms Aris4Math.ThirtyFour.TwentyOneSevenSelection.two_sevens
