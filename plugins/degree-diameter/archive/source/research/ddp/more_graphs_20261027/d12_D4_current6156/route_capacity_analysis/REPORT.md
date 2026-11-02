# C19 versus C20: route-capacity diagnosis and one controlled wider-filter trial

2026-10-27. Terminal status: no new graph; the authorized finite trial is complete.

The initial prediction was that some ordered base pair had at most 19 effective good-four-step or even short-route voltage forms. It was refuted: the minimum number of distinct integer forms is 23. The minimum formal phase/fiber incidence capacity from an x=0 start is 2277, exceeding 20·81=1620. Consequently, a simple local count does not explain why the published C19 construction succeeds while the author's fixed-base C20 strict search has no passer. Simultaneous modular placement and collisions between forms remain the issue. These capacities are upper capacities, not constructive coverage guarantees.

The fixed base permutations are a=(0123) and b=(0132), with inverse labels A and B. They are not involutions. Among 108 reduced four-letter words, 100 route matrices have rank four and eight rank three. The bad-word IDs exactly match the author's file. The literal source voltage vector (0,12,4,0;17,0,0,1), reduced modulo 19, has a complete inherited I/R2/G4 certificate. This inherits the existing source certificate; no old source BFS was repeated. With precisely the same integers modulo 20, both the author's strict filter and the wider certificate leave 54 ordered deck-representative controller slots. For example, root base 0 misses target base 0 at phases 5,10,15. Exact length-at-most-four affine image enumeration from fiber x=0 leaves 3708 endpoints in total over the four base roots. These are representative-start misses, not unordered bad pairs of a generated graph. This literal cannot have diameter four.

## Why a wider filter is valid

The already verified Mizuno proof in `research/ddp/breadth_20261027_wave5/mizuno_d4_source/proof_ja.md`, §§2,3.2,3.3,4, applies to **any** reduced two-letter controller word. It does not require the shortest controller distance to equal two. All freely reducing insertions have the same affine center because the matrices are inverse consistent; their four rank-three hyperplanes form a pencil covering all 81 fiber states. The empty-word certificate handles a common controller vertex, and any one of the 100 full-rank four-letter words handles its endpoint. Thus I ∪ R2 ∪ G4 is sufficient for every fiber start.

The actual 6156 recipe uses singular representatives that differ from those inverse-consistent matrices only by a row in the corresponding line direction; their one-step line relations are identical. `PENCIL_APPLICABILITY.json` records this comparison. The author's strict filter instead exempts only shortest distances zero and two. A vertex at distance one that also has a reduced two-walk can therefore be rejected by that sufficient screen despite satisfying the inherited pencil certificate. This does not invalidate the author's construction or the reported strict-filter exhaustion.

## Frozen new slice and result

Only C20 and the original base/chart were used. The slice was

    va=(0,x,y,0), vb=(z,0,0,1), x,y,z in {0,...,19}.

It forces a zero-voltage base triangle, so it specifically contains the distance-one plus reduced-two-walk overlap responsible for the filter distinction. Before execution, `zero_triangle_wide20/PREDICTION.json` predicted at least one wider-certificate passer.

All 8000 assignments were tested once. All fail the wider certificate already from base root 0. The implementation retained 7220 simple and 780 nonsimple controllers; it did not discard repeated label relations. The prediction is refuted. Native filter CPU was 0.006084 seconds; preparation, compilation and filtering used 1.334219858 seconds. No final graph was generated and no BFS was run.

This is a complete negative result for this sufficient certificate on this fixed slice. It is not a proof that all 8000 lifted graphs fail D4: combinations of the remaining lower-rank affine routes were not exhaustively scored in this trial. It also does not exclude other C20 voltage slices, base permutations, or charts. There is no numerical basis from this trial to nominate a new base pair. The next action is to stop this scope rather than re-run the author's closed order19–27 strict scan or add another voltage grid.

Evidence: `RESULT.json`, `SYMBOLIC_SLOTS.json`, `NUMERIC_WORD_TABLES.json`, `PENCIL_APPLICABILITY.json`, and `zero_triangle_wide20/{PREDICTION.json,route_forms.txt,filter.cpp,RESULT.json,terminal.json}`. The first analysis cost 0.011393669 CPU seconds and generated no graph.


## Follow-up packet and metric clarification

`universal_exactNB4_*` and `universal_wide_*` are hypothetical controller endpoint profiles for a different chart in which all 108 reduced four-letter words would have full rank. They do not assert current Mizuno-chart rank-three routes cover their targets. Actual current-chart zero-source unions are the `x0_*` fields. See `METRIC_SCOPE_NOTES.json` for field-by-field scope.

The independently frozen four-bad-word packet at y=9 was tested once in `bad4_packet_probe/`. Although its four controller endpoints coalesce at base0/phase10, its normals have rank four and its affine union has only 65 points for each of all 81 sources. That prediction is refuted; no packet-aware voltage scan follows.


The final explicitly authorized augmentation added only aab/BAA at x=10,y=9. It also failed: six-route unions contain 73,75,77 points depending on source, and no source has full 81-point coverage. See `six_route_packet_probe/REPORT.md`. The conditional 20-value z trial was not started. The fixed packet investigation has ended.
