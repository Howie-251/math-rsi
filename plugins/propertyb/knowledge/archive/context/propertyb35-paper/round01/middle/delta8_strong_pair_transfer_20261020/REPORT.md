# Delta-eight strong-pair transfer: complete bounded pilot and precise residuals

The complete requested bounded calculation is finished. The original fifteen degree spectra project to twenty selected degree-pair types and one hundred degree-pair/codegree inputs. The two old double-lock layouts give ninety-six strict certificates. Exactly four inputs remain, all with codegree five. A genuine exterior degree-eight point with triple inclusion zero exists for each of those four inputs. Its complete necessary three-lock domain has sixty-four inputs after using the already strict eight/high double-lock gates. The fixed eight old three-lock layouts close forty and leave twenty-four nonstrict inputs, all listed below. No further layouts or larger domains were searched.

This is a partial strong-pair gate. It does **not** establish all pointpair codegrees at most four in every delta-eight case and does not close the delta-eight coloring branch or the full36 problem.

## 1. Exact original input and the fifteen degree spectra

Let H consist of35 distinct five-element edges on21 vertices, cover every point pair, and have minimum degree at least eight. Write b for its number of degree-eight vertices and

\[
e=\sum_v(d(v)-9)_+.
\]

The total degree175 gives b=14+e. There are7-e degree-at-least-nine points, so e<=6; the positive excess partition of e has length at most7-e. The complete degree spectra are the fifteen listed in the existing input `../min_degree_eight_singleton_star_20261020/CONDITIONAL_SCALAR_RESULT.json`:

|Source ID|e|Positive excess partition|Exact degree multiset|
|---:|---:|---|---|
|0|0|empty|8^14,9^7|
|1|1|1|8^15,9^5,10|
|2|2|1+1|8^16,9^3,10^2|
|3|2|2|8^16,9^4,11|
|4|3|1+1+1|8^17,9,10^3|
|5|3|1+2|8^17,9^2,10,11|
|6|3|3|8^17,9^3,12|
|7|4|1+1+2|8^18,10^2,11|
|8|4|1+3|8^18,9,10,12|
|9|4|2+2|8^18,9,11^2|
|10|4|4|8^18,9^2,13|
|11|5|1+4|8^19,10,13|
|12|5|2+3|8^19,11,12|
|13|5|5|8^19,9,14|
|14|6|6|8^20,15|

Only the exact degree lists are read from that file. Its conditional scalar assumptions about lambda, C3 or Gamma minimum degree are **not** imported here; none is needed for the local permutation calculations below.

For every actual selected pair u,v, sort its degree labels as d_u<=d_v. The pair may occur only if the exact source spectrum has the required degree multiplicities, including two actual copies when the degrees are equal. `PAIRS.py` obtains all such pairs from combinations of the twenty-one actual degree entries, then generates every codegree

\[
5\le c\le\min(d_u,d_v).
\]

The union has twenty degree-pair types and one hundred distinct (d_u,d_v,c) keys. Each key records **all** source spectrum IDs containing it. The independent verifier instead uses degree multiplicity counters and a separate Cartesian construction; its complete keys and source-ID sets agree exactly.

## 2. Complete fixed double-lock calculation

For an actual pair with codegree c, its exact thirty-five original edge traces are recovered by

\[
\mu_0=35-d_u-d_v+c,\quad \mu_1=d_u-c,\quad
\mu_2=d_v-c,\quad \mu_3=c.
\]

Only the two previously used layouts (10,21) and (21,10) are tested. All quotas are zero. The cheap primary count uses the integer factorial-scaled conditional permutation arithmetic; it does not call a position solver, LP or layout grid. The first full profile used0.030541 CPU seconds, below the requested initial ten-second cutoff. It completed the entire one-hundred-key domain, so no partial-prefix extrapolation is involved.

Ninety-six keys are strict. The complete nonstrict list is:

|Source ID|e|Selected degrees|c|Best of the two fixed bounds|
|---:|---:|---|---:|---|
|8|4|10,12|5|232491/230945|
|9|4|11,11|5|232722/230945|
|11|5|10,13|5|221843/218790|
|12|5|11,12|5|235046/230945|

Every selected input with c>=6 is strict. In particular the new source13 pairs involving degree fourteen and the source14 degree-eight/degree-fifteen pairs are all strict; it would be incorrect to treat e5/6 as an untested continuation of the old degree<=13 table. All codegree>=5 pairs in source spectra other than8,9,11,12 are already excluded in a non-B H by these fixed certificates. This conclusion is only a codegree gate, not a coloring theorem for those whole spectra when all codegrees are small.

## 3. An actual exterior degree-eight point with no triple inclusion

Consider one of the four remaining actual pairs u,v, with lambda(u,v)=5. Their five common original edges each contain only three other points. Their union outside{u,v} contains at most fifteen vertices.

Neither u nor v has degree eight. Sources8,9 have b=18 degree-eight points; sources11,12 have b=19. Therefore at least b-15>=3 degree-eight points are outside all five uv edges. Choose one such actual point z. It satisfies

\[
d(z)=8,\qquad I(z,u,v)=0.
\]

This is a direct union-size argument. It does not assert that every edge through z meets{u,v}, and it does not apply the clean-singleton-star lemma outside its “every edge meets F” hypothesis.

Put p=lambda(z,u), q=lambda(z,v). Pair coverage gives p,q>=1. Since no z edge contains both u and v, p+q<=8. If p>=5, its selected degree pair is (8,d_u), one of the **already strict** keys from Section2; that alone colors H. The same applies when q>=5. Thus under the non-B assumption it is valid, without any global lambda assumption, to impose

\[
1\le p,q\le4.
\]

This uses strict pair certificates independent of the four unresolved high/high inputs, so it is not circular.

Label (z,u,v) by bits0,1,2. Their exact three-lock inventory is uniquely

\[
\begin{aligned}
\mu_7&=0,&\mu_3&=p,&\mu_5&=q,&\mu_6&=5,\\
\mu_1&=8-p-q,&\mu_2&=d_u-5-p,&
\mu_4&=d_v-5-q,&\mu_0&=32-d_u-d_v+p+q.
\end{aligned}
\]

It has thirty-five original indices, selected degrees exactly(8,d_u,d_v), pair inclusions(p,q,5), and triple inclusion zero. All sixteen choices p,q=1,...,4 are nonnegative for each of the four high pairs. Thus the complete actual necessary domain is sixteen inventories per source, sixty-four in total. It is a necessary domain and makes no full-H realizability claim.

The alternate independent domain construction starts directly from the four unresolved pair keys and p,q in1,...,4, checks b>3c in every applicable source spectrum, verifies every required (8,d),codegree5...8 exclusion against the already strict pair keys, and rebuilds all sixty-four exact trace-count vectors. The complete key sets and every count match the primary domain.

## 4. Single-case pilot and fixed eight-layout result

The layout menu was fixed before the first case, using four old profiles and their reflections in positions1,...,21:

\[
\begin{split}
&(1,11,12),\ (1,21,9),\ (10,11,21),\ (11,1,21),\\
&(11,21,1),\ (12,11,1),\ (21,1,13),\ (21,11,10).
\end{split}
\]

Coordinates are always(z,u,v). The first actual inventory was high pair(10,12), p=q=1. Its pilot bound was566609/583440<1. `TRIPLE_PILOT.json` saves its full input, all eight fixed values and the selected certificate. Only after that cheap first-case result was the same menu applied to the complete sixty-four-input domain. This used0.079908 CPU seconds. It produced forty strict certificates and the following twenty-four nonstrict inputs; no additional positions were tried after seeing these failures.

|High pair|p|q|Best fixed bound|
|---|---:|---:|---|
|10,12|1|2|25213/24310|
|10,12|1|3|343/340|
|10,12|2|3|4945/4862|
|10,12|3|4|2211/2210|
|10,13|1|2|898357/875160|
|10,13|1|3|22234/21879|
|10,13|2|3|7489/7293|
|10,13|3|4|14701/14586|
|11,11|1|1|21992/21879|
|11,11|1|2|25213/24310|
|11,11|1|3|343/340|
|11,11|2|2|4893/4862|
|11,11|2|3|4945/4862|
|11,11|3|3|110204/109395|
|11,11|3|4|2211/2210|
|11,12|1|1|17701/17680|
|11,12|1|2|25499/24310|
|11,12|1|3|347/340|
|11,12|2|2|3071/3060|
|11,12|2|3|25011/24310|
|11,12|2|4|12226/12155|
|11,12|3|3|48849/48620|
|11,12|3|4|2237/2210|
|11,12|4|4|5177/5148|

These are failures of the specified sufficient upper bound, not noncolorable hypergraphs, realized examples, or a proof that no other available certificate works. The equal-degree(11,11) input retains both ordered attachment coordinates as generated; no new symmetry-transport or extra-layout pass is silently included in the forty strict count.

## 5. Independent actual35-index replay and artifacts

`VERIFY.py` independently reconstructs the two complete domains as described above. For **every** one of the one-hundred double-lock and sixty-four triple-lock inputs, including the nonstrict ones, it expands the trace multiset to thirty-five different original-edge indices. It computes the chosen fixed certificate with `computations/independent_structure_bounds.py`, using falling-factorial injection arithmetic on all1190 ordered distinct pairs and all21 pivot positions. Every best bound matches the primary integer-factorial arithmetic exactly, and its strict/nonstrict status agrees. This covers3444 actual rows.

The ninety-six accepted double-lock certificates and forty accepted triple-lock certificates are stored in `VERIFY_RESULT.json`, with their actual35 masks, chosen positions, zero quota and every A/B/C row. Each bound is interpreted through the existing conditional permutation-to-original-coloring lemma. Neither implementation assumes that free points have degree eight; their actual H identities remain free in the common conditional sample.

The independent run completed with status PASS in2.144018 CPU seconds. Including both primary profiles and the small repeated pair profile when importing its arithmetic helper, the complete task used under three CPU seconds, well below the twenty-CPU-second budget. No Lean, LP, new position solver, large layout grid, whole-H search or broad star enumeration was run.

Files:

- `PAIR_RESULT.json`: the fifteen exact source spectra, all one-hundred actual selected-pair inputs, source-ID coverage, both fixed values and all four nonstrict pair keys.
- `TRIPLE_PILOT.json`: the first-case bounded pilot.
- `TRIPLE_RESULT.json`: all sixty-four exact actual inventories, eight fixed values each, forty strict and twenty-four nonstrict.
- `VERIFY_RESULT.json`: independent full-domain agreement, all164 best-bound replays,3444 rows and136 accepted fixed certificates.
- `PAIRS.py`, `TRIPLES.py`, `VERIFY.py`: reproducible bounded computations.

Reproduction:

```sh
python3 context/propertyb35-paper/round01/middle/delta8_strong_pair_transfer_20261020/PAIRS.py
python3 context/propertyb35-paper/round01/middle/delta8_strong_pair_transfer_20261020/TRIPLES.py
python3 context/propertyb35-paper/round01/middle/delta8_strong_pair_transfer_20261020/VERIFY.py
```

No formal manuscript, frozen q4 source, wiki navigation or other branch was edited. The remaining mathematical question is whether the common actual pool of at least three or four clean exterior eight-degree points forces one of the forty strict local types, or whether an independently justified stronger local argument closes the twenty-four explicit inputs. This task stops at the requested precise bounded result and leaves that question open.
