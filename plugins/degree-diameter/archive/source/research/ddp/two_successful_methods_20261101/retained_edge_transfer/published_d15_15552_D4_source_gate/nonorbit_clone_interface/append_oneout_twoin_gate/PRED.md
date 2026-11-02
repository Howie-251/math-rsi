# Frozen-source full-N cloning: append / one-out-two-in

Fixed input is the accepted original15552/116316 simple source and the accepted864 ordered center labels. Every clone uses the original simple open neighbourhood, frozen before adding any clones. Binary domain: one clone per original center, not anI33 whole-plane search, not cloning the enlarged16416 graph.

For each old vertex w compute actual input degree d(w), incumbent load L864(w), and residual R(w)=16-d(w)-L864(w). Accepted old loads are0/1. A zero-residual slot therefore has exactly one responsible incumbent clone.

**Falsifiable prediction:** every currently unselected center has zero-residual neighbours belonging to at least two different incumbent clones. If supported this blocks both direct append and a one-clone removal. This is a local rigidity prediction, not a maximum864/full-nonorbit impossibility claim; the actual blocked-owner distribution can refute it.

First test append of any unselected center: every old neighbour must have R>=1. If no append, complete one-out-two-in: for each removed incumbent center u, permit new centers v,t outside the retained863, mutually distinct, including re-adding u. A center is individually feasible iff every zero-residual neighbour is owned by that removed clone. Centers blocked by at least two owners cannot be helped by one removal.

For two individually feasible centers, the exact simultaneous test is

    1_N(v)(w)+1_N(t)(w) <= R(w)+1_N(u)(w) for every oldw.

Only shared neighbours need the remaining comparison: their restored capacity must be at least2. Olddegree14 slots can have capacity2 and may be shared; full neighbourhoods are NOT required to be disjoint.

Return all15552 center blocking/owner profiles, each removal's complete feasible-center list, and actual pair stages until first hit or completeNO/budgetUNKNOWN. First hit saves865 ordered centers, source-based16417 complete edges and all frozen-N bindings, loads, degree histograms and literal input provenance. A one-out-two-in hit replaces one old clone: only the original15552 source edges are all preserved, not every edge of the old16416 graph.

The degree gate and literal production are not fresh diameter acceptance. Existing generic FullNeighborhoodClones distance interface is inherited; no sourceD4/old16416 BFS, field/rank, Lean or review is repeated. No new graph/parameter/Lean count here. First hit stops for root acceptance; completeNO closes only append and one-out-two-in around this incumbent, not2-out3-in, arbitrarypacking or maximum864.

Single process, same cumulative20CPU including inherited read2.0 and new preparation reserve0.5. Soft stopping leaves output time; actual parse, profiles, pairing and artifact production all enter processCPU. No compile, solver, hash, external query or automatic continuation.
