import Aris4Math.ThirtyFour.WeightedThreePartition
import Aris4Math.ThirtyThree.TwentyFourSelection

/-! Actual eight-lock selection at 24 vertices and 34 edges. A three-class
partition of the seven-degree vertices is enlarged by the six-degree vertices
that avoid their exceptional neighbor's class. -/

namespace Aris4Math.ThirtyFour.TwentyFourMatchingSelection

open scoped BigOperators
open Aris4Math.ThirtyThree.TwentyFourSelection (sevenVertices)
open Aris4Math.ThirtyFour.WeightedThreePartition (colorWeight)

variable (H : Simple5Hypergraph (Fin 24))

/-- The new edge budget gives t + 2r ≥ 22. -/
theorem six_seven_budget (cover : H.PairCovering) (size : H.edges.card=34) :
    22 ≤ 2*H.sixVertices.card+(sevenVertices H).card := by
  have each (x : Fin 24) : 8 ≤ H.degree x+
      (if H.degree x=6 then 2 else 0)+(if H.degree x=7 then 1 else 0) := by
    have low := ThirtyThree.TwentyFourSelection.minimum_degree H cover (by simp) x
    split_ifs <;> omega
  have sum := Finset.sum_le_sum (s := Finset.univ) (fun x _ => each x)
  have sumtwo : (∑ x : Fin 24, if H.degree x=6 then 2 else 0)=2*H.sixVertices.card := by
    rw [← Finset.sum_filter]
    simp [Simple5Hypergraph.sixVertices,Nat.mul_comm]
  have bound : 192 ≤ 170+2*H.sixVertices.card+(sevenVertices H).card := by
    simpa [Finset.sum_add_distrib,sumtwo,H.sum_degrees,size,sevenVertices] using sum
  omega

/-- The loop-free excess weight restricted to actual seven-degree vertices. -/
def sevenWeight (x y : Fin 24) : ℕ :=
  if x ≠ y ∧ H.degree x=7 ∧ H.degree y=7 then H.codegree x y-1 else 0

theorem sevenWeight_symm (x y : Fin 24) : sevenWeight H x y=sevenWeight H y x := by
  simp only [sevenWeight,H.codegree_comm x y,ne_comm,and_left_comm,and_comm]

theorem sevenWeight_self (x : Fin 24) : sevenWeight H x x=0 := by simp [sevenWeight]

theorem sevenWeight_degree (cover : H.PairCovering) (x : Fin 24) :
    (∑ y : Fin 24, sevenWeight H x y) ≤ 5 := by
  by_cases dx : H.degree x=7
  · have erase := Finset.sum_erase_add (s := Finset.univ) (sevenWeight H x)
      (Finset.mem_univ x)
    rw [sevenWeight_self,Nat.add_zero] at erase
    rw [← erase]
    calc
      _ ≤ ∑ y ∈ Finset.univ.erase x, (H.codegree x y-1) := by
        apply Finset.sum_le_sum
        intro y _
        unfold sevenWeight
        split_ifs <;> omega
      _ = 5 := by rw [H.sum_codegree_excess cover x,dx]; norm_num
  · simp [sevenWeight,dx]

/-- A low vertex can use every class except its bad partners' colors. This
may exclude an unnecessary class when its partner is not seven-degree; the
two-class lower bound still holds. -/
def availableColors (color : Fin 24 → Fin 3) (x : Fin 24) : Finset (Fin 3) :=
  Finset.univ \ (H.badPartners x).image color

theorem availableColors_card (cover : H.PairCovering) (color : Fin 24 → Fin 3)
    (x : Fin 24) (dx : H.degree x=6) : 2 ≤ (availableColors H color x).card := by
  have one := H.badPartners_card_le_one_of_twenty_four cover (by simp) dx
  have image := Finset.card_image_le (s := H.badPartners x) (f := color)
  have diff := Finset.card_le_card_sdiff_add_card
    (s := (Finset.univ : Finset (Fin 3))) (t := (H.badPartners x).image color)
  change 3 ≤ (availableColors H color x).card+((H.badPartners x).image color).card at diff
  omega

def highClass (color : Fin 24 → Fin 3) (k : Fin 3) : Finset (Fin 24) :=
  (sevenVertices H).filter fun x => color x=k

def lowClass (color : Fin 24 → Fin 3) (k : Fin 3) : Finset (Fin 24) :=
  H.sixVertices.filter fun x => k ∈ availableColors H color x

def classLocks (color : Fin 24 → Fin 3) (k : Fin 3) : Finset (Fin 24) :=
  highClass H color k ∪ lowClass H color k

theorem highClass_degree (color : Fin 24 → Fin 3) (k : Fin 3)
    {x : Fin 24} (hx : x ∈ highClass H color k) : H.degree x=7 :=
  (Finset.mem_filter.mp (Finset.mem_filter.mp hx).1).2

theorem highClass_color (color : Fin 24 → Fin 3) (k : Fin 3)
    {x : Fin 24} (hx : x ∈ highClass H color k) : color x=k :=
  (Finset.mem_filter.mp hx).2

theorem lowClass_degree (color : Fin 24 → Fin 3) (k : Fin 3)
    {x : Fin 24} (hx : x ∈ lowClass H color k) : H.degree x=6 :=
  (Finset.mem_filter.mp (Finset.mem_filter.mp hx).1).2

theorem classLocks_degrees (color : Fin 24 → Fin 3) (k : Fin 3)
    {x : Fin 24} (hx : x ∈ classLocks H color k) : H.degree x=6 ∨ H.degree x=7 := by
  rcases Finset.mem_union.mp hx with high | low
  · exact Or.inr (highClass_degree H color k high)
  · exact Or.inl (lowClass_degree H color k low)

theorem classes_disjoint (color : Fin 24 → Fin 3) (k : Fin 3) :
    Disjoint (highClass H color k) (lowClass H color k) := by
  apply Finset.disjoint_left.mpr
  intro x high low
  have d7 := highClass_degree H color k high
  have d6 := lowClass_degree H color k low
  omega

theorem classLocks_mixed_unit (cover : H.PairCovering) (color : Fin 24 → Fin 3)
    (k : Fin 3) {x y : Fin 24} (hx : x ∈ lowClass H color k)
    (hy : y ∈ highClass H color k) : H.codegree x y=1 := by
  have dx := lowClass_degree H color k hx
  have dy := highClass_degree H color k hy
  have xy : x ≠ y := by intro eq; subst y; omega
  have positive := H.one_le_codegree cover xy
  have allowed := (Finset.mem_sdiff.mp (Finset.mem_filter.mp hx).2).2
  have cy := highClass_color H color k hy
  by_contra notOne
  have bad : y ∈ H.badPartners x := Finset.mem_filter.mpr
    ⟨Finset.mem_erase.mpr ⟨xy.symm,Finset.mem_univ y⟩,by omega⟩
  exact allowed (Finset.mem_image.mpr ⟨y,bad,cy⟩)

theorem sum_highClass_cards (color : Fin 24 → Fin 3) :
    (∑ k : Fin 3, (highClass H color k).card)=(sevenVertices H).card := by
  simpa [highClass] using
    Finset.sum_card_fiberwise_eq_card_filter (sevenVertices H) Finset.univ color

theorem sum_lowClass_cards (cover : H.PairCovering) (color : Fin 24 → Fin 3) :
    2*H.sixVertices.card ≤ ∑ k : Fin 3, (lowClass H color k).card := by
  have double : (∑ k : Fin 3, (lowClass H color k).card)=
      ∑ x ∈ H.sixVertices, (availableColors H color x).card := by
    simp only [lowClass,Finset.card_eq_sum_ones,Finset.sum_filter]
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro x _
    simp
  rw [double]
  calc
    _ = ∑ _x ∈ H.sixVertices, 2 := by simp [Nat.mul_comm]
    _ ≤ _ := Finset.sum_le_sum (fun x hx =>
      availableColors_card H cover color x (Finset.mem_filter.mp hx).2)

theorem exists_large_class (cover : H.PairCovering) (size : H.edges.card=34)
    (color : Fin 24 → Fin 3) : ∃ k, 8 ≤ (classLocks H color k).card := by
  have low := sum_lowClass_cards H cover color
  have high := sum_highClass_cards H color
  have budget := six_seven_budget H cover size
  have split : (∑ k : Fin 3, (classLocks H color k).card)=
      (∑ k : Fin 3, (highClass H color k).card)+
      ∑ k : Fin 3, (lowClass H color k).card := by
    calc
      _ = ∑ k : Fin 3, ((highClass H color k).card+(lowClass H color k).card) :=
        Finset.sum_congr rfl (fun k _ => Finset.card_union_of_disjoint
          (classes_disjoint H color k))
      _ = _ := Finset.sum_add_distrib
  by_contra absent
  have each (k : Fin 3) : (classLocks H color k).card ≤ 7 := by
    by_contra high
    exact absent ⟨k,by omega⟩
  have upper := Finset.sum_le_sum (s := Finset.univ) (fun k _ => each k)
  have bound : (∑ k : Fin 3, (classLocks H color k).card) ≤ 21 := by
    simpa using upper
  omega

/-- Actual excess degree at most one expresses a matching of codegree-two
pairs. The last condition excludes mixed six/seven matching edges. -/
def MatchingLocks (S : Finset (Fin 24)) : Prop :=
  (∀ x ∈ S, H.degree x=6 ∨ H.degree x=7) ∧
  (∀ x ∈ S, (∑ y ∈ S.erase x, (H.codegree x y-1)) ≤ 1) ∧
  (∀ x ∈ S, ∀ y ∈ S, H.degree x=6 → H.degree y=7 → H.codegree x y=1)

theorem classLocks_matching (cover : H.PairCovering) (color : Fin 24 → Fin 3)
    (defect : ∀ x, colorWeight (sevenWeight H) color x (color x) ≤ 1)
    (k : Fin 3) : MatchingLocks H (classLocks H color k) := by
  refine ⟨fun x hx => classLocks_degrees H color k hx,?_,?_⟩
  · intro x hx
    rcases Finset.mem_union.mp hx with hxHigh | hxLow
    · have dx := highClass_degree H color k hxHigh
      have cx := highClass_color H color k hxHigh
      calc
        _ ≤ ∑ y ∈ (classLocks H color k).erase x,
            if color y=color x then sevenWeight H x y else 0 := by
          apply Finset.sum_le_sum
          intro y hy
          obtain ⟨yx,hy⟩ := Finset.mem_erase.mp hy
          rcases Finset.mem_union.mp hy with hyHigh | hyLow
          · have dy := highClass_degree H color k hyHigh
            have cy := highClass_color H color k hyHigh
            simp [sevenWeight,yx.symm,dx,dy,cx,cy]
          · have unit := classLocks_mixed_unit H cover color k hyLow hxHigh
            rw [H.codegree_comm y x] at unit
            simp [unit]
        _ ≤ ∑ y : Fin 24, if color y=color x then sevenWeight H x y else 0 :=
          Finset.sum_le_sum_of_subset (Finset.subset_univ _)
        _ ≤ 1 := defect x
    · have dx := lowClass_degree H color k hxLow
      calc
        _ ≤ ∑ y ∈ Finset.univ.erase x, (H.codegree x y-1) :=
          Finset.sum_le_sum_of_subset (Finset.erase_subset_erase x (Finset.subset_univ _))
        _ = 1 := by rw [H.sum_codegree_excess cover x,dx]; norm_num
  · intro x hx y hy dx dy
    have hxLow : x ∈ lowClass H color k := by
      rcases Finset.mem_union.mp hx with high | low
      · have d7 := highClass_degree H color k high; omega
      · exact low
    have hyHigh : y ∈ highClass H color k := by
      rcases Finset.mem_union.mp hy with high | low
      · exact high
      · have d6 := lowClass_degree H color k low; omega
    exact classLocks_mixed_unit H cover color k hxLow hyHigh

theorem MatchingLocks.mono {S T : Finset (Fin 24)} (h : MatchingLocks H S)
    (sub : T ⊆ S) : MatchingLocks H T := by
  refine ⟨fun x hx => h.1 x (sub hx),?_,fun x hx y hy => h.2.2 x (sub hx) y (sub hy)⟩
  intro x hx
  exact (Finset.sum_le_sum_of_subset (Finset.erase_subset_erase x sub)).trans
    (h.2.1 x (sub hx))

/-- Every actual selected pair has codegree one or two. -/
theorem MatchingLocks.pair_codegree (cover : H.PairCovering)
    {S : Finset (Fin 24)} (h : MatchingLocks H S)
    {x y : Fin 24} (hx : x ∈ S) (hy : y ∈ S) (xy : x ≠ y) :
    H.codegree x y=1 ∨ H.codegree x y=2 := by
  have lower := H.one_le_codegree cover xy
  have single : H.codegree x y-1 ≤ ∑ z ∈ S.erase x, (H.codegree x z-1) :=
    Finset.single_le_sum (f := fun z => H.codegree x z-1)
      (fun z _ => Nat.zero_le _) (Finset.mem_erase.mpr ⟨xy.symm,hy⟩)
  have row := h.2.1 x hx
  omega

/-- A selected vertex has at most one selected codegree-two neighbor. -/
theorem MatchingLocks.bad_unique {S : Finset (Fin 24)} (h : MatchingLocks H S)
    {x y z : Fin 24} (hx : x ∈ S) (hy : y ∈ S) (hz : z ∈ S)
    (xy : x ≠ y) (xz : x ≠ z) (badY : H.codegree x y=2)
    (badZ : H.codegree x z=2) : y=z := by
  by_contra yz
  have sub : ({y,z} : Finset (Fin 24)) ⊆ S.erase x := by
    intro a ha
    simp only [Finset.mem_insert,Finset.mem_singleton] at ha
    rcases ha with rfl | rfl
    · exact Finset.mem_erase.mpr ⟨xy.symm,hy⟩
    · exact Finset.mem_erase.mpr ⟨xz.symm,hz⟩
  have two : (∑ a ∈ ({y,z} : Finset (Fin 24)), (H.codegree x a-1)) ≤
      ∑ a ∈ S.erase x, (H.codegree x a-1) := Finset.sum_le_sum_of_subset sub
  have notmem : y ∉ ({z} : Finset (Fin 24)) := by simpa using yz
  rw [Finset.sum_insert notmem,Finset.sum_singleton,badY,badZ] at two
  have row := h.2.1 x hx
  omega

/-- Every exceptional matching edge joins vertices in the same degree role. -/
theorem MatchingLocks.bad_same_degree {S : Finset (Fin 24)} (h : MatchingLocks H S)
    {x y : Fin 24} (hx : x ∈ S) (hy : y ∈ S) (bad : H.codegree x y=2) :
    H.degree x=H.degree y := by
  rcases h.1 x hx with dx | dx <;> rcases h.1 y hy with dy | dy
  · omega
  · have unit := h.2.2 x hx y hy dx dy
    omega
  · have unit := h.2.2 y hy x hx dy dx
    rw [H.codegree_comm y x] at unit
    omega
  · omega

/-- Eight actual distinct locks with degree six or seven; all exceptional
codegrees form a matching, with no edge crossing the two degree roles. -/
theorem exists_eight_matching_locks (cover : H.PairCovering) (size : H.edges.card=34) :
    ∃ S : Finset (Fin 24), S.card=8 ∧ MatchingLocks H S := by
  obtain ⟨color,defect⟩ := WeightedThreePartition.exists_three_part_defect_one
    (sevenWeight H) (sevenWeight_symm H) (sevenWeight_self H) (sevenWeight_degree H cover)
  obtain ⟨k,large⟩ := exists_large_class H cover size color
  obtain ⟨S,sub,card⟩ := Finset.exists_subset_card_eq large
  exact ⟨S,card,MatchingLocks.mono H (classLocks_matching H cover color defect k) sub⟩

/-- Indexed actual locks for a downstream local-type caller. -/
theorem exists_eight_matching_vertices (cover : H.PairCovering) (size : H.edges.card=34) :
    ∃ f : Fin 8 ↪ Fin 24,
      (∀ i, H.degree (f i)=6 ∨ H.degree (f i)=7) ∧
      (∀ i j, i ≠ j → H.codegree (f i) (f j)=1 ∨ H.codegree (f i) (f j)=2) ∧
      (∀ i j k, i ≠ j → i ≠ k → H.codegree (f i) (f j)=2 →
        H.codegree (f i) (f k)=2 → j=k) ∧
      (∀ i j, H.codegree (f i) (f j)=2 → H.degree (f i)=H.degree (f j)) := by
  obtain ⟨S,card,matching⟩ := exists_eight_matching_locks H cover size
  let e : ↥S ≃ Fin 8 := Fintype.equivFinOfCardEq (by simpa using card)
  let f : Fin 8 ↪ Fin 24 :=
    ⟨fun i => (e.symm i).val,Subtype.val_injective.comp e.symm.injective⟩
  have inside (i : Fin 8) : f i ∈ S := (e.symm i).property
  refine ⟨f,fun i => matching.1 (f i) (inside i),?_,?_,?_⟩
  · intro i j ij
    exact MatchingLocks.pair_codegree H cover matching (inside i) (inside j) (f.injective.ne ij)
  · intro i j k ij ik badJ badK
    exact f.injective (MatchingLocks.bad_unique H matching (inside i) (inside j) (inside k)
      (f.injective.ne ij) (f.injective.ne ik) badJ badK)
  · intro i j bad
    exact MatchingLocks.bad_same_degree H matching (inside i) (inside j) bad

end Aris4Math.ThirtyFour.TwentyFourMatchingSelection

#print axioms Aris4Math.ThirtyFour.TwentyFourMatchingSelection.exists_eight_matching_locks
#print axioms Aris4Math.ThirtyFour.TwentyFourMatchingSelection.exists_eight_matching_vertices
