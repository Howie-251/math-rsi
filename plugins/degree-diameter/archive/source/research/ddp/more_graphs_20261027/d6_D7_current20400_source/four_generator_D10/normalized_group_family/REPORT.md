# The actual source group has no connected quartic Cayley graph of diameter10

The normalized family is complete: all213new cases were constructed
and checked, and the three proved old-control equivalents were
inherited without new graph construction or BFS. There are zero
D10hits, zero untested cases and zero UNKNOWN results. The frozen
prediction of a successful degree4,D10graph on20400vertices is refuted.

The independently supplied normalization_proof/PROOF.md establishes
coverage of every connected undirected degree4Cayley generating set
on the actual source group Gamma. It reduces the two inverse pairs to

    first = alpha^a,   a in {1,3,5,7},
    second = N(v,c17=1)*Hbeta*alpha^b,   b=0,...,8,
    v in {(1,0),(1,1),(1,2),(1,3),(1,4),(0,1)}.

All216parameter combinations are retained. The proof handles the
other involution allocations and establishes that these216cases are
connected. This is a complete representative family, not a claim of
216nonisomorphic graphs. The producer used the actual Hbeta from
h48_complement, not the original positive source generator B.

normalization_proof/CONTROL_IDENTITIES.json supplies exact algebraic
identities for the previously measured controls:

| Old source-pair control | Inherited normalized case | New BFS |
|---|---|---:|
| A,B | a1,b4,v(1,4), ordinal28 | 0 |
| A,C | a1,b5,v(1,1), ordinal31 | 0 |
| B,C | a5,b4,v(1,3), ordinal135 | 0 |

Only their isomorphism-invariant diameter11 and root coverage counts
are inherited. Their old literal witness labels were not transported
to the normalized labeling and are explicitly null in the normalized
rows. They must not be read as actual normalized witness vertices.

For each of the213new cases, the actual four permutations and their
true inverses give a simple4-regular graph on20400vertices with40800
edges. Complete ordinary BFS from0reaches all vertices. Abstract
right multiplication of Gamma preserves these left-Cayley edges and
acts transitively, so each measured root eccentricity is the exact
global diameter. The diameter distribution, including the inherited
three cases, is110cases at11,104at12, and2at13. No case has diameter
at most10. Distance histograms and first actual beyond10witnesses
for all newly tested cases are preserved in RESULT.json.

Consequently, with the normalization proof, **no connected undirected
4-regular Cayley graph on this actual Gamma has diameter at most10**.
Its minimum possible quartic Cayley diameter is exactly11, since the
old controls already attain11. This is a fixed-group statement. It
does not exclude other groups of order20400, arbitrary20400-vertex
quartic graphs, or improve the general N(4,10) bound. It is not a
claim of historical priority or a Lean result.

Native CPU was0.133757seconds, compilation1.677065seconds, and total
producer parent-plus-child CPU1.834137seconds, within the10second
budget. There were213new root BFS runs, zero old-control reruns,
zero source D7checks, zero downloads and zero exported failed graphs.
The fixed family is closed and stopped. No generator, phase, field,
frame or scalar was tuned in response to a smaller bad-target count.
The separately authorized chi17=6action is a different group model
and is not included in this chi17=5fixed-group theorem.
