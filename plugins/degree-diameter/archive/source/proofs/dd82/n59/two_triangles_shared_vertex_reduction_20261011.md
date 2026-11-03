# Exactly two triangles sharing only one vertex: three necessary templates

## Claim and status

Assume an original legal 59-vertex graph and actual zero-row N15. Suppose its only triangles are $oab$ and $ocd$, sharing only $o$. Then the necessary row and transport parameters reduce to the three templates below. This is a reduction of the whole shared-vertex case, not an exclusion or an actual graph witness.

Dependencies are the fully stated zero-heavy endpoint lemma in `n15_heavy_endpoints_avoid_two_triangles_20261011.md`, the general theorem in `nonzero_support_transport_20261011.md`, and the original-graph four- and five-step trace identities. No N15 condition is imposed on a nonzero row. The new reduction is pending review and formalization.

## First reduction: no extra cross repeats among the four outer vertices

The shared vertex $o$ has two triangles and is adjacent to all other nonzero vertices. Its nonedge repeat budget is two and lies at zero vertices. The endpoint lemma excludes a weight-two zero endpoint, so its nonedge pattern is 11.

For outer vertices belonging to different triangles, for example $a,c$, their sole nonzero common neighbor is $o$. If $B_{ac}>0$, there is an additional, necessarily zero common neighbor $x$. It is not adjacent to $o$, since that would give a further triangle. The two common neighbors $a,c$ give $B_{ox}\ge1$. Zero-endpoint transport gives

$$B_{ox}=(BA)_{ox}\ge B_{oa}A_{ax}+B_{oc}A_{cx}=2.$$

Thus $B_{ox}=2$, contradicting the endpoint lemma at the two-triangle vertex $o$. Hence

$$B_{ac}=B_{ad}=B_{bc}=B_{bd}=0.$$

Each outer vertex therefore has exactly two nonzero support vertices: the center and its mate in the same triangle. Both have weight one and are adjacent. Its remaining row sum four is at zero vertices, so its zero-repeat pattern initially is 22, 211 or 1111. The general zero-support theorem excludes 211: its lone weight-two zero repeat would have to be isolated, but the nonzero support is a weight-one edge and has no independent set of total weight two. Only 22 and 1111 remain.

## Row parameters

For each outer root $r$, let $c_r$ be the weighted edge sum inside its zero repeat support, and let $a_r$ be the weighted edge sum from that zero support to the center and its triangle mate.

For a 22 outer row, the two heavy zero repeats must be paired. Thus

$$c_r=4,\quad a_r=0,\quad s_r=10,\quad e_r=0.$$

For a 1111 outer row, write $c_r\in\{0,1,2\}$ for its number of zero matching edges. The isolated zero repeats each meet exactly one nonzero support vertex. Thus

$$a_r=4-2c_r,\quad s_r=6,\quad e_r=4-c_r.$$

At the center, its two zero repeats either are paired or both are isolated. Put $\alpha=0$ in the first case and $\alpha=2$ in the second. Its four nonzero support vertices have weight one and induce $2K_2$, so

$$s_o=6,\qquad e_o=2+\alpha/2.$$

For each outer vertex $r$, let $x_r$ count the zero repeats of $o$ adjacent to $r$. Then

$$x_r\ge0,\qquad \sum_{r\in\{a,b,c,d\}}x_r=\alpha.$$

Commutation couples these counts to the outer rows. For each triangle pair there is a common nonnegative integer $m$, with

$$a_a=x_a+m_{ab},\quad a_b=x_b+m_{ab},$$
$$a_c=x_c+m_{cd},\quad a_d=x_d+m_{cd}.\tag{1}$$

To verify this, expand $(BA)_{ro}=(BA)_{or}$. Both nonzero-support contributions are one, leaving the equality between the weighted zero repeats of $r$ adjacent to $o$ and $x_r$. Expanding $(BA)_{ab}=(BA)_{ba}$ similarly leaves a common weighted zero-to-mate contribution $m_{ab}$; the $c,d$ pair is identical. These are equalities from the same actual matrix, not freely assigned per-row parameters.

## Trace arithmetic and complete classification of these parameters

There are 54 zero vertices. Let $k$ count the outer 22 rows. Then

$$s=54\cdot10+6+10k+6(4-k)=570+4k.$$

The four-cycle identity with $n=59,T=2$ gives $s\equiv6\pmod8$, hence $k$ is one or three. The trace congruence $\sum_{t(r)>0}e_r+T\equiv4\pmod5$ becomes

$$c_a+c_b+c_c+c_d\equiv e_o+4\pmod5.\tag{2}$$

If $k=3$, let $c$ be the remaining 1111 row's parameter. When $\alpha=0$, (2) requires $12+c\equiv1\pmod5$, impossible for $0\le c\le2$. When $\alpha=2$, (2) forces $c=0$, so this row has $a_r=4$. Its mate is a 22 row with $a=0$. Equation (1) would require $x_r-x_{r'}=4$, impossible because all $x$ together sum to two. Thus $k=1$.

Relabel so that $a$ is the unique 22 row. Then $c_a=4,a_a=0$, and (1) forces $x_a=m_{ab}=0$. Equation (2) says

$$c_b+c_c+c_d\equiv e_o\pmod5.$$

For $\alpha=0$, the sum is exactly two; (1) gives $c_b=2$ and $c_c=c_d$, leaving $c_c=c_d=0$.

For $\alpha=2$, the sum is exactly three. Since $a_b=x_b\le2$, either $c_b=1$ or $c_b=2$. If $c_b=1$, then $x_b=2$ uses the whole central contribution; (1) forces $c_c=c_d=1$. If $c_b=2$, then $x_b=0$, and $c_c+c_d=1$. Exchanging $c,d$ if needed gives $(c_c,c_d)=(0,1)$; equation (1) then forces $(x_c,x_d)=(2,0)$ and $m_{cd}=2$.

The complete necessary parameter list is therefore:

|Template|$\alpha$|$(c_a,c_b,c_c,c_d)$|$(a_a,a_b,a_c,a_d)$|$(x_a,x_b,x_c,x_d)$|$(m_{ab},m_{cd})$|
|---|---:|---|---|---|---|
|I|2|(4,1,1,1)|(0,2,2,2)|(0,2,0,0)|(0,2)|
|II|0|(4,2,0,0)|(0,0,4,4)|(0,0,0,0)|(0,4)|
|III|2|(4,2,0,1)|(0,0,4,2)|(0,0,2,0)|(0,2)|

In every row of this table, $a$ has zero-repeat pattern22 and $b,c,d$ have pattern1111. The classification is proved above and does not depend on the exploratory finite enumeration used to discover it.

## Exact neighborhood interpretation and the remaining obstruction

Every zero vertex is adjacent to at most one of $o,a,b,c,d$. Adjacent nonzero vertices cannot have a zero common neighbor because that would make an additional triangle. Nonadjacent cross-pair outer vertices cannot have a zero common neighbor by the first reduction.

Thus the five private neighborhoods $P_o,P_a,P_b,P_c,P_d$ are pairwise disjoint, with sizes respectively $4,6,6,6,6$. The remaining set has size $59-5-28=26$ and contains only zero vertices with no nonzero neighbors.

For private neighborhoods of adjacent nonzero vertices, the common-neighbor formula gives

$$e(P_o,P_r)=x_r,\qquad e(P_a,P_b)=m_{ab},\qquad e(P_c,P_d)=m_{cd}.$$

For example, a vertex $y\in P_r$ shares with $o$ the nonzero neighbor $r$ and its neighbors in $P_o$, so $B_{oy}=d_{P_o}(y)$. The other equalities follow in the same way. All nonempty blocks specified in the table are matchings: their two relevant nonedge rows have weight at most one at zero vertices, so the same formulas bound each endpoint's block degree by one.

The blocks between private neighborhoods belonging to different triangles, and their incidence with the 26-point remainder, are not resolved by this argument. They must still be realized in one graph together with all zero-row matchings. No contradiction or full graph witness is supplied for any of the three templates. Two disjoint triangles remain a separate, larger case that was not classified in this bounded task.
