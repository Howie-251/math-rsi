import Aris4Math
import Mathlib.Data.Fintype.Powerset
import Mathlib.Data.Fintype.EquivFin
import Mathlib.Logic.Equiv.Fintype
import Mathlib.Data.Fin.VecNotation

/-!
Analytic classification of linear block families on six points.
The blocks here are actual finite subsets; no classification certificate is
assumed. Pair coverage is needed only to recover the two-element blocks.
-/

open scoped BigOperators

namespace Aris4Math.BlockClassification

variable {α : Type*} [DecidableEq α]

/-- Distinct blocks have at most one common point. -/
def Linear (blocks : Finset (Finset α)) : Prop :=
  ∀ B ∈ blocks, ∀ C ∈ blocks, B ≠ C → (B ∩ C).card ≤ 1

/-- The intersection bound and the ambient size bound control two block sizes. -/
theorem two_block_sizes (W : Finset α) (blocks : Finset (Finset α))
    (inside : ∀ B ∈ blocks, B ⊆ W) (linear : Linear blocks)
    {B C : Finset α} (hB : B ∈ blocks) (hC : C ∈ blocks) (hne : B ≠ C) :
    B.card + C.card ≤ W.card + 1 := by
  have hunion : (B ∪ C).card ≤ W.card :=
    Finset.card_le_card (Finset.union_subset (inside B hB) (inside C hC))
  have hinter := linear B hB C hC hne
  have hsum := Finset.card_union_add_card_inter B C
  omega

/-- A five-element block is the only block of size at least three. -/
theorem five_block_unique_large (W : Finset α) (blocks : Finset (Finset α))
    (six : W.card = 6) (inside : ∀ B ∈ blocks, B ⊆ W) (linear : Linear blocks)
    {B : Finset α} (hB : B ∈ blocks) (five : B.card = 5) :
    ∀ C ∈ blocks, 3 ≤ C.card → C = B := by
  intro C hC large
  by_contra hne
  have bound := two_block_sizes W blocks inside linear hC hB hne
  omega

/-- Erasing a shared point leaves disjoint residual blocks. -/
theorem erased_blocks_disjoint (blocks : Finset (Finset α)) (linear : Linear blocks)
    {x : α} {B C : Finset α} (hB : B ∈ blocks) (hC : C ∈ blocks)
    (hne : B ≠ C) (hxB : x ∈ B) (hxC : x ∈ C) :
    Disjoint (B.erase x) (C.erase x) := by
  apply Finset.disjoint_left.mpr
  intro y hyB hyC
  have hy := Finset.mem_inter.mpr
    ⟨Finset.mem_of_mem_erase hyB, Finset.mem_of_mem_erase hyC⟩
  have hx := Finset.mem_inter.mpr ⟨hxB, hxC⟩
  have eq := Finset.card_le_one.mp (linear B hB C hC hne) y hy x hx
  exact (Finset.mem_erase.mp hyB).1 eq

/-- A point belongs to at most two triples on a six-element ground set. -/
theorem triple_degree_le_two (W : Finset α) (triples : Finset (Finset α))
    (six : W.card = 6) (inside : ∀ B ∈ triples, B ⊆ W)
    (three : ∀ B ∈ triples, B.card = 3) (linear : Linear triples)
    (x : α) : (triples.filter (fun B => x ∈ B)).card ≤ 2 := by
  let star := triples.filter (fun B => x ∈ B)
  by_cases hx : x ∈ W
  · have disj : (↑star : Set (Finset α)).PairwiseDisjoint (fun B => B.erase x) := by
      intro B hB C hC hne
      exact erased_blocks_disjoint triples linear
        (Finset.mem_filter.mp hB).1 (Finset.mem_filter.mp hC).1 hne
        (Finset.mem_filter.mp hB).2 (Finset.mem_filter.mp hC).2
    have small : star.biUnion (fun B => B.erase x) ⊆ W.erase x := by
      intro y hy
      obtain ⟨B, hB, hy⟩ := Finset.mem_biUnion.mp hy
      exact Finset.mem_erase.mpr ⟨(Finset.mem_erase.mp hy).1,
        inside B (Finset.mem_filter.mp hB).1 (Finset.mem_of_mem_erase hy)⟩
    have bound := Finset.card_le_card small
    rw [Finset.card_biUnion disj] at bound
    have sum : (∑ B ∈ star, (B.erase x).card) = star.card * 2 := by
      apply Finset.sum_const_nat
      intro B hB
      have hcard := Finset.card_erase_add_one (Finset.mem_filter.mp hB).2
      have hb := three B (Finset.mem_filter.mp hB).1
      omega
    rw [sum, Finset.card_erase_of_mem hx, six] at bound
    dsimp [star] at bound
    omega
  · have empty : star = ∅ := by
      apply Finset.eq_empty_iff_forall_notMem.mpr
      intro B hB
      exact hx (inside B (Finset.mem_filter.mp hB).1 (Finset.mem_filter.mp hB).2)
    change star.card ≤ 2
    simp [empty]

/-- Count all incidences of a family with its containing ground set. -/
theorem incidence_count (W : Finset α) (blocks : Finset (Finset α))
    (inside : ∀ B ∈ blocks, B ⊆ W) :
    (∑ x ∈ W, (blocks.filter (fun B => x ∈ B)).card) =
      ∑ B ∈ blocks, B.card := by
  simp only [Finset.card_eq_sum_ones, Finset.sum_filter]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro B hB
  rw [← Finset.sum_filter]
  have filter : W.filter (fun x => x ∈ B) = B := by
    ext x
    simp only [Finset.mem_filter]
    exact ⟨fun h => h.2, fun h => ⟨inside B hB h, h⟩⟩
  rw [filter]

/-- Every linear triple family on six points has at most four blocks. -/
theorem triple_count_le_four (W : Finset α) (triples : Finset (Finset α))
    (six : W.card = 6) (inside : ∀ B ∈ triples, B ⊆ W)
    (three : ∀ B ∈ triples, B.card = 3) (linear : Linear triples) :
    triples.card ≤ 4 := by
  have count := incidence_count W triples inside
  have right : (∑ B ∈ triples, B.card) = triples.card * 3 :=
    Finset.sum_const_nat three
  have left : (∑ x ∈ W, (triples.filter (fun B => x ∈ B)).card) ≤ 12 := by
    calc
      _ ≤ ∑ _x ∈ W, 2 := Finset.sum_le_sum
        (fun x _ => triple_degree_le_two W triples six inside three linear x)
      _ = 12 := by simp [six]
  rw [right] at count
  omega

/-- Beside a four-element block, any other large block is a triple containing
both points outside the four-element block. -/
theorem large_beside_four (W : Finset α) (blocks : Finset (Finset α))
    (six : W.card = 6) (inside : ∀ B ∈ blocks, B ⊆ W) (linear : Linear blocks)
    {B C : Finset α} (hB : B ∈ blocks) (four : B.card = 4)
    (hC : C ∈ blocks) (large : 3 ≤ C.card) (hne : B ≠ C) :
    C.card = 3 ∧ W \ B ⊆ C ∧ (B ∩ C).card = 1 := by
  have bound := two_block_sizes W blocks inside linear hB hC hne
  have three : C.card = 3 := by omega
  have hi := linear C hC B hB hne.symm
  have hdiff : C \ B ⊆ W \ B := by
    intro x hx
    exact Finset.mem_sdiff.mpr
      ⟨inside C hC (Finset.mem_sdiff.mp hx).1, (Finset.mem_sdiff.mp hx).2⟩
  have hcard := Finset.card_le_card hdiff
  have outside : (W \ B).card = 2 := by
    rw [Finset.card_sdiff_of_subset (inside B hB), six, four]
  have split := Finset.card_sdiff_add_card_inter C B
  have equal : C \ B = W \ B := by
    apply Finset.eq_of_subset_of_card_le hdiff
    omega
  refine ⟨three, ?_, ?_⟩
  · rw [← equal]
    exact Finset.sdiff_subset
  · rw [Finset.inter_comm]
    omega

/-- There is at most one other large block beside a four-element block. -/
theorem four_block_at_most_one_other (W : Finset α) (blocks : Finset (Finset α))
    (six : W.card = 6) (inside : ∀ B ∈ blocks, B ⊆ W) (linear : Linear blocks)
    {B : Finset α} (hB : B ∈ blocks) (four : B.card = 4) :
    (blocks.filter (fun C => 3 ≤ C.card ∧ C ≠ B)).card ≤ 1 := by
  apply Finset.card_le_one.mpr
  intro C hC D hD
  rcases Finset.mem_filter.mp hC with ⟨hC, largeC, neC⟩
  rcases Finset.mem_filter.mp hD with ⟨hD, largeD, neD⟩
  by_contra hne
  have c := (large_beside_four W blocks six inside linear hB four hC largeC neC.symm).2.1
  have d := (large_beside_four W blocks six inside linear hB four hD largeD neD.symm).2.1
  have bound := Finset.card_le_card (Finset.subset_inter c d)
  rw [Finset.card_sdiff_of_subset (inside B hB), six, four] at bound
  have hi := linear C hC D hD hne
  omega

/-- A set contained in the union of two sets is bounded by its two intersections. -/
theorem card_le_two_intersections (B C D : Finset α) (inside : D ⊆ B ∪ C) :
    D.card ≤ (D ∩ B).card + (D ∩ C).card := by
  have cover : D = (D ∩ B) ∪ (D ∩ C) := by
    ext x
    simp only [Finset.mem_union, Finset.mem_inter]
    constructor
    · intro hx
      rcases Finset.mem_union.mp (inside hx) with hb | hc
      · exact Or.inl ⟨hx, hb⟩
      · exact Or.inr ⟨hx, hc⟩
    · rintro (h | h) <;> exact h.1
  calc
    D.card = ((D ∩ B) ∪ (D ∩ C)).card := congrArg Finset.card cover
    _ ≤ _ := Finset.card_union_le _ _

/-- Two disjoint triples fill the six-point set and exclude every third triple. -/
theorem disjoint_triples_only (W : Finset α) (triples : Finset (Finset α))
    (six : W.card = 6) (inside : ∀ B ∈ triples, B ⊆ W)
    (three : ∀ B ∈ triples, B.card = 3) (linear : Linear triples)
    {B C : Finset α} (hB : B ∈ triples) (hC : C ∈ triples) (disj : Disjoint B C) :
    triples = {B, C} := by
  have cover : B ∪ C = W := by
    apply Finset.eq_of_subset_of_card_le (Finset.union_subset (inside B hB) (inside C hC))
    rw [Finset.card_union_of_disjoint disj, three B hB, three C hC, six]
  ext D
  constructor
  · intro hD
    by_cases dB : D = B
    · simp [dB]
    by_cases dC : D = C
    · simp [dC]
    have hd := card_le_two_intersections B C D (cover.symm ▸ inside D hD)
    have db := linear D hD B hB dB
    have dc := linear D hD C hC dC
    have size := three D hD
    omega
  · intro hD
    simp only [Finset.mem_insert, Finset.mem_singleton] at hD
    rcases hD with rfl | rfl <;> assumption

/-- Three or more triples must meet pairwise in exactly one point. -/
theorem triple_intersection_eq_one (W : Finset α) (triples : Finset (Finset α))
    (six : W.card = 6) (inside : ∀ B ∈ triples, B ⊆ W)
    (three : ∀ B ∈ triples, B.card = 3) (linear : Linear triples)
    (many : 3 ≤ triples.card) {B C : Finset α}
    (hB : B ∈ triples) (hC : C ∈ triples) (hne : B ≠ C) : (B ∩ C).card = 1 := by
  have upper := linear B hB C hC hne
  have positive : (B ∩ C).Nonempty := by
    by_contra h
    have disj : Disjoint B C := Finset.disjoint_iff_inter_eq_empty.mpr
      (Finset.not_nonempty_iff_eq_empty.mp h)
    have only := disjoint_triples_only W triples six inside three linear hB hC disj
    have bound : triples.card ≤ 2 := only ▸ Finset.card_le_two
    omega
  have lower := Finset.card_pos.mpr positive
  omega

section IncidenceIsomorphism

variable {β ι : Type*} [Fintype α] [Fintype β] [DecidableEq β]
  [Fintype ι] [DecidableEq ι]

omit [DecidableEq α] [DecidableEq β] in
/-- The finite incidence transform is injective: counts of all upper fibers
determine counts of exact fibers. The proof is downward induction on subsets. -/
theorem exact_fibers_of_upper_fibers (f : α → Finset ι) (g : β → Finset ι)
    (upper : ∀ S, (Finset.univ.filter (fun x => S ⊆ f x)).card =
      (Finset.univ.filter (fun y => S ⊆ g y)).card) :
    ∀ S, (Finset.univ.filter (fun x => f x = S)).card =
      (Finset.univ.filter (fun y => g y = S)).card := by
  intro S
  generalize hn : Fintype.card ι - S.card = n
  induction n using Nat.strong_induction_on generalizing S with
  | h n ih =>
    let above := (Finset.univ : Finset (Finset ι)).filter (fun T => S ⊆ T)
    have self : S ∈ above := by simp [above]
    have sumf := Finset.sum_card_fiberwise_eq_card_filter Finset.univ above f
    have sumg := Finset.sum_card_fiberwise_eq_card_filter Finset.univ above g
    have sum_eq : (∑ T ∈ above, (Finset.univ.filter (fun x => f x = T)).card) =
        ∑ T ∈ above, (Finset.univ.filter (fun y => g y = T)).card := by
      rw [sumf, sumg]
      simpa [above] using upper S
    have proper : (∑ T ∈ above.erase S, (Finset.univ.filter (fun x => f x = T)).card) =
        ∑ T ∈ above.erase S, (Finset.univ.filter (fun y => g y = T)).card := by
      apply Finset.sum_congr rfl
      intro T hT
      obtain ⟨hne, hT⟩ := Finset.mem_erase.mp hT
      have sub : S ⊆ T := (Finset.mem_filter.mp hT).2
      have lt : S.card < T.card := Finset.card_lt_card (Finset.ssubset_iff_subset_ne.mpr ⟨sub, Ne.symm hne⟩)
      have le : T.card ≤ Fintype.card ι := Finset.card_le_univ _
      exact ih (Fintype.card ι - T.card) (by omega) T rfl
    rw [← Finset.sum_erase_add above _ self, ← Finset.sum_erase_add above _ self,
      proper] at sum_eq
    omega

omit [DecidableEq α] [DecidableEq β] in
/-- Equal incidence fibers produce a genuine vertex bijection preserving every
indexed block. This is the semantic bridge from counts to labeling. -/
theorem exists_equiv_of_upper_fibers (f : α → Finset ι) (g : β → Finset ι)
    (upper : ∀ S, (Finset.univ.filter (fun x => S ⊆ f x)).card =
      (Finset.univ.filter (fun y => S ⊆ g y)).card) :
    ∃ e : α ≃ β, ∀ x, g (e x) = f x := by
  classical
  have fiber : ∀ S, Fintype.card {x // f x = S} = Fintype.card {y // g y = S} := by
    intro S
    simpa only [Fintype.card_subtype] using exact_fibers_of_upper_fibers f g upper S
  let equiv := fun S => Fintype.equivOfCardEq (fiber S)
  exact ⟨Equiv.ofFiberEquiv equiv, Equiv.ofFiberEquiv_map equiv⟩

omit [DecidableEq α] [DecidableEq β] in
/-- When each point lies in at most two indexed blocks, ground-set size,
block sizes, and pairwise intersection sizes determine the entire incidence
structure up to a bijection. No listing of set families is involved. -/
theorem exists_equiv_of_incidence_data (f : α → Finset ι) (g : β → Finset ι)
    (smallf : ∀ x, (f x).card ≤ 2) (smallg : ∀ y, (g y).card ≤ 2)
    (total : Fintype.card α = Fintype.card β)
    (single : ∀ i, (Finset.univ.filter (fun x => i ∈ f x)).card =
      (Finset.univ.filter (fun y => i ∈ g y)).card)
    (pairs : ∀ i j, i ≠ j →
      (Finset.univ.filter (fun x => i ∈ f x ∧ j ∈ f x)).card =
      (Finset.univ.filter (fun y => i ∈ g y ∧ j ∈ g y)).card) :
    ∃ e : α ≃ β, ∀ x, g (e x) = f x := by
  apply exists_equiv_of_upper_fibers f g
  intro S
  by_cases empty : S.card = 0
  · have eq := Finset.card_eq_zero.mp empty
    simpa [eq] using total
  by_cases one : S.card = 1
  · obtain ⟨i, rfl⟩ := Finset.card_eq_one.mp one
    simpa using single i
  by_cases two : S.card = 2
  · obtain ⟨i, j, hne, rfl⟩ := Finset.card_eq_two.mp two
    simpa only [Finset.insert_subset_iff, Finset.singleton_subset_iff] using pairs i j hne
  have large : 3 ≤ S.card := by omega
  have ef : (Finset.univ.filter (fun x => S ⊆ f x)) = ∅ := by
    apply Finset.eq_empty_iff_forall_notMem.mpr
    intro x hx
    have hc := Finset.card_le_card (Finset.mem_filter.mp hx).2
    have hs := smallf x
    omega
  have eg : (Finset.univ.filter (fun y => S ⊆ g y)) = ∅ := by
    apply Finset.eq_empty_iff_forall_notMem.mpr
    intro y hy
    have hc := Finset.card_le_card (Finset.mem_filter.mp hy).2
    have hs := smallg y
    omega
  simp [ef, eg]

/-- The set of indexed blocks containing a vertex. -/
def signature (B : ι → Finset α) (x : α) : Finset ι :=
  Finset.univ.filter (fun i => x ∈ B i)

omit [Fintype α] [DecidableEq ι] in
@[simp] theorem mem_signature (B : ι → Finset α) (x : α) (i : ι) :
    i ∈ signature B x ↔ x ∈ B i := by simp [signature]

/-- Indexed block systems with the same incidence data are related by an
actual vertex equivalence that maps each block to its corresponding block. -/
theorem exists_equiv_map_blocks (B : ι → Finset α) (C : ι → Finset β)
    (smallB : ∀ x, (signature B x).card ≤ 2)
    (smallC : ∀ y, (signature C y).card ≤ 2)
    (total : Fintype.card α = Fintype.card β)
    (single : ∀ i, (B i).card = (C i).card)
    (pairs : ∀ i j, i ≠ j → (B i ∩ B j).card = (C i ∩ C j).card) :
    ∃ e : α ≃ β, ∀ i, (B i).map e.toEmbedding = C i := by
  have hs (i : ι) : (Finset.univ.filter (fun x => i ∈ signature B x)).card =
      (Finset.univ.filter (fun y => i ∈ signature C y)).card := by
    simpa only [mem_signature, Finset.filter_mem_eq_inter, Finset.univ_inter] using single i
  have hp (i j : ι) (hne : i ≠ j) :
      (Finset.univ.filter (fun x => i ∈ signature B x ∧ j ∈ signature B x)).card =
      (Finset.univ.filter (fun y => i ∈ signature C y ∧ j ∈ signature C y)).card := by
    have hf (D : ι → Finset α) :
        Finset.univ.filter (fun x => i ∈ signature D x ∧ j ∈ signature D x) = D i ∩ D j := by
      ext x
      simp
    have hg : Finset.univ.filter (fun y => i ∈ signature C y ∧ j ∈ signature C y) = C i ∩ C j := by
      ext y
      simp
    rw [hf, hg]
    exact pairs i j hne
  obtain ⟨e, he⟩ := exists_equiv_of_incidence_data (signature B) (signature C)
    smallB smallC total hs hp
  refine ⟨e, ?_⟩
  intro i
  ext y
  constructor
  · intro hy
    obtain ⟨x, hx, rfl⟩ := Finset.mem_map.mp hy
    have hsig : i ∈ signature C (e x) := (he x).symm ▸ (mem_signature B x i).mpr hx
    exact (mem_signature C _ i).mp hsig
  · intro hy
    refine Finset.mem_map.mpr ⟨e.symm y, ?_, e.apply_symm_apply y⟩
    have hsig : i ∈ signature C (e (e.symm y)) := by simpa using hy
    exact (mem_signature B _ i).mp (he (e.symm y) ▸ hsig)

omit [Fintype α] [DecidableEq ι] in
/-- The signature cardinal is the actual incidence count in an injectively
indexed family, including points outside all blocks. -/
theorem signature_card_eq (B : ι → Finset α) (injective : Function.Injective B)
    (x : α) :
    (signature B x).card =
      ((Finset.univ.image B).filter (fun D => x ∈ D)).card := by
  rw [Finset.filter_image]
  exact (Finset.card_image_of_injective _ injective).symm

end IncidenceIsomorphism

end Aris4Math.BlockClassification

#print axioms Aris4Math.BlockClassification.five_block_unique_large
#print axioms Aris4Math.BlockClassification.triple_degree_le_two
#print axioms Aris4Math.BlockClassification.triple_count_le_four
#print axioms Aris4Math.BlockClassification.four_block_at_most_one_other
#print axioms Aris4Math.BlockClassification.disjoint_triples_only
#print axioms Aris4Math.BlockClassification.triple_intersection_eq_one
#print axioms Aris4Math.BlockClassification.exact_fibers_of_upper_fibers
#print axioms Aris4Math.BlockClassification.exists_equiv_of_incidence_data
#print axioms Aris4Math.BlockClassification.exists_equiv_map_blocks
