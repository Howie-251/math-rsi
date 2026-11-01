# Uniform RS exponential seed

Implemented `formal/Aris4Math/General/Growth/Seed.lean`, without modifying shared definitions.

Exports in namespace `Aris4Math.General.RS`:

- `seed_ak_half {k} (hk : 2 ≤ k) : (1/2 : ℝ) ≤ ak k (1/(k:ℝ))`.
- `seed_acceptedAt {k} (hk : 17 ≤ k) : AcceptedAt k (2^k) (1/(k:ℝ))`.
- `seed_rsAccepts {k} (hk : 17 ≤ k) : RSAccepts k (2^k)`.
- `acceptedAt_p_pos {k M} (hM : 1 ≤ M) {p} (hA : AcceptedAt k M p) : 0 < p`.

The proof uses Mathlib's Bernoulli inequality at `1/(k-1)`. Multiplying by `(1-1/k)^k` and using the exact product `(1-1/k)*(1+1/(k-1))=1` gives the half bound. At budget `2^k`, the exponent is exactly two and the pair coefficient is at most four; the previously checked integral bound gives `J≤1/k`. The uniform strict slack is `4/k<1/4` for `k≥17`, whereas `a^2≥1/4`. Thus the exact shared `AcceptedAt` definition is proved, not a replacement estimate. The positivity result observes that `p=0` gives both sides zero, contradicting strict acceptance for a positive budget.

Local executed evidence:

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
cd /Users/rfy_naiveai/Desktop/aris4math/formal
lake env lean Aris4Math/General/Growth/Seed.lean -o .lake/build/lib/lean/Aris4Math/General/Growth/Seed.olean
lake env lean ../context/propertyb-general-lean-growth/seed/Audit.lean
```

Both commands exited 0. `compile04.log` is the final module log, with no warning or error, and `audit.log` is the independent import/caller log. All four exports have transitive axioms only `propext`, `Classical.choice`, and `Quot.sound`. Earlier compile logs preserve implementation diagnostics and are not final verification evidence.

Self-audit: all quantifiers are uniform in `k`; no numeric enumeration or fixed-17 theorem is used. The strict inequality comes from `k>16`, so the non-strict half bound suffices. Natural edge budgets are cast before subtraction exactly as required by `AcceptedAt`. This is checked local formalization and self-review, not cross-family review or another-machine reproduction. Owned scope is complete; main integration remains with the parent.
