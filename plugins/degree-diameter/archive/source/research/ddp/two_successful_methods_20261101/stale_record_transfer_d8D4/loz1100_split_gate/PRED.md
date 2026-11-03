# A single vertex split of the inherited Loz1100 source

Prediction before the only new calculation: among the actual distance-four
targets from identity0, at least one has a single possible first neighbor
on every shortest four-step route. Such a singleton support would immediately
exclude every nontrivial partition of the eight source neighbors between
two adjacent split vertices. The prediction can fail; then test the finite
boundary-support two-coloring condition and return any surviving partition,
without automatically generating a1101 graph.

The already accepted source recipe is RIGHT-law C20 semidirect_2 Z55:

    (j,x)(k,v)=(j+k mod20, x*2^k+v mod55), label=55*j+x.

Positive generators are(1,0),(12,33),(11,1),(16,19), together with their true
inverses. This recipe is inherited from
more_graphs_20261027/d8_D5_loz1100_cyclic25_cover/REPORT.md and run.py;
their failed5500-point cyclic25 cover is a different rule, and is not rerun.
No same-rule1100 single-split exclusion was located in the targeted local
split/source notes. The source's simplicity,8-regularity and diameter4 are
inherited, not independently revalidated.

Replace source root0 by adjacent roles a,b. Partition its eight original
neighbors into nonempty A,B, retain all other source edges, join a to A and
b to B. Both degrees are at most8 when1<=|A|<=7. For every old target at
source distance4, BOTH A and B must meet its first-hop support. Crossing the
new a-b edge before following a four-step source route costs five steps.
Conversely all old targets at source distance<=3 are automatically within4
of both roles: route through the appropriate role with at most one added
step. This is only a new-root necessary gate; old-old routes through the
split root can also lengthen and are not certified by boundary survival.

One radius-four identity route/support calculation is input to this new
question, not a source all-root BFS. Cayley left translation lets us fix
root0 and transfers a failure to every possible split root. No general
automorphism search is needed. If any singleton support exists, stop with
its actual target and genuine four-step route and a logical count of all
254 oriented partitions (127 up to A/B exchange) excluded. If no singleton
exists, check at most127 complement representatives. If one survives,
return it for root's next decision, without a full candidate/BFS.

New case total at most10CPU seconds including preparation, with a separately
declared conservative0.1CPU preparation allowance. No compilation, solver,
full source validity/D4 recheck, all-root BFS, old5500 cover run, new edge
file, field/rank/Lean, review, installation, hash or web task.
