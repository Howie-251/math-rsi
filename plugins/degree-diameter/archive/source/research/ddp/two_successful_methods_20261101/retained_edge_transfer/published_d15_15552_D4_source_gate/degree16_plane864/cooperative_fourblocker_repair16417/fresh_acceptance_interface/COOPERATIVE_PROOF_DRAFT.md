# Conditional proof for the cooperative16417 literal

This is a preparation template, not an acceptance result. It applies only
after the independent checker binds the actual new16417/{{M}} literal.

Let C be the accepted16416/129240 graph, built from original G on15552
vertices plus864 frozen-full-N clones. C has an accepted concrete D4
kernel target F3Graph15552.Clone16416.d16_16416 and literal label binding.
No source D4, field or old BFS is rechecked here.

The future literal checker independently derives N_v from the old-original
induced graph inside C. It finds the saturated original vertices in N_v,
their unique current clone owners, and checks that the four owners are
exactly the four declared donors D. It deletes exactly those donor-old
edges, adds newZ-fullN_v, and permits exactly the declared simple graph H
on D plusZ. Originaldegree14 overlap is allowed. Degree accounting and
the complete candidate stream certify all final degrees<=16 and the exact
edge delta, without importing producer masks or weighted-route tables.

Remove the four donor VERTICES conceptually to form base B=C-D, with16412
vertices. They remain as modified helpers in the final literal; this is
not a relabeling or loss of four vertices in that literal. All base edges
are unchanged. B contains every original15552 vertex, all116316 original
edges, and the other860 untouched full-N clones.

For each donor d, the accepted old role labels give its original center
c_d<15552. The checker verifies directly in the one old C literal that
N_C(d)=N_G(c_d), containing only original vertices. Define r:C->B by fixing
all base vertices and sending each removed donor d to c_d. Every donor-old
edge maps to a genuine original G edge in B, and C has no donor-donor
edges. Every other edge is fixed. Thus r is a graph retraction. Mapping
the already accepted C Walk<=4 between base vertices through r proves
all base-base pairs have a genuine B Walk<=4. There is no need for a new
16412-root suite. The source retraction is only an upper-bound argument
for this STABLE BASE, not a collapse claim for the final five helpers.

The only modified/new vertices are four donors and Z. The checker runs
ordinary BFS from each of these five actual helper labels on the complete
final candidate file. All16417 targets must be reached within4, including
the other helpers. These five complete rows cover every pair with a helper
endpoint; the base theorem covers all remaining pairs. Hence all final
pairs have distance<=4.

The checker additionally measures fixed old label0 on the NEW candidate
and saves a real shortest4-walk. This proves non-D3 directly. It must NOT
reuse the source0/81 non-D3 witness by collapse: H may join helpers whose
original centers are not adjacent. Alternatively the elementary cap16
Moore radius3 bound3857 is below16417.

This is a JOINT five-helper final-graph proof. Paths may use the other
actual helpers; no sequential one-helper/current-prefix claim is made.
The method is neither ordinary SingleExtension (old donor edges change)
nor another immutable-fullN-clone addition (four donor neighborhoods are
partly removed and H adds helper edges).

Concrete new Lean, weighted-search proof interfaces, priority, reviews,
ROOT release and counters remain separate tasks. This preparation closes
none of them and invokes no old verification suite.
