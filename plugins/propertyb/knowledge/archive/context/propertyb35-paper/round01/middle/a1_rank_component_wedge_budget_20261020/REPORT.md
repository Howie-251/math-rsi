# A1 component-rank / wedge-budget pilot: this safe relaxation is redundant

## Result

The requested exact pilot at n1=519 gives **P_component=13074**, exactly the previous unrestricted singleton-graph threshold upper bound. It does not lower the retained necessary-profile value L=2730456 to the repair threshold2722720.

More strongly, the proposed component relaxation equals the old unrestricted graph upper bound for **every e=595−n1≥34**, including all currently saved25 profiles. This is an analytic stopping result, not a failure to finish the DP. No further profiles, LPs, locks, original H or negative layouts were searched.

The optimum graph reconstructed below is actually connected and has no isolated vertices. Thus recovering connectedness of the component optimizer, by itself, cannot improve this witness. The missing information is a stronger constraint on the actual incidence Gram block than the size-only rank lower bound rho(35)=7.

## 1. Exact necessary scalar domain

H has the original reduced A1 roles on21 vertices and35 distinct five-edges. The supplied paper reduction gives the graph Gamma on the35 original edge indices, adjacent precisely when the intersection is not one, at most three isolated vertices. The real matrix

    AA^T−J=A(I21−J21/25)A^T

is positive semidefinite of rank at most21 and block-diagonal by Gamma components. For a block of s distinct equal-weight binary rows, affine coordinate projection gives rank at least

    rho(s)=1+ceil(log2 s),  including rho(1)=1.

Consequently actual component data (s_i,m_i) satisfy

    sum s_i=35,  sum m_i=e=595−n1,
    sum rho(s_i)<=21,  #{i:s_i=1}<=3,
    m_i=0 if s_i=1;
    s_i−1<=m_i<=C(s_i,2) otherwise.

No component partition or its realization as an H is assumed. The task's new at-most-three-isolates lemma is used as a supplied necessary input, not reproved by this program.

Let f(s) be the maximum wedge pair sum for five nonnegative integer groups of total s:

    f(s)=(s²−(5−b)a²−b(a+1)²)/2,  s=5a+b,0<=b<5.

A Gamma vertex of degree q has singleton degree34−q. Thus P<=sum_v g(q_v), where g(q)=f(34−q), q=0..34. The second difference of g is nonnegative, since f(s+1)−f(s)=s−floor(s/5) is nondecreasing.

For an s-vertex m-edge component we safely replace its internal graph by **any** s-vertex m-edge simple graph. Its upper bound is U(s,m,0), where the offset r counts already removed universal vertices:

    U(s,m,r)=max{g(r)+U(s−1,m,r),
                   g(s−1+r)+U(s−1,m−s+1,r+1)}.

Invalid m outside[0,C(s,2)] has value minus infinity; U(0,0,r)=0. The exact component relaxation maximizes the sum of these U-values under the displayed integer constraints. Its maximizing graph inside a declared component is not assumed connected.

## 2. Why U is a valid unrestricted-graph maximum

For any fixed graph size and edge count, choose a graph maximizing the convex degree sum and then the lexicographically greatest sorted degree sequence. If d(u)<=d(v) and uw is an edge while vw is not, with w distinct from u,v, move uw to vw. Convexity does not lower the objective and the sorted degree sequence strictly increases. Such a pair therefore cannot occur at the chosen maximizer. This gives nested neighborhoods N(u)\{v} subset N(v)\{u} when d(u)<=d(v).

A graph with nested neighborhoods has either an isolated vertex or a universal vertex. Indeed, if the minimum degree is positive, let v have maximum degree and u any other vertex. A neighbor w of u, if w!=v, is also adjacent to v by nesting; nesting again from w toward v shows u adjacent to v. (If u's only chosen neighbor is v the conclusion is already immediate.) Removal preserves nesting. Thus the maximizer is a threshold graph and the isolated/universal recurrence above computes its exact value, including an offset r in the convex function. This argument does not assume the maximizer is connected.

The original singleton graph is the complement of Gamma, so its unrestricted maximum at edge count n1 agrees with U(35,595−n1,0). At n1=519 the value is13074.

## 3. Exact component DP and its no-gain certificate

PILOT.cpp computes D(n,r,e), the best sum of U-values for nontrivial declared components with n total vertices, exactly r total rho and e edges. Starting at D(0,0,0)=0, it adds a component of size s>=2, rho(s), and m in[s−1,C(s,2)]. The vertex coordinate strictly increases, so this finite dynamic program covers every component multiset, albeit possibly in more than one order. Such repetition cannot change a maximum. It finally maximizes

    i*g(0)+D(35−i,r,76),  0<=i<=3, r<=21−i.

The program does not silently impose connectedness on the threshold extremizer. Its exact maximum13074 has the legal relaxed component certificate

    one component (s,m,rho)=(35,76,7), zero declared isolates.

There is also an exact proof that no new bound can result here. Let U_N(e)=U(35,e,0).

* Given any admissible declared component collection, choose arbitrary simple-graph maximizers for each U(s_i,m_i,0) and take their disjoint union. This is a35-vertex e-edge simple graph, whether or not each chosen piece is connected. Hence the sum is at most U_N(e).
* If e>=34, the single declared block s=35,m=e is allowed: its connectivity edge lower bound holds, rho(35)=7<=21, and it declares no singleton components. Its value is exactly U_N(e).

Therefore the proposed safe component majorant equals U_N(e) for all34<=e<=595. In the retained range397<=n1<=546, one has49<=e<=198. Thus the entire current domain falls in this no-gain range. This is why no additional25-profile run or multiplier LP was warranted. Any linear component majorant must also respect this single component constraint and cannot price it below13074 at the pilot.

## 4. Independent exact verification and a genuine graph optimizer

VERIFY.py does not import the C++ implementation. It enumerates every labeled simple graph through six vertices (33867 graphs in total), groups by edge count, and compares the direct maximum of sum g(degree) with its separately implemented threshold recurrence. Every comparison agrees.

It then separately evaluates U(35,76,0), recovers an explicit maximizing threshold graph, and saves all76 distinct graph edges, its threshold sequence, degree histogram and connected components. The optimizer has

    Gamma-degree histogram: 34^2, 11^1, 3^9, 2^23.

It is connected on all35 graph vertices and has zero isolates. Its singleton-degree histogram is0^2,23^1,31^9,32^23, giving exactly

    2*f(0)+f(23)+9*f(31)+23*f(32)=13074.

This graph satisfies the **retained scalar component constraints**: one connected35-vertex76-edge graph and rho budget7. It is not asserted to be the non-one intersection graph of any original H. In particular no20/21-dimensional realization of its weighted off-diagonal Gram entries or A1 edge colors/roles was constructed. It is a relaxation witness, not a hypergraph counterexample.

## 5. Files, actual cost and stopping point

- PILOT.cpp/PILOT: fixed exact component DP, compiled with clang++−std=c++17−O3 and assertions enabled.
- PILOT.json: complete pilot maximum, selected component data, measured0.013279 CPU seconds.
- VERIFY.py/VERIFY.json: independent graph-definition checks, threshold optimizer and literal76 graph edges; measured0.260139 CPU seconds, PASS.

Reproduction from the project root:

```sh
clang++ -std=c++17 -O3 context/propertyb35-paper/round01/middle/a1_rank_component_wedge_budget_20261020/PILOT.cpp -o context/propertyb35-paper/round01/middle/a1_rank_component_wedge_budget_20261020/PILOT
context/propertyb35-paper/round01/middle/a1_rank_component_wedge_budget_20261020/PILOT
python3 -B context/propertyb35-paper/round01/middle/a1_rank_component_wedge_budget_20261020/VERIFY.py
```

The total measured computation was below0.3 CPU seconds; the20CPU budget was not consumed or extended. No whole-H or component graph enumeration beyond the independent six-vertex definition test was performed. No proof/nav/wiki/Lean files were changed. The original A1 and25 aggregate survivors remain open. To improve this route one must retain additional actual Gram/incidence information inside a large component, rather than the size-only rho lower bound or connectedness alone. No stronger unproved restriction has been substituted in this report.
