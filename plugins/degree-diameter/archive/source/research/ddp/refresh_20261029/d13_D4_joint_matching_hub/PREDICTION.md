# Frozen complete central-matching selector on source6804

Use only the literal source6804.edges and its already bound construction. Its 3,402 central plain edges form a perfect matching. Select at most six of these edges, with no fixed fiber coordinate or subgroup orbit; remove them and join all their endpoints T to one new hub w. Old degrees stay 13, the hub has degree at most 12, and the candidate order is 6,805. This differs from the two closed hand-fixed matching domains. A targeted query of this source's records found no existing complete 3,402-selector model.

Frozen prediction: some selection simultaneously gives max d_G(x,T)<=3 and preserves all old-old distances at most 4. The prediction is unproved.

Initial exact necessary model: (i) one R3-cover clause for every one of the 6,804 old targets, selecting a central edge with at least one endpoint in its original radius-three ball; (ii) at most six selected edges; (iii) for each (u,t) with original distance four and geodesic first-step support exactly the central partner of u, selection of u's central edge implies a selected endpoint in B2(t). Shared C2(t) variables are encoded equivalent to their complete selector ORs. Such a C2(t) must not contain u's own edge. The 81 fiber representatives and their BFS first-step data are expanded through every left-controller translation, covering all 6,804 vertices.

Safe symmetry: at least one selected matching edge has an endpoint in controller cell identity. This is an OR of all 81 such edge selectors, justified by left-controller multiplication; no particular fiber coordinate is fixed.

One bounded CEGIS batch: at most 90 aggregate CPU seconds including preparation, solver aggregate at most 60 seconds, at most eight solver rounds. Each SAT selection is checked on its literal changed graph independently of the clause-generation path. A genuine diameter-four hit is immediately saved and reported. A bad old pair must have original distance four. Its next cut is the OR of all original length-four geodesics avoiding deleted edges, together with the exact hub-repair terms C0(x)C2(y), C1(x)C1(y), C2(x)C0(y). No sampled path list, nogood, random seed, or score optimization is allowed.

The initial model may suffice for a terminal UNKNOWN or raw UNSAT. Neither is promoted to certified family nonexistence. An UNKNOWN, exhausted budget, eighth completed round, or verified hit ends this batch. No automatic timer extension, ninth round, additional deletion type, or source change follows.
