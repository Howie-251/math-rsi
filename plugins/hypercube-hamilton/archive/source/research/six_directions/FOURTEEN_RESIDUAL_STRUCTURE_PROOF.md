# Fourteen-hole residual structure and one new maximal-A sufficient route

2026-11-02. Proof-writer/producer `/root/fourteen_reuse_review`. **All new structural computations, reduction and finite application below require fresh independent review.** This work does not self-accept its results and does not modify any frozen source or main state.

## Exact structure of the3,923 Hall-retained covered records

The source streams are `FOURTEEN_HALL_remaining_v{1,7,31}_covered.bin`,13-byte sorted Z6/W7 records. Their3,923 geometries are invariant under the coordinate-permutation stabilizer fixing root0 and target v. Exhausting that actual group yields88 exact disjoint orbits:

| target | Records | Group order | Orbits |
|---|---:|---:|---:|
|1|840|120|12|
|7|1188|36|46|
|31|1895|120|30|
|Total|3923|—|88|

`FOURTEEN_RESIDUAL_STRUCTURE.tsv` lists every representative, orbit size, root-hole-neighbor count and forced-edge count. The JSON supplies all marked sets, every covered-graph allowed/forced edge, one explicit25-edge perfect matching, actual target-mate possibilities, and cut structures. Unlike the earlier Hall exclusions, every retained representative has a positive original matching. Its orbit images give positive matchings for every record.

For each representative we orient covered-graph nonmatching edges E->O and matching edges O->E. An edge outside the chosen perfect matching occurs in some perfect matching exactly when it lies on a directed alternating cycle; equivalently its endpoints are mutually reachable. A chosen matching edge is forced exactly when it lies on no such cycle. This is exact because the symmetric difference of two perfect matchings is a disjoint union of alternating cycles; conversely flipping one directed alternating cycle gives another perfect matching.

There are575 records with no forced edge,3,036 with one and312 with two. In every forced case, every forced edge has a covered endpoint of degree one. The JSON includes this elementary positive certificate: all five other cube neighbors of the stated leaf are original holes. Thus every original matching must use that unique covered neighbor. Exactness of the complete classification uses the alternating-cycle argument; the new necessary-edge evidence needs no unsuccessful matching search.

The root-neighborhood histogram is explicit in the JSON. In particular the575 records with no forced edge consist of455 v31 records with all six root neighbors holes and120 v31 records with five root neighbors holes. Every v1/v7 record has at least one degree-one-forced original edge.

## Two explored routes and their boundaries

A root-in-obstruction extension is valid under an additional internal-edge certificate. If a local single forced pair is root-q and q has an original forced short edge q-h internally in B, then that edge is unchanged by suppression: q has Y parity, h has opposite parity and hence is outside Y; neither endpoint is an attachment port. Therefore actual L contains q-h and cannot contain root-q. For several disjoint same-parity forced pairs, the component of L+R through root-q exits V(R) at h and cannot be cyclic; other obstruction cycles are avoided by the usual completion-pair construction. The automatic deletion-gap inequality is unchanged because root is not an original port.

We exhaustively tested this sufficient geometric route using every accepted explicit forced class and the new six single/two double candidate classes from `FOURTEEN_FORCED_candidate_classes.json`. Every original forced edge was justified by its degree-one endpoint. It yields zero additional hits on these3,923 records. This is a failure of this conservative route, not a negative path result. The new local candidates remain conditional on their separate local acceptance gate.

For the maximal-A route,22 orbits/888 records have at least one usable accepted marked B option before solving the A finite premise. Intersecting with the separately produced `FOURTEEN_FORCED_remaining_v*_covered.bin` leaves only three orbits/180 records, indices79,85,87 in the structure table. This intersection avoids redoing previously covered work. The fullA finite run below closes the middle orbit as a producer sufficient construction; the other two remain open under this route.

## New60-record representative and exact theorem

Take root u=0,target v=31 and

Z={39,43,45,51,60,63}, W={1,2,4,8,14,16,32}.

Its stabilizer orbit fixing u,v has60 records, all in the new FORCED residual. We claim conditionally on the finite certificate gate below that **every realizing original25-short-edge matching M** has a Hamilton0--31 path containing M with only short new edges. No original matching is chosen favorably.

Cut by bit32, with A=Q5 at bit32 zero. All Z lie in B. A holes are0 and J={1,2,4,8,14,16}; B holes are Z union {32}. Because63 is a hole, covered target31 must be internally A-matched. Write L=M restricted to A. Its graph G has

E={3,5,6,9,10,12,15,17,18,20,23,24,27,29,30},
O={7,11,13,19,21,22,25,26,28,31}.

Every t in T={7,11,13,19,28,31}=mirror(Z) is internally L-covered: crossing at t would require its B mirror, which is a hole. Extend L by adding short G edges to any inclusion-maximal matching Lstar. This preserves all original edges and coverage of T. The target mate h=L(31)=Lstar(31) is unchanged. There are at most10 Lstar edges, so at least five even G vertices remain unmatched.

The finite certificate supplies for every such maximal Lstar:

- an unmatched even q, a t in T minus {31} adjacent to q;
- distinct unit holes w,b in {1,2,4,8,16};
- a short forest P on A minus {0,31}, degree two at q,b and degree one everywhere else, containing q-t;
- acyclicity of the labeled union P+Lstarprime, where Lstarprime replaces31-h by w-h;
- a simultaneous actual B marked input in an already accepted single-forced T19 class, with its obstruction meeting {mirror(w),mirror(b)}.

All duplicates between required and forest edges are labeled two-edge cycles and are rejected. The finite test does not replace this premise by a deficient universal rank.

Let Xstar be the unmatched vertices of G. With S=J minus {w,b}, |S|=4, the endpoints of P+Lstarprime are exactly (Xstar minus {q}) union S. The original unmatched surplus is five even vertices; removing q leaves surplus four, and S adds four odd endpoints. Thus the endpoint counts are balanced. There are at least eight endpoints, hence at least four path components. Pair the endpoints across opposite parities to join the paths cyclically: alternate the even-even and odd-odd paths (whose numbers agree), insert even-odd paths, and orient/concatenate cyclically; if all paths are even-odd simply concatenate them consistently. This gives a matching Dstar joining distinct components into one thirty-cycle C_A=P+Lstarprime+Dstar.

For actual Lprime=L minus31-h plus w-h, put D=Dstar union (Lstarprime minus Lprime). This is a matching because the second set is contained in Lstarprime and Dstar avoids its covered vertices. The cycle is also P+Lprime+D. Its deletion endpoints are exactly the original A crossing ports minus q, together with S. A maximal extension is therefore sufficient for every original L contained in it. The additional original odd hole14 is explicitly in S and is covered by Dstar, never by Lstar; it is not silently treated as an original matching endpoint.

Delete D and the short edge q-t from C_A. The edge q-t is disjoint from D: q is Lstar-unmatched and excluded from Dstar endpoints, while t is originally internally L-covered and hence covered by Lprime. Attach all actual M crossings, the four short bridges from S and the short bridge t--mirror(t). The consumed B vertex mirror(t) was a Z hole. The only conflicts with original B matching edges occur at Y=mirror(S). These four same-parity vertices were originally internally B-covered, since their A mirrors were original holes. Their distinct opposite-parity mates are outside holes and all attachment endpoints. Thus simultaneous suppression has only pendant conflicts and cannot create a cycle.

The actual compressed B matching has minority hole {32}, majority holes (Z minus {mirror(t)}) union Y (nine vertices), and omissions exactly Y (four vertices). This is an exact marked T19 input, not an unmarked type assertion. Every finite option is transported simultaneously to one of the accepted `TWELVE_NEW_FORCED_REVIEW.json` rows79,178,361,363,373.

The selected obstruction pair has at least one endpoint in {mirror(w),mirror(b)}. Both these vertices are originally internally B-covered nonports, outside Y; their actual short B edges remain unchanged after compression, and their mates have parity opposite Y and outside the obstruction. Consequently the actual compressed matching cannot contain that same-parity obstruction pair. Apply its accepted local iff theorem to obtain a cycle on B minus Y, retaining the arbitrary compressed matching with short new edges.

Expand every compressed path and suppressed original edge. This yields one sixty-two-cycle on Q6 minus0,31 containing the modified matching F=M minus31-h plus w-h. Remove w-h, prepend the short0-w edge, and append the original short h-31 edge. The resulting Hamilton0--31 path retains every original edge, including h-31; all completion edges and compression placeholders have disappeared. The only new physical edges are short.

## Complete finite positive gate, producer evidence

The full domain is every inclusion-maximal G matching covering T, not merely maximum matchings. The unmatched optional-odd-subset/injective-neighbor DP counts287,469, split as274,691 ten-edge,12,772 nine-edge and6 eight-edge matchings. The DFS supplies the same number of unique positive original matching records. Each32-byte record stores at most eleven sorted edges padded255, then size at byte22, q,t,w,b,forest case, two-byte forest row, common permutation and internal-target flag. Byte layout matches the earlier positive maximal-A format; no old accepted finite domain is imported as if it included this one.

The new run `FOURTEEN_RESIDUAL_STRUCTURE_maxA_full_85.json` exhausts all287,469 and finds a positive forest for each. It uses the five old short forest pools as candidate witnesses only; their rank metadata is not a premise. In particular the7998-row pools that were unnecessary for the twelve-hole proof are valid candidates here solely when their selected physical forest passes direct checks. Every selected forest must be independently checked against its actual q,t,w,b and common permutation. The finite report's historical case03 label actually counts case1 under the generalized indexing; the authoritative complete case histogram is in the new producer sanity JSON.

`FOURTEEN_RESIDUAL_STRUCTURE_sanity.py` checks all287,469 selected forests, original matchings, maximality, T coverage, uniqueness, degrees, opening edges, exact options and labeled union acyclicity directly. It also checks balanced endpoint counts and equality to the independently implemented producer DP cardinality. This is **producer sanity, not fresh independent acceptance**. The future reviewer must independently establish the complete domain and all positive witness conditions, plus the exact B marked lookup and orbit/application sets.

The60 positive original-label records and exact complement after the separate FORCED source gate are frozen separately. Candidate remaining counts become240 at v1,702 at v7 and1585 at v31, total2527. These are producer sufficient counts pending the new reduction/finite/application review. No full14 or P6 closure follows.

For orbit79, the current pool fails by maximal input index83; for orbit87 by index120. Their saved positive prefixes and failed inputs are diagnostic only. They do not refute extension or even the broader maximal-A route. The failure can occur because every q available in the restricted B-compatible option library is already matched. A useful next step is a second opening operation or additional accepted B marked classes, rather than trusting further rank flags.

## Brief18-hole template observation

The separately conditional150-record eighteen-hole domain has four fixed-target orbits of sizes30,60,30,30, all with W containing the full root-neighbor star. Only its final30-record orbit has all eight Z in B for the same bit32 cut. There A has three extra odd holes14,22,25, b=8; the analogous one-consumed-Z opening would demand B shape (1,13,6), a new local certificate obligation. The other120 records have one or two even A holes and require a larger variation. This is a structural observation only, not an eighteen-hole theorem or acceptance.
