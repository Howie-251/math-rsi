# Rajiv5334 central transfer: a two-route witness excludes the fixed-base C3 expansion

The proposed8001-vertex centralC3 transfer is impossible for the fixed projected base. Exact enumeration of all22409 reduced words of length at most5 finds eight base endpoints with only two distinct mod3 signed generator-count vectors. The endpoint(phase1,fiber48), label175, has an even stronger witness: only two reduced base walks of length at most5 reach it at all. They are baC and CdB, each of length3. Thus no assignment of four centralC3 voltages can reach all three target-fiber vertices within5steps. The frozen obstruction prediction is supported. The81 assignments were not enumerated, as instructed after a capacity obstruction.

The whole computation used0.083968 CPU seconds on one worker. No known-source BFS, C2 verification, adjacency reproduction, new graph, other field, offset search, seed or follow-up variant was run. No record or actual diameter of a generated graph is claimed. The original5334 mechanism as a whole remains open to changes outside this exact projection/cover scope.

## Exact source decomposition and action

The saved known source uses right multiplication

    (i,x)(j,y) = (i+j mod21, x*25^j+y mod254),

with four positive generators(2,60),(3,122),(6,81),(8,169), and their inverses. Modulo127 the translations are[60,122,81,42]. Exact modular arithmetic checks25 has exact multiplicative order21 modulo127: its powers at3 and7 are4 and19, while power21 is1. Therefore the projected2667-point base is precisely C21 semidirect F127 with these fixed generators.

Since254=2*127 and25 is1 modulo2, the original source splits by CRT into this fixed base times a trivial centralC2. Its original central generator parities are[0,0,1,1], taken from60,122,81,169, not from the chosen modulo127 representatives. Expanding the central factor toC3 would keep the projected action and four projected translations fixed and choose any omega in C3^4. This is exactly81 assignments. Equivalently it would use fiber modulus381 and the four CRT lifts of the fixed F127 voltages. This task does not alter the quotient toC63 or assume that a different extension is the same group.

The ledger was read before computation. The known5334 baseline was already verified in the earlier package and is not re-counted as a new result. The old metacyclic_d5_transfer concerns the unrelated2810-point two-copyC5 source and fixed p311 canonical transfers. It does not exclude this C21/F127 central question. The UT3(F9) central-capacity family is also unrelated. SCOPE_READ.json preserves this separation.

## Exact route and signed-count computation

Use A=(2,60), B=(3,122), C=(6,81), D=(8,42) in the projected base, with lowercase denoting inverses. The inverse formula is(-u,-b*25^(-u)). All eight projected signed generators are distinct, so inverse-reduced generator words correspond exactly to nonbacktracking walks from the identity in this Cayley graph.

The enumeration covers the empty word and all lengths1..5 without an immediate inverse pair:

    1+8+56+392+2744+19208=22409.

At each projected endpoint it stores the distinct integer signed-count vectors and their coordinatewise mod3 reductions. Central coordinates are additive, so a word with count vector c reaches central coordinate omega dot c modulo3. An arbitrary walk can be inverse-reduced without changing its projected or central endpoint, so omitted backtracking walks supply no additional possibilities.

The minimum number of integer count vectors is2, and the minimum number of mod3 classes is2. Eight of the2667 base endpoints have fewer than three mod3 classes. MULTIPLICITY.json records the full count histograms, without using those counts as an ordinary unordered bad-pair metric.

## Concrete endpoint obstruction

For endpoint(1,48), the exhaustive reduced-word list is exactly

    baC: integer counts(-1,-1,1,0), mod3 counts(2,2,1,0),
    CdB: integer counts(0,1,1,-1), mod3 counts(0,1,1,2).

Their projected phases are-3-2+6=1 and6-8+3=1 modulo21, respectively. Both projected fiber coordinates are48. No reduced walk of lengths0..5 other than these two reaches that endpoint. All literal routes and vectors are saved in OBSTRUCTION.json.

For every central assignment omega=(omegaA,omegaB,omegaC,omegaD), the reachable center values above that endpoint are contained in

    {-omegaA-omegaB+omegaC, omegaB+omegaC-omegaD}.

This set has at most two elements, fewer than three. The two values can coincide, making coverage even smaller. Therefore all81 trivial centralC3 assignments fail, without testing them individually. On the originalC2 parity vector[0,0,1,1] these two routes give1 and0, explaining why the known double cover can just separate this fiber. This is a local interpretation of the saved witness, not a revalidation of the originalC2 graph.

## Direct corollary for ordinary covers of this frozen base

The fact here is two base walks, not merely two abelian count vectors. Fix any lift of the identity in an ordinary k-fold graph cover of this exact2667-point base, with local edge bijection. Every walk of length at most5 to a vertex over175 projects to a base walk of that length. A projected immediate backtrack lifts to an immediate return to the same vertex, so removing it preserves the lift endpoint. The projected walk therefore reduces to one of the two saved nonbacktracking walks. Each has exactly one lift from the fixed lifted root.

Consequently at most two vertices above175 can be within5steps. For k>2 some fiber vertex is farther than5 or disconnected. This excludes all ordinary k-fold covers with k>2 of this frozen base, including non-Galois or per-edge permutation-voltage covers as long as the projection remains locally bijective. No extra calculation is needed. FIXED_BASE_COVER_COROLLARY.json gives the frozen labels and hypotheses.

This concrete corollary does not exclude branched or added-edge constructions, a different base graph, changed projected generators or translations, or all mechanisms derived from Rajiv5334. To repair this particular bottleneck one must change the available projected short routes; central voltages alone only relabel the endpoints of the two existing routes. No such repair variant was attempted. The task is terminal at the exact obstruction.
