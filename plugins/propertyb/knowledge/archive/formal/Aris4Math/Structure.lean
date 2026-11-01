import Aris4Math

/-!
Actual hypergraph incidence identities and degree consequences.
The identities are proved from the finite edge set and five-uniformity;
they are not additional hypotheses of the original Property B target.
-/
open scoped BigOperators

namespace Aris4Math.Simple5Hypergraph

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- Number of actual edges through x. -/
def degree (H : Simple5Hypergraph V) (x : V) : Nat :=
  (H.edges.filter fun e => x ∈ e).card

/-- Number of actual edges through both x and y. -/
def codegree (H : Simple5Hypergraph V) (x y : V) : Nat :=
  (H.edges.filter fun e => x ∈ e ∧ y ∈ e).card

/-- Every distinct vertex pair belongs to an edge. -/
def PairCovering (H : Simple5Hypergraph V) : Prop :=
  ∀ x y, x ≠ y → ∃ e ∈ H.edges, x ∈ e ∧ y ∈ e

/-- Double count the incidences (vertex, edge). -/
theorem sum_degrees (H : Simple5Hypergraph V) :
    (∑ x : V, H.degree x) = 5 * H.edges.card := by
  conv_lhs => simp only [degree, Finset.card_eq_sum_ones, Finset.sum_filter]
  rw [Finset.sum_comm]
  calc
    (∑ e ∈ H.edges, ∑ x : V, if x ∈ e then 1 else 0) =
        ∑ e ∈ H.edges, e.card := by simp
    _ = ∑ _e ∈ H.edges, 5 := Finset.sum_congr rfl H.five_uniform
    _ = 5 * H.edges.card := by simp [Nat.mul_comm]

/-- Double count the incidences (other vertex, edge through x). -/
theorem sum_codegrees_erase (H : Simple5Hypergraph V) (x : V) :
    (∑ y ∈ Finset.univ.erase x, H.codegree x y) = 4 * H.degree x := by
  simp only [codegree, Finset.card_eq_sum_ones, Finset.sum_filter]
  rw [Finset.sum_comm]
  calc
    (∑ e ∈ H.edges, ∑ y ∈ Finset.univ.erase x, if x ∈ e ∧ y ∈ e then 1 else 0) =
        ∑ e ∈ H.edges, if x ∈ e then 4 else 0 := by
      apply Finset.sum_congr rfl
      intro e he
      by_cases hx : x ∈ e
      · simp only [hx, true_and, if_true]
        rw [Finset.sum_boole]
        have filt : ((Finset.univ.erase x).filter (· ∈ e)) = e.erase x := by
          ext y
          simp only [Finset.mem_filter, Finset.mem_erase, Finset.mem_univ, and_true]
        rw [filt, Finset.card_erase_of_mem hx, H.five_uniform e he]
        norm_num
      · simp [hx]
    _ = 4 * H.degree x := by
      simp only [degree, Finset.card_eq_sum_ones, Finset.sum_filter]
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro e _
      split_ifs <;> simp

omit [Fintype V] in
/-- Pair covering supplies the actual positive codegree used in the sum. -/
theorem one_le_codegree (H : Simple5Hypergraph V) (cover : H.PairCovering)
    {x y : V} (hne : x ≠ y) : 1 ≤ H.codegree x y := by
  obtain ⟨e, he, hx, hy⟩ := cover x y hne
  exact Finset.one_le_card.mpr ⟨e, Finset.mem_filter.mpr ⟨he, hx, hy⟩⟩

/-- The standard minimum-degree inequality, derived from incidences. -/
theorem pairCovering_degree_bound (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (x : V) : Fintype.card V - 1 ≤ 4 * H.degree x := by
  calc
    Fintype.card V - 1 = ∑ _y ∈ Finset.univ.erase x, 1 := by simp
    _ ≤ ∑ y ∈ Finset.univ.erase x, H.codegree x y := by
      apply Finset.sum_le_sum
      intro y hy
      exact H.one_le_codegree cover (Finset.mem_erase.mp hy).1.symm
    _ = 4 * H.degree x := H.sum_codegrees_erase x

/-- At most 32 edges and pair covering force at most 25 vertices. -/
theorem card_le_twenty_five (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edge_bound : H.edges.card ≤ 32) : Fintype.card V ≤ 25 := by
  have h := Finset.sum_le_sum (s := Finset.univ)
    (fun x _ => H.pairCovering_degree_bound cover x)
  simp only [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, Nat.cast_id] at h
  rw [← Finset.mul_sum, H.sum_degrees] at h
  have total : 5 * H.edges.card ≤ 160 := by omega
  have product : Fintype.card V * (Fintype.card V - 1) ≤ 640 := by omega
  by_contra hn
  have hv : 26 ≤ Fintype.card V := by omega
  have hv' : 25 ≤ Fintype.card V - 1 := by omega
  nlinarith

/-- The numerical total is a consequence of actual edge cardinality. -/
theorem sum_degrees_eq_160 (H : Simple5Hypergraph V) (edges32 : H.edges.card = 32) :
    (∑ x : V, H.degree x) = 160 := by rw [H.sum_degrees, edges32]

/-- Exact six-degree vertex set. -/
def sixVertices (H : Simple5Hypergraph V) : Finset V :=
  Finset.univ.filter fun x => H.degree x = 6

/-- Counting low-degree vertices from an actual degree budget. -/
theorem sixVertices_budget (H : Simple5Hypergraph V) (edges32 : H.edges.card = 32)
    (min_degree : ∀ x, 6 ≤ H.degree x) :
    7 * Fintype.card V ≤ 160 + H.sixVertices.card := by
  have each (x : V) : 7 ≤ H.degree x + if H.degree x = 6 then 1 else 0 := by
    have hd := min_degree x
    split_ifs <;> omega
  have h := Finset.sum_le_sum (s := Finset.univ) (fun x _ => each x)
  simpa [Finset.sum_add_distrib, H.sum_degrees_eq_160 edges32,
    sixVertices, Nat.mul_comm] using h

/-- Twenty-four points give at least eight vertices of degree six. -/
theorem sixVertices_card_ge_eight (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges32 : H.edges.card = 32) (vertices24 : Fintype.card V = 24) :
    8 ≤ H.sixVertices.card := by
  have minimum (x : V) : 6 ≤ H.degree x := by
    have h := H.pairCovering_degree_bound cover x
    rw [vertices24] at h
    omega
  have budget := H.sixVertices_budget edges32 minimum
  rw [vertices24] at budget
  omega

/-- Twenty-five points give at least fifteen vertices of degree six. -/
theorem sixVertices_card_ge_fifteen (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edges32 : H.edges.card = 32) (vertices25 : Fintype.card V = 25) :
    15 ≤ H.sixVertices.card := by
  have minimum (x : V) : 6 ≤ H.degree x := by
    have h := H.pairCovering_degree_bound cover x
    rw [vertices25] at h
    omega
  have budget := H.sixVertices_budget edges32 minimum
  rw [vertices25] at budget
  omega

/-- A six-degree vertex on 25 points has codegree exactly one with every other point. -/
theorem codegree_eq_one_of_twenty_five (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (vertices25 : Fintype.card V = 25) {x : V} (degree6 : H.degree x = 6)
    {y : V} (hne : x ≠ y) : H.codegree x y = 1 := by
  have lower : ∀ z ∈ Finset.univ.erase x, 1 ≤ H.codegree x z := by
    intro z hz
    exact H.one_le_codegree cover (Finset.mem_erase.mp hz).1.symm
  have eqsum : (∑ _z ∈ Finset.univ.erase x, 1) =
      ∑ z ∈ Finset.univ.erase x, H.codegree x z := by
    rw [H.sum_codegrees_erase, degree6]
    simp [vertices25]
  have equal := (Finset.sum_eq_sum_iff_of_le lower).mp eqsum
  exact (equal y (Finset.mem_erase.mpr ⟨hne.symm, Finset.mem_univ y⟩)).symm

omit [Fintype V] in
/-- Symmetry is inherited from actual edge membership. -/
theorem codegree_comm (H : Simple5Hypergraph V) (x y : V) :
    H.codegree x y = H.codegree y x := by simp [codegree, and_comm]

/-- Total excess codegree, without replacing actual incidence counts by inputs. -/
theorem sum_codegree_excess (H : Simple5Hypergraph V) (cover : H.PairCovering) (x : V) :
    (∑ y ∈ Finset.univ.erase x, (H.codegree x y - 1)) =
      4 * H.degree x - (Fintype.card V - 1) := by
  rw [Finset.sum_tsub_distrib]
  · rw [H.sum_codegrees_erase]
    simp
  · intro y hy
    exact H.one_le_codegree cover (Finset.mem_erase.mp hy).1.symm

/-- Vertices other than x sharing at least two edges with x. -/
def badPartners (H : Simple5Hypergraph V) (x : V) : Finset V :=
  (Finset.univ.erase x).filter fun y => 2 ≤ H.codegree x y

/-- Every bad partner consumes at least one unit of the excess budget. -/
theorem badPartners_card_le_excess (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (x : V) : (H.badPartners x).card ≤ 4 * H.degree x - (Fintype.card V - 1) := by
  rw [← H.sum_codegree_excess cover x]
  simp only [badPartners, Finset.card_eq_sum_ones, Finset.sum_filter]
  apply Finset.sum_le_sum
  intro y _
  split_ifs <;> omega

/-- A six-degree vertex on 24 points has at most one bad partner. -/
theorem badPartners_card_le_one_of_twenty_four (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (vertices24 : Fintype.card V = 24)
    {x : V} (degree6 : H.degree x = 6) : (H.badPartners x).card ≤ 1 := by
  have h := H.badPartners_card_le_excess cover x
  simpa [vertices24, degree6] using h

omit [Fintype V] in
/-- Greedily choose k pairwise non-related points when every point has at most
one other related point. The construction removes at most two points per step. -/
theorem exists_pairwise_avoiding_subset (R : V → V → Prop) [DecidableRel R]
    (symmetric : ∀ x y, R x y → R y x) :
    ∀ (k : Nat) (S : Finset V),
      (∀ x ∈ S, ((S.erase x).filter (R x)).card ≤ 1) → 2 * k ≤ S.card →
      ∃ T ⊆ S, T.card = k ∧ ∀ a ∈ T, ∀ b ∈ T, a ≠ b → ¬ R a b := by
  intro k
  induction k with
  | zero =>
      intro S _ _
      refine ⟨∅, Finset.empty_subset S, rfl, ?_⟩
      simp
  | succ k ih =>
      intro S bad size
      have nonempty : S.Nonempty := Finset.card_pos.mp (by omega)
      obtain ⟨x, hx⟩ := nonempty
      let B := insert x ((S.erase x).filter (R x))
      let S' := S \ B
      have xnot : x ∉ (S.erase x).filter (R x) := by simp
      have smallB : B.card ≤ 2 := by
        dsimp [B]
        rw [Finset.card_insert_of_notMem xnot]
        have h := bad x hx
        omega
      have largeS' : 2 * k ≤ S'.card := by
        have h := Finset.card_le_card_sdiff_add_card (s := S) (t := B)
        change S.card ≤ S'.card + B.card at h
        omega
      have subS : S' ⊆ S := Finset.sdiff_subset
      have bad' : ∀ y ∈ S', ((S'.erase y).filter (R y)).card ≤ 1 := by
        intro y hy
        apply le_trans (Finset.card_le_card ?_) (bad y (subS hy))
        intro z hz
        rcases Finset.mem_filter.mp hz with ⟨hz, hr⟩
        rcases Finset.mem_erase.mp hz with ⟨hne, hzs⟩
        exact Finset.mem_filter.mpr ⟨Finset.mem_erase.mpr ⟨hne, subS hzs⟩, hr⟩
      obtain ⟨T, subT, cardT, independent⟩ := ih S' bad' largeS'
      have xnotS' : x ∉ S' := by simp [S', B]
      have xnotT : x ∉ T := fun h => xnotS' (subT h)
      have avoids (y : V) (hy : y ∈ T) : ¬ R x y := by
        have hyS' := subT hy
        have hyS := subS hyS'
        have hyB : y ∉ B := (Finset.mem_sdiff.mp hyS').2
        have hyne : y ≠ x := by
          intro heq
          subst y
          exact hyB (Finset.mem_insert_self _ _)
        intro related
        apply hyB
        exact Finset.mem_insert_of_mem
          (Finset.mem_filter.mpr ⟨Finset.mem_erase.mpr ⟨hyne, hyS⟩, related⟩)
      refine ⟨insert x T, ?_, ?_, ?_⟩
      · exact Finset.insert_subset_iff.mpr ⟨hx, subT.trans subS⟩
      · rw [Finset.card_insert_of_notMem xnotT, cardT]
      · intro a ha b hb hne
        rcases Finset.mem_insert.mp ha with hax | hat
        · subst a
          rcases Finset.mem_insert.mp hb with hbx | hbt
          · subst b
            exact False.elim (hne rfl)
          · exact avoids b hbt
        · rcases Finset.mem_insert.mp hb with hbx | hbt
          · subst b
            exact fun h => avoids a hat (symmetric a x h)
          · exact independent a hat b hbt hne

/-- The four locks needed at v=24 exist in the actual hypergraph. -/
theorem exists_four_six_degree_codegree_one (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (edges32 : H.edges.card = 32)
    (vertices24 : Fintype.card V = 24) :
    ∃ T : Finset V, T.card = 4 ∧ (∀ x ∈ T, H.degree x = 6) ∧
      ∀ x ∈ T, ∀ y ∈ T, x ≠ y → H.codegree x y = 1 := by
  let R := fun x y => 2 ≤ H.codegree x y
  have symmetric : ∀ x y, R x y → R y x := by
    intro x y h
    simpa only [R, H.codegree_comm y x] using h
  have bad : ∀ x ∈ H.sixVertices,
      ((H.sixVertices.erase x).filter (R x)).card ≤ 1 := by
    intro x hx
    have hd : H.degree x = 6 := (Finset.mem_filter.mp hx).2
    apply le_trans (Finset.card_le_card ?_)
      (H.badPartners_card_le_one_of_twenty_four cover vertices24 hd)
    intro y hy
    rcases Finset.mem_filter.mp hy with ⟨hy, hr⟩
    rcases Finset.mem_erase.mp hy with ⟨hne, _⟩
    exact Finset.mem_filter.mpr ⟨Finset.mem_erase.mpr ⟨hne, Finset.mem_univ y⟩, hr⟩
  have enough : 2 * 4 ≤ H.sixVertices.card := by
    simpa using H.sixVertices_card_ge_eight cover edges32 vertices24
  obtain ⟨T, subT, cardT, independent⟩ :=
    exists_pairwise_avoiding_subset R symmetric 4 H.sixVertices bad enough
  refine ⟨T, cardT, ?_, ?_⟩
  · intro x hx
    exact (Finset.mem_filter.mp (subT hx)).2
  · intro x hx y hy hne
    have positive := H.one_le_codegree cover hne
    have notbad := independent x hx y hy hne
    dsimp [R] at notbad
    omega

/-- Seven six-degree points with pairwise codegree one are available at v=25. -/
theorem exists_seven_six_degree_codegree_one (H : Simple5Hypergraph V)
    (cover : H.PairCovering) (edges32 : H.edges.card = 32)
    (vertices25 : Fintype.card V = 25) :
    ∃ T : Finset V, T.card = 7 ∧ (∀ x ∈ T, H.degree x = 6) ∧
      ∀ x ∈ T, ∀ y ∈ T, x ≠ y → H.codegree x y = 1 := by
  have enough : 7 ≤ H.sixVertices.card :=
    le_trans (by decide) (H.sixVertices_card_ge_fifteen cover edges32 vertices25)
  obtain ⟨T, subT, cardT⟩ := Finset.exists_subset_card_eq enough
  refine ⟨T, cardT, ?_, ?_⟩
  · intro x hx
    exact (Finset.mem_filter.mp (subT hx)).2
  · intro x hx y _ hne
    exact H.codegree_eq_one_of_twenty_five cover vertices25
      (Finset.mem_filter.mp (subT hx)).2 hne

end Aris4Math.Simple5Hypergraph

#print axioms Aris4Math.Simple5Hypergraph.sum_degrees
#print axioms Aris4Math.Simple5Hypergraph.sum_codegrees_erase
#print axioms Aris4Math.Simple5Hypergraph.card_le_twenty_five
#print axioms Aris4Math.Simple5Hypergraph.sixVertices_card_ge_eight
#print axioms Aris4Math.Simple5Hypergraph.sixVertices_card_ge_fifteen
#print axioms Aris4Math.Simple5Hypergraph.codegree_eq_one_of_twenty_five
