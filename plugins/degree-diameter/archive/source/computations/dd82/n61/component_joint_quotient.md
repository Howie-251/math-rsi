# Order61 joint-quotient search and prepared stabilizer reduction

Status: all65 necessary size domains are now complete across three preserved batches. The original profile completed7, finding3 labelled Q in2 size types; the remaining run completed40 then interrupted the next input; the separately reviewed stabilizer search completed exactly the18 unfinished inputs with no Q, in0.382438874CPU/0.387258556wall. Dedicated symmetry-sanity passed before launch. The saved-result checker independently verified all models and complete disjoint recorded coverage. Search exhaustiveness rests on the reviewed source and terminal records. Historical launch plans and budget descriptions below are retained; no further run is pending.

This remains the V3 weighted-defect quotient mechanism and the project's mathematical `experiment-bridge` adaptation. The actual upstream results are 25,196 row-screen inputs →142 survivors →65 norm-screen survivors. No prior screen or n62 computation will be rerun. The n62 source was read only for its general balanced-row compatibility method; its size restrictions, constants, guards, and searches are not imported.

## Complete finite input and search

Read only `component_norm_screen.result.json`, requiring complete status and counts c=5,7,9,11,13,15,17 of4,3,10,11,18,10,9. Preserve every input size tuple and its actual diagonal domains. Following the actual Gemini round3 direction and root decision, this profile selects only the four c=5 and three c=7 inputs. The other58 are explicitly unselected; a complete seven-input result does not decide them or authorize their execution.

For every interface i,j, put g=gcd(n_i,n_j), a=n_j/g, b=n_i/g. Its complete balanced simple degree-eight domain is

q_ij=a t, q_ji=b t, 0≤t≤min(g, floor(8/a), floor(8/b)).

For candidate row diagonal d, require the two exact sums

Σq_ij=8−d, Σq_ij q_ji=n_i+11−d−d².

Assigned rows fix both directions of all their interfaces. A memoized suffix DP counts completions of each remaining row under the two sums, with all already fixed entries subtracted. Select an unassigned row with smallest positive completion count (deterministic index tie break); zero count is a necessary rejection. This count is used only for variable ordering and exact zero detection, not as a bound on the number of full Q solutions.

Use a bitset to require that some sum of the presently feasible row diagonals reaches the remaining trace8−(c−1)/2. Stream every remaining row assignment. If row j is already assigned, its complete column is fixed by balance; therefore the candidate row i can immediately be tested against

Σ_k q_ik q_kj+q_ij=n_j.

While generating row i, all terms are nonnegative, so a partial sum exceeding n_j−q_ij is impossible. At completion the sum must equal that value. The reverse entry is also checked directly. No unknown matrix entry is silently set to zero: unassigned terms are used only for a nonnegative lower bound, then are completely assigned before equality is tested.

In the original `profile` and `remaining` modes, every full Q is retained by these steps: its next selected row occurs in the full t-domain, satisfies both moments and the trace test, and satisfies the already assigned off-diagonal identities. Deterministic MRV gives one assignment path for each labelled Q; those two modes keep their original search logic without symmetry reductions. At each model in every mode, a separate direct integer matrix multiplication checks all entries of Q²+Q−11I=1 nᵀ, rows, balance, diagonals, and simple interface bounds.

## Known model and lifting scope

The root supplied this abstract quotient:

```text
n=(2,5,6,18,30)
Q=0 5 3 0 0
  2 0 0 0 6
  1 0 1 6 0
  0 0 2 1 5
  0 1 0 3 4
```

It is a sanity input, not an expected negative outcome. Along a positive quotient edge whose two diagonals are1 and which has no common third neighbor, an actual lift would satisfy SX+XT+X=J for two internal matchings. The commuting involutions L:X↦SX and R:X↦XT give I+L+R eigenvalues3,1,1,−1; hence X=J/3, contradicting binary X. The profile only marks such pairs after a model is found; it never prunes them. A model without this mark is not asserted liftable, and the profile makes no claim that this is the only lifting obstruction.

## Sanity, budget, and output

`--mode sanity` checks the given model, the root's additional (3,3,15,15,25) model, and the two saved c=3 examples by direct matrix multiplication, then verifies retention of each given row through row generation and progressively assigned interfaces. It does not enumerate the old c=3 classification. It prints a result without creating a data file.

`--mode profile` performs one continuous deterministic traversal of the seven selected inputs in saved order. It enumerates all labelled models reached within one single-core budget, including alternatives with the same sizes. OS CPU cap10 seconds, internal CPU stopping at9 seconds, internal wall stopping at18 seconds, external wall cap20 seconds,4 GiB. There is no restart, enlarged budget, or automatic follow-up. The remaining58 require a separate root decision based on measured cost.

Original commands (historical; do not rerun the completed profile):

```bash
python computations/dd82/n61/component_joint_quotient.py --mode sanity
timeout 20s python computations/dd82/n61/component_joint_quotient.py --mode profile
```

Save `.profile.json` with all65 input records and explicit selection flags, per-item statistics/resources, every actual Q entry and sizes, and post-model lifting marks. Each item is `MODEL`, `EXHAUSTED_NO_MODEL`, `UNKNOWN_BUDGET`, or `NOT_STARTED`; `enumeration_complete` separately distinguishes a model-bearing completed domain from a model-bearing interrupted one. `COMPLETE_SELECTED_PROFILE` means exactly the seven selected domains were exhausted; `full_input_complete` remains false. Budget exhaustion does not imply infeasibility. Models are labelled, not distinct isomorphism classes or actual graphs.

Root manages the independent source review and the existing Gemini thread; no new reviewer, solver package, queue, hash, or shared-status edit is introduced here.

## New delta: stabilizer sorting for exactly18 unfinished sizes

The actual remaining-input run completed all c=9,11,13 domains and the first c=15 domain. Its second c=15 tuple, `(2^8,5^5,10^2)`, used about53.337 CPU seconds and41,612 search nodes before the global limit. This is the concrete repeated-label bottleneck motivating the new reduction; no completed size is rerun.

At a search node, let K be the assigned indices and i the row chosen by the existing MRV rule. Group the still unassigned columns j≠i by the exact key

`(n_j, tuple(full_original_diagonal_domain_j), (q_kj for k in sorted(K)))`.

Within each key, require q_ij to be nondecreasing in j. Do not sort together columns with different diagonal domains or different previously assigned-row signatures. The generator already orders columns by option count and then index; equal-key columns have equal sizes and option counts, so it encounters their indices in increasing order. It compares each option only with the previous member of its own key. The suffix counts remain unreduced; they are used for MRV and necessary zero tests exactly as before.

Coverage proof: take any target completion at this node. Permute columns within one key and simultaneously apply the same permutation to row labels, fixing every assigned index and the current i. Sizes and complete diagonal domains are unchanged. Every assigned row is unchanged because its entries on that key are equal. Every assigned column is also unchanged: detailed balance and the common size n_j determine q_jk from q_kj. The original matrix equation, row sums, trace, and all earlier canonical inequalities are preserved; the earlier assigned rows remain entrywise identical. Choose the permutation to sort the entries of row i inside each key. This target representative occurs in the canonical generator. After assigning row i, apply the same argument to the smaller stabilizer at the next node. Induction preserves at least one representative of every original size/domain-preserving isomorphism class.

MRV does not invalidate the argument: the permitted permutation fixes the current i and leaves the current assigned state unchanged, so that node's selected row is unchanged. Unreduced row counts may overestimate canonical choices but cannot incorrectly declare zero when a target completion exists.

This is a covering symmetry reduction, not a claim of unique canonical forms. Saved model counts may include isomorphic duplicates and are not labelled-model totals or exact isomorphism-class counts.

## Delta inputs, sanity, and resources

`unresolved` reads both actual `.profile.json` and `.remaining.json`, collects precisely those size tuples with `enumeration_complete=true`, and subtracts their union from the full65 inputs. Require7 and40 completed tuples respectively,47 in their union, and exactly18 remaining. An interrupted tuple with no model is not treated as complete. Previously found models likewise do not alone imply completion. The old modes do not read these completion files or enable canonical sorting.

`symmetry-sanity` applies canonical enumeration only to the two actual c=5 model size types. It requires an output isomorphic to each supplied Q under a size- and diagonal-domain-preserving permutation, checking the relevant at most5! permutations directly. Every returned Q also passes the existing direct matrix verifier. This does not rerun the c=3 classification. The mode was actually executed before unresolved and retained both classes; see component_joint_quotient.symmetry-sanity.json.

The unresolved run has OS CPU cap60 seconds, internal stopping at57 CPU/73 wall seconds, external wall cap75 seconds, single CPU1 and4 GiB. It writes only `.unresolved.json`, preserving both previous results. Each of the18 selected inputs still distinguishes model found, exhausted without model, or budget interruption; `enumeration_complete` now means exhaustive coverage up to the proved stabilizer reduction. The combined65-input coverage flag can become true only if all18 new inputs finish, relying explicitly on the saved47 completed inputs. No automatic extra run follows.

New commands, to be run by root only after delta source review:

```bash
python computations/dd82/n61/component_joint_quotient.py --mode symmetry-sanity
timeout 75s python computations/dd82/n61/component_joint_quotient.py --mode unresolved
```
