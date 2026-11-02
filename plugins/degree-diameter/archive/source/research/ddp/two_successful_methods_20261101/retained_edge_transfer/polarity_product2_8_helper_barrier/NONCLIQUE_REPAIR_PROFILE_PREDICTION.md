# Prediction: exact q2 repair classes constrain the next nonclique controller

2026-11-01, before independent attack. Fixed interface: the saved literal
15-vertex q2 relation in factor_radius2_support_once.py, a genuine585-point
q8 polarity factor, r4 original-neighborhood copies of all325 product
absolute classes, cap31, all mandatory edges retained, arbitrary added
free-peer edges. This is a conditional new controller study, not a new graph.
The32-subset experiment already gives the exact q2 repair-class profile.

For helper h let p_h be its number of actual F pins and d_h its helper
degree. In each B-absolute column b, let T_b be the distinct A rows among
its pins and t_b=|T_b|. The hard targets X in that column are the ten
nonabsolute A vertices times b. A mandatory two-step old suffix can cover
only the union of q2 supports of T_b; no other B column reaches b in two
factor steps. The exact additional A based classes required by the missed
targets are g(t)=5,4,1,0,0,0 for t0..5. Their mandatory direct target pairs
partition all ten vertices, so each required class really needs an F-peer
or neighboring helper pin in that column. Since g(t)>=5-2t, predict

    325 <= 6 p_h + sum_{g adjacent h} p_g.                 (1)

Repeated pin copies do not improve the own support, and distinct own class
count<=p_h. Each own pin has at most four free peers after its helper edge.
Choosing a minimum-helper-degree vertex d gives p_h,p_g<=31-d, hence

    325 <= (d+6)(31-d), so d must be in9..16.              (2)

This is a restriction on any successful helper controller in this fixed
model, not an exclusion of cap31. It is new use of the exact repair profile,
not a new discovery of the old585 Steiner data.

## One specific nonclique alternative: balanced complete bipartite helpers

Test H=K_(t,t),1<=t<=31, without assuming uniform/disjoint pins. Put p=31-t.
For h in the left part, all left pins are reachable in three helper/pin
steps, right pins in two, and right-pin free peers in three. Its own pins
also allow one/two free peers and same-class mandatory suffixes. Therefore

    |B3(h) intersect F| <= (6t+24)p.

Indeed left pins<=tp, right pins plus peers<=5tp, own one-peer extras<=4p,
two-peer extras<=16p and same-class extras<=4p. F has1625 vertices, so only
t8..19 can survive this bound. Then12<=p<=23.

Let S_h be the unowned based classes whose ENTIRE26-element old-U neighbor
set is covered by h's own pins with an old suffix of length<=2. Any such
class(a,b) requires at least8 distinct pins in A row a (cover its eight
A-absolute/B-nonabsolute targets), and at least2 distinct pins in B column b
(cover the two A-nonabsolute/B-absolute targets; each other A absolute
two-support hits only one of that pair). These projection conditions are
only necessary, so ignoring their remaining compatibility is safe.

Call an A row heavy at eight pins. At p<=23 there are at most two heavy rows.
With one heavy row, each saved unowned class needs two pins outside it in
its own column: |S_h|<=floor((p-8)/2). With two heavy rows, at least16 pins
are in them. In a column containing no heavy-row pin, at most two heavy-row
classes can be saved and this needs at least two nonheavy pins; with one
heavy-row pin at most one class can be saved and needs a nonheavy pin; with
two heavy-row pins no unowned heavy-row class remains. Hence |S_h|<=p-16.
With no heavy row it is zero. Thus predict the universal upper bound

    |S_h| <= C(p)=max(0,floor((p-8)/2),p-16).             (3)

Write A,B for the unions of based classes pinned by the left/right
helpers, a=|A|,b=|B|,i=|A intersect B|. Each h on the left must have all325
old neighbor classes covered either by right-helper pins, its own pins,
its own at most4p free peers, or S_h. Summing over both helper parts and
charging a class in A intersect B at least once on each side gives

    2t*325 <= t(a+b) + 2t(5p+C(p)) - 2i.

Here a+b<=2tp and i>=max(0,a+b-325). On t8..19,2tp>=325; the right-side
bound is increasing in a+b because t>=2. Thus it is necessary that

    (t-1)*325 <= t*((t+3)*p+C(p)).                        (4)

Predict that no t8..19 satisfies(4), closing balanced K_(t,t) at cap31,
even with arbitrary F-peer edges. This would exclude one concrete proposed
replacement for the already excluded clique, not arbitrary noncliques,
unbalanced bipartite helpers, changed sources or rewiring.

Independent paper attack plus one tiny scalar sweep t1..31/d0..31<=2CPU
should check(1), the exact q2 pair geometry, (3), all route types and the
set-union/intersection summation. No actual585 table recomputation, source
8775 generation, BFS, solver, Lean, paid review or new search queue.
If supported, the next controller must satisfy min degree9..16 and cannot
be a clique or balanced complete bipartite graph; use saved actual block
data to specify a new connection rule before any search. If refuted, save
the precise missing route or counting counterexample and do not apply it.
