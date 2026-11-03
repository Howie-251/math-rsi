# Order61: prepared individual-row moment screen

Status: source prepared; no profile or full run. Root will arrange one independent source review and decide launch. This is the same weighted-defect quotient mechanism, not a new search queue. The existing size screen completed 36,143 inputs and retained 25,196; it will not be rerun.

Implementation follows the project `experiment-bridge` skill under the V3 mathematical adaptation: one exact local CPU computation, tiny sanity before execution, parseable results, bounded resource use, and root-managed local review/Gemini. No training, submission workflow, hashes, or new orchestration framework applies. `AUTO_DEPLOY=false` for this explicit preparation task; code review is handled by root.

## Exact necessary condition

For row i of size n_i and candidate diagonal d, detailed balance gives, for each j≠i,

g=gcd(n_i,n_j), a=n_j/g, b=n_i/g,
q_ij=a t_ij, q_ji=b t_ij,
0≤t_ij≤min(g, floor(8/a), floor(8/b)).

The bound t≤g is the actual simple-graph bound q_ij≤n_j and q_ji≤n_i. Row eight and the diagonal of Q²+Q−11I=1 nᵀ give

Σ a t_ij=8−d,
Σ a b t_ij²=n_i+11−d−d².

The integer DP stores a bitset of reachable second moments for each first sum 0,…,8. It processes every other component separately. Every contribution is nonnegative, so discarding first sums above8 or second moments above n_i+11 cannot remove a requested solution. The latter bound serves all candidate d simultaneously. Identical `(n_i, sorted other sizes)` rows share a bounded cache; this changes only runtime.

Remove d exactly when its requested state is unreachable. Apply the existing, already checked prefix/suffix trace DP to require Σd=8−(c−1)/2 and retain only values participating in some such sum. Individual rows can use incompatible choices for the shared t_ij. Surviving sizes therefore remain only a necessary domain; neither an abstract Q nor a graph is asserted.

## Inputs, checks, and outputs

Input is only `component_large_size_screen.result.json`. Require its complete status and the actual survivor counts for c=5,7,9,11,13,15,17:

327, 2310, 5587, 6588, 5378, 3247, 1759 (total25,196).

`--mode sanity` compares the entire reachable-state table with independent Cartesian-product enumeration for five tiny artificial rows. It does not rerun the old c=3 quotient enumeration and writes no result file.

`--mode profile` processes the first32 saved survivors per c (224 inputs), in saved order, under5 CPU seconds/15 wall seconds. It writes `.profile.json` and never labels this as full coverage. The profile can be used once to judge the proposed full budget; no automatic continuation is implemented.

`--mode full` processes all25,196 saved survivors once, under60 CPU seconds/90 wall seconds, single CPU1 and4 GiB. Internal stopping reserves time for output; a cooperative budget stop is recorded as partial; an OS hard kill or an exception outside the scan handler may leave no completed result file, with processed counts and the actual survivors of that processed prefix. It writes `.result.json`. No rerun, enlarged budget, or subsequent Q enumeration is automatic.

Per c, record processed tuples, nonempty individual-row domains, post-trace survivors, diagonal-value counts, CPU time, original source indices, and all retained sizes/domains. Save total CPU/wall and cache statistics. Timing starts before input parsing; stored timing is sampled before JSON serialization. Exact values and complete flags, not anticipated speed, determine coverage.

Prepared commands, requiring the corresponding root launch decision:

```bash
python computations/dd82/n61/component_row_moment_screen.py --mode sanity
python computations/dd82/n61/component_row_moment_screen.py --mode profile
python computations/dd82/n61/component_row_moment_screen.py --mode full
```

No claim follows yet about how many sizes survive. A complete zero result would exclude the input quotient-size domain by necessary conditions. A nonzero result gives a smaller domain for a separately reviewed compatibility problem; it does not authorize that next computation.

## Actual execution

Fresh code review: component_row_moment_code_review.md, no blocking mathematical defect; interruption wording above corrected. Sanity compared203 complete artificial assignments over5 rows, PASS. Profile224 sizes completed0.248125391 CPU/0.272114068 wall seconds, zero survivors in this selected prefix. Full run completed all25,196 inputs once:211 with nonempty row domains,142 after trace,4.428952082 CPU/4.446510348 wall seconds. All outputs are complete, no budget interruption. Gemini round3 reviewed the source and actual reduction. The later norm filter retained65 necessary size vectors. No joint Q or graph realization follows.
