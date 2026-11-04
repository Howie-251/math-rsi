# Sixteen-hole root-star positive extension package

Status: producer proof and positive finite certificates, awaiting independent review. This package proves a statement for one exact 30-geometry orbit if its finite certificates are accepted. It does not prove the complete sixteen-hole layer or P6. The surrounding reduction of the full sixteen-hole layer still assumes the complete fourteen-hole theorem.

Let $Q_6$ have vertices $0,\ldots,63$ in binary coordinates. Put
$$Z=\{39,43,45,51,53,57,63\},\qquad W=\{1,2,4,8,14,16,22,32\}.$$
The claim is that every short matching $M$ whose uncovered vertices are exactly $\{0\}\cup Z\cup W$ has a Hamilton path from $0$ to the specified covered vertex $31$, containing every edge of $M$. Coordinate permutations fixing $0$ and $31$ transfer this claim to its orbit. There are 24 matching edges. No assertion concerns only one sampled matching.

## Imports and finite premises

The proof uses the already accepted generic complete-graph matching-connectivity rank theorem, as recorded in `HIGHER_FORCED_CHERRY_TRANSFER.md` and `HIGHER_FORCED_CHERRY_REVIEW.json`. Its local single-cherry criterion says: if all endpoint pairings of certified short path forests contain a forced pair $pq$, and their pairings after deleting $pq$ have full rank $2^{18/2-1}=256$, then every complete matching $F$ on the original 20 endpoints with $pq\notin F$ can be joined to one of these forests to form a single cycle. The columns and $F$ may have arbitrary parity. Necessity follows from the labelled 2-cycle when $pq\in F$. This is a local theorem on complete matchings, not a short-matching restriction.

The new local premises are exactly the three inputs indexed 5, 6, 7 in `SIXTEEN_STAR_B_summary.json`. For each, 256 short forests and a $256\times256$ reduced matrix are supplied. Forest records have 34 bytes (17 short edges), full endpoint pairings 20 bytes, reduced pairings and columns 18 bytes, and matrix rows 32 bytes. The three inputs together contain 768 forests and 196608 matrix bits. The root $0$ is a degree-two internal vertex of each local forest; its two surviving unit neighbors force the listed pair. All degrees, path components, endpoint pairings, matrix entries, and full rank are directly checkable. A deficient search for any other input is not an imported negative result.

The other new finite premise ranges over **every** inclusion-maximal short matching $L^*$ of the bipartite A graph described below that covers $T$. For each such matching, the 32-byte records in `SIXTEEN_STAR_A_full_certificates.bin` give a compatible opening forest and an exact simultaneous B input. The positive forest families are the old case00 and case03 files `TWELVE_ROOT_STAR_OPENING_case_00_forests.bin` and `...case_03_forests.bin`; no rank-8031 or exhaustiveness assertion about those families is used.

## Maximal lift and the A completion

Split along coordinate 32: $A=\{0,\ldots,31\}$ and $B=A+32$. Write $\bar x=x\mathbin\oplus32$. Let
$$T=\bar Z=\{7,11,13,19,21,25,31\},\quad J_5=\{1,2,4,8,16\},\quad W_A=J_5\cup\{14,22\}.$$
The covered A graph is the cube graph induced by the 15 nonzero even vertices $E$ and the nine odd vertices
$$O=\{7,11,13,19,21,25,26,28,31\}.$$
Let $L$ be the actual internal-A edges of $M$. Every vertex of $T$ is covered internally: its cross neighbor lies in $Z$, an original B hole. In particular **the target 31 is always internally matched** in this orbit. Write its actual edge as $31h$. Extend $L$ by adding short edges in this graph until it is inclusion-maximal, obtaining $L^*$. This keeps every edge of $L$, still covers $T$, and has size $m^*\le9$. This is a finite maximal-extension step, not a choice of a new original matching.

The finite record for $L^*$ gives $q,t,w,b$, an A coordinate permutation, and one supplied opening forest $P$. Its checked properties are:

- $q\in E$ is unmatched by $L^*$; $t\in T\setminus\{31\}$; $w,b\in J_5$ are distinct.
- $P$ is a short path forest on $A\setminus\{0,31\}$, with degree 2 at $q,b$ and degree 1 at every other vertex. It contains the short opening edge $qt$. It has 16 edges and 14 path components.
- Replace $31h$ in $L^*$ by $wh$, to obtain $L^{*\prime}$. The **labelled** union $P+L^{*\prime}$ is acyclic. The component DSU must reject coincident edges as cycles of length two; the finite test has that convention.
- The simultaneous marked B input described below maps to one of the three certified local inputs under a single B coordinate permutation.

Since $31h\in L\subseteq L^*$, its mate is the same in both matchings. Set $L'=L-31h+wh$. Thus $L'\subseteq L^{*\prime}$, with no virtual-cross case to assume. Both modified matchings are matchings. The new edge $wh$ may be long, but has opposite-parity endpoints and is handled as a matching edge, not certified as a cube edge.

Let $S=W_A\setminus\{w,b\}$; it has three units and the two vertices 14 and 22. In $P+L^{*\prime}$ all non-endpoint vertices have degree two: $w$ has its new matching edge, $b$ has degree two in $P$, and each matched original covered vertex has one edge of each colour. Its endpoint set is
$$Q^*=(X^{*\prime}\setminus\{q\})\cup S,$$
where $X^{*\prime}$ is the set of unmatched vertices in the modified covered A domain $(E\cup O)\setminus\{31\}\cup\{w\}$. There are $15-m^*$ even vertices in $X^{*\prime}$ and $9-m^*$ odd vertices. Consequently $Q^*$ contains $14-m^*$ vertices of each parity. The acyclic union has exactly $14-m^*\ge5$ path components.

Any path forest with equally many even and odd endpoints admits an opposite-parity endpoint matching $D^*$ joining all its paths into one cycle. For completeness, pair the paths having two even endpoints with the equally many paths having two odd endpoints, alternating these paths in a ring; insert all paths with opposite-parity endpoints at a ring connection. If there are only mixed paths, orient and join them in a ring directly. The endpoint matching edges are allowed to be arbitrary opposite-parity pairs. This proves existence without prescribing an arbitrary $D^*$ in advance.

Define
$$D=D^*\cup(L^{*\prime}\setminus L').$$
It is a matching: $D^*$ meets vertices unmatched by $L^{*\prime}$, and the added edges meet vertices matched only by the extension. Its domain is exactly $(X'\setminus\{q\})\cup S$, where $X'$ is the actual modified covered A domain unmatched by $L'$. Hence $|D|=14-|L|$. Moreover $P+L'+D=P+L^{*\prime}+D^*$ is the same single 30-vertex cycle. The vertex $t$ is already matched by the actual $L$ and is distinct from 31, so no edge of $D$ meets $t$. The edge $qt$ belongs to $P$ and is disjoint from $D$. All original internal-A edges except $31h$ remain.

## Actual B matching and safe forced pair

Delete $D$ and $qt$ from this A cycle. Attach the original matching cross edges at all vertices of $X'$ (including $q$), and add the five short bridges $s\bar s$ for $s\in S$ and the short bridge $t\bar t$. This gives disjoint paths inducing a matching of their B endpoints. The opening at $q$ reconnects its original cross edge; the opening at $t$ uses an original B hole $\bar t$. There is no coincidence between these endpoints: $t$ is internal in the original matching, whereas $X'$ consists of cross ports, and $S$ consists of original A holes. The changed edge $wh$ remains an internal-A matching edge throughout.

Combine the induced B pairing with all original internal-B matching edges. The five vertices $Y=\bar S$ have degree two; the other active vertices have degree one. Each $y\in Y$ was originally covered in B because $S\cap T=\varnothing$. Its original B mate has opposite parity, hence is not in $Y$. Every degree-two vertex is in $Y$, so a cycle entirely inside the degree-two set is impossible. Suppression of these five vertices therefore gives a legitimate complete matching $F_B$ on the 20 vertices outside
$$H_B=\{32\}\cup(Z\setminus\{\bar t\})\cup Y.$$
There is one minority hole, eleven majority holes, and the five omitted vertices are $Y$. This argument covers all actual internal-B edges and all induced long pairs; no shortness is required of $F_B$.

After the identification $B\to A$, the simultaneous marked input is
$$M_B=\{0\},\quad J_B=(T\setminus\{t\})\cup S,\quad U_B=S,\quad R_B=\{\{w,b\}\}.$$
The checked B map sends these three sets and the forced pair together to the listed exact input. Since precisely three of the five unit neighbors of 0 lie in $S$, the two remaining neighbors are $w,b$ and force the complement pair.

The pair endpoints $\bar w,\bar b$ were originally internally covered in B: their cross neighbors $w,b$ were original A holes. They have the same parity as $Y$, and neither belongs to $Y$. Their original short internal-B edges have other endpoints of opposite parity, outside $Y$; those edges remain isolated matching edges under the suppression just described. In particular the actual compressed matching $F_B$ cannot contain $\bar w\bar b$. This is an explicit preservation argument, not a root-not-obstruction assumption and not an inference from deficient rank.

The accepted single-cherry criterion applied to the newly certified exact B input gives a short B forest whose union with $F_B$ is a single cycle. Expand every suppressed Y path and every induced A path. The result is a single 62-vertex cycle on $Q_6\setminus\{0,31\}$, containing the auxiliary edge $wh$ and every other original matching edge. Delete $wh$, attach the short edge $0w$, and restore the original matching edge $h31$. This produces the desired Hamilton path from 0 to 31 containing every original edge of $M$.

## Finite domain, formats and scope

The A finite domain has 120463 distinct maximal matchings covering $T$: 120075 have size 9 and 388 have size 8. The producer provides positive records for all of them. A checker can establish domain completeness without trusting the producer traversal: enumerate the unmatched odd subset $U\subseteq O\setminus T=\{26,28\}$, injectively match every odd vertex in $O\setminus U$ to a neighboring even vertex, and require every vertex of $N(U)$ to be used. This last condition is exactly inclusion maximality. A mask DP on the 15 even vertices counts this domain. The producer performed this additional count, but it remains subject to independent recomputation.

Each A record is 32 bytes: sorted original short edges in bytes 0..21, padding 255; size at 22; $q,t,w,b$ at 23..26; opening case at 27; little-endian forest index at 28..29; A permutation index at 30; target-internal flag at 31 (always 1). Permutation index uses lexicographic permutations of coordinates 0..4 and output bits read the specified input bits. `SIXTEEN_STAR_checked_options.json` supplies a simultaneous B permutation for every formal option. Only B classes 5,6,7 occur in the positive records, with counts 100785,1092,18586.

The 30 actual geometries are certified by `SIXTEEN_STAR_actual_witnesses.bin`, 6-byte records `<BIB>`: target, index in its 15-byte source raw file, and the common five-coordinate permutation taking actual Z and W to the representative. Coordinate 32 is fixed. Exact complementary raw files retain 118 geometries, namely 0/18/100 for targets 1/7/31. This source subset and complement depend only on finite set equality; no remaining matching is claimed unrealizable or extendible. `SIXTEEN_LOCAL_REVIEW.json` is the final accepted source gate for the 148-record input. Full fourteen-hole, full sixteen-hole and P6 are not closed by this package.
