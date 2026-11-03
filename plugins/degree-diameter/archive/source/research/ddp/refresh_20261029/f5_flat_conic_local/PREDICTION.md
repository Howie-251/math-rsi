# Frozen single flat conic-color control

The old fixed-matrix 10^60 coefficient domain is excluded by its saved holonomy/odd-external-cycle proof. This task changes every linear map to I. It does not revisit those coefficient choices under the old maps.

Use only the literal30 controller. Each triangle's sorted vertices (a<b<c) give colors0,1,2 to edgesab,ac,bc. Each external pentagon is rotated to its least vertex and given the lexicographically smaller orientation, then its five edges receive colors[3,4,3,4,5]. This is one deterministic proper six-edge-coloring; no coloring/field/controller search is authorized.

For colors t=0,1,2,3,4 use v_t=(1,t,t²) over F5; color5 uses(0,0,1). A nondegenerate conic has every three distinct directions independent. Thus every triangle's three noise directions are independent and every controller vertex has four directions in general position. Triangle coefficients are {0,1,-1}; external coefficients are {1,-1}; reverse coefficients are negatives. All external coefficient gaps have the same shape±2. The new edge relation is y=x+t*v_e, so every closed word has identity holonomy and global translations act transitively in each fiber.

The discriminating prediction is that the single assignment's four-step same-fiber route unions cover all125 displacements on the old obstructing pentagon roots0,20,28,22,9, even though their external gaps are equal. A positive result would refute transfer of the old alternating-gap necessity to this changed mechanism, not prove globalD4. A negative result stops this one construction control and reports exact missing displacements; no coloring/gap/field retries.

Only reuse the saved closed-controller words at those five roots and evaluate their translation sums. No graph expansion, BFS, all-controller coverage scan, solver, or ordinary bad-pair objective. At most30 CPU seconds, one worker. The proper-color and conic-rank checks are local input validation, not new candidate enumeration.
