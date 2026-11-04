# Next route for T15 core 0: three-avoided Q4 circles

Date: 2026-11-01. Research note, not an audited closure theorem.
Full core 0, T15 and P6 remain open.

## Geometry and a sufficient double-bridge step

Core 0 has minority hole $0$, omitted holes $1,2$, and included holes
$7,11,13$. Cut coordinate zero. In common Q4 labels obtained by deleting
that bit, the one-face $A$ has holes $0,3,5,6$ (omit $0$), and the
zero-face $B$ has holes $0,1$ (omit $1$).

For zero original crossings, choose distinct $s,t\in\{3,5,6\}$ whose
corresponding B vertices are not paired together by $F_B$. Add the
artificial edge $st$ to $F_A$. The resulting A matching has two even
holes, one $0$, so Q4 N14 gives a 15-cycle omitting $0$.
Delete $st$ and attach the two short bridges to $s_B,t_B$. If
$k_s=F_B(s)$ and $k_t=F_B(t)$, replace
$sk_s,tk_t$ by the auxiliary edge $k_sk_t$ in $F_B$.
The resulting B matching has holes $0,1,s,t$.

A 13-cycle omitting $1,s,t$ and containing that matching expands to
a 30-cycle on the desired Q5 support: expand $k_sk_t$ through $s_B$,
the entire A path, and $t_B$. All original edges are restored; all new
surviving edges are short. This is a sufficient construction, not a proof
that a successful pair always exists. Positive-crossing versions need
additional forest/port analysis and are not established here.

## The local three-avoid statement is not universally true

For the two marked families, $Q_4$ has holes $0,s,t,1$, and one asks for
a 13-cycle omitting $s,t,1$, retaining every edge of an arbitrary
complete-graph matching on the other twelve vertices.

The producer `q4_three_avoided_probe.cpp` supplies complete tables.
`verify_q4_three_avoided.py` independently checks all $10395=11!!$
matchings per family and every positive cycle. For each claimed negative,
it enumerates **all** short new-degree completions: choose two short
neighbors of the only retained free vertex $0$, then pair the remaining
ten vertices by short edges outside the required matching. Every such
union has at least two components. Results:

| omitted vertices | positive | impossible | total negative completions checked |
|---|---:|---:|---:|
|$3,5,1$|10362|33|84|
|$3,6,1$|10325|70|220|

The third pair $5,6$ is obtained from $3,6$ by swapping coordinates one
and two, which fixes $0,1$. Data and exact negative matchings are in
`q4_three_avoided_verification.json`. These negative local statements are
not counterexamples to T15 or P6. They prevent silently assuming that a
three-avoided circle always exists.

## Complete diagnostic for the zero-crossing B matching

`t15_core0_three_avoid_choice.py/.json` checks all $135135=13!!$ B
matchings with holes $0,1$, trying all three pairs $\{s,t\}$ above.
A pair is rejected if it is already an edge of $F_B$, or if its suppressed
matching belongs to the exact negative table. The number of usable pairs
has histogram

$$\{0:18,\ 1:310,\ 2:32587,\ 3:102220\}.$$

Thus this simple double-bridge choice stalls on $18$ B matchings even at
zero crossings. This is a complete producer diagnostic, not yet a fresh
independently audited theorem about core 0. The $18$ matchings are saved
in full. They might be bypassed by another coordinate cut, a different
transfer, or a richer joint construction. Do not discard them as
unrealizable: B matchings here are allowed to contain long edges.

## Next obligations

1. Audit the exact Q4 three-avoid negative classification if it becomes a
   proof input; positive certificates and independent completion checks
   are already present.
2. Analyze the $18$ zero-crossing B obstructions and a general
   positive-crossing port transfer before claiming core 0 closure.
3. Check whether the new transfer also covers other remaining core IDs.
   A success only for core 0 does not establish the remaining thirteen
   cores in the current sufficient cover, or the seven Q6 EP0 orbits.
