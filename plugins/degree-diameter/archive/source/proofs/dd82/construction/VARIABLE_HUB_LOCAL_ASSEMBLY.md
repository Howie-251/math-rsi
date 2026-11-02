# A one-sided exact hub equation is impossible

Date: 2026-10-12. This is a computer-assisted local obstruction using the
complete ten-type $(10_3)$ classification, one finite existence screen,
and one independent reimplementation of that screen. It closes the last
nonuniform quotient from the six-by-ten equitable-partition enumeration.
It does not exclude arbitrary sixty-vertex graphs or the uniform
degree-three fiber model.

## The local claim

Let $S$ be a perfect-matching adjacency matrix on ten points, and let
$Z,Y$ be ten-by-ten zero-one matrices with row and column sums three and
two, respectively. Assume

$$S+YY^T+ZZ^T=J_{10}+4I_{10}.\tag{1}$$

There do not exist permutation matrices $M,N,P$ and a symmetric,
zero-diagonal, zero-one cubic adjacency matrix $C$ satisfying

$$M+SM+MC+ZN+YP=J_{10}.\tag{2}$$

The completed finite check below proves the claim without requiring $C$
to be connected or to satisfy $\lambda_2(C)\le2$. Thus the extra spectral
restriction from the full quotient is not needed here. No symmetry of
$Z$, fixed choice of $C$, common labeling of different fibers, or old
degree-one bridge exclusion is assumed.

## Normalizing M preserves all the data

Right-multiply (2) by $M^T$. The result is

$$I+S+C'+ZN'+YP'=J,\tag{3}$$

where

$$C'=MCM^T,\qquad N'=NM^T,\qquad P'=PM^T.$$

Conjugation preserves every adjacency property of $C$, and $N',P'$ remain
independent permutations. Equation (1) is unchanged. Thus choosing the
hub coordinate of a source vertex to be its matching partner loses no
candidate. Suppress the primes henceforth.

## Why the 71 local states are complete

The exact equivalence in
[D1_LOCAL_CONFIGURATION_CATALOG.md](D1_LOCAL_CONFIGURATION_CATALOG.md)
proves that (1) is equivalent to these data:

* a linear combinatorial $(10_3)$ configuration with incidence matrix $Z$;
* a perfect matching $S$ in its primal cubic leave;
* the point-edge incidence matrix $Y$ of the remaining two-factor,
  with arbitrary labels on its ten edge columns.

The published complete classification gives the ten representatives used
in that note. All their primal leave matchings are listed in
[the existing local catalog](../../../computations/dd82/construction/d1_10_3_catalog/local_interfaces.json).
The counts are $6,6,6,6,8,6,6,9,7,11$, totaling **71**.
Completeness of the configuration types retains the published
classification dependency documented there; neither finite check below
claims to reclassify all $(10_3)$ configurations.

It is legitimate to fix one column labeling of $Z$ and one edge ordering
of $Y$ in each state because $N$ and $P$ are independent unrestricted
column permutations. There is also no missing point-label freedom.
If $U$ normalizes the point labels and $V,W$ normalize the respective
column labels, replace

\[
\begin{aligned}
S&\mapsto USU^T,& C&\mapsto UCU^T,\\
Z&\mapsto UZV^T,& N&\mapsto VNU^T,\\
Y&\mapsto UYW^T,& P&\mapsto WPU^T.
\end{aligned}
\]

Both (1) and (3) are preserved. In the graph interpretation this relabels
the source and its normalized hub coordinates together. It does not fix
an unrelated interface or constrain either remaining permutation.

The preparation in
[variable_hub_local_run.py](../../../computations/dd82/construction/variable_hub_local_run.py)
reads each representative's actual incidence rows and transposes them
into ten three-point column sets. For every primal leave matching it
uses the actual ten edges of `leave - S` as the two-point columns of $Y$.
The complete 71 states are preserved in
[states.json](../../../computations/dd82/construction/variable_hub_local_run/states.json)
and their compact masks in
[input.txt](../../../computations/dd82/construction/variable_hub_local_run/input.txt).

## Exact elimination of C and the finite column choices

Let $s(v)$ be the matching partner of $v$. For each target column $v$,
choose one column $z_v$ of $Z$ and one column $y_v$ of $Y$. The choices
over the ten targets must each be bijections onto their respective ten
columns. These are exactly the independent permutation matrices $N,P$:
$N_{z_v,v}=1$ and $P_{y_v,v}=1$.

Write $B_{z_v}$ for the selected three-point column set and $E_{y_v}$ for
the selected two-point edge set. Equation (3) with a zero-one $C$ is
equivalent, column by column, to

$$B_{z_v}\cap E_{y_v}=\varnothing,\qquad
(B_{z_v}\cup E_{y_v})\cap\{v,s(v)\}=\varnothing,\tag{4}$$

and

$$\operatorname{supp}C_{\cdot v}
 =\{0,\ldots,9\}\setminus
   \bigl(\{v,s(v)\}\cup B_{z_v}\cup E_{y_v}\bigr).\tag{5}$$

The seven removed points in (5) are distinct, so each resulting column
has exactly three ones and has zero at its own diagonal position.
Once both column bijections are complete, the matrix identity
$C=J-I-S-ZN-YP$ also gives row sum three. The only remaining adjacency
condition is symmetry:

$$u\in\operatorname{supp}C_{\cdot v}
\quad\Longleftrightarrow\quad
v\in\operatorname{supp}C_{\cdot u}.\tag{6}$$

Equations (4)--(6), and the two column bijections, therefore give an exact
finite parametrization of every solution of (1)--(3), before imposing
any connectivity or spectral condition.

## Actual primary search and why its rejection is exhaustive

The [C++ source](../../../computations/dd82/construction/variable_hub_local_search.cpp)
forms every pair $(z_v,y_v)$ satisfying (4) for each column $v$, and stores
the uniquely determined three-point complement (5). A recursive step
chooses an unassigned column with the fewest currently available choices.
It rejects a choice only if one of its two input columns has already
been used, or if its required memberships against already assigned
columns disagree with (6). Both presence and absence of an edge are
checked by the equality of the restricted masks.

This search order adds no condition. Every pair of input-column
bijections satisfying (4)--(6) has exactly its own branch through these
choices. Conversely a complete branch defines the required permutations
and symmetric cubic $C$ by (5). No assumption about a special cubic graph
or a repeated interface enters the domains.

The [primary result](../../../computations/dd82/construction/variable_hub_local_run/search.json)
and [all per-state results](../../../computations/dd82/construction/variable_hub_local_run/states.results.jsonl)
record:

* 71 states, all `complete_no_witness`;
* zero unknown states and `all_states_decided: true`;
* 1,818 recursive nodes in total;
* **zero complete leaves in every state**.

The source contains a connectedness check at complete leaves, but no leaf
was reached, so that check rejected nothing. No spectral filter was used.
The absence of leaves thus excludes every symmetric cubic completion,
including disconnected ones. The metadata `all_solutions_enumerated:
false` describes the existence-search design, which would stop at the
first positive witness; it does not turn these completed zero cases into
partial searches.

The process exited normally. Its internal recorded CPU time was
0.002163 seconds; measured process CPU was **0.006882 seconds**, wall time
**0.008374736 seconds**, with one CPU under the ten-second internal cap.
See [resources.json](../../../computations/dd82/construction/variable_hub_local_run/resources.json).

## One independent finite check

Because the zero is decisive, the root agent ran one independent
[Python checker](../../../computations/dd82/construction/variable_hub_local_verify.py).
It reads the original
[Grunbaum triple table](../../../computations/dd82/construction/d1_10_3_catalog/10_3_grunbaum.json),
reconstructs the primal leaves, enumerates their perfect matchings anew,
and searches the same mathematically defined column choices in fixed
target order using Python sets. It does not use the C++ masks, its
minimum-domain row order, its prepared input, or any connectivity or
spectral pruning.

The [independent result](../../../computations/dd82/construction/variable_hub_local_run/independent_verification.json)
records `complete: true`, the same 71 states, **zero witnesses**, 12,383
recursive nodes, and **0.062481497 CPU seconds**. The different recursion
counts reflect the different orders. This verifies the finite zero from
the original triple data; it does not remove the external ten-type
classification dependency. No third enumeration is needed or claimed.

## Application to the last nonuniform quotient

For the quotient with internal degrees $(1,1,1,1,3,3)$ in
[VARIABLE_111133_OBLIGATION.md](VARIABLE_111133_OBLIGATION.md), use actual
un-normalized interface matrices and select

$$S=S_0,\quad C=C_4,\quad Z=F_{03},\quad Y=F_{05},
\quad M=F_{04},\quad N=F_{34},\quad P=F_{54}.\tag{7}$$

The diagonal defect block of fiber 0 is zero. Its two external
degree-one interfaces, together with $S_0^2=I$, contribute three copies
of $I$ to the diagonal block of $A^2$. Therefore its remaining two
interfaces satisfy exactly (1).

The cross pair $0\to4$ also has zero defect and capacity ten. Its routes
are:

* direct interface $F_{04}=M$;
* intermediate vertices in the endpoint fibers: $S_0M$ and $MC_4$;
* middle fiber 3: $F_{03}F_{34}=ZN$;
* middle fiber 5: $F_{05}F_{54}=YP$.

Middle fiber 1 contributes zero because $q_{01}=0$, and middle fiber 2
contributes zero because $q_{24}=0$. All route slots are therefore exactly
those in (2), with row count $1+1+3+3+2=10$. Diameter two forces equality
to $J$. The matrices $M,N,P$ are permutations because those three
interfaces have degree one, and $C_4$ is a symmetric simple cubic graph.
Hence every realization of this quotient would supply the impossible
local data. This excludes **all 24 labeled matrices in orbit 4**.

## Final scope of this local result

The [complete nonuniform quotient enumeration](SIX_FIBER_VARIABLE_INTERNAL_DEGREE.md)
left four orbits, of sizes 2, 12, 60, and 24. The size-12 orbit was
excluded by its odd-cycle determinant argument. The size-60 orbit was
excluded in
[VARIABLE_D1_FIVE_ONE_BRIDGE_EXCLUSION.md](VARIABLE_D1_FIVE_ONE_BRIDGE_EXCLUSION.md),
and the size-2 orbit in
[VARIABLE_001223_OBLIGATION.md](VARIABLE_001223_OBLIGATION.md).
The present local obstruction excludes the final size-24 orbit.

Thus the stated classification and finite checks exclude **every
nonuniform internal-degree equitable partition into six fibers of ten**
for an eight-regular diameter-two graph on sixty vertices. This conclusion
does not cover uniform degree-three fibers, does not force an arbitrary
sixty-vertex graph to have such a partition, and is not a Lean theorem.
