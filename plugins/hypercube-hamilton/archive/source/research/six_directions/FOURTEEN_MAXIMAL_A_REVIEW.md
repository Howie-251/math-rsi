# Fourteen-hole maximal-A independent review

Verdict: **PASS**, restricted to the new 60-record maximal-A sufficient route.
Reviewer: fresh `/root/fourteen_maxa_audit`, user-selected GPT-6.1-sol/high,
ARIS proof-checker workflow. `review_independence: same-family`;
`acceptance_status: provisional`. This is a mathematical argument plus an
independently implemented exhaustive finite check, not Lean verification.
The producer, root reviewer, and producer sanity script are not independent
acceptance authorities for this decision.

The accepted FORCED source has 2,587 covered-target records. Exactly 60 of
its v=31 records are now proved sufficient for every realizing original
short matching. Its exact residual is 2,527 = 240 + 702 + 1,585. The already
accepted fourteen-hole free-target branch remains proved, with zero free
records outstanding. Full fourteen-hole and full P6 remain unproved.

## Inputs, trust boundary, and reproducibility

The audited claim is the maximal-A section of
`FOURTEEN_RESIDUAL_STRUCTURE_PROOF.md`, frozen by
`FOURTEEN_RESIDUAL_STRUCTURE_MANIFEST.json` (SHA256
`8100b79d8b34249952585150b95586ac6b1a78d806ffe349297181c5c6b3858c`).
The checker verifies every listed input and output digest. In particular,
the source `FOURTEEN_FORCED_REVIEW.json` is bound to
`3e3042d5ea24490589b7d75242d5140614503fc5dc920c6eee4a11c6358e34b1`;
its accepted residual digests are checked against the actual three streams.
The imported local `TWELVE_NEW_FORCED_REVIEW.json` is bound to
`60317e5e8c091ece3d16834c71b29fd196ebee11d93a0ed8dbbab2cc4dc895dd`.
Only its five exact accepted marked T19 statements 79,178,361,363,373 are
used. Its universal local iff theorem concerns arbitrary perfect matchings
on the covered domain, with a cycle adding short edges iff its stated
same-parity pair is absent. No deficient-rank inference is imported.

General accepted path-compression and endpoint-completion arguments may be
reused, but the changed six-hole A geometry, the extra original hole14,
every selected physical forest, the actual B marked inputs, and actual
obstruction exclusion are checked here. Old forest pools are witness
containers only: their ranks and their former finite domains are irrelevant.
Producer scripts are never imported or executed by the new checker.

Run `D:/anaconda/python.exe FOURTEEN_MAXIMAL_A_REVIEW_check.py` from this
directory (or supply its absolute path). It reads frozen producer files and
writes only `FOURTEEN_MAXIMAL_A_REVIEW_check.json`. The recorded full run
checked 287,469 witnesses in about 31 seconds. No producer file, source
stream, production ledger, or main run state was modified.

The exploratory 88-orbit structure classification, zero-hit alternative
root-in-obstruction search, failed prefixes for orbits79/87, and eighteen-hole
observation are not additional theorem acceptances in this review. They are
unnecessary for the exact 60-record subtraction certified here.

## Quantified statement and proof-obligation ledger

For every original short matching M realizing
Z={39,43,45,51,60,63}, W={1,2,4,8,14,16,32}, root0 and covered target31,
there is a Hamilton 0--31 path retaining every M edge and adding only short
edges. The statement transports under the actual common cube automorphisms
fixing0,31; its entire accepted application domain is the 60 checked images.
The following closes each nontrivial obligation.

1. **Actual induced A domain.** In the bit32 cut, A's original holes are
   {0} union J, J={1,2,4,8,14,16}. Hence G has 15 even and 10 odd vertices.
   T=mirror(Z)={7,11,13,19,28,31} consists of covered A vertices whose B
   mirrors are holes. Since M is short, these vertices cannot cross and
   are internally L=M|A covered. In particular31 has an internal even
   mate h, unchanged by extending L. All unmatched G vertices are exactly
   original crossing ports, not unfilled original holes.
2. **Maximalization and quantifiers.** Greedily add disjoint G edges to
   obtain any inclusion-maximal Lstar containing L. It still covers T,
   and has at most10 edges. No maximum-cardinality assumption is used.
   The independently enumerated whole maximal domain supplies a positive
   witness for this actual Lstar; witness selection may depend on M through
   Lstar. This proves a universal-in-M existence assertion.
3. **Finite witness soundness.** Each selected q is even and Lstar-unmatched;
   t is in T minus31 and adjacent to q; w,b are distinct units in J. The
   selected physical P is short on A minus{0,31}, has degrees2 exactly at
   q,b and degrees1 elsewhere, and contains q-t. Replace31-h in Lstar by
   w-h to obtain Lstarprime. This auxiliary edge may be long, which is
   permitted at this stage. Labelled P+Lstarprime is acyclic: duplicated
   edges are rejected as two-edge cycles rather than collapsed.
4. **Exact endpoints and completion.** Write Xstar=G minus V(Lstar) and
   S=J minus{w,b}. The endpoint set is exactly
   Qstar=(Xstar minus{q}) union S, with14-|Lstar| endpoints of each parity.
   Thus there are at least8 endpoints and at least4 path components.
   The numbers of even-even and odd-odd path components agree. If they
   are nonzero, cyclically alternate these types and insert all mixed
   components in one transition with orientations making every join
   opposite-parity. If all components are mixed, orient each even-to-odd
   and concatenate cyclically. These joins form a matching Dstar between
   distinct components, giving one simple30-cycle. There are at least4
   components, so no physical edge can coincide with an existing path
   edge. Dstar need not be short and later disappears.
5. **Lift to the arbitrary actual L.** Since31 is already covered in L,
   its mate h is unchanged and Lprime=L-31h+wh is a submatching of
   Lstarprime. Put D=Dstar union(Lstarprime minus Lprime). This is a
   matching: the added difference is a submatching of Lstarprime, whose
   covered vertices avoid Dstar. Its support is exactly
   (X minus{q}) union S, with X=G minus V(L), by taking the difference
   of the covered vertex sets. Consequently C_A=P+Lprime+D is the same
   simple30-cycle. This algebra proves the lift simultaneously for every
   submatching L covering T; enumeration of only favorable original M
   is not being substituted. Hole14 belongs to S for every option and
   is covered by Dstar, never by Lstar. The original extra hole is not
   silently counted as an original crossing port.
6. **Opening and attachment.** Both q and t avoid D: q is unmatched in
   Lstar and excluded from Qstar; t is originally internally L-covered
   and still covered by Lprime. Also q-t is not required by Lprime,
   since q was an actual crossing port. Delete D and q-t from C_A.
   These are disjoint edges and leave a path forest with endpoints
   exactly X union S union{t}. Attach all actual M crossings, the four
   short S bridges, and t--mirror(t). The latter consumes an original Z
   hole, so has no original B conflict. Every retained A vertex now has
   degree2, and every retained required A edge remains present.
7. **Simultaneous suppression is legal.** The B attachment set is the
   disjoint union of actual crossing endpoints, Y=mirror(S), and
   mirror(t). Every Y vertex was originally internally B-covered,
   because its A mirror was an original hole. Y is one parity, its
   original mates are distinct and opposite parity, and those mates
   lie outside all attachment endpoints by matching disjointness.
   Thus each conflict is a pendant original B edge. Even when an A
   transfer joins two Y vertices, suppressing both gives a path between
   their distinct mates, not a cycle. No internal A cycle is present,
   since a nonempty matching was removed from a simple A cycle.
8. **Actual compressed local domain.** After suppressing those paths the
   B matching has minority hole{32}, majority holes
   (Z minus{mirror(t)}) union Y, and omissions exactly Y. These are
   1,9,4 distinct vertices respectively. It is an arbitrary perfect
   matching on the22 covered B vertices. The local theorem permits
   arbitrary required matching edges, so the compression need not
   preserve shortness. All208 full finite options independently match
   an accepted minority/majority/omission/forced-hole/pair tuple under
   one common coordinate permutation, rather than separate set maps.
9. **Actual R obstruction, not original-only exclusion.** For each option
   its transported R has two same-parity endpoints outside holes and
   intersects {mirror(w),mirror(b)}. Either protected vertex is originally
   internally B-covered: its A mirror is an original hole. It is outside
   Y, consumed Z, and every original crossing port. Its actual short
   original B edge survives all compression unchanged: its mate has
   parity opposite Y and hence cannot be suppressed at Y. Since the
   other endpoint of R has the same parity as the protected vertex,
   that actual surviving edge is different from R. The actual compressed
   matching therefore cannot contain R. Checking only original M_B
   would have been insufficient; the unchanged-edge argument is essential.
10. **Invoke local theorem with every hypothesis.** The actual marked
    1:9:4 domain and arbitrary perfect matching satisfy the transported
    accepted T19 iff theorem; item9 discharges its only obstruction.
    It yields a cycle on B minus Y retaining the compressed matching,
    with all newly added edges short. Expand each compressed edge and
    suppressed original edge. Distinct interiors and the local single
    cycle give one62-cycle on Q6 minus{0,31}, containing all of
    F=M-31h+wh. All auxiliary D edges and placeholders have disappeared.
11. **Restore the original matching and endpoints.** The62-cycle contains
    the auxiliary wh. Delete it, prepend short0-w, and append the original
    short h-31. Since w was an original hole, wh was not an original
    required edge. The resulting Hamilton0--31 path preserves all original
    edges, including the restored31-h, and adds only short physical edges.
12. **Finite domain completeness.** A fresh recursion processes the actual
    ten odd G vertices, tries every currently unused short even partner,
    and also permits an unmatched choice exactly outside T. A leaf is
    inclusion-maximal iff every neighbor of each unmatched odd is used.
    This is necessary and sufficient because G is bipartite. Its exact
    set of partner words has 287,469 elements. Every legal certificate
    word occurs in that independent set exactly once, and the sets are
    equal. Hence no size8/9 maximal input, optional unmatched vertex,
    or boundary case can be omitted through a claimed cardinality alone.
13. **Exact application and inherited branch.** Independently applying all
    120 permutations of the low five coordinates gives exactly60 images
    of the full Z/W representative. All60 are in the accepted FORCED
    v31 residual. Every supplied actual transport is checked simultaneously
    against its actual source index and full record, fixing root0,target31.
    The positive streams and complementary streams agree byte-for-byte
    with the independent partition. There is no overlap with an earlier
    accepted subtraction. Free-target closure is inherited solely from
    the bound accepted FORCED source; this proof makes no new free claim.

## Independent finite results and attempted failures

The exact domain count is 274,691 size10 +12,772 size9 +6 size8 =287,469.
Every selected record passed matching legality, T coverage, uniqueness,
forest shortness and degree constraints, opening-edge membership, labelled
cycle rejection, exact endpoint equality and endpoint balance. Endpoint
populations were8,10,12 in those same respective counts. The selected
case histogram is case1:250,808; case2:21,650; case3:129; case4:14,882;
case0:0. There are35,195 distinct transformed forests used.

All208 B options passed exact common-map verification; accepted class
counts are79:52,363:52,361:52,178:26,373:26. The checker recomputes the
actual B sets from Z,J,t,w,b, verifies transported R and the protected
endpoint parity/nonport exclusions, and records all common-map witnesses.
It does not trust the registry's status or a class identifier alone.

Counterexample pressure included a maximal nonmaximum matching (the6
size8 and12,772 size9 cases were explicitly checked), duplicate physical
required/forest edges (labelled union rejects them), treating14 as a port
(exact endpoint sets enforce14 in S), omitting an original L edge during
maximalization (the submatching identity preserves it), changing target's
mate (31 belongs to T), a completion touching t or q (exact supports
exclude them), a Y-to-Y transfer (pendant-conflict proof covers it), and
an R pair manufactured by compression (protected original short edge
survives). No counterexample or unresolved proof obligation was found.
There are no limit, asymptotic, probabilistic, or uniformity transitions.
Dependencies are acyclic: accepted source/local theorem -> new universal
finite A gate -> new splice -> exact60 partition. No new result is used
to justify one of its own inputs.

The accepted residual counts are v1:240, v7:702, v31:1,585. This review
does not imply closure of the2,527 remaining covered geometries, full
fourteen-hole extension, eighteen-hole extension, or full P6.
