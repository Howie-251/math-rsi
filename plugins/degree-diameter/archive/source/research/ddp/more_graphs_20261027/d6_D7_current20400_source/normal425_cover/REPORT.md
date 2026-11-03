# Actual normal425 subgroup and a complete 48-base voltage recipe

The frozen recovery succeeded. It uses the six previously verified
left regular automorphism permutations and cached actual source CSR.
There was no source decode, BFS, candidate graph or large generated-
group enumeration in this task. Both dependent agents received the
READY recipe immediately after its complete adjacency match.

Number the source generators0..5 in the saved N0order. Words denote
permutation composition from left to right as group multiplication,
so the rightmost permutation acts first on a vertex. In the fixed
lexicographic nonbacktracking word scope of length at most4, only
51words were examined before both required factors were found:

- s0*s1*s2 has order10; its square gives a of order5.
- s0*s2*s4 has order85; its fifth power gives z of order17.
- With B=s1 of order12, b=B^4*a*B^(-4) has order5 and is independent
  of a. The first prescribed conjugator already works; A,B,C fallbacks
  were not tried.

The word orders were read from their0cycles, justified by the proved
regular action. Actual full permutation powers were then constructed
by cycle rotations. All three commutation identities were checked
on every20400vertex, and b(0) is outside the five-point a-orbit of0.
Thus <a,b> is C5². The commuting order17element z gives

    N=<a,b,z> = C5 x C5 x C17, |N|=425.

The425coordinates a^i*b^j*z^k(0) were explicitly distinct. For each
of the six source generators, its conjugates of a,b,z have their
0images in this425-point set. In a regular action, equal0images
identify equal group elements, so these18checks establish that each
conjugate belongs to N. Conjugation preserves subgroup order; hence
N is normal in the source group. No general normal-subgroup solver
or reported group-name assumption was used in place of these checks.

Enumerating the N-orbits on actual vertices gives48disjoint orbits,
each425points. Choose each orbit's minimum old vertex as its base
representative; number bases by increasing representative. Every old
vertex has exactly one coordinate (base,i,j,k), where i,j are modulo5
and k modulo17. The encoding is i+5*j+25*k within each fiber.

At each representative, sort its six actual source neighbors by
old label. A neighbor's coordinate determines a directed base port
with target base and voltage (a,b,c17). N acts by graph automorphisms
and its three generators commute, so translating that edge gives

    (base,i,j,k) --
    (port.to, i+port.a mod5, j+port.b mod5, k+port.c17 mod17).

Every base dart has one explicit reverse_port with opposite voltage.
The complete formula was checked at every old vertex: all122400
directed adjacencies, equivalently61200undirected source edges,
match the actual CSR exactly. This is full literal recipe recovery,
not a diameter re-verification or only a quotient graph match.

COVER_RECIPE.json contains the48base records, representatives and
six directed ports each. vertex_coordinates.u32le.bin contains the
quadruple(base,i,j,k) for every old vertex. The inverse lookup is
coordinate_vertices.u32le.bin, at index425*base+i+5*j+25*k. All are
little-endian uint32. NORMAL_GENERATORS.json gives actual word/power
witnesses, three full permutation files, commutation checks and all
18conjugation coordinates. WORD_SEARCH.json preserves the actual
51-word prefix; it is not presented as an enumeration of all936words.

Total recorded recovery CPU was0.114660seconds. The formula has
1200*m vertices when the last cyclic modulus is changed to m, but
connectedness and D7 of any changed modulus are not inherited.
The separately assigned agents own the finite m18/19 actual graph
checks and the1200-state projected short-route analysis. This task
creates no new candidate or lower bound and stops with the actual
source cover recipe ready.
