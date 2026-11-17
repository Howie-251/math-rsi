# Twenty-two-point safe outer-arm extraction

Order L1..L4 < U1..U6 < r < s < V1..V6 < R1..R4, with physical labels
L=1..4, U=5..10, r=11, s=12, V=13..18, R=19..22.
Retain all 14-point predicates, with source/terminal row locks only for R6
wholly within the original 14-point domain 5..18. New L/R points can be
other matched rows; they are never excluded as endpoints merely because
they were absent from the 14-point projection.

Throughout the full 22-point domain: packet, no R7/B6, no weak7, no R5 from
U to V, no R6 ending in U or starting in V, r cannot start B5, s cannot end
B5, no B4(r,s), and the true terminal/source and B5 first/last pair fans.
Within the 12-point U union V only: each pool no R5/B5, no crossing R5,
no mixed B4, and not both pools containing R4.

Freeze true R5(L1,L2,L3,L4,U1) and R5(V6,R1,R2,R3,R4), coming from the
incoming red-six supply of U1 and outgoing red-six supply of V6. These
introduce no claimed R6 endpoints at any newly retained L/R point.

R4/R5/R6 endpoint flags are one-way witnesses used only to prohibit weak7.
Every admissible physical coloring extends by assigning each flag its true
path-existence value. No flag is used as an exact count or physical witness.
SAT will be independently checked by enumerating every physical subset.
