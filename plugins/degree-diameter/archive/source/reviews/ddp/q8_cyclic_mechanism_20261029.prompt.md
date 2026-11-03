# Targeted mathematical feedback on the q8 auxiliary construction

Please read the listed local files and act as a complementary mathematical reviewer. Do not run code, BFS, solvers, installs, or modify files. Focus on one concrete shared-route issue, not a list of templates.

The same active degree/diameter Goal seeks a complete graph beyond a current public lower bound. A q8 construction in Rishabh Rajiv's September2026 paper, Definition1/Theorem1, would yield1088vertices/degree13/D3 if an auxiliary K on64vertices contains eight Q3 cubes, has maxdegree5, and D<=3. Current Comellas13D3 is972. The author already has1088/degree14 via a3regular extra gadget and explicitly had not found the degree2 gadget. No main1088/13 graph has been generated.

Existing boundaries: fixed J5-plus-I1 affine3840 class all failed, published K64degree6 has94of96extraedges D3critical so pure deletion cannot work, unrestricted crosspencil2factor SAT90sec UNKNOWN. Do not re-review or suggest rerunning those. New work uses vertices(a,l) in Z8 x F2^3, fixed cube edges l XOR1/2/4. It is based on the author's successful q9 cyclic-voltage method, not random phases.

Read:
1. research/ddp/refresh_20261029/q8_cyclic_gadget_construction/PREDICTION.md and RESULT.json
2. research/ddp/refresh_20261029/q8_cyclic_gadget_construction/pi_twist_obstruction/PROOF.md, RESULT.json, and selected SUMSET_TABLE.jsonl entries if needed
3. research/ddp/refresh_20261029/q8_cyclic_halfturn_repair/PREDICTION.md, RESULT.json, FIRST_CANDIDATE.json
4. research/ddp/refresh_20261029/q8_cyclic_orbit_sat/PREDICTION.md, run_once.py, MODEL.json and RESULT.json if it exists

New derivation: sigma(a,l)=(a+delta_l,pi(l)), where pi(l)=l XOR3 if even parity, XOR5 if odd. Opposite cube label l XOR7 has reachable phases exactly A_l+A_r, A_l={0,delta_l,-delta_pi(l)}, r=l XOR2 (even) or XOR4 (odd). An analytic delta=[1,3,2,6,2,6,1,3] makes all opposite-label pairs work, but all64roots fail other targets, including same-label phase4. Exact441 comparisons of3sets containing0 give just18 full sums: both must be three-term arithmetic progressions of odd widths1 and3, one of each. The resulting same-label short loops never attain4; hence this entire fixed-pi Z8 voltage family is impossible, not just that one delta. Please verify the logic and stated scope.

This understanding changed the generator: pi=(0,1,3)(4,5,7)(2,6), cycle voltages each4, so all same-label halfturns are guaranteed. Frozen14406proper phase assignments all fail; the first fixes allsame-label phases but misses other label classes. Do not suggest another phase seed or local bad-pair optimization.

The latest exact model no longer fixes pi: all simple extra edges invariant under deck(a,l)->(a+1,l) are represented by244undirected orbit variables, including pencil-internal chords and same-label halfturn matchings. Actual neighbor degree2 uses occurrence multiplicities, since offsets±1/2/3 share one orbit but give two neighbors. R2 is shared across256undirected pair orbits, R3 has228crosspencil pair orbits. A valid existence-preserving symmetry clause requires one of orbit(0,0,1),(0,1,1),(0,3,1),(0,7,1): some odd offset is needed for connectivity; cube global translation/axis permutation and deck-unit multiplication normalize such an edge. No old two-edge0-8/0-16 fix is used. All24428variables/86597clauses follow exact path gates; single120sec run returnedUNKNOWN if RESULT says so. This symmetry class is not claimed WLOG for every K64.

Please answer:
- Is the full fixed-pi halfturn exclusion correct, including degenerate phases?
- Does the new orbit model's degree multiplicity, undirected orbit representative, path quantification and four-orbit symmetry preserve its stated class?
- Based on these actual failures, is there a specific structural obstruction or a concrete change in shared connections worth testing next? A short falsifiable rule or counterexample is useful; a general method list or another longer timer is not. If no useful additional judgment is supported, say exactly what remains uncertain.

Static model agreement is not independent numerical verification or Lean proof. Existing valid examples remain104/4pairs, confirmed main-table examples103/3pairs, completeLean1,3750latest-global noveltypending; no new record should be claimed here.
