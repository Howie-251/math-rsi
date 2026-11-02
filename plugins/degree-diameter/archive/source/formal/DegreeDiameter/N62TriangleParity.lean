import DegreeDiameter.N62TriangleMate
import Mathlib.Combinatorics.SimpleGraph.Clique
import Mathlib.Data.ZMod.Basic

namespace DegreeDiameter
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section
variable {V : Type*} [Fintype V]

/-- The actual vertices outside T with a unit repeat entry from T. On an
order-62 actual triangle, these are exactly its three derived mates. -/
def triangleMateSet (G : SimpleGraph V) (T : Finset V) : Finset V :=
  Finset.univ.filter (fun y => y ∉ T ∧ ∃ x ∈ T, defectMatrix G x y = 1)

private theorem triangle_mate_set_of_rows (G : SimpleGraph V) {r a b w u v : V}
    (hd : Disjoint ({r,a,b} : Finset V) ({w,u,v} : Finset V))
    (hR : threeUnitRow G r a b w) (hA : threeUnitRow G a r b u)
    (hB : threeUnitRow G b r a v) :
    triangleMateSet G {r,a,b} = {w,u,v} := by
  unfold threeUnitRow at hR hA hB
  ext y
  by_cases hy : y ∈ ({r,a,b} : Finset V)
  · have hy' : y ∉ ({w,u,v} : Finset V) := fun h => Finset.disjoint_left.mp hd hy h
    have hn : y ∉ triangleMateSet G {r,a,b} := by
      intro hm
      exact (Finset.mem_filter.mp hm).2.1 hy
    exact iff_of_false hn hy'
  · have hyr : y ≠ r := by intro h; subst y; simp at hy
    have hya : y ≠ a := by intro h; subst y; simp at hy
    have hyb : y ≠ b := by intro h; subst y; simp at hy
    simp [triangleMateSet, hR, hA, hB, hyr, hya, hyb]

/-- The concrete mate-set map preserves the actual finite triangle set and
is an involution there, with disjoint source and target triangles. -/
theorem n62_triangle_mate_set_properties (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {T : Finset V} (hT : G.IsNClique 3 T) :
    G.IsNClique 3 (triangleMateSet G T) ∧ Disjoint T (triangleMateSet G T) ∧
      triangleMateSet G (triangleMateSet G T) = T := by
  obtain ⟨r,a,b,hra,hrb,hab,rfl⟩ := SimpleGraph.is3Clique_iff.mp hT
  obtain ⟨w,u,v,hwu,hwv,huv,hd,_,hR,hA,hB,hW,hU,hV⟩ :=
    n62_triangle_has_paired_triangle G hdeg hdiam hcard hra hrb hab
  have hforward := triangle_mate_set_of_rows G hd hR hA hB
  have hback := triangle_mate_set_of_rows G hd.symm hW hU hV
  rw [hforward]
  exact ⟨SimpleGraph.is3Clique_triple_iff.mpr ⟨hwu,hwv,huv⟩, hd, hback⟩

/-- The actual triangle mate-set involution has no fixed triangle. -/
theorem n62_triangle_mate_set_ne (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {T : Finset V} (hT : G.IsNClique 3 T) :
    triangleMateSet G T ≠ T := by
  intro heq
  have hd := (n62_triangle_mate_set_properties G hdeg hdiam hcard hT).2.1
  rw [heq] at hd
  have hempty : T = ∅ := Finset.eq_empty_iff_forall_not_mem.mpr
    (fun x hx => Finset.disjoint_left.mp hd hx hx)
  have hc := hT.card_eq
  simp [hempty] at hc

/-- The number of all actual unordered triangles in an arbitrary original
order-62 graph is even. No simplicity assumption on the defect matrix is used. -/
theorem n62_triangle_count_even (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) : Even (G.cliqueFinset 3).card := by
  have hzero : (∑ T ∈ G.cliqueFinset 3, (1 : ZMod 2)) = 0 := by
    apply Finset.sum_involution (fun T _ => triangleMateSet G T)
    · intro T hT
      decide
    · intro T hT _
      exact n62_triangle_mate_set_ne G hdeg hdiam hcard (SimpleGraph.mem_cliqueFinset_iff.mp hT)
    · intro T hT
      exact SimpleGraph.mem_cliqueFinset_iff.mpr
        (n62_triangle_mate_set_properties G hdeg hdiam hcard
          (SimpleGraph.mem_cliqueFinset_iff.mp hT)).1
    · intro T hT
      exact (n62_triangle_mate_set_properties G hdeg hdiam hcard
        (SimpleGraph.mem_cliqueFinset_iff.mp hT)).2.2
  apply ZMod.natCast_eq_zero_iff_even.mp
  simpa using hzero

end
end DegreeDiameter
