import DegreeDiameter.N62D0Components

#print DegreeDiameter.D0ParentTemplate
#print DegreeDiameter.D0EdgeBoutTemplate
#print DegreeDiameter.ClosedDoubleFour
#check @DegreeDiameter.n62_d0_parent_root_row
#check @DegreeDiameter.n62_d0_parent_repeat_profile
#check @DegreeDiameter.n62_d0_match_closed_component
#check @DegreeDiameter.bout_common_neighbors_of_unit_repeat
#check @DegreeDiameter.n62_d0_bout_closed_component
#check @DegreeDiameter.closedDoubleFour_no_external_repeat
#check @DegreeDiameter.d0_bout_template_of_unit_repeat
#print axioms DegreeDiameter.n62_d0_parent_root_row
#print axioms DegreeDiameter.n62_d0_parent_repeat_profile
#print axioms DegreeDiameter.n62_d0_match_closed_component
#print axioms DegreeDiameter.bout_common_neighbors_of_unit_repeat
#print axioms DegreeDiameter.n62_d0_bout_closed_component
#print axioms DegreeDiameter.closedDoubleFour_no_external_repeat
#print axioms DegreeDiameter.d0_bout_template_of_unit_repeat

open DegreeDiameter
example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k p q w a : V}
    (h : D0ParentTemplate G r i j k p q w a) (hwa : ¬ G.Adj w a) :
    ∃ b, ClosedDoubleFour G r w b a ∧
      ¬ G.Adj r w ∧ ¬ G.Adj r b ∧ ¬ G.Adj r a ∧
      ¬ G.Adj w b ∧ ¬ G.Adj w a ∧ ¬ G.Adj b a :=
  n62_d0_match_closed_component G hdeg hdiam hcard h hwa

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k p q w a b : V}
    (hp : D0ParentTemplate G r i j k p q w a) (hwa : G.Adj w a)
    (hrb : G.Adj r b) (hbi : b ≠ i) (hbj : b ≠ j) (hbk : b ≠ k)
    (hbp : b ≠ p) (hbq : b ≠ q) (hwb : defectMatrix G w b = 1) :
    ClosedDoubleFour G r w b a ∧ G.Adj r b ∧ G.Adj w a ∧
      ¬ G.Adj r w ∧ ¬ G.Adj r a ∧ ¬ G.Adj w b ∧ ¬ G.Adj b a :=
  n62_d0_bout_closed_component G hdeg hdiam hcard
    (d0_bout_template_of_unit_repeat G hp hwa hrb hbi hbj hbk hbp hbq hwb)
