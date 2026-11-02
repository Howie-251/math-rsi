# Root review: automorphisms and a new small-orbit construction

2026-10-12, phase begun 07:37:13 UTC. These are local mathematical and
computational checks. External review and Lean acceptance are separate;
no new arbitrary-order exclusion or graph above 57 follows.

## Completed local checks

- Read the complete S6/A4 generation/search source, actual preparation and
  search resource records, both complete histograms and both independent
  all-source BFS summaries. The two supplied actions give 8+8 degree-eight
  orbital unions, all failing. Saved complete graphs have 60 vertices,
  240 edges, all degrees eight, diameter four and 690 bad pairs each.
  The elementary stabilizer argument covers every order-twelve subgroup
  of S6: non-even H gives transitive A6; even H has four Sylow 3-subgroups,
  is A4, and has one of the two faithful six-letter actions. Together with
  the previous A6 exclusion this closes all transitive S6 targets.
- Read the full arbitrary-graph proof in
  `proofs/dd82/construction/AUTOMORPHISM_PRIME_60_61_OBSTRUCTION.md`.
  The fixed graph has diameter two because nonadjacent fixed vertices
  have fewer than seven common neighbours. A fixed boundary leaf forces
  fixed-set size 2 or 9, contradicting the actual residues 4 and 5. The
  large-prime propagation lemma then restricts Aut of a 60-point target
  to prime divisors 2,3,5. No transitivity hypothesis is used here.
- Read the full independently checked proof
  `VT60_ABELIAN_ODD_NORMAL_SEMIREGULAR.md`. Both normality and transitivity
  are indispensable: they give equal p-point orbits. Abelianity makes
  orbit stabilizers equal within each orbit; distinct stabilizers across
  an edge force Kp,p. The p=3 argument uses the unique partner of each
  three-point orbit, excludes three stabilizer classes by two-step paths,
  then bounds same-class reach by 26+2<30. The C15 corollary explicitly
  retains the previously completed four Z15-orbit dependency.
- Read the primitive-catalog report, actual orbit source and saved
  result summaries. The nine official degree-60 records have minimum
  nontrivial undirected orbital degree at least 12, so each recorded
  action is excluded without graph enumeration. Published low-degree
  primitive classification and correspondence to this official catalog
  remain explicit external dependencies if promoting this to all
  primitive actions. The small computation is not a proof of catalog
  completeness; no all-VT60 claim is made.

## Actual cyclic seed diagnosis and current construction

The actual twenty-bad-pair graph was not shown to have a C5 action. Its
complete original-fibre-preserving subgroup test has no free C5; the
unrestricted automorphism iteration timed out after 4.600 CPU seconds.
The endpoint-based unique-lift proposal fails: forty other vertices
have only ten distinct endpoint-neighbour sets, each repeated four times.
This is an obstruction to that shortcut, not a nonexistence proof for C5.

The older fifty-bad-pair graph does have a saved, explicitly verified
permutation of type 5^12. All 240 edges were checked; relabelling yields
354 possible edge orbits and 48 selected orbits. Exact voltage coverage
reproduces all fifty bad pairs. These data are saved under
`computations/dd82/construction/cyclic5_twelve_orbits60_endpoint_run/seed50/`.

A new construction experiment releases all original six-fibre and
Petersen restrictions. Its degree-preserving moves change a selected
orbit's shift or replace two selected orbits by two new orbits on a
re-pairing of their four quotient endpoints. Loops contribute degree two
and represent actual five-cycles; distinct-orbit checks ensure simplicity.
One deterministic strict-descent episode has a total 30 CPU-second limit;
no quotient necessary condition is imposed on intermediate states.
At this checkpoint the search implementation/run is active; its result
is not yet claimed. Actual accepted graphs and final independent BFS
are required before reporting an improvement.

The separate order-59 order-seven proof is written in
`AUTOMORPHISM_ORDER7_N59_EXCLUSION.md` and awaiting independent review at
this checkpoint. It will not be labelled reviewed before that completes.

No n62, known 57/63–65, or old Lean work was restarted. No hashes were
generated. Previous Antigravity C17 authentication failures remain closed
with no mathematical verdict; no new external state justified a retry.

## Completed follow-up checks, approximately08:22UTC

The order59 order-seven proof has now been independently checked and
accepted. Together with the earlier60/61 argument, the order-seven
obstruction covers arbitrary targets at all three orders59–61.

The actual twenty-bad-pair graph now HAS a verified freeC5 action. The
three-relation endpoint graph (adjacency,bad pairs,signature pairing) has
an order-five action; its ten four-point signature classes have a connected
quotient with every nonempty interface a perfect matching. Transporting
one root-class bijection yields an actual order-ten automorphism whose
square has type5^12. Root read the full lifting source and actual result;
all240 original edges were checked. The two incomplete earlier diagnostics
are superseded on existence, not retroactively made complete enumerations.

Root read the full general orbit-switch C++ source, the seed20 adaptation
diff and full runner, actual search/resource outputs and independent BFS
summaries. The old50 and actual20 seeds have complete single/two-orbit
neighbourhoods with no strict improvement:60092 and60792 legal nonidentity
parameter choices, respectively. Repeated terminal graphs were not deduped.
Actual final graphs remain50 and20 bad pairs, both diameter3. No neutral
extension or random restart occurred.

Root derived and read the independently checked complete proof in
CYCLIC5_K66_QUOTIENT_EXCLUSION.md. All-internal-cycle quotients first
reduce to2I+A(K6,6). Normalized six-by-six F5 voltage differences yield
both Gram matrices5I+J. Common complex row/column sums would have squared
norm11, forcing six fifth roots' multiplicities to have square sum16,
which is impossible. The exactly-one-independent-orbit case is separately
excluded using quotient row budgets. Thus any target for a freeC5 action
needs at least two independent orbits. The actual20 seed has precisely
the excluded all-internal-cycle quotient; keeping its quotient for a
further voltage-only search has no mathematical justification.

Root also read the complete four-orbit quotient source and actual full
result. All49995 deletion sets and105 pairings each finished. Among
5249475 parameter choices,165915 satisfy all necessary quotient filters;
every one has no independent orbit and is already excluded by the pure
proof. The report's padding argument preserves all repairs changing at
most four selected orbits. Hence this chosen-action local domain is
closed; it is not a lower bound on arbitrary unsymmetric graph edits.

A distinct58-point construction input was generated from an actual HS50
order-seven automorphism. Root read its full source and result: all175
HS edges and232 new graph edges are checked, the action has two fixed
points and eight7-cycles, and the complete58/232/eight-regular seed has
105 bad pairs by independent BFS. It preserves induced HS and is a known
failed baseline. The new subsequent construction releases all original
HS core edge-orbit choices; at this checkpoint its bounded search is
still pending. No unchanged induced-HS search was restarted.

## Final58 construction check, 2026-10-12 08:28 UTC

Root read CYCLIC7_EIGHT_ORBITS58_SEED.md in full, including the general
fixed-layer argument, f2 independence and f9 star/false-twin branch.
The full f2 generator is distinguished from f9 and arbitrary graphs.
Root read the complete C7 switch C++ source, real three-level outputs,
resource records and runner's original-HS comparison. Weighted scoring
counts each fixed point once and each seven-orbit representative seven
times, then divides directed bad pairs by two. All moves preserve the
fixed15 actual edges and each core row degree. No quotient condition
was imposed on intermediate states.

Actual descent105→77→63 ended after three complete49221-move scans.
Both accepted states, complete edge tables and parameters are retained;
final independent BFS is58/232/all8/diam3/63bad. Direct comparison with
the original175HS edges finds zero deletions in every accepted state.
Therefore no genuine exit from the known-closed induced-HS family has
occurred. Further attachment-only repair is not a useful next target.
All computations are finished; final short narrative report is being
saved from these already complete artifacts. Overall N interval remains
57..61, with no graph above57 and no new arbitrary58–61 exclusion.

Final narrative report CYCLIC7_EIGHT_ORBITS58_SWITCH_RESULT.md is now saved
and read by root. All agents and computations have finished; no report,
solver, search or external call remains pending at the phase checkpoint.
