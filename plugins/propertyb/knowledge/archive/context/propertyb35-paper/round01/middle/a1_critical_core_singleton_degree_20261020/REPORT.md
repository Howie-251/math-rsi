# Critical-core singleton budget: valid new restriction, explicit surviving graph relaxation

## Result

The proposed critical-core argument is valid, in the stronger induced-core form proved in [CRITICAL_CORE_LEMMA.md](CRITICAL_CORE_LEMMA.md). Every non-B simple five-uniform35-edge H has an induced at-least34-vertex singleton-intersection core with minimum degree at least5. Thus its non-one-intersection graph Gamma has at most one vertex of degree greater than29.

This excludes the **saved** old extremal graph with two Gamma-universal vertices. It does not close the retained A1 relaxation: the requested five-edge transfer is a valid literal simple-graph operation, and yields a graph satisfying even the stronger induced-core condition while retaining wedge cost13002. Its scalar relaxation still has L=2726136>2722720, with margin3416. No claim that13002 is the new constrained maximum is made; the new constrained maximum is bounded below by this example and above by the old13074.

## 1. Why the critical step uses the same original H

Take an inclusion-minimal non-B subfamily K of H. The accepted T33 theorem gives |K|>=34. For each original e in K and each v in e, a proper coloring of K−e makes e monochromatic. If changing v to the opposite color made no other edge monochromatic, K would be proper. A newly bad edge must contain v and have all its other points previously opposite to e, so its exact intersection with e is {v}. The five different vertices of e require five different original K edges. Therefore the singleton graph induced by K has minimum degree at least5.

This argument neither declares the original H critical nor preserves its A1 degree roles after deleting an edge. Different e/v may use different colorings; only the original-edge existence conclusions are combined. They are valid for a common fixed K. Detailed general quantifiers and proof are in the lemma file.

At attachment-group level the same conclusion says every e in K has at least one singleton neighbor attached at each of its five points already inside K. The balanced-five-group wedge maximum f(s) does not automatically decrease under this extra group nonemptiness when s>=5; its maximizing balanced groups already have all entries positive. Thus the direct new information is a genuine graph/core restriction, not a free subtraction from the old f(s) formula.

## 2. Explicit degree-preserving graph transfer

The previous independent graph certificate is read from

    ../a1_rank_component_wedge_budget_20261020/VERIFY.json.

It saves a connected35-vertex76-edge Gamma graph with degree histogram

    34^2,11^1,3^9,2^23,

and sum f(34−degree)=13074. In the saved numbering its two universal vertices are u=0,v=1, and its degree11 vertex is w=25. All23 degree2 vertices are adjacent only to u,v and are not adjacent to w.

Choose five of those degree2 vertices z. For each, delete the edge uz and add wz. Each old edge exists and each new edge is absent; the new endpoints are distinct, so no loop or repeated edge is introduced. The number of edges remains76, and each selected leaf retains degree2. The changes are

    q(u):34 ->29,   q(w):11 ->16,   q(v)=34 unchanged.

The final Gamma-degree histogram is

    34^1,29^1,16^1,3^9,2^23.

Hence its singleton-graph degree histogram is

    0^1,5^1,18^1,31^9,32^23.

There is precisely one singleton degree below5. In fact, deleting the unique degree-zero singleton vertex v leaves an induced34-vertex singleton graph of minimum degree exactly5: deleting an isolated singleton vertex does not remove any singleton neighbors. Thus this graph passes the **stronger** critical-core necessary condition, not only the weaker exception count.

The only changed wedge costs are those of u,w. Exact values are

    f(23)=211, f(18)=129, f(5)=10,
    P_new=13074−f(23)+f(18)+f(5)=13002.

All76 graph edges, the five removal/addition pairs, both degree histograms and the34-vertex induced-core list are saved in CHECK.json.

## 3. Exact surviving aggregate calculation

Retain the previously saved A1 moment relaxation

    (n0,n1,n2,n3,n4)=(34,519,5,29,8), tau=0.

The graph has e=76=595−519 non-one pairs, agreeing with that total. Only the joint wedge budget is reduced to P=13002. The existing capacities are

    C <= (33n0,26n1+339,24n2,13n3,4n4).

Filling the highest event weights first under the single shared P budget gives

    C=(0,12473,120,377,32),
    L=(36C0+120C1+330C2+792C3+1716C4)/2+3432n1
     =2726136=2722720+3416.

So the new graph restriction cannot by itself prove L<2722720 in this relaxation. The prior P bound reduction72 reduces L by60*72=4320; its old excess7736 becomes3416.

The graph is not claimed to arise from any five-uniform H. In particular its individual graph edges have not been supplied with actual intersection sets or an incidence matrix, and the scalar C values are only capacity allocations, not constructed original middle-edge flags. This is a witness that the retained graph/core restriction plus aggregate-capacity relaxation is insufficient. It is not a non-B hypergraph, not a counterexample to T33 or the36 target, and not a joint Gram realization.

## 4. Exact checks and scope

CHECK.py independently reads the frozen literal graph, performs the five set operations, verifies all degree and induced-core claims, computes f by exact integers, and recomputes the complete C allocation/L with Fraction. Its result is PASS_RELAXATION_WITNESS_ONLY; measured0.000380 CPU seconds. No optimizer, graph enumeration, H search, negative layout, Lean or external model was run. No proof/nav/wiki file was modified.

Reproduction:

```sh
python3 -B context/propertyb35-paper/round01/middle/a1_critical_core_singleton_degree_20261020/CHECK.py
```

The reusable new fact is the original critical core with five distinct singleton attachments per edge. The explicit relaxation survives this fact, including its induced34-core strengthening. A further actual incidence/weighted-Gram or attachment-colored common capacity is required; no unproved threshold-with-minimum-degree extremal principle was used.
