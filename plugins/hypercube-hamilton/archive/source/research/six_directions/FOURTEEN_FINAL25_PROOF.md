# Fourteen-hole final two root-star orbits

Status: frozen producer proof and positive finite evidence, pending fresh independent review. This package proves an extension statement for two exact geometry orbits if its positive certificates are accepted. It does not by itself assemble the full fourteen-hole theorem or P6. The source reduction to the last 25 geometries is a separate dependency, `FOURTEEN_MID_SELECTED_PROOF.md` and its final independent review.

Throughout $Q_6$ has vertices $0,\ldots,63$. Set
$$Z=\{39,43,45,51,53,57\},\quad J_5=\{1,2,4,8,16\},\quad T=\{7,11,13,19,21,25\}.$$
The two representatives have prescribed free root $u=0$ and prescribed covered target $v=31$, and uncovered sets $\{0\}\cup Z\cup W_i$, where
$$W_0=J_5\cup\{14,32\},\qquad W_1=J_5\cup\{32,62\}.$$
For **every** short matching $M$ with either uncovered set, the claim is that $M$ is contained in a Hamilton path from 0 to 31. Each original matching has 25 edges. The proof includes original matchings where target 31 crosses the chosen split; it does not assume target-internal behavior from a maximal extension.

## Exact local B premises

The only new B inputs are five exact marked rows in `FOURTEEN_FINAL25_B_summary.json`: indices 0,1,7 for orbit 0 and indices 100,101 for orbit 1. Each has 22 covered endpoints and one forced complement pair $pq$. Deleting that pair leaves 20 endpoints and a certified square rank-512 matrix. There are 2560 forests and 1310720 connectivity bits altogether. Orbit-0 forest records have 34 bytes; orbit-1 forest records have 36 bytes. Full endpoint pairings have 22 bytes, reduced pairings and columns 20 bytes, and reduced matrix rows 64 bytes.

The mathematical import is the accepted single-cherry complete-matching criterion in `HIGHER_FORCED_CHERRY_TRANSFER.md` / `HIGHER_FORCED_CHERRY_REVIEW.json`, using the complete-graph GF2 connectivity rank $2^{20/2-1}=512$. For any one of these exact inputs, full reduced rank implies that **every complete matching** $F$ on the original 22 endpoints with $pq\notin F$ can be joined to a certified short forest into one cycle. The arbitrary complete matching need not be short or bipartite. If $pq\in F$, the labelled common pair makes a separate cycle, proving the converse. The positive forests and reduced rank are new finite premises, not imported merely because another marked input has the same cardinalities.

The local forest at an internal hole has degree two; at covered endpoints degree one; at omitted holes degree zero. The recorded forced cherry is the unique internal hole with the two indicated remaining cube neighbors. Its short two-edge path forces $pq$ in every endpoint pairing. The certificate can be verified solely from short edges, path components, recorded pairings, every matrix bit, and GF2 elimination. No search exhaustiveness or deficient rank is needed.

## The two A maximal domains

Split along bit 32: $A=\{0,\ldots,31\}$, $B=A+32$, and write $\bar x=x\oplus32$. Put $E=\{x\in A\setminus\{0\}:\operatorname{parity}(x)=0\}$, so $|E|=15$. In orbit 0 the originally covered A odd vertices are
$$O_0=\{7,11,13,19,21,22,25,26,28,31\};$$
in orbit 1 they are all eleven odd vertices of weight at least three, denoted $O_1$. Write $j=1$ in orbit 0 and $j=0$ in orbit 1, so $|O_i|=11-j$, and the original A holes other than 0 are
$$W_A=J_5\cup\{14\}\quad(i=0),\qquad W_A=J_5\quad(i=1).$$

Let $L$ be the actual internal-A submatching of $M$. It covers every vertex of $T$, since their mirrors form $Z$. In orbit 1 it also covers even vertex 30, since $\bar{30}=62$ is an original B hole. Extend $L$ by adding short edges in the graph induced by $E\cup O_i$ until it is inclusion-maximal, giving $L^*$. This extension still covers $T$, and in orbit 1 still covers 30. Every actual $L$ therefore has an extension in the stated finite domain. No extra assumption about other unmatched vertices is imposed.

For every such maximal matching, the supplied A record gives $q,t,w,b$, a positive opening forest $P$ under one common coordinate permutation, and a simultaneous exact B input. The following are the finite positive properties:

- $q$ is an even vertex unmatched by $L^*$; $t\in T$; $w,b$ are distinct units in $J_5$.
- $P$ is a short path forest on $A\setminus\{0,31\}$, degree two at $q,b$ and degree one elsewhere. It has 16 edges, 14 components, and contains the opening edge $qt$.
- If 31 is matched in $L^*$, replace its edge $31h^*$ by $wh^*$; otherwise leave $L^*$ unchanged. Denote the result by $L^{*\prime}$. The labelled union $P+L^{*\prime}$ is acyclic. A common edge is a two-cycle and must fail the component test.
- The simultaneous marked B input, including its forced pair, has one common coordinate map to one of the five new certified inputs.

Only the old case00 and case03 **positive forest** files are used. Their rank 8031 is not a theorem premise; the proof does not require them to enumerate every possible opening forest. The 805006 positive A records are the completeness evidence for the required maximal domain.

## Monotone lift, including the actual target-cross cases

Let $31h$ be the original target matching edge. If it is internal A, remove it and insert the auxiliary edge $wh$ internally in A. If it crosses, then $h=63$; replace it by the auxiliary crossing edge $w63$. These auxiliary edges are allowed to be long. Both have opposite-parity endpoints and will be deleted in the final path construction. Let $L'$ be the resulting internal-A matching. Its covered vertex domain is
$$G'_A=(E\cup O_i)\setminus\{31\}\cup\{w\}.$$
Let $X'$ be this domain's vertices unmatched by $L'$. Their incident original or virtual cross edges are retained as ports.

The submatching inclusion $L'\subseteq L^{*\prime}$ holds in all three cases:

1. If the actual target edge is internal, it is an edge of $L\subseteq L^*$, so the maximal matching uses the same mate $h$. Both modifications replace $31h$ by $wh$.
2. If the actual target edge crosses and 31 is unmatched in $L^*$, then $L'=L$ and $L^{*\prime}=L^*$.
3. If the actual target edge crosses but the maximal extension adds $31h^*$, then $L'=L$; removing the newly added $31h^*$ and adding $wh^*$ keeps every edge of $L$. Thus $L^{*\prime}$ contains $L'$ and the new $wh^*$ may be used as a completion edge.

In particular one must not replace the actual cross edge by the maximal target edge. The actual cross edge becomes $w63$ throughout cases 2 and 3. Vertex 63 is not a unit mirror, not $\bar t$ (because $31\notin T$), and not a mirror of a source in $W_A$. No prescribed boundary port collides with it. In orbit 1 the originally required internal coverage of vertex 30 survives the modification: an actual internal edge at 30 remains, or is changed only from $31\,30$ to $w\,30$; a maximal extension cannot steal an already matched actual 30.

Put $S=W_A\setminus\{w,b\}$, with $|S|=3+j$. In the acyclic graph $P+L^{*\prime}$ all vertices have degree one or two. Let $m^*=|L^*|$. Its endpoint set is
$$Q^*=(X^{*\prime}\setminus\{q\})\cup S,$$
where $X^{*\prime}$ is the set of unmatched vertices in $G'_A$ under $L^{*\prime}$. There are $15-m^*$ even and $11-j-m^*$ odd vertices in $X^{*\prime}$. Removing even $q$ and adding the $3+j$ odd sources gives $14-m^*$ endpoints of each parity. The graph has $14-m^*\ge3$ path components, as $m^*\le11$.

There exists an opposite-parity matching $D^*$ of these endpoints joining all paths into one cycle. To see this directly, the number of even-even paths equals the number of odd-odd paths. Alternate such paths in a ring and insert the mixed-endpoint paths into ring connections. If all paths are mixed, orient and join them directly in a ring. Complete opposite-parity endpoint edges are permitted in this auxiliary construction.

Set
$$D=D^*\cup(L^{*\prime}\setminus L').$$
This is a matching, since endpoints of $D^*$ are unmatched by $L^{*\prime}$ and the added edges are mutually disjoint. Its domain is precisely $(X'\setminus\{q\})\cup S$, with $|D|=14-|L|$. The graph
$$P+L'+D=P+L^{*\prime}+D^*$$
is the same single cycle on all 30 vertices of $A\setminus\{0,31\}$. The vertex $t\in T$ is matched by the actual $L$, so $D$ avoids $t$; it also avoids $q$. The short edge $qt$ is therefore disjoint from $D$. In the third case the auxiliary edge $wh^*$ in $L^{*\prime}\setminus L'$ belongs to $D$ and is deleted in the next step; it is never mistaken for an original matching edge.

## Actual B suppression, local safety and final Hamilton path

Delete all edges of $D$ and the opening edge $qt$ from the A cycle. Keep the original/virtual matching cross edges at every vertex of $X'$ (including $q$). Add the short bridges $s\bar s$ for all $s\in S$ and $t\bar t$. This makes disjoint paths inducing a complete pairing of the resulting B boundary vertices. Vertex $q$ opens its actual cross port; $t$ opens to the original B hole $\bar t$; the sources $S$ were original A holes. All these endpoints are distinct. In actual-target-cross cases the port at $w$ is the virtual edge $w63$; in the target-internal case the auxiliary edge $wh$ remains inside the A paths.

Combine this induced pairing with the original internal-B matching edges. Exactly the vertices $Y=\bar S$ have degree two. Their original B mates exist because $S\cap T=\varnothing$ and their mirrors are not the minority B holes. Every vertex of $Y$ has the same parity, and each original short matching edge incident to $Y$ leaves $Y$. A cycle in the combined graph would require every vertex on it to have degree two, hence to lie in $Y$, which is impossible. Suppression of the degree-two vertices therefore produces a valid complete matching $F_B$ on the 22 vertices outside the new local hole set
$$H_B=M_B^{\mathrm{actual}}\cup(Z\setminus\{\bar t\})\cup Y,$$
where $M_B^{\mathrm{actual}}=\{32\}$ in orbit 0 and $\{32,62\}$ in orbit 1. Original B minority holes remain holes, and the original majority hole $\bar t$ is filled by the extra bridge.

Under the B identification $x\mapsto x\oplus32$, the exact marked input is
$$M_B=\{0\}\ (i=0),\quad M_B=\{0,30\}\ (i=1),$$
$$J_B=(T\setminus\{t\})\cup S,\quad U_B=S,\quad R_B=\{\{w,b\}\}.$$
Its common map is explicitly supplied in `FOURTEEN_FINAL25_checked_options.json`. In orbit 0 it is type 1:9 with four omitted holes; in orbit 1 it is type 2:8 with three omitted holes. Both have 22 covered endpoints. The hole 0 has exactly the two remaining unit neighbors $w,b$, forcing their complement pair.

The actual compressed matching avoids the forced pair. The vertices $\bar w,\bar b$ were originally covered internally in B, since their original cross neighbors $w,b$ were A holes. They are outside $Y$, and their original short internal-B edges have opposite-parity other endpoints also outside $Y$. None is an induced cross boundary endpoint; in particular the virtual cross edge, when present, ends at 63, which is distinct from these unit mirrors. Thus the original short matching edges incident to $\bar w,\bar b$ survive unchanged in $F_B$. Their same-parity endpoints cannot be matched to one another. This proves $\bar w\bar b\notin F_B$ for **every** original matching, including all virtual-cross cases. No unverified mixed-parity obstruction rule is used.

The new local full-rank criterion now gives a short B forest whose union with $F_B$ is a single cycle. Expand the suppressed Y paths and all induced A paths. The result is a single 62-vertex cycle on $Q_6\setminus\{0,31\}$ that contains every edge of the modified original matching, including the actual auxiliary edge $wh$ (internal or virtual crossing). Delete that auxiliary edge. Attach the short edge $0w$ at $w$ and restore the original target matching edge $h31$ at the other end. This gives a Hamilton path from 0 to 31 containing every original edge of $M$.

## Positive finite domain and actual geometry coverage

The exact maximal domains are:

| orbit | size 11 | size 10 | size 9 | size 8 | total |
|---|---:|---:|---:|---:|---:|
| 0 | 0 | 274691 | 17040 | 12 | 291743 |
| 1 | 412439 | 100020 | 804 | 0 | 513263 |

All 805006 records are positive. Domain completeness can be counted independently of the producer DFS: choose the unmatched odd subset $U\subseteq O_i\setminus T$, match every vertex of $O_i\setminus U$ injectively to an even cube neighbor, and require the used-even set to contain $N(U)$ and, in orbit 1, also 30. The neighborhood condition is exactly inclusion maximality; the additional 30 condition is the required internal coverage. A 15-even-vertex mask DP gives the table. Uniqueness, legality, maximality, coverage, the positive DSU witness, and equality of count to the DP establish the universal finite premise. The producer replay checks do not constitute independent acceptance.

A records use the established 32-byte format: sorted original edge pairs in bytes 0..21 padded with 255; size byte 22; $q,t,w,b$ bytes 23..26; opening case byte 27; little-endian forest index bytes 28..29; A permutation index byte 30; target-internal-in-the-maximal-matching flag byte 31. The latter is not an assertion that the arbitrary actual target is internal. Lexicographic coordinate permutations use output bits reading the chosen input bits. The corresponding simultaneous B map appears in the checked options file.

The two orbit representatives have exactly 20 and 5 records in the source `FOURTEEN_MID_SELECTED_remaining_v31_covered.bin`. Source records have 13 bytes, Z6 then W7. The actual-to-representative maps use the first five coordinates and fix coordinate 32, root 0, and target 31. `FOURTEEN_FINAL25_actual_witnesses.bin` has 25 records of 7 bytes `<BIBB>`: target, source index, orbit, permutation. Exact complements `FOURTEEN_FINAL25_remaining_v{1,7,31}_covered.bin` are all empty. This proves only the precise final-subset application conditional on the independently accepted upstream source reduction. A full fourteen-hole assembly must separately verify the entire upstream chain, its free targets, and any predecessor imports before marking the full layer or P6 proved.
