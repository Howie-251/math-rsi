# Complete free-C5 order-60 CNF: preparation and actual seed check

Proposed run: `dd82-v3-c5-full60-20261013`. Status:
**PREPARATION COMPLETE; FIRST SOLVER RUN UNKNOWN**. Preparation itself made no solver, graph search, or new BFS calls. The later actual call and its limits are recorded below; historical preparation counters remain unchanged.
This implements the experiment-bridge input/sanity stage under the V3
mathematical adaptation, with automatic deployment disabled by the
parent's explicit preparation-only scope. Direction review, code review
and any future solver authorization belong to the parent.


## Mechanism selection and actual first execution — 2026-10-13

This run uses the V3 mathematical adaptation of research-pipeline,
idea-discovery, experiment-bridge and auto-review-loop. The actual local
idea-discovery instructions were read for this change of mechanism. Existing
literature and both enriched case-study pages are reused: compact generation
must be connected to all real paths, and an unsuccessful restricted search
should motivate an actual change of representation. The free C5 action was
observed in a failed full graph; it is not inferred to occur in every target.
The full 354-orbit input releases the quotient simultaneously, unlike the
closed old fixed quotient or bounded repair neighborhoods. The previous
false-twin mechanism has a completed separate loop and is not reset here.

The task adaptation omits paper-novelty ranking, a new literature survey,
GPU pilots, publication scoring, rendering and manifest generation. No claim
of completing the unadapted idea-discovery pipeline or its publication gate
is made. The prepared reduction and this section are the compact research
contract: an actual verified order60 graph is success; prepared input,
quotient matrices and UNKNOWN are not. Universal order60 coverage is not
claimed for this chosen C5 domain.

Gemini direction review SUCCESS on thread
`96b3d1dd-a98e-4f75-8fb8-d0ec91fa37fe` accepted the candidate preservation and
one bounded full-domain test. Raw response:
`reviews/dd82/20261013_V3_c5_direction.json`. Requested and CLI-reported
model/effort are gemini-3.8-flash-high/high, not independently attested.
Its proposed cause of difficulty (path auxiliaries and symmetry) is a
hypothesis, not a measured causal diagnosis. A quotient has 66 off-diagonal
entries plus 12 internal choices, and candidate quotients alone are not lifts.

The sole first call actually finished with **UNKNOWN**, exit0,
118.335497 CPU seconds and 120.157846 wall seconds, maximum RSS86.90MB.
It encountered765014 conflicts,2571474 decisions and1189097455 propagations.
No proof output, model, new edge list or BFS was produced; no solver state
was retained. Exact command, bounds and result are in
`cyclic5_full60_run/launch.json`, `result.json` and `solver.log`.
No unchanged repeat is scheduled. The next actual modification follows the
reviewed quotient/voltage decomposition, with all final candidates still
subject to expanded-graph verification; its outcome is pending.

## Preparation evidence (preserved)

The input permits all simple graphs on twelve free C5 vertex orbits;
it fixes neither the quotient nor any Petersen or other old core.
After the necessary conditions and legitimate orbit relabelling below,
the CNF is satisfiable if and only if a degree-eight, diameter-two graph
on sixty vertices with this free C5 action exists.

## Complete orbit domain

Use vertices $v(a,t)=5a+t$, where $0\le a<12$ and $t\in\mathbb Z_5$,
and translation $v(a,t)\mapsto v(a,t+1)$. For $a<b$ and $d\in\mathbb Z_5$,
one primary variable selects the five edges
$\{v(a,t),v(b,t+d)\}$ for all $t$. For $a=b$ the two available variables
select the internal steps $\{\pm1\}$ and $\{\pm2\}$, each a five-cycle.
Thus there are $\binom{12}{2}5+12\cdot2=354$ variables.

The actual generator checks that these 354 disjoint sets each have five
edges and together partition all $\binom{60}{2}=1770$ unordered pairs.
It saves every pair's variable in `edge_variables.json` and every orbit,
its representative pair and all five expanded pairs in `palette.json`.
Every invariant simple graph is uniquely a union of these edge orbits.
Conversely every choice of the variables defines such a graph. Any free
C5 action on sixty vertices admits these coordinates by labelling its
twelve cycles and choosing an origin in each.

The prior diagnosis, switch and local quotient-profile sources were
inspected; no existing complete 354-variable CNF was found. The current
source is
[`cyclic5_full60_prepare.py`](../../../computations/dd82/construction/cyclic5_full60_prepare.py).
All actual products are in
[`cyclic5_full60_run/`](../../../computations/dd82/construction/cyclic5_full60_run/).

## Exact degrees, including repeated literals

Every target is eight-regular: a vertex of degree at most seven can
reach at most $1+8\cdot7=57$ vertices within distance two. For each orbit
representative $u=v(a,0)$, list all 59 other actual vertices $w$ and
the corresponding edge variable $x_{uw}$, retaining repeated variables.
The 55 cross-orbit variables occur once each. Each of the two internal
variables occurs twice, for the two neighbours in its cycle. Hence the
list length is 59, with 57 distinct variables, and its sum is exactly
the degree of $u$. Translation makes all five vertices of that orbit
have the same degree.

The existing `unary_thresholds` helper gives the exact thresholds

$$
s_{r,k}\quad\Longleftrightarrow\quad
\sum_{h=1}^{r}\ell_h\ge k,
\qquad 1\le k\le\min(r,9),
$$

using the bidirectional recurrence
$s_{r,k}\leftrightarrow(s_{r-1,k}\lor(\ell_r\land s_{r-1,k-1}))$,
with the corresponding boundary cases. This induction is valid for a
list of literals even when two positions contain the same literal.
It never replaces the list by a set. The two final units
$s_{59,8}$ and $\neg s_{59,9}$ enforce degree exactly eight.
The twelve counters produce 5,940 variables and 22,968 clauses.
Their complete input lists and threshold mappings are saved.

Eight-regularity implies 240 actual edges, hence 48 selected five-edge
orbits; these totals need no extra restriction.

## Complete distance-two coverage

Every unordered point-pair orbit has size five, including the internal
ones, because a nonidentity element of the odd group C5 cannot preserve
a two-element set. The palette therefore also supplies precisely 354
pair-orbit representatives. For each representative $\{u,v\}$ the CNF
requires

$$
x_{uv}\ \lor\
\bigvee_{w\in V\setminus\{u,v\}}
\left(x_{uw}\land x_{wv}\right).
$$

All 58 actual middle vertices are retained, with a separate Tseitin
variable and the three exact AND clauses for each route. If two route
variables have the same primary inputs, or the two inputs of a route
coincide, they are still encoded as their actual conjunctions. There
is no route deduplication or lost multiplicity assumption. A witness
to any route is a real two-edge path in the same expanded graph.
Distance is invariant under translation, so coverage of these 354
representatives covers all 1,770 pairs. Thus the degree and coverage
part is an exact encoding of the target in the complete orbit domain.

## Proved necessary clauses and legal normalization

The proofs used here are
[CYCLIC5_ORBIT_SWITCH_AND_QUOTIENT.md](CYCLIC5_ORBIT_SWITCH_AND_QUOTIENT.md)
and [CYCLIC5_K66_QUOTIENT_EXCLUSION.md](CYCLIC5_K66_QUOTIENT_EXCLUSION.md).
Their quotient defect is $D=M^2+M-7I-5J\ge0$, with row sum five and
even diagonal entries at most four. These imply:

- A vertex orbit cannot contain both internal cycles. Twelve binary
  clauses encode this necessary condition.
- At least two vertex orbits must be independent. Orbit labels are
  arbitrary, so label two such orbits 0 and 1. The four negative units
  on their two internal-step variables preserve at least one labelled
  representative of every target. They impose no choice of quotient.
- A cross-interface multiplicity $q$ is at most three. If either
  endpoint has an internal cycle, $q\le2$; if both do, $q\le1$.

For the last item, an independent-orbit row has external degree eight
and square sum at most sixteen; a multiplicity at least four would
force square sum at least $4^2+4=20$. An internal-degree-two row has
external degree six and square sum at most ten; multiplicity at least
three would force square sum at least $3^2+3=12$. If two internally
cyclic orbits shared multiplicity at least two, one row would have
diagonal defect at least two and that off-diagonal defect at least five,
exceeding its total five.

For each of 66 cross interfaces, the five variables obey:

1. A negative clause on each four-subset: five clauses enforcing
   $q\le3$.
2. For each of the four endpoint/step choices, a negative clause on
   that internal variable together with each cross three-subset:
   $4\cdot10=40$ guarded clauses enforcing $q\le2$.
3. For each of the four pairs of endpoint steps, a negative clause on
   those two internal variables together with each cross two-subset:
   $4\cdot10=40$ guarded clauses enforcing $q\le1$.

This adds $66(5+40+40)=5610$ clauses and no variables. Each possible
internal step separately supplies its guard; the condition that one
internal cycle is present has not been replaced by the stronger and
incorrect requirement that both internal variables be true. The full
clause list is saved in `necessary_multiplicity_clauses.json`.

No other row-type, fixed quotient, Fourier, spectral or old-edge
restriction is imposed. These necessary conditions may obstruct a
local-switch path through failed graphs, as the cited switch note
explains, but this CNF solves for all final primary assignments at once;
it is not traversing that local-switch state graph.

## Actual input and failed-seed sanity

| Item | Count |
| --- | ---: |
| Primary edge-orbit variables | 354 |
| Exact degree threshold variables | 5,940 |
| Actual two-edge path variables | 20,532 |
| Total variables | 26,826 |
| Exact degree clauses | 22,968 |
| At most one internal cycle clauses | 12 |
| Two normalized independent orbits units | 4 |
| Multiplicity clauses | 5,610 |
| Tseitin AND clauses | 61,596 |
| Pair-orbit coverage clauses | 354 |
| Total clauses | 90,544 |
| Actual DIMACS bytes | 1,470,321 |

The only imported archive definitions are `CNFEmitter`,
`unary_thresholds` and `add_iff_and`; no old branch, constraint set or
solver routine is executed. The source has no solver-launch code.

The seed is the actual 20-bad-pair graph from
`cyclic5_twelve_orbits60_signature_lift_run/seed20/seed.edges`, already
expressed as $5a+t$. From those edges the preparation reconstructs all
354 primary values, every counter threshold and every conjunction.
Reading and evaluating the actual DIMACS gives:

- all degree, AND, internal-at-most-one and 5,610 multiplicity clauses
  satisfied;
- exactly four false coverage clauses, at pair representatives
  $(40,57),(40,59),(45,52),(45,54)$, corresponding to zero-based
  palette indices 330, 332, 337, 339;
- exactly two false normalized-independence unit clauses, because this
  old seed has an internal cycle in every orbit.

There are therefore six false clauses in this diagnostic assignment,
not six bad-pair orbits. Translating the four failed coverage pairs
gives exactly twenty distinct failed pairs. The preparation reads the
previous independent BFS output and the saved old-to-new vertex map,
checks that the mapped original edge table equals this seed, and
compares the twenty pairs individually. They agree exactly. No BFS is
rerun, and the known-invalid seed is not presented as satisfying the
new independent-orbit condition.

The complete actual evidence is in `encoding.json`, `sanity.json`,
`seed.assignment.txt`, `coverage.json` and the variable/edge mappings.
The single preparation used 0.436524902 process CPU seconds and
0.573706076 wall seconds. It made zero solver calls and zero BFS calls.

The preparation result is an exact input plus a successful consistency
check. It neither constructs a target nor proves that the free-C5
family is empty. A future solver result would still require a complete
model-to-graph check or an appropriately verified UNSAT certificate,
and even a family exclusion would not settle unrestricted order 60.

## Prepared discovery runner — not executed

[`cyclic5_full60_solve.py`](../../../computations/dd82/construction/cyclic5_full60_solve.py)
is now prepared for one future call. Only its Python syntax was checked;
no solver, model decode or BFS was executed during this runner task.
The parent controls whether to launch it, using:

```sh
python computations/dd82/construction/cyclic5_full60_solve.py solve --cpu 0
```

The runner leaves the prepared input unchanged and passes no seed or
fixed quotient to CaDiCaL. It uses one pinned CPU, `-t 120` as the solver's
soft real-time limit, an OS CPU limit of 120 seconds, a 180-second
wrapper wall limit and 4 GiB address-space limit. Proof output is
disabled. A saved `launch.json` prevents a second solver call through
the same runner. UNKNOWN is retained as UNKNOWN; an UNSAT return is
RAW_UNSAT and supports no exclusion without a certificate.

For SAT, a separately bounded decoder requires a complete assignment
and evaluates every clause of the actual input. It expands the selected
primary orbit variables into all five edges of each orbit, verifies
48 selected orbits and 240 distinct edges, and saves the full parameters,
edge list and graph JSON. It then invokes the existing generic
`verify_hs_candidate.py` independently on that graph. Acceptance requires
exactly 60 vertices, 240 edges, every degree eight, no bad pair and
diameter at most two. The checker runs only if SAT decoding succeeds.
The preparation stage remains **PREPARED_NOT_RUN**.
