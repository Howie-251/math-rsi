# Actual weak-lock selection lemmas

All statements concern the same finite simple k-uniform pair-covering hypergraph H on v vertices, with M edges, degrees d(x), and codegrees lambda(x,y). Write a=k−1. Pair coverage gives lambda(x,y)≥1 and sum_{y≠x} lambda(x,y)=a d(x). These are selection tools; they do not alone prove a Property B bound.

## Lemma W: a weak wedge around a prescribed unit edge

Let R be a vertex set of size r, and let x,y∈R with lambda(x,y)=1. If

    a(d(x)+d(y)) < 2v+2r−6,

then there is z∈R\{x,y} such that one of lambda(x,z),lambda(y,z) equals one and the other is at most two.

Proof. Let u_x,u_y denote unit-codegree degrees inside R. Suppose no such z exists. Each of the u_y−1 unit neighbors z of y other than x then has lambda(x,z)≥3. In the full x row, start with baseline two on v−1 partners. There are at most u_x+(v−r) unit partners in all of V. The identified u_y−1 partners each add at least one. Therefore

    a d(x) ≥ 2(v−1)−u_x−(v−r)+(u_y−1)
           = v+r−3−u_x+u_y.

Interchanging x,y and adding gives a(d(x)+d(y))≥2v+2r−6, contradiction. ∎

For k=6,v=36,M=66,min degree10, R={d≤12} has r≥24. A degree10 point has at most50−35=15 nonunit partners, so has at least r−16≥8 unit partners in R. Choose one y; 5(10+d(y))≤110<114≤2v+2r−6. Hence an actual triple containing the degree10 point, all degrees at most12, has pair-codegrees all one except possibly one pair of codegree two. For the 11-regular v36 case take R=V; 110<138. For v35,min degree11 take R={d=11}; r≥24, a point has at least r−22≥2 unit partners, and110<112≤2v+2r−6.

## Lemma E: extending actual locks with bounded total pair excess

Let S be s distinct vertices, let t=sum_{x∈S}d(x), let

    b=sum_{{x,z}⊂S}(lambda(x,z)−1),
    E=a t−s(v−1)−2b.

For y outside S put e(y)=sum_{x∈S}(lambda(x,y)−1). Then e(y)≥0 and sum_{y∉S}e(y)=E. For an integer q≥0, at least

    p=v−s−floor(E/(q+1))

outside vertices have e(y)≤q. If H has minimum degree δ and p>0, one of these vertices has degree at most

    δ+floor((kM−t−(v−s)δ)/p).

Proof. Sum the codegree rows of S and subtract the twice-counted internal codegrees, then subtract s for each outside vertex; this yields E. Every outside vertex not in the indicated pool costs at least q+1 of this nonnegative excess. Every outside degree is at leastδ. If all p or more pool vertices exceeded the displayed bound, their excess degrees alone would exceed the total outside excess kM−t−(v−s)δ. ∎

For q=1, the new vertex has unit codegree with every old lock except possibly a single pair of codegree two. This retains the actual old trace; new trace classification must project to it. No assumption of independent incident edges or arbitrary trace realizability is made.

## General method status

These two paper lemmas have been checked by the primary agent. Their instantiated probability tables and complete application coverage have separate independent checks; they are not consequences of merely writing these formulas. This note does not resume Lean or change the current accepted global lower bound.
