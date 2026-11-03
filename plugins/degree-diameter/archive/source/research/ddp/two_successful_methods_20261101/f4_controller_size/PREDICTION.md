# One justified controller-size test, not a template sweep

2026-11-01. Current accepted B graph uses the literal Bhakar C60 controller and five conic directions over F4, with a full five-plane pencil on every dart and a rank-three nonbacktracking three-word for every nonadjacent/equal ordered controller pair.

## A certificate capacity bound before the experiment

Suppose a simple five-regular controller has c vertices and uses the same five-conic F4 frame, exact reverse charts, a full backtrack pencil at every edge, and the same rank-route certificate. On the quotient at a central dart, the four incoming and four outgoing projected directions are four-element subsets of PG(1,4), which has five points. Full pencil coverage forces their union to have five points, hence intersection size three. Of the sixteen central turns, exactly three have rank below three and thirteen have rank three. Thus all directed three-words provide exactly 5c*13=65c rank-three words.

There are c(c-5) required ordered nonadjacent/equal endpoints. Each needs at least one word. For each equal endpoint, a rank-three word and its reverse are different nonbacktracking triangle words, both rank three. This spends at least one further word per source beyond the endpoint count. Therefore c(c-4)<=65c, so c<=69; the parity of a five-regular graph makes c even, giving c<=68.

This bounds the specific full-pencil/rank-route certificate. It does not rule out general F4 fiber graphs with collective lower-rank route coverage, a changed frame, or another graph construction.

## One controlled continuation of the actual controller

The actual C60 has 3 base states and a Z20 deck. Keep a's permutation [0,2,1] and voltages [6,3,12], b's three-cycle with zero voltages, and the matching between (0,g) and (1,g+1). Extend only the even deck size to22 and change the third-state matching shift from10 to11, so it remains a true matching. C66 is the only larger multiple-of-six order allowed by the preceding certificate bound. No other modulus, voltage or random seed is queued.

Prediction to test: this direct continuation may preserve the necessary controller diameter-three coverage. Check literal C20 binding to the saved controller first, then all <=3 controller words for the three deck-translation root classes of C66. If one control target is missing, no fiber chart can repair it; stop this specific continuation before SAT or graph generation. If the necessary gate passes, save the controller for one separately budgeted chart test. A controller PASS alone is not a graph.

Budget: one deterministic controller experiment, at most10CPU seconds; no full fiber graph or source-distance recheck. Return a concrete missing target and its route-residue class on failure.

## Revised rule after the actual counterexample

The one fixed continuation failed: root0 misses target2, and the three translation root classes reach only53,58,55 of66 controller states. This is a missing controller route, not a chart-rank collision. No chart SAT was run.

To distinguish a fixed-voltage accident from a structural obstruction, run one complete finite gate over the same C3 x Z22 controller organization. Release the four actual voltage variables a=(alpha,beta,gamma) and the 0-to1 matching offset tau, keep b the zero-voltage three-cycle and the2-layer matching shift11. A simple five-regular inverse-port controller requires alpha in1..21 excluding11; beta,gamma,tau nonzero; beta+gamma nonzero mod22. This gives20*21*20*21=176400 literal assignments (not normalized or claimed nonisomorphic).

Prediction: if the residue gaps are only a bad original assignment, at least one such controller will have all three root classes covered in at most3 steps. If none does, the complete stated voltage domain is closed before any fiber matrix is considered. If any pass, additionally check the intended full-rank-NB3 certificate has at least one NB3 word for every required nonadjacent/equal pair. Save every passing voltage tuple and return its count; do not automatically launch a chart search.

One C++ exact enumeration, one worker, at most30CPU seconds. No full fiber graph, random seeds, solver or old-controller recheck. This changes connection voltages rather than repeating the failed fixed assignment; the new finite domain includes it once as part of the complete enumeration, with that overlap explicitly acknowledged.
