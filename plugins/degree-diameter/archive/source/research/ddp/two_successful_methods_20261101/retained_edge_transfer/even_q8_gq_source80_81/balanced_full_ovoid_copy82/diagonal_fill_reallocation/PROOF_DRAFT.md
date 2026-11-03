# Fixed346516 reallocation and final concrete Lean bridge

From the accepted346515 literal graph, remove exactly65 diagonal clone-to-own-
filler edges and add hub346515 adjacent to all65 original fillers342225..342289.
Every one of13862745 filled-source H edges is retained. Diagonal ownership is
the actual spread-owner index, never an assumption j=i. Each clone now has its
open original-U neighborhood; diagonal degree80, off-diagonal degree81. The
new hub has degree65. Thus n346516, m14204970 and histogram
{65:1,80:65,81:4225,82:342225}, as measured by the one-stream producer.

Production consumed0.940117171 CPU including compilation and preparation,
without BFS, field/geometry/projection work or Lean. The separate fresh validator
bound all4225 raw-U neighborhoods and the exact65-edge delta, preserved the
entire H body, and checked actual ordinary BFS only from65 changed diagonal
clones and hub. All66 distributions matched. It did not rerun4160 unchanged
off-diagonal roots or any old-root BFS; their all-pair routes use U/H interiors.

The source-only all-pair proof is the same rule as the accepted7532 test:
raw-U full-neighborhood cloning gives U/clone pairs; filled H retains old pairs;
filler/clone paths end in a retained raw-U pin, with the omitted own-filler
edge replaced by a2walk through another flag; hub routes use an owner filler
and a flag. Prefixes build these modified clones directly from H, then hub.
This changes the old mandatory full-N_H clone rule and therefore does not
contradict the fixed-adjacency augmentation obstruction.

This draft now has an actual unconditional concrete Lean realization:
DegreeDiameter.Portfolio.Q8DiagonalFill.d82_346516 and FinalClaim/final_claim,
explicit Fin346516 label, degree<=82, genuine Walk D3 and structural nonD2.
The generic proof, new670+670 small bridge checks across q4/q8, standalone
Audit and external recipe correspondence are documented in
../../../diagonal_fill_reallocation_formalization/PROOF.md and the local
formalization/FINAL.json. Only standard three axioms occur. There is no claim
of a formal ASCII parser, exact formal regularity, paid-review inheritance,
world record or resolved priority.
