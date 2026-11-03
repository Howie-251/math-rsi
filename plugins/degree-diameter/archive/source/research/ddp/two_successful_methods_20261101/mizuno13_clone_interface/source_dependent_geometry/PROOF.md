# Source-dependent affine full27 blocks: regular315 gate

The domain is one complete27-point affine W-transverse block H_R+c per chosen source among the315 nonself/noP fibers with affine M equal to the matching ordinary-port matrix. W=span(e0,e1), H_R={(Rt,t):t in F3^3}, R a2-by3 matrix. All729 R are covered, grouped into40 distinct systems of four normal-containment equations and one M-separation equation. The nine phases do not alter either condition. No solver, source BFS, complete graph generation, or global packing model was used.

## The suggested g<=3 obstruction is false

All315 M target translations d lie outside target W. At every one of364 targets, the four incoming ordinary noise directions are exactly the four distinct projective lines of W. Exhaustive finite algebra gives gmax4 for175 sources and gmax3 for140. Here g counts ordinary81-point output hyperplanes whose directions contain target W, subject to exact local M separation. The complete type/source bindings are in PREPARED_GEOMETRY.json and RESULT.json.

Source0 has the concrete slope R=[[2,2,1],[2,0,0]], with H basis (2,2,1,0,0),(2,0,0,1,0),(1,0,0,0,1). Its four output normals are (0,0,1,0,0), (0,0,1,1,0), (0,0,1,2,2), (0,0,1,2,0). Each kills W. A direct local readout gives324 ordinary neighbors,27 matching neighbors, zero overlap, and351 distinct old neighbors. This is a locally valid g4 block, refuting both g<=3 and g<=2. EXPLICIT_G4_COUNTEREXAMPLE.json contains the27 center labels and all outputs; it does not claim a global packing.

## Combining normal exclusivity with matching capacity

If two selected ordinary output hyperplanes enter the same target, disjointness requires parallel hyperplanes: distinct normals intersect in27 points. A shared normal kills both incoming noise directions, which are distinct lines of W, so the normal kills all W. Consequently every output not containing W is the sole ordinary provider at its target. Let B count these distinct exclusive target fibers. For selected source a, B receives4-g(a), hence B>=sum_a(4-gmax(a)).

Let s_b count ordinary block providers at target b and x_mate(b) indicate its matching provider. Each ordinary provider has81 points, each M provider27, and the target has243 old vertices, each with spare capacity1. Thus3*s_b+x_mate(b)<=9. With integral s_b and binary x, this implies s_b+x_mate(b)<=3. Summing rows yields5*T<=1092. At each of the B exclusive targets, s_b=1, so s_b+x_mate(b)<=2 and that row loses at least1. Therefore5*T+B<=1092, and

    sum_selected (9-gmax(a)) <=1092.

There are175 sources of cost5 and140 of cost6. The cheapest211 choices cost175*5+36*6=1091, while the cheapest212 cost1097. Therefore T<=211, at most5697 clones, and final order at most94149. This is37 below saved14D5=94186, and less than the213 full blocks needed for a strict improvement.

## Scope and next finite question

This closes only the315-source affine full27-block domain. It does not exclude the49 exceptional fibers, nonlinear W-transversals, partial blocks, mixed block sizes, other clone rules, or other sources. The geometry-only bound240 remains a true but weaker necessary bound. The old prediction that M legality forces g<=3 remains recorded as disproved. For213 full blocks, the combined cost gate requires at least186 g4 sources, hence at least11 exceptional g4-capable sources beyond the175 regular ones. Extending the row argument to self ports requires checking loop-deletion geometry first.

Preparation and complete type algebra used0.141003423 CPU seconds; one explicit local binding used0.021695149. The original uniform-H terminal and main project state were left unchanged.
