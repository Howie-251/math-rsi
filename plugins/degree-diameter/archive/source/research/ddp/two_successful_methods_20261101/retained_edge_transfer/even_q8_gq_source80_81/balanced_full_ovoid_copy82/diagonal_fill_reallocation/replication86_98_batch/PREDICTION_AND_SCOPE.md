# One frozen-G1 replication batch: degree86 and98 only

2026-11-01, before execution. Source G1 is the accepted346516-vertex,
14204970-edge, maxdegree82 graph `../graph_d82_D3_n346516.edges`. Its independent
new roles J are4225 first clones plus its first hub, source labels342290+h,
h=0..4225. Their full source neighborhoods are disjoint subsets of the old
H labels below342290, with union size342225. Exactly65 old H vertices are
outside that union. No83 graph is used as a source.

For r=4 and16, append r copies of every frozen full N_G1(J_h), no new-new
edges, and keep all source edges. New labels are346516+4226*b+h, b<r.
The two selected outputs are:

|case|r|n|m|maxdegree|predicted degree histogram|
|---|---:|---:|---:|---:|---|
|multiplicity5_degree86|4|363420|15573870|86|65:5,80:325,81:20865,86:342225|
|multiplicity17_degree98|16|414132|19680570|98|65:17,80:1105,81:70785,98:342225|

The rule is n=346516+4226r, m=14204970+342225r. Each source pin vertex starts
at degree82 and gains r; all other source vertices and all copied roles have
their old degree. The copied-role histogram per block is65:1,80:65,81:4160.
If any literal count, pin multiplicity, degree or ordering differs, record
failure rather than repairing the prediction silently.

Budget: one production batch at most30 CPU seconds including preparation,
C++ compilation, the single source parse, both complete writes and small
recipes. One worker. Producer checks headers, strict lex ordering, preserved
edge counts, actual role N sizes, old loads and all final degrees; it runs no
BFS or old geometry/field/finite/Lean/solver check. The fresh independent
validator is separate. No hashes, installs, other cap or root-state writes.

Every prefix has genuine diameter-at-most3: old-old walks stay in G1; a new
role reaches old vertices by replacing a source-center departure with its
copied first edge, using only G1 interior vertices. Between two new roles,
replace both end departures of a G1 center-to-center walk. If the centers
coincide, use a common old neighbor; if adjacent, their old centers give the
three-walk. In general the standard full-neighborhood-clone Walk lemma
applies to arbitrary center sets and a source with no isolated vertices.
It uses no future new vertex. Retraction sending each copy to its source
center preserves every edge, hence retains the source's non-D2 obstruction.

The public window has actual checked guarantees4225*Delta. Margins70 and82
are relative to that located guarantee only; exact-rule priority and global
status remain UNKNOWN. Actual producer PASS is not fresh acceptance or
concrete Lean completion. Root alone changes counts and requests new reviews.
