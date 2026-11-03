# Simultaneous boundary reconstruction: actual diagnostic and exact input

## Proposed change and current status

Replace a sequence of individual two-edge switches by one simultaneous
completion of every edge touching a data-derived active set $R$. Keep
only the induced graph on $O=V\setminus R$ fixed. Require exact degree
eight and genuine distance-two coverage on the completed graph.

The recommended first input is the saved order58 graph with21 bad pairs,
using **all24 endpoints** of those pairs as $R$. This permits $1,092$
binary edge choices jointly; it does not restrict the number of deleted
old HS edges. No completion solver or optimization was launched by this
subtask. The diagnostics below are actual reads and exact finite counts.

## Why the accepted weighted trajectory did not settle this input

The inspected `fullgraph60_weighted.cpp` evaluates both replacements of
every disjoint pair of edges, then chooses one weighted improvement.
Its one completed trajectory used59.006266 CPU seconds and accepted449
moves; its best accepted raw score remained20. The disposition in
`FULLGRAPH60_WEIGHTED_PREPARATION.md` closes additional computation in
that unchanged mechanism. This proposal does not change pair weights,
extend that trajectory, or treat its accepted minimum as a lower bound.

The current edge tables supply a more specific diagnostic than bad-set
migration. In each of the original20-bad, alternative20-bad, and final
26-bad graphs, the bad-pair graph is bipartite with minimum vertex cover
of size10. Taking the deterministic cover returned by an augmenting-path
matching gives these active sets:

- Original and alternative20: $\{40,41,\ldots,49\}$.
- Final26: $\{21,22,26,28,33,37,39,49,50,51\}$.

In all three cases the complementary50 vertices have induced degree7,
zero common neighbors on each adjacent pair, and one on each nonadjacent
pair. These actual Moore50 parameters were checked directly. The
induced-HS obstruction in
[CONSTRUCTION_CASE_STUDY_ACTIONS_20261011.md](CONSTRUCTION_CASE_STUDY_ACTIONS_20261011.md)
uses exactly these parameters, so no new group or isomorphism catalogue
is required to apply its counting proof. A completion that freezes one
of those50-point complements is already excluded.

In particular the final26 graph retains a different such induced core,
despite losing its original fiber representation. This is a **new
diagnosis**, consistent with the earlier report, which excluded only
the particular original C5 permutation and original fiber structure.

## Actual active-set comparison

The order58 source was read literally from
`computations/dd82/construction/twin59_to_58_deflation_run/component.path1.edges`.
Its bad graph has a minimum vertex cover
$\{40,41,42,44,46,48,52,53\}$ of size8. This smaller patch is also
invalid: after fixing its50-point complement, vertices3,12,45 have no
active ports. Their outside neighbors have respectively7,7,5 total
active ports, fewer than the required8 active vertices.

The reason is exact: if $r_o=0$, every path of length at most two from
$o\in O$ to $R$ must use an outside neighbor $v\in N_{G[O]}(o)$ and
one of its $r_v$ ports. Hence every completion requires
$$\sum_{v\in N_{G[O]}(o)}r_v\geq |R|.$$
The minimum bad-pair cover is therefore not a suitable completion
patch in any of these four tested cases.

For the all-endpoint patches requested by the root, the actual counts
are instead:

| Source | $|R|,|O|$ | Fixed edges in $O$ | Outside residual degrees | Outside pairs needing an $R$ witness |
|---|---|---:|---|---:|
| Original20 / alternative20, order60 |20,40|120|40 of degree2|60|
| Final26, order60 |25,35|94|13 of degree2,22 of degree3|86|
| Saved21, order58 |24,34|84|7 of degree2,18 of degree3,9 of degree4|138|

All these residual degrees are positive; the zero-port obstruction
above is absent. Every listed outside-pair obligation has an actual
common neighbor in $R$ in the saved graph. Full lists of those witnesses
are retained. Also every $R$–$O$ pair is initially covered. This follows
both from the actual bad-pair lists and from the definition of $R$ as
their entire endpoint set: initial failures lie only in $R\times R$.
Thus the original boundary is already a simultaneous witness for all
degree, outside-pair, and mixed-pair constraints, while the joint move
must repair the remaining internal pairs without losing them.

For the order58 source, explicitly
$$R=\{3,9,12,14,28,29,40,41,42,43,44,45,46,47,
48,49,50,51,52,53,54,55,56,57\}.$$
Its fixed34-point graph agrees with the restriction of the original
HS reference, mapped from original60 labels by deleting41 and42.
Only84 of the reference175 HS edges are frozen; the other91 have at
least one endpoint in $R$ and are free. The model therefore does not
freeze an induced HS50 or impose an old two-deletion limit. This removes
those direct known obstructions; it is not evidence that a completion
exists or that no further fixed-core obstruction is possible.

## Exact simultaneous completion domain

Let $Q$ be the fixed adjacency on $O$, $b_{oa}\in\{0,1\}$ for every
$o\in O,a\in R$, and $h_{ab}=h_{ba}\in\{0,1\}$ for distinct
$a,b\in R$. These are the actual adjacency entries of a single graph,
not separately guessed path or defect data. Set $h_{aa}=0$ and impose
$$\sum_{a\in R}b_{oa}=8-d_Q(o),\qquad
\sum_{o\in O}b_{oa}+\sum_{b\in R\setminus\{a\}}h_{ab}=8.$$
No per-active-vertex cut degree is fixed.

Outside pairs covered by a fixed edge or a fixed two-step $Q$ path
need no further constraint. For each remaining outside pair $o,o'$,
require
$$\bigvee_{a\in R}(b_{oa}\land b_{o'a}).$$
For every mixed pair $o,a$, require
$$b_{oa}\ \lor\!\bigvee_{v\in N_Q(o)}b_{va}
\ \lor\!\bigvee_{b\in R\setminus\{a\}}(b_{ob}\land h_{ba}).$$
For every distinct active pair $a,b$, require
$$h_{ab}\ \lor\!\bigvee_{o\in O}(b_{oa}\land b_{ob})
\ \lor\!\bigvee_{c\in R\setminus\{a,b\}}(h_{ac}\land h_{cb}).$$
These three cases list every possible intermediate vertex. Together
with the degree equations they are necessary and sufficient for a
simple8-regular diameter-two completion with this exact frozen $Q$.
Tseitin variables, if used, must express the actual two-edge conjunctions.

The order58 input has816 cut variables and276 active-pair variables,
and138+816+276=1,230 nonconstant pair-coverage constraints before
auxiliary encoding. Its degree equations fix the total cut size104 and
the active-edge count44, but leave their incidence pattern free. Up to
all148 existing nonfixed edges may be replaced simultaneously. A path
of intermediate two-switch states, a raw-score improvement at each
step, a fixed fiber partition, or a fixed group action is not required.

## Bounded next execution and outcome boundary

The next executable input is this one order58 frozen34-point instance.
Prepare the simplified exact CNF and check the existing graph assignment:
all degree and auxiliary definitions must hold, and coverage must fail
on exactly its21 saved bad pairs. A single root-managed bounded solve
can then seek a full graph, with no automatic patch-size ladder or
restart queue. SAT requires an expanded edge list and independent full
BFS. Checked UNSAT closes only this frozen34-point completion family;
UNKNOWN leaves it undecided. Neither result is an unrestricted order58
or58–61 exclusion.

## Actual diagnostic receipts

Sources and outputs under `computations/dd82/construction/`:

- `fullgraph60_boundary_patch_diagnostic.py` and `.result.json`: actual
  graph domains, bad-pair covers, fixed-edge lists and outside obligations.
- `fullgraph60_boundary_patch_witnesses.json`: every outside obligation
  with its actual common active neighbors, plus the exact84/91 split of
  fixed/free reference HS edges for the order58 input.

The first three-graph diagnostic used0.002614990 internal CPU seconds;
the extension to the order58 source and minimum-cover checks used
0.003319226; the outside-witness/reference-edge check used0.003349707.
Total measured internal diagnostic CPU was0.009283923 seconds, excluding
interpreter startup. Their measured internal wall times were respectively
0.005240981,0.006282628,0.003345340 seconds. No new graph was generated,
no neighborhood search or BFS was repeated, and no solver was launched.
