# Trace-sensitive link-overlap quota

Exact diagnostic strengthening, 2026-10-13. It is not used by any retained
strict certificate of the complete T34 paper candidate. The final 22-point
four-low table has 167 direct and two ordinary-joint certificates; the eight
weighted entries at 23 points are all non-strict diagnostics. The inequality
has a scoped Gemini review, but its Lean formalization is not needed for the
current proof. An earlier use-description was corrected after checking the
actual saved certificate fields.

Fix an actual selected center i in a simple five-uniform H on v vertices,
and a set R of other selected locks to avoid. Let F be the n distinct
incident edges avoiding R. Their links are distinct four-subsets of the
v−1−|R| allowed vertices. If d_a counts occurrences in these links, then

    sum_{unordered e,f in F} |(e∩f)\{i}| = sum_a choose(d_a,2)
      >= sum_a max(d_a−1,0) >= 4n−(v−1−|R|).

For a trace slot (T,U), let z_TU count distinct unordered edge pairs with
these traces whose links intersect. Set b=|T∩U|−1 and f_T=5−|T|.
An actual pair has link-intersection size at most

    h(T,U) = min(3, b + min(f_T,f_U)).

The bound 3 uses simplicity: two distinct five-edges through i cannot
share four additional vertices. For T=U this also gives 3, unless the
trace is already a full edge; the capacity of a repeated full trace is
then actually zero. Thus every actual input obeys the weighted quota

    sum_{T,U avoiding R} h(T,U) z_TU
       >= max(0,4n−(v−1−|R|)).

This retains the ordinary bad-pair count quotas. A quota with coefficients
h enters the repaired dual exactly like an ordinary quota: its multiplier
delta contributes delta*h to slot demand, delta*q to the subtraction,
and any excess demand is charged against the same slot capacity. No
integrality, strong duality, or independence assumption is required.

Pairs already sharing another lock are necessarily bad. They may be fixed
to their capacity in a stronger relaxation, but this diagnostic does not
need that extra equality. The slot domain continues to include them, even
though their opposing-side probability weight can be zero.

Acceptance requires exact independent replay of all weighted coefficients
and of actual injection probabilities. Floating point optimization only
proposes a certificate; a non-strict result says nothing about colorability.
