# Actual order62 double-repeat oddness, 2026-10-11

Scope: the odd-double-count step in `proofs/dd82/n62/D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md`, section 3. The sole extra graph premise is explicitly `∀ x y, defectMatrix G x y ≤ 2`. This module does not derive that bound, classify heavy-repeat templates, pair closed components globally, prove a D1 representative exists, or exclude arbitrary order62 graphs.

`DegreeDiameter/N62DoubleParity.lean` proves:

- `n62_four_cycle_flags_even`: the actual opposite-pair flags have even cardinality, using swapping as a fixed-point-free involution. This theorem needs no defect bound.
- `n62_four_cycle_flag_incidence`: under the actual bound B≤2, flag count is P1+3d.
- `n62_double_repeat_incidence`: the actual ordered defect-row count is 2P1+4d+6T=186.
- `n62_double_nonedge_pair_count_odd`: the actual double-nonedge count is odd, by these counts and the existing actual triangle-count evenness theorem.
- `n62_double_repeat_pairs_eq_nonedge_pairs`: every double repeat is a nonedge, by the already proved original-edge defect bound.
- `n62_double_repeat_pair_count_odd`: final original-graph caller, asserting odd cardinality of all actual unordered B=2 pairs.

Here P1 is `(unitNonedgePairs G).card`, d is `(doubleNonedgePairs G).card`, and T is `(G.cliqueFinset 3).card`. All are sets of actual vertices of G. `doubleRepeatPairs G` counts all actual unordered pairs with B[x,y]=2 without adding a nonadjacency clause. Its proved equality to `doubleNonedgePairs G` connects the final count to the intermediate incidence calculation.

`fourCycleFlags G` consists of ordered pairs (P,Q): P is an actual unordered nonedge and Q is an actual two-subset of its common-neighbor set. Every such Q is a nonedge, because otherwise its two common neighbors would violate the original-edge defect bound. Swapping P,Q preserves flags and has no fixed point, since P=Q would force a graph loop. No abstract supplied cycle or pairing certificate occurs. The cardinal identity uses the actual powersetCard 2, giving choose(2,2)=1 for unit repeats and choose(3,2)=3 for double repeats.

Verification (Lean/mathlib 4.24, at most three threads):

```bash
cd formal
source ../.tools/lean-env.sh
export LEAN_NUM_THREADS=3 RAYON_NUM_THREADS=3
lake build DegreeDiameter.N62DoubleParity
lake env lean ReviewN62DoubleParity.lean
```

Successful build: `logs/n62-double-parity-full-third.log` (exit 0). Dedicated definitions/types/transitive-axioms/raw-caller audit: `logs/n62-double-parity-type-axiom-audit.log` (exit 0). All six exported theorem chains depend only on propext, Classical.choice and Quot.sound. Earlier failed API attempts are retained and are not proof evidence. No sorry, new axiom, native_decide or hashes were introduced. Shared entry point, STATUS and cross-family source review remain parent-owned.
