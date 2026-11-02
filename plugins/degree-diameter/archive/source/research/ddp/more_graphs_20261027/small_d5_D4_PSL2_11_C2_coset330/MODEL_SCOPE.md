# Complete fixed-action degree5 family on330 PSL2(F11)/C2 cosets

This experiment reuses, without reconstruction or a fresh audit, the previously bound660 projective matrices and their multiplication/inverse tables in ../small_d6_D3_PSL2_11_C5_coset132/. Let G=PSL2(F11) and t=(0,1;10,0), an actual projective involution from that binding. Here the new stabilizer is H={identity,t}; vertices are the330 right H-cosets xH, with root0=H.

For any H-doublecoset D, the corresponding directed adjacency is xH to xdH for d in D. This is independent of representative because D is H-biinvariant. An inverse-closed union of doublecosets gives an undirected G-invariant graph; excluding H excludes loops. Conversely, every G-invariant graph in this fixed action is such a union of stabilizer suborbits, with inversion pairing any nonselfpaired doublecosets. Thus inversion orbits of nonloop doublecosets are the indivisible undirected adjacency atoms. Their valencies add because they partition the nonloop neighbor set.

## Actual new-stabilizer binding

The producer recovered168 H-doublecosets: six of size2 and162 of size4. The normalizer of H is the centralizer of its sole nonidentity element t; it has actual order12. Its six H-cosets are the fixed suborbits. After excluding the loop, inversion gives three self-paired matching atoms of degree1 and one degree2 atom obtained by pairing the two remaining fixed suborbits. Outside the normalizer,24 of the162 degree2 suborbits are self-paired; the other138 form69 inverse pairs of degree4. Therefore the complete undirected atom list has

    three atoms of degree1,
    twenty-five atoms of degree2,
    sixty-nine atoms of degree4.

The actual group products establish these counts; none was inserted merely to match the proposal. Every atom is inverse-closed, nonloop, symmetric and representative-independent, checked over all660 group representatives. For every coset the97 atoms partition all329 other vertices exactly, binding both their completeness and their lack of overlap. INPUT_BINDING.json and ATOMS.json save the precise doublecosets, inversion pairing, group IDs and root neighbors.

## Exact valency5 enumeration

Solving the nonnegative degree sum with at most three distinct degree1 atoms gives exactly three possibilities:

    1+2+2: 3*C(25,2)=900,
    1+4: 3*69=207,
    1+1+1+2: 25.

All1132 distinct atom subsets were saved in CANDIDATE_INPUT.json and processed exactly once. Every resulting graph is a simple5regular graph on330 vertices with825 edges. Each candidate's connectivity closure was computed; for connected candidates the complete identity-coset radius4 was computed. Left G multiplication is transitive and preserves each atom union, so identity-radius4 coverage would prove global diameter at most4. The degree5 radius3 Moore bound106<330 would then give exact diameter4.

There were118 disconnected candidates and1014 connected candidates; all1014 connected identity-radius4 tests failed. No positive graph or independent all-root check was needed. Global diameters of negative cases and ordinary unordered bad-pair counts were not measured and remain null. Missing counts in CASES.jsonl refer only to vertices outside the one tested root's radius4.

A graph of maximum degree at most4 and diameter4 has at most161 vertices, below330. Hence checking all valency5 graphs suffices for every simple undirected G-invariant graph of maximum degree at most5 and diameter4 in this fixed G/H action. The complete negative result is for that action; it does not exclude all330-point graphs, other groups or actions, or the general(5,4) cell.

This changes the stabilizer and available adjacency atoms within the same PSL2 coset mechanism. It is not1132 independent methods, nor a repetition of the previous132/H5 or660-point norm5 arithmetic rule. No other stabilizer, group or parameter was started after this batch.
