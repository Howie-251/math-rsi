# PSL2(11)/C2: valid atoms and complete1132-choice scope

Verdict: **VALID**. The inverse-paired orbital atoms have weights1 with multiplicity3,2 with multiplicity25, and4 with multiplicity69. Their weight-five subsets are exactly the1132 candidates, covering every simple undirected graph of maximum degree at most5 invariant under this fixed action that could have D<=4. This is a paper review; no matrix table, coset, graph, numerical sample, solver, or BFS is recomputed.

The actual660-element group table is reused from the [132-point construction](../small_d6_D3_PSL2_11_C5_coset132/ANALYSIS_CONSTRUCTION.md). Only the stabilizer is changed. Let G=PSL2(F11), let t be the class of [[0,1],[-1,0]], and put H=<t>, of order2. The vertices xH number660/2=330. The public target baseline and its read scope are separately recorded in [SOURCE_BASELINE.json](SOURCE_BASELINE.json).

## Normalizer, six fixed cosets, and internal atoms

Because H has a unique nonidentity element, N_G(H)=C_G(t). A determinant-one matrix M centralizes the projective class of t precisely when Mt=tM or Mt=-tM. The commuting matrices have shape [[a,b],[-b,a]], with a^2+b^2=1; they form the norm-one cyclic group of order12 over F121, hence a cyclic group of order6 modulo sign. The anticommuting matrices have shape [[a,b],[b,-a]], with a^2+b^2=-1. They form a coset of the first group, give six projective involutions, and invert its cyclic group. Therefore N is dihedral of order12.

The element t is the unique involution in the cyclic rotation subgroup C6 and is central in N. Thus N has seven involutions in total: t and the six reflections. Its quotient N/H is dihedral of order6, hence S3.

The H-fixed vertices xH are exactly those with x in N, giving six fixed cosets. Remove the root H to avoid loops. The other five fixed cosets, interpreted in N/H=S3, consist of three self-inverse elements and one inverse pair of order-three elements. Thus they supply three symmetric degree-one matching atoms and one degree-two atom. It would be incorrect to count all five nonroot fixed cosets as separate undirected degree-one atoms.

## Outside double cosets and the role of no order4

Every nonfixed H-orbit on G/H has length2. There are324 outside vertices, hence162 outside suborbits. For g outside N, H intersect gHg^-1 is trivial, so its double coset is the four-element set

    HgH = {g, tg, gt, tgt}.

PSL2(F11) has no element of order4. A direct matrix proof is enough: if a projective class of M had order4, the class of M^2 would be a nontrivial involution and tr(M^2)=0. The determinant-one trace identity gives tr(M)^2=2. But2 is nonsquare modulo11, since2^5=-1 there. This contradiction does not need a numerical group enumeration.

If the outside double coset is selfpaired, g^-1 is one of its four displayed members. If g^-1=g, it contains the involution g. If g^-1=tg or gt, then g^2=t, giving forbidden order4. In the final case g^-1=tgt, the element tg is an involution. Thus every selfpaired outside double coset contains an involution; the no-order4 step is essential because the set has even size.

The group has55 involutions, as established by the trace-zero argument in the132-point proof. Seven lie in N, leaving48 outside. For an outside involution g, its double coset contains exactly the two involutions g and tgt. They are distinct. Neither tg nor gt is involutory, because that would make t and g commute and put g in N. Consequently there are48/2=24 selfpaired outside double cosets, each a degree-two atom.

The remaining162-24=138 outside suborbits are paired with distinct inverse suborbits, giving69 degree-four atoms. Combining them with the internal atoms above yields exactly

    weight1: 3 atoms,
    weight2: 1+24=25 atoms,
    weight4: 69 atoms.

The producer's [ATOMS.json](ATOMS.json) is the actual matrix/coset binding; the paper counts do not replace or re-enumerate that artifact.

## Exactly1132 degree-five unions

An invariant root neighborhood must be a union of H-suborbits, and an undirected graph must include each inverse partner. Hence it is a union of distinct atoms just counted. The only ways their weights can sum to5 are:

* 1+2+2: choose one of three weight-one atoms and two of25 weight-two atoms, giving900 choices;
* 1+4: choose one of three weight-one atoms and one of69 weight-four atoms, giving207 choices;
* 1+1+1+2: take all three weight-one atoms and one of25 weight-two atoms, giving25 choices.

The total is900+207+25=1132. Repeated copies of an atom are not allowed in a simple graph and would add no new edges.

Every union defines adjacency by xH~yH when x^-1*y belongs to the corresponding H-biinvariant subset D. It is representative-independent, inverse-closed, and disjoint from H, hence simple and undirected. Left multiplication by G preserves adjacency and is transitive. Each selected union has degree5 and330*5/2=825 edges. Connectivity is not automatic; it is an additional producer check or a consequence of complete root coverage.

A graph of maximum degree at most4 and diameter at most4 has order at most1+4+12+36+108=161, less than330. Therefore every graph in this fixed transitive action with maximum degree<=5 and D<=4 must have degree5 and is one of these1132 unions. No lower-valency invariant target is omitted. This completeness is not a classification of arbitrary330-vertex graphs or all vertex-transitive graphs.

## Mechanism and terminal boundary

Changing the stabilizer from C5 to C2 changes the actual orbital mechanism: the132-point action had only one available matching plus one five-neighbor orbital, whereas this action admits several distinct low-valency atoms that can be combined without imposing extra symmetry. These are complete invariant graph choices, not free bad-pair edits.

One of the25 unions of type1+1+1+2 takes only the internal N/H atoms. It contains all five nonidentity elements of S3 in each normalizer block and is exactly55 disjoint copies of K6. Thus the atom count itself never implies connectivity. The other combinations likewise require full actual coverage, not only degree or transitivity.

The producer's [RESULT.json](RESULT.json) records all1132 cases processed:118 disconnected and1014 connected cases, each of the latter failing its identity radius4 check. The actual atom multiplicities matched the paper counts, with zero untested cases. This paper reads that terminal evidence without repeating it. Combining that completed computation with the completeness above excludes D<=4 in this fixed G/H action of maximum degree<=5. Negative radius checks do not supply an exact larger diameter or ordinary unordered bad-pair total; both remain null.

No additional group, subgroup, orbital profile, graph, or solver is proposed by this review. The old matrix construction and all numerical results retain their original evidence paths and credits.
