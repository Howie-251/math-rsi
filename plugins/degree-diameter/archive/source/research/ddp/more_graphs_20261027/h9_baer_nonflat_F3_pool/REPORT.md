# Nonflat F3 Qplanes: no N11 pool,34 new twelve-pin N12 neighborhoods

The complete new plane scope was enumerated and screened. There are1120 maximal totally isotropic three-dimensional vector subspaces overF3. Exact RREF comparison removes the364 previously tested G2 flatplanes, leaving756 nonflat F3-defined Qplanes. Each reused all7560 Baer masks, so5715360 new plane/Baer occurrences were tested. No old flatplane Baer occurrence or orbit search was repeated.

On current N11 source37631, no raw13point Baer set passes the current degree filter, so its legal pool is empty. The prediction that nonflat planes would supply at least one legal N11 neighborhood is refuted in this complete scope. Combined with the previous empty N11 pool for the364 flatplanes on the same37631 source, the full1120 F3-defined plane scope has no degree-legal complete folded Baer neighborhood. This does not cover the other Q9 planes or other blocking-set rules.

On current N12 source42398,42 raw Baer occurrences pass olddegree eligibility. Eight fold to13pins and exceed the degree12 cap. The remaining34 fold to12pins and are all distinct, each with zero anchor capacity. None duplicates an actual pinset from the older410-item flatplane pool. These34 are a new source pool, not accepted new graphs: no oldcore or full-source R4 computation, anchor search or graph generation was performed. The fixed42398 source is previously accepted through actualdegree/completeR4 induction; latest independent allsource graph remains42377.

## Complete F3-plane classification

The existing coordinate cache has364 normalized singular F3 points. For every triple of distinct such projective points with pairwise polar form0, the program computes the canonical RREF of their three vectors. Rank2 triples are rejected; rank3 triples span a totally singular3space, since Q of a linear combination is the sum of the individual Q terms and pairwise polar terms. Conversely every maximal isotropic3space has an independent triple among its13projective F3points, so this enumeration is exhaustive.

There are262080 independent pairwise-polar triples and14560 collinear triples. RREF deduplication gives1120spaces, matching(3+1)(3^2+1)(3^3+1)=1120 for Q(6,3). The364 old plane bases from h9_baer_plane_pool/planes.json are RREF-normalized by the same function, are all distinct, and all lie in this set. Removing those exact keys leaves756. all_F3_planes.json records every basis, its13 F3point IDs and old/nonflat flag. plane_calibration.json saves all counts before the new degree screen begins.

A direct coordinate Pluecker test finds8736 H3-collinear point pairs across the old flatplanes and zero across all756 nonflat planes. In particular none of the new planes contains an H3 incidence line. This is a coordinate membership check, not an incidence graph reconstruction or graph BFS. Together with the established polar-distance relation it supports the intended geometric separation from the old flatplane-star setting, but it did not yield a legal N11 neighborhood under the present degrees.

Each F3 basis extends overF9 to a totally singular PG2(F9). The program maps its91 coefficient points into the existing66430point cache. It reuses exactly the earlier baer_masks.u64.bin and the same91point order from orbit.json; there is no new7560-state group enumeration. The reused full PGL3(F9) orbit is already justified by the generator and projective-frame stabilizer arguments in h9_baer_plane_pool/REPORT.md.

## Blocking rule and degree filter

The Baer blocking proof only uses a totally singular plane, not a G2 flatplane. For any polar functional on that plane, restricting to the threeF3 coordinates of a Baer subplane gives a linear map F3^3 to F9, a two-dimensional F3space. It has a nonzero kernel, so every polar section meets the raw13point Baer set. The established H9 polar-distance correspondence and calibrated fold projection therefore give R4 coverage of the old bare core by the complete folded image. The point-to-point route remains four graph steps. Extra copies and later appended vertices still require actual complete whole-source coverage before a new graph can be accepted. No such check was run in this pool task.

For each current source, a91bit plane mask marks raw points whose folded oldvertex has degree belowDelta. Only Baer masks entirely inside that mask survive. Their13 raw points are then folded, deduplicated and checked against the actual pin-count cap. Every distinct folded image remains mandatory. This accounts correctly for raw point collisions and charges one new edge per distinct old pin. Filtering is based on current37631 and42398 source degrees, using the unchanged calibrated point-to-core maps. The old flatplane pool and reports were left unchanged.

pool11.json is empty. pool12.json contains34 sorted twelve-pin neighborhoods, each with current degrees, anchorcap0 and one complete primary13rawpoint witness. The witness includes raw IDs and coordinates, RREF plane basis, Baer orbit ID and exact91bit mask; all occurrence references are retained. nonflat_planes.json distinguishes the plane's13 F3points from its91 F9points. The actual Baer13point sets are generally different from those13 F3points.

## Cost and terminal scope

Plane calibration used0.093898 native CPU seconds. The100-new-plane profile processed756000 Baer occurrences in0.003569 plane-enumeration CPU seconds and projected0.120963 total native seconds. The full native run used0.142997 CPU seconds, compilation2.738306, and the driver measured2.884050 total child CPU seconds, below15. All756 new planes reached terminal degree-screen states.

This is only the F3-defined Qplane extension:1120 such planes exist, and this task screened their756 nonflat complement. It does not enumerate all598600 generators of Q(6,9), and does not claim a general N11 upper bound. N12's34 complete mandatory neighborhoods await a separately authorized full-source coverage test. No solver, graph BFS, incidence or WL rebuild, anchors, new graph or shared-document edit occurred. The task is stopped at the frozen pool.
