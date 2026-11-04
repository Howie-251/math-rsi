# Nine actual Q5 inputs: single/double cherries and one full positive class

## Claim

Use exactly the nine marked rows below, with original61-profile indices.
Write $H=M\cup J$, $K=Q_5\setminus H$, and $U\subset J$ for the marked
omissions. All sets are original five-cube vertex labels. For each of
the eight forced rows let $R$ be its specified matching of covered pairs.
For EVERY perfect matching $F$ of the COMPLETE graph on $K$, a simple
cycle on exactly $Q_5\setminus U$ containing $F$ and adding only cube
edges exists if and only if the LABELLED graph $F+R$ is acyclic.
For row54, the conclusion holds for every arbitrary $F$ without a condition.
Long and same-parity required edges are allowed. A common cube automorphism
transports minority,majority,omissions and the whole paired matching $R$.

| Index | Minority $M$ | Majority $J$ | Omitted $U$ | Forced cherries $h:(p,q)$ | Reduced rank |
|---:|---|---|---|---|---:|
|13|0,3|1,2,4,7,13,14,21,25,28,31|1,2,4,7|0:(8,16);3:(11,19)|128|
|14|0,3|1,2,4,7,13,21,25,26,28,31|1,2,4,7|0:(8,16);3:(11,19)|128|
|19|0,3|1,4,8,13,14,21,22,26,28,31|1,4,8,26|0:(2,16)|256|
|20|0|1,2,4,7,11,13,19,21,25,26,31|1,2,4,13,26|0:(8,16)|256|
|27|0,3|1,4,8,14,21,22,25,26,28,31|1,4,8,14|0:(2,16)|256|
|28|0,3|4,8,13,14,16,21,22,25,28,31|4,8,16,25|0:(1,2)|256|
|29|0|1,2,4,7,11,13,14,19,21,25,31|1,2,4,14,25|0:(8,16)|256|
|30|0|1,2,4,11,13,14,19,25,26,28,31|1,2,4,19,28|0:(8,16)|256|
|54|0,3,5|8,11,13,14,22,25,26,28,31|8,11,13|none; unconditional|512|

## Status and assumptions

PROVABLE AS STATED relative to the primary generic rank theorem and the
specified positive finite certificates, pending FRESH independent local
verification. The producer author check is not independent acceptance.
This is neither unrestricted T39/T2_10/T1_11 nor a full fourteen-hole theorem.

Import the generic complete-graph matching-connectivity bound
$\operatorname{rank}_{\mathrm{GF}(2)}H_t\le2^{t/2-1}$ for every even
$t\ge2$, Cygan--Kratsch--Nederlof Corollary3.5, with the primary statement
recorded in `A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md`. The already accepted
`HIGHER_FORCED_CHERRY_TRANSFER.md` Section5 gives a compatible multi-pair
rank criterion; the full proof for these exact data is written below.
No Q6 theorem or failed search is an assumption of the local proof.

## Notation and strategy

A legal short complement forest $S$ has degree0 at $U$, degree2 at
$H\setminus U$, degree1 at $K$, and no cycle. Its path-endpoint matching
is $P(S)$. All nine rows have $|K|=20$. For a forced row let $r=|R|$,
$K^-=K\setminus V(R)$, and $P^-=P(S)\setminus R$.
We prove analytic necessity, verify reduced positive rank, and use row-space
spanning for the universal arbitrary matching. Finite generator exhaustion
and original full-matrix search ranks are not premises.

## 1. Forced paths and necessary obstruction

For every listed cherry $h:(p,q)$, the only short neighbors of $h$ outside
$U$ are exactly $p,q$, and both are in $K$. Every permissible cycle must
contain $p-h-q$. A covered terminal has one required $F$ edge and one
complement edge, so the entire complement path is exactly $p-h-q$ and
$P(S)$ contains the matching pair $pq$. These cherry terminal pairs are
pairwise disjoint within each row.

Deleting the nonempty $F$ from a connected cycle gives a legal short
forest. If $F+R$ has a labelled cycle, all vertices of that cycle already
have their two alternating edges, so it persists as a proper component of
$F+P(S)$. The nonempty residual terminal set $K^-$ lies outside it.
Thus a connected endpoint union is impossible. This proves necessity.
For one pair it is exactly $pq\notin F$. For two pairs absence of the
individual $R$ edges is NOT sufficient: cross-pairing their four endpoints
can itself form an alternating4-cycle. The theorem uses full acyclicity.

## 2. Reduced positive rank proves sufficiency

Suppose $F+R$ is acyclic. Its components are paths, with degree2 on
$V(R)$ and degree1 on $K^-$. Compress them to an arbitrary perfect
matching $F^-$ on $K^-$. For every selected $P(S)=R\cup P^-$,
component-preserving suppression gives

$$F+P(S)\text{ connected}\quad\Longleftrightarrow\quad
F^-+P^-\text{ connected}.$$

The supplied legal forests give a reduced connectivity restriction of
rank128 at16 endpoints for rows13/14, and rank256 at18 endpoints for the
six single-cherry rows. These meet exactly the generic respective upper
bounds $2^{16/2-1}$ and $2^{18/2-1}$. Their complete rows consequently
span the full matching-connectivity row space. Every arbitrary $F^-$
column is nonzero: orient its required pairs and cyclically link consecutive
ends to obtain another perfect matching forming one alternating cycle.
If all selected rows vanished on $F^-$, all rows would vanish, contradiction.
Hence some selected forest connects with this arbitrary required matching.

Undo suppression and expand every endpoint path. This gives a simple
cycle on exactly $Q_5\setminus U$ containing all $F$, with every other
physical edge short. A common required/forest physical edge would be a
length-one complement path and shared endpoint pair, hence an isolated
labelled two-edge component, incompatible with connectedness on20 terminals.

For row54 there is no forced pair. Its512 legal forests and512 arbitrary
matching columns have full binary rank512 at20 endpoints, the complete
matrix upper bound. The same nonzero-column/spanning argument applies
directly, establishing the unconditional local theorem. No deficient rank
or absence of a forced hole is used as a positive/negative certificate.

## 3. Finite certificate boundary

New forced prefixes are `FOURTEEN_FORCED_orbit_XXX`. Row54 uses its unchanged
frozen source prefix `FOURTEEN_NEW_TYPES_orbit_054`.

| Rows | Count per row | Forest bytes | Full pairing bytes | Reduced pairing/column bytes | Matrix row bytes |
|---|---:|---:|---:|---:|---:|
|13,14|128|36|20|16|16|
|19,27,28|256|36|20|18|32|
|20,29,30|256|34|20|18|32|
|54|512|38|20|20|64|

For forced rows suffixes are `_forests.bin`, `_full_pairs.bin`, `_pairs.bin`,
`_columns.bin`, `_matrix.bin`, `_pivots.bin`, `_combos.bin`, `_config.txt`,
and `.json`. Full pairings contain $R$; reduced pairings delete exactly
its covered endpoints. The square reduced matrices have low-bit-first
entries. For row54 `_pairs.bin` is already the full20-terminal pairing.
The total is2304 forests/columns and688128 connectivity bits.

The producer extracts independent columns of an existing positive full-row
matrix and suppresses $F+R$ in those columns. Extraction metadata explains
provenance but need not be trusted: the reduced forests, derived pairs,
arbitrary columns and binary matrices stand on their own. Fresh audit
must verify every short edge, exact support/degree, omission, acyclicity,
physical cherry, full pairing, reduced deletion, valid column, connectivity
bit and exact reduced rank. The producer author checker recomputes these
properties and matrix ranks but does not supply independent acceptance.

## Dependency map and boundary

Primary generic rank plus independently verified finite positive data imply
the exact nine local statements. The actual Q6 application is separate,
in `FOURTEEN_FORCED_APPLICATION.md`; it must prove acyclicity of the ACTUAL
compressed matching plus all pairs of $R$, not merely avoid each pair.
The other52 profile rows, including the single-cherry row15 of deficient
rank192, receive no classification here. No failed rank search disproves
any local or global theorem. No new root-in-obstruction route, full
fourteen-hole Q6 or P6 closure is claimed.
