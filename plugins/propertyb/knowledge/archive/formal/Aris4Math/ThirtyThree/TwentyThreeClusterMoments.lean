import Aris4Math.ThirtyThree.TwentyThreeSelection
import Mathlib.Tactic.IntervalCases

/-! Incidence moments for three actual codegree-two cliques. -/
namespace Aris4Math.ThirtyThree.TwentyThreeClusterMoments

open scoped BigOperators
variable {V : Type*} [Fintype V] [DecidableEq V]

theorem sum_inter_card (H : Simple5Hypergraph V) (S : Finset V) :
    (∑ e ∈ H.edges, (e ∩ S).card) = ∑ x ∈ S, H.degree x := by
  simp only [Simple5Hypergraph.degree, Finset.card_eq_sum_ones, Finset.sum_filter]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro e _
  simp [Finset.inter_comm]

theorem sum_inter_product (H : Simple5Hypergraph V) (A B : Finset V) :
    (∑ e ∈ H.edges, (e ∩ A).card * (e ∩ B).card) =
      ∑ x ∈ A, ∑ y ∈ B, H.codegree x y := by
  simp only [Simple5Hypergraph.codegree, Finset.card_eq_sum_ones, Finset.sum_filter]
  apply Eq.symm
  calc
    (∑ x ∈ A, ∑ y ∈ B, ∑ e ∈ H.edges, if x ∈ e ∧ y ∈ e then 1 else 0) =
        ∑ x ∈ A, ∑ e ∈ H.edges, ∑ y ∈ B, if x ∈ e ∧ y ∈ e then 1 else 0 := by
      apply Finset.sum_congr rfl
      intro x _
      rw [Finset.sum_comm]
    _ = ∑ e ∈ H.edges, ∑ x ∈ A, ∑ y ∈ B, if x ∈ e ∧ y ∈ e then 1 else 0 := by
      rw [Finset.sum_comm]
    _ = ∑ e ∈ H.edges, (∑ _x ∈ e ∩ A, 1) * (∑ _y ∈ e ∩ B, 1) := by
      apply Finset.sum_congr rfl
      intro e _
      simp only [Finset.sum_const, nsmul_eq_mul, Nat.mul_one]
      have h (x y : V) : (if x ∈ e ∧ y ∈ e then 1 else 0) =
          (if x ∈ e then 1 else 0) * (if y ∈ e then 1 else 0) := by
        split_ifs <;> simp_all
      simp_rw [h, ← Finset.mul_sum, ← Finset.sum_mul]
      simp [Finset.inter_comm, Nat.mul_comm]

theorem clique_square_moment (H : Simple5Hypergraph V) (S : Finset V)
    (degrees : ∀ x ∈ S, H.degree x = 7)
    (pairs : ∀ x ∈ S, ∀ y ∈ S, x ≠ y → H.codegree x y = 2) :
    (∑ e ∈ H.edges, (e ∩ S).card * (e ∩ S).card) =
      S.card * (7 + 2 * (S.card - 1)) := by
  rw [sum_inter_product]
  have row (x : V) (hx : x ∈ S) : (∑ y ∈ S, H.codegree x y) =
      7 + 2 * (S.card - 1) := by
    have h := Finset.sum_erase_add (s := S) (fun y => H.codegree x y) hx
    have diag : H.codegree x x = 7 := by
      simpa [Simple5Hypergraph.codegree, Simple5Hypergraph.degree] using degrees x hx
    have off : (∑ y ∈ S.erase x, H.codegree x y) = 2 * (S.card - 1) := by
      calc
        _ = ∑ _y ∈ S.erase x, 2 := Finset.sum_congr rfl (fun y hy =>
          pairs x hx y (Finset.mem_erase.mp hy).2 (Finset.mem_erase.mp hy).1.symm)
        _ = _ := by simp [Finset.card_erase_of_mem hx, Nat.mul_comm]
    dsimp only at h
    omega
  calc
    _ = ∑ _x ∈ S, (7 + 2 * (S.card - 1)) := Finset.sum_congr rfl row
    _ = _ := by simp

theorem cross_moment (H : Simple5Hypergraph V) (A B : Finset V)
    (pairs : ∀ x ∈ A, ∀ y ∈ B, H.codegree x y = 1) :
    (∑ e ∈ H.edges, (e ∩ A).card * (e ∩ B).card) = A.card * B.card := by
  rw [sum_inter_product]
  calc
    _ = ∑ _x ∈ A, B.card := Finset.sum_congr rfl (fun x hx => by
      rw [Finset.sum_congr rfl (fun y hy => pairs x hx y hy)]
      simp)
    _ = _ := by simp

theorem clipped_moment (a b c : ℕ) (total : a + b + c ≤ 5)
    (clipped : min a 2 + min b 2 + min c 2 ≤ 3) :
    a*a + b*b + c*c + 12*(a*b + a*c + b*c) ≤ 13*(a+b+c) := by
  have ha : a ≤ 5 := by omega
  have hb : b ≤ 5 := by omega
  have hc : c ≤ 5 := by omega
  interval_cases a <;> interval_cases b <;> interval_cases c <;> norm_num at *

theorem sizes_moment_contradiction (a b c : ℕ)
    (ha : 5 ≤ a ∧ a ≤ 7) (hb : 5 ≤ b ∧ b ≤ 7) (hc : 5 ≤ c ∧ c ≤ 7)
    (many : 19 ≤ a+b+c) :
    91*(a+b+c) < a*(7+2*(a-1)) + b*(7+2*(b-1)) + c*(7+2*(c-1)) +
      12*(a*b + a*c + b*c) := by
  obtain ⟨ha,ha'⟩ := ha
  obtain ⟨hb,hb'⟩ := hb
  obtain ⟨hc,hc'⟩ := hc
  interval_cases a <;> interval_cases b <;> interval_cases c <;> norm_num at *

/-- The large clipped trace is forced by actual edge-incidence and pair moments. -/
theorem exists_large_clipped_trace (H : Simple5Hypergraph V) (A B C : Finset V)
    (ab : Disjoint A B) (ac : Disjoint A C) (bc : Disjoint B C)
    (degrees : ∀ x ∈ A ∪ B ∪ C, H.degree x = 7)
    (aa : ∀ x ∈ A, ∀ y ∈ A, x ≠ y → H.codegree x y = 2)
    (bb : ∀ x ∈ B, ∀ y ∈ B, x ≠ y → H.codegree x y = 2)
    (cc : ∀ x ∈ C, ∀ y ∈ C, x ≠ y → H.codegree x y = 2)
    (crossAB : ∀ x ∈ A, ∀ y ∈ B, H.codegree x y = 1)
    (crossAC : ∀ x ∈ A, ∀ y ∈ C, H.codegree x y = 1)
    (crossBC : ∀ x ∈ B, ∀ y ∈ C, H.codegree x y = 1)
    (ha : 5 ≤ A.card ∧ A.card ≤ 7) (hb : 5 ≤ B.card ∧ B.card ≤ 7)
    (hc : 5 ≤ C.card ∧ C.card ≤ 7) (many : 19 ≤ A.card+B.card+C.card) :
    ∃ e ∈ H.edges, 4 ≤ min (e ∩ A).card 2 + min (e ∩ B).card 2 +
      min (e ∩ C).card 2 := by
  have da : ∀ x ∈ A, H.degree x = 7 := fun x hx => degrees x (by simp [hx])
  have db : ∀ x ∈ B, H.degree x = 7 := fun x hx => degrees x (by simp [hx])
  have dc : ∀ x ∈ C, H.degree x = 7 := fun x hx => degrees x (by simp [hx])
  have first (S : Finset V) (d : ∀ x ∈ S, H.degree x = 7) :
      (∑ e ∈ H.edges, (e ∩ S).card) = 7*S.card := by
    rw [sum_inter_card, Finset.sum_congr rfl d]
    simp [Nat.mul_comm]
  have total (e : Finset V) (he : e ∈ H.edges) :
      (e ∩ A).card + (e ∩ B).card + (e ∩ C).card ≤ 5 := by
    have hab : Disjoint (e ∩ A) (e ∩ B) := ab.mono Finset.inter_subset_right Finset.inter_subset_right
    have hac : Disjoint (e ∩ A) (e ∩ C) := ac.mono Finset.inter_subset_right Finset.inter_subset_right
    have hbc : Disjoint (e ∩ B) (e ∩ C) := bc.mono Finset.inter_subset_right Finset.inter_subset_right
    have hh := Finset.card_le_card (show (e ∩ A) ∪ (e ∩ B) ∪ (e ∩ C) ⊆ e by
      intro x hx
      rcases Finset.mem_union.mp hx with hx | hx
      · rcases Finset.mem_union.mp hx with hx | hx
        · exact (Finset.mem_inter.mp hx).1
        · exact (Finset.mem_inter.mp hx).1
      · exact (Finset.mem_inter.mp hx).1)
    rw [Finset.card_union_of_disjoint (Finset.disjoint_union_left.mpr ⟨hac,hbc⟩),
      Finset.card_union_of_disjoint hab, H.five_uniform e he] at hh
    exact hh
  by_contra hn
  have small (e : Finset V) (he : e ∈ H.edges) :
      min (e ∩ A).card 2 + min (e ∩ B).card 2 + min (e ∩ C).card 2 ≤ 3 := by
    have : ¬4 ≤ min (e ∩ A).card 2 + min (e ∩ B).card 2 + min (e ∩ C).card 2 :=
      fun h => hn ⟨e,he,h⟩
    omega
  have summed := Finset.sum_le_sum (s := H.edges) (fun e he =>
    clipped_moment _ _ _ (total e he) (small e he))
  simp only [Finset.sum_add_distrib, ← Finset.mul_sum] at summed
  rw [clique_square_moment H A da aa, clique_square_moment H B db bb,
    clique_square_moment H C dc cc, cross_moment H A B crossAB,
    cross_moment H A C crossAC, cross_moment H B C crossBC,
    first A da, first B db, first C dc] at summed
  have bad := sizes_moment_contradiction A.card B.card C.card ha hb hc many
  omega

end Aris4Math.ThirtyThree.TwentyThreeClusterMoments
