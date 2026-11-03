import DegreeDiameter.Defect
import Mathlib.Tactic.Ring
import Mathlib.Algebra.Order.Ring.Int
import Mathlib.Combinatorics.SimpleGraph.Connectivity.Connected

namespace DegreeDiameter
open Matrix
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section
variable {V : Type*} [Fintype V]

/-- The actual positive support of the defect matrix, with its diagonal
removed to define a simple graph for every input. For legal order62 graphs
the diagonal is zero, so adjacency is exactly positivity of the actual defect. -/
def repeatSupport (G : SimpleGraph V) : SimpleGraph V where
  Adj x y := x ≠ y ∧ 0 < defectMatrix G x y
  symm := by
    intro x y h
    refine ⟨h.1.symm,?_⟩
    rw [(defect_symmetric G).apply x y]
    exact h.2
  loopless := by intro x h; exact h.1 rfl

/-- The loop-free support definition agrees exactly with actual positive
entries once regularity has been derived from the original graph. -/
theorem n62_repeat_support_adj_iff (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (x y : V) :
    (repeatSupport G).Adj x y ↔ 0 < defectMatrix G x y := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  constructor
  · exact And.right
  · intro hh
    refine ⟨?_,hh⟩
    intro heq
    subst y
    rw [defect_diagonal G hreg] at hh
    omega

/-- A finite symmetric nonnegative integer matrix of constant row sum
has only constant-on-positive-edges integer vectors at its row-sum eigenvalue. -/
theorem integer_weighted_harmonic_edge_eq (B : Matrix V V ℤ) (k : ℤ) (f : V → ℤ)
    (h0 : ∀ x y, 0 ≤ B x y) (hsym : ∀ x y, B x y = B y x)
    (hrow : ∀ x, ∑ y, B x y = k) (hf : ∀ x, ∑ y, B x y * f y = k * f x)
    {x y : V} (hxy : 0 < B x y) : f x = f y := by
  have hz (u : V) : ∑ v, B u v * f u * (f u - f v) = 0 := by
    calc
      _ = f u * (f u * (∑ v, B u v) - ∑ v, B u v * f v) := by
        simp only [mul_sub,Finset.mul_sum,← Finset.sum_sub_distrib]
        apply Finset.sum_congr rfl
        intro v _
        ring
      _ = 0 := by rw [hrow,hf]; ring
  have htotal : ∑ u, ∑ v, B u v * (f u - f v)^2 = 0 := by
    calc
      _ = ∑ u, ∑ v, (B u v * f u * (f u - f v) + B v u * f v * (f v - f u)) := by
        apply Finset.sum_congr rfl
        intro u _
        apply Finset.sum_congr rfl
        intro v _
        rw [hsym v u]
        ring
      _ = (∑ u, ∑ v, B u v * f u * (f u - f v)) +
          ∑ u, ∑ v, B v u * f v * (f v - f u) := by simp only [Finset.sum_add_distrib]
      _ = 0 := by
        rw [Finset.sum_comm (f := fun u v => B v u * f v * (f v - f u))]
        simp [hz]
  have he0 (u v : V) : 0 ≤ B u v * (f u - f v)^2 := mul_nonneg (h0 u v) (sq_nonneg _)
  have hxsum := (Finset.sum_eq_zero_iff_of_nonneg (fun u _ =>
    Finset.sum_nonneg (fun v _ => he0 u v))).mp htotal x (Finset.mem_univ x)
  have hterm := (Finset.sum_eq_zero_iff_of_nonneg (fun v _ => he0 x v)).mp hxsum y (Finset.mem_univ y)
  have hsquare : (f x - f y)^2 = 0 := (mul_eq_zero.mp hterm).resolve_left (ne_of_gt hxy)
  exact sub_eq_zero.mp (sq_eq_zero_iff.mp hsquare)

/-- Actual B-harmonic integer functions are constant on actual repeat components. -/
theorem n62_repeat_harmonic_constant (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (f : V → ℤ)
    (hf : ∀ x, ∑ y, defectMatrix G x y * f y = 3 * f x)
    {x y : V} (hxy : (repeatSupport G).Reachable x y) : f x = f y := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hrow (u : V) : ∑ v, defectMatrix G u v = 3 := by
    simpa [hcard] using defect_row_sum G hreg u
  have hedge {u v : V} (huv : (repeatSupport G).Adj u v) : f u = f v :=
    integer_weighted_harmonic_edge_eq (defectMatrix G) 3 f
      (defect_nonnegative G hreg hdiam) (fun s t => ((defect_symmetric G).apply s t).symm)
      hrow hf huv.2
  obtain ⟨p⟩ := hxy
  induction p with
  | nil => rfl
  | cons h p ih => exact (hedge h).trans ih

/-- Actual vertices in a repeat-support component, as a finite set. -/
def repeatComponentVertices (G : SimpleGraph V) (C : (repeatSupport G).ConnectedComponent) : Finset V :=
  Finset.univ.filter (fun x => x ∈ C.supp)

@[simp] theorem mem_repeatComponentVertices (G : SimpleGraph V)
    (C : (repeatSupport G).ConnectedComponent) (x : V) :
    x ∈ repeatComponentVertices G C ↔ x ∈ C.supp := by simp [repeatComponentVertices]

/-- Integer indicator of an actual repeat component. -/
def repeatComponentIndicator (G : SimpleGraph V) (C : (repeatSupport G).ConnectedComponent) (x : V) : ℤ :=
  if x ∈ C.supp then 1 else 0

/-- The number of original G-neighbors of a vertex lying in an actual
repeat component. This uses G adjacency, not repeat adjacency. -/
def repeatComponentNeighborCount (G : SimpleGraph V)
    (C : (repeatSupport G).ConnectedComponent) (x : V) : ℕ :=
  ((G.neighborFinset x).filter (fun y => y ∈ C.supp)).card

/-- Component indicators are actual eigenvectors of B with eigenvalue three. -/
theorem n62_repeat_component_indicator_harmonic (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (C : (repeatSupport G).ConnectedComponent) :
    ∀ x, ∑ y, defectMatrix G x y * repeatComponentIndicator G C y =
      3 * repeatComponentIndicator G C x := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hrow (u : V) : ∑ v, defectMatrix G u v = 3 := by
    simpa [hcard] using defect_row_sum G hreg u
  have hterm (x y : V) : defectMatrix G x y * repeatComponentIndicator G C y =
      defectMatrix G x y * repeatComponentIndicator G C x := by
    by_cases hb : defectMatrix G x y = 0
    · simp [hb]
    have hp : 0 < defectMatrix G x y := lt_of_le_of_ne (defect_nonnegative G hreg hdiam x y) (Ne.symm hb)
    have ha := (n62_repeat_support_adj_iff G hdeg hdiam hcard x y).mpr hp
    have hc := C.mem_supp_congr_adj ha
    simp only [repeatComponentIndicator,hc]
  intro x
  calc
    _ = ∑ y, defectMatrix G x y * repeatComponentIndicator G C x :=
      Finset.sum_congr rfl (fun y _ => hterm x y)
    _ = _ := by rw [← Finset.sum_mul,hrow]

/-- Original adjacency applied to a component indicator equals the actual
integer-cast neighbor count into that component. -/
theorem adjacency_mul_repeat_indicator (G : SimpleGraph V)
    (C : (repeatSupport G).ConnectedComponent) :
    adjacencyMatrix G *ᵥ repeatComponentIndicator G C =
      fun x => (repeatComponentNeighborCount G C x : ℤ) := by
  funext x
  simp only [Matrix.mulVec,dotProduct,adjacencyMatrix,SimpleGraph.adjMatrix_apply,
    repeatComponentIndicator,repeatComponentNeighborCount]
  simp_rw [ite_mul,one_mul,zero_mul]
  rw [← Finset.sum_filter]
  have heq : Finset.univ.filter (fun y => G.Adj x y) = G.neighborFinset x := by ext y; simp
  rw [heq]
  simp

/-- Commutation makes the actual original-neighbor count vector B-harmonic. -/
theorem n62_repeat_component_neighbor_count_harmonic (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (C : (repeatSupport G).ConnectedComponent) :
    ∀ x, ∑ y, defectMatrix G x y * (repeatComponentNeighborCount G C y : ℤ) =
      3 * (repeatComponentNeighborCount G C x : ℤ) := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hi : defectMatrix G *ᵥ repeatComponentIndicator G C =
      (3 : ℤ) • repeatComponentIndicator G C := by
    funext x
    exact n62_repeat_component_indicator_harmonic G hdeg hdiam hcard C x
  have heq : defectMatrix G *ᵥ (adjacencyMatrix G *ᵥ repeatComponentIndicator G C) =
      (3 : ℤ) • (adjacencyMatrix G *ᵥ repeatComponentIndicator G C) := by
    rw [Matrix.mulVec_mulVec,← adjacency_defect_commute G hreg,← Matrix.mulVec_mulVec,
      hi,Matrix.mulVec_smul]
  rw [adjacency_mul_repeat_indicator] at heq
  intro x
  exact congrFun heq x

/-- Actual repeat components form an equitable partition for original G:
vertices in the same repeat component have equal original-neighbor counts
into every chosen repeat component. No quotient certificate is assumed. -/
theorem n62_repeat_components_equitable (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (C D : (repeatSupport G).ConnectedComponent)
    {x y : V} (hx : x ∈ D.supp) (hy : y ∈ D.supp) :
    repeatComponentNeighborCount G C x = repeatComponentNeighborCount G C y := by
  have hh := n62_repeat_harmonic_constant G hdeg hdiam hcard
    (fun v => (repeatComponentNeighborCount G C v : ℤ))
    (n62_repeat_component_neighbor_count_harmonic G hdeg hdiam hcard C)
    (D.reachable_of_mem_supp hx hy)
  exact Int.ofNat.inj hh


/-- The actual original-graph degree from one repeat component into another.
A representative is chosen only to define the value; the theorem below
proves that every vertex in the source component gives this same value. -/
def repeatComponentDegree (G : SimpleGraph V)
    (D C : (repeatSupport G).ConnectedComponent) : ℕ :=
  repeatComponentNeighborCount G C D.nonempty_supp.choose

/-- The actual integer quotient matrix induced by the repeat components. -/
def repeatQuotientMatrix (G : SimpleGraph V) :
    Matrix (repeatSupport G).ConnectedComponent (repeatSupport G).ConnectedComponent ℤ :=
  fun D C => (repeatComponentDegree G D C : ℤ)

/-- Every actual vertex realizes the constructed quotient entry. -/
theorem n62_repeat_component_degree_spec (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (D C : (repeatSupport G).ConnectedComponent)
    {x : V} (hx : x ∈ D.supp) :
    repeatComponentNeighborCount G C x = repeatComponentDegree G D C := by
  exact n62_repeat_components_equitable G hdeg hdiam hcard C D hx D.nonempty_supp.choose_spec

/-- In particular, every actual repeat component has constant original
internal degree, with the concrete degree given by the quotient diagonal. -/
theorem n62_repeat_component_internal_degree (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (C : (repeatSupport G).ConnectedComponent) :
    ∀ x ∈ C.supp, ((G.neighborFinset x).filter (fun y => y ∈ C.supp)).card =
      repeatComponentDegree G C C := by
  intro x hx
  exact n62_repeat_component_degree_spec G hdeg hdiam hcard C C hx

end
end DegreeDiameter
