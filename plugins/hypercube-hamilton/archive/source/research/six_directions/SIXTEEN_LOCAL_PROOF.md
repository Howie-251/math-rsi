# Nine chosen Q5 inputs for the conditional sixteen-hole residual

## Claim and status

PROVABLE AS STATED relative to the generic matching-connectivity rank
theorem and the exact finite positive certificates, pending fresh
independent local review. No Q6 predecessor hypothesis is needed for
these auxiliary local statements. This producer does not audit its own work.

Use exactly indices9,11,1,2,33,7,12,14,15 from the frozen
`SIXTEEN_NEW_TYPES_summary.json`, with exact marked minority,majority and
omitted sets copied in `SIXTEEN_LOCAL_CERT_summary.json`. Let $H$ be their
hole union, $U$ their specified omissions and $K=Q_5\setminus H$.

- For indices9,11,1,2, for EVERY arbitrary perfect matching $F$ of the
  COMPLETE graph on $K$, a simple cycle on exactly $Q_5\setminus U$
  containing $F$ and adding only short edges exists iff the specified
  covered pair $pq$ is not an edge of $F$.
- For indices33,7,12,14,15, that local cycle exists for EVERY arbitrary
  complete-graph $F$ without an obstruction condition.

Required edges may be long or same-parity. The entire marked input and
forbidden pair are transported together under a common cube automorphism,
including parity reversal. Only these nine exact inputs are claimed;
no unrestricted hole-count theorem or unselected local rank is imported.

| Index | Minority | Majority | Omissions | Forced included hole/pair | Full/reduced terminals; rank |
|---:|---|---|---|---|---|
|9|0|1,2,4,7,11,13,14,19,21,25,26,28,31|1,2,4,14,26,28|0:(8,16)|18/16;128|
|11|0|1,2,4,11,13,14,19,21,22,25,26,28,31|1,2,4,11,13,14|0:(8,16)|18/16;128|
|1|0,3|1,2,4,13,14,21,22,25,26,28|1,2,4,28|0:(8,16)|20/18;256|
|2|0,3|1,4,8,13,14,21,22,25,26,28|1,4,8,28|0:(2,16)|20/18;256|
|33|0,3|4,11,13,14,21,22,25,26,28,31|4,11,21,25|none|20/20;512|
|7|0,3,5|8,11,14,16,22,25,26,28,31|8,11,16|none|20/20;512|
|12|0,3,5|8,11,14,21,22,25,26,28,31|8,11,21|none|20/20;512|
|14|0,3|4,7,13,14,21,22,25,26,28,31|4,7,13,25|none|20/20;512|
|15|0,3|4,8,13,14,21,22,25,26,28,31|4,8,21,25|none|20/20;512|

## Assumptions and dependency map

Import the generic binary matching-connectivity rank formula
$\operatorname{rank}_{\mathrm{GF}(2)}H_n=2^{n/2-1}$ on ALL complete-graph
perfect matchings, Cygan--Kratsch--Nederlof Corollary3.5, with version and
domain alignment in `A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md`. At residual
terminal counts16,18,20 the upper bounds are128,256,512. No bipartite
restriction on required matchings or finite-rank extrapolation is used.

The acyclic local DAG is generic rank bound plus independently checked
positive forests, endpoint pairs, columns and matrices, implying these
exact local statements. The actual Q6 application is separate. In
particular no desired full fourteen- or sixteen-hole theorem is an input
to the local proof.

## 1. Ordinary forest/rank criterion

A legal short complement forest has degree0 at $U$, degree2 at
$H\setminus U$, degree1 at $K$, and no cycle. Its components are paths
covering exactly the retained vertices and pairing the covered terminals;
write that matching as $P$.

For the five unconditional rows,512 supplied legal forest pairings and512
valid arbitrary matching columns form a binary connectivity matrix of
rank512 at20 terminals. Their complete rows in $H_{20}$ are independent
and span its entire row space by the generic upper bound. Every arbitrary
required matching column is nonzero: orient its ten pairs and cyclically
link consecutive ends to construct a connecting perfect matching. Thus
some selected forest connects to every such required matching.

Expanding the endpoint paths gives a connected degree2 graph on exactly
$Q_5\setminus U$. A common required/forest physical edge would be a
length-one forest path and shared endpoint pair, creating an isolated
labelled two-edge component rather than a connected union. Hence the
cycle is simple, contains all required edges, and adds only short edges.

## 2. Forced-pair criterion

For each of the four conditional rows, the declared included hole0 has
exactly the two retained short neighbors $p,q$, both covered. Every legal
complement must use the physical path $p-0-q$, and covered degree1 makes
this an entire endpoint-pair component. If $F$ contains $pq$, that path
and the required edge form a proper isolated triangle; a spanning cycle
is impossible. This is an analytic obstruction, not a rank-failure claim.

Every supplied forest has that physical cherry and full pairing containing
$pq$. Delete exactly that pair, leaving $P^-$ on
$K^-=K\setminus\{p,q\}$. For arbitrary $F$ excluding $pq$, put
$a=F(p),b=F(q)$. The four vertices are distinct; replace $pa,qb$ by $ab$
to obtain a valid arbitrary matching $F^-$ on $K^-$. Suppressing the
labelled path $a-p-q-b$ proves

$$F+P\text{ connected}\quad\Longleftrightarrow\quad
F^-+P^-\text{ connected}.$$

The supplied reduced matrices meet the full generic rank bound128 on16
terminals or256 on18 terminals. Their complete rows span the respective
matching-connectivity row space. Every arbitrary $F^-$ column is nonzero
by cyclically linking its oriented pairs, so one selected row connects.
Undo suppression and expand the selected forest, obtaining the required
simple cycle with only short added edges. Common physical edges are
excluded by the full connected endpoint union exactly as above. Necessity
and sufficiency therefore apply to the SAME complete-graph matching domain.

## 3. Certificate interface and independent obligations

New reduced prefixes are `SIXTEEN_LOCAL_FORCED_orbit_009`, `_011`, `_001`,
`_002`. The five ordinary inputs retain their unchanged source prefixes
`SIXTEEN_NEW_TYPES_orbit_{033,007,012,014,015}`. Source preparation,
profile/search/summary and all root evidence remain unchanged.

| Inputs | Records each | Forest bytes | Full pairs | Reduced pairs/columns | Matrix row bytes |
|---|---:|---:|---:|---:|---:|
|9,11|128|34|18|16|16|
|1,2|256|36|20|18|32|
|33,14,15|512|36|20|20|64|
|7,12|512|38|20|20|64|

For forced inputs `_full_pairs.bin` preserves full endpoint pairs and
`_pairs.bin` removes exactly the specified pair. Ordinary `_pairs.bin`
already is the full pairing. All columns are arbitrary complete matchings
on the declared residual terminal set. Reduced/square matrix, pivot and
combo rows use low-bit-first binary layout. Forests, configurations and
extraction metadata have their usual suffixes. In total3328 forests and
columns, and1474560 connectivity bits, require independent verification.

The producer's extraction selects independent source matrix columns and
contracts their forced pair. This explains provenance; neither the
original full matrix nor its claimed rank is needed if a fresh checker
directly validates the resulting legal forests, full/reduced pairings,
matching columns, every matrix bit and exact binary rank. Producer author
checks recompute these but are not independent acceptance. Source-family
exhaustiveness and deficient nonselected searches prove nothing negative.

## Boundary

This theorem proves only the nine exact auxiliary inputs once their finite
certificates are independently accepted. The other candidate geometries or
source searches are not additional accepted local theorems. Conditional
high-layer predecessor assumptions belong only to the separate actual
application and global domain reduction. Full sixteen-hole Q6 and full P6
remain unproved by this package.
