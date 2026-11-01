# High three-core 888: complete bounded diagnostic

The complete 888 high-three-core domain has 36 labeled inventories. Its three-lock permutation bounds are strict on 27. For the other nine inventories, adjoining the **same original H's** six-degree point gives 298 necessary four-lock inputs; 279 are strict and 19 remain nonstrict. An independent second domain representation and all fixed-witness original-index arithmetic passed.

Consequently 32 of the 36 complete labeled three-core inventory classes are fully repaired. The two surviving shapes, up to permuting the three eight-degree points, are

\[
 (q;c_{12},c_{13},c_{23})=(2;2,2,2),\qquad(2;2,2,3).
\]

Their surviving actual six-star data comprise nineteen labeled inputs, nine \(S_3\)-orbits. This does not prove that every 888 high core is repairable or realizable, and it does not cover 889/899/999 cores.

## 1. Actual hypotheses and caller

Let H have 21 vertices, 35 distinct five-element edges, and cover every point pair. Work in the reduced A1 role: one six-degree point x, one seven-degree point p, nine eight-degree points (four with codegree two from x and five with codegree one), and ten nine-degree points unit with x. The previously proved strong-pair cases give the non-B necessary condition \(\lambda\le4\); its exact ranges are recorded in §2 of `../high_edge_intersection_repair_20261020/REPORT.md`. If H violates one of those restrictions, the corresponding existing gate already colors H.

Select **actual distinct eight-degree vertices** \(v_1,v_2,v_3\) for which

\[
 q=I_{123}=|\{e\in H:\{v_1,v_2,v_3\}\subseteq e\}|\ge2.
\]

Thus at least two different original edges contain the common triple. Merely having one original edge through three points is not this caller. Write \(a=\lambda_{12},b=\lambda_{13},c=\lambda_{23}\). Necessarily \(2\le a,b,c\le4\) and \(2\le q\le\min(a,b,c)\).

The exact traces on these three labeled vertices are uniquely

\[
 \mu_7=q,\quad\mu_3=a-q,\quad\mu_5=b-q,\quad\mu_6=c-q,
\]
\[
 \mu_1=8-a-b+q,\quad\mu_2=8-a-c+q,\quad\mu_4=8-b-c+q,
 \quad\mu_0=11+a+b+c-q.
\]

Masks are binary subsets of the three locks, not subset cardinalities. Enumerating the three inclusive codegrees and q yields exactly 36 nonnegative labeled inventories. Every actual selected triple has one of them. Their row-excess restrictions add no missing choices: a core point sees only two core partners, each of codegree at most four, so their partial excess is at most six, below its full row budget twelve.

## 2. Original permutation criterion and complete three-lock result

The calculation uses the established original-H permutation bound. Each saved witness fixes the actual lock labels in distinct positions of a uniform permutation and uniformly permutes all other vertices. At each pivot position it takes the minimum of the A/B/C event bounds, with actual same-index diagonal terms removed and the nested link/pure-link deduction subtracted from C. If the sum is below one, some such permutation gives a proper coloring of this same H.

For center i the total quota is \(\lceil(4d_i-20)/3\rceil\); the pure quota with s locks is \(\max(0,\lceil(4\mu_{\{i\}}-(21-s))/3\rceil)\). Pure slots are reserved before the remainder of the total quota is allocated, so these two deductions are not added twice. This task changes none of that existing proof or quota mechanism.

`PILOT.py` uses `SubsetEngine` to find lock positions, and independently verifies the stored A/B/C values. All 36 three-lock inventories are present in `PILOT.json`; 27 are strict, with strict maximum \(1803/1870<1\). The nine nonstrict source ids and parameters are:

|source ids|q|codegrees, up to reordering|three-lock bound|
|---|---:|---|---:|
|0|2|222|\(2001/1870\)|
|1,3,9|2|223|\(951/935\)|
|4,10,12|2|233|\(440059/437580\)|
|13|2|333|\(190/187\)|
|14|3|333|\(24433/24310\)|

## 3. Same-H six-star extension: full domain, not independent slot choices

The point x is distinct from all three selected locks. Let \(\ell_i=\lambda(x,v_i)\in\{1,2\}\), keeping all eight labeled role patterns. For every original three-lock trace T, define \(h_T\) to be the number of its original edge indices also containing x. These actual counts satisfy

\[
 0\le h_T\le\mu_T,\quad \sum_{T\subseteq[3]}h_T=6,
 \quad\sum_{T\ni i}h_T=\ell_i.
\]

All these constraints are enforced together. The first generator chooses the nonempty \(h_T\) recursively and recovers \(h_0\). Thus it does not combine unrelated individual star choices. No block can contain a selected point twice, because traces are sets; each selected block has size at most three. This imposes no partition assumption on all twenty outside vertices.

With x as the new bit zero and the former locks shifted left one bit, the exact four-lock inventory is

\[
 \nu_{2T+1}=h_T,\qquad\nu_{2T}=\mu_T-h_T.
\]

It keeps all 35 original edge indices, preserves their traces, and gives degree vector (6,8,8,8). In particular it automatically preserves all three x-codegrees, the original inclusive core counts, and edge-size feasibility.

For the nine nonstrict raw inventories, the complete h domains have respective sizes 17,27,27,41,27,41,41,60,17, totaling **298**. Every actual H in one of those inventories induces one of these h inputs. `EXTENDED.json` contains all 298 with their own inventory and own fixed positions. Its strict maximum is \(2203/2210<1\), and its full maximum (including honest nonstrict entries) is \(232/221>1\).

All extensions of raw source ids 4,10,12,13,14 are strict. Hence these five labeled core classes, together with the original 27 strict classes, give 32 complete classes. In particular, every q≥3 888 core is covered, as is every q=2 core whose pair-codegree multiset is not 222 or 223.

## 4. Exact surviving boundary

`RESIDUALS.json` records all nineteen residual keys and their complete nine \(S_3\)-orbits. The table gives one representative per orbit. The vector h is ordered by mask 0,1,2,3,4,5,6,7; each representative retains its own lock positions in the JSON.

|extended id|core codegrees, q=2|x-margins|h vector|bound|orbit size|
|---:|---|---|---|---:|---:|
|0|222|111|5,0,0,0,0,0,0,1|\(12227/12155\)|1|
|1|222|111|3,1,1,0,1,0,0,0|\(232/221\)|1|
|3|222|112|2,1,1,0,2,0,0,0|\(1134/1105\)|3|
|7|222|122|1,1,2,0,2,0,0,0|\(109858/109395\)|3|
|15|222|222|2,1,1,0,1,0,0,1|\(25227/24310\)|1|
|16|222|222|0,2,2,0,2,0,0,0|\(2299/2210\)|1|
|18|223|111|4,1,0,0,0,0,1,0|\(12214/12155\)|3|
|30|223|211|4,1,0,0,0,0,0,1|\(12214/12155\)|3|
|32|223|211|2,2,1,0,1,0,0,0|\(109723/109395\)|3|

Thus, in a non-B reduced-A1 H, **every** actual 888 triple with q≥2 must have one of these surviving core/star patterns, transported by the same permutation of the three eight-degree labels. This is a necessary local structure, not a list of non-B hypergraphs. The finite caller coverage uses the full labeled 36/298 lists; the nine-orbit compression is only a readable representation and is not used to omit labeled cases.

None of these nineteen has \(h_7\ge2\). Therefore the previously proved repair for a four-intersection kernel containing x does not directly remove one merely by observing this selected core.

## 5. Low three-core x+B+B diagnostic

For an actual common triple x,b1,b2 lying in at least two edges, the A1 x-codegrees force q=2 and \(\lambda(x,b_i)=2\). The remaining codegree \(c=\lambda(b_1,b_2)\) is 2,3,or4. The complete three-lock inventories have degree vector (6,8,8), and their exact optimized bounds are respectively

\[
 c=2:\ 1957/1870,\qquad
 c=3:\ 12196/12155,\qquad
 c=4:\ 4621/4862<1.
\]

Hence the c=4 actual subcase is repaired by this three-lock witness. The c=2,3 cases remain at this diagnostic level. No further free point was added.

## 6. Independent domain and fixed-witness replay

`VERIFY.py` imports neither the DP engine nor either generation script. It constructs the three-lock domain using q plus the **exact residual pair-trace slots**, rather than inclusive codegrees; all 36 full keys equal the saved domain. For the six-star domain, it partitions the labeled 1/2 occurrences of the three core points into actual center-edge blocks, disallowing repeated copies of a point in one block, and recovers the empty center blocks. Its 298 complete (source,role,h) keys equal the recursive h-domain exactly.

For all 36+3+298=337 saved profiles, the verifier expands the inventory into 35 original-index trace stubs, independently recomputes all 21 A/B/C rows, recomputes the nested quota deductions, and checks the saved fractions. Thus it checks 7077 independent position rows, including all nineteen honestly nonstrict results. Actual result: PASS, `VERIFY.json`.

The recorded CPU intervals were 0.620 seconds for the complete raw domain and low diagnostic, 4.682 seconds for all 298 DP extensions, and 4.412 seconds for the independent domain/fixed replay: total approximately **9.713 CPU seconds**. There was no remaining budget for a meaningful additional 889/899/999 pilot, and none was run.

Reproduction, without rerunning position optimization:

```sh
.tools/math-python/bin/python context/propertyb35-paper/round01/middle/high_three_core_generic_20261020/VERIFY.py
```

The scripts and JSON are bounded trace-inventory evidence; no H, free-point layout, or negative-edge family was enumerated. No Lean, MCP, wiki or navigation change was made. This task has no new cross-family review. A full generic high-three-core theorem remains unproved, so no new canonical complete-branch theorem is asserted.
