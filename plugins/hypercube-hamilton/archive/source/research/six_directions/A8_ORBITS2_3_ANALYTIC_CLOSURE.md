# A8 residual orbits 2 and 3: analytic closure by closed matching sets

Date: 2026-11-01. ARIS proof-writer package; fresh independent review pending.

## Claim

Write $V(Q_5)=\{0,\ldots,31\}$ in binary coordinates. Let $F$ be an
arbitrary matching of the complete graph on these vertices whose hole
set is one of

$$H_2=\{0,3,5,6,15,25,26,28\},$$
$$H_3=\{0,3,5,15,23,25,26,28\}.$$

There is a simple cycle on exactly $V(Q_5)\setminus\{0\}$ containing
every edge of $F$ and using only short edges outside $F$. The same
conclusion holds under every coordinate permutation of either marked
hole geometry. These are the second and third residual orbits in
`A8_geometry_census.json`, of respective sizes 20 and 30.

## Status

**PROVABLE AS STATED**, relative to the previously certified Q4 inputs
listed below. This package proves the two specified orbits and makes
no claim that the remaining A8 orbits or full A8 are closed. Independent
proof-checker review of this new argument is pending.

## Assumptions, notation, and dependency map

No required edge is assumed short or bipartite. The five numerical even
holes are called majority holes, the three odd holes minority holes.
The forbidden hole is $v=0$. In both cases put $W=\{25,26,28\}$,
and write $Z=H_j\setminus(W\cup\{0\})$ for the four available majority
holes. Direct bit geometry shows no vertex of $Z$ is short-adjacent
to a vertex of $W$; this is a property of these particular geometries,
not an extra condition on the arbitrary matching.

For a cut bit $b\in\{1,2,4,8,16\}$, let $A$ be its zero face and
$B$ its one face. The internal matching edges are $F_A,F_B$, the
crossing matching is $C$, its size is $c$, and its endpoint sets are
$X_A,X_B$. A short mirror across the cut is denoted $\bar t=t\oplus b$.

The imported inputs are:

1. GQ4-avoid in `Q4_GENERAL_AUGMENTATION.md`: arbitrary hole counts
   of imbalance two permit a face cycle avoiding a specified majority hole.
2. The exact Q4 T15 classification in `Q4_T15_CLASSIFICATION.md`.
3. The exact Q4 T63 classification in `A8_Q4_T63_CLASSIFICATION.md`.

The latter input and the double/three-bridge path construction were
independently accepted in `A8_BRIDGE_INPUTS_REVIEW.md`. We reproduce
the needed construction in Step 1, including its extension to the
delta-five cut, so it is not being invoked outside its former delta-minus-one
statement. The small checker `A8_orbits2_3_geometry_check.py` verifies
the bit identities and orbit sizes used below; it enumerates no matching
instances and is not a substitute for the analytic matching argument.

## Proof strategy

Assume no required cycle exists. If all bridge choices at a suitable
cut fail, their fixed obstructions and nonfixed endpoint restrictions
force an eight-vertex covered set to be closed under the matching.
Applying this at bits 8 and 16 yields three disjoint closed four-vertex
sets. The remaining covered set is then closed too. Other cuts forbid
its matching from changing selected low bits, leaving vertex 1 with
no possible distinct partner. This contradicts the original matching.

## Proof

### Step 1. A common sufficient bridge construction

Select $k$ original holes $t_1,\ldots,t_k\ne0$ in $A$, where $k=2$
or $3$, and put $Y=\{\bar t_1,\ldots,\bar t_k\}$. In each application
below these mirrors are original covered vertices, and removing the
selected holes leaves original $A$ hole excess two in the majority class.
Consequently $T=X_A\cup\{t_1,\ldots,t_k\}$ has even size. Write
$d=|T|/2$.

Define the graph

$$G=F_B\cup C\cup\{t_i\bar t_i:1\le i\le k\}.$$

Every vertex of $T$ has degree one. Only the vertices of $Y$ have
degree two in $B$; each such vertex is incident to a bridge leading
to a degree-one endpoint in $T$. Hence $G$ is a path forest, not a
graph with a closed component. Pair the two $T$ endpoints of every
$T$--$T$ component to get a matching $P$ on $T$. Every other component
meeting $T$ has a terminal in $B$ and a root in $T$.

Suppose the chosen local completion theorem on $B$ has exactly one
possible obstruction edge $pq$, with $p,q$ original covered vertices
outside $Y$. Suppose $pq\notin F_B$. If both $p,q$ are rooted terminals,
add to $P$ the edge between their roots, obtaining $J$; otherwise put
$J=P$. This is a matching, because roots of terminal components do
not occur in $P$. Write $e=|J|-|P|\in\{0,1\}$.

If there is a terminal outside $\{p,q\}$, the number of terminal roots,
$2d-2|P|$, is even and strictly larger than $2e$. Thus $d>|J|$.
Complete $J$ to a perfect matching $D$ on $T$. GQ4-avoid applies to
$F_A\cup D$, giving a cycle $K$ on $A\setminus\{0\}$. Delete $D$.
The resulting path forest pairs $T$ by a matching $Q$ after each path
is contracted; the multigraph $Q\cup D$ is one cycle. Since $J$ is
a proper subset of $D$, the graph $Q\cup J$ has no cycle.

Attach $G$ to the uncontracted paths. A closed component would give
a cycle in $Q\cup P\subseteq Q\cup J$, and is therefore impossible.
The result compresses to a matching $L$ on $B$ whose holes are exactly
the original $B$ holes together with $Y$. Its suppressed interiors
contain every vertex of $A\setminus\{0\}$ and every vertex of $Y$.

The edge $pq$ does not belong to $L$. If either endpoint belongs to
a component of $G$ not meeting $T$, that component is an original
edge of $F_B$, and $pq\notin F_B$ excludes it. Such a component cannot
be a longer $B$--$B$ path because traversing a bridge vertex leads
to a degree-one endpoint in $T$. In the other case both endpoints
are rooted terminals. A compressed $pq$ edge would give a path
between their roots in $Q\cup P$; together with the prescribed extra
edge of $J$, this would be a cycle in $Q\cup J$, a contradiction.

The local T15 or T63 theorem therefore supplies a cycle on $B\setminus Y$
containing $L$. Expanding the compressed paths restores every suppressed
vertex exactly once and gives the required cycle on $Q_5\setminus\{0\}$.
All original edges survive, and all other edges are short: the only
additional original-face edges come from GQ4-avoid and the local theorem,
and every selected bridge is short.

We have proved: if the required global cycle does not exist and
$pq\notin F_B$, there is no rooted terminal outside $\{p,q\}$.
Equivalently, with $S=Y\cup\{p,q\}$,

$$X_B\subseteq S,\qquad
F_B(y)\in S\text{ for every }y\in Y\text{ internally covered in }B.\tag{R}$$

For this equivalence, a port outside $S$ is itself an impermissible
terminal, and an internally matched bridge with partner outside $S$
produces that partner as an impermissible terminal. These exhaust all
components leading from $T$ to a nonbridge $B$ terminal. This reasoning
handles all mixtures of port and internal bridge vertices, with no
restriction on the crossing count.

### Step 2. How failure of every choice forces a closed set

We use (R) in three kinds of cut, summarized next. Here $M$ is the
complete candidate set of covered bridge mirrors, $k$ are selected,
and $S$ is independent of which $k$ are selected.

| geometry | cut bit | $M$ | $k$ | $S$ | distinguished vertex |
|---|---:|---|---:|---|---:|
| $H_2$ | 8 | $11,13,14$ | 2 | $11,13,14,31$ | 31 |
| $H_2$ | 16 | $19,21,22,31$ | 3 | $19,21,22,23,31$ | 23 |
| $H_3$ | 8 | $11,13,31$ | 2 | $11,13,14,31$ | 14 |
| $H_3$ | 16 | $19,21,31$ | 2 | $19,21,22,31$ | 22 |

We verify the local theorem conditions in Steps 3--4. In every row,
$S=M\cup\{r\}$ where $r$ is the distinguished vertex. For each
choice of selected bridge vertices $Y\subset M$, its possible obstruction
edge is $r u$, where $u$ is the unique unselected member of $M$.
These obstruction edges all meet $r$, so at most one can belong to
the matching $F$. There are three choices when $|M|=3$ and four when
$|M|=4$. After discarding the at most one fixed-obstruction choice,
the remaining choices still cover every member of $M$: two distinct
two-subsets of a three-set cover it, and three distinct three-subsets
of a four-set cover it.

Assume the global cycle does not exist. Apply (R) to every nonfixed
choice. We get $X_B\subseteq S$ and, by the preceding choice coverage,
every internally matched vertex of $M$ has its partner in $S$. The
only vertex of $S$ that could still be internally matched to $B\setminus S$
is $r$.

All vertices of $S$ are covered. For the three rows with $|S|=4$,
the face $A$ has four original holes, so $c$ is even. For the row
with $|S|=5$, $A$ has five original holes, so $c$ is odd. Hence
$|S|-c$ is even in every row. Exactly $c$ vertices of $S$ are ports,
because all $B$ ports lie in $S$. If $r$ were matched to $B\setminus S$,
the remaining internally matched vertices of $S$ would number
$|S|-c-1$, which is odd. They cannot all be paired within $S$; yet
no other vertex of $S$ is allowed an external partner. This contradiction
shows that $r$ does not escape either.

Every covered vertex of $B\setminus S$ therefore has its partner in
$B\setminus S$: it is not a port and cannot be paired to $S$. Thus

$$C_b=(B\setminus S)\setminus H_j$$

is closed under the original matching. Notice that this parity argument
also covers zero crossings and every port/internal mixture. It does
not assume that the distinguished vertex was selected as a bridge.

### Step 3. Verification of the two-bridge local inputs

In each two-bridge row of the table, $A$ has four majority holes and
no minority holes; $B$ has the one remaining majority hole $a$ and
all three minority holes. The candidates $M$ are mirrors of the three
available majority holes in $A$ other than $0$. Selecting two candidates
consumes two majority holes in $A$, leaving exactly two majority holes,
so GQ4-avoid applies in Step 1.

For $H_2$ at bit 8 and for $H_3$ at bit 8 the singleton hole is
$a=15$, with its four neighbors in the face $B$ equal to
$\{11,13,14,31\}=S$. For $H_3$ at bit 16 the singleton is $a=23$,
whose four neighbors in $B$ are $\{19,21,22,31\}=S$.
After compression, the holes of $L$ are the singleton majority hole
$a$ and five minority holes (the original three plus the two selected
bridge vertices). T15 is therefore exactly applicable with those
two selected vertices avoided. Since they both neighbor $a$, its sole
possible obstruction is the matching edge on the two remaining members
of $S$, namely $r u$ as in Step 2. All vertices of $S$ are originally
covered, as can also be read directly from $H_2,H_3$.

### Step 4. Full three-bridge verification for the delta-five cut

For $H_2$ at bit 16, all five majority holes $0,3,5,6,15$ lie in $A$,
and all three minority holes lie in $B$. The mirrors of the four
available majority holes are

$$M=\{19,21,22,31\}.$$

These are covered vertices and are exactly the four neighbors of
$a=23$ within $B$. Choose any three of the four original available
majority holes for the bridges. Pairing their endpoints and all ports
in $D$ removes three majority holes from $A$, leaving exactly two
majority holes, one of which is $0$. Thus the target-face cycle required
in Step 1 follows from GQ4-avoid for every pairing $D$.

The compressed $B$ matching has six minority holes: the original
three odd holes and the three odd bridge vertices. Avoid precisely
the bridge vertices and apply T63. The three chosen vertices have
unique common neighbor $a=23$ in the face $B$. Its only remaining
neighbor is the unselected candidate $u\in M$. Thus the unique possible
T63 obstruction is $23\,u$. This is precisely the edge $r u$ in Step 2,
with $S=M\cup\{23\}$ of size five.

The graph argument in Step 1 is valid for these majority-to-minority
bridges as well as for minority-to-majority bridges. It uses the
post-consumption imbalance in $A$, the hole pattern of $L$, distinct
covered mirror vertices, and path compression; every one of these
conditions has just been checked. No assumption that $A$ originally
contains minority holes, or that $c$ exceeds a threshold, occurs.

### Step 5. Two closed eight-sets yield three closed four-sets

Steps 2--4, under the supposition that there is no global cycle, give
for both geometries the same closed sets

$$C_8=\{8,9,10,12,24,27,29,30\},$$
$$C_{16}=\{16,17,18,20,24,27,29,30\}.$$

The intersection of two closed matching sets is closed, since the
partner of each point must lie in both. Their differences are also
closed: if a point of $C_8\setminus C_{16}$ had its partner in the
intersection, that partner would have its unique partner outside the
closed set $C_{16}$, a contradiction. The same reasoning applies to
$C_{16}\setminus C_8$. Therefore the following disjoint four-sets are
all closed:

$$I=\{24,27,29,30\},\quad D_8=\{8,9,10,12\},\quad
D_{16}=\{16,17,18,20\}.$$

Put $U=I\cup D_8\cup D_{16}$. The other twelve covered vertices
$R_j=Q_5\setminus(H_j\cup U)$ are closed as well, since their partners
cannot enter any of the three closed four-sets or the original holes.

### Step 6. Delta-zero cuts restrict the matching on the remaining set

The needed cuts and local data are:

| geometry | cut bit | selected bridge mirrors $Y$ | singleton $a$ | remaining neighbor edge $pq$ | $S=Y\cup\{p,q\}$ |
|---|---:|---|---:|---|---|
| $H_2$ | 1 | $27,29$ | 25 | $9\,17$ | $9,17,27,29$ |
| both | 2 | $27,30$ | 26 | $10\,18$ | $10,18,27,30$ |
| both | 4 | $29,30$ | 28 | $12\,20$ | $12,20,29,30$ |

For each listed cut, $A$ has two majority holes, including $0$, and
two minority holes. Select both minority holes as the bridges. Their
mirrors in the table are covered. After consumption $A$ has two majority
holes, so GQ4-avoid applies. The original $B$ holes have three majority
holes and one minority singleton $a$; the bridge mirrors have majority
parity. Thus the compressed matching has the T15 pattern, and the
four neighbors of $a$ in $B$ are exactly the listed set $S$. T15's
possible obstruction is the listed remaining neighbor edge $pq$.

Every listed $pq$ joins a member of $D_8$ to a member of $D_{16}$.
These sets are disjoint and closed, so $pq\notin F$. Step 1 therefore
applies to each cut. The assumed absence of a global cycle forces
$X_B\subseteq S\subseteq U$.

Now suppose an original matching edge with both endpoints in $R_j$
crossed that cut. Its $B$ endpoint would be a port in $R_j$, contrary
to $X_B\subseteq U$ and $R_j\cap U=\varnothing$. Consequently every
matching edge within $R_j$ preserves every listed cut bit.

### Step 7. Contradiction at vertex 1

For the second residual orbit the closed remaining set is

$$R_2=\{1,2,4,7,11,13,14,19,21,22,23,31\}.$$

By Step 6 every matching edge in $R_2$ preserves bits 1, 2, and 4.
The only vertex of $R_2$ with the same three low bits as vertex 1 is
vertex 1 itself. A matching has no loop, so 1 has no possible partner.

For the third residual orbit the closed remaining set is

$$R_3=\{1,2,4,6,7,11,13,14,19,21,22,31\}.$$

Here bits 2 and 4 are preserved. Vertex 1 is the only member of $R_3$
having both those bits zero. It again has no distinct possible partner.

Both contradictions refute the supposition that a global cycle does
not exist. The asserted cycle therefore exists for every arbitrary
matching with hole set $H_2$ or $H_3$.

### Step 8. Orbit coverage

A coordinate permutation fixes $0$ and preserves short edges, matching
edges, parity, and the cycle condition. The respective marked geometries
have 20 and 30 distinct coordinate images; these sizes are checked by
directly generating all 120 permutations in the accompanying checker.
Hence the two analytic arguments cover all 50 normalized geometries
in those two residual orbits.

## Verification and remaining scope

Run `D:\anaconda\python.exe A8_orbits2_3_geometry_check.py` in this
directory. Its output `A8_orbits2_3_geometry_check.json` checks every
candidate set, local hole count, local obstruction edge, nonfixed-choice
coverage after any possible single fixed obstruction, parity identity,
closed-set identity, and final isolated vertex class. It performs zero
matching-instance enumerations. The mathematical matching argument is
the proof above and still requires fresh independent semantic review.

The original A8 statement is not weakened for these two orbits. This
package by itself establishes no result for the other residual orbits
or for the entire P6 problem. No previously frozen proof or main
ledger was modified.
