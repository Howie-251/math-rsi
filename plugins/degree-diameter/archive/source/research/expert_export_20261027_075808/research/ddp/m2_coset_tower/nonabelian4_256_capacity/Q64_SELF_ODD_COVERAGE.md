# Exact Q64 self-orbit odd-phase coverage reduction

This is a paper consequence of the group and undirected voltage rules.
It does not evaluate a coordinate assignment, add a graph search, or
assert a uniform positive defect.

Fix the phase mask and actual legal Z32 voltage coordinates. Let

    R_i = {x in Z32 : (i,(x,1)) is reachable within three steps
                        from (i,e)}.

Every base walk counted here starts and ends at i. Reverse it, replacing
each directed voltage by its inverse. The reversed walk is still valid,
has the same length, and evaluates to the inverse group element. In Q64,

    (x,1)^(-1)=(x+16,1).

Consequently R_i=R_i+16. If pi:Z32 -> Z16 is reduction modulo 16, then

    R_i = pi^(-1)(pi(R_i)),
    |R_i| = 2*|pi(R_i)|,
    missing_self_odd(i) = 2*(16-|pi(R_i)|).

These are equalities, even if the lift is disconnected or some voltages
produce fewer distinct endpoints than the formal capacity suggests. Simplicity
is still required for the intended degree-eight construction; the
inversion argument itself only needs inverse edge maps.

For fixed phases, each short-word coordinate is an affine Z32 form

    c + sum a_k*z_k, with c in {0,16}.

After reduction modulo 16, the constant disappears. Thus pi(R_i) is
obtained by evaluating the saved self/odd coefficient vectors modulo 16.
Inversion pairs (a,c) with (a,c+16), so one representative of each pair
is enough for this projected set.

This proves two implementation consequences without assuming any
additional symmetry:

1. Exact self/odd coverage depends only on the thirteen coordinates
   modulo 16. Changing any one coordinate by 16 leaves all four
   self/odd reachable sets unchanged, as full subsets of Z32.
2. Put delta_i=16-|pi(R_i)|. The total missing count over the four full
   group-orbit roots is at least 2*sum_i delta_i. Since common left
   Q64 action has four free vertex orbits of size 64, the full graph's
   number of unordered pairs at distance greater than three or
   unreachable is exactly 32 times that four-root missing count.
   Therefore a deterministic lower bound is

       full_bad_pairs >= 64*sum_i delta_i.

A D3 candidate must have every delta_i=0. This permits a small necessary
filter or a partial-score lower bound before evaluating all other
targets. If the current objective uses four-root missing counts, the
safe partial bound is 2*sum_i delta_i, not the full-graph factor 64.

The reduction supplies **no assignment-independent positive lower
bound** for a surviving phase mask. Its projected forms could cover
all sixteen values. It also does not determine any of the other
twenty-eight root–target–phase slots: off-diagonal inverse walks start
at the other base vertex, so they do not establish this same-root
central-translation pairing there. Passing the projected self/odd
test cannot replace actual full coverage or the authorized graph
verification.

No additional finite computation was performed for this note.

## Appendix: the saved best has a central-quotient obstruction

The subsequent actual Q64 batch is recorded separately in
`../nonabelian4_256_search/`. Its independently checked best has D4,
832 bad unordered pairs, and four-root missing counts (9,6,3,8).
The saved `best.coverage_diagnosis.json` shows all four self/odd slots
complete, so the preceding self/odd lower bound is zero for that graph.
It is not an explanation of its remaining defect or a sufficient
coverage test.

There is, however, a different exact necessary condition. Let

    z=(16,0), Z={e,z}.

This is a central subgroup of Q64. The quotient reduces x modulo 16:

    Q64/Z = D32 = Z16 semidirect_{-1} C2,
    (x,s)(y,t)=(x+(-1)^s*y mod16, s xor t).

Project each voltage and retain the same four-orbit base. The quotient
has 128 vertices. Distinct parallel original matchings may coincide
after projection; merging such repeated edges does not change quotient
distances. A quotient walk can be lifted from any chosen original
starting vertex by taking its corresponding sequence of voltage edges.
Conversely, projection takes every original walk to a quotient walk.
Therefore, for any target quotient vertex with central lifts v and vz,

    d_quotient(pi(u),pi(v)) = min(d_original(u,v),d_original(u,vz)).

In particular, if both original targets have distance greater than
three, the quotient target is genuinely missing. This is stronger
than merely observing one missing lift.

For the saved best, root orbit 0 to target orbit 3 at odd phase misses
both x=3 and x=19; the reverse class pair misses those same coordinates.
These are the two lifts of x mod16=3. The stored-distance diagnosis
reported by the root gives quotient root deficits

    (1,0,0,1),

with both missing targets at distance four. The observation also follows
at the necessary-coverage level from the two complete missing central
pairs listed in `best.coverage_diagnosis.json`. No new BFS was used here.

Now fix all thirteen voltage coordinates modulo 16, and fix their
phases. Each coordinate has two central lifts, giving at most 2^13
normalized choices. A choice that creates duplicate parallel voltages
would still need to be rejected for simplicity. Every legal choice has
exactly the same quotient graph, because multiplying any voltage by z
does not affect its projection.

For every such legal lift, each of the two missing quotient targets
forces both of its central lifts to remain missing. Thus the four-root
missing count is at least four. The common left Q64 action gives

    full_bad_pairs = 32 * four_root_missing_count >= 32*4 = 128.

Equivalently, the quotient's 32 unordered bad pairs between those two
orbits each have four bad lifted pairs, again giving 128. More
generally, a quotient four-root missing total M forces full bad pairs
at least 64*M.

This excludes D3 for the fixed saved-best modulo-16 assignment under
all central flips; **it does not exclude other modulo-16 assignments**.
A quotient-first construction followed by binary central lifts is a
possible future method, but was not implemented or searched in this
note. Even a D3 quotient would only be necessary: its paths need not
cover both central lifts of every target.
