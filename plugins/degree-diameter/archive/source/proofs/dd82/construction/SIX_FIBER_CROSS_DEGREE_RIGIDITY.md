# Six ten-vertex fibers: arbitrary equitable cross degrees are forced to one

Date: 2026-10-11. Pure analytic proof; no enumeration or graph solver.

## Claim

Let a simple undirected graph of degree eight and diameter at most two
have an equitable partition into six fibers of size ten, each inducing a
three-regular graph. Allow arbitrary nonnegative integer cross degrees
$q_{ij}$: every vertex in fiber $i$ has $q_{ij}$ neighbors in fiber $j$.
Then

$$q_{ij}=1\quad\text{for every }i\ne j.$$

Thus every interface is a perfect matching. In particular, allowing
multiple cross matchings or absent interfaces does not enlarge this
construction family. No symmetry inside the fibers, Cayley action, or
assumption about defect-matrix support components is used.

## Proof

Set $q_{ii}=0$ and write $Q=(q_{ij})$. Equal fiber sizes and undirected
edge counting give $q_{ij}=q_{ji}$. Each vertex already has three internal
neighbors, so

$$Q\mathbf1=5\mathbf1.$$

For a fixed source in fiber $i$ and a different target fiber $j$, the
direct edges and paths of length two have total count

$$q_{ij}+3q_{ij}+3q_{ij}+\sum_{k\ne i,j}q_{ik}q_{kj}
  =7q_{ij}+(Q^2)_{ij}.$$

They must reach all ten vertices of the target fiber. Therefore

$$7q_{ij}+(Q^2)_{ij}\ge10\qquad(i\ne j).\tag{1}$$

Sum (1) over the five choices $j\ne i$. The row sum of $Q^2$ is $25$,
and its diagonal entry is $\sum_k q_{ik}^2$. It follows that

$$50\le35+25-\sum_k q_{ik}^2,
\qquad \sum_k q_{ik}^2\le10.$$

For integers, $q_{ik}^2\equiv q_{ik}\pmod2$, so the square sum has the
same odd parity as the row sum five. Hence every row has squared norm
at most nine.

If some $q_{ij}=0$, symmetry and Cauchy–Schwarz give

$$10\le(Q^2)_{ij}
 =\sum_k q_{ik}q_{jk}
 \le\sqrt{\left(\sum_k q_{ik}^2\right)
                 \left(\sum_k q_{jk}^2\right)}\le9,$$

a contradiction. Every off-diagonal entry is therefore a positive
integer. There are five such entries in each row and they sum to five,
so all equal one. $\square$

## Consequence for internal graphs and scope

Once all interfaces are matchings, a two-step route leaving a fiber and
returning to it returns to its starting vertex. Thus each internal cubic
graph on ten vertices must itself have diameter at most two. It attains
the cubic Moore bound and is the Petersen graph; a short direct uniqueness
proof is included in [the equal-fiber capacity note](EQUAL_FIBER_SINGLE_MATCHING_CAPACITY.md).

Consequently every graph in the stated equitable six-fiber family is
already in the full six-Petersen-fiber family with fifteen arbitrary
perfect matchings. This result excludes a proposed enlargement of that
family; it does not exclude the full six-Petersen-fiber family or arbitrary
60-vertex graphs.

An integer-composition enumeration was initially prepared but never
launched. After the analytic proof closed the question, the unused source
was removed. No enumeration counts or computational exclusion are claimed.

## External discussion C7

Root independently read this proof. Gemini C7 accepted its complete
mathematical derivation as supplied in the prompt; it did not claim to
read this later saved source file. Raw response and exact prompt:
`reviews/dd82/20261011_C7_hs59_degree7_rigidity.json`. Requested and
CLI-selected gemini-3.8-flash-high/high are metadata, not independent
backend attestation. No numerical verification was needed or run.
