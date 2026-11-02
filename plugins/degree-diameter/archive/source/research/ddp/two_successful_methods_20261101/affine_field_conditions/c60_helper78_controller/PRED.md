# Fixed Bhakar C60 plus 18 helpers: prediction before computation

The accepted source is only the 60-by-5 controller in
`../../f7_c60_d35/PARAMETERS.json`, with its accepted controller route
certificate. Its author remains Bhakar (author repository
`f4t4nt/degree-diameter-graphs`); this experiment does not reattribute it or
rerun the 20,580-vertex source graph.

Preserve all 150 old edges. Add helpers 60+i, i=0,...,17, whose induced graph
is K3 on 0..2, K3 on 3..5, K4 on 6..9, K4 on 10..13, and K4 on 14..17.
Assign each old vertex exactly one helper. Helpers 0..5 each receive four
pins and helpers 6..17 each receive three pins. The resulting graph has
78 vertices, 234 edges, and degree exactly six.

Prediction: a partition satisfying the complete conditions below gives
A^3 positive on all 6,084 ordered controller pairs. Combined with the
accepted F9 six-port local data and the separately prepared arbitrary
dart-port cross-chart extension, this is a candidate interface for
78*729 = 56,862 vertices and degree 54, 1,512 above the located public
55,350 guarantee. Global priority/record status remains pending. No full
56,862-vertex graph is authorized or generated here.

For C_i the H clique containing helper i, the exact constraints are:

1. Each old vertex has one color i, with loads four/six groups and
   three/twelve groups as above.
2. Each of the 129 unordered helper pairs in distinct H components has an
   old source edge joining its two pin groups. There are 150 old edges,
   leaving 21 edges beyond this necessary pair count.
3. For every helper i and old vertex v, at least one of these holds:
   color(v) belongs to C_i; some old u reachable from v in exactly two old
   steps has color i; or some old neighbor w of v has color in C_i minus i.
   The exact-two-step support includes v itself, and is not a closed R2 set.

Only legal helper relabeling is removed: increasing minimum pin within each
clique and increasing minimum pin across cliques of the same size. In
particular old vertex 0 is not forced into the size-four-pin orbit.

One CNF and one CaDiCaL solve only: preprocessing/encoding at most 20 CPU
seconds; solver at most 60 CPU seconds and 90 wall seconds; total scope at
most 90 CPU seconds including preparation and verification. UNKNOWN is a
terminal bounded result, not an exclusion or permission to continue its
timer. SAT requires direct enumeration of all 78*216 three-step walks,
all 6,084 ordered pairs, literal edge checks, and saved witnesses. UNSAT
only excludes this fixed source and H decomposition after translation
review. No solver installation, old graph BFS, Lean, Gemini, global STATE,
or Wiki edits.
