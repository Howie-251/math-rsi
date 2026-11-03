# Full independent free pins: target scope and inversion lex leader

The independent model uses one selector for each actual free old vertex:648 or810 selectors, each with cost1, total at most15. It must impose coverage of every15552 or102060 old target. Exact identical support rows may be deduplicated, but the earlier target inversion-orbit folding is no longer valid: the selected neighbor set need not be invariant.

The source automorphism i,x -> i,-x permutes free pins and target vertices and preserves the cardinality bound. If a set S covers every target, so does -S. A lex leader may therefore choose one of these two solutions without loss. This is different from requiring S=-S, which is a genuine restriction and is not imposed on this new model.

List all nonzero free pairs {p_j,-p_j}, orient each by minimum old label, and order the pairs by that minimum. Write x_j for the selector of the smaller label and y_j for its partner. Zero pins are fixed by inversion and omitted from this comparison. Require that in the first pair with x_j different from y_j, x_j=1 and y_j=0. Exactly one of S and -S satisfies this for every asymmetric S; symmetric S satisfy the lex condition vacuously. With the usual Boolean order0<1 this chooses the lexicographically greater bitvector, not the lesser. Either consistent orientation is sound.

An exact prefix implementation introduces equality bits q_j and prefix bits p_j:

    p_0 = True,
    q_j <-> (x_j <-> y_j),
    p_(j+1) <-> (p_j AND q_j),
    NOT p_j OR x_j OR NOT y_j.

The equality equivalence has four clauses:

    (NOT q_j OR NOT x_j OR y_j)
    (NOT q_j OR x_j OR NOT y_j)
    (q_j OR x_j OR y_j)
    (q_j OR NOT x_j OR NOT y_j).

The prefix equivalence has three:

    (NOT p_(j+1) OR p_j)
    (NOT p_(j+1) OR q_j)
    (NOT p_j OR NOT q_j OR p_(j+1)).

These establish by induction that p_j is true exactly when all preceding pairs are equal. In particular p_final is true exactly when S=-S, regardless of the zero selectors. The bits cannot be left free or treated as only an informal witness. An equivalent implementation without separate q_j is acceptable if it enforces the same bidirectional definition.

The proposed additional clause NOT p_final deliberately excludes all inversion-invariant sets. That is a separate cut, not part of the without-loss lex argument. It is justified for this experiment only by inheriting the previous complete full-inversion model's raw UNSAT receipts. The new actual CNF then represents asymmetric free-pin sets modulo the lex symmetry; its union with the previously tested invariant domain covers all free-pin single-append possibilities. Because those previous negative results have no independently checked proof artifact, the combined conclusion retains that uncertified computational qualification. The new CNF by itself must not be described as an unmodified full-family test.

This cut does not affect a positive witness's mathematical validation: expand only the648/810 original pin selectors, never the prefix/equality/cardinality auxiliaries. Check at most15 distinct pins, actual old degree14 and complete original-target cached OR. Adding the new point to exactly those pins gives its distance1+d_G(S,t), while old-old paths remain. A passed full cover therefore yields a complete degree15/D4 orD5 extension independently of any trust in the negative-domain cut.

If lex is omitted, the independent model is still complete and only explores both orientations. If NOT p_final is omitted, the lex model itself covers the entire free-pin family up to inversion, without needing the earlier negative assumption. Both are valid alternatives; the executed producer must record which one it uses. No new ports, coordinates, source edges, balls or solver runs are introduced by this paper.

Evidence: ../full_free_directions/ANALYSIS_DIRECTION_COVER.md for source inversion and exact free labels; ../full_inversion_port_cover/RESULT.json for the inherited invariant-domain negative receipts; this directory's actual PREDICTION and producer code for the chosen encoding. This is a paper review with zero numerical experiment, BFS, cache OR or solver call.

Static implementation observation: prepare.py and the relevant run.py construction/decoding block were read once. They use all original n targets without inversion folding, arbitrary-width exact support deduplication, individual cost1 pin selectors and the stated five-clause direct prefix equivalence. The initial prefix is true, final prefix false, and lex orientation selects the smaller label at the first differing pair. The SAT branch expands only original selectors, checks all support clauses and the complete original-n ball OR, then checks actual old pin degrees before edge export. No blocking issue was found. This was a static reading only, with zero calibration, solver or BFS run.

Inherited terminal outcome: both scheduled60-second calls return UNKNOWN, with solver CPU59.902467 and60.032781; the two-source aggregate is127.968020737, under160. No candidate or source was skipped. Consequently the asymmetric and unrestricted free-pin append domains remain open. The actual receipt is inherited, not recomputed by this review, and no further timer is started.
