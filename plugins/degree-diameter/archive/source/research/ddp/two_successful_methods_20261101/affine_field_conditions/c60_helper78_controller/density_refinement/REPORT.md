# Necessary-density refinement: bounded UNKNOWN; all continuation ends

The separately authorized refined solve returned **UNKNOWN**, exit 0.
It used 25.982805 CPU seconds and 26.072252 wall seconds. New preparation,
including exact triple classification, used 0.086470454 CPU seconds.
The new worker total was 26.079807853 CPU seconds; combined with the
previous 59.218354853, the tracked scope total is **85.298162706 CPU
seconds**, below 90. There were exactly two solver calls in the combined
scope: the original bounded solve and this new necessary-cut refinement.
No third timer or further numerical continuation is authorized or run.

The exact source classification retained 19,260 of 34,220 triples:
8,120 were nonindependent; among the 26,100 independent triples, 6,840
had neighbor union below 14. Their full lists and neighbor-union
histogram are in `TRIPLE_FILTER.json`. The accepted source remains
attributed to Bhakar.

The refined CNF has 44,460 variables and 228,927 clauses. It keeps the
previous 145,047 clauses and appends only the proved necessary cuts:
1,800 independence binary clauses and 82,080 forbidden-triple ternary
clauses for helpers 6..17. Independent paper and actual-code reviews
both passed. No helper number, source, pin loads, or fixed H component
structure changed.

The solution file again contains only `c UNKNOWN`, with no partial pin
partition. No controller, port table, 56,862-vertex fiber, accepted graph,
or record claim resulted. Both bounded UNKNOWN results leave this fixed
H18 case open; neither is an UNSAT exclusion. Canonical CNFs, logs,
commands, final solver statistics, and timing records remain saved in
their separate directories. The original UNKNOWN artifacts were not
modified by this refinement.

All numerical work in this H18 scope has ended. No old fiber BFS, Lean,
Gemini, installation, Wiki, global STATE, or other global edits occurred.
