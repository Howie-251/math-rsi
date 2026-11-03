# Coordinate handoff for64 eligible longside lines

NONSTABLE_PLANES64.json is complete:64 input rational singular lines, exactly6 cached nonstable maximal singular planes per line,384 distinct planes total. The existing21840-plane cache was filtered rather than regenerated. The input remains bound to the accepted42402/245937 degree12 source; no degree or coverage filtering was repeated here.

Each record includes the line’s two RREF rows e0,e1, the global cached plane_index, its local index0..5, the plane RREF basis, and complement_w chosen as the first plane-basis row outside the line span. It also contains81 raw quadric point IDs, with index u+9*v corresponding to normalized(w+u*e0+v*e1). These are exactly the affine points off the input line. The field encoding and addition/multiplication tables are supplied at the top level.

For every plane, algebraic checks confirm rank3, Q=0 on the basis and zero pairwise polar products, so the whole plane is totally singular. Both it and its Frobenius conjugate contain the input rational line, and their combined vector rank is4. Their intersection therefore has vector dimension2 and is exactly that line. All81 off-line points are distinct, belong to the cached quadric, and avoid the line’s10 points. Frobenius partner plane indices are also recorded, without using them to skip producer scope.

The script is prepare_planes64.py; its pre-run question and result are PLANES64_PREDICTION.json and PLANES64_RESULT.json. The measured process CPU checkpoint was0.295276962 seconds, under the15-CPU allocation and14-CPU worker hard limit. This task generated no projectivities, degree pool, R4 ball, graph, BFS or solver call. Its work is part of the parent’s single60-CPU construction batch, not an independent method.
