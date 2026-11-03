import DegreeDiameter.N62DoubleRoot
import DegreeDiameter.N62DoubleParity

namespace DegreeDiameter
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section
variable {V : Type*} [Fintype V]

/-- The actual unit-repeat neighbors of the endpoints of an unordered pair.
For a double pair in a closed B4, these are exactly the other double pair. -/
def doublePairMate (G : SimpleGraph V) (P : Finset V) : Finset V :=
  Finset.univ.filter (fun z => ∃ x ∈ P, defectMatrix G x z = 1)

private theorem two_one_unit_iff (G : SimpleGraph V) {v d u z : V}
    (hr : twoOneRow G v d u) (hdu : d ≠ u) :
    defectMatrix G v z = 1 ↔ z = u := by
  rw [hr z]
  by_cases hzd : z = d
  · subst z; simp [hdu]
  · simp [hzd]

/-- The pairing is read directly from the four actual rows and is its own inverse. -/
theorem closedDoubleFour_pair_mates (G : SimpleGraph V) {r w b a : V}
    (h : ClosedDoubleFour G r w b a) :
    doublePairMate G {r,w} = {a,b} ∧ doublePairMate G {a,b} = {r,w} ∧
      ({a,b} : Finset V) ≠ {r,w} := by
  obtain ⟨hrw,hrb,hra,hwb,hwa,hba,hR,hW,hA,hB⟩ := h
  have hRu (z : V) : defectMatrix G r z = 1 ↔ z = a := two_one_unit_iff G hR hwa
  have hWu (z : V) : defectMatrix G w z = 1 ↔ z = b := two_one_unit_iff G hW hrb
  have hAu (z : V) : defectMatrix G a z = 1 ↔ z = r := two_one_unit_iff G hA hrb.symm
  have hBu (z : V) : defectMatrix G b z = 1 ↔ z = w := two_one_unit_iff G hB hwa.symm
  refine ⟨?_,?_,?_⟩
  · ext z
    simp [doublePairMate,hRu,hWu]
  · ext z
    simp [doublePairMate,hAu,hBu]
  · intro hh
    have hr : r ∈ ({a,b} : Finset V) := by rw [hh]; simp
    simpa [hra,hrb] using hr

/-- With no D1 parent representative, every actual double pair has a
canonical other double pair, with no orientation or choice certificate. -/
theorem n62_double_pair_mate_properties (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62)
    (hno : ¬ ∃ r w a, D1MatchParentTemplate G r w a)
    {P : Finset V} (hP : P ∈ doubleRepeatPairs G) :
    doublePairMate G P ∈ doubleRepeatPairs G ∧
      doublePairMate G (doublePairMate G P) = P ∧ doublePairMate G P ≠ P := by
  obtain ⟨r,w,hrw,hb,rfl⟩ := (Finset.mem_filter.mp hP).2
  rcases n62_double_root_d1_or_closed_component G hdeg hdiam hcard hb with hD1 | hclosed
  · obtain ⟨a,ha⟩ := hD1
    exact False.elim (hno ⟨r,w,a,ha⟩)
  obtain ⟨a,b,h⟩ := hclosed
  obtain ⟨hm,hback,hne⟩ := closedDoubleFour_pair_mates G h
  obtain ⟨_,hrb,_,_,_,hba,_,_,hA,_⟩ := h
  have hab2 : defectMatrix G a b = 2 := by
    have hh := hA b
    simpa [hrb.symm] using hh
  refine ⟨?_,?_,?_⟩
  · rw [hm]
    exact Finset.mem_filter.mpr ⟨Finset.mem_univ _,a,b,hba.symm,hab2,rfl⟩
  · rw [hm,hback]
  · rw [hm]
    exact hne

/-- Absence of an actual D1 representative pairs all actual double edges,
so their cardinality is even. This step requires no global defect bound. -/
theorem n62_double_repeat_pairs_even_of_no_d1 (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62)
    (hno : ¬ ∃ r w a, D1MatchParentTemplate G r w a) :
    Even (doubleRepeatPairs G).card := by
  have hz : (∑ P ∈ doubleRepeatPairs G, (1 : ZMod 2)) = 0 := by
    apply Finset.sum_involution (fun P _ => doublePairMate G P)
    · intro P hP; decide
    · intro P hP _
      exact (n62_double_pair_mate_properties G hdeg hdiam hcard hno hP).2.2
    · intro P hP
      exact (n62_double_pair_mate_properties G hdeg hdiam hcard hno hP).1
    · intro P hP
      exact (n62_double_pair_mate_properties G hdeg hdiam hcard hno hP).2.1
  apply ZMod.natCast_eq_zero_iff_even.mp
  simpa using hz

/-- Every legal order-62 graph whose actual defect entries are at most two
has an actual D1_MATCH parent representative. The defect bound remains an
explicit hypothesis; no triple-repeat elimination is assumed implicitly. -/
theorem n62_exists_d1_match_parent (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (hbound : ∀ x y, defectMatrix G x y ≤ 2) :
    ∃ r w a, D1MatchParentTemplate G r w a := by
  by_contra hno
  obtain ⟨k,hk⟩ := n62_double_repeat_pairs_even_of_no_d1 G hdeg hdiam hcard hno
  obtain ⟨j,hj⟩ := n62_double_repeat_pair_count_odd G hdeg hdiam hcard hbound
  omega

end
end DegreeDiameter
