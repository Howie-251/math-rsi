# High-intersection wedges are paid by point-pair triple flags

## General lemma

Let H=(V,E) be a finite simple r-uniform hypergraph, with r≥4 and M=|E|≥1. For each unordered point-pair P⊆V let λ_P be its original-edge codegree. Define the nonnegative excess statistic

\[
\tau_+=\sum_{P\in\binom V2}\binom{\max(\lambda_P-1,0)}2.
\]

Let Q be the simple graph whose vertices are the M original edges of H, with two vertices adjacent precisely when their intersection has size r−1. Put

\[
t=|E(Q)|,\qquad W_Q=\sum_{F\in E}\binom{d_Q(F)}2,
\qquad c_r=\binom{r-2}2>0.
\]

Then

\[
c_r W_Q\le3\sum_{P\in\binom V2}\binom{\lambda_P}3.
\tag{1}
\]

If all point-pair codegrees satisfy λ_P≤L, then

\[
c_r W_Q\le L\tau_+.
\tag{2}
\]

Moreover, writing 2t=aM+b with integers a≥0 and0≤b<M,

\[
W_Q\ge (M-b)\binom a2+b\binom{a+1}2.
\tag{3}
\]

Consequently (2) and (3) give a joint necessary restriction on the number of high-intersection original-edge pairs and the actual point-pair codegree excess. There is no point-pair-covering, minimum-degree, or vertex-count hypothesis.

**Proof of (1).** Group the wedge count by unordered triples S={E,F,G} of distinct original edges. Let w(S) be the number of Q-wedges on these three graph vertices, where a wedge consists of a middle vertex and its unordered pair of neighbors. The possible three-vertex graphs give w(S)∈{0,1,3}: a path contributes one wedge and a triangle contributes three. Hence

\[
W_Q=\sum_{S\in\binom E3}w(S).
\]

If w(S)>0, choose one of its wedge centers, say F. Both E∩F and G∩F have r−1 points inside the r-set F. Their intersection therefore has at least r−2 points, all contained in E∩F∩G. Thus, with m(S)=|E∩F∩G|,

\[
\binom{m(S)}2\ge c_r\ge \frac{c_r}3w(S).
\]

The same inequality is immediate when w(S)=0. Summing over S and double-counting a point-pair together with three original edges containing it gives

\[
\sum_S\binom{m(S)}2
=\sum_P\binom{\lambda_P}3
\ge\frac{c_r}3W_Q,
\]

which is (1). A triangle is included once in the left sum and contributes three, not one, to W_Q; this is exactly the reason for the factor three. No separate flag budget is charged independently to each wedge. The factor three in (1) is necessary: take a fixed (r−2)-set S and three edges S∪{a,b}, S∪{a,c}, S∪{b,c}. Their Q is a triangle, W_Q=3, and the flag sum is exactly C(r−2,2), giving equality in (1).

**Proof of (2).** For every integer λ≥0,

\[
3\binom\lambda3
=\lambda\binom{\max(\lambda-1,0)}2.
\tag{4}
\]

For λ≥1 this is the ordinary binomial identity; for λ=0 both sides are zero by the displayed max convention. In particular λ=0,1,2 contribute zero to both statistics. Applying λ≤L termwise to (4), then using (1), gives (2). If H covers every point-pair, λ≥1 and τ_+ agrees with the usual statistic τ=Σ_P C(λ_P−1,2). Without covering one must retain the max convention.

**Proof of (3).** The graph degrees are nonnegative integers with sum2t. If two integers x,y have y≥x+2, replacing them by x+1,y−1 decreases their contribution to ΣC(d,2) by y−x−1>0. Iterating proves that the minimum under only this sum and the number M of entries occurs when M−b entries equal a and b entries equal a+1. This gives (3). Applying it to the actual graph degrees is valid even if a minimum degree sequence in this scalar relaxation were not realizable by a particular Q. ∎

## Five-uniform, codegree-at-most-four consequence

For r=5 and L=4, c_r=3, so

\[
3W_Q\le4\tau_+.
\tag{5}
\]

Thus for M=35 the necessary integer lower bound is

\[
\tau_+\ge
\left\lceil\frac34\left[(35-b)\binom a2+b\binom{a+1}2\right]\right\rceil,
\quad a=\left\lfloor\frac{2t}{35}\right\rfloor,\quad b=2t-35a.
\tag{6}
\]

The following table gives every value t=0,…,35. Each pair of columns is independent; Wmin denotes the right-hand side of (3), not an additional structural realization claim.

|t|Wmin|Necessary τ+≥|t|Wmin|Necessary τ+≥|
|---:|---:|---:|---:|---:|---:|
|0|0|0|18|1|1|
|1|0|0|19|3|3|
|2|0|0|20|5|4|
|3|0|0|21|7|6|
|4|0|0|22|9|7|
|5|0|0|23|11|9|
|6|0|0|24|13|10|
|7|0|0|25|15|12|
|8|0|0|26|17|13|
|9|0|0|27|19|15|
|10|0|0|28|21|16|
|11|0|0|29|23|18|
|12|0|0|30|25|19|
|13|0|0|31|27|21|
|14|0|0|32|29|22|
|15|0|0|33|31|24|
|16|0|0|34|33|25|
|17|0|0|35|35|27|

In particular τ_+=0 forces W_Q=0, so Q has maximum degree at most one and t≤floor(35/2)=17. In a point-covering five-uniform input, one may replace τ+ by τ and t by the usual n4, yielding the actual original-H restrictions3W_Q≤4τ and τ=0⇒n4≤17. This is a necessary structural restriction, not a proof that all inputs meeting it are colorable, and does not close A2/A3.

## Verification receipt

[CHECK.py](CHECK.py) checks all eight labeled graphs on three vertices and their exact wedge multiplicities, the low-codegree identity including λ=0,1,2, the discrete-convex smoothing inequality on the relevant degree range, and all36 exact scalar values in (6). [CHECK.json](CHECK.json) records PASS in0.000209 CPU seconds. The proof is the analytic double count above; no original-H or free-set search was performed. The finite checks and mathematical review here are same-family/provisional, without a new cross-family review claim.
