# Single finite combinatorial lemma with a direct coloring payoff

Please work on this self-contained obligation, with no broad file reading, hypergraph generation, agents or optimizer runs. It is a new approach, not another W table. Seek an analytic proof or counterexample; a clear precise obstruction is acceptable.

Let P,Q be arbitrary partitions of a 20-element set into five blocks of size four. Choose uniformly a 10-element red set; the rest is blue. Let B(P) mean that P has at least one entirely red block AND at least one entirely blue block.

Prove or refute:

    # {10-subsets R : B(P) and B(Q)} >= 400.

The application only needs a lower bound of 319. Intersections of P and Q are arbitrary, including repeated blocks. Equivalently their 5x5 intersection matrix is any nonnegative integer matrix with every row and column sum four. Do not assume entries<=1.

Known sharp-looking example: points (i,j) with i!=j in {0,...,4}, P rows, Q columns. If red row i and blue row j occur in a common bad coloring, the only possible red column is j and the only possible blue column is i. This forces seven red and seven blue points; the other six have choose(6,3)=20 choices. The ordered i,j give 20 disjoint possibilities, hence exactly400. A full tiny check of all184756 balanced subsets agrees. Identical partitions give16980 common bad subsets.

Single-partition bad count is exactly16980, by inclusion-exclusion:

    20 choose(12,6) -60 choose(8,2) +30 choose(4,2).

Why this is useful: In a 25-vertex,35-edge,pair-covering simple five-uniform H, select three degree-six vertices a,b,c sharing G={a,b,c,u,v}. Their other stars give three such partitions of the same20 outside points. Color u,v oppositely, the20 points balanced10/10, and extend the three low vertices independently whenever their partition does not have both monochromatic colors. Put D=d(u)+d(v), alpha=lambda_uv-1. The union-bound failure numerator over N=choose(20,10)=184756 is exactly

    161050 +2002(D-5alpha).

Subtracting one positive intersection of two partition conflicts is legitimate. If D-5alpha<=12, the excess over N is at most318. Thus the above lemma makes the coloring strict. In particular ANY edge with five degree-six vertices is handled (D12,alpha0). Simple low-point incidence already forces such an edge whenever there are at least20 degree-six vertices, so this lemma would close both entire r20 andr21 subfamilies without the earlier local design classification.

Please target this exact two-partition inequality, rather than simply restating the conditional coloring implication. Prefer a short extremal/compression argument reducing arbitrary intersection matrices to the orthogonal example, if valid; verify the direction rather than assuming smoothing is monotone. If the400 bound is false, a319 bound may still suffice; return an explicit integer matrix counterexample to any claimed bound. Finite local classification can later be used if needed, but do not run one yourself in this consultation. Give a concise mathematical result and the exact remaining gap.
