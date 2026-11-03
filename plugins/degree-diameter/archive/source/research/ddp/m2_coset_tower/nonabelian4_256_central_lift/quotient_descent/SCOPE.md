# Projection-bound descent: executed scope

This is one finite construction profile on the same Q64 four-orbit K4 base with multiplicities `[3,3,2,2,3,3]`, targeting a simple 256-vertex degree-8 diameter-3 lift. It changes the search objective to a projection lower bound. It is not an exhaustive search of the projection family or a continuation of the completed one/two-coordinate source balls.

The short-walk and central-affine routines were copied from `../search.cpp` into this directory. The parent implementation was not edited. A projection assigns each of the 13 free base edges a D32 element, encoded `a+16*p`; tree edges `[0,3,6]` stay identity. Full Q64 elements are encoded `x+32*p`, and the canonical section is `a+32*p`.

For each of four orbit roots, all freely reduced base walks of length at most three generate affine central forms `(mask,constant)` in their quotient target slots. Exact duplicate forms are removed; if two duplicates have different path lengths, the shortest length is retained for radius-three calibration. Let `Nempty` count empty slots and `Nsingleton` count slots with exactly one distinct affine form. The objective is

`L = 2*Nempty + Nsingleton`.

Each empty slot loses both full vertices for every center assignment, and each singleton-form slot loses one. Thus L is a lower bound on the sum of four root deficits. It is not an actual graph score. Candidate ordering is lexicographic `(L,Nempty,M)` with M used only at L=0; M is the exact minimum actual deficit over legal central lifts. No phase-capacity filter is imposed.

Projection legality is existence of a legal central assignment. Parallel base edges with the same quotient voltage impose XOR inequality on their central bits. Up to two equal projected voltages are allowed; three in the same parallel class are impossible. The C++ scorer checks the GF2 system. For the start sampler, whose parallel classes are disjoint, the equivalent maximum multiplicity of two is used.

There are exactly 16 starts:

1. The projection of the old independently verified graph with 832 bad unordered pairs.
2. The observed best-L projection from completed two-coordinate cursor 52852: change old-source edge 8 to quotient code 31 and edge 13 to code 29.
3. Fourteen fresh distinct legal projections from Python `random.Random(20261027080)`, each proposed by independent uniform choices of the 13 D32 voltages and accepted only when legal and not previously selected. This is conditional-uniform sampling without replacement. Tree coordinates remain zero.

The second start replaced one fresh start before this profile was launched, following explicit parent authorization. It did not increase the number of starts. Actual starts and sampler draw counts are saved in `starts.json` and `starts.txt`.

Each start has nine segments, each with at most 30 strict descent moves. A move is selected only after the full 13*31=403 one-coordinate neighborhood has been inspected. Illegal projections are counted and skipped; among the legal neighbors only a strict lexicographic improvement is accepted. Ties do not cause moves. A segment ends at a full-neighborhood local minimum or the move limit. Between segments, two distinct free coordinates are both changed; proposals are repeated only until the final projection has a nonempty legality system. Kicks use a separate deterministic `std::mt19937_64` stream seeded 20261027080. There is no added start or random restart.

Only L=0 projections enter exact center optimization. The copied sparse bad-affine-subspace method scores all legal assignments among the 8,192 central masks. A zero actual deficit saves the explicit graph and stops immediately. Otherwise the best actual center lift would be saved, with its evaluated-scope selection clearly stated. If no L=0 projection occurs, only a projection/lower-bound artifact is saved. Repeated L=0 projections can reuse their exact cached result.

The first formal source score is calibrated against the existing independent distance matrix of the old graph: all four representative roots times 256 radius-three distances are compared, with old distances greater than three truncated to missing. This reuses saved evidence and introduces no BFS. The old source's 8,192 central masks are not rescored. A budget stop saves the current start, segment, step, next neighbor cursor, current state, and best neighbor so far; it does not commit a partially inspected neighborhood or restart the process.

The authorized budget is one worker and 180 CPU seconds including preparation and compilation. The executed profile finished all 16 starts inside that limit; `REPORT.md` and `terminal.json` record the actual outcome.
