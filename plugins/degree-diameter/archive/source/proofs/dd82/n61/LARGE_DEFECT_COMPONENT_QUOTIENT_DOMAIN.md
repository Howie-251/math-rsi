# Order61: complete necessary size domain for at least five defect components

Status: necessary-domain reduction reviewed in the same-mechanism Gemini discussions; actual row/norm screen results accepted in round3. All65 final necessary size domains have since completed joint quotient enumeration. The historical stage descriptions below retain their original limited scope. The full new connection and actual evidence are in CONNECTED_DEFECT_REDUCTION.md, accepted in the actual round4 review. This file alone is not a quotient-realization or whole-graph exclusion.

Let c=2m+1 in {5,7,9,11,13,15,17}. For every target, Q is nonnegative integral with row8, detailed balance n_i q_ij=n_j q_ji, and Q²+Q−11I=1nᵀ. Sizes are at least2 and sum61. The diagonal has trace8−m; also0<=q_ii<n_i and n_i q_ii is even.

## Necessary arithmetic from the actual quotient

The undirected positive off-diagonal support of Q is connected and has diameter at most2: for i≠j the positive entry (Q²+Q)_ij=n_j supplies a direct edge or a two-step path. Detailed balance makes support symmetric.

If a prime p>8 divides one n_i, along every positive edge n_i q_ij=n_j q_ji with both nonzero q's at most8 it also divides n_j. Connectivity would make p divide every size and hence61. This would force p=61, impossible since every size is less than61. Thus all size prime factors lie in {2,3,5,7}.

Some size is not divisible by3 because their sum61 is not. Along each positive edge, the 3-adic valuations of the two sizes differ by at most1, since each positive q is at most8. Diameter at most2 therefore implies v_3(n_i)<=2 for every i.

Every i has a positive neighbor j. Balance and q_ij>=1,q_ji<=8 imply n_j>=ceil(n_i/8). All other c−2 sizes are at least2, so

n_i+ceil(n_i/8)+2(c−2)<=61,
n_i<=floor(8(65−2c)/9).

For c=5,7,...,17 these upper bounds are48,45,41,38,34,31,27. In particular49 and50 cannot occur when c>=5.

## Exact size-only count

The single short standard-library integer DP in computations/dd82/n61/component_large_size_domain.py counts sorted size multisets satisfying only the conditions above. It processes each allowed denomination once, with increasing number of parts allowing its repetitions. Its state dp[k][s] counts multisets of k parts summing to s. The complete saved result is component_large_size_domain.result.json in the same directory.

| c | Size multisets |
|---|---:|
|5|1026|
|7|4443|
|9|8331|
|11|9070|
|13|6918|
|15|4188|
|17|2167|

Total36143. Algorithm CPU0.001083823s/wall0.004592128s, CPU1, one run. No Q matrix, solver call or graph search occurred. Diagonal/trace/interface feasibility is not included in these counts.

## Further exact constraints, not yet applied in that run

Put r=(-1+3sqrt(5))/2 and s=(-1−3sqrt(5))/2. The spectral projections of the symmetrized quotient are positive semidefinite. Its eigenvalue8 projection has diagonal n_i/61, and the other projection diagonals give

s+(8−s)n_i/61 <= q_ii <= r+(8−r)n_i/61.

Equivalently, for integer d=q_ii, this is the entirely integer test

(122d−17n_i+61)^2 <= 45(61−n_i)^2.

This must hold with0<=d<=8, d<n_i, n_i*d even, and sum_i d_i=8−m. The test is necessary; positivity of these diagonals alone is not positivity of the full projectors.

For each fixed sorted size multiset, define g_ij=gcd(n_i,n_j). All possible balanced interfaces are parameterized without loss by integers t_ij=t_ji:

q_ij=(n_j/g_ij)t_ij,
q_ji=(n_i/g_ij)t_ij,
0<=t_ij<=min(g_ij,floor(8g_ij/n_j),floor(8g_ij/n_i)).

Indeed the two reduced size ratios are coprime, so detailed balance forces exactly these multiples. Simple graph interfaces additionally give q_ij<=n_j and q_ji<=n_i, hence t_ij<=g_ij. Set each diagonal to8 minus its off-diagonal row sum. Check nonnegativity, the diagonal conditions and the entire matrix polynomial. This describes a finite complete quotient search domain; no enumeration of those t assignments has run and no completion time is claimed.

Even a successful abstract Q still requires an actual common adjacency A and its nonnegative B blocks. Excluding all these c>=5 quotients would leave connected defect c=1. Its one-by-one quotient is simply Q=(8) and supplies no internal partition; it needs a different original-graph obligation.


## Actual necessary screen and next shared-row obligation

`component_large_size_screen.result.json` records the single complete screen:36,143 inputs,25,196 survivors,2.908794415 CPU seconds/2.912979212 wall seconds. It applies diagonal/trace feasibility, possible-interface support connectivity and diameter2, and row capacities. Survivors by c=5,7,9,11,13,15,17 are327,2310,5587,6588,5378,3247,1759. It did not test common interface choices or the full polynomial.

A stronger necessary test follows immediately from the same polynomial. For a fixed row i and diagonal d, writing a_j=n_j/g_ij and b_j=n_i/g_ij gives

`sum_(j!=i) a_j t_ij = 8-d`,
`sum_(j!=i) a_j b_j t_ij^2 = n_i+11-d-d^2`.

These two equations must use the same t choices in each row. An exact two-coordinate dynamic program can decide row feasibility and remove impossible diagonals, followed by the global trace test. Separate row feasibility still does not imply that shared t_ij choices agree between rows. This next test is under implementation; no result yet.
