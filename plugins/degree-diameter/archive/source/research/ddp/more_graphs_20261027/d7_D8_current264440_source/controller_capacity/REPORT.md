# Fixed440state LEFT-law controller capacity

The prediction minimum>=641 is supported. Dynamic programming counts all2351462 reduced prefixes of length0 through8, including the empty prefix. The minimum endpoint count is 4964, first at slot2 `(phase0,normal11=2)`; maximum 6039. `RESULT.json` contains all440counts, the full histogram, per-depth endpoint counts and final last-dart counts. State encoding is `11*phase+normal11`.

The input is exactly the source projection: LEFT law `(n,I)(m,J)=(n+6^I*m,I+J)`, forward darts `(1,4),(3,9),(9,6)`, true inverse darts `(6,36),(4,31),(7,34)`, and self-inverse `(0,20)`. Each step excludes only the specific reverse of the last dart. The DP aggregates `(state,lastdart)` counts and does not materialize a word list.

The whole Python worker used 0.046728 CPU seconds, including preparation/output, under an enforced three-second RLIMIT_CPU hard limit; no compilation. It exited successfully with no live handle. Frozen PREDICTION, source, runner, log, complete results and terminal are saved.

This necessary count gate passes but makes no field-image or diameter assertion. Distinct projected words may lift to the same F641 value. No source/new graph, field evaluation, word list, BFS or solver was run here. The sole field641 producer receives the minimum slot before its image evaluation and inherits these raw counts; no separate construction-method row is created for this diagnostic.
