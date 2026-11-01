import Aris4Math.Structure

open scoped BigOperators

namespace Aris4Math.Simple5Hypergraph

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- Actual partners of codegree exactly one, excluding the vertex itself. -/
def goodPartners (H : Simple5Hypergraph V) (x : V) : Finset V :=
  Finset.univ \ insert x (H.badPartners x)

theorem mem_goodPartners (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (x y : V) : y ∈ H.goodPartners x ↔ y ≠ x ∧ H.codegree x y = 1 := by
  simp only [goodPartners, Finset.mem_sdiff, Finset.mem_univ, true_and,
    Finset.mem_insert, not_or, badPartners, Finset.mem_filter,
    Finset.mem_erase, Finset.mem_univ, and_true]
  constructor
  · rintro ⟨hne, hbad⟩
    have hp := H.one_le_codegree cover (Ne.symm hne)
    constructor
    · exact hne
    · have : ¬ 2 ≤ H.codegree x y := fun h => hbad ⟨hne, h⟩
      omega
  · rintro ⟨hne, hone⟩
    exact ⟨hne, by omega⟩

theorem goodPartners_budget (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (x : V) : Fintype.card V ≤ (H.goodPartners x).card +
      1 + (4 * H.degree x - (Fintype.card V - 1)) := by
  have h := Finset.card_le_card_sdiff_add_card (s := Finset.univ)
    (t := insert x (H.badPartners x))
  have hc := Finset.card_insert_le x (H.badPartners x)
  have hb := H.badPartners_card_le_excess cover x
  change Fintype.card V ≤ (H.goodPartners x).card +
    (insert x (H.badPartners x)).card at h
  omega

/-- A lower degree bound outside S and a larger bound on S give an actual
incidence budget. -/
theorem subset_degree_budget (H : Simple5Hypergraph V) (S : Finset V)
    (base extra : Nat) (minimum : ∀ x, base ≤ H.degree x)
    (higher : ∀ x ∈ S, base + extra ≤ H.degree x) :
    base * Fintype.card V + extra * S.card ≤ 5 * H.edges.card := by
  have each (x : V) : base + (if x ∈ S then extra else 0) ≤ H.degree x := by
    split_ifs with h
    · exact higher x h
    · simpa using minimum x
  have h := Finset.sum_le_sum (s := Finset.univ) (fun x _ => each x)
  simpa [Finset.sum_add_distrib, H.sum_degrees, Nat.mul_comm] using h

theorem exists_degree_five_to_seven_of_twenty_one
    (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges32 : H.edges.card = 32) (vertices21 : Fintype.card V = 21) :
    ∃ x, 5 ≤ H.degree x ∧ H.degree x ≤ 7 := by
  have minimum (x : V) : 5 ≤ H.degree x := by
    have h := H.pairCovering_degree_bound cover x
    rw [vertices21] at h
    omega
  by_contra hn
  have higher (x : V) : 8 ≤ H.degree x := by
    have hm := minimum x
    have : ¬ (5 ≤ H.degree x ∧ H.degree x ≤ 7) := fun h => hn ⟨x, h⟩
    omega
  have budget := H.subset_degree_budget Finset.univ 8 0 higher
    (fun x _ => by simpa using higher x)
  simp [vertices21, edges32] at budget

theorem exists_degree_six_of_twenty_three
    (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges32 : H.edges.card = 32) (vertices23 : Fintype.card V = 23) :
    ∃ x, H.degree x = 6 := by
  by_contra hn
  have higher (x : V) : 7 ≤ H.degree x := by
    have h := H.pairCovering_degree_bound cover x
    rw [vertices23] at h
    have : H.degree x ≠ 6 := fun h => hn ⟨x, h⟩
    omega
  have budget := H.subset_degree_budget Finset.univ 7 0 higher
    (fun x _ => by simpa using higher x)
  simp [vertices23, edges32] at budget

/-- At 22 points the complete two-lock alternatives arise from actual degrees. -/
theorem exists_two_locks_of_twenty_two
    (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges32 : H.edges.card = 32) (vertices22 : Fintype.card V = 22) :
    ∃ x y, x ≠ y ∧ H.codegree x y = 1 ∧
      ((H.degree x = 6 ∧ H.degree y = 6) ∨
       (H.degree x = 6 ∧ H.degree y = 7) ∨
       (H.degree x = 7 ∧ H.degree y = 7)) := by
  have minimum (x : V) : 6 ≤ H.degree x := by
    have h := H.pairCovering_degree_bound cover x
    rw [vertices22] at h
    omega
  by_cases hsix : ∃ x, H.degree x = 6
  · obtain ⟨x, hx⟩ := hsix
    have size := H.goodPartners_budget cover x
    rw [vertices22, hx] at size
    have partner : ∃ y ∈ H.goodPartners x, H.degree y ≤ 7 := by
      by_contra hn
      have high : ∀ y ∈ H.goodPartners x, 6 + 2 ≤ H.degree y := by
        intro y hy
        have : ¬ H.degree y ≤ 7 := fun h => hn ⟨y, hy, h⟩
        omega
      have budget := H.subset_degree_budget (H.goodPartners x) 6 2 minimum high
      rw [vertices22, edges32] at budget
      omega
    obtain ⟨y, hy, dy⟩ := partner
    obtain ⟨hne, hcodeg⟩ := (H.mem_goodPartners cover x y).mp hy
    refine ⟨x, y, Ne.symm hne, hcodeg, ?_⟩
    have ly := minimum y
    rcases (show H.degree y = 6 ∨ H.degree y = 7 by omega) with h6 | h7
    · exact Or.inl ⟨hx, h6⟩
    · exact Or.inr (Or.inl ⟨hx, h7⟩)
  · have min7 (x : V) : 7 ≤ H.degree x := by
      have h := minimum x
      have : H.degree x ≠ 6 := fun h => hsix ⟨x, h⟩
      omega
    let S := Finset.univ.filter fun x => H.degree x = 7
    have size : 16 ≤ S.card := by
      have each (x : V) : 8 ≤ H.degree x + if H.degree x = 7 then 1 else 0 := by
        have h := min7 x
        split_ifs <;> omega
      have h := Finset.sum_le_sum (s := Finset.univ) (fun x _ => each x)
      have hs : 8 * Fintype.card V ≤ 160 + S.card := by
        simpa [Finset.sum_add_distrib, H.sum_degrees_eq_160 edges32,
          S, Nat.mul_comm] using h
      rw [vertices22] at hs
      omega
    obtain ⟨x, hx⟩ := Finset.card_pos.mp (show 0 < S.card by omega)
    have dx : H.degree x = 7 := (Finset.mem_filter.mp hx).2
    let B := insert x (H.badPartners x)
    have bsize : B.card ≤ 8 := by
      have hb := H.badPartners_card_le_excess cover x
      rw [vertices22, dx] at hb
      have hi := Finset.card_insert_le x (H.badPartners x)
      dsimp [B]
      omega
    have large := Finset.card_le_card_sdiff_add_card (s := S) (t := B)
    obtain ⟨y, hy⟩ := Finset.card_pos.mp (show 0 < (S \ B).card by omega)
    obtain ⟨hyS, hyB⟩ := Finset.mem_sdiff.mp hy
    have good : y ∈ H.goodPartners x := by
      exact Finset.mem_sdiff.mpr ⟨Finset.mem_univ y, hyB⟩
    obtain ⟨hne, hcodeg⟩ := (H.mem_goodPartners cover x y).mp good
    exact ⟨x, y, Ne.symm hne, hcodeg,
      Or.inr (Or.inr ⟨dx, (Finset.mem_filter.mp hyS).2⟩)⟩

omit [Fintype V] in
theorem edge_unique_of_codegree_one (H : Simple5Hypergraph V)
    {x y : V} (hone : H.codegree x y = 1)
    {e f : Finset V} (he : e ∈ H.edges) (hf : f ∈ H.edges)
    (hxe : x ∈ e) (hye : y ∈ e) (hxf : x ∈ f) (hyf : y ∈ f) : e = f := by
  apply Finset.card_le_one.mp (le_of_eq hone) e
    (Finset.mem_filter.mpr ⟨he, hxe, hye⟩) f
    (Finset.mem_filter.mpr ⟨hf, hxf, hyf⟩)

/-- The complete alternatives at 23 points: either two degree-six locks,
or degrees 6,7,7 with all pair codegrees one and no edge through all three. -/
theorem exists_locks_of_twenty_three
    (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges32 : H.edges.card = 32) (vertices23 : Fintype.card V = 23) :
    (∃ x y, x ≠ y ∧ H.degree x = 6 ∧ H.degree y = 6 ∧ H.codegree x y = 1) ∨
    (∃ x y z, x ≠ y ∧ x ≠ z ∧ y ≠ z ∧
      H.degree x = 6 ∧ H.degree y = 7 ∧ H.degree z = 7 ∧
      H.codegree x y = 1 ∧ H.codegree x z = 1 ∧ H.codegree y z = 1 ∧
      ∀ e ∈ H.edges, ¬ (x ∈ e ∧ y ∈ e ∧ z ∈ e)) := by
  have minimum (x : V) : 6 ≤ H.degree x := by
    have h := H.pairCovering_degree_bound cover x
    rw [vertices23] at h
    omega
  obtain ⟨x, dx⟩ := H.exists_degree_six_of_twenty_three cover edges32 vertices23
  let W := H.goodPartners x
  have sizeW : 20 ≤ W.card := by
    have h := H.goodPartners_budget cover x
    rw [vertices23, dx] at h
    change 23 ≤ W.card + 1 + (4 * 6 - (23 - 1)) at h
    omega
  by_cases hpair : ∃ y ∈ W, H.degree y = 6
  · obtain ⟨y, hy, dy⟩ := hpair
    obtain ⟨hne, hone⟩ := (H.mem_goodPartners cover x y).mp hy
    exact Or.inl ⟨x, y, Ne.symm hne, dx, dy, hone⟩
  · right
    let S := W.filter fun y => H.degree y = 7
    have minW (y : V) (hy : y ∈ W) : 7 ≤ H.degree y := by
      have h := minimum y
      have : H.degree y ≠ 6 := fun hd => hpair ⟨y, hy, hd⟩
      omega
    have sizeS : 18 ≤ S.card := by
      have each (y : V) : 6 + (if y ∈ W then 2 else 0) ≤
          H.degree y + (if y ∈ S then 1 else 0) := by
        by_cases hyW : y ∈ W
        · have hymin := minW y hyW
          by_cases hy7 : H.degree y = 7
          · have hyS : y ∈ S := Finset.mem_filter.mpr ⟨hyW, hy7⟩
            simp [hyW, hyS, hy7]
          · have hyS : y ∉ S := by simp [S, hy7]
            simp only [hyW, hyS, if_true, if_false, Nat.add_zero]
            omega
        · have hyS : y ∉ S := fun h => hyW (Finset.mem_filter.mp h).1
          simpa [hyW, hyS] using minimum y
      have h := Finset.sum_le_sum (s := Finset.univ) (fun y _ => each y)
      have hs : 6 * Fintype.card V + 2 * W.card ≤ 160 + S.card := by
        simpa [Finset.sum_add_distrib, H.sum_degrees_eq_160 edges32,
          Nat.mul_comm] using h
      rw [vertices23] at hs
      omega
    obtain ⟨y, hy⟩ := Finset.card_pos.mp (show 0 < S.card by omega)
    obtain ⟨hyW, dy⟩ := Finset.mem_filter.mp hy
    obtain ⟨hyx, cxy⟩ := (H.mem_goodPartners cover x y).mp hyW
    obtain ⟨e, he, hxe, hye⟩ := cover x y (Ne.symm hyx)
    let B := insert y (H.badPartners y ∪ e)
    have sizeB : B.card ≤ 12 := by
      have hb := H.badPartners_card_le_excess cover y
      rw [vertices23, dy] at hb
      have hu := Finset.card_union_le (H.badPartners y) e
      have hi := Finset.card_insert_le y (H.badPartners y ∪ e)
      have hc := H.five_uniform e he
      dsimp [B]
      omega
    have sizeDiff := Finset.card_le_card_sdiff_add_card (s := S) (t := B)
    obtain ⟨z, hz⟩ := Finset.card_pos.mp (show 0 < (S \ B).card by omega)
    obtain ⟨hzS, hzB⟩ := Finset.mem_sdiff.mp hz
    obtain ⟨hzW, dz⟩ := Finset.mem_filter.mp hzS
    obtain ⟨hzx, cxz⟩ := (H.mem_goodPartners cover x z).mp hzW
    have hzne : z ≠ y := fun h => hzB (by simp [B, h])
    have hzbad : z ∉ H.badPartners y := fun h =>
      hzB (Finset.mem_insert_of_mem (Finset.mem_union_left _ h))
    have hze : z ∉ e := fun h =>
      hzB (Finset.mem_insert_of_mem (Finset.mem_union_right _ h))
    have hzgood : z ∈ H.goodPartners y :=
      Finset.mem_sdiff.mpr ⟨Finset.mem_univ z,
        by simpa only [Finset.mem_insert, not_or] using And.intro hzne hzbad⟩
    have cyz := ((H.mem_goodPartners cover y z).mp hzgood).2
    refine ⟨x, y, z, Ne.symm hyx, Ne.symm hzx, Ne.symm hzne,
      dx, dy, dz, cxy, cxz, cyz, ?_⟩
    intro f hf hxyz
    have hfe := H.edge_unique_of_codegree_one cxy hf he hxyz.1 hxyz.2.1 hxe hye
    exact hze (hfe ▸ hxyz.2.2)

end Aris4Math.Simple5Hypergraph

#print axioms Aris4Math.Simple5Hypergraph.exists_degree_five_to_seven_of_twenty_one
#print axioms Aris4Math.Simple5Hypergraph.exists_two_locks_of_twenty_two
#print axioms Aris4Math.Simple5Hypergraph.exists_locks_of_twenty_three
