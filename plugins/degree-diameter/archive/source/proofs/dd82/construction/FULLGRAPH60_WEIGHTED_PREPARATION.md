# Full-vertex weighted search: preparation and actual bounded result

Run `dd82-v3-fullgraph-weighted60-20261013`: the preparation snapshot
was **PREPARED_NOT_RUN**, with source compiled and numerical sanity passed.
The root subsequently ran the single authorized trajectory: **the best
raw bad count among accepted trajectory states remained 20; the final
graph has 26 bad pairs. No verified target was produced.** The actual
result and independent BFS are recorded below.
The original preparation receipt used the
transposed spelling `dd82-v3-fullgraph60-weighted-20261013`; that receipt
is preserved, while `changes.preparation.json` records the corrected
existing ARIS run name without rewriting the original execution.

The implementation follows the project's experiment-bridge skill under
the V3 mathematical adaptation: exact CPU graph computation, preparation
before deployment, and independent graph verification owned by the root.
Automatic deployment is disabled for this task. There is no GPU,
submission workflow, hash, or new experiment platform.

## Actual input and changed domain

The seed path is read from the existing actual record
[`twin_seed_unrestricted_switch_run/twin60.json`](../../../computations/dd82/construction/twin_seed_unrestricted_switch_run/twin60.json),
whose `source` points to
[`petersen_all_matchings_run/candidate.best.edges`](../../../computations/dd82/construction/petersen_all_matchings_run/candidate.best.edges).
Its complete text was copied unchanged to
[`fullgraph60_weighted_run/seed.edges`](../../../computations/dd82/construction/fullgraph60_weighted_run/seed.edges).
It has 60 vertices, 240 edges, all degrees eight, and 20 uncovered pairs.
The old complete unrestricted two-switch scan had 42,440 legal distinct
neighbors and best distinct-neighbor score 22. That old result is a
reference, not a newly repeated experiment.

The new state is an arbitrary labelled simple eight-regular graph on
these 60 vertices. Every pair of disjoint edges and both alternative
pairings are considered, rejecting replacements with existing added
edges and, after the first accepted move, the exact inverse of the most
recent accepted switch. The inverse test compares unordered removed and
added edge sets. No fiber partition, C5 action, false-twin condition, HS
core, triangle cap, or original edge is preserved by a constraint.

## Weighted rule

For each unordered vertex pair maintain a positive integer weight,
initially one, and evaluate

`W(G)=sum_{u<v} w_uv [u,v have no edge and no common neighbor]`.

Each iteration completely scans the current legal two-switch
neighborhood. If its minimum W is strictly below the current W, perform
that move; ties use the first move in deterministic lexicographic edge
order. The last accepted move persists across weight-only updates;
only another accepted move replaces it. Raw bad-pair count can increase. There is no
temperature, random generator, restart, or neutral weighted move.
All weights remain positive, so W is zero exactly when every pair is
covered by a path of length at most two.

When every eligible move has `delta_m=W(G_m)-W(G)>=0`, let k_m count
old bad pairs repaired by m. A uniform increment t on the current bad
pairs changes this difference exactly to `delta_m-t*k_m`: newly bad
pairs were previously covered and do not receive an increment. Therefore
the program increments every current bad-pair weight by

`t = min_{eligible m, k_m>0} (floor(delta_m/k_m)+1)`.

This skips exactly the ineffective unit increments before the first
eligible strict improvement becomes available, then rescans. The same
complete scan computes k_m on changed-endpoint pairs and caches this
threshold; it needs no extra candidate scoring. Partial scans never
trigger a weight jump.

Only the four switched vertices change their adjacency rows. A pair
whose two endpoints are outside that set retains both its adjacency
and its common-neighbor set. Thus a trial's exact weighted/raw changes
are computed on the 230 unordered pairs incident with that four-set.
After accepting a move, the implementation recomputes the full objective
and checks both scores against the predicted values. A partial scan at
the time boundary never supplies an accepted move or a weight update.

### A fixed graph cannot trap this rule indefinitely

Let u,v be a currently uncovered pair. Their neighbor sets are disjoint.
There exist nonadjacent `a in N(u)` and `b in N(v)`: otherwise each
`a in N(u)` would have u and all eight vertices of `N(v)` as distinct
neighbors, contradicting degree eight. Removing ua and vb and adding
uv and ab is therefore a legal two-switch that repairs at least the
old bad pair uv. Each of the eight choices of a admits at least one such
b, giving at least eight distinct repair switches. Banning a single
inverse still leaves at least seven eligible choices.

While the graph remains unchanged, all its old bad-pair weights increase
together. For that fixed move, any new bad pairs belonged to the old
covered set and their weights do not increase. No additional element
can be added to the already complete set of old bad pairs; the move
repairs at least one of them. Consequently its weighted difference
decreases by at least one on every such uniform increment, and after
finitely many increments it is strictly improving. This only prevents
infinite stasis at one graph. It neither proves existence of a target
nor guarantees convergence or completion within the resource bound.

## Actual preparation and saved outputs

Source:
[`fullgraph60_weighted.cpp`](../../../computations/dd82/construction/fullgraph60_weighted.cpp)
and
[`fullgraph60_weighted_run.py`](../../../computations/dd82/construction/fullgraph60_weighted_run.py).

The actual command executed was:

```
python3 computations/dd82/construction/fullgraph60_weighted_run.py prepare
```

The first compile exposed a local `apply`/`std::apply` name collision;
the operation was renamed `apply_switch`, then compilation and sanity
were run. The original compiler output is retained as
`compile.first_attempt.log`. The successful compilation used
1.007837 CPU seconds and 1.067711 wall seconds. The sanity process used
0.094103 CPU seconds and 0.115612 wall seconds; these are stage timings,
not a total including the failed first compile.

Exactly 1,000 legal proposed switches were checked without accepting
an optimization trajectory: 500 with unit weights and 500 with
nonuniform positive weights. An independent explicit adjacency matrix
and all actual intermediate vertices recomputed every pair's coverage;
it does not use the bitset-intersection or changed-endpoint formula.
All weighted and raw scores agreed, every move preserved simplicity
and all degrees, and every inverse operation restored the seed. A
separate same-graph weight increment check also passed. This is a short
implementation sanity, not a new neighborhood result or full-graph BFS.

Receipts:
[`preparation.json`](../../../computations/dd82/construction/fullgraph60_weighted_run/preparation.json)
and
[`sanity.json`](../../../computations/dd82/construction/fullgraph60_weighted_run/sanity.json).

Gemini direction review, thread
`a5651107-8d41-4c2f-b90a-cace40b49f2e`, motivated the inverse ban and
exact weight jump before launch. Only the new behavior received an
additional `prepare_changes` sanity: a real move has exactly one inverse
candidate, the ban persists through weight changes, and the next accepted
move replaces it. For 64 trial moves, k_m agrees with full pair-set
differences; independent explicit coverage verifies `delta_m-t*k_m`
at the computed threshold and its predecessor. All checks passed, using
0.013540 CPU and 0.017629 wall seconds. Successful recompilation used
1.399783 CPU seconds. This restricted sanity did not repeat the original
1,000-proposal check or establish a new neighborhood result.

The original source and changed source/runner were read by root. These
are local same-family checks; the Gemini direction response is not
represented as an execution or code-level verification.
Receipts are
[`changes.preparation.json`](../../../computations/dd82/construction/fullgraph60_weighted_run/changes.preparation.json)
and
[`change_sanity.json`](../../../computations/dd82/construction/fullgraph60_weighted_run/change_sanity.json).

The formal command, whose execution is owned by root, is:

```
python3 computations/dd82/construction/fullgraph60_weighted_run.py run
```

It permits one process on CPU 0, a 60 CPU-second operating-system limit,
90 wall seconds, and 4 GiB memory. Internal limits of 59 CPU/88 wall
seconds reserve time for output. A launch receipt prevents accidentally
starting a second episode. The runner does not perform another search
or invoke BFS automatically.

During the formal trajectory, strict new raw-bad minima save complete
edge tables and JSON; the first departure, best graph, and final current
graph are saved separately. A compact event log records every accepted
switch and every weight update, sufficient to replay from the seed;
the final 60-by-60 weight matrix is saved explicitly. Counters include
complete/partial scans, evaluations, weight updates, and raw-bad
increasing/equal steps, inverse bans, maximum weight and the number of
distinct pairs receiving increments. First/best/final bad-pair lists
and overlaps with the initial bad set are saved. Every accepted graph
is directly compared with the preceding four full adjacency arrays,
recording equality counts by lag without hashes. These counts do not
measure all-time uniqueness, and bad-set migration alone does not prove
that the original C5 action has been lost.

No RNG state exists. The final graph, weights and last accepted move
give a state checkpoint; an incomplete neighborhood is not retained.
There is no automatic continuation.

A target candidate stops immediately and requires the parent's
independent full-edge BFS. Otherwise the output is only a bounded
heuristic result. It cannot prove nonexistence of an order-60 target.

## Formal result

The root executed exactly one formal trajectory, which exited normally
with `stop_reason=budget_during_neighborhood`. The last partial scan
did not supply an accepted move or weight update. The process used
**59.006266 CPU seconds and 59.150185 wall seconds**, excluding the
earlier preparation and the separate subsequent BFS checks. It remained
single-threaded on CPU 0, with no restart or extra trajectory.

| Actual quantity | Value |
| --- | ---: |
| Complete neighborhood scans | 520 |
| Final partial scans | 1 |
| Eligible switches evaluated | 22,086,250 |
| Accepted weighted-descent moves | 449 |
| Accepted moves increasing raw bad count | 164 |
| Accepted moves preserving raw bad count | 121 |
| Weight-update events | 71 |
| Unit-increment rounds skipped by exact jumps | 2 |
| Total pair-weight increments | 2,787 |
| Distinct pairs whose weights increased | 1,135 |
| Maximum final pair weight | 13 |
| Exact inverse moves excluded | 518 |
| Final weighted objective | 193 |

Actual execution and counts are in
[`resources.json`](../../../computations/dd82/construction/fullgraph60_weighted_run/resources.json)
and
[`search.json`](../../../computations/dd82/construction/fullgraph60_weighted_run/search.json).
The resource record's `independent_final_bfs_performed=false` describes
the runner, which deliberately does not run BFS. The root subsequently
ran the generic independent checker on the four saved graphs below;
each has 60 vertices, 240 edges, every degree eight, and diameter three.

| Saved graph | Bad pairs | Intersection with original 20 bad pairs |
| --- | ---: | ---: |
| `candidate.best` (unchanged original seed) | 20 | 20 |
| `candidate.first_departure` | 22 | 14 |
| `candidate.current` | 26 | 0 |
| `candidate.alternative20` (first non-seed state with 20) | 20 | Not used for the conclusion |

The four independent receipts are
[`candidate.best.verification.json`](../../../computations/dd82/construction/fullgraph60_weighted_run/candidate.best.verification.json),
[`candidate.first_departure.verification.json`](../../../computations/dd82/construction/fullgraph60_weighted_run/candidate.first_departure.verification.json),
[`candidate.current.verification.json`](../../../computations/dd82/construction/fullgraph60_weighted_run/candidate.current.verification.json),
and
[`candidate.alternative20.verification.json`](../../../computations/dd82/construction/fullgraph60_weighted_run/candidate.alternative20.verification.json).
Corresponding complete edge tables/graph JSON and bad-pair lists are
saved in the same run directory.

The root replayed all events using complete adjacency states and direct
equality. There were 449 distinct states including the initial graph
among 450 visits, hence one accepted return visit; the recent-state
counter identifies one lag-three return. Seven accepted states had raw
score 20, while the highest accepted raw score was 68. These are actual
trajectory statistics, not an imposed uniqueness threshold.

The structural receipt
[`trajectory.structure.json`](../../../computations/dd82/construction/fullgraph60_weighted_run/trajectory.structure.json)
also directly checks the saved original C5 permutation and original
six-fiber structure. The first departure no longer preserves that
specific C5 action, but still lies in the original six-Petersen-fiber
matching model. The alternative 20-bad graph likewise loses that
specific action while retaining the original fiber model; its edge
symmetric difference from the seed is 14. It is not a best-score
improvement, and no nonisomorphism or absence of every possible C5
action is claimed.

The final 26-bad graph genuinely leaves the original six-fiber degree
pattern at 38 vertices, removes 22 original internal-fiber edges, and
has edge symmetric difference 122 from the seed. It also fails to
preserve the specific original C5 action. This conclusion comes from
direct adjacency/edge checks, not merely from migration of the bad-pair
set. It shows the released search domain was used, while the minimum
bad count still failed to improve.

The complete accepted-move and weight-update sequence, final weights,
last move and state checkpoint are retained. The pilot is complete and
nonexhaustive; it supplies no order-60 exclusion or target construction.
Same-thread Gemini round 2 result review has returned SUCCESS; its
accepted scope and the root's corrections are recorded below.
No additional search, diagnosis, or audit was launched for this report.


## Actual workflow adaptation and direction result

This is run dd82-v3-fullgraph-weighted60-20261013. The local research-pipeline, idea-discovery/idea-creator and experiment-bridge instructions are used with the explicit V3 mathematics adaptation. Existing source-paper case studies and both enriched wiki paper pages supply context; no new broad survey, novelty score, publication ranking, GPU pilot or second-model brainstorming gate is claimed. A local shard checked old search domains; another independently derived a concrete generaln61 component obligation, which remains separate from this60-vertex mechanism. Gemini selected one executable full-graph pilot; no claim of novel mathematics is needed.

Direction SUCCESS on thread a5651107-8d41-4c2f-b90a-cace40b49f2e, actual CLI gemini-3.8-flash-high/high. Root accepted the exact reversal ban and the exact weight jump, not the proposed hashes or arbitrary uniqueness/weight thresholds. The original seed's42440 neighbors are not a constant for all8-regular graphs. Root and a fresh local reader checked the original source; root checked the actual modification and added sanity. Full raw request/response and reviewer memory are in the matching .aris/traces/auto-review-loop directory. The formal trajectory and independent graph checks are complete.

## Same-thread result review and closure

Gemini round 2 returned **SUCCESS** on the same thread, with actual
returned model/effort `gemini-3.8-flash-high` / `high`. The original
response is preserved in
[`20261013_V3_fullgraph_actual_results_review.json`](../../../reviews/dd82/20261013_V3_fullgraph_actual_results_review.json)
and the matching trace's `002` response. It confirmed the implemented
inverse ban and exact weight jump, the fixed-state non-stasis argument,
the actual trajectory and graph checks, and the absence of a produced
target. This is a review of supplied evidence, not a second execution.

The root retained the following corrections to the review:

- An “entropic barrier” and a search-space size of approximately
  `10^70` are not established by this experiment and are not adopted
  as findings.
- Twenty is the best recorded raw count on the accepted trajectory.
  The program did not retain a minimum raw score over all 22,086,250
  evaluated proposals. It therefore does not establish that every
  evaluated candidate had at least 20 bad pairs, much less a global
  lower bound.
- Seven accepted visits at raw score 20 are visit counts. They do not
  establish seven distinct labelled graphs or seven nonisomorphic
  graphs.
- The structural checks negate the particular original C5 permutation
  and, for the final graph, the original fiber representation. They
  do not exclude alternative C5 actions or another representation of
  the same type.
- Reviewer advice does not determine the user's authorization scope.
  The root makes the execution decision under the existing user
  instructions; the reviewer's statement about authorization is not
  itself permission or a user-imposed restriction.

On the actual outcome, the root adopted **no additional computation in
this unchanged mechanism**. Its bounded review loop closes early after
2 of at most 4 rounds: direction review, implemented changes, one real
pilot, independent checks, result review and an explicit stop decision.
No further search or review is appended merely to fill the remaining
rounds. Arbitrary order-60 graphs and the overall unresolved 58–61
construction/exclusion problem remain open.
