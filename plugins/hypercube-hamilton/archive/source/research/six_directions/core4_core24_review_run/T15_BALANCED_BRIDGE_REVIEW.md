# T15 balanced bridge: independent review

Verdict: **PASS, same-family / provisional**, for the complete matching
quantifier of cores **2, 7, 10, 44** only. The deterministic finite checks
pass. No FATAL, CRITICAL, MAJOR, or MINOR mathematical issue was found.
This is not a proof of all T15 geometries, the full eight-hole layer, or P6.

Reviewer: `gpt-6.1-sol`, reasoning `high`, fresh context `fork_turns=none`.
This is the actual configuration, not the proof-checker skill's nominal
Astra/ultra configuration. No cross-family semantic acceptance is claimed.
Applied instruction source:
`F:/c4free-hypercube-main/ARIS/skills/skills-codex/proof-checker/SKILL.md`.
Per the parent assignment, this independent shard records its own audit
artifacts only and does not overwrite global proof or claim ledgers.

## Statement and assumptions

For each marked six-hole Q5 geometry represented by rows 2,7,10,44 of
`t15_analytic_geometry.json`, and every complete-graph matching covering
exactly the other 26 vertices, there is a simple cycle on exactly 30
vertices omitting the two marked majority holes, containing every original
matching edge, whose other edges are cube edges. All cube automorphic
images, including opposite parity orientation, follow by transporting the
entire construction. No restriction is placed on crossing partners or
lengths of original edges.

The only mathematical input beyond elementary graph operations is Q4 N14.
I read its precise statement in `Q4_CORE_AND_A4_SPLIT.md` and independently
checked **all 270270 positive base certificates** (135135 in each of the
two representatives), without importing the author's checker. XOR taking
the omitted hole to 0 makes the other even hole have weight 2 or 4;
coordinate permutation takes it to 3 or 15. These operations preserve the
problem, so the checked representatives prove every N14 application here.

## Dependency and obligation ledger

The acyclic dependency graph is: N14 base certificates + short-edge
geometry -> A cycle/path; balanced positive/negative tables -> direct
bridge or exact B exception; exceptional B witnesses + complement factor
obstruction -> shared optional edge; path expansion or two-cycle splice
-> the stated 30-cycle. No T15 theorem, A4 theorem, eight-hole conclusion,
or P6 conclusion occurs upstream.

| Obligation | Hypothesis discharge and result |
|---|---|
| Geometry | Independently deleted the specified coordinate and normalized both faces by the same permutation. Obtained exactly (x,y,r,s)=(0,1,9,3),(0,1,9,10),(0,1,9,15),(9,11,10,6). The minority is 0 in B; the retained B hole is 7. |
| Crossing count | Each face has 13 original covered vertices. Thus 13-c is nonnegative even: c is odd, 1 through 13. Internal matchings have (13-c)/2 edges. |
| Artificial A matching | X_A and z are disjoint free sets for F_A; their size c+1 is positive even. F_A union D has seven edges and exactly two same-even holes x and the other bridge. N14 omits x. |
| Nonport bridge | Deleting the nonempty matching D from a simple cycle yields disjoint paths. Crossing attachments and the new z bridge have endpoint set X_B union {z_B}. Their path compression R meets F_B only at z_B. Its mate q lies in X_B; F_B's mate k lies outside X_B, so k differs from q. Suppression yields a valid six-edge matching on the twelve vertices outside 0,7,y,z. |
| Occupied bridge | For z_B in X_B and c>=3, d=C inverse(z_B) is a covered A port, different from hole z. Prescribe zd in D; at least one other D edge is deleted. The former endpoints z,d then lie in different path components. Adding z_A z_B joins those components and does not close a cycle. The residual endpoints are exactly X_B minus {z_B}; F_B and their compression have disjoint supports. |
| Preferred table | Preferred geometries (9,1) and (10,11), the latter a coordinate image of (9,11), have zero negative records. This closes every c>=3 and c=1 when r_B is not the unique port. |
| Single-crossing alternate | In the remaining case C={d_A r_B}, s_B is internally covered. The unique D={ds} gives an A path; with crossing and s bridge its compression is rs. Suppression replaces sk by rk. It is invertible because r is covered in L_B. |
| Exact exceptions | Independently transformed full negative lists for (s,y) and inverted the replacement. Counts are exactly 3,1,10,1; all 15 stored B matchings agree, with no duplication or omission per core. No assumption about F_A or d enters this inverse. |
| B optional union | All 101 saved B cycles have exactly the required 14 vertices, contain all six edges of their corresponding F_B, and have only short remaining edges. Their optional unions agree with saved masks and have sizes 17 through 22. Only this certified subset is used. |
| Degree obstruction | On Q4-x remove the certified union U. Independently choose both distinct center-s neighbors, then enumerate every perfect matching of the remaining twelve vertices using allowed short edges. No factor exists in any of the 15 cases. This is exhaustive for degree(s)=2 and degree(v)=1 elsewhere. |
| A optional degrees | With D={dr}, N14 minus dr is a spanning path from d to r on A-x. Its only internally unmatched vertex for F_A is s. Thus H=P minus F_A has degree 2 at s, degree 1 at d and r, and degree 1 at every covered internal vertex. All H edges are short. Hence H intersects U for every permitted A path, without choosing or enumerating F_A. |
| Existential order | First choose any N14 A path, next find uv in H intersect U, finally select the saved B cycle witnessing uv. No assertion that one B cycle realizes the whole union is used. |
| Final splice | P plus d_A r_B and r_A r_B is a simple 16-cycle since d differs from r. It is disjoint from the B 14-cycle, which excludes r_B. Delete the optional uv edge from each cycle and add mirror bridges at u and v: the two paths become one simple 30-cycle. |

## Independent finite checks

The reproducible checker is `T15_BALANCED_BRIDGE_independent_check.py`.
Its output and exact SHA256 input set are in
`T15_BALANCED_BRIDGE_independent_check.json`; the review JSON repeats the
hashes. It imports no author generator or checker.

Each balanced table contains 10395 distinct complete-graph perfect
matchings on the twelve covered vertices. I generate the entire expected
matching set independently by pairing the least remaining vertex with
every other remaining vertex; the partition by its partner proves this
enumeration exhaustive. Every stored mate array is checked as a fixed-point
free involution on exactly that support; equality with the expected set
proves no omitted matching and no repeated matching. All positive cycle
records are checked directly.

For every claimed negative, any optional completion must have degree 2
at free vertices 0 and 7 and degree 1 at each of the twelve covered
vertices. Since 0 and 7 have cube distance 3, they are not adjacent.
Choose their two short neighbors each. The four chosen neighbors must
be distinct; all other eight vertices must form a short perfect matching.
Original matching edges are excluded from the optional edge set. I exhaust
all such choices and check connectivity of their union with F. A spanning
simple 2-regular connected graph is precisely a spanning cycle. Every
candidate union was disconnected. This proves genuine infeasibility,
independently of the author's alternating-path search.

| Avoided pair | Positive | Negative | Disconnected degree completions |
|---|---:|---:|---:|
| 3,1 | 10392 | 3 | 36 |
| 3,4 | 10393 | 2 | 18 |
| 3,8 | 10385 | 10 | 84 |
| 3,11 | 10395 | 0 | 0 |
| 3,13 | 10394 | 1 | 9 |
| 9,1 | 10395 | 0 | 0 |
| 9,2 | 10394 | 1 | 9 |
| 9,8 | 10392 | 3 | 18 |
| 9,11 | 10395 | 0 | 0 |
| 9,14 | 10394 | 1 | 9 |
| 15,1 | 10385 | 10 | 84 |
| 15,8 | 10345 | 50 | 300 |
| 15,11 | 10392 | 3 | 18 |
| Total | 135051 | 84 | 585 |

The six permutations of coordinates 0,1,2 fixing coordinate 3 preserve
the marked pair 0,7. I checked each representative's orbit against the
stored orbit list, verified agreement of negative sets under all repeated
images, and verified that their union is exactly the 49 admissible marked
pairs (t,y). Thus both preferred and alternate table applications are
covered, including transformed complete negative lists.

## Edge preservation, safety, and boundary cases

All original internal long edges are part of a required matching and are
retained. An artificial D edge can be long but is always deleted.
Compressed edges can be long but are always expanded to their paths;
the suppressed edge kq is expanded through original kz and the compressed
path, so original kz is restored. These artificial edges have disjoint
interiors, ensuring simultaneous expansion preserves simplicity.

The first bridge is short because it joins equal local labels. Its A
endpoint is an original hole, so it cannot be an original crossing; its
B endpoint is either internal or is the explicitly treated occupied port.
The occupied-port argument is needed only for c>=3; c=1 is deliberately
handled by alternate bridge and then the spectrum argument. In that final
argument the shared uv is outside F_A and F_B. Its B endpoints exclude r
and y, and its A endpoints exclude x. The new u and v bridges therefore
cannot be the sole original crossing d_A r_B. This remains true when
u=d or v=d; the original crossing is retained while the deleted optional
edge frees exactly the degree needed for the new bridge.

At c=13 the internal matchings are empty but all port-pairing and forest
counts remain valid. At c=1 the root d cannot equal r or s because those
are original holes. The distinguished-edge argument never applies to
the one-edge D case. No empty crossing case is possible. Both parity
orientations and arbitrary crossing bijections are respected throughout.

## Closure and limitations

All obligations of the four-core statement are discharged, including its
previously stated finite inputs and N14 base. Counterexample attempts
included all negative table matchings, both occupied/free mirror statuses,
the c=1 endpoint degrees, maximal c=13, possible reuse of an original
crossing in a new bridge, and union-versus-single-witness quantifiers.
None produced a counterexample or uncovered a missing case.

No theorem statement was modified. No global file was edited. This audit
does not integrate the four cores into an eight-hole parent census, and
does not audit the other T15, EP0, or same-face arguments.
