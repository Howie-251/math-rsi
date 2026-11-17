# Two Q6 forced-port cores: independent proof audit

Verdict: **PASS**, same-family / provisional. Both universal Q6 core closures and the exact Q7 parent-domain filter are proved modulo explicit accepted imports.

The declared matching domain is all complete-graph matchings on the cube vertex set with exactly the displayed six holes, including prescribed long and same-parity edges. No P6 assumption is used.

## Proof-obligation ledger

**MC1: Universal matching domain.** All F subset K(Q6) with exactly six specified holes; long and same-parity prescribed edges allowed.

**MC2: Old face transports.** Independent exhaustive coordinate-permutation normalization gives type2 for cuts2,3 of1007 and type4 for cuts4,5 of2189; exact eight edges reconstructed.

**MC3: Universal failure.** For even port count c=0 or c>=4 universal failure forces all8 obstruction edges internally; c=2 forces at least7. A missing edge can be avoided in a complete-graph perfect pairing whenever c>=4.

**MC4: New cut geometry.** Every reconstructed obstruction edge crosses new bit1 or bit3; its B endpoint is an original port if the edge belongs to F.

**MC5: Port counting.** Each Ti has8 points, their intersection4, union12; each misses at most1 actual port, hence union misses at most2. Extra ports are allowed.

**MC6: Usable auxiliary edge.** Three vertex-disjoint candidate pairs lie in W; at most2 absent points cannot hit all3 pairs. All79 missing subsets of size<=2 checked per core.

**MC7: Six exact automorphisms.** Every stated permutation/translation preserves cube adjacency and transports the entire unordered omitted pair, target triple, and7-8 edge jointly. Swapping omitted holes is legitimate.

**MC8: Arbitrary completion D.** Even XB admits an arbitrary complete-graph perfect pairing containing the available candidate edge; FB union D is perfect on B minus U and includes that edge.

**MC9: One-edge local path.** Accepted as an explicit separate import only after fresh kernel PASS and all of its declared input hashes verify.

**MC10: Boundary degree and acyclicity.** Removing D from a30-vertex simple path gives a forest. At either path endpoint that is a port, both cross edge and bridge restore degree2; distinct A attachments preclude cycles.

**MC11: General two-hole closure.** After compression FA union T has precisely opposite-parity holes a and the third unconsumed I vertex. PROOF_PACKAGE Proposition3 at d5 gives a32-vertex spanning path from a to any short neighbor y, because p(y)=p(third I); close by short ay. This general C1 applies to arbitrary long/same-parity pairs; P6 is not assumed.

**MC12: Expansion.** The A cycle uses each compressed pair; expanding gives one simple62-vertex cycle, omitting exactly U, containing every original F edge. Added real edges are short.

**MC13: Exact parent filter.** Independent column-signature classification, complete coordinate orbits180 and60, and every112814 input record checked; retained/deleted outputs byte-for-byte equal producer.

**MC14: Scope.** Counts are ordered labeled hole-record counts, not matching counts; only cores1007,2189 close. Other cores, full Q6 T15, full Q7/P7 remain open.

## Independently reconstructed transports

For each old face, translate its omitted point f to0, delete the old cut bit in increasing coordinate order, then send input coordinate i to p[i]. This reconstructs the accepted type and its complete eight-edge obstruction without trusting producer plans.

| Core | Old cut | f | p | Type | New cut |
|---|---:|---:|---|---:|---:|
| 1007 | 2 | 11 | [1, 0, 2, 3, 4] | 2 | 1 |
| 1007 | 3 | 7 | [1, 0, 2, 3, 4] | 2 | 1 |
| 2189 | 4 | 47 | [1, 2, 3, 0, 4] | 4 | 3 |
| 2189 | 5 | 31 | [1, 2, 3, 0, 4] | 4 | 3 |

Full lifted edges, all port sets, and the six joint automorphisms are stored in the check JSON. Each map was checked on all32x32 vertex pairs for short adjacency. The port-hitting claim was also checked on all79 subsets of W of size0,1,2 for each core.

## Transfer boundary cases and general C1

In B, 30 non-hole vertices give |XB|=30-2|FB|, hence even. At a path endpoint r in XB the unique prescribed path edge is in D; deleting it isolates r, then the original cross edge and the short bridge to its I mirror give degree2. A path of30 vertices cannot join its two endpoints by a single D edge. Attachments XA and the two I vertices are distinct, so adding them as leaves to the path forest creates no cycle. Compression gives disjoint attachment pairs T, not an arbitrary potentially intersecting graph.

The remaining two A holes are a and the unconsumed I vertex, which have opposite parity. Proposition3 supplies the spanning path and the short closing edge as explained in MC11, for arbitrary complete-graph prescribed pairs. The imported same-parity A2 is used only for the old-cut transfer; it is not substituted for this balanced two-hole C1.

The supplementary abstract path check tested every32768 subset of the15 prescribed edges of a30-vertex path as D, including zero ports and either/both endpoints being ports:8192 cases with0 endpoint ports,16384 with1,8192 with2. All have internal B degree2 and exactly two distinct A leaves per component. This supports, and does not replace, the general proof.

## Exact parent-domain filter

Independent coordinate-column signatures classify every valid 2:1 cut; separate full coordinate-orbit sets have sizes180(core1007) and60(core2189). Input uniqueness, vertex parities, and cross non-adjacency preconditions were checked for all112814 records. The independently retained and deleted byte sequences equal both producer outputs exactly.

| Record set | Count | SHA256 |
|---|---:|---|
| Q7_EIGHT_COVERED_AFTER_CORE386.bin | 112814 | de2e817a2fa6069a97c8ccd369fb298c215171f6c49a1292dbf868b4968f396d |
| Q7_EIGHT_COVERED_TWO_FORCED_CORES_REMOVED.bin | 5446 | e3e8ba0e9460b885494605871edc5977abc0433cceca6626393cc3baa47f11cf |
| Q7_EIGHT_COVERED_AFTER_TWO_FORCED_CORES.bin | 107368 | badc4516268353f40e68ec5e2f9b2860688fcf73c213b50ae525333e05d7d566 |

Deleted records split as4776(core1007) plus670(core2189). Remaining records are88132 with a2:1 cut and19236 without; the nonempty residual signatures are85(84068) and1054(4064). These are labeled hole records, not prescribed matching counts.

## Imports, counterexample pass, and scope

Accepted half-layer and old transfer receipts were used as declared imports; all1695 and8 bound input hashes respectively were independently rechecked with zero mismatches. Imported classification matrices were not recomputed. Producer geometry JSONs were treated only as hints, never as proof. The new one-edge matrix is the separate fresh kernel audit responsibility.

New one-edge receipt PASS: True; receipt-bound hashes checked: 6.

Counterexample candidates examined: zero/two/many crossing ports; endpoints as one or two ports; both endpoints in the same D edge; long or same-parity auxiliary pairs; extra unforced ports; two missing ports in different candidate edges; exchanged omitted points; duplicate compressed/prescribed edges; using a same-parity hole theorem for the balanced A face. The degree, attachment, parity, and exact joint transport checks rule these out. No counterexample or open intrinsic proof gap found.

The separate one-edge kernel is accepted here only through its fresh independent PASS receipt and verification of all six declared source hashes. With that dependency discharged, both universal core closures and the parent-filter application are accepted modulo the stated imports.

The conclusion does not close cores85 or1054, complete Q6 T15, full Q7, or P7. No proof, state, frozen source, producer output, or existing review was modified. Only new review artifacts were written.
