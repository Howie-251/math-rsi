# Order61 row-moment screen: code review

2026-10-13. Fresh same-family Codex review, **provisional** under the project-local `experiment-bridge` skill and V3 mathematical adaptation. This is not Gemini review or an execution result.

**Verdict: no blocking defect found for the planned sanity/profile/full sequence.** Reviewed `component_row_moment_screen.py`, its companion note, the source size-screen implementation including `trace_supported`, and the actual input JSON through summaries and one saved example per c. No screen, solver, external review, or Lean run was executed.

The input is marked complete and contains exactly 327, 2310, 5587, 6588, 5378, 3247, 1759 survivors for c=5,7,9,11,13,15,17, totaling 25,196. The saved size tuples are sorted, sum to 61, have c entries and c nonempty diagonal domains, and their diagonal values lie between 0 and 6. Thus the row indexing and domain bounds used here hold for the actual input.

The arithmetic is correct. Detailed balance parameterizes each pair by the same integer t: with g=gcd(n,h), a=h/g, b=n/g, the entries are at and bt. `options` uses exactly 0≤t≤min(g,⌊8/a⌋,⌊8/b⌋), including the simple-graph bound t≤g, and contributes (at, abt²). Consequently, selecting the state (8−d, n+11−d−d²) enforces both the row sum and the diagonal entry of Q²+Q−11I=1nᵀ.

The DP processes each other component once using a fresh successor table, so a single component cannot be reused. Its integer bitsets represent precisely the reachable pairs. Truncation at first sum 8 and second moment n+11 is valid because every contribution is nonnegative and every requested target is within those bounds. Negative targets are rejected. The bounded row cache preserves multiplicities and excludes only the current component; repeated equal sizes therefore do not change the domain.

The reused prefix/suffix trace routine retains exactly values that occur in some assignment summing to 8−(c−1)/2. One filtering pass suffices: every value in a witnessing assignment is itself supported by that same assignment. Combining this with independent row feasibility is a necessary screen only; the code and output explicitly leave shared t compatibility, off-diagonal polynomial equations, and graph realization unchecked.

Default profile coverage is the first 32 saved inputs per c (224 total); full coverage is all 25,196. Completion flags correctly separate selected-profile completion from full-input completion. Cooperative budget checks occur before processing a tuple and before each row; a stop during row computation does not count that unfinished tuple. Processed counts, survivor source indices, per-c counters, and cache statistics support inspection of the resulting prefix. Limits are 5 CPU/15 wall seconds for profile and 60 CPU/90 wall seconds for full, one selected CPU and 4 GiB; the reserves allow output time. The tiny sanity comparison independently enumerates the full reachable-state tables for its five artificial rows; root still needs to execute it and assess the profile before the full run.

**Non-blocking wording correction:** the companion note's “any interruption is recorded as partial” is stronger than the implementation. Handled cooperative budget expiration writes a partial result; hard CPU termination and interruptions outside the scan's `try` do not guarantee a JSON artifact. An asynchronous hard wall alarm can also interrupt per-tuple bookkeeping. Narrow the note to cooperative budget stops, and do not treat an abruptly interrupted process as completed coverage. No extra interruption machinery is needed for the planned bounded run.

No code changes were made. No conclusion about survivor counts or order61 existence follows before actual execution and review of its coverage.
