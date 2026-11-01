import Aris4Math.BlockClassification
import Aris4Math.Avoidance

/-!
Explicit six-point labels, obtained from analytic incidence data.
The only closed finite checks concern the displayed reference configurations.
-/

namespace Aris4Math.K6Classification

open BlockClassification

variable {α : Type*} [DecidableEq α] [Fintype α]

/-- The paper's nine large-block representatives, with labels shifted from
1,...,6 to 0,...,5. Two-element blocks are recovered separately. -/
def representative (k : Fin 9) : Finset (Finset (Fin 6)) :=
  match k.val with
  | 0 => ∅
  | 1 => {{0, 1, 2}}
  | 2 => {{0, 3, 4}, {1, 2, 3}}
  | 3 => {{0, 4, 5}, {1, 2, 3}}
  | 4 => {{0, 3, 4}, {1, 2, 3}, {1, 4, 5}}
  | 5 => {{0, 1, 3}, {0, 4, 5}, {1, 2, 4}, {2, 3, 5}}
  | 6 => {{0, 1, 2, 5}}
  | 7 => {{0, 3, 4, 5}, {1, 2, 3}}
  | _ => {{0, 1, 2, 3, 5}}

def largeBlocks (blocks : Finset (Finset α)) : Finset (Finset α) :=
  blocks.filter (fun B => 3 ≤ B.card)

/-- Complete a large-block family by all pairs that no large block covers. -/
def pairCompletion (large : Finset (Finset α)) : Finset (Finset α) :=
  large ∪ ((Finset.univ.powersetCard 2).filter (fun P => ∀ B ∈ large, ¬ P ⊆ B))

/-- The full block representative, including all uniquely determined pairs. -/
def fullRepresentative (k : Fin 9) : Finset (Finset (Fin 6)) :=
  pairCompletion (representative k)

/-- Pair coverage and linearity uniquely recover every two-element block from
the large blocks. This does not enumerate complete graph decompositions. -/
theorem recover_pairs (blocks : Finset (Finset α))
    (lower : ∀ B ∈ blocks, 2 ≤ B.card) (linear : Linear blocks)
    (covers : ∀ P : Finset α, P.card = 2 → ∃ B ∈ blocks, P ⊆ B) :
    blocks = pairCompletion (largeBlocks blocks) := by
  ext P
  constructor
  · intro hP
    by_cases large : 3 ≤ P.card
    · exact Finset.mem_union_left _ (Finset.mem_filter.mpr ⟨hP, large⟩)
    · apply Finset.mem_union_right
      apply Finset.mem_filter.mpr
      have size : P.card = 2 := by have h := lower P hP; omega
      refine ⟨Finset.mem_powersetCard.mpr ⟨Finset.subset_univ _, size⟩, ?_⟩
      intro B hB sub
      rcases Finset.mem_filter.mp hB with ⟨hB, big⟩
      have ne : P ≠ B := by intro eq; rw [eq] at size; omega
      have bound := linear P hP B hB ne
      rw [Finset.inter_eq_left.mpr sub, size] at bound
      omega
  · intro hP
    rcases Finset.mem_union.mp hP with hlarge | hpair
    · exact (Finset.mem_filter.mp hlarge).1
    · rcases Finset.mem_filter.mp hpair with ⟨hpair, free⟩
      have size := (Finset.mem_powersetCard.mp hpair).2
      obtain ⟨B, hB, sub⟩ := covers P size
      have small : B.card ≤ 2 := by
        by_contra h
        exact free B (Finset.mem_filter.mpr ⟨hB, by omega⟩) sub
      have eq : P = B := Finset.eq_of_subset_of_card_le sub (by omega)
      exact eq.symm ▸ hB

omit [Fintype α] in
/-- Enumerate the members of an actual finite family by their exact count. -/
theorem exists_indexing (blocks : Finset (Finset α)) {n : Nat} (count : blocks.card = n) :
    ∃ B : Fin n → Finset α, Function.Injective B ∧ Finset.univ.image B = blocks := by
  let e : Fin n ≃ ↥blocks := Fintype.equivOfCardEq (by simp [count])
  refine ⟨fun i => (e i).val, ?_, ?_⟩
  · intro i j h
    exact e.injective (Subtype.ext h)
  · ext D
    constructor
    · intro h
      obtain ⟨i, _, rfl⟩ := Finset.mem_image.mp h
      exact (e i).property
    · intro h
      exact Finset.mem_image.mpr ⟨e.symm ⟨D, h⟩, Finset.mem_univ _, by simp⟩

/-- A single block can be relabeled to any block of the same size. -/
theorem label_single (six : Fintype.card α = 6) (B : Finset α) (R : Finset (Fin 6))
    (size : B.card = R.card) :
    ∃ e : α ≃ Fin 6, B.map e.toEmbedding = R := by
  have smallB (x : α) : (signature (fun _ : Unit => B) x).card ≤ 2 :=
    (Finset.card_le_univ _).trans (by decide)
  have smallR (x : Fin 6) : (signature (fun _ : Unit => R) x).card ≤ 2 :=
    (Finset.card_le_univ _).trans (by decide)
  obtain ⟨e, he⟩ := exists_equiv_map_blocks (fun _ : Unit => B) (fun _ : Unit => R)
    smallB smallR (by simpa using six) (fun _ => size)
    (fun i j h => False.elim (h (Subsingleton.elim i j)))
  exact ⟨e, he ()⟩

/-- Two blocks can be relabeled once their sizes and intersection size match. -/
theorem label_two (six : Fintype.card α = 6) (B C : Finset α) (R S : Finset (Fin 6))
    (sizeB : B.card = R.card) (sizeC : C.card = S.card)
    (inter : (B ∩ C).card = (R ∩ S).card) :
    ∃ e : α ≃ Fin 6, B.map e.toEmbedding = R ∧ C.map e.toEmbedding = S := by
  let actual : Bool → Finset α := fun b => if b then B else C
  let model : Bool → Finset (Fin 6) := fun b => if b then R else S
  have smallB (x : α) : (signature actual x).card ≤ 2 := by
    simpa using Finset.card_le_univ (signature actual x)
  have smallR (x : Fin 6) : (signature model x).card ≤ 2 := by
    simpa using Finset.card_le_univ (signature model x)
  have singles : ∀ b, (actual b).card = (model b).card := by
    intro b
    cases b
    · exact sizeC
    · exact sizeB
  have pairs : ∀ b c, b ≠ c → (actual b ∩ actual c).card = (model b ∩ model c).card := by
    intro b c hne
    cases b <;> cases c
    · exact False.elim (hne rfl)
    · simpa [actual, model, Finset.inter_comm] using inter
    · exact inter
    · exact False.elim (hne rfl)
  obtain ⟨e, he⟩ := exists_equiv_map_blocks actual model smallB smallR
    (by simpa using six) singles pairs
  exact ⟨e, he true, he false⟩

/-- The analytic pair-intersection theorem and incidence matching label every
linear family of three or more triples against any matching reference. -/
theorem label_many_triples (six : Fintype.card α = 6) (triples : Finset (Finset α))
    (three : ∀ B ∈ triples, B.card = 3) (linear : Linear triples)
    {n : Nat} (count : triples.card = n) (many : 3 ≤ n)
    (C : Fin n → Finset (Fin 6))
    (smallC : ∀ x, (signature C x).card ≤ 2)
    (singleC : ∀ i, (C i).card = 3)
    (pairC : ∀ i j, i ≠ j → (C i ∩ C j).card = 1) :
    ∃ e : α ≃ Fin 6, triples.image (fun B => B.map e.toEmbedding) = Finset.univ.image C := by
  obtain ⟨B, inj, enum⟩ := exists_indexing triples count
  have mem (i : Fin n) : B i ∈ triples := enum ▸ Finset.mem_image.mpr ⟨i, Finset.mem_univ _, rfl⟩
  have smallB (x : α) : (signature B x).card ≤ 2 := by
    rw [signature_card_eq B inj, enum]
    exact triple_degree_le_two Finset.univ triples (by simpa using six)
      (fun _ _ => Finset.subset_univ _) three linear x
  have singles (i : Fin n) : (B i).card = (C i).card := (three _ (mem i)).trans (singleC i).symm
  have pairs (i j : Fin n) (hne : i ≠ j) : (B i ∩ B j).card = (C i ∩ C j).card := by
    rw [pairC i j hne]
    exact triple_intersection_eq_one Finset.univ triples (by simpa using six)
      (fun _ _ => Finset.subset_univ _) three linear (count.symm ▸ many)
      (mem i) (mem j) (fun h => hne (inj h))
  obtain ⟨e, he⟩ := exists_equiv_map_blocks B C smallB smallC
    (by simpa using six) singles pairs
  refine ⟨e, ?_⟩
  rw [← enum, Finset.image_image]
  exact Finset.image_congr (fun i _ => he i)

/-- The three-triple triangle configuration has the exact paper labels. -/
theorem label_three_triples (six : Fintype.card α = 6) (triples : Finset (Finset α))
    (three : ∀ B ∈ triples, B.card = 3) (linear : Linear triples)
    (count : triples.card = 3) :
    ∃ e : α ≃ Fin 6, triples.image (fun B => B.map e.toEmbedding) = representative 4 := by
  let C : Fin 3 → Finset (Fin 6) := ![{0, 3, 4}, {1, 2, 3}, {1, 4, 5}]
  have small : ∀ x, (signature C x).card ≤ 2 := by decide
  have singles : ∀ i, (C i).card = 3 := by decide
  have pairs : ∀ i j, i ≠ j → (C i ∩ C j).card = 1 := by decide
  have labels : Finset.univ.image C = representative 4 := by decide
  simpa only [labels] using label_many_triples six triples three linear count (by decide) C small singles pairs

/-- Four triples form the K4 edge/vertex dual, with explicit paper labels. -/
theorem label_four_triples (six : Fintype.card α = 6) (triples : Finset (Finset α))
    (three : ∀ B ∈ triples, B.card = 3) (linear : Linear triples)
    (count : triples.card = 4) :
    ∃ e : α ≃ Fin 6, triples.image (fun B => B.map e.toEmbedding) = representative 5 := by
  let C : Fin 4 → Finset (Fin 6) := ![{0, 1, 3}, {0, 4, 5}, {1, 2, 4}, {2, 3, 5}]
  have small : ∀ x, (signature C x).card ≤ 2 := by decide
  have singles : ∀ i, (C i).card = 3 := by decide
  have pairs : ∀ i j, i ≠ j → (C i ∩ C j).card = 1 := by decide
  have labels : Finset.univ.image C = representative 5 := by decide
  simpa only [labels] using label_many_triples six triples three linear count (by decide) C small singles pairs

/-- The two-triple case splits by its intersection size, not by enumerating
possible block families. -/
theorem label_two_triples (six : Fintype.card α = 6) (triples : Finset (Finset α))
    (three : ∀ B ∈ triples, B.card = 3) (linear : Linear triples)
    (count : triples.card = 2) :
    ∃ k : Fin 9, (k = 2 ∨ k = 3) ∧ ∃ e : α ≃ Fin 6,
      triples.image (fun B => B.map e.toEmbedding) = representative k := by
  obtain ⟨B, C, hne, family⟩ := Finset.card_eq_two.mp count
  have hB : B ∈ triples := by simp [family]
  have hC : C ∈ triples := by simp [family]
  have hcardB := three B hB
  have hcardC := three C hC
  have interle := linear B hB C hC hne
  by_cases empty : (B ∩ C).card = 0
  · obtain ⟨e, heB, heC⟩ := label_two six B C {0, 4, 5} {1, 2, 3}
      (by simpa using hcardB) (by simpa using hcardC) (by simpa using empty)
    refine ⟨3, Or.inr rfl, e, ?_⟩
    simp [family, heB, heC, representative]
  · have one : (B ∩ C).card = 1 := by omega
    obtain ⟨e, heB, heC⟩ := label_two six B C {0, 3, 4} {1, 2, 3}
      (by simpa using hcardB) (by simpa using hcardC) (by simpa using one)
    refine ⟨2, Or.inl rfl, e, ?_⟩
    simp [family, heB, heC, representative]

/-- A linear triple family on six points is one of the first six labeled
representatives. The implication records exactly the two-triple branch. -/
theorem classify_triples (six : Fintype.card α = 6) (triples : Finset (Finset α))
    (three : ∀ B ∈ triples, B.card = 3) (linear : Linear triples) :
    ∃ k : Fin 9, k.val ≤ 5 ∧
      ((k = 2 ∨ k = 3) → triples.card = 2) ∧ ∃ e : α ≃ Fin 6,
        triples.image (fun B => B.map e.toEmbedding) = representative k := by
  have bound := triple_count_le_four Finset.univ triples (by simpa using six)
    (fun _ _ => Finset.subset_univ _) three linear
  by_cases zero : triples.card = 0
  · let e : α ≃ Fin 6 := Fintype.equivOfCardEq (by simpa using six)
    refine ⟨0, by decide, by simp, e, ?_⟩
    simp [Finset.card_eq_zero.mp zero, representative]
  by_cases one : triples.card = 1
  · obtain ⟨B, family⟩ := Finset.card_eq_one.mp one
    have size : B.card = 3 := three B (by simp [family])
    obtain ⟨e, he⟩ := label_single six B {0, 1, 2} (by simpa using size)
    refine ⟨1, by decide, by simp, e, ?_⟩
    simp [family, he, representative]
  by_cases two : triples.card = 2
  · obtain ⟨k, hk, e, he⟩ := label_two_triples six triples three linear two
    exact ⟨k, by rcases hk with rfl | rfl <;> decide, fun _ => two, e, he⟩
  by_cases threeCount : triples.card = 3
  · obtain ⟨e, he⟩ := label_three_triples six triples three linear threeCount
    exact ⟨4, by decide, by simp, e, he⟩
  · have four : triples.card = 4 := by omega
    obtain ⟨e, he⟩ := label_four_triples six triples three linear four
    exact ⟨5, by decide, by simp, e, he⟩

/-- All nine analytic cases, including explicit labels. Only the assumptions
that blocks have size at most five and distinct blocks share at most one point
are needed for the large-block classification. -/
theorem classify_six (six : Fintype.card α = 6) (blocks : Finset (Finset α))
    (at_most_five : ∀ B ∈ blocks, B.card ≤ 5) (linear : Linear blocks) :
    ∃ k : Fin 9, ((k = 2 ∨ k = 3) → Avoidance.TwoTripleShape blocks) ∧
      ∃ e : α ≃ Fin 6,
        (largeBlocks blocks).image (fun B => B.map e.toEmbedding) = representative k := by
  have sixU : (Finset.univ : Finset α).card = 6 := by simpa using six
  have inside : ∀ B ∈ blocks, B ⊆ (Finset.univ : Finset α) := fun _ _ => Finset.subset_univ _
  by_cases five : ∃ B ∈ blocks, B.card = 5
  · obtain ⟨B, hB, hb⟩ := five
    have family : largeBlocks blocks = {B} := by
      ext C
      simp only [largeBlocks, Finset.mem_filter, Finset.mem_singleton]
      constructor
      · rintro ⟨hC, large⟩
        exact five_block_unique_large Finset.univ blocks sixU inside linear hB hb C hC large
      · rintro rfl
        exact ⟨hB, by omega⟩
    obtain ⟨e, he⟩ := label_single six B {0, 1, 2, 3, 5} (by simpa using hb)
    refine ⟨8, by simp, e, ?_⟩
    simp [family, he, representative]
  by_cases four : ∃ B ∈ blocks, B.card = 4
  · obtain ⟨B, hB, hb⟩ := four
    by_cases other : ∃ C ∈ blocks, 3 ≤ C.card ∧ C ≠ B
    · obtain ⟨C, hC, hc, hne⟩ := other
      have data := large_beside_four Finset.univ blocks sixU inside linear hB hb hC hc hne.symm
      have unique := Finset.card_le_one.mp
        (four_block_at_most_one_other Finset.univ blocks sixU inside linear hB hb)
      have family : largeBlocks blocks = {B, C} := by
        ext D
        simp only [largeBlocks, Finset.mem_filter, Finset.mem_insert, Finset.mem_singleton]
        constructor
        · rintro ⟨hD, hd⟩
          by_cases eq : D = B
          · exact Or.inl eq
          · exact Or.inr (unique D (Finset.mem_filter.mpr ⟨hD, hd, eq⟩)
              C (Finset.mem_filter.mpr ⟨hC, hc, hne⟩))
        · rintro (rfl | rfl)
          · exact ⟨hB, by omega⟩
          · exact ⟨hC, hc⟩
      obtain ⟨e, heB, heC⟩ := label_two six B C {0, 3, 4, 5} {1, 2, 3}
        (by simpa using hb) (by simpa using data.1) (by simpa using data.2.2)
      refine ⟨7, by simp, e, ?_⟩
      simp [family, heB, heC, representative]
    · have family : largeBlocks blocks = {B} := by
        ext C
        simp only [largeBlocks, Finset.mem_filter, Finset.mem_singleton]
        constructor
        · rintro ⟨hC, hc⟩
          by_contra ne
          exact other ⟨C, hC, hc, ne⟩
        · rintro rfl
          exact ⟨hB, by omega⟩
      obtain ⟨e, he⟩ := label_single six B {0, 1, 2, 5} (by simpa using hb)
      refine ⟨6, by simp, e, ?_⟩
      simp [family, he, representative]
  · have small : ∀ B ∈ blocks, B.card ≤ 3 := by
      intro B hB
      have bound := at_most_five B hB
      have nofive : B.card ≠ 5 := fun h => five ⟨B, hB, h⟩
      have nofour : B.card ≠ 4 := fun h => four ⟨B, hB, h⟩
      omega
    have eqtriples : largeBlocks blocks = blocks.filter (fun B => B.card = 3) := by
      apply Finset.filter_congr
      intro B hB
      have bound := small B hB
      omega
    have three : ∀ B ∈ largeBlocks blocks, B.card = 3 := by
      intro B hB
      rw [eqtriples] at hB
      exact (Finset.mem_filter.mp hB).2
    have lin : Linear (largeBlocks blocks) := by
      intro B hB C hC hne
      exact linear B (Finset.mem_filter.mp hB).1 C (Finset.mem_filter.mp hC).1 hne
    obtain ⟨k, _, htwo, e, he⟩ := classify_triples six (largeBlocks blocks) three lin
    refine ⟨k, ?_, e, he⟩
    intro h
    exact ⟨small, eqtriples ▸ htwo h⟩

/-- A good six-point deletion has one of seven explicit representatives;
both two-triple cases are excluded by the stronger deletion lemma. -/
theorem classify_good_six (six : Fintype.card α = 6) (blocks : Finset (Finset α))
    (at_most_five : ∀ B ∈ blocks, B.card ≤ 5) (linear : Linear blocks)
    (good : ¬ Avoidance.TwoTripleShape blocks) :
    ∃ k : Fin 9, k ≠ 2 ∧ k ≠ 3 ∧ ∃ e : α ≃ Fin 6,
      (largeBlocks blocks).image (fun B => B.map e.toEmbedding) = representative k := by
  obtain ⟨k, htwo, e, he⟩ := classify_six six blocks at_most_five linear
  exact ⟨k, fun h => good (htwo (Or.inl h)), fun h => good (htwo (Or.inr h)), e, he⟩

end Aris4Math.K6Classification

#print axioms Aris4Math.K6Classification.label_three_triples
#print axioms Aris4Math.K6Classification.label_four_triples
#print axioms Aris4Math.K6Classification.classify_six
#print axioms Aris4Math.K6Classification.classify_good_six
#print axioms Aris4Math.K6Classification.recover_pairs
