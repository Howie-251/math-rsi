# Concrete mathematical consultation: select a matching hitting nineteen original edges

Work read-only in `/Users/rfy_naiveai/Desktop/aris4math`. Use Gemini 4 Argon / high. Return a bounded mathematical argument; do not edit project files, launch agents, enumerate hypergraphs, or run new optimization. Be candid if the proposed sufficient route is false or not established. Do not repeat the project status.

The original unresolved goal is Property B for every finite simple five-uniform hypergraph with at most 35 edges. This consultation concerns only the actual branch:

* H has 24 vertices and 35 distinct five-element edges;
* every pair of vertices lies in at least one edge;
* every vertex has degree at least seven.

For a perfect matching P of the 24 vertices, let h(P) be the number of original edges containing at least one P-pair, and t(P) the number containing two. Write lambda_xy for actual pair codegree, w_xy=lambda_xy-1, W(P)=sum_{p in P} w_p. Exactly

    sum_{xy} w_xy = 74,
    deg_w(x)=4 d_H(x)-23 >=5, with deg_w(x)=1 mod 4,
    h(P)=12+W(P)-t(P).

Question: can one prove that some P has h(P)>=19, using the actual shared five-edges? This selection alone is not the entire coloring theorem: h>=20 suffices, while h=19 also needs two compatible leftover bad events. We are separately studying that equality obligation.

Read these short source files in this directory:

1. `PROOF.md`: exact pairing coloring gate; do not confuse actual edge intersection with shared matching components.
2. `INTEGER_EXCESS_MATCHING.md`: proves integer weighted graph W>=7, but provides a real H for which *every* maximum-W matching hits at most18. A19-hit matching exists there with W7,t0. Thus maximizing W then fixing t is a failed strategy.
3. `SELECTION_ATTEMPT.md`: choose P maximizing h, then minimizing t. Put u=35-h,s=h-t. Two-pair switching summed gain/loss gives 5u<=8s. Three-pair switches give precisely the same aggregate inequality. The secondary criterion with integral strict losses gives h18 => t<=5, not t=0. Double-hit edges cannot become unhit under complete two- or three-pair re-pairings. A *fractional* shared hypergraph satisfies all continuous degree/paircover constraints with optimal h18; it is not an integer-H counterexample. This identifies a real integrality obstacle.

Please pursue a genuinely new exact argument for W-t>=7, or produce a rigorous actual-H obstruction to this sufficient route. In particular consider original-edge private ownership, integer degree congruences, or a global combinatorial selection theorem. It is acceptable to return a specific proved intermediate with a clearly missing step; do not replace the target by W>=7, continuous switches, an unproved matching theorem, or a long list of speculative methods.

If deriving a general weighted-hypergraph matching theorem, state its assumptions and prove that the actual H satisfies them. No presumption that this claim is true. Avoid generic scoring/checklists and redundant defensive discussion (HERO); focus on the precise mathematical obstacle. Limit reading to the named files and their necessary local definitions, and give at most one main route plus a decisive diagnostic.
