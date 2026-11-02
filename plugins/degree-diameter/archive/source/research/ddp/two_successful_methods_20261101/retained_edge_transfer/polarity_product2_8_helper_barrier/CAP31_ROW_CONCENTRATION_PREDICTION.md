# Unreviewed refinement: a possible concentration constraint at cap31

2026-11-01. Working derivation after the supported650-target barrier. No experiment, graph generation, independent acceptance or Lean claim is made for this refinement. It is outside the three new graphs' C scope.

Keep the exact source/uniform-copy/mandatory-edge assumptions of PREDICTION_AND_PROOF.md. For helper h, count distinct based classes in each O_A row: s_a(h)=number of b in O_B for which h is adjacent to some free representative of class(a,b). Repeated copies of the same class count once.

Additional factor fact to check: for different absolutes beta,b in B, at most ONE nonabsolute vertex v adjacent to b lies within old distance2 of beta. Any such v gives a length3 factor walk beta--w--v--b. The GQ point/nonincident-polar-line projection should make that three-walk unique. This is stronger than mere absolute-code distance3 and needs explicit justification, rather than inheriting it without checking.

If this fact holds, and h owns no class(a,b), its s_a(h) different row pins cover at most s_a(h) of the8 old nonabsolute neighbors of b. If s_a(h)<8, some saturated old target(a,v) is uncovered by the direct-pin old suffixes. Reaching that target within3 then requires a representative of class(a,b) either among a helper-neighbor's pins or among an added F-peer of h's own pins.

Let T_h be the union of such accessible classes. The same route/degree accounting bounds |T_h|<=r*p_h+sum_{g~h}p_g. If ALL five rows of EVERY helper have fewer than8 distinct owned classes, all325 classes are in its own-pin classes or T_h, so

    325 <= (r+1)*p_h + sum_{g~h}p_g.

Sum over the helper graph and use p_h+d_h<=27+r:

    325 <= max_d (27+r-d)*(r+1+d) = (r+14)^2,

with optimum d13. At r4/cap31 this gives325<=324, a contradiction. Thus, if the extra uniqueness premise and this derivation are supported, any successful cap31 augmentation must have at least one helper with at least8 distinct based classes in one absolute-A row. It would be unsound to conclude every helper must satisfy it, or that31 is impossible.

This would reject the tempting balanced ownership controller5K13 with each helper having19pins spread(0,4,5,5,5) over its five rows; no such controller or source graph was generated. It would change the next generation rule toward deliberately concentrated row ownership, then require actual simultaneous coverage in the B factor and valid undirected peer edges. Favorable local quadratic counts alone do not supply such a rule.

Status: prediction only. First verify the exact GQ uniqueness step and the row-to-class coverage reduction. Do not start an8-subset enumeration, polarity-table build, helper solver or new source graph merely from this note.
