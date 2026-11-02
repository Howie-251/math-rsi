import Mathlib

/-
DRAFT / NOT KERNEL CHECKED.  N59_MANUAL12_ACTIVE, same research round.
This is the graph-semantic commutator step used in THEORY_WORKING §9.3.
It does not assert that an arbitrary graph has the P16 partition.  The
unique-common-neighbour and support hypotheses must be supplied from the
actual P-core/B definitions as described in the mathematical proof.
No historical RAW is verified here.  No toolchain was available locally.
-/
namespace N59TriangleTransport

variable {V : Type*} [Fintype V] [DecidableEq V]

noncomputable def a (G : SimpleGraph V) (x y : V) : ℤ := by
  classical
  exact if G.Adj x y then 1 else 0

/-- Actual N59 repeat matrix, including the diagonal correction. -/
noncomputable def repeatWeight (G : SimpleGraph V) (x y : V) : ℤ := by
  classical
  exact (∑ z : V, a G x z * a G z y) + a G x y
    - 7 * (if x = y then 1 else 0) - 1

/-- Once the only common A-neighbour has zero B-weight in the r-row,
    the entire commutator contribution must come from NON-neighbours of r. -/
theorem triangle_shadow_transport
    (G : SimpleGraph V) (B : V → V → ℤ)
    (hB : ∀ x y, 0 ≤ B x y)
    (hcomm : ∀ x y, (∑ z : V, a G x z * B z y) =
      ∑ z : V, B x z * a G z y)
    (r c e : V) (hrc : G.Adj r c) (hce : 1 ≤ B c e)
    (hcommon : ∀ w, G.Adj r w → G.Adj w e → w = c)
    (hrc0 : B r c = 0) :
    1 ≤ ∑ w : V, if ¬ G.Adj r w then B r w * a G w e else 0 := by
  classical
  have hnonneg (w : V) : 0 ≤ a G r w * B w e := by
    exact mul_nonneg (by unfold a; split_ifs <;> norm_num) (hB w e)
  have hterm : a G r c * B c e ≤ ∑ w : V, a G r w * B w e := by
    exact Finset.single_le_sum (fun w _ => hnonneg w) (Finset.mem_univ c)
  have hleft : 1 ≤ ∑ w : V, a G r w * B w e := by
    have ht : a G r c * B c e = B c e := by simp [a, hrc]
    rw [ht] at hterm
    exact le_trans hce hterm
  have hrestrict : (∑ w : V, B r w * a G w e) =
      ∑ w : V, if ¬ G.Adj r w then B r w * a G w e else 0 := by
    apply Finset.sum_congr rfl
    intro w hw
    by_cases hrw : G.Adj r w
    · by_cases hwe : G.Adj w e
      · have heq : w = c := hcommon w hrw hwe
        subst w
        simp [hrc0, hrc]
      · simp [a, hrw, hwe]
    · simp [hrw]
  rw [hcomm r e, hrestrict] at hleft
  exact hleft

/-- A graph-theoretic contradiction, not merely a numerical example:
    every possible non-neighbour repeat support avoids e. -/
theorem impossible_shadow_avoidance
    (G : SimpleGraph V) (B : V → V → ℤ)
    (hB : ∀ x y, 0 ≤ B x y)
    (hcomm : ∀ x y, (∑ z : V, a G x z * B z y) =
      ∑ z : V, B x z * a G z y)
    (r c e : V) (hrc : G.Adj r c) (hce : 1 ≤ B c e)
    (hcommon : ∀ w, G.Adj r w → G.Adj w e → w = c)
    (hrc0 : B r c = 0)
    (havoid : ∀ w, ¬ G.Adj r w → B r w = 0 ∨ ¬ G.Adj w e) : False := by
  classical
  have hh := triangle_shadow_transport G B hB hcomm r c e hrc hce hcommon hrc0
  have hz : (∑ w : V, if ¬ G.Adj r w then B r w * a G w e else 0) = 0 := by
    apply Finset.sum_eq_zero
    intro w hw
    by_cases hrw : G.Adj r w
    · simp [hrw]
    · rcases havoid w hrw with hb | ha
      · simp [hrw, hb]
      · simp [hrw, a, ha]
  rw [hz] at hh
  norm_num at hh

/-- The t1 application: after the two private R1 supports avoid e,
    a remaining distinguished M-support must really be adjacent to e. -/
theorem distinguished_support_must_meet
    (G : SimpleGraph V) (B : V → V → ℤ)
    (hB : ∀ x y, 0 ≤ B x y)
    (hcomm : ∀ x y, (∑ z : V, a G x z * B z y) =
      ∑ z : V, B x z * a G z y)
    (r c e m : V) (hrc : G.Adj r c) (hce : 1 ≤ B c e)
    (hcommon : ∀ w, G.Adj r w → G.Adj w e → w = c)
    (hrc0 : B r c = 0)
    (havoid : ∀ w, ¬ G.Adj r w → w ≠ m → B r w = 0 ∨ ¬ G.Adj w e) :
    G.Adj m e := by
  classical
  by_contra hme
  apply impossible_shadow_avoidance G B hB hcomm r c e hrc hce hcommon hrc0
  intro w hrw
  by_cases hwm : w = m
  · subst w
    exact Or.inr hme
  · exact havoid w hrw hwm

/-- Explicit binding to the original graph's B, rather than a free matrix. -/
theorem actual_repeat_distinguished_support_must_meet
    (G : SimpleGraph V)
    (hB : ∀ x y, 0 ≤ repeatWeight G x y)
    (hcomm : ∀ x y, (∑ z : V, a G x z * repeatWeight G z y) =
      ∑ z : V, repeatWeight G x z * a G z y)
    (r c e m : V) (hrc : G.Adj r c) (hce : 1 ≤ repeatWeight G c e)
    (hcommon : ∀ w, G.Adj r w → G.Adj w e → w = c)
    (hrc0 : repeatWeight G r c = 0)
    (havoid : ∀ w, ¬ G.Adj r w → w ≠ m →
      repeatWeight G r w = 0 ∨ ¬ G.Adj w e) : G.Adj m e := by
  exact distinguished_support_must_meet G (repeatWeight G) hB hcomm
    r c e m hrc hce hcommon hrc0 havoid

#print axioms triangle_shadow_transport
#print axioms impossible_shadow_avoidance
#print axioms distinguished_support_must_meet
#print axioms actual_repeat_distinguished_support_must_meet

end N59TriangleTransport
