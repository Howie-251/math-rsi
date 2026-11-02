# Deterministic switches in the full twelve-orbit C5 domain

One complete neighbourhood of the verified 50-bad-pair seed was tested
after releasing all original six-Petersen-fibre restrictions. No strictly
improving move exists in the specified one- or two-edge-orbit
neighbourhood. The episode stopped immediately after that complete
round: zero moves were accepted, and the final graph remains the
60-vertex, 240-edge, eight-regular input with diameter three and fifty
bad pairs. This is a local obstruction for the stated moves at this
seed, not an exclusion of the full C5-invariant graph family.

Source:
[cyclic5_twelve_orbits60_switch.cpp](../../../computations/dd82/construction/cyclic5_twelve_orbits60_switch.cpp),
[runner](../../../computations/dd82/construction/cyclic5_twelve_orbits60_switch_run.py).
Actual records:
[search.json](../../../computations/dd82/construction/cyclic5_twelve_orbits60_switch_run/search.json),
[resources.json](../../../computations/dd82/construction/cyclic5_twelve_orbits60_switch_run/resources.json).

## Input and full graph domain

The input is the actual voltage representation of the old fifty-bad-pair
graph, exported and checked in
[the endpoint and old-seed report](CYCLIC5_TWELVE_ORBITS60_ENDPOINT_AND_OLD_SEED.md).
It is distinct from the later twenty-bad-pair graph, whose C5 symmetry
has not been established.

Vertices are (a,t), 0≤a<12 and t∈Z5, labelled 5a+t. The complete domain
contains 354 edge orbits under common translation of t: five matching
shifts for each unordered pair of distinct vertex orbits, and two
internal cycle orbits of steps one and two per vertex orbit. All have
five edges and together partition K60. The seed selects 48 of them.

The new experiment allows any of these 354 orbits. It imposes no
Petersen internal graph, old six-fibre interface condition, quotient
capacity filter or retained Hoffman–Singleton core. Every trial is a
complete graph obtained by replacing selected edge orbits.

## Precisely enumerated moves

For every currently selected orbit, enumerate all legal shifts on its
unchanged unordered quotient endpoint pair. An internal orbit has shifts
one and two; a nonloop quotient pair has shifts zero through four.

For every unordered pair of distinct selected orbits, list their four
quotient endpoint occurrences. Enumerate all three perfect matchings of
these four occurrences, including the original quotient pairing, and
all legal shifts for the two resulting orbits. Reject a repeated new
orbit, a new orbit already selected outside the removed pair, and an
unchanged final orbit set. This includes simultaneous changes of two
shifts without changing their quotient endpoint pairs. Repeated endpoint
labels can make different parameter choices produce the same graph;
the recorded counts are parameter choices, not distinct graphs.

A quotient loop contributes two to the degree of its vertex orbit; a
nonloop contributes one at each endpoint. Re-pairing the same four
endpoint occurrences therefore preserves every weighted quotient degree,
even when the number of quotient loops changes. Since edge orbits
partition K60 and duplicate selected orbits are rejected, every trial
remains simple with sixty vertices, 240 edges and all degrees eight.

The score is the exact number of bad unordered pairs in the expanded
60-vertex graph. For each of the twelve representatives (a,0), the code
forms its actual one- and two-step neighbourhood using all sixty
adjacency rows. If the sum of the twelve missing-target counts is b,
the full number of bad unordered pairs is 5b/2 by translation symmetry.
Thus this is an exact graph score, not a quotient surrogate.

The algorithm scans moves in fixed order, retains the first move attaining
each strictly smaller score, and would accept a minimum only after
completing the round. A partial round at the CPU boundary would save its
best complete graph with the partial status. There is no random restart,
neutral move or increase in score.

## Actual complete round

| Round | Starting bad pairs | Single-orbit choices | Two-orbit choices | Legal nonidentity evaluations | Minimum | Complete |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 50 | 234 | 78,324 | 60,092 | 50 | yes |

The raw choice counts include choices later rejected by identity or
duplicate-orbit checks. The legal count may include the same final graph
through several parameter descriptions. Every valid graph in the stated
neighbourhood is nevertheless tested, since all three endpoint pairings
and every permitted shift are included.

No candidate had fewer than fifty bad pairs, so no move was accepted and
there was no second round. The exact stop reason is
`complete_neighborhood_no_strict_improvement`. This establishes a local
minimum for strict descent; it makes no assertion about neutral paths,
larger moves or the global 354-orbit construction domain.

## Complete graph and independent check

- [Final full edge table](../../../computations/dd82/construction/cyclic5_twelve_orbits60_switch_run/candidate.best.edges).
- [Graph, all 48 selected parameters and move record](../../../computations/dd82/construction/cyclic5_twelve_orbits60_switch_run/candidate.best.json).
- [Independent all-source BFS and all fifty bad pairs](../../../computations/dd82/construction/cyclic5_twelve_orbits60_switch_run/candidate.best.verification.json).
- [Structure in original six-fibre labels](../../../computations/dd82/construction/cyclic5_twelve_orbits60_switch_run/final.structure.json).
- [Exact input catalogue](../../../computations/dd82/construction/cyclic5_twelve_orbits60_switch_run/input.txt)
  and [saved initial complete state](../../../computations/dd82/construction/cyclic5_twelve_orbits60_switch_run/state000.json).

The existing independent checker reads only the final expanded graph and
performs BFS from all sixty vertices. Its score agrees with the search:
all degrees eight, diameter three, fifty bad pairs, and `valid_target=false`.
No separate initial BFS was repeated. Because no move was accepted, the
final graph retains the original six Petersen fibres; the search domain
itself allowed them to change. There are no missing accepted-state
artifacts: the number of accepted moves is zero.

## Resources

The runner reserved a total thirty-CPU-second budget including compilation
and the final independent check, pinned execution to one CPU, and limited
the search address space to 1 GiB. The complete round terminated well
before its allocated 27.705502254 search CPU seconds.

| Component | CPU seconds |
| --- | --- |
| Compilation | 1.291754 |
| Search process | 0.017155 |
| Independent final BFS | 0.029914 |
| Python runner | 0.006308259 |
| Total | 1.345140515 |

Total wall time was 1.378710624 seconds. Within the C++ process the search
record reports 0.015672 CPU seconds and 0.016294253 wall seconds; the
complete neighbourhood itself used 0.012649 CPU seconds. No solver,
additional episode or follow-on search ran, and no job remains active.
