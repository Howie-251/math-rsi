import DegreeDiameter.N62RepeatComponents
import Mathlib.Combinatorics.SimpleGraph.Connectivity.WalkCounting

namespace DegreeDiameter
open Matrix
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section
variable {V : Type*} [Fintype V]

/-- Actual cardinality of a repeat-support component. -/
def repeatComponentSize (G : SimpleGraph V) (C : (repeatSupport G).ConnectedComponent) : ℕ :=
  (repeatComponentVertices G C).card

/-- Actual vertex/component membership matrix. -/
def repeatMembershipMatrix (G : SimpleGraph V) :
    Matrix V (repeatSupport G).ConnectedComponent ℤ :=
  fun x C => repeatComponentIndicator G C x

/-- The rank-one matrix whose column C is the actual size of C. -/
def repeatSizeMatrix (G : SimpleGraph V) :
    Matrix (repeatSupport G).ConnectedComponent (repeatSupport G).ConnectedComponent ℤ :=
  fun _ C => (repeatComponentSize G C : ℤ)

/-- Multiplying by actual component membership evaluates a component
matrix at the unique component containing the vertex. -/
theorem repeat_membership_mul (G : SimpleGraph V)
    (M : Matrix (repeatSupport G).ConnectedComponent (repeatSupport G).ConnectedComponent ℤ)
    (x : V) (C : (repeatSupport G).ConnectedComponent) :
    (repeatMembershipMatrix G * M) x C = M ((repeatSupport G).connectedComponentMk x) C := by
  simp [Matrix.mul_apply,repeatMembershipMatrix,repeatComponentIndicator,
    SimpleGraph.ConnectedComponent.mem_supp_iff,ite_mul]

/-- Each actual vertex belongs to exactly one repeat component. -/
theorem repeat_component_indicator_sum (G : SimpleGraph V) (x : V) :
    ∑ C : (repeatSupport G).ConnectedComponent, repeatComponentIndicator G C x = 1 := by
  simp [repeatComponentIndicator,SimpleGraph.ConnectedComponent.mem_supp_iff]

/-- Summing the actual indicator gives the actual component size. -/
theorem repeat_component_indicator_card (G : SimpleGraph V)
    (C : (repeatSupport G).ConnectedComponent) :
    ∑ x, repeatComponentIndicator G C x = (repeatComponentSize G C : ℤ) := by
  simp [repeatComponentIndicator,repeatComponentSize,repeatComponentVertices]

/-- The actual adjacency/membership intertwining identity realizes the
constructed quotient, without any supplied equitable matrix. -/
theorem n62_adjacency_repeat_membership (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) :
    adjacencyMatrix G * repeatMembershipMatrix G =
      repeatMembershipMatrix G * repeatQuotientMatrix G := by
  ext x C
  rw [repeat_membership_mul]
  have hA := congrFun (adjacency_mul_repeat_indicator G C) x
  have hx : x ∈ ((repeatSupport G).connectedComponentMk x).supp := rfl
  have hd := n62_repeat_component_degree_spec G hdeg hdiam hcard _ C hx
  exact hA.trans (congrArg (fun n : ℕ => (n : ℤ)) hd)

/-- The actual B action on the membership columns is scalar three. -/
theorem n62_defect_repeat_membership (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) :
    defectMatrix G * repeatMembershipMatrix G = (3 : ℤ) • repeatMembershipMatrix G := by
  ext x C
  exact n62_repeat_component_indicator_harmonic G hdeg hdiam hcard C x

private theorem ones_repeat_membership (G : SimpleGraph V) :
    (onesMatrix : Matrix V V ℤ) * repeatMembershipMatrix G =
      repeatMembershipMatrix G * repeatSizeMatrix G := by
  ext x C
  rw [repeat_membership_mul]
  simpa [Matrix.mul_apply,onesMatrix,repeatMembershipMatrix,repeatSizeMatrix] using
    repeat_component_indicator_card G C

/-- The actual quotient satisfies R²+R=10I+1 nᵀ, with n the actual
component-size vector. Only original graph hypotheses are used. -/
theorem n62_repeat_quotient_quadratic (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) :
    repeatQuotientMatrix G * repeatQuotientMatrix G + repeatQuotientMatrix G =
      (10 : ℤ) • (1 : Matrix (repeatSupport G).ConnectedComponent
        (repeatSupport G).ConnectedComponent ℤ) + repeatSizeMatrix G := by
  have hAS := n62_adjacency_repeat_membership G hdeg hdiam hcard
  have hBS := n62_defect_repeat_membership G hdeg hdiam hcard
  have hAAS : (adjacencyMatrix G * adjacencyMatrix G) * repeatMembershipMatrix G =
      repeatMembershipMatrix G * (repeatQuotientMatrix G * repeatQuotientMatrix G) := by
    rw [Matrix.mul_assoc,hAS,← Matrix.mul_assoc,hAS,Matrix.mul_assoc]
  have hexp : defectMatrix G * repeatMembershipMatrix G =
      repeatMembershipMatrix G * (repeatQuotientMatrix G * repeatQuotientMatrix G + repeatQuotientMatrix G) -
      (7 : ℤ) • repeatMembershipMatrix G - repeatMembershipMatrix G * repeatSizeMatrix G := by
    rw [defectMatrix,Matrix.sub_mul,Matrix.sub_mul,Matrix.add_mul,hAAS,hAS,Matrix.smul_mul,Matrix.one_mul,
      ones_repeat_membership,Matrix.mul_add]
  rw [hexp] at hBS
  ext D C
  obtain ⟨x,hx⟩ := D.nonempty_supp
  have hxD : (repeatSupport G).connectedComponentMk x = D := hx
  have hh := congrArg (fun M => M x C) hBS
  dsimp only at hh
  simp only [Matrix.sub_apply,Matrix.add_apply,Matrix.smul_apply,smul_eq_mul,repeat_membership_mul,
    repeatMembershipMatrix,repeatComponentIndicator,SimpleGraph.ConnectedComponent.mem_supp_iff,hxD] at hh
  simp only [Matrix.add_apply,Matrix.smul_apply,smul_eq_mul,Matrix.one_apply]
  omega

/-- The actual quotient has row sum eight. -/
theorem n62_repeat_quotient_row_sum (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (D : (repeatSupport G).ConnectedComponent) :
    ∑ C, repeatQuotientMatrix G D C = 8 := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  obtain ⟨x,hx⟩ := D.nonempty_supp
  have hxD : (repeatSupport G).connectedComponentMk x = D := hx
  have hrow : ∑ y, adjacencyMatrix G x y = 8 := by
    have hh := congrArg (fun M => M x x) (adjacency_mul_ones G hreg)
    simpa [Matrix.mul_apply,onesMatrix] using hh
  have he (C : (repeatSupport G).ConnectedComponent) : repeatQuotientMatrix G D C =
      ∑ y, adjacencyMatrix G x y * repeatComponentIndicator G C y := by
    have hh := congrArg (fun M => M x C) (n62_adjacency_repeat_membership G hdeg hdiam hcard)
    dsimp only at hh
    rw [repeat_membership_mul,hxD] at hh
    exact hh.symm
  calc
    _ = ∑ C, ∑ y, adjacencyMatrix G x y * repeatComponentIndicator G C y := by
      apply Finset.sum_congr rfl
      intro C _
      exact he C
    _ = ∑ y, adjacencyMatrix G x y * (∑ C, repeatComponentIndicator G C y) := by
      rw [Finset.sum_comm]
      simp only [Finset.mul_sum]
    _ = 8 := by simp [repeat_component_indicator_sum,hrow]

/-- The actual repeat components partition all 62 original vertices. -/
theorem n62_repeat_component_sizes_sum (G : SimpleGraph V)
    (hcard : Fintype.card V = 62) :
    ∑ C : (repeatSupport G).ConnectedComponent, repeatComponentSize G C = 62 := by
  have hh : (∑ C : (repeatSupport G).ConnectedComponent, (repeatComponentSize G C : ℤ)) = 62 := by
    simp_rw [← repeat_component_indicator_card G]
    rw [Finset.sum_comm]
    simp [repeat_component_indicator_sum,hcard]
  exact_mod_cast hh


private theorem component_balance_double_sum (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (D C : (repeatSupport G).ConnectedComponent) :
    (repeatComponentSize G D : ℤ) * repeatQuotientMatrix G D C =
      ∑ x, ∑ y, repeatComponentIndicator G D x * adjacencyMatrix G x y *
        repeatComponentIndicator G C y := by
  rw [← repeat_component_indicator_card,Finset.sum_mul]
  apply Finset.sum_congr rfl
  intro x _
  by_cases hx : x ∈ D.supp
  · have hid : repeatComponentIndicator G D x = 1 := by simp [repeatComponentIndicator,hx]
    simp only [hid,one_mul]
    have hh := congrFun (adjacency_mul_repeat_indicator G C) x
    have he := n62_repeat_component_degree_spec G hdeg hdiam hcard D C hx
    exact (hh.trans (congrArg (fun n : ℕ => (n : ℤ)) he)).symm
  · have hid : repeatComponentIndicator G D x = 0 := by simp [repeatComponentIndicator,hx]
    simp [hid]

/-- Actual undirected G edges between two repeat components can be counted
from either end, giving the quotient balance identity. -/
theorem n62_repeat_quotient_balance (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (D C : (repeatSupport G).ConnectedComponent) :
    (repeatComponentSize G D : ℤ) * repeatQuotientMatrix G D C =
      (repeatComponentSize G C : ℤ) * repeatQuotientMatrix G C D := by
  rw [component_balance_double_sum G hdeg hdiam hcard D C,
    component_balance_double_sum G hdeg hdiam hcard C D]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro x _
  apply Finset.sum_congr rfl
  intro y _
  have hs : adjacencyMatrix G y x = adjacencyMatrix G x y := by
    simp [adjacencyMatrix,SimpleGraph.adj_comm]
  rw [hs]
  ring

/-- Each actual quotient entry is a nonnegative integer. -/
theorem repeat_quotient_nonnegative (G : SimpleGraph V)
    (D C : (repeatSupport G).ConnectedComponent) : 0 ≤ repeatQuotientMatrix G D C := by
  exact Int.natCast_nonneg _

/-- Actual connected components have positive actual cardinality. -/
theorem repeat_component_size_pos (G : SimpleGraph V)
    (C : (repeatSupport G).ConnectedComponent) : 0 < repeatComponentSize G C := by
  obtain ⟨x,hx⟩ := C.nonempty_supp
  exact Finset.card_pos.mpr ⟨x,(mem_repeatComponentVertices G C x).mpr hx⟩

end
end DegreeDiameter
