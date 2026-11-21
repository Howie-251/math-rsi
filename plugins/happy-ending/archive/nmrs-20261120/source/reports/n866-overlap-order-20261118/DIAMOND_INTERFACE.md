<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# Actual shared chronology in an elementary Ferrers diamond

2026-11-18. This note transcribes the explicit general calculation supplied by
`proof_lead`; it is a same-session structural interface, not a new hole row or
independent acceptance of the full866 argument.

Let A be a Ferrers ideal and let x,y be two individually addable incomparable
cells, with x_1<y_1 and x_2>y_2. Write B=A+x, C=A+y and D=A+x+y, and assume
all four actual state owners are occupied in one input. Inclusion fixes A
before B,C and both before D. The one actual order between B and C is shared
by every overlapping local test; it cannot be chosen separately per slice.

If actual B<C, the ordered packet(A,B,C,D) has colors B,B,R,R. Indeed the
successive directed difference labels are x,y,x, and the other one-cell
differences are B→D:y and A→C:y. Strict x-growth forces the first two blue
triples, while strict y-growth forces the final two red triples. If actual
C<B, the ordered packet(A,C,B,D) is R,R,B,B by the same calculation with the
middle owners reversed.

In either order the actual three-point paths A,B,D and A,C,D are respectively
blue and red and have the same two outer owners A,D. This gives an explicit
two-branch calibration of the common O/B-C order atom and actual chronological
triple color semantics used by local_schema.py.

It does **not** show that both coordinates of the last-pair state σ(A,D) are
at least2. That state concerns a fixed terminal pair and is different from
the common outer endpoints of the two paths. The suggested stronger inference
was explicitly withdrawn and is not used in any generated clause or row.

## A common-order 14-corner model at A=1357

This section records the concrete paper construction supplied by the parent
and `proof_lead`. Its checks below are symbolic hand checks; no scientific
program or solver was run for this section. It gives an actual ordered
signotope with one simultaneous system of admissible difference-cell labels.
It does **not** assert an exact terminal-ideal realization of its prescribed
state names, an occupied61-state realization, or a new certified hole row.

Let the common bottom ideal have column heights (3,2,1,0), hence chart name
A=1357. Its four individually addable cells are

$$x_k=(k,5-k),\qquad k=1,2,3,4.$$

For every S contained in [4], prescribe the ideal

$$I_S=A\cup\{x_k:k\in S\}.$$

All16 are ideals: each x_k is already addable to A, and the four new cells
are pairwise incomparable. In the chart name, bit k increments the
(5-k)-th entry of1357. Axis1 is the **lowest** binary bit and axis4 the
highest. Order the owners by the increasing integer

$$n(S)=\sum_{k\in S}2^{k-1}.$$

The selected271-row nine-hole representative is

$$1268,1358,1378,1478,1567,2345,2456,2457,3467.$$

Its intersection with this16-corner cube is exactly the two corners
{1}=1358 and {3,4}=2457. The following table supplies the complete chart
dictionary. The last column gives the highest differing bit from the
previous **retained** owner; it is blank at the first owner and at deletions.

| Binary integer | S | Chart name | Retained? | Previous-pair bit h |
|---:|---|---|---|---:|
|0|empty|1357|yes|—|
|1|{1}|1358|no|—|
|2|{2}|1367|yes|2|
|3|{1,2}|1368|yes|1|
|4|{3}|1457|yes|3|
|5|{1,3}|1458|yes|1|
|6|{2,3}|1467|yes|2|
|7|{1,2,3}|1468|yes|1|
|8|{4}|2357|yes|4|
|9|{1,4}|2358|yes|1|
|10|{2,4}|2367|yes|2|
|11|{1,2,4}|2368|yes|1|
|12|{3,4}|2457|no|—|
|13|{1,3,4}|2458|yes|3|
|14|{2,3,4}|2467|yes|2|
|15|{1,2,3,4}|2468|yes|1|

### One shared pair-label and triple-color rule

For any earlier S and later T, put

$$h(S,T)=\max(S\mathbin\triangle T),\qquad
\sigma(S,T)=x_{h(S,T)}.$$

The highest differing binary bit changes from0 to1, so this is a genuine
choice in I_T minus I_S. It is one fixed choice per pair across all local
slices. The common bottom A cancels from every difference.

For any three chronologically increasing owners S<T<U, write
p=h(S,T), q=h(T,U). Then p and q are distinct. If both were k, the first
pair would require bit k of T to be1 and the second would require it to
be0. Define the actual triple to be blue when p<q and red when p>q.
For a blue triple, the first coordinates of its two shared pair labels
strictly increase. For a red triple, their second coordinates5-p,5-q
strictly increase. Thus every triple meets the required color-growth
condition with these same pair labels.

### Every four-packet is legal

For four owners S<T<U<V, set p=h(S,T), q=h(T,U), r=h(U,V).
For three successive owners the outer-pair level is the maximum of the
two successive levels: the larger changed bit cannot be cancelled by the
smaller change. Consequently

$$h(S,U)=\max(p,q),\qquad h(T,V)=\max(q,r).$$

The maximum of p,q,r occurs only once. Adjacent equality is impossible by
the preceding argument. If p=r were maximal, the middle step at the lower
bit q would leave that maximal bit equal to1 in U, while the last step
would require it to be0 in U, a contradiction.

In packet order (STU,STV,SUV,TUV), the possibilities are therefore:

| Unique largest level | Packet colors |
|---|---|
|p|RRRB or RRRR|
|q|BBRR|
|r|BBBB or RBBB|

For example, when q is largest, the four comparisons are respectively
p<q, p<max(q,r), max(p,q)>r, and q>r. Each displayed packet has at most
one change. This checks all four-subsets, including those spanning many
successive rows of the table, and proves the coloring is an ordered
rank-3 signotope.

### Path bounds and the missing-lowest-corner obstruction

Along a blue path, successive pair levels strictly increase; along a red
path they strictly decrease. There are only four levels, so every
monochromatic path has at most5 vertices. In particular neither blue6 nor
red6 exists, even on the full16-corner cube.

A blue5 would have successive levels exactly1,2,3,4. Its first step
flips bit1 from0 to1 and leaves all higher bits unchanged. At the next
step bit2 must still be0 before it flips; the earlier lower-bit step
cannot change it. Applying the same argument to bits3 and4 shows all
four bits of the initial owner were0. After the first step the owner
is exactly {1}. Hence every blue5 in this construction starts at the
empty corner and has {1} as its second corner. Removing {1} destroys
**all** blue5 paths. This reasoning applies to every retained subfamily
of the cube that omits {1}; removal of {3,4} is not needed for the bound.

For comparison, a red5 must have successive levels4,3,2,1. Once a bit
has been flipped, all later steps change only lower bits, so its last
owner is necessarily [4]. On the stated14-corner domain, both bounds
are attained by the following hand-checkable common-end paths:

* Blue4:1357,1367,1457,2468, with pair levels2,3,4.
* Red5:1357,2357,2458,2467,2468, with pair levels4,3,2,1.

Any pair of same-end blue and red paths has at most4+5=9 vertices when
their two lengths are added. Under the weak8 convention requiring a
length sum at least10, there is no weak8. In particular this is a
genuine14-point signotope satisfying the stronger bounds no blue5 and
no red6, and hence also the ambient blue7/red8 exclusions.

The specified I_S are **admissible ideal labels**, not a claim about
ideals recomputed from all actual longest terminal-pair paths of this
coloring. Such recomputation need not recover the prescribed I_S; no
extension to the other47 occupied owners of a61-state candidate has
been constructed. The example consequently blocks an obstruction based
only on these14 corners, common pair order, directed difference labels,
strict color growth, packets, and the stated same-end path bounds. It
does not certify that the selected nine-hole vector is globally feasible.
