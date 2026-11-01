# 23-point minimum-degree-seven branch

Current result: the complete23-point minimum-degree-seven paper candidate, with all retained exact certificates independently replayed. Main proof: N23_MIN_SEVEN.md. The full23-point branch dispatcher is N23_COMPLETE_DISPATCHER.md. No Lean claim.

For H23 with34 edges and pair coverage, the r>=14 degree7 vertices carry the weighted graph w=lambda-1 of maximum weighted degree6. Strong lambda>=4 was already handled in the frozen first-hour threshold package. See SELECTION.md for the proof that a six-point set minimizing total weight W satisfies (r-7)d_S(x)+2W<=30, hence either max degree<=2/W<=6 or max degree3/W<=4.

The latter has9 graph shapes and66 trace profiles after strict-projection pruning, all strictly bounded by4809/4862. The former has725 residual trace orbits after lower-dimensional projections;530 pure-quota and117 joint-layout certificates are strict, leaving78 traces on only five disjoint-clique shapes.

If the minimum W=6, the weighted graph on all degree7 vertices is exactly2K7, r=14; every pair from a degree7 to a degree8 vertex is unit. The17 still-open six-point traces on2K3 admit209 extensions by an arbitrary degree8 vertex, and all209 have strict pure-quota bounds. This closes W=6 as a paper candidate.

For W2/3/4, choose a seventh degree7 vertex whose total weight to S is at most floor((36-2W)/(r-6)), hence at most4/3/3. Minimum-W exchanges and all six-point projections leave just4/1/3/7 labelled neighbor vectors for the old shapes2K2+2I, K3+3I,3K2,K3+K2+I. The complete20949 trace promotions leave1125 labelled seven-point profiles:1124 pure bounds are strict, and the single1002/1001 residue has an exact joint-layout bound904545552/910000091<1. All1124+1 have independent exact replay. This closes the branch as a paper candidate.

Evidence:
- FOUR_LOW.json: complete699 four-point trace orbits,617 pure strict and11 joint strict,71 residues.
- FIVE_DEGREE_TWO.json: complete246 five-point trace orbits after four-projection pruning,110 pure and47 joint strict,89 residues.
- SIX_DEGREE_TWO_CANON.json: complete725 six-point trace orbits after five-projection pruning;530 pure,84 first joint,33 additional full-order joint,78 residues.
- SIX_DEGREE_THREE.json: complete9 graph shapes /66 six-point profiles, all pure strict.
- EQUALITY_SEVEN.json: complete209 seven-point profiles, all pure strict.
- STRICT_WITNESSES_VERIFIED.json:1478 exact pure-quota/labelled-injection replays.
- FOUR_LOW_STRICT_JOINT_VERIFIED.json (11), FIVE_DEGREE_TWO_STRICT_JOINT_VERIFIED.json (47), SIX_DEGREE_TWO_CANON_STRICT_JOINT_VERIFIED.json (84), SIX_RESIDUES_STRICT_JOINT_VERIFIED.json (33).
- SIX_DEGREE_THREE_VERIFIED.json:66 additional pure replays.

All tables describe local type counts, not entire hypergraph enumeration. Their actual input is the selected vertices of H; completeness is via nonnegative integer higher-trace multiplicities, pair/degree equalities, and all possible splits when adjoining a selected vertex. Classification coverage and actual selection must be carried into Lean later. The proposal solver is never an axiom: independent replay uses rational arithmetic and labelled-injection probabilities, with complete slot capacities, avoided-lock quotas, and repaired dual inequalities.

Final additional evidence: SEVEN_SELECTED.json, SEVEN_SELECTED_STRICT_VERIFIED.json (1124), SEVEN_SELECTED_JOINT_VERIFIED.json (1). Total retained replay in this directory:2668 pure certificates and176 joint certificates. See MIDDLE_SELECTION_REVIEW.md for the requested independent actual-selection review of r=1..>=7, and N23_COMPLETE_DISPATCHER.md for the whole23-point paper map.
