# Three low vertices at 22 points; six low vertices at 23 points

## Claim

Let $H$ be a finite simple five-uniform hypergraph, with exactly $34$ edges,
covering every vertex pair. Each of the following hypotheses implies Property B:

1. $|V(H)|=22$ and at least three vertices have degree six.
2. $|V(H)|=23$ and at least six vertices have degree six.

## Status

PROVABLE AS STATED as a paper candidate with explicit finite local certificates.
This is not the whole 22/23-point theorem or a Lean result. The general
locked-permutation probability lemmas, avoided bad-pair quotas, and exact
mixed-layout inequality are the dependencies.

## Assumptions, notation, and strategy

For a selected lock set $S$, let $n_T$ count actual edges with exact trace
$T\subseteq S$. Let $d(x)$ and $\lambda(x,y)$ denote degree and codegree.
Simplicity is used in the bad-link quota; pair
coverage gives $\lambda\ge1$. A degree-six center satisfies

$$\sum_{y\ne x}(\lambda(x,y)-1)=25-v.$$

We first classify four low locks using this budget. For 23 points the few
non-strict types are required to hold for every selected low subset; consecutive
extensions either supply a strict bound or force one six-low type. One actual
additional vertex of degree seven or eight then finishes that type.

## Dependency map

Actual degree and pair budgets → complete local trace inventories → concrete
strict position/dual certificates → conditional permutation failure below one
→ an actual proper coloring. The 23-point branch additionally uses simultaneous
restrictions on all low subsets and a degree-counted extra lock.

## Proof

### 1. Complete four-low inventory

Choose four degree-six vertices. Write $\lambda_{ij}\ge1$ for their six
codegrees. Their internal excess at each center is at most $25-v$. Choose
nonnegative exact triple multiplicities $t_{ijk}$ and exact quadruple
multiplicity $q$. Recover exact pair, singleton and empty multiplicities by

$$n_{ij}=\lambda_{ij}-q-\sum_{T\supseteq\{i,j\},\ |T|=3}t_T,$$
$$n_i=6-\sum_{T\ni i,\ |T|\ge2}n_T,\qquad
 n_\varnothing=34-\sum_{T\ne\varnothing}n_T.$$

Retain precisely nonnegative values. Every actual input is retained because
these are identities; the finite ranges follow from the pair budgets.
Relabelings transport both actual traces and the certificate positions.

For $v=22$, the $214$ labelled pair budgets give $2066$ nonnegative labelled
profiles, or $169$ orbits. Every orbit has a strict exact certificate; the
largest bound is $1412912767/1430000000<1$. Thus four actual low locks settle
the at-least-four part of Claim 1.

For $v=23$, the $56$ budgets give $464$ labelled profiles, or $50$ orbits.
Exactly $42$ orbits have the retained strict certificates. In a counterexample,
every four-low restriction must therefore belong to the remaining eight.

The independently implemented first-uncovered-pair recursion removes a block
containing that pair, decreases its pair budgets, and repeats until all budgets
are zero. Any actual nonempty remaining inventory has a block containing the
selected positive pair, so induction proves exhaustiveness. It recovers exactly
the same $2066/169$ and $464/50$ domains. Evidence is
`FOUR_LOW_{22,23}_COVERAGE.json`, with arithmetic in the corresponding
`FOUR_LOW_*_VERIFIED.json`.

### 1b. Exactly three lows at 22 points

If a degree-seven vertex exists, select it with the three lows. Each low has
internal excess at most three, and the seven-degree point has internal excess
at most seven. The same four-lock reconstruction gives $3175$ labelled inputs
and $687$ orbits preserving the degree roles. Every orbit is strict and its
saved certificate was independently replayed. The complete evidence is
`THREE_LOW_FULL_22.json`; no unit-cross-pair assumption is used here.

Otherwise the remaining nineteen vertices all have degree eight: their degrees
are at least eight and sum to $170-18=152=19\cdot8$. For each of the three lows,
at most three other vertices are nonunit neighbors. At least ten degree-eight
vertices are therefore unit with all three lows. Denote this set by $U$.

For a selected $u\in U$, the full three-low/one-unit-eight domain has $53$
orbits; all but four are strict. These four all have unit low-low codegrees.
Their exact counts and the strict alternatives are in `MIXED_LOW_22.json`.
If no strict alternative applies, consider any two distinct $u,w\in U$.
Their codegree may initially be any integer from one through eight. Complete
promotion of $w$ into the old four-lock inventory, with both four-lock
projections residual, gives $90$ orbits. The proof of this enumeration is the
promotion argument in Step 2, using degree eight for the old and new high
locks and degree six for the other locks. The codegree ranges are not restricted
to unit or double pairs by assumption.

Of these $90$ orbits, $88$ are strict. Both remaining exact inventories have
$n_{\{u,w\}}=2$ and every trace containing $u,w$ together with any low equal to
zero. Thus in a counterexample, for every pair $u,w\in U$, no actual edge
contains that pair and a low. Fix one low $x$. Each of its six incident edges
contains at most one member of $U$. But $\lambda(x,u)=1$ for every $u\in U$,
so these six edges must cover at least ten distinct $U$ vertices. This is
impossible. Evidence is `THREE_LOW_NO_SEVEN_FULL_22.json`, which contains the
actual colored profiles and independently replayed strict witnesses. Claim 1
now follows in all cases.

### 2. Complete addition of a low lock

Given an actual $s$-lock inventory, add another degree-six vertex $x$.
For each positive old trace $T$ of size at most four, let $p_T$ be the number
of its edges also containing $x$. Necessarily $0\le p_T\le n_T$; promotion
decreases $n_T$ by $p_T$ and gives trace $T\cup\{x\}$ multiplicity $p_T$.
There are $6-\sum p_T$ further edges through $x$ avoiding the old locks, so
this number becomes the singleton-$x$ multiplicity and is subtracted from the
old empty count. All results must be nonnegative.

The new codegrees are $\lambda(i,x)=\sum_{T\ni i}p_T$. Require them to be at
least one and to respect each old center's remaining excess and the new
center's total internal excess of at most two. These constraints are necessary
for every actual extension. Conversely the generator visits every allowed
integer promotion vector. It need not assert global realizability.

Every old-size subset of an actual counterexample must still be a residual
profile. Projecting the new traces onto each such subset is therefore a valid
filter. Exact trace projection adds multiplicities, never discards an edge.

Starting with the eight four-low residues, the five-low extension/filter leaves
$12$ orbits, of which $10$ have strict certificates. Extending the two remaining
five-low orbits gives $780$ labelled extensions; all-subset filtering leaves
$13$ labels in three orbits. Two are strict. Thus every selected six-low set
in a putative counterexample must have the single remaining type:

- split the six labels into two triples $A,B$;
- each triple is an exact trace of multiplicity one;
- each of the nine cross pairs is an exact trace of multiplicity one;
- each singleton has multiplicity two;
- the empty trace has multiplicity eleven.

These sum to $2+9+12+11=34$ edges and degree six at every lock.
The evidence is `EXTEND_LOW_23_{5,6}.json` and their exact verification files.

### 3. Seven low vertices are impossible in the residual regime

The complete extension of the unique six-low type by a seventh low vertex has
$1432$ labelled promotion vectors. None has all its six-low projections equal
to the required residual orbit. The preceding promotion and projection
arguments prove that every actual seven-low configuration would have appeared
in this test. `EXTEND_LOW_23_7.json` records the empty filtered domain.
Consequently, if there are at least seven lows, a strict certificate is already
available on some subset.

### 4. Exactly six lows have a suitable seventh lock

Assume exactly six degree-six vertices and the residual type above. The other
$17$ vertices have total degree $170-36=134$ and each has degree at least seven.
If $h$ of them have degree at least nine, then $134\ge119+2h$, hence $h\le7$.
At least ten external vertices consequently have degree seven or eight; call
their set $Q$.

All low-low codegrees in the residual type equal one. Each low has total
codegree excess two, giving total excess twelve from the six lows to all
external vertices. If every vertex of $Q$ consumed at least two units, the
total would be at least twenty. Hence there is $x\in Q$ with

$$\sum_{i\in S}(\lambda(i,x)-1)\le1.$$

Its six low incidences are all unit, except possibly one codegree two. Its
degree is seven or eight. The same promotion construction, with singleton
multiplicity $d(x)-\sum p_T$, yields $331$ labelled extensions and $18$ orbits
for each of those two degrees. Every one of the $36$ colored profiles has a
strict exact certificate. This finishes the residual six-low case and Claim 2.

Actual counts, positions and independently replayed mixed-layout coefficients
are saved in `MIXED_LOW_23.json`. Arithmetic success is used only after the
degree-counted actual lock and the exhaustive promotion argument above.

### 5. Why a strict certificate gives the original conclusion

For each fixed actual $H$, the corresponding bad-pair count vector is fixed
before layouts are varied. Each layout gives its own conditional probability
upper bound $U_\ell(z)$. Direct certificates show one such bound is below one;
mixed certificates use nonnegative rational weights of sum one to show their
weighted average is below one. In the latter case some layout has its own
bound below one. The established greedy-coloring counting lemma then gives a
successful permutation and an actual two-coloring of $H$. This does not
identify probabilities from different conditional sample spaces.

## Remaining work

Cross-family review and Lean connections are pending. In particular the
seven-low empty residual catalogue must be kernel connected to all actual
projections, rather than supplied as an unexplained assumption. The new
weighted-overlap quota, when used by a certificate, is proved separately in
`WEIGHTED_OVERLAP_QUOTA.md`. No whole-hypergraph search is a premise.
