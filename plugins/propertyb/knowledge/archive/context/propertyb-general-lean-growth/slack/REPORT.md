# Strict logarithmic slack for the actual integer gain

Completed and frozen module: `formal/Aris4Math/General/Growth/Slack.lean`.

The module proves the exact requested original-parameter interface:

```lean
integerGain_log_slack {k M n : ℕ}
  (hk : 17 ≤ k) (hM : 2 ^ k ≤ M)
  (hn : n * (n - 1) ≤ k * (k - 1) * (M + integerGain k M)) :
  (2 + 2 * Real.log (k : ℝ)) * (integerGain k M : ℝ) + 2 <
    (M : ℝ) / (cliqueBudget k n : ℝ)
```

`cliqueBudget_gt_one hk n` separately proves `1 < (cliqueBudget k n : ℝ)` for all `n`, with no `n ≥ k` assumption.

The proof uses the same actual gain and actual clique budget. The natural-floor upper bound gives `(2+2log k)s ≤ sqrt(M)/4`. The previously proved `sqrt(M)>8` makes this quantity plus 2 strictly less than `sqrt(M)/2`. The natural vertex budget, together with `M+s≤2M`, gives `r≤2sqrt(M)`; positivity of `r` and `sqrt(M)^2=M` then show `sqrt(M)/2≤M/r`. There are no new certificate, probability, or structural assumptions beyond the displayed natural budget.

Executed verification:

- Direct module compilation to its own `.olean`: exit 0.
- Independent import `ActualCaller.lean`: exit 0. It reconstructs the original formula with let-bound `s` and `r` for arbitrary parameters, and supplies a concrete boundary caller `k=n=17`, `M=131072` with its structural hypothesis discharged internally.
- Four printed transitive-axiom lists contain only `propext`, `Classical.choice`, and `Quot.sound`; see `actual-caller.log`.

Reproduction from `formal/`, after root-managed dependencies:

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
lake env lean Aris4Math/General/Growth/Slack.lean -o .lake/build/lib/lean/Aris4Math/General/Growth/Slack.olean
lake env lean ../context/propertyb-general-lean-growth/slack/ActualCaller.lean
```

This is local incremental verification and independent import, not external-machine reproduction or cross-family review.
