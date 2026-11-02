# Exact K6 dominating-neighborhood extension criterion

Let H be the accepted972-vertex source, with diameter at most3,864 vertices of degree13 and108 free vertices of degree12. Its induced free graph F has18 components P2,6 components P3,9 components P4 and3 components P6, as bound by the producer's actual source data. Keep the entire induced source graph unchanged.

Add six fresh vertices h0,...,h5 as a clique. Choose disjoint old-pin sets A0,...,A5 and put S=their union. Each helper is adjacent to precisely its own Ai among old vertices.

For every helper i and old target t,

    d_new(hi,t)=min(1+d_H(Ai,t),2+d_H(S\Ai,t)).

Every route on the right exists. Conversely, choose a shortest simple path. If it visits another helper hj after an old-vertex prefix, replace the whole prefix by the clique edge hi-hj. If it uses multiple helper edges before entering H, replace them by the direct clique edge. Therefore a shortest path either enters H through Ai directly, or uses one clique edge and enters through some other Aj. It cannot later revisit a helper without the same shortening. These are exactly the two terms.

Thus helper i covers every old target within3 exactly when

    R2_H(Ai) union R1_H(S\Ai)=V(H).

This is a complete condition for helper-old pairs. Old-old distances are inherited from unchanged H, and all helper-helper distances equal1. Consequently these six equations and the degree constraints suffice for global diameter at most3.

Now require S to dominate F using closed neighborhoods in F. Each free target t then equals or is adjacent in H to some selected pin p. If p is in Ai, helper i reaches t in at most2; otherwise it reaches t through the helper owning p in at most3. Hence all108 free targets are automatically covered by every helper. Only the864 originally full targets need explicit coverage clauses. More generally any target in R1_H(S) is automatic for all helpers; a remaining target needs Ai to meet its R2 coverers for each of the six colors.

A path Pn has domination number ceil(n/3): one selected vertex covers at most3 path vertices, and every-third-center choices attain the bound. Hence

    gamma(F)=18*1+6*1+9*2+3*2=48.

The helper clique consumes5 degrees, leaving at most8 spokes per helper,48 total. Within this F-dominating construction every valid S therefore has exactly48 distinct pins and every Ai has size8. All old pins have one free slot, so disjointness is mandatory. Each selected old pin and every helper ends with degree13; the60 unselected free source vertices remain degree12. The resulting graph has978 vertices and6264+48+15=6327 edges.

Every P3 component has its center forced in a minimum dominating set. Requiring its six centers to belong to six distinct helper colors is an additional construction restriction, not a consequence of domination alone. Within that restricted class the helper labels may be permuted to assign those centers colors0,...,5. No negative result under that restriction excludes every possible K6 extension.

This proof assumes the selected source component model and pin lists are actually bound to H. It does not claim that gamma(F)=48 or scalar capacity alone makes the six full-target coverage systems feasible. No solver, graph generation, source BFS or candidate verification was performed for this file. A positive producer graph is to receive one independent literal degree/retained-edge and full978-source diameter check; otherwise no candidate BFS is run.

Producer disposition: both the LP and the single MIP returned status2, infeasible, in total2.079970 CPU seconds. No candidate was produced, so no independent graph or BFS check followed. These are numerical solver results for the fixed minimum-dominating-set and distinct-P3-center-color model; this proof supplies its exact path interpretation, not an independently certified infeasibility argument or an exclusion of arbitrary K6 helper rules.
