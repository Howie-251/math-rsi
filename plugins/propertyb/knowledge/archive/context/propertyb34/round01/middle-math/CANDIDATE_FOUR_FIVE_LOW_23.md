# Four or five degree-six vertices at 23 points

## Claim and status

A simple five-uniform hypergraph on 23 vertices with 34 edges and covering
every pair has Property B if exactly four or exactly five vertices have
degree six. This is a complete paper candidate with exact finite local
certificates. Lean implementation and cross-family review remain pending.
Together with `CANDIDATE_LOW_BRANCHES.md`, it covers at least four lows.

Write $r$ for the number of six-degree vertices. Every other vertex has
degree at least seven. Let $Q$ be those of degree seven or eight. Counting
degrees gives $|Q|\ge13$ for $r=4$ and $|Q|\ge11$ for $r=5$: if $h$ external
vertices have degree at least nine, then respectively
$146\ge7\cdot19+2h$ and $140\ge7\cdot18+2h$.
Every six-degree vertex has total codegree excess
$\sum_{y\ne x}(\lambda(x,y)-1)=2$.

## Four lows and common-unit external locks

Choose any four lows $L$. At least $|Q|-8$ members of $Q$ are unit with all
of $L$; call their full set $U$. Thus $|U|\ge5$ when $r=4$ and
$|U|\ge3$ when $r=5$.

The complete four-low inventory at 23 points has 50 orbits, eight of which
remain after the strict four-lock bounds. Their coverage and independent
arithmetic are already recorded in `CANDIDATE_LOW_BRANCHES.md`.
Add any actual $u\in U$. For each degree 7 or 8, complete trace promotion
gives 50 labelled extensions and 32 degree-preserving orbits. All but five
degree-seven and six degree-eight profiles are strict. Every surviving
profile has all low-low pairs unit. Evidence: `MIXED_LOW_23_4.json`.

This conclusion holds for every selected four-low set, because each has a
nonempty $U$. Consequently all pairs among the $r$ lows are unit, including
when $r=5$.

## Simultaneous restrictions on pairs and triples from U

Add a second member of $U$ without imposing any high-high unit condition.
The only initial caps are actual degrees and the old and new codegree-excess
budgets. Both one-high projections must be among the above residues.
The complete inventory has 1615 labelled promotions, 1575 after projection
filtering, and 543 degree-preserving orbits. Of these, 512 have strict exact
certificates. Every residual pair obeys

$$\lambda(u,w)=\begin{cases}2,&d(u)=d(w)=8,\\1,&\text{otherwise.}\end{cases}$$

There are 13 residual $(7,7)$ types, one $(7,8)$ type and 17 $(8,8)$ types.
The mixed-degree residual has no trace of size at least three. The evidence
is `TWO_HIGH_23_4.json`.

Now add a third actual member of $U$, using the preceding pair restrictions
and requiring every two-high projection to remain residual. The complete
promotion/filter domain has 5212 labelled promotions, 1403 retained labels
and 241 orbits. Exactly 240 are strict. The unique remaining profile has
high degrees $(7,8,8)$ and the following exact traces:

- every low-low pair and every low-high pair occurs once;
- the pairs joining the seven-degree point to either eight-degree point
  occur once; the pair of eights occurs twice;
- each high singleton occurs once, no low singleton occurs;
- there are nine empty traces, and no trace of size at least three.

These give 34 edges, low degrees six and high degrees 7,8,8. In particular,
every three members of $U$ in a putative counterexample must consist of
exactly one seven-degree point and two eight-degree points.
Evidence: `MORE_HIGH_23_4_3.json`.

## Exactly four lows

Here $|U|\ge5$, so choose four distinct members. If $k$ of them have degree
seven, counting seven-degree appearances in their four triples gives $3k$.
Every triple would have exactly one, which instead gives four appearances.
The equation $3k=4$ is impossible. Thus a strict local certificate exists.

## Exactly five lows

Choose four of them and three actual members of their $U$, which exists
because $|U|\ge3$. A strict seven-lock profile already finishes the proof.
Otherwise the selected seven locks have the unique residual above. Add the
actual fifth low. Its codegrees to the first four lows are one, as already
proved. No unit assumption is imposed on its codegrees to the three high
locks; its total excess is at most two.

Complete promotion of this new six-degree lock gives 876 labelled inputs
and 63 degree-preserving orbits. Every orbit has a strict exact certificate,
with maximum $4707/5005$. Evidence: `FIFTH_LOW_23.json`.

## Coverage and arithmetic

For every extension, the promotion variable $p_T$ counts actual old-trace
edges containing the new lock, so $0\le p_T\le n_T$. The new singleton and
old empty count are determined by the actual new degree. All actual inputs
obey these constraints. Projection sums exact trace counts and preserves all
34 edges; discarding a strict projection is sound because that projection
already supplies a coloring. Relabeling only permutes equal-degree roles and
transports certificate positions.

Strict subset-layout bounds were independently recomputed from labelled
injections by `SubsetEngine.verify`. The retained mixed-layout certificates
were checked with exact rational weights, both directed slot probabilities,
actual profile degrees, avoided quotas and capacity penalties by
`verify_joint_layout.verify`. The shared bad-vector weak-dual lemma then
gives a strict bound for at least one actual layout. The original
locked-permutation lemmas turn this into a proper coloring.

These are complete local trace domains, not enumerations of whole
hypergraphs. Their general coverage and actual-H connection still need Lean.
