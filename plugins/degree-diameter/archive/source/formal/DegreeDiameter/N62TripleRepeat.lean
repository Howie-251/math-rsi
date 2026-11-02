import DegreeDiameter.N62TriangleMate
import DegreeDiameter.N62RepeatQuotient

namespace DegreeDiameter
open Matrix
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section
variable {V : Type*} [Fintype V]

/-- The actual finite set of common original-graph neighbors. -/
def commonNeighborVertices (G : SimpleGraph V) (u v : V) : Finset V :=
  (G.neighborFinset u).filter (fun x => G.Adj x v)

@[simp] theorem mem_commonNeighborVertices (G : SimpleGraph V) (u v x : V) :
    x ∈ commonNeighborVertices G u v ↔ G.Adj u x ∧ G.Adj v x := by
  simp [commonNeighborVertices,SimpleGraph.adj_comm]

private theorem saturated_single_row (f : V → ℤ) (h0 : ∀ x, 0 ≤ f x)
    (hs : ∑ x, f x = 3) {v : V} (hv : f v = 3) :
    ∀ x, f x = if x = v then 3 else 0 := by
  have he := Finset.sum_erase_add (s := Finset.univ) f (Finset.mem_univ v)
  have hz : ∑ x ∈ Finset.univ.erase v, f x = 0 := by omega
  intro x
  by_cases hx : x = v
  · simpa [hx] using hv
  simp only [hx,if_false]
  exact (Finset.sum_eq_zero_iff_of_nonneg (fun y _ => h0 y)).mp hz x (by simp [hx])

/-- An actual triple entry saturates both actual repeat rows. -/
theorem n62_triple_repeat_rows (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    (∀ x, defectMatrix G u x = if x = v then 3 else 0) ∧
    (∀ x, defectMatrix G v x = if x = u then 3 else 0) := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hs (x : V) : ∑ y, defectMatrix G x y = 3 := by simpa [hcard] using defect_row_sum G hreg x
  have hvu : defectMatrix G v u = 3 := by rw [(defect_symmetric G).apply u v,hb]
  exact ⟨saturated_single_row _ (defect_nonnegative G hreg hdiam u) (hs u) hb,
    saturated_single_row _ (defect_nonnegative G hreg hdiam v) (hs v) hvu⟩

/-- Actual triple-repeat endpoints are distinct and nonadjacent in the original graph. -/
theorem n62_triple_repeat_nonadj (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    u ≠ v ∧ ¬ G.Adj u v := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  constructor
  · intro he; subst v; rw [defect_diagonal G hreg] at hb; omega
  · intro ha
    have hh := n62_edge_defect_le_one G hdeg hdiam hcard ha
    omega

/-- An actual triple-repeat endpoint lies in no original triangle. -/
theorem n62_triple_endpoint_zero_triangle (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    zeroTriangleVertex G u := by
  have hn := (n62_triple_repeat_nonadj G hdeg hdiam hcard hb).2
  have hr := (n62_triple_repeat_rows G hdeg hdiam hcard hb).1
  intro x y hux huy hxy
  have hxv : x ≠ v := by rintro rfl; exact hn hux
  have hl := defect_incident_triangle_ge_one G hux huy hxy.symm
  rw [hr x,if_neg hxv] at hl
  omega

/-- Actual triple-repeat endpoints have exactly four actual common neighbors. -/
theorem n62_triple_common_card (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    (commonNeighborVertices G u v).card = 4 := by
  obtain ⟨hne,hn⟩ := n62_triple_repeat_nonadj G hdeg hdiam hcard hb
  have hh := defect_off_diagonal G hne
  simp only [adjacencyMatrix,SimpleGraph.adjMatrix_apply,if_neg hn] at hh
  change commonNeighborCount G u v = 4
  omega

/-- The common neighbors of an actual triple pair form an independent set in G. -/
theorem n62_triple_common_nonadj (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v x y : V} (hb : defectMatrix G u v = 3)
    (hx : x ∈ commonNeighborVertices G u v) (hy : y ∈ commonNeighborVertices G u v) :
    ¬ G.Adj x y :=
  n62_triple_endpoint_zero_triangle G hdeg hdiam hcard hb x y
    ((mem_commonNeighborVertices G u v x).mp hx).1
    ((mem_commonNeighborVertices G u v y).mp hy).1

private theorem triple_common_pair_lower (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v x y : V} (hb : defectMatrix G u v = 3)
    (hx : x ∈ commonNeighborVertices G u v) (hy : y ∈ commonNeighborVertices G u v)
    (hxy : x ≠ y) : 1 ≤ defectMatrix G x y := by
  have huv := (n62_triple_repeat_nonadj G hdeg hdiam hcard hb).1
  have hx' := (mem_commonNeighborVertices G u v x).mp hx
  have hy' := (mem_commonNeighborVertices G u v y).mp hy
  have hsub : ({u,v} : Finset V) ⊆ commonNeighborVertices G x y := by
    intro z hz
    rcases Finset.mem_insert.mp hz with hzu | hz
    · subst z
      exact (mem_commonNeighborVertices G x y u).mpr ⟨hx'.1.symm,hy'.1.symm⟩
    · have hzv : z = v := Finset.mem_singleton.mp hz
      subst z
      exact (mem_commonNeighborVertices G x y v).mpr ⟨hx'.2.symm,hy'.2.symm⟩
  have hc : 2 ≤ commonNeighborCount G x y := by
    simpa [commonNeighborVertices,commonNeighborCount,huv] using Finset.card_le_card hsub
  have hn := n62_triple_common_nonadj G hdeg hdiam hcard hb hx hy
  have he := defect_off_diagonal G hxy
  simp only [adjacencyMatrix,SimpleGraph.adjMatrix_apply,if_neg hn] at he
  omega

private theorem saturated_indicator_row (f : V → ℤ) (S : Finset V)
    (h0 : ∀ x, 0 ≤ f x) (hs : ∑ x, f x = (S.card : ℤ))
    (hl : ∀ x ∈ S, 1 ≤ f x) : ∀ x, f x = if x ∈ S then 1 else 0 := by
  let g : V → ℤ := fun x => if x ∈ S then 1 else 0
  have hle (x : V) : g x ≤ f x := by
    by_cases hx : x ∈ S
    · simpa [g,hx] using hl x hx
    · simpa [g,hx] using h0 x
  have hz : ∑ x, (f x - g x) = 0 := by
    rw [Finset.sum_sub_distrib,hs]
    simp [g]
  intro x
  exact sub_eq_zero.mp ((Finset.sum_eq_zero_iff_of_nonneg
    (fun y _ => sub_nonneg.mpr (hle y))).mp hz x (Finset.mem_univ x))

/-- Every actual common neighbor has precisely unit defect to the other three common neighbors.
This complete row also proves that no positive repeat entry leaves the common-neighbor set. -/
theorem n62_triple_common_rows (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v x : V} (hb : defectMatrix G u v = 3)
    (hx : x ∈ commonNeighborVertices G u v) :
    ∀ y, defectMatrix G x y = if y ∈ commonNeighborVertices G u v ∧ y ≠ x then 1 else 0 := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hc : ((commonNeighborVertices G u v).erase x).card = 3 := by
    rw [Finset.card_erase_of_mem hx,n62_triple_common_card G hdeg hdiam hcard hb]
  have hs : ∑ y, defectMatrix G x y = (((commonNeighborVertices G u v).erase x).card : ℤ) := by
    rw [hc]
    simpa [hcard] using defect_row_sum G hreg x
  have hr := saturated_indicator_row (defectMatrix G x) ((commonNeighborVertices G u v).erase x)
    (defect_nonnegative G hreg hdiam x) hs (fun y hy =>
      triple_common_pair_lower G hdeg hdiam hcard hb hx (Finset.mem_erase.mp hy).2
        (Finset.mem_erase.mp hy).1.symm)
  intro y
  simpa only [Finset.mem_erase,and_comm] using hr y

/-- Distinct members of the generated four-set have exactly the original triple endpoints as common neighbors. -/
theorem n62_triple_common_pair_neighbors (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v x y : V} (hb : defectMatrix G u v = 3)
    (hx : x ∈ commonNeighborVertices G u v) (hy : y ∈ commonNeighborVertices G u v)
    (hxy : x ≠ y) : commonNeighborVertices G x y = {u,v} := by
  have huv := (n62_triple_repeat_nonadj G hdeg hdiam hcard hb).1
  have hx' := (mem_commonNeighborVertices G u v x).mp hx
  have hy' := (mem_commonNeighborVertices G u v y).mp hy
  have hsub : ({u,v} : Finset V) ⊆ commonNeighborVertices G x y := by
    intro z hz
    rcases Finset.mem_insert.mp hz with hzu | hz
    · subst z
      exact (mem_commonNeighborVertices G x y u).mpr ⟨hx'.1.symm,hy'.1.symm⟩
    · have hzv : z = v := Finset.mem_singleton.mp hz
      subst z
      exact (mem_commonNeighborVertices G x y v).mpr ⟨hx'.2.symm,hy'.2.symm⟩
  have hn := n62_triple_common_nonadj G hdeg hdiam hcard hb hx hy
  have hbxy : defectMatrix G x y = 1 := by
    rw [n62_triple_common_rows G hdeg hdiam hcard hb hx]
    simp [hy,hxy.symm]
  have he := defect_off_diagonal G hxy
  simp only [adjacencyMatrix,SimpleGraph.adjMatrix_apply,if_neg hn] at he
  have hc : (commonNeighborVertices G x y).card = 2 := by
    change commonNeighborCount G x y = 2
    omega
  exact (Finset.eq_of_subset_of_card_le hsub (by simp [hc,huv])).symm

/-- Outside the triple endpoints, a vertex cannot have two distinct neighbors in the generated four-set. -/
theorem n62_triple_outside_common_neighbors_unique (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v z x y : V} (hb : defectMatrix G u v = 3)
    (hzu : z ≠ u) (hzv : z ≠ v)
    (hx : x ∈ commonNeighborVertices G u v) (hy : y ∈ commonNeighborVertices G u v)
    (hzx : G.Adj z x) (hzy : G.Adj z y) : x = y := by
  by_contra hxy
  have hz : z ∈ commonNeighborVertices G x y :=
    (mem_commonNeighborVertices G x y z).mpr ⟨hzx.symm,hzy.symm⟩
  rw [n62_triple_common_pair_neighbors G hdeg hdiam hcard hb hx hy hxy] at hz
  simp [hzu,hzv] at hz

private theorem repeat_component_eq_of_closed (G : SimpleGraph V) (S : Finset V) {r : V}
    (hr : r ∈ S) (hconn : ∀ x ∈ S, (repeatSupport G).Reachable r x)
    (hclosed : ∀ x ∈ S, ∀ y, (repeatSupport G).Adj x y → y ∈ S) :
    repeatComponentVertices G ((repeatSupport G).connectedComponentMk r) = S := by
  have hw : ∀ {a b : V}, (repeatSupport G).Walk a b → a ∈ S → b ∈ S := by
    intro a b p
    induction p with
    | nil => exact id
    | cons ha p ih => exact fun h => ih (hclosed _ h _ ha)
  ext x
  rw [mem_repeatComponentVertices]
  constructor
  · intro hx
    have hre := ((repeatSupport G).connectedComponentMk r).reachable_of_mem_supp (by rfl) hx
    obtain ⟨p⟩ := hre
    exact hw p hr
  · intro hx
    exact SimpleGraph.ConnectedComponent.sound (hconn x hx).symm

/-- The triple endpoints are precisely one actual repeat-support component. -/
theorem n62_triple_pair_component (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    repeatComponentVertices G ((repeatSupport G).connectedComponentMk u) = {u,v} := by
  obtain ⟨hu,hv⟩ := n62_triple_repeat_rows G hdeg hdiam hcard hb
  have huv := (n62_repeat_support_adj_iff G hdeg hdiam hcard u v).mpr (by omega)
  apply repeat_component_eq_of_closed G {u,v} (by simp)
  · intro x hx
    simp only [Finset.mem_insert,Finset.mem_singleton] at hx
    rcases hx with rfl | rfl
    · exact SimpleGraph.Reachable.rfl
    · exact huv.reachable
  · intro x hx y hxy
    simp only [Finset.mem_insert,Finset.mem_singleton] at hx ⊢
    rcases hx with rfl | rfl
    · right
      by_contra hy
      have hh := hu y
      simp only [hy,if_false] at hh
      have := hxy.2
      omega
    · left
      by_contra hy
      have hh := hv y
      simp only [hy,if_false] at hh
      have := hxy.2
      omega

/-- The four common neighbors are precisely one actual repeat-support component. -/
theorem n62_triple_common_component (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v x : V} (hb : defectMatrix G u v = 3)
    (hx : x ∈ commonNeighborVertices G u v) :
    repeatComponentVertices G ((repeatSupport G).connectedComponentMk x) = commonNeighborVertices G u v := by
  apply repeat_component_eq_of_closed G _ hx
  · intro y hy
    by_cases hxy : x = y
    · subst y; exact SimpleGraph.Reachable.rfl
    · apply SimpleGraph.Adj.reachable
      apply (n62_repeat_support_adj_iff G hdeg hdiam hcard x y).mpr
      rw [n62_triple_common_rows G hdeg hdiam hcard hb hx]
      simp [hy,Ne.symm hxy]
  · intro y hy z hyz
    by_contra hz
    have hh := n62_triple_common_rows G hdeg hdiam hcard hb hy z
    simp only [hz,false_and,if_false] at hh
    have := hyz.2
    omega

/-- An actual triple entry constructs actual support components of sizes two and four. -/
theorem n62_triple_component_sizes (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    repeatComponentSize G ((repeatSupport G).connectedComponentMk u) = 2 ∧
    ∃ C : (repeatSupport G).ConnectedComponent,
      repeatComponentVertices G C = commonNeighborVertices G u v ∧ repeatComponentSize G C = 4 := by
  have huv := (n62_triple_repeat_nonadj G hdeg hdiam hcard hb).1
  have hc := n62_triple_common_card G hdeg hdiam hcard hb
  constructor
  · simp [repeatComponentSize,n62_triple_pair_component G hdeg hdiam hcard hb,huv]
  · obtain ⟨x,hx⟩ := Finset.card_pos.mp (show 0 < (commonNeighborVertices G u v).card by omega)
    refine ⟨(repeatSupport G).connectedComponentMk x,
      n62_triple_common_component G hdeg hdiam hcard hb hx,?_⟩
    unfold repeatComponentSize
    rw [n62_triple_common_component G hdeg hdiam hcard hb hx,hc]

end
end DegreeDiameter
