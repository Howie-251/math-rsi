# A degree-two repair for every 23-point minimum-seven input

Let $H$ have 23 vertices and 35 distinct five-element edges. On the 35 original edges define $\Gamma$ by joining distinct edges whose intersection has size other than one.

**Local theorem.** If an original edge $F$ has $q_\Gamma(F)=2$ and all five points of $F$ have degree at least seven in $H$, then $H$ has Property B.

There is no assumption on the degrees of the eighteen points outside $F$. Neither pair-cover, edge-criticality, a bound on point-pair codegrees, nor any bound on the maximum degree is used. Consequently, combining this result with the existing unconditional $q_\Gamma(F)\le1$ repair, every non-Property-B 23-point 35-edge simple five-uniform $H$ of minimum point degree at least seven satisfies

\[
 \delta(\Gamma)\ge3. \tag{1}
\]

This is a reduction for the whole minimum-seven class. It does not prove that the whole class is colorable.

## 1. The actual edge inventory

Fix $F=\{0,1,2,3,4\}$. Its two exceptional neighboring original edges have traces $T_1,T_2\subseteq F$. Each trace is empty or has size two, three, or four. Size one would make that edge nonadjacent in $\Gamma$; size five would make it equal to $F$, contradicting simplicity. The exceptional edges may have equal traces and are always counted as two indexed original edges.

The other 32 original edges meet $F$ in exactly one point. Let $a_i$ count those attached at $i$, and let

\[
 h_i=\mathbf1_{i\in T_1}+\mathbf1_{i\in T_2}.
\]

The exact original point degree is

\[
 d_H(i)=1+a_i+h_i,
 \qquad \sum_i a_i=32,
 \qquad a_i\ge6-h_i. \tag{2}
\]

No realization or sufficiency of this necessary inventory is assumed.

## 2. One actual anchor and one common sample

Choose an anchor $i\in F$, color it red and the other four points of $F$ blue, and choose 11 of the eighteen outside points red. The sample count is $D=\binom{18}{11}=31824$. The original edge $F$ is already proper. A singleton edge attached at the anchor is red-bad in $R=\binom{14}{7}=3432$ samples; every other singleton edge is blue-bad in $B=\binom{14}{11}=364$ samples.

The $a_i$ red singleton edges have distinct external four-sets: equal external four-sets with the same anchor would be equal original edges. The six-set lemma in [SIX_RED_PROOF.md](SIX_RED_PROOF.md) and its extension to more red edges therefore give the valid deduction

\[
 L(a)=
 \begin{cases}
 120\max(a-1,0),&a\le5,\\
 2616+120(a-6),&a\ge6.
 \end{cases} \tag{3}
\]

For $a\le5$, this is a tree deduction. For $a\ge6$, the six-set result is applied to six red events, and the remaining events are attached to their union event in a star. Blue attached edges are retained with their original indices, including any repeated external four-sets attached at different blue points.

An exceptional edge with nonempty trace is already proper if the anchor belongs to its trace. Otherwise its trace is all blue, and the number of bad samples is $\binom{13+|T|}{11}$. An empty-trace exceptional edge can be red or blue; its bad count is

\[
 E_0=\binom{13}{6}+\binom{13}{11}=1794.
\]

Write

\[
 e(T,i)=
 \begin{cases}
 1794,&T=\varnothing,\\
 0,&i\in T,\\
 \binom{13+|T|}{11},&T\ne\varnothing, i\notin T.
 \end{cases}
\]

Thus the number of failed samples for this one anchor is at most

\[
 U_i=a_iR+(32-a_i)B-L(a_i)+e(T_1,i)+e(T_2,i). \tag{4}
\]

If any $U_i<D$, some sample colors every one of the 35 original edges properly. Only one anchor is used to obtain that coloring; bounds from different anchors are not added.

## 3. Nineteen elementary trace types

Set $f(a)=aR+(32-a)B-L(a)$, which is increasing for $a\ge0$. For a fixed exceptional contribution $E$, let $b(E)$ be the least nonnegative integer $a$ such that $f(a)+E\ge D$. If every anchor failed this upper-bound test, (2) and (4) would force

\[
 a_i\ge \max(6-h_i,b(e(T_1,i)+e(T_2,i))). \tag{5}
\]

An unordered pair of traces is determined, up to relabeling of $F$, by $p=|T_1|\le q=|T_2|$ and $r=|T_1\cap T_2|$. Here $p,q\in\{0,2,3,4\}$ and

\[
 \max(0,p+q-5)\le r\le p.
\]

There are exactly 19 possibilities. The following table lists, in sorted order, the five lower bounds in (5). Every row has sum greater than 32, contradicting (2).

| $p$ | $q$ | $r$ | five forced lower bounds on $a_i$ if every anchor fails | sum |
|---:|---:|---:|---|---:|
|0|0|0|7,7,7,7,7|35|
|0|2|0|7,7,7,7,7|35|
|0|3|0|6,6,7,7,7|33|
|0|4|0|6,7,7,7,7|34|
|2|2|0|7,8,8,8,8|39|
|2|2|1|7,7,8,8,8|38|
|2|2|2|7,7,7,8,8|37|
|2|3|0|7,7,8,8,8|38|
|2|3|1|6,7,8,8,8|37|
|2|3|2|6,6,8,8,8|36|
|2|4|1|5,8,8,8,8|37|
|2|4|2|6,8,8,8,8|38|
|3|3|1|7,7,7,7,8|36|
|3|3|2|6,7,7,8,8|36|
|3|3|3|6,6,8,8,8|36|
|3|4|2|5,7,7,8,8|35|
|3|4|3|6,7,8,8,8|37|
|4|4|3|5,5,8,8,8|34|
|4|4|4|6,8,8,8,8|38|

For example $f(6)=27440$ and $f(7)=30388$. A blue three-trace contributes 4368, so an anchor with $a_i=6$ has at most $27440+4368=31808<D$ failed samples. A blue two-trace contributes 1365; with $a_i=7$ it gives 31753. The table is obtained by the same integer substitutions, not by enumerating hypergraphs or outside-set layouts.

All trace possibilities and actual degree possibilities have now been covered, proving the local theorem and (1).

## 4. Evidence and scope

[SIX_RED_CHECK.py](SIX_RED_CHECK.py) checks 36 feasible three-set Venn parameter rows, all 141 rank-at-most-two heavy graphs, and every scalar case in the analytic six-set proof. Its [receipt](SIX_RED_CHECK.json) is PASS. The separate full written read-through [SIX_RED_REVIEW.md](SIX_RED_REVIEW.md) reports no gap and is labeled same-family/provisional.

[Q2_THRESHOLD_CHECK.py](Q2_THRESHOLD_CHECK.py) regenerates this19-row threshold table directly from sizes and intersections. [Q2_INDEPENDENT.py](Q2_INDEPENDENT.py) independently checks all 351 unordered labeled trace pairs and all 150315 necessary singleton-count compositions without taking the $S_5$ quotient or importing the discovery table. All are strict; maximum31808/31824 and minimum guaranteed success count 16, CPU0.164275 seconds. The independent program uses the proven six-set deduction, and independently reconstructs the binomial counts and actual inventory constraints. It is an arithmetic coverage check, not an independent proof of the six-set lemma or a classification of actual $H$.

The only imported coloring statement is the unconditional $q\le1$ theorem in [the existing23-point repair](../twentythree_low_nonunit_degree_20261020/PROOF.md). The new $q=2$ result is self-contained apart from the analytic six-set lemma in this directory. It does not use the 21-point $\Gamma$-degree or codegree gates. The degree-at-least-seven hypothesis on the five points of $F$ remains part of the new statement; the present bounds do not remove it. No Lean, new locking layout, whole-hypergraph enumeration, or cross-family acceptance is claimed.
