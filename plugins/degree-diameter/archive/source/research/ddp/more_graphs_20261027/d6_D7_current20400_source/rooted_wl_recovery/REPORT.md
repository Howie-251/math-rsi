# Rooted 1-WL recovers one actual automorphism of the 20400 source

The frozen prediction was supported. The longest sparse6 literal
was extracted from the saved primary Sage script and decoded with
the already available networkx. No author code was executed. The
actual graph is simple, with20400vertices,61200edges and degree6 at
every vertex. No graph BFS or original D7 verification was run.

Initial colors distinguish the root with color1 and give every other
vertex color0. At every round the signature is the old color followed
by the sorted tuple of neighbor colors; all distinct whole-graph
signatures are numbered in lexicographic order. The class counts for
root0 were

    3,4,5,6,10,58,2991,20400.

Thus its rooted partition became discrete at round8. This was a
testable property, not an inference from the reported regular
automorphism group. It also provides a mathematical certificate that
an automorphism fixing root0 must be the identity: it preserves each
successive color and hence every final singleton.

Only the conditionally authorized second root was then processed:
the first old neighbor in numeric order,850. The same canonical
procedure again became discrete at round8, with the same class-count
sequence. Matching identical singleton colors defines a permutation
pi. Direct checks establish that pi is bijective, pi(0)=850, and all
61200old undirected edges map to edges, with zero failures. This is
one actual nonidentity graph automorphism, not just an unverified
color-based guess or a claim about all group generators.

AUTOMORPHISM_CHECK.json records the complete edge-check scope.
automorphism.pi.u32le.bin contains all20400images in source vertex
order. The two root JSON files preserve round counts and terminal
cell histograms, and their color arrays are saved separately. The
decoded source is cached once as adjacency.csr.u32le.bin, layout
uint32 n,2m,n+1offsets,then2m neighbor IDs, so later authorized work
can reuse the literal without parsing the primary script again.

Total recorded CPU was0.886444seconds, including0.503509seconds for
networkx import and literal decode. The two refinement runs used
0.170037 and0.174886seconds. There was no dependency installation,
extra root, extra anchor, 2-WL, group enumeration, candidate graph
or new lower bound. The task stops with this one recovered actual
automorphism; the remaining neighbor maps and a full algebraic
normal-form/generator recipe have not been recovered here.
