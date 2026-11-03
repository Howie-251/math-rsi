# Brown+hub: complete three-edge switch neighborhood

## Claim and status

The fixed labeled seed is the previously verified Brown graph on $57$ vertices,
with a new vertex $57$ adjacent to its eight degree-$7$ vertices. It is a simple
$8$-regular graph on $58$ vertices with $232$ edges. Its score, the number of
unordered vertex pairs at distance greater than $2$, is $21$.

The mathematical move and scoring lemmas below are **PROVABLE AS STATED**.
The numerical conclusion is a completed finite local-neighborhood computation,
with a saved full graph and independent BFS validation of its minimum example.
It is not a Lean theorem or an arbitrary-graph nonexistence result.

Among **all** moves that delete three vertex-disjoint seed edges and replace them
by a different perfect matching whose union with the deleted matching is a
six-cycle, subject to simplicity, the minimum score is $34$. There are no
score-preserving or improving moves of this specified kind. A move retaining
the hub's eight neighbors has score at least $45$.

## Assumptions and notation

Let $G$ be the fixed seed and let $E(G)$ denote its edges. A move chooses a
three-edge matching $D\subset E(G)$ with six-element endpoint set $U$, and a
perfect matching $F$ on $U$. It produces
$H=(V(G),(E(G)\setminus D)\cup F)$.

For a graph $K$, define
$$
M_K(u)=V(K)\setminus\left(\{u\}\cup N_K(u)
                 \cup\bigcup_{v\in N_K(u)}N_K(v)\right),
\qquad Q(K)=\frac12\sum_u |M_K(u)|.
$$
Thus $Q(K)$ counts precisely the unordered pairs not connected by a path of
length at most $2$, including disconnected pairs if any.

The graph source is `computations/dd82/construction/brown57.edges`. The
neighborhood program uses its edge list, adds the hub, checks every resulting
degree is $8$, and saves the explicit seed before computation.

## Strategy and dependencies

1. Characterize the eight replacement matching patterns on each endpoint set.
2. Prove the score update can be computed using only the six changed rows.
3. Enumerate every eligible deleted matching and every replacement pattern,
   recording all legal moves and the score histogram.
4. Read the saved minimum example as a fresh edge list and run independent
   all-pairs BFS. This checks its actual graph and score; it does not independently
   rerun the entire neighborhood enumeration.

## Move legality and coverage

**Step 1: replacement patterns.** A perfect matching $F$ sharing no edge with
$D$ makes $D\cup F$ a simple $2$-regular graph on six vertices, with edges
alternating between the two matchings. All its cycles have even length at least
$4$. There is only one possible cycle decomposition on six vertices under these
conditions: a single cycle of length $6$.

There are $15$ perfect matchings on six labeled vertices. For each of the three
edges of $D$, exactly three perfect matchings contain that edge. Intersections
for two specified edges, and for all three, each have size one. Consequently
the number avoiding all edges of $D$ is
$$15-(3\cdot3-3+1)=8.$$
The source generates these eight patterns recursively by pairing the smallest
unused endpoint with each allowed partner. The original deleted pairs are
positions $(0,1),(2,3),(4,5)$, and pairing within one such pair is forbidden.

**Step 2: simplicity and degrees.** The six endpoints are distinct. Both $D$
and $F$ have exactly one incident edge at each endpoint. Requiring
$F\cap E(G)=\varnothing$ guarantees all three additions are new edges;
loops and repeated added edges are already excluded by the matching. Hence
$H$ is simple and has exactly the same degree sequence as $G$.

The source temporarily deletes $D$ before checking the new edges. This is
equivalent to checking against the original graph because the eight patterns
already satisfy $F\cap D=\varnothing$.

**Step 3: completeness and multiplicities.** The seed has $232$ edges. Three
nested loops with strictly increasing indices visit all
$\binom{232}{3}=2,054,360$ unordered triples, discarding exactly those with
fewer than six distinct endpoints. For each surviving triple the eight
patterns above cover every permitted replacement, and the nonedge test is the
only additional rejection. No resulting graph is duplicated: its edge
difference from $G$ determines both $D$ and $F$ uniquely.

This coverage concerns three *vertex-disjoint* removed edges. It does not assert
coverage of every conceivable degree-preserving operation changing three
edges with shared endpoints, or of longer sequences of moves.

## Exact score update

**Step 4: unaffected pairs.** If $u,v\notin U$, both adjacency rows
$N_H(u)$ and $N_H(v)$ equal their rows in $G$. The pair's adjacency and the
intersection of these two neighbor sets are unchanged, so its distance-at-most-
two status is unchanged. Only pairs with at least one endpoint in $U$ can
change score.

**Step 5: count affected pairs once.** Define
$$
T_K(U)=\sum_{u\in U}|M_K(u)|
       -\frac12\sum_{u\in U}|M_K(u)\cap U|.
$$
An uncovered pair with precisely one endpoint in $U$ contributes once to the
first sum and zero to the second. An uncovered pair with both endpoints in $U$
contributes twice to the first sum and once after the factor $1/2$ in the
second. Thus $T_K(U)$ counts each affected uncovered unordered pair exactly
once, and
$$Q(H)=Q(G)-T_G(U)+T_H(U).$$
This identity is the program's score update. Each of the six new rows computes
the complete union of its eight neighbors' adjacency rows, with no approximation.
As an implementation check, $146$ sampled incremental scores were compared
against a complete $58$-row score and all agreed.

## Completed computation

Standalone one-thread C++17 source:
`computations/dd82/construction/brown58_three_switch.cpp`.

The first bounded run used an $8$-second limit and completed in $1.13627$ wall
seconds, $1.13617$ CPU seconds. No further run or annealing was needed.

| Scope | Legal moves | Minimum score |
|---|---:|---:|
| All permitted three-edge switches | 9,537,248 | 34 |
| Hub's incident edge changes | 983,136 | 34 |
| Hub's neighbor set stays fixed | 8,554,112 | 45 |

There were $1,698,648$ vertex-disjoint deleted-edge triples. The JSON report
records `complete: true`, all histogram entries, the actual runtime, and the
minimum move. The minimum $34$ occurs for $4,368$ distinct legal moves.

One minimum example deletes
$$\{\{0,49\},\{2,24\},\{33,57\}\}$$
and adds
$$\{\{0,2\},\{49,33\},\{24,57\}\}.$$
It repairs the three previously uncovered pairs
$\{27,57\},\{45,57\},\{55,57\}$ and creates $16$ new uncovered pairs,
giving $21-3+16=34$.

The independent verifier imports no generator or switch code. It reads each
saved edge list into sets and runs ordinary queue-based BFS from every vertex.
Both saved graphs are simple with $58$ vertices, $232$ edges and all degrees $8$.
The seed's distance histogram is $(232,1400,21)$ for distances $(1,2,3)$;
the minimum neighbor's is $(232,1387,34)$. Both have diameter $3$, not $2$.
The verifier's exit status $1$ is its expected signal that the requested
degree-$8$, diameter-$2$ condition fails.

Artifacts, all under `computations/dd82/construction/`:

- `brown58_three_switch.json`: full neighborhood counts and score histograms.
- `brown58_three_switch.seed.edges` and `.seed.bfs.json`: complete seed and BFS.
- `brown58_three_switch.best_neighbor.edges` and `.best_neighbor.bfs.json`:
  complete minimum neighbor and BFS.
- `brown58_three_switch.independent_comparison.json`: edge differences and
  repaired/new missing pairs recomputed from saved artifacts.

Reproduction from the project root:

```sh
g++ -O3 -std=c++17 -Wall -Wextra computations/dd82/construction/brown58_three_switch.cpp -o /tmp/dd82_brown58_three_switch
/tmp/dd82_brown58_three_switch computations/dd82/construction/brown57.edges 8 computations/dd82/construction/brown58_three_switch
python computations/dd82/construction/verify_edges.py computations/dd82/construction/brown58_three_switch.best_neighbor.edges --out computations/dd82/construction/brown58_three_switch.best_neighbor.bfs.json
```

## Interpretation and limits

The previously completed two-edge-switch neighborhood had minimum $26$ from
this seed. The present change of move neighborhood addresses the possibility
that one three-edge move might improve or preserve its score even though every
two-edge switch worsens it. The completed result excludes that possibility for
the specified six-cycle moves; the smallest one-step score increase is $13$.
It does not exclude an improving multi-step path whose first move increases the
score, other seeds, other move classes, or any arbitrary order-$58$ graph.
No new upper bound on $N(8,2)$ follows. No unmodified long annealing run was made.
