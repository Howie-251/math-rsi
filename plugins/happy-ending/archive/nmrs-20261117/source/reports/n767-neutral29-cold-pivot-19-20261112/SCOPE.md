# Exact scope and source-to-CNF coverage

This is a fresh nineteen-point necessary-subdomain probe, not a C_r state-cardinality campaign and not a replay or modification of a sealed job. Scientific execution is on the authoritative Linux server. The single physical order is `1,...,19`; true means red. There is exactly one color variable per physical triple. No role creates a second color variable for the same point.

The roles are `L=1..5`, `A=6..10`, `B=10..14`, `T=A union B=6..14`, `R=15..19`, with common pivot `10`. No permutation of this specified order is claimed.

The required red paths are `(1,2,3,4,5,6)`, `(14,15,16,17,18,19)`, `(6,7,8,9,10)` and `(10,11,12,13,14)`. Only their consecutive triple terms are asserted as units; packet heredity also makes every triple in each displayed path red. All additional predicates range over every increasing subset of the full nineteen-point domain:

1. Every four-point packet has at most one color change in `(abc,abd,acd,bcd)` order.
2. No red seven-point path; no blue six-point path.
3. No opposite-color paths with the same actual outer endpoints and length sum at least nine, including overlapping interiors.
4. No blue four ends in `A`; no blue four starts in `B`.
5. No blue five starts or ends in `T`.
6. No blue four with both outer endpoints in `T`. Internal points are never restricted to a role pool.
7. No red six with terminal `<10` and penultimate point in `T`.
8. No red six with initial point `>10` and second point in `T`.
9. `chi(x,5,6)=R` for `x=1,2,3,4`, and `chi(14,15,y)=R` for `y=16,17,18,19`. These are consequences of the frozen red arms but are retained as literal units.

The ambient blue-five supplies at the marked arm pairs are consumed only through predicate 9. The CNF does not assert that these blue fives lie in the nineteen points. It does not require the nine T labels to possess both red-six anchors inside this subdomain, and does not prohibit all blue fives. It adds no local owner, full-population, geometric-realizability or extension assumptions.

## Literal clauses and projection equivalence

For a path `p`, write `r(p)` for its consecutive physical triple variables. Red means all these variables are true; blue means all are false. A forbidden red path gives `OR(-r(p))`; a forbidden blue path gives `OR(r(p))`. Fixed red paths give positive unit clauses. Packet clauses forbid exactly the eight four-bit words having at least two changes.

Weak seven uses three endpoint auxiliaries `E_k(s,t)`, for `k=4,5,6`. For **every** actual candidate red k-path `p` with outer pair `(s,t)`, add

`OR(-r(p)) OR E_k(s,t)`.

For **every** candidate blue `(9-k)`-path `q` with the same outer pair, add

`-E_k(s,t) OR OR(r(q))`.

No auxiliary is counted or reported as exact existence. Any coloring satisfying the listed path predicates extends to the CNF by assigning `E_k(s,t)` its true physical red-path-existence value. Conversely a satisfying assignment forbids all three same-endpoint color-length splits. Since red seven and blue six are forbidden, every possible larger weak violation shortens, retaining its actual endpoints, to one of `R6+B3`, `R5+B4`, `R4+B5` (or already forbidden red seven/blue six). Shortening follows packet heredity. Thus the color projection is exactly the stated finite necessary-condition model.

`verify.py --schema` imports no builder and independently reconstructs the complete expected normalized clause set, including every path in each predicate. It requires exact equality to the saved DIMACS and checks variable/header bounds. `verify.py --sat` independently checks the complete DIMACS assignment, then enumerates **every** increasing subset of size at least two, reconstructs all actual monochromatic paths, all exact same-endpoint length sets, packets and every stated role/fan condition. It saves the complete 969-triple color table and actual-path catalog.

## Execution and evidence interpretation

The existing workspace Kissat binary is invoked as a controlled external process with a sixty-second internal budget and a seventy-five-second wall limit. Each process owns a fresh process group; timeout sends TERM followed by KILL. An UNSAT result is provisional unless the bound `drat-trim` invocation exits successfully with `s VERIFIED`; solver exit 20 and no external timeout are also required. A SAT result is accepted only after independent literal and physical checks, with solver exit 10 and no timeout. Every source, CNF, solver/checker binary, log and result is hash-bound.

A verified SAT witness demonstrates only compatibility of these necessary nineteen-point consequences. It does not extend the labels to ambient through/neutral roles in a seventy-five-point input, prove existence of the neutral29 layer, or establish geometric realizability. A checked UNSAT result excludes the entire specified fixed-order finite model; its transfer to an original mathematical input additionally uses the caller's proved extraction of these nineteen labels and constraints. No external review or global acceptance is performed.
