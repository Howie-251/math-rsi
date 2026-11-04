# Proof Package: core 0 double-bridge transfer

Date: 2026-11-01. ARIS proof-writer. This is an additional local result;
no prior audit or global coverage files have been changed.

## Claim

Let $F$ be an arbitrary complete-graph matching on $V(Q_5)$ with holes
$\{0,1,2,7,11,13\}$. The prescribed omitted vertices are $1,2$.
If no edge of $F$ crosses coordinate zero, then there is a simple cycle
on $V(Q_5)\setminus\{1,2\}$ containing $F$, all of whose edges outside
$F$ are short hypercube edges.

The original universal core 0 claim, without the zero-crossing hypothesis,
is **NOT CURRENTLY JUSTIFIED** by this package. Full T15, eight-hole P6,
and full P6 remain open.

## Status

**PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION**: the displayed claim with
zero original crossings is proved relative to the explicitly imported Q4
finite classification. The new positive certificates have an independent
checker implemented separately from their producer; a fresh-context human
or agent audit of this package is still pending.

## Assumptions and notation

Cut coordinate zero. Label the one-face $A$ by $a\mapsto2a+1$ and the
zero-face $B$ by $b\mapsto2b$. Local labels belong to $\{0,\ldots,15\}$.
The holes are $\{0,3,5,6\}$ in $A$ and $\{0,1\}$ in $B$; omit $0_A$
and $1_B$. Thus $F_A$ has six edges and $F_B$ has seven edges. Required
edges may have arbitrary lengths and parity types.

For a matching $L$, write $L(v)$ for the mate of a covered vertex $v$.
A short edge joins binary labels differing in one bit. A path forest may
include an isolated vertex when explicitly stated.

## Proof strategy and dependency map

1. Import Q4 N14 from `Q4_CORE_AND_A4_SPLIT.md`: a matching with two
   same-parity holes has a 15-cycle omitting either specified hole.
2. Import the complete three-avoid Q4 classification checked in
   `q4_three_avoided_verification.json`: for omitted local vertices
   $(3,5,1)$ and $(3,6,1)$ there are respectively 33 and 70 bad matchings
   among all $10395$ matchings; all others have positive 13-cycle witnesses.
   Swapping coordinate bits one and two gives the $(5,6,1)$ family.
3. A two-bridge suppression handles every B matching except an explicitly
   enumerated set of 18; the remaining $18\cdot10395$ full inputs have
   directly checked Q5 positive certificates.

## Proof

### Step 1. The two-bridge suppression

Choose distinct $s,t\in\{3,5,6\}$ with $F_B(s)\ne t$. Let $u$ be the
remaining element of $\{3,5,6\}$. Add the artificial edge $st$ to $F_A$.
Its two holes are the even vertices $0,u$. N14 supplies a 15-cycle on
$A\setminus\{0_A\}$ containing this augmented matching. Deleting $st$
leaves a spanning $s_A$--$t_A$ path $P$ preserving $F_A$.

Set $k_s=F_B(s)$ and $k_t=F_B(t)$. Since $F_B(s)\ne t$, the four
vertices $s,t,k_s,k_t$ are distinct. Define
$$
L=F_B-\{sk_s,tk_t\}+\{k_sk_t\}.
$$
This is a six-edge matching with holes $0,1,s,t$. If it is outside the
appropriate exact Q4 negative table, it has a 13-cycle on
$B\setminus\{1_B,s_B,t_B\}$ containing $L$. Expand the artificial edge
$k_sk_t$ through the path
$$
k_s,s_B,s_A,P,t_A,t_B,k_t.
$$
Here the notation uses $P$ for its interior traversal, without repeating
its endpoints. The added cross-face edges $s_Bs_A,t_At_B$ are short.
The expansion restores both original B matching edges. Its internal
vertices consist of the 15 A vertices and $s_B,t_B$, disjoint from the
13-cycle. The expanded graph is one simple cycle with $30$ vertices,
retains every original required edge, and has only short new edges.

### Step 2. Exhausting the B choices

Independently enumerate all $13!!=135135$ perfect pairings of the B
covered set $\{0,\ldots,15\}\setminus\{0,1\}$. For each, try the three
unordered pairs in $\{3,5,6\}$, reject an existing B matching edge, and
test the suppressed matching against the complete negative table.
`verify_t15_core0_double_bridge.py` reconstructs the complete list using
the checked Q4 negative records, rather than trusting the producer list.
The exact histogram of successful choices is
$$
\{0:18,\ 1:310,\ 2:32587,\ 3:102220\}.
$$
Consequently Step 1 handles $135117$ B matchings for every one of the
$10395=11!!$ A matchings. No search claim about a failed B choice is
interpreted as a global obstruction.

### Step 3. The finite exceptional family

For each of the 18 remaining B matchings, enumerate all $10395$ A
matchings on the twelve nonhole A vertices. The producer
`t15_core0_double_bridge_residual.cpp` contracts required edges into
two-vertex blocks, adds the four retained free vertices as singleton
blocks, and searches oriented block orders joined by short edges.
All $187110$ cases have a positive witness. Total search nodes are
$33388547$; the largest single search uses $6795$ nodes. These counts
are diagnostics; the proof uses the positive witnesses only.

The binary file `t15_core0_double_bridge_residual.bin` has one 56-byte
record per input: 26 required-edge endpoint bytes, then 30 cycle vertex
bytes. Its SHA-256 is
`be5790d93f08f0c68726448be8c83273eeb188aeb0dbe22ffee1026e29bc74d1`.

The separately implemented checker regenerates every A pairing and the
complete exceptional B list. For every record it checks the exact input,
30 distinct vertices, exact support $V(Q_5)\setminus\{1,2\}$, containment
of all 13 original edges, and shortness of every other edge, including
the closing edge. It also checks exact file length and enumeration count.
All $187110$ certificates pass; there are no missing, exhausted, or
node-limited inputs. Thus these witnesses prove every exceptional input.

Steps 1--3 exhaust all zero-crossing inputs and prove the displayed claim.

## An arbitrary-even-crossing sufficient transfer

The following lemma isolates the positive-crossing obligation without
assuming that the successful choices always exist.

Let $C$ be the original crossing matching, with A endpoint set $X_A$.
Its cardinality $c$ is even, $0\le c\le12$. Choose any perfect pairing
$D$ of $X_A$ and distinct $s,t\in\{3,5,6\}$. Then
$F_A\cup D\cup\{st\}$ is a matching with same-parity holes $0,u$.
Use N14 to obtain a 15-cycle $K$ on $A\setminus\{0_A\}$ containing it.

Form $H$ by deleting $D\cup\{st\}$ from $K$, inserting all original
crossings $C$, both short bridges at $s,t$, and $F_B$. Include the retained
free vertex $0_B$ as an isolated vertex. If $H$ has no cycle component,
then every other component is a path with endpoints in
$B\setminus\{0_B,1_B,s_B,t_B\}$: all 15 A vertices and $s_B,t_B$ have
degree two, all twelve remaining covered B vertices have degree one, and
$0_B$ has degree zero. This degree statement still holds when $s_B$ or
$t_B$ is an original crossing endpoint. There is no assumption that these
two vertices are internally covered in B.

Compress the six nontrivial paths of $H$ to a matching $L$ on the twelve
endpoint vertices. If $L$ is outside the exact three-avoid negative table
for omitted $1,s,t$, a 13-cycle containing $L$ expands through those six
paths to a simple 30-cycle with the required support. Every original edge
is already in $H$, and all original edges survive expansion. Each new
edge is either a short A cycle edge, a short bridge, or a short B cycle
edge. This proves the sufficient transfer.

The condition that $H$ contain no cycle component must be checked. Omitting
it could leave an already closed component inaccessible to the B cycle.
The condition that $L$ avoid the negative table must also be checked.
N14 alone supplies neither condition.

## Corrections or missing assumptions

For positive crossings the unresolved universal claim is: every original
input admits some choice of $D$, $s,t$, and N14 cycle $K$ for which both
conditions of the sufficient transfer hold, or admits an alternative
construction. No such universal choice theorem is proved here.

There are only $140152$ possible internal A partial matchings. By crossing
count $c=0,2,4,6,8,10,12$, their counts are respectively
$10395,62370,51975,13860,1485,66,1$. These counts follow from
$\binom{12}{c}(11-c)!!$, with $(-1)!!=1$. However the B port locations and
the crossing bijection remain part of the input; enumerating A partials
alone cannot prove the full claim.

### A complete short-degree enumeration replaces artificial pairings

For fixed $s,t$ and remaining retained hole $u$, every possible A path
forest needed by the transfer has the form $F_A\cup N$, where $N$ consists
only of short edges and has degree two at $u$ and degree one at each of
the other fourteen vertices in $A\setminus\{0_A\}$. This follows by
subtracting the required-edge degree: each internally covered A vertex
already has one edge of $F_A$, each crossing port has its original
crossing, and $s,t$ have their short bridges; $u$ has none of those edges.

Conversely, any such $N$ disjoint from $F_A$ that makes $F_A\cup N$ a
forest has exactly the required endpoint set $X_A\cup\{s,t\}$. Thus it
can be tested in the same transfer without introducing any $D$.

There are exactly 116 candidate sets $N$ for each $u\in\{3,5,6\}$.
To enumerate them completely, choose the two distinct short neighbors of
$u$, delete those three vertices, and enumerate all short perfect
matchings of the remaining twelve vertices. This is exhaustive because
the two edges at $u$ are forced by that choice and all remaining degrees
are one. `t15_core0_short_degree_completions.json` contains all three
116-pattern lists, independently generated in Python with their degree
conditions checked. The C++ program
`t15_core0_port_spectrum_count.cpp` generates the same candidates and
enumerates the endpoint-pairing spectra over all A partial matchings.
Its output is diagnostic unless separately audited.

This reduces the per-input sufficient test to at most $3\cdot116=348$
candidate A forests, followed by the explicit cycle-component and bad-table
tests. It does **not** establish that one of the 348 candidates succeeds
for every B internal matching and every crossing bijection.

The complete producer count, saved in
`t15_core0_port_spectrum_count.json`, gives the following minima for the
largest endpoint-pairing spectrum among the three choices of $s,t$:

| $c$ | A partials | minimum best spectrum | maximum best spectrum |
|---:|---:|---:|---:|
|0|10395|1|1|
|2|62370|2|3|
|4|51975|7|15|
|6|13860|20|64|
|8|1485|41|98|
|10|66|77|116|
|12|1|116|116|

For $c=2$, the sum of best spectrum sizes is $187104=3\cdot62370-6$.
Since every best spectrum has size two or three, exactly six A partials
have best size two, and all other A partials admit all three abstract
four-endpoint pairings for some choice of $s,t$. This local assertion is
still a producer diagnostic pending independent verification. Whether
the three pairings suffice for every B input has not been established.

## Open risks and reproducibility

- Q4 N14 and the complete Q4 classification are imported proof inputs.
- The new independent checker verifies positive witnesses and exact
  enumeration; it does not replace the prior audit of the negative Q4
  classification.
- Fresh-context audit of this proof and checker remains pending.
- No positive-crossing core 0 closure, other entire-core closure, or
  new global eight-hole coverage count is claimed.

Run `g++ -O3 -std=c++17` on the producer source, then run its executable
with `t15_core0_double_bridge_b_inputs.txt`,
`t15_core0_double_bridge_residual.bin`, and
`t15_core0_double_bridge_residual_failures.txt` as its three arguments.
Run `python research/six_directions/verify_t15_core0_double_bridge.py` from
the workspace root for the independent check. The checked report is
`t15_core0_double_bridge_verification.json`.
