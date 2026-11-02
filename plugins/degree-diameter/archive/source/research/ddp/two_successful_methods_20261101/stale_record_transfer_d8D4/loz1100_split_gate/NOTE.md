# The inherited1100 source cannot gain one point by this single split

Actual result: the singleton-support prediction is supported. The identity
route layers have sizes(1,8,56,361,674). Of the674 distance-four targets,
95 have singleton first-hop supports. The first target is2, with support
mask64, whose only first neighbor is533 (port6 in the saved dart order).
A genuine old four-step route is0--533--459--223--2. The split side not
assigned neighbor533 cannot reach2 within four steps. This logically excludes
all254 oriented partitions, or127 up to swapping the two roles; no partition
enumeration was needed, and there are no survivors.

The terminal receipt records actual process CPU0.016906178 seconds plus
a separately declared conservative preparation charge0.1, for total
case charge0.116906178/10. No candidate edge file or full-target BFS was run.

The actual prediction result, all distance-four first-hop support masks and
the terminal CPU are saved separately. If RESULT gives a singleton witness,
every partition is rejected logically without enumerating partitions: that
single mandatory first neighbor belongs to only one side. If it instead
reports a two-coloring rejection, the127 complement representatives were
actually checked. This is a split-route calculation, not a rerun of source
graph validity or an all-root source BFS.

Take an old target x at source distance4 from root0. Any route of length at
most4 from either split role to x must begin with one of that role's assigned
old neighbors. A route starting across the new role-role edge has at least
one inserted step beyond a four-step source route. Projecting any putative
short route back onto the source gives a length-at-most4 source route; at
distance4 it must be a geodesic with first neighbor in that role's assigned
set. Therefore both parts of the partition must meet every recorded
first-hop support. A singleton, or failure of all127 two-colorings, excludes
the rule. The genuine source four-step path is a witness of the actual
boundary target, not a path in a newly generated graph.

Old targets at source distance at most3 cause no new-root exception: a source
geodesic can be followed from either role with at most one role-role step,
giving length at most4. No old-old pair was tested; if this necessary gate
had survived, old routes crossing the split root could still gain a step.
Here the failed new-root necessary condition already suffices to stop before
generating any1101 edge file or running full-target BFS.

The source is the inherited RIGHT-law C20 semidirect_2 Z55 Cayley recipe.
Left translations preserve its fixed generator graph and carry any chosen
source root to identity0, including its neighbor partitions. Thus the
identity obstruction excludes this same single-split rule at every source
vertex; no general automorphism enumeration is used. The previous failed
5500-point cyclic25 cover is a separate scope, not a premise that this split
must fail.

This does not exclude splitting multiple vertices, adding other edges,
moving other source edges, other sources or any general(8,4) construction.
No new graph, global record or Lean result is counted. The batch stops.

