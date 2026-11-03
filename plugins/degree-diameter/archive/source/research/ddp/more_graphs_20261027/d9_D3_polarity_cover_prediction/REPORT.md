# Actual585 polarity source supports the port/Steiner prediction

2026-10-27. The frozen prediction is supported in every tested component. This is a structural certificate for the fixed published source, not a new graph construction.

## Source binding and inherited facts

The official diameter-three description identifies Q′8 as the585-vertex quotient of a generalized quadrangle incidence graph by a polarity, citing Delorme1985. Its primary implicit adjacency list is

https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD3/n585d9k3.txt

The project had already saved this exact source and its adjacency partition in `research/ddp/polarity585_replication/`. This task reused that local literal and saved a copy here, without downloading or rerunning all-source diameter verification. Existing checked facts are n585, m2600,65 vertices of degree8 and520 of degree9; the former are independent, and each latter has exactly one former neighbor. Source diameter3 is inherited from the published source.

The relevant prior Wiki entries already cover complete twin replication, the need for65 pins for one new root, and the small-helper range. Those experiments were not repeated. The new question was the complete triple structure of the port-R2 incidence sets.

## New targeted calculation

Let P be the65 degree8 ports and B the520 other vertices. Direct neighbor-set expansion computed only R2(p), for each p∈P. Every R2(p) meets P only in{p}. Combined with the inherited sourceD3, this establishes that all distinct ports are at distance3. The closed one-balls of P cover each of585 vertices exactly once, so P is a perfect1code.

For every t∈B, define S(t)={p∈P:t∈R2(p)}. All520 sets have size9 and are distinct. Counting their triples gives the full universe of C(65,3)=43680 triples, each with multiplicity exactly1. Thus the actual incidence structure is Steiner3-(65,9,1), without assuming this geometry from its name. The corresponding design parameters are point multiplicity72 and pair multiplicity9; these follow from the established triple design.

`BLOCKS.json` contains all520 literal sets, and `PORT_R2.json` contains all65 expanded two-balls. `RESULT.json` stores the cardinality and multiplicity checks and reports no bad triple. The computation used0.050057112 CPU seconds. No helper sets, solver, candidate graph, random seed, or full-source BFS were used.

## Consequence and scope

The parent-provided `CONDITIONAL_COUNTING_LEMMA.md` can now use these actual source premises, rather than an unverified analogy to a polarity graph. The paper argument and its final scope are maintained by the parent and its assigned theory checker; this note supplies the finite source data only. It neither labels a failed search as a nonexistence proof nor claims a new lower bound. Arbitrary graphs at the same parameter are outside this fixed-source structural certificate. This data task is complete; no further source or helper computation is pending.
