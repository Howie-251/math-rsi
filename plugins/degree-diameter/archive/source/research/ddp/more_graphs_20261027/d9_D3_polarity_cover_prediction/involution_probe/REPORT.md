# A verified single involution from the actual derived affine plane

2026-10-27. The requested nontrivial order-two graph automorphism has been constructed and checked. It is reusable source structure, not a new graph or graph record.

## Construction without an automorphism-group search

An original GF8 coordinate recipe was not available locally. Instead, the already verified literal Steiner3-(65,9,1) data gives an intrinsic construction. Fix the port p=0. The72 blocks containing p, with p removed, are the lines of a64-point affine plane of order8. The eight blocks indexed by the actual graph neighbors N(p)={1,...,8} give a special parallelclass.

Take O=73 in its special line, B=86 on that line, and C=138 off the line. The special line is{73,86,90,101,108,120,127,129}. For X off that line, define sigma(X) by intersecting the line through X parallel to OB with the line through B parallel to OX. This gives sigma(C)=158. For X on OB, use the same parallelogram prescription with origin C and image158, avoiding the degenerate intersection. Set sigma(p)=p.

This defines one specific candidate on the65 ports. No direction, displacement, matrix, or automorphism-group enumeration was performed. Every transformed nine-port block was found among the520 existing distinct blocks, so the port action lifts uniquely to the other520 graph vertices. The complete permutation is in `sigma.json`.

## Actual checks

The lifted map is a bijection of all585 vertices, squares to the identity, and is nontrivial (73 maps to86). Its only fixed port is0; the other64 ports give32 transpositions. Its full graph fixed set is exactly{0,1,2,3,4,5,6,7,8}. All2600 original edges map to edges, with zero failures. Since the map is bijective on a finite graph, this is an actual graph automorphism. These checks do not assume a Suzuki group identification or an unverified coordinate labeling.

The one-candidate calculation used0.002791158 CPU seconds. There was no BFS, dependency installation, graph construction, or large group computation.

## Identification of the nine parallelclasses

A further explicitly requested read-only check used the same blocks and adjacency. The nine parallelclasses are exactly:

- the eight block indices N(p);
- for each a in N(p), the eight block indices N(a) minus{p}.

Each class consists of eight pairwise disjoint eight-point derived lines. Together they partition all72 derived lines. For each of the latter eight classes U_a, the actual source identity is U_a union{p}=N_source(a). The check used0.000161110 CPU seconds and is saved in `PARALLEL_CLASS_IDENTIFICATION.json` with all literal classes.

Thus using those nine pins reconstructs an old open neighborhood. In a modified graft, this becomes a full false twin only if that old vertex a retains its neighborhood; source equality alone does not certify a claim about a graph with deleted edges. The parent's specified graft excludes deletion endpoints in N(p), so that premise must be checked against its full edge rule rather than inferred from the source signature alone.

The proposed graft is being closed by the parent's short-route argument; none of its56 choices was generated here. This source-analysis task now pauses, preserving the verified permutation and parallelclasses. It does not continue an automorphism search or start a new graph candidate.
