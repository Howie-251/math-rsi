# RS integral and finite relative-order interface

Owned module: `formal/Aris4Math/General/RS/Integral.lean`.
Namespace: `Aris4Math.General.RS`.

The stable definitions are `jk k p = ∫ y in 0..p, (1-y^2)^(k-1)` and
`ak k p = 1-(1-p)^k`.

For n=k−1 the finite quantity `orderSum n p` is

\[
\sum_{a=0}^n\sum_{b=0}^n {n\choose a}{n\choose b}
p^{a+b}(1-p)^{n-b}\frac{a!b!}{(a+b+1)!}.
\]

Here a is the number of initially opposite vertices in the final failed edge
whose eligibility and earlier order are required; b is the number of eligible
vertices of the triggering initial edge whose order must follow the distinguished
vertex. The required ordering places all a vertices before the distinguished
vertex and all b after it; its uniform relative-order probability is
`a! b! / (a+b+1)!`. Non-red vertices of the final edge contribute no eligibility
restriction and therefore no extra factor `(1-p)^(n-a)`.

The algebraic connection `p * orderSum (k-1) p = jk k p` holds for all natural k
and all real p. Only the probabilistic interpretation and positivity estimates
need 0≤p≤1 and k≥2. The proof route is exact:

1. `beta_nat` proves ∫₀¹ t^a(1−t)^b = a!b!/(a+b+1)!, by integer b induction
   and the fundamental theorem applied to t^(a+1)(1−t)^(b+1).
2. `binomial_order_integrand` applies the binomial theorem to `(1+pt)^n` and
   `((1-p)+p(1-t))^n=(1-pt)^n`.
3. `orderSum_integral` exchanges only finite sums with the integral.
4. `jk_rescale` uses y=pt and `(1-pt)(1+pt)=1-(pt)^2`.

No general Gamma/Beta-function machinery, external certificate or additional
axiom is needed. The final source compiled successfully (`build06.log`, exit 0,
no diagnostics), and `Audit.lean` independently imported its generated olean,
restated the explicit k-indexed finite-sum identity, and printed types, definitions
and transitive axioms (`audit-final.log`, exit 0). All audited declarations depend
only on `propext`, `Classical.choice`, and `Quot.sound`.

The convenience theorem `finite_order_sum_eq_jk` uses the ranges `0,…,k−1`
directly and therefore has hypothesis `1 ≤ k`. The n-indexed `orderSum_eq_jk`
requires no k hypothesis. The originally requested probability domain k≥2,
0≤p≤1 supplies this range hypothesis automatically.

The initial failed audit (`audit.log`) tested the k-indexed range at k=0, where
the displayed range is empty and is not the n=k−1 range. Its failure was resolved
by the correct `1 ≤ k` hypothesis in the explicit range theorem. It did not affect
the already compiled all-k n-indexed identity.

## Reproduce

From `formal/`, with the project-local `ELAN_HOME` and `PATH`:

```
lake env lean -o .lake/build/lib/lean/Aris4Math/General/RS/Integral.olean Aris4Math/General/RS/Integral.lean
lake env lean ../context/propertyb-general-lean-pilot/integral/Audit.lean
```

This module proves the analytic/finite-sum bridge. It does not itself establish
that the actual RS algorithm's witness event has this finite weight; algorithm
semantics, disjoint-variable counting, relative-order uniformity and the final
union bound remain integration obligations of the main RS proof.
