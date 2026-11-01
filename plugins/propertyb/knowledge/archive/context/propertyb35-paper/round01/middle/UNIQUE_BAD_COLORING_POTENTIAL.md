# Unique bad balanced colorings: actual blocker identities and the potential obstruction

This pilot gives an exact same-blocker formulation and a degree-sensitive bound. It does not close the22- or23-vertex branches. In particular, simply minimizing the degree sum of the unique bad edge supplies no automatic contradiction; it only restricts transitions whose target still has exactly one bad edge. No old19-point aggregate-moment LP was rerun.

## 1. Existence and number of unique-bad states

For n in {22,23,24}, take all labelled balanced colorings, with red size r=floor(n/2) and blue size b=n-r. A fixed five-edge is monochromatic with probability

    [binom(n-5,r-5)+binom(n-5,r)] / binom(n,r).

For35 edges the expected number f of monochromatic edges is70/57 when n=22, and30/23 when n=23 or24. These are strictly below two. Under a non-Property-B assumption every balanced state has f>=1, so a state with f=1 exists. More quantitatively the proportion of unique-bad states is at least2-Ef, namely44/57 or16/23, respectively. This remains useful global information; selecting only one potential-minimal state discards this counting lower bound unless a further argument reconnects it.

Fix one unique-bad balanced coloring and interchange color names if necessary so that its unique bad edge e is red. In the odd case r may now denote either11 or12. Write R,B for its actual color classes, |R|=r, |B|=b.

## 2. The same actual critical edges control every swap

For each blue y define

    A_y = {g in H : g intersect B = {y}},

and for each x in e define

    B_x = {h in H : h intersect R = {x}}.

Thus A_y consists of red-critical edges with four red vertices and minority vertex y; B_x consists of blue-critical edges with four blue vertices and minority vertex x. These are actual edge families, not separately chosen extremal data for different exchanges. Set

    a_y=|A_y|, b_x=|B_x|,
    r_xy=#{g in A_y:x in g},
    c_xy=#{h in B_x:y in h}.

Swap x in e with y in B. The old edge e ceases to be monochromatic. A new red edge must be an element of A_y avoiding x; a new blue edge must be an element of B_x avoiding y. These two possibilities are disjoint and exhaust all new monochromatic edges. Therefore the exact number after the swap is

    f_xy = a_y+b_x-r_xy-c_xy.                            (1)

A non-Property-B hypothesis imposes f_xy>=1 for every one of the5b swaps. Unlike an upper bound depending only on |e intersect g|, equation(1) preserves all actual sharing of critical edges across different swaps.

The basic point-degree capacities are

    b_x + sum_y r_xy <= d(x)-1,                         (2)
    a_y + sum_{x in e} c_xy <= d(y).                     (3)

In(2) the excluded edge is e; the two counted critical families are disjoint. In(3), every counted blue-critical edge has a unique red vertex, so it is counted at most once. Also

    sum_y c_xy=4b_x,
    sum_{x in e} r_xy=sum_{g in A_y}|e intersect g|.

These are simultaneous identities for the original H and can be used without pretending that the row blockers are independent.

## 3. A stronger row-intersection inequality

For each x let

    C_x = intersection_{h in B_x}(h intersect B),

with C_x=B when B_x is empty. Precisely for y in C_x no blue-critical edge blocks the swap (x,y). Consequently, if there is no repairing swap, every y in C_x must have some g in A_y avoiding x. Summing this actual incidence statement gives

    sum_{x in e}|C_x|
      <= sum_y sum_{g in A_y}(5-|e intersect g|).         (4)

For example, |C_x| is b if b_x=0, is exactly4 if b_x=1, and can be zero already when b_x=2. Thus if n_i counts the x in e with b_x=i, then a valid weaker consequence is

    b n_0+4 n_1
      <= sum_y sum_{g in A_y}(5-|e intersect g|).         (5)

This bound retains the fact that multiple swaps may have the same blocking edges. It is stronger information than counting each ordered source/target edge pair in isolation, but its left side can vanish when every b_x>=2.

## 4. A degree-sensitive capacity from pair coverage

For x in e, the red edge e covers only its four fellow vertices in e. There are r-5 red vertices outside e. An edge in B_x covers none of them. Any other edge through x is bichromatic in the source state, so it contains at most three additional red vertices. Pair coverage therefore implies

    r-5 <= 3[d(x)-1-b_x],
    b_x <= d(x)-1-ceil((r-5)/3).                         (6)

This improves the trivial b_x<=d(x)-1 and genuinely uses the degree of the actual point x and its required red neighbors. For r=11 the upper bound is d(x)-3; for r=12 it is d(x)-4.

However, at the relevant degrees this does not force b_x<=1. At degree seven it permits b_x=4 for r=11 or3 for r=12; even degree six with r=12 permits b_x=2. Two distinct disjoint four-subsets of B exist for b>=11. If these are the blue parts of two edges in B_x, every swap in that row is blocked, with no need for an A_y edge. Ten such critical edges, two for each x in e, fit within the35-edge budget and the bounds(2),(6). This is a feasible local obstruction to the present inequalities, not a claimed full pair-covering H.

A concrete degree-seven row template at r=b=12 illustrates why rowwise pair coverage alone does not eliminate it. Let e={x,e2,e3,e4,e5}, let the other red points be z1,...,z7, and let B={b1,...,b12}. The seven edges through x may have the following forms:

    e;
    {x,b1,b2,b3,b4}, {x,b5,b6,b7,b8};
    {x,z1,z2,b9,b10}, {x,z3,z4,b11,b12},
    {x,z5,z6,b1,b9}, {x,z7,b2,b10,b11}.

They cover every other vertex in the x-row, are all bichromatic except e, and the two blue-critical edges block every swap involving x. Compatibility of five such rows inside one35-edge H would require genuinely joint information; it cannot be assumed either possible or impossible from this template.

## 5. What minimizing the bad-edge degree potential actually adds

Put D(g)=sum_{v in g}d(v), and choose a unique-bad balanced coloring minimizing D(e). If a swap has f_xy=1, its unique new bad edge g must satisfy

    D(g)>=D(e).                                         (7)

For f_xy>=2, minimization among unique-bad states gives no comparison at all. This is the precise restriction; it is not valid to infer that one of several new bad edges has degree sum at least D(e), or to subtract its weight from the source without an extra argument.

One can make the potential global without curing this problem. Choose epsilon>0 so small that every edge weight w(g)=1+epsilon D(g) is below2. Every state with two or more bad edges has total bad weight at least2, whereas every unique-bad state has weight below2. Therefore a global weight minimizer is unique-bad and satisfies

    sum_{g new bad after(x,y)} w(g) >= w(e).

But this inequality is automatic whenever f_xy>=2. Its only nontrivial content is again(7), on unique-to-unique transitions. Such transitions are reversible by the same swap. A degree potential cannot orient this reversible transition graph into an immediate contradiction merely by selecting its minimum.

In particular, if e consists entirely of minimum-degree vertices, then D(e)=5 delta is already the least possible edge weight, and(7) imposes no further restriction on any target edge. This is a real limitation for low-degree-edge branches, rather than a numerical defect of the old aggregate LP.

## 6. Pilot outcome and next required information

The exact constraints(1)--(6) are reusable and depend on the original degrees and the same critical edge families. They leave a clear obstruction: two suitably placed opposite-critical edges per x can make all C_x empty while remaining within the degree and edge-count budgets. A useful global proof must therefore force overlap among these actual four-subsets, constrain their compatibility across the five x, or recover the large global unique-state count after imposing the potential minimum. Merely replacing the old K_t coefficients by degree labels is not such an argument.

A bounded check on the one already explicit colorable H24 in `pairing_global/COUNTEREXAMPLE.json` sampled100,000 balanced colorings, including7,250 states with exactly one bad edge entirely of degree-seven points. It found no state in that sample without a repairing swap. This is not an exhaustive state check and gives neither a counterexample to the stronger local theorem nor evidence sufficient to prove it. Raw scope and counts are in `unique_bad_potential/CONTROL_PILOT.json`; no hypergraph was generated or enumerated.

This stage stops with the exact new blocker system and degree bound. It has not obtained a contradiction that significantly reduces the22- or23-point proof, and it does not repeat the already failed19-point moment relaxation.
