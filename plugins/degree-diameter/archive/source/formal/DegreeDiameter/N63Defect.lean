import DegreeDiameter.Defect
import Mathlib.Combinatorics.SimpleGraph.Matching
import Mathlib.Algebra.Polynomial.AlgebraMap

namespace DegreeDiameter

open scoped BigOperators
open Matrix Polynomial
attribute [local instance] Classical.propDecidable
noncomputable section

/-- The integer Chebyshev recurrence adapted to `P + P⁻¹`. -/
def n63Chebyshev : ℕ → Polynomial ℤ
  | 0 => 2
  | 1 => X
  | n + 2 => X * n63Chebyshev (n + 1) - n63Chebyshev n

/-- Each factor retains its own cycle length, at most 63. -/
def n63Annihilator : Polynomial ℤ :=
  ∏ k ∈ Finset.range 63, (n63Chebyshev (k + 1) - 2)

variable {V : Type*} [Fintype V]

/-- A nonnegative integer row of total weight two has exactly two unit contributions,
possibly at the same position. -/
theorem n63_row_two_classification (f : V → ℤ) (hnonneg : ∀ v, 0 ≤ f v)
    (hsum : ∑ v, f v = 2) :
    (∃ v, f v = 2 ∧ ∀ w, w ≠ v → f w = 0) ∨
    (∃ v w, v ≠ w ∧ f v = 1 ∧ f w = 1 ∧ ∀ x, x ≠ v → x ≠ w → f x = 0) := by
  classical
  have hpos : 0 < ∑ v, f v := by omega
  obtain ⟨v, _, hv⟩ := (Finset.sum_pos_iff_of_nonneg (fun x _ => hnonneg x)).mp hpos
  have hvle : f v ≤ 2 := by
    calc f v ≤ ∑ x, f x := Finset.single_le_sum (fun x _ => hnonneg x) (Finset.mem_univ v)
         _ = 2 := hsum
  have herase : ∑ x ∈ Finset.univ.erase v, f x = 2 - f v := by
    have := Finset.sum_erase_add (s := Finset.univ) f (Finset.mem_univ v)
    omega
  by_cases hv2 : f v = 2
  · left
    refine ⟨v, hv2, fun w hw => ?_⟩
    have hwle : f w ≤ ∑ x ∈ Finset.univ.erase v, f x :=
      Finset.single_le_sum (fun x _ => hnonneg x) (by simp [hw])
    have := hnonneg w
    omega
  · have hv1 : f v = 1 := by omega
    have herasepos : 0 < ∑ x ∈ Finset.univ.erase v, f x := by omega
    obtain ⟨w, hwmem, hwpos⟩ :=
      (Finset.sum_pos_iff_of_nonneg (fun x _ => hnonneg x)).mp herasepos
    have hwv : w ≠ v := (Finset.mem_erase.mp hwmem).1
    have hwle : f w ≤ ∑ x ∈ Finset.univ.erase v, f x :=
      Finset.single_le_sum (fun x _ => hnonneg x) hwmem
    have hw1 : f w = 1 := by omega
    right
    refine ⟨v, w, hwv.symm, hv1, hw1, fun x hxv hxw => ?_⟩
    have herase2 := Finset.sum_erase_add (s := Finset.univ.erase v) f hwmem
    have hxle : f x ≤ ∑ y ∈ (Finset.univ.erase v).erase w, f y :=
      Finset.single_le_sum (fun y _ => hnonneg y) (by simp [hxv, hxw])
    have := hnonneg x
    omega

/-- The original graph hypotheses give the exact row-two condition. -/
theorem n63_original_defect_row_sum (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 63) (u : V) : ∑ v, defectMatrix G u v = 2 := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  simpa [hcard] using defect_row_sum G hreg u

/-- The ordinary support contains exactly the defect entries of weight one. -/
def n63UnitDefectGraph (G : SimpleGraph V) (hreg : G.IsRegularOfDegree 8) : SimpleGraph V where
  Adj u v := defectMatrix G u v = 1
  symm := by
    intro u v huv
    exact (defect_symmetric G).apply u v ▸ huv
  loopless := by
    intro v h
    rw [defect_diagonal G hreg] at h
    omega

/-- An entry two uses the entire row: all other entries are zero. -/
theorem n63_doubled_edge_isolated (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 63) {u v : V} (huv : defectMatrix G u v = 2) :
    u ≠ v ∧ defectMatrix G v u = 2 ∧
      (∀ w, w ≠ v → defectMatrix G u w = 0) ∧
      (∀ w, w ≠ u → defectMatrix G v w = 0) := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hnonneg := defect_nonnegative G hreg hdiam
  have hsymm := (defect_symmetric G).apply
  have hisolate : ∀ a b, defectMatrix G a b = 2 →
      ∀ w, w ≠ b → defectMatrix G a w = 0 := by
    intro a b hab w hwb
    obtain (⟨v', hv', hzero⟩ | ⟨v', w', hvw, hv', hw', hzero⟩) :=
      n63_row_two_classification (defectMatrix G a) (hnonneg a)
        (n63_original_defect_row_sum G hdeg hdiam hcard a)
    · by_cases hb : b = v'
      · exact hzero w (by simpa [hb] using hwb)
      · have := hzero b hb
        omega
    · by_cases hb : b = v'
      · subst b; omega
      · by_cases hb' : b = w'
        · subst b; omega
        · have := hzero b hb hb'; omega
  have hvu : defectMatrix G v u = 2 := (hsymm u v).trans huv
  refine ⟨?_, hvu, hisolate u v huv, hisolate v u hvu⟩
  intro heq
  subst v
  rw [defect_diagonal G hreg] at huv
  omega

/-- After isolated doubled edges are discarded, the actual defect support is a union of cycles. -/
theorem n63_unit_defect_isCycles (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 63)
    (hreg : G.IsRegularOfDegree 8) : (n63UnitDefectGraph G hreg).IsCycles := by
  intro u ⟨v, huv⟩
  change defectMatrix G u v = 1 at huv
  obtain (⟨w, hw, hzero⟩ | ⟨v', w', hvw, hv', hw', hzero⟩) :=
    n63_row_two_classification (defectMatrix G u) (defect_nonnegative G hreg hdiam u)
      (n63_original_defect_row_sum G hdeg hdiam hcard u)
  · by_cases hvw : v = w
    · subst v; omega
    · have := hzero v hvw; omega
  · apply Set.ncard_eq_two.mpr
    refine ⟨v', w', hvw, ?_⟩
    ext x
    change defectMatrix G u x = 1 ↔ x ∈ ({v', w'} : Set V)
    simp only [Set.mem_insert_iff, Set.mem_singleton_iff]
    constructor
    · intro hx
      by_cases hxv : x = v'
      · exact Or.inl hxv
      · right
        by_contra hxw
        have := hzero x hxv hxw
        omega
    · rintro (rfl | rfl) <;> assumption

/-- A simple cycle visits at most the vertices of the ambient finite type. -/
theorem n63_cycle_length_le_card {H : SimpleGraph V} {u : V} (p : H.Walk u u)
    (hp : p.IsCycle) : p.length ≤ Fintype.card V := by
  have hinj : Function.Injective (fun i : Fin p.length => p.getVert i.val) := by
    intro i j hij
    apply Fin.ext
    exact hp.getVert_injOn' (by simp only [Set.mem_setOf_eq]; omega)
      (by simp only [Set.mem_setOf_eq]; omega) hij
  simpa using Fintype.card_le_of_injective _ hinj

/-- Every nondoubled defect component is witnessed by an actual simple closed walk;
the bound on its length is the original graph cardinality, rather than an lcm bound. -/
theorem n63_unit_defect_component_cycle (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 63) (hreg : G.IsRegularOfDegree 8)
    {u v : V} (huv : defectMatrix G u v = 1) :
    ∃ p : (n63UnitDefectGraph G hreg).Walk u u,
      p.IsCycle ∧ 3 ≤ p.length ∧ p.length ≤ 63 ∧
      p.toSubgraph.verts = ((n63UnitDefectGraph G hreg).connectedComponentMk u).supp := by
  have hcycles := n63_unit_defect_isCycles G hdeg hdiam hcard hreg
  obtain ⟨p, hp, hverts⟩ :=
    hcycles.exists_cycle_toSubgraph_verts_eq_connectedComponentSupp
      (c := (n63UnitDefectGraph G hreg).connectedComponentMk u) (by rfl) ⟨v, huv⟩
  exact ⟨p, hp, hp.three_le_length, by simpa [hcard] using n63_cycle_length_le_card p hp,
    hverts⟩

/-- Two distinct unit entries exhaust a nonnegative integer row of sum two. -/
theorem n63_row_eq_two_units (f : V → ℤ) (hnonneg : ∀ v, 0 ≤ f v)
    (hsum : ∑ v, f v = 2) {v w : V} (hvw : v ≠ w) (hv : f v = 1) (hw : f w = 1) :
    f = Pi.single v 1 + Pi.single w 1 := by
  classical
  have herase := Finset.sum_erase_add (s := Finset.univ) f (Finset.mem_univ v)
  have herase2 := Finset.sum_erase_add (s := Finset.univ.erase v) f
    (by simp [hvw.symm] : w ∈ Finset.univ.erase v)
  funext x
  by_cases hxv : x = v
  · subst x
    simp [hv, hvw]
  by_cases hxw : x = w
  · subst x
    simp [hw, hvw.symm]
  have hxle : f x ≤ ∑ y ∈ (Finset.univ.erase v).erase w, f y :=
    Finset.single_le_sum (fun y _ => hnonneg y) (by simp [hxv, hxw])
  have hxnonneg := hnonneg x
  have hxzero : f x = 0 := by omega
  simp [hxzero, hxv, hxw]

/-- The defect matrix acts along the two ordinary neighbors of a vertex. -/
theorem n63_defect_mulVec_two_units (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 63) {u v w : V} (hvw : v ≠ w)
    (huv : defectMatrix G u v = 1) (huw : defectMatrix G u w = 1) :
    defectMatrix G *ᵥ Pi.single u 1 = Pi.single v 1 + Pi.single w 1 := by
  classical
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hrow := n63_row_eq_two_units (defectMatrix G u)
    (defect_nonnegative G hreg hdiam u)
    (n63_original_defect_row_sum G hdeg hdiam hcard u) hvw huv huw
  ext x
  rw [Matrix.mulVec_single_one]
  exact ((defect_symmetric G).apply u x).trans (congrFun hrow x)

/-- At an internal cycle vertex the matrix has precisely the predecessor and successor columns. -/
theorem n63_cycle_mulVec_step (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 63) (hreg : G.IsRegularOfDegree 8)
    {u : V} (p : (n63UnitDefectGraph G hreg).Walk u u) (hp : p.IsCycle)
    {i : ℕ} (hi : 1 ≤ i) (hi' : i < p.length) :
    defectMatrix G *ᵥ Pi.single (p.getVert i) 1 =
      Pi.single (p.getVert (i - 1)) 1 + Pi.single (p.getVert (i + 1)) 1 := by
  apply n63_defect_mulVec_two_units G hdeg hdiam hcard
    (hp.getVert_sub_one_ne_getVert_add_one hi'.le)
  · have hadj := p.adj_getVert_succ (i := i - 1) (by omega)
    have hadj' : (n63UnitDefectGraph G hreg).Adj (p.getVert (i - 1)) (p.getVert i) := by
      simpa [Nat.sub_add_cancel hi] using hadj
    exact hadj'.symm
  · exact p.adj_getVert_succ hi'

/-- The initial matrix step sees the forward and backward first vertices. -/
theorem n63_cycle_mulVec_start (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 63) (hreg : G.IsRegularOfDegree 8)
    {u : V} (p : (n63UnitDefectGraph G hreg).Walk u u) (hp : p.IsCycle) :
    defectMatrix G *ᵥ Pi.single u 1 =
      Pi.single (p.getVert 1) 1 + Pi.single (p.reverse.getVert 1) 1 := by
  apply n63_defect_mulVec_two_units G hdeg hdiam hcard
  · change p.snd ≠ p.reverse.snd
    simpa only [SimpleGraph.Walk.snd_reverse] using hp.snd_ne_penultimate
  · exact SimpleGraph.Walk.adj_snd hp.not_nil
  · exact SimpleGraph.Walk.adj_snd hp.reverse.not_nil

/-- Chebyshev evaluation propagates once in each direction along an actual defect cycle. -/
theorem n63_chebyshev_cycle_mulVec (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 63) (hreg : G.IsRegularOfDegree 8)
    {u : V} (p : (n63UnitDefectGraph G hreg).Walk u u) (hp : p.IsCycle) :
    ∀ n, n ≤ p.length →
      (aeval (defectMatrix G) (n63Chebyshev n)) *ᵥ Pi.single u 1 =
        Pi.single (p.getVert n) 1 + Pi.single (p.reverse.getVert n) 1 := by
  classical
  apply Nat.twoStepInduction
  · intro _
    simp only [n63Chebyshev, map_ofNat, SimpleGraph.Walk.getVert_zero]
    rw [show (2 : Matrix V V ℤ) = 1 + 1 by norm_num, Matrix.add_mulVec,
      Matrix.one_mulVec]
  · intro _
    simpa only [n63Chebyshev, aeval_X] using
      n63_cycle_mulVec_start G hdeg hdiam hcard hreg p hp
  · intro n hn hn1 hn2
    rw [n63Chebyshev, map_sub, map_mul, aeval_X, Matrix.sub_mulVec,
      ← Matrix.mulVec_mulVec, hn1 (by omega), hn (by omega), Matrix.mulVec_add,
      n63_cycle_mulVec_step G hdeg hdiam hcard hreg p hp (by omega) (by omega),
      n63_cycle_mulVec_step G hdeg hdiam hcard hreg p.reverse hp.reverse (by omega)
        (by simpa using (show n + 1 < p.length by omega))]
    simp only [Nat.add_sub_cancel]
    abel

/-- The factor indexed by the genuine cycle length kills the starting basis vector. -/
theorem n63_cycle_factor_mulVec_zero (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 63) (hreg : G.IsRegularOfDegree 8)
    {u : V} (p : (n63UnitDefectGraph G hreg).Walk u u) (hp : p.IsCycle) :
    (aeval (defectMatrix G) (n63Chebyshev p.length - 2)) *ᵥ Pi.single u 1 = 0 := by
  classical
  rw [map_sub, Matrix.sub_mulVec, n63_chebyshev_cycle_mulVec G hdeg hdiam hcard hreg p hp
    p.length le_rfl]
  simp only [SimpleGraph.Walk.getVert_length, ← SimpleGraph.Walk.length_reverse p,
    SimpleGraph.Walk.getVert_length, map_ofNat]
  rw [show (2 : Matrix V V ℤ) = 1 + 1 by norm_num, Matrix.add_mulVec, Matrix.one_mulVec]
  simp only [SimpleGraph.Walk.length_reverse, SimpleGraph.Walk.getVert_length, sub_self]

/-- A doubled edge sends the basis vector to twice its unique partner. -/
theorem n63_doubled_edge_mulVec (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 63) {u v : V} (huv : defectMatrix G u v = 2) :
    defectMatrix G *ᵥ Pi.single u 1 = Pi.single v 1 + Pi.single v 1 := by
  classical
  have hiso := n63_doubled_edge_isolated G hdeg hdiam hcard huv
  ext x
  rw [Matrix.mulVec_single_one]
  change defectMatrix G x u = _
  rw [(defect_symmetric G).apply u x]
  by_cases hx : x = v
  · subst x
    simp [huv]
  · simp [hiso.2.2.1 x hx, hx]

/-- The length-two factor handles isolated doubled edges. -/
theorem n63_doubled_edge_factor_mulVec_zero (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 63) {u v : V} (huv : defectMatrix G u v = 2) :
    (aeval (defectMatrix G) (n63Chebyshev 2 - 2)) *ᵥ Pi.single u 1 = 0 := by
  classical
  have hvu := (n63_doubled_edge_isolated G hdeg hdiam hcard huv).2.1
  have hstep := n63_doubled_edge_mulVec G hdeg hdiam hcard huv
  have hback := n63_doubled_edge_mulVec G hdeg hdiam hcard hvu
  simp only [n63Chebyshev, map_sub, map_mul, aeval_X, map_ofNat, Matrix.sub_mulVec]
  rw [← Matrix.mulVec_mulVec, hstep, Matrix.mulVec_add, hback,
    show (2 : Matrix V V ℤ) = 1 + 1 by norm_num, Matrix.add_mulVec, Matrix.one_mulVec]
  abel

/-- Each original basis vector is killed by a factor with its actual component length in `2..63`. -/
theorem n63_original_defect_local_factor (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 63) (u : V) :
    ∃ r : ℕ, 2 ≤ r ∧ r ≤ 63 ∧
      (aeval (defectMatrix G) (n63Chebyshev r - 2)) *ᵥ Pi.single u 1 = 0 := by
  classical
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  obtain (⟨v, hv, _⟩ | ⟨v, w, hvw, hv, hw, _⟩) :=
    n63_row_two_classification (defectMatrix G u) (defect_nonnegative G hreg hdiam u)
      (n63_original_defect_row_sum G hdeg hdiam hcard u)
  · exact ⟨2, le_rfl, by omega, n63_doubled_edge_factor_mulVec_zero G hdeg hdiam hcard hv⟩
  · obtain ⟨p, hp, hp3, hp63, _⟩ :=
      n63_unit_defect_component_cycle G hdeg hdiam hcard hreg hv
    exact ⟨p.length, by omega, hp63, n63_cycle_factor_mulVec_zero G hdeg hdiam hcard hreg p hp⟩

/-- The product of all component-length factors annihilates the actual defect matrix.
No permutation, component certificate, or extra spectral assumption is supplied. -/
theorem n63_original_defect_annihilator (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 63) : aeval (defectMatrix G) n63Annihilator = 0 := by
  classical
  apply Matrix.ext_of_mulVec_single
  intro u
  obtain ⟨r, hr2, hr63, hr⟩ := n63_original_defect_local_factor G hdeg hdiam hcard u
  have hdiv : n63Chebyshev r - 2 ∣ n63Annihilator := by
    unfold n63Annihilator
    have hmem : r - 1 ∈ Finset.range 63 := Finset.mem_range.mpr (by omega)
    simpa [Nat.sub_add_cancel (by omega : 1 ≤ r)] using
      (Finset.dvd_prod_of_mem (fun k => n63Chebyshev (k + 1) - 2) hmem)
  obtain ⟨q, hq⟩ := hdiv
  rw [hq, mul_comm, map_mul, ← Matrix.mulVec_mulVec, hr, Matrix.mulVec_zero,
    Matrix.zero_mulVec]

end
end DegreeDiameter
