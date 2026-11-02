import DegreeDiameter.N62D0Bin

#print DegreeDiameter.D0EdgeBinTemplate
#check @DegreeDiameter.bin_common_neighbor_of_unit_repeat
#check @DegreeDiameter.n62_d0_bin_root_rows
#check @DegreeDiameter.n62_d0_bin_parent_repeat_profile
#check @DegreeDiameter.n62_d0_bin_third_repeat
#check @DegreeDiameter.no_n62_d0_edge_bin_template
#print axioms DegreeDiameter.bin_common_neighbor_of_unit_repeat
#print axioms DegreeDiameter.n62_d0_bin_root_rows
#print axioms DegreeDiameter.n62_d0_bin_parent_repeat_profile
#print axioms DegreeDiameter.n62_d0_bin_third_repeat
#print axioms DegreeDiameter.no_n62_d0_edge_bin_template

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : DegreeDiameter.degreeAtMostEight G)
    (hdiam : DegreeDiameter.diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k b d w a : V}
    (h : DegreeDiameter.D0EdgeBinTemplate G r i j k b d w a) : False :=
  DegreeDiameter.no_n62_d0_edge_bin_template G hdeg hdiam hcard h
