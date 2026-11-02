# Prediction before checking target48: capacity837 fails real line complementarity

2026-11-01. The exact controller-capacity LP gives837 total centers, with27 centers each in layers17,35,74 feeding target48. This is only a necessary capacity model. Predict that the837 weight vector cannot be realized even by arbitrary center subsets, because these three incoming noise directions are linearly independent over F9.

## Geometry prediction and falsification criterion

Inside the729-vertex target fiber, each selected source center contributes a complete9-point affine line in its incoming noise direction. Each of the three families must be internally disjoint and the three families pairwise disjoint. If the three directions form a basis, identify them with the coordinate axes. Let the three line counts be A,B,C, all positive. Then

    A+B+C <= q^2-q+1,
    A*B*C <= floor(q^2/4)^3.

For q9 this gives total<=73 and product<=8000. The proposed A=B=C=27 has total81 and product19683, violating both. This is not just an obstruction to F3 trace hyperplanes: it applies to arbitrary unions of complete lines.

For coordinate-x lines R subset Y×Z, coordinate-y lines G subset X×Z, coordinate-z lines Bset subset X×Y, disjointness forces the relevant projection supports to be disjoint:
Z_R cap Z_G empty, Y_R cap Y_Bset empty, X_G cap X_Bset empty.
Write a=|X_G|, b=|Y_R|, c=|Z_R|, then each lies in1..q-1 and

    A<=bc, B<=a(q-c), C<=(q-a)(q-b).

Their product is at most a(q-a)b(q-b)c(q-c)<=floor(q²/4)^3.
Their sum is at most q²-[b(q-a-c)+ac]. If a+c<=q, bracket >=(a-1)(c-1)+q-1. If a+c>=q, bracket >=(q-1-a)(q-1-c)+q-1. Thus sum<=q²-q+1.
Sharp sum example counts1,q-1,(q-1)^2. Sharp balanced q9 example a5,b4,c5 gives20,20,20.

## Targeted actual check

Check only actual three incoming darts of target48 from17,35,74, their noise directions, and their determinant using existing GF9 tables. Do not repeat all old field/rank certificates or old source BFS. One <=5CPU table calculation can enumerate a,b,c in1..8 to check the two sharp bounds and the20/20/20 direct line witness; it is a check of the prediction, not a substitute for the projection proof.

If supported, reject the837 weight vector and change the generated weights/point sets to respect actual three-way line complementarity. Do not mark the whole fixed-W pool infeasible: the separate single bounded actual-pin packing pilot asks only for>=811 and allows different weights. No full graph is produced or counted by this note.

