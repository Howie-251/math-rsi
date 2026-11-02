# Static review: packed independent-port support beyond64 selectors

Verdict: no blocking issue found in the packed support and variable mapping in run.py. This review executes no array calculation, graph, ball traversal, solver or candidate.

For m=72 or90 independent port selectors, each unpacked ball is an n-entry uint8 row. Stacking then transposing gives shape(n,m), with column i corresponding exactly to groups[i], whose selector is i+1. Packing along axis1 with bitorder='little' places this selector's support in bit i of the target row. Converting the packed bytes with int.from_bytes(...,'little') preserves the entire72/90-bit integer. The lowbit.bit_length() extraction therefore emits the correct1-based selector id, including selectors above64. Row deduplication changes neither support nor clause semantics.

The90-column case pads the last byte with six zero bits. They do not create selector literals91..96. Counter auxiliaries start after m, so cover literals and counter variables remain disjoint. All cardinality inputs are cost-one single-port selectors here; the same position-based sequential counter correctly enforces at most15.

SAT reconstruction also uses Python arbitrary-width integers for chosen selectors. It checks every deduplicated support clause, expands to unique actual pins, enforces cardinality<=15 and then recomputes the explicit OR of the selected saved R3/R4 balls against the complete n-bit target set. Port eligibility and source/cache binding are inherited from the previously saved eligible-ball data, as in the symmetry model.

This is the independent-pin model on the same canonical zero/plus/minus port domain, without the pair-selection tie. It does not claim to cover all free source pins. No result is inferred from UNKNOWN, and this static review does not check an UNSAT proof. The already executed short-call records and the parent's separately recorded same-CNF continuation are not modified here.
