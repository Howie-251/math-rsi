# One full-core boundary discriminator, 2026-10-27

Main mathematical candidate SP: no full 25-point complete ordered rank-3
no-B5/no-R6/no-weak7 coloring Y contains actual red five-sets A,B with
max A < min B and with t=max B an internal right root of Y.

## Exhaustive critical E6 entry

In an actual critical R with E={e1<...<e6}, tau=5, |R|=b+5, use the fixed
T=E\{e2}, Y=R\T. Any R6 ending e1 gives a five-set A wholly before e1,
inside Y. Any R6 ending e2 starts e1 and has four interior points between
e1 and e2; deleting e1 gives a red five-set B inside Y ending e2.
Thus max A<e1<min B, and e2 is an internal right root in Y. With the scoped
b=25, Y has exactly25 vertices. No choice of a convenient alternative
minimum transverse/complement is made. SP would exclude the entire E6
critical full-core branch, across all e(Y)=m(Y) equality types, but E5
would remain open. This is not asserted to prove D<=29 by itself.

## Full model and positive quantifiers

All2300 triple colors on the actual order25 are free. Require all12650
packets, noB5, noR6, noweak7. The D7 joint prohibition may be retained from
the unchanged base builder since noB5/noR6 already implies it by joining.
The two red five-sets and right root are existential over every actual
position, not fixed to favorable five-blocks or prefix positions.

An acceptable simple encoding: exact H_S <=> all ten triples of S red for
every five-subset S; root_v -> all triples (v,i,j) red for v<i<j, with no
use of unconstrained forward flags as positive existence. For every cut
c=4..19 in zero-based order, L_c is the OR of H_S with max S<=c;
K_S <=> H_S AND root_maxS; U_c is the OR of K_S with min S>c.
Selectors choose at least one cut and imply both L_c,U_c. Equivalence ORs
or direct positive disjunctions suffice. Every actual candidate has a
canonical extension, and every SAT selector supplies both real paths.
Root flags are existential witnesses, not reported as exact identities.

## Decision meanings, comparative value, and authorization

SAT with every clause checked and a full direct semantic recollection
refutes SP on a genuinely full core. It says the critical E6 proof must
use the remaining external endpoints and their private paths, not only the
two disjoint incoming witnesses and the root boundary. It does not refute
the joint tau5/full-core target. Checked/bound UNSAT would exclude the full
E6 critical branch using the reduction above; raw UNSAT is not enough.
Timeout has no conclusion, including on any unsearched cut/equality type.

This uses actual full capacity and all equality types, whereas the earlier
15-point minor deliberately omitted saturation and was refuted. The full
n30 D7 and n18 tau>=5 sealed jobs are not restarted or reused as conclusions.

Authorized: one new authoritative Linux external AE run, <=60s wall/CPU,
<=3GiB, native Sol/high, new saturated_pair25/ only. Preserve complete
source/formula/solver/assignment/semantic bindings. If SAT, recompute e,m
and provide both actual paths and every root triple. No retries, fallback,
new solver budget, or proof check. If execution fails, keep raw status.
