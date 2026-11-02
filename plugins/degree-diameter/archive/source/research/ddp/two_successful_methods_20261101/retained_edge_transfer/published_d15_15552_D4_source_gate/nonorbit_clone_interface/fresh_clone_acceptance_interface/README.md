# Prepared fresh acceptance interface — not executed

No new candidate is assumed. The old plane864 verifier was read as a
reference; its hardcoded I32, controller projection and all16416-root BFS
are not invoked by this interface. No graph, center list, solver return or
old data suite has been read during this preparation.

The new executable source is `verify_candidate.py`. It requires ROOT to
first observe an actual complete graph with more than864 roles and supply
its fresh budget. Its center input is either an ordered JSON integer list
or `{"centers": [old_label0, ...]}`. This order is binding: role j has new
label15552+j. It accepts arbitrary point-level centers, not only whole
controller planes. Old source rows have their explicit vertex label first;
the source is the accepted `source15552.author.adjlist.txt`.

Future invocation, only after ROOT gives the actual files and budget:

```
python verify_candidate.py \
  --source /absolute/repo/research/ddp/more_graphs_20261027/d15_D4_current15552/source15552.author.adjlist.txt \
  --candidate /absolute/new-case/complete.edges \
  --centers /absolute/new-case/ordered_centers.json \
  --out /absolute/new-case/independent_acceptance \
  --cpu-budget ROOT_ASSIGNED_SECONDS
```

The checker reads the accepted original source once and the new complete
edge file once; it checks the header, strict lex/simple body, exact116316
old edges, every full immutable old N, zero new-new edges, all labels and
all degrees<=16. It writes `ALL_NEW_ROLE_BINDINGS.tsv` with ordered actual
neighbors and actual load/degree histograms. It never substitutes producer
neighborhood data. It uses exact pointwise old degree+load, so it does not
exclude legal source-degree14/load2 cases by accident.

`STRUCTURE_PROOF_DRAFT.md` cites the closed source and generic Walk theorem,
handles adjacent/equal centers and all prefixes, and transports the source
old0/81 non-D3 witness by collapse. The actual checker would instantiate
that text only after full literal PASS. It performs zero BFS, field, solver,
Lean or reviews, and does not update any ROOT counts or Wiki. All resulting
PASS statements would still be pending ROOT acceptance and a separate new
concrete Lean goal.

Preparation is code-only and unexecuted; syntax/runtime/data checks remain
inside the future explicitly budgeted run. If the current global warm MIP
has no improvement, no data suite is run and no acceptance PASS is created.
