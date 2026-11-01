"""Independent reconstruction of the1715-vertex/2520-edge non-B five-uniform subcubic-image example."""
from pathlib import Path
from itertools import combinations,product
from collections import Counter
import json,time
HERE=Path(__file__).parent

def main():
    start=time.time();U=tuple(range(5));next_vertex=5;records=[];gadgets=[]
    def fresh(n):
        nonlocal next_vertex
        a=tuple(range(next_vertex,next_vertex+n));next_vertex+=n;return a
    def add(pair,tail,kind):
        pair=frozenset(pair);tail=frozenset(tail)
        assert len(pair)==2 and len(tail)==3 and pair.isdisjoint(tail)
        edge=pair|tail;assert len(edge)==5
        records.append(dict(active=pair,tail=tail,edge=edge,kind=kind))
    for T in combinations(U,3):
        C=[fresh(3) for _ in range(3)]
        for triangle in C:
            for pair in combinations(triangle,2):add(pair,T,'first_triangle')
        transversals=list(product(*C));assert len(set(transversals))==27
        for Tprime in transversals:
            prism=fresh(6);top,bottom=prism[:3],prism[3:]
            for layer in (top,bottom):
                for pair in combinations(layer,2):add(pair,T,'prism_triangle')
            for i in range(3):add((top[i],bottom[i]),Tprime,'prism_matching')
        gadgets.append(dict(tail=T,triangles=C,transversals=len(transversals)))
    assert next_vertex==1715 and len(records)==2520 and len(gadgets)==10
    edges=[r['edge'] for r in records];pairs=[r['active'] for r in records]
    assert len(set(edges))==2520 and len(set(pairs))==2520
    assert set().union(*edges)==set(range(next_vertex))
    image_degree=Counter(v for pair in pairs for v in pair)
    hyper_degree=Counter(v for e in edges for v in e)
    image_hist=Counter(image_degree.get(v,0) for v in range(next_vertex))
    hyper_hist=Counter(hyper_degree[v] for v in range(next_vertex))
    assert image_hist=={0:5,2:90,3:1620}
    assert hyper_hist=={1026:5,29:90,3:1620}
    assert sum(image_degree.values())==5040 and sum(hyper_degree.values())==12600
    assert all(r['active']<=r['edge'] for r in records)
    assert all(image_degree.get(v,0)==0 for v in U)
    assert Counter(r['kind'] for r in records)=={'first_triangle':90,'prism_triangle':1620,'prism_matching':810}

    tri=[(0,1),(0,2),(1,2),(3,4),(3,5),(4,5)]
    matching=[(0,3),(1,4),(2,5)];prism_checks=[]
    for c in (0,1):
        no_c_triangles=[];no_opposite_matching=[];joint=[]
        for coloring in product((0,1),repeat=6):
            a=not any(coloring[x]==coloring[y]==c for x,y in tri)
            b=not any(coloring[x]==coloring[y]==1-c for x,y in matching)
            if a:
                no_c_triangles.append(coloring);assert sum(x==c for x in coloring)<=2
            if b:
                no_opposite_matching.append(coloring);assert sum(x==c for x in coloring)>=3
            if a and b:joint.append(coloring)
        assert len(no_c_triangles)==16 and len(no_opposite_matching)==27 and not joint
        prism_checks.append(dict(tail_color=c,states_checked=64,no_c_triangle_edge=16,no_opposite_matching_edge=27,joint_satisfying=0))
    # Check only the32 colorings of the initial five-point pigeonhole gadget.
    assert all(any(len({color[v] for v in T})==1 for T in combinations(U,3)) for color in product((0,1),repeat=5))
    out=dict(status='PASS',scope=__doc__,vertices=next_vertex,hyperedges=len(edges),uniformity=5,simple_hypergraph=True,image_simple=True,image_edges=len(pairs),image_max_degree=max(image_degree.values()),image_degree_histogram=dict(sorted(image_hist.items())),hypergraph_degree_histogram=dict(sorted(hyper_hist.items())),binding_checks=dict(all_active_pairs_have_two_distinct_vertices=True,all_tails_have_three_distinct_vertices=True,all_pairs_disjoint_from_their_tails=True,all_active_pairs_subset_corresponding_hyperedge=True,image_pair_to_hyperedge_is_bijection=True,only_active_pairs_contribute_image_degree=True),gadgets=dict(initial_vertices=5,initial_triples=10,first_triangles=30,first_triangle_vertices=90,prisms=270,prism_vertices=1620,transversals_per_initial_triple=27),edge_kinds=dict(Counter(r['kind'] for r in records)),prism_checks=prism_checks,initial_pigeonhole_colorings_checked=32,global_hypergraph_colorings_enumerated=0,conclusion='The explicitly reconstructed simple five-uniform hypergraph is non-Property-B by the local forcing proof in the companion Markdown, while its specified simple image has maximum degree3.',scope_exclusion='This2520-edge construction is not a35-edge counterexample and does not settle the active m(5)>=36 goal.',elapsed_seconds=time.time()-start)
    (HERE/'GEMINI_SUBCUBIC_COUNTEREXAMPLE_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
