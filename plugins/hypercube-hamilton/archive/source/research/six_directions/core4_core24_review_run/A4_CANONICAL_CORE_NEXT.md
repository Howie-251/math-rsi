# Remaining canonical A4 core and next transfer obligation

Date: 2026-11-01. R1A in `A4_SINGLE_GEOMETRY_REDUCTION.md` and its independent
review reduce the unresolved A4 geometry to holes $a=0,v=1,b=14,t=22$,
with forbidden $v=1$. Matching edges on the other 28 vertices remain
arbitrary. This file records the next route, not a completed proof.

## Opposite-hole avoided-circle transfer

Split on coordinate 0. Side A (odd integer labels) contains only the hole
$v=1$; side B contains $a,b,t$. The crossing count $c$ is positive odd.
The two candidate short bridges from $b,t$ go to $15,23$ in A. These A
vertices are covered. If $c=1$, at least one candidate is internally covered;
if $c\ge3$, either an internal or a crossing candidate can be used.

For a chosen bridge $tw$ (relabel $b,t$ if needed), pair B ports together
with $t$ into D. Then $F_B\cup D$ is near-perfect with opposite holes $a,b$,
so NC_4 gives a full B circle. Delete D, attach real crossing edges and tw.

If $w$ is internally covered in A, compress paths into R, let
$k=F_A(w),d=R(w)$, and form

$$L=(F_A\setminus\{wk\})\cup(R\setminus\{wd\})\cup\{kd\}.$$

If $w$ is a crossing port, require $c\ge3$ and choose D to contain $tx$,
where $x=F(w)$ is its B partner. Then the two relevant B segments are
different, join at w, and compress to R on $X_A\setminus\{w\}$; set
$L=F_A\cup R$.

In both cases L is a matching with precisely two opposite-parity holes
$v,w$ in A, at distance three. A 14-cycle on $A\setminus\{v,w\}$ extending
L would expand to the desired 31-cycle for F, restoring w and all of B.
What is NOT established is that the choices of bridge, D and B circle
always produce an extendable L.

## Q4 caution: excluding half-layers alone is insufficient

`q4_opposite_avoided_probe.cpp` diagnoses all 135135 matchings for each
normalized opposite-hole pair $0,1$ and $0,7$. It reports 51 and 53 failures
respectively, including 36 and 8 failures without half-layers. This is a
diagnostic classification, not yet a fully independently certified complete
positive/negative exception table.

The 8 reported non-half-layer examples for distance three, plus 20 stored
examples for distance one, have separately been verified by
`verify_q4_opposite_avoided_obstructions.py`. It enumerates every short
perfect matching on the 14 allowed vertices: every extending circle would
be the union of the required matching and one of these completions. All
such unions in each listed example have at least two components. The
checker also directly verifies that none contains a half-layer. Thus these
28 individual obstructions are independently certified, although completeness
of the full exception table is not yet independently certified.

They are NOT counterexamples to A4 or P6: the four-dimensional subproblem
asks to avoid TWO opposite-parity holes simultaneously. Do not extend the
five-dimensional no-half-layer theorem to Q4 without accounting for these
exceptions.

## Concrete next actions

1. Export positive certificates for every successful distance-three Q4
   avoided-circle instance and all 53 negative instances; independently
   certify a complete finite exception table.
2. Prove a choice/repair argument for the transfer above that avoids every
   exceptional output L, or derive a direct construction for the canonical
   family. The single-crossing case is a particularly small interface:
   the compressed matching is $F_A-wk+kd$ with the unique A port d, independent
   of the particular B circle. Its two candidate bridge endpoints can be
   analyzed directly against the exception table.
3. Only a proof for ALL canonical matchings would close A4. Then the existing
   full six-hole reduction applies; the remaining 8--18-hole P6 levels
   still require separate closure.
