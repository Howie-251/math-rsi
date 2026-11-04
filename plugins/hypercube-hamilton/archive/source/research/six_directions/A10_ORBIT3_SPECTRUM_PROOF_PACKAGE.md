# Final A10 orbit: exact short-forest spectrum interface

2026-11-01. ARIS proof-writer producer package. A separate fresh checker
must review this package and the separate universal rank argument.

## Claim and status

The original target remains unchanged: every arbitrary matching $F$ of
$K(Q_5)$ with holes

$$H=\{0,1,2,4,8,15,23,27,29,30\}$$

has a simple extending cycle on exactly $Q_5\setminus\{0\}$ with only
short new edges. This is the last five-geometry marked A10 orbit.

**PROVABLE AS STATED for the spectrum interface and positive-forest
witnesses below.** The universal assertion about all $F$ is conditional
here on the row-space coverage criterion in Section5. Its rank verification
belongs to a separate producer/checker package; no unverified rank assertion
is made in this file.

## Assumptions and notation

Let $V=\{0,\ldots,31\}$, $J=H\setminus\{0\}$ and $K=V\setminus H$.
The fixed terminal order is

$$3,5,6,7,9,10,11,12,13,14,16,17,18,19,20,21,22,24,25,26,28,31.$$

Thus $|J|=9$, $|K|=22$, and an original matching $F$ is any perfect
matching of $K$. Every $j\in J$ is free for $F$. A short complement $S$
uses only edges of $Q_5-0$, has degree two at every $j\in J$, and degree
one at every terminal $k\in K$.

The members of $J$ are pairwise nonadjacent. Let $\mathcal P$ consist
of all endpoint matchings obtained by compressing the components of such
$S$. For $F,P$ on $K$, their union is a **labeled multigraph**: an edge
occurring in both matchings is retained twice. Write $A[P,F]=1$ exactly
when that multigraph is connected. Since both matchings are perfect,
connectedness then means one alternating cycle.

## Proof strategy and dependencies

The interface and enumeration depend only on bit adjacency, elementary
degree counting, and perfect matchings. No A8, A10, prior failed face
template, or global matching sample is used. A future universal proof
combines these positive witnesses with a finite row-space certificate.

### 1. Every short complement is a forest of a fixed form

There is no edge of $S$ between two members of $J$. Every vertex of $K$
has $S$-degree one. Therefore a component containing a hole $j$ consists
exactly of the two-edge path through $j$, with two distinct terminals as
endpoints. No such path can meet another hole component, because a shared
terminal would have degree at least two. Every other component is a single
short edge between two terminals. In particular no component is a cycle.

There are nine hole paths, occupying eighteen terminals. The remaining
four terminals form exactly two one-edge components. Consequently $S$
has exactly twenty edges and eleven components, and compressing those
components gives a perfect matching $P$ on all twenty-two terminals.

### 2. Exact equivalence with the original extension problem

Suppose a desired cycle $C$ through $F$ exists. Let $S=E(C)\setminus F$.
The degree conditions above follow from $F$ covering exactly $K$ and
every other cycle edge being short. Section1 shows that $S$ has the required
form, so its compressed matching $P$ lies in $\mathcal P$. Contracting the
nine hole paths preserves connectedness; the resulting labeled graph is
$F\cup P$. Hence $A[P,F]=1$.

Conversely suppose a supplied short-forest witness $S$ compresses to $P$
and $A[P,F]=1$. Expand each $P$ edge to its recorded short path. All paths
have disjoint interiors and endpoints partition $K$, so expansion gives
one connected degree-two graph on exactly $V\setminus\{0\}$ containing
every edge of $F$. A direct $S$ edge coinciding with an $F$ edge would have
formed an isolated two-parallel-edge component in $F\cup P$, incompatible
with connectedness on twenty-two vertices. Thus no repeated physical edge
survives expansion. The result is a simple $31$-cycle and all its edges
outside $F$ belong to $S$, hence are short.

An $F$ edge equal to a compressed hole-path pair would instead expand to
a triangle component. The same connectedness test excludes it. Keeping the
two matching labels, rather than deleting duplicate endpoint pairs, is
therefore essential.

We have proved the exact equivalence

$$\forall F\quad \text{desired extension exists}
\quad\Longleftrightarrow\quad
\forall F\ \exists P\in\mathcal P:\ A[P,F]=1.$$

For sufficiency, a complete spectrum is unnecessary: any positive-witness
subfamily satisfying the right side suffices.

### 3. Complete small enumeration of the positive spectrum

The four odd holes are the unit vertices $1,2,4,8$. Their neighbors in
$Q_5-0$ are covered even weight-two vertices. For each unit hole choose
an unordered pair of distinct neighbors, with no terminal reused across
holes. Exhaustive recursion over these four choices gives $114$ low-side
assignments, occupying eight of the ten even terminals.

The five even holes are the weight-four vertices $15,23,27,29,30$.
Their covered short neighbors are weight-three vertices and $31$. Choose
two distinct covered neighbors at each hole, without reuse. Exhaustive
recursion over these five choices gives $564$ high-side assignments,
occupying ten odd terminals. The covered odd vertex $16$ is never used
on this side, as it has no short neighbor among the weight-four holes.

For every one of the $114\cdot564=64296$ low/high combinations, exactly
two even and two odd terminals remain. There are exactly two bijections
between the two pairs. Retain a bijection exactly when both edges are short.
Every short complement from Section1 occurs in this enumeration: each hole
component specifies its unique unordered neighbor pair, and its two isolated
components specify one of these bijections. The converse construction
directly satisfies every required degree and shortness condition.

The enumeration produces $17496$ forests and $17496$ distinct endpoint
pairings. Thus each stored $P$ has one stored $S$, and in this geometry
the compression map is injective. The universal proof needs neither this
injectivity nor the enumeration's completeness if it uses only a selected
positive family with independently checked witnesses.

Every $P$ has four even--even pairs, five odd--odd pairs, and two mixed
pairs. The partner of $16$ is one of $17,18,20,24$, each occurring $4374$
times. The partner of $31$ is a weight-three terminal: $7,11,13,14$ occur
$1764$ times each, and $19,21,22,25,26,28$ occur $1740$ times each.
These are exact full-spectrum statistics, not samples of original $F$.

The marked stabilizer permutes the first four coordinates and fixes bit
$16$. Its action on this spectrum is free, yielding $729$ orbits of size
$24$. This optional structure statistic plays no role in the logical
interface or a later rank proof.

### 4. Frozen positive-witness data and association format

The producer writes only files with prefix `A10_ORBIT3_SPECTRUM_`.

* `pairs.bin`: $17496$ records of $22$ bytes. Each record lists eleven
  unordered pairs using original Q5 labels, with endpoints sorted inside
  each pair and pairs sorted lexicographically. All records are themselves
  lexicographically sorted. Its SHA256 is
  `38164400c618448d1a2ebb188c2873100b0d8615c3528c1db5646b694bd12559`.
* `forests.bin`: $17496$ records of $40$ bytes. Each lists the twenty
  actual short edges of $S$, in the same canonical edge format. Record
  $i$ corresponds exactly to record $i$ of `pairs.bin`. Its SHA256 is
  `0b8a5a55059ab3b24fc8e31258a16b1b3732af6593f85c53223ca93ff869f965`.

Both displayed basenames abbreviate the full prefix. A selected rank basis
can therefore store just the zero-based record index of each selected $P$;
its complete short-forest witness is retrieved at offset $40i$ in the
forest file, and its pairing at offset $22i$ in the pair file. Explicit
selected pairing records can alternatively be located by binary search.

`A10_ORBIT3_SPECTRUM_verify.py` directly decodes every pair and forest record,
checks all actual edges are short, all vertices are in $Q_5-0$, all hole and
terminal degrees are exact, every component is a two- or three-vertex path,
all thirty-one vertices occur, and its compressed matching equals the
associated stored $P$. It checks all $17496$ records are distinct and sorted.
All checks pass. This is a producer-side check; independent acceptance is
still required and must not simply trust this status field.

### 5. Sufficient row-space coverage criterion

Let $\mathcal M$ be the finite set of every perfect matching on $K$ and
regard the full matrix $A$ above as a matrix over $\mathbb F_2$. Suppose
a positive-witness family $\mathcal B\subseteq\mathcal P$ has rows spanning
the row space of the full matching-connectivity matrix.

Fix any original matching $F$. Its column in the full matrix is nonzero:
label its pairs $(x_i,y_i)$ for $i=1,\ldots,11$ and choose the matching
with pairs $(y_i,x_{i+1})$, with cyclic indexing. Its union with $F$ is
one alternating cycle, so that row has entry one in column $F$.

If every selected row had entry zero at $F$, every linear combination
of selected rows would also have entry zero there. Row spanning would
force the entire column to be zero, contradicting the construction.
Therefore some $P\in\mathcal B$ has $A[P,F]=1$. Section2 expands its stored
forest and proves the desired cycle for this arbitrary $F$.

It follows that a separate proof of a global rank upper bound, together
with an equally large independent selected-row rank and these legal forest
witnesses, can close the original orbit without enumerating all original
matchings. A finite rank computation by itself must be linked to the full
matrix through a proved rank upper bound or explicit row-space factorization.
This package deliberately leaves that rank step to the separate proof.

## Corrections or missing assumptions

No extra assumption on $F$ was introduced. The only open input to a full
closure from this package is universal row-space coverage. The complete
spectrum's small size and positive forest records alone do not prove it.

## Open risks and remaining scope

The complete-enumeration and positive-witness claims require independent
checking. A later rank certificate must use exact $\mathbb F_2$ arithmetic,
the correct labeled-matching connectivity matrix and the fixed terminal
order, and must bind selected rows to the supplied forest witnesses.
Until the separate universal proof and fresh combined review pass, this
producer package does not declare full A10 or P6.
