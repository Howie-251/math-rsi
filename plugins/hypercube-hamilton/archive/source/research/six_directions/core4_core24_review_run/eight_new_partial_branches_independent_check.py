"""Fresh audit supplement: geometry, multigraph lifting, short-degree coverage.

No producer or previous checker is imported. Q4 negative-table correctness and
the N10/N14/Fink/T44 theorems remain explicit mathematical imports.
"""
from pathlib import Path
from itertools import permutations, combinations
from collections import Counter
import json, hashlib

R = Path(__file__).resolve().parent
V = set(range(16))
def edge(a,b): return tuple(sorted((a,b)))
def es(rows): return {edge(a,b) for a,b in rows}
def tr(x,p): return sum(((x>>j)&1)<<p[j] for j in range(len(p)))

def components(edges, vertices):
    adj = {v:[] for v in vertices}
    for k,(a,b) in enumerate(edges):
        assert a in adj and b in adj
        adj[a].append((b,k)); adj[b].append((a,k))
    unseen=set(vertices); out=[]
    while unseen:
        start=next(iter(unseen)); todo=[start]; nodes=set(); ids=set()
        while todo:
            a=todo.pop()
            if a in nodes: continue
            nodes.add(a); unseen.remove(a)
            for b,k in adj[a]:
                ids.add(k)
                if b not in nodes: todo.append(b)
        out.append((nodes,ids))
    return adj,out

def check_geometry():
    rows=json.loads((R/'eight_ep0_fast_route_check.json').read_text())['orbits']
    images=set(); closed=0
    for row in rows:
        v=row['target']; z=set(row['Z']); w=set(row['W']); holes={0}|z|w
        orbit={(tr(v,p),tuple(sorted(tr(a,p) for a in z)),
                tuple(sorted(tr(a,p) for a in w)))
               for p in permutations(range(6)) if tr(v,p)==v}
        assert len(orbit)==row['target_preserving_orbit_size']
        assert images.isdisjoint(orbit); images |= orbit
        sufficient=set()
        for i in range(6):
            face={a for a in range(64) if (a>>i&1)==(v>>i&1)}
            if 0 not in face or len(z&face)!=2 or w&face: continue
            s={a^(1<<i) for a in w}
            for q in face-holes-{v}:
                h=q^(1<<i)
                if q.bit_count()%2!=1 or h in holes: continue
                n={q^(1<<j) for j in range(6) if j!=i}
                if n-s==z&face: sufficient.add(edge(q,h))
        assert sufficient==es((g['q'],g['mirror']) for g in row['triangle_sufficient_crossing_edges'])
        if row['all_realizing_matchings_EP0_closed']:
            h=15 if v==1 else 63
            neighbors={h^(1<<j) for j in range(6)}-holes
            assert h not in holes and neighbors
            assert all(edge(h,q) in sufficient for q in neighbors)
            closed+=len(orbit)
        else:
            m=es(row['matching_avoiding_all_triangle_rule_edges'])
            assert len(m)==28 and not (m&sufficient)
            ends=[a for e in m for a in e]
            assert len(set(ends))==56 and set(ends)==set(range(64))-holes
            assert all((a^b).bit_count()==1 for a,b in m)
    assert len(images)==50 and closed==11
    return {'disjoint_normalized_geometries':50,'EP0_closed':11,'EP0_open':39}

def check_lifting():
    obj=json.loads((R/'t15_sameface_positive_c2_certificates.json').read_text())
    a_by_type={}
    for a in obj['A_certificates']:
        a_by_type.setdefault(tuple(a['avoid']),a)
    checked=0
    for b in obj['B_exception_certificates']:
        z=b['z']; u=b['root_side_B_port']; t=b['other_B_port']
        f=es(b['F_B']); y=set(b['ports'])
        assert len(f)==7 and {a for e in f for a in e}==V-y
        # Independent connected-component compression, preserving edge identity.
        multiedges=list(f)+[(0,u),(z,t)]
        adj,parts=components(multiedges,V)
        assert all(len(adj[x])==(2 if x in (0,z) else 1) for x in V)
        compressed=set()
        for nodes,ids in parts:
            endpoints=[x for x in nodes if len(adj[x])==1]
            assert len(endpoints)==2 and len(ids)==len(nodes)-1
            compressed.add(edge(*endpoints))
        assert len(compressed)==7
        cyc=b['compressed_cycle']
        ce=es((cyc[i-1],cyc[i]) for i in range(14))
        assert len(cyc)==len(set(cyc))==14 and set(cyc)==V-{0,z}
        assert compressed<=ce
        for av,a in a_by_type.items():
            p,q=a['artificial_pair']
            # Map the original A crossing bijection p->u,q->t. Both A orders
            # are certified; pick the one that gives the saved B excursion.
            path=next(w['path'] for w in a['witnesses']
                      if w['z']==z and w['root_side_port']==p)
            ap=es(zip(path,path[1:])); fa=es(a['F_A'])
            assert edge(p,q) in ap
            # Physical labels: A=x and B=16+x; bridges are short xor16.
            required=fa|{edge(16+x,16+y) for x,y in f}|{edge(p,16+u),edge(q,16+t)}
            full=(ap-{edge(p,q)})|{edge(16+x,16+y) for x,y in ce-compressed}|{edge(16+x,16+y) for x,y in f}|{edge(p,16+u),edge(q,16+t),edge(0,16),edge(z,16+z)}
            support=set(range(32))-set(av)
            ad,parts=components(list(full),support)
            assert len(full)==30 and len(parts)==1
            assert all(len(ad[x])==2 for x in support)
            assert required<=full
            assert all((x^y).bit_count()==1 for x,y in full-required)
            checked+=1
    assert checked==12720
    return {'B_multigraph_contractions':6360,'explicit_full_Q5_lifts':checked,
            'A_scope':'one representative per avoid geometry for actual lifting; all 1680 A paths separately checked by existing independent checker'}

def short_pairings(vs):
    if not vs:
        yield frozenset(); return
    a=min(vs)
    for bit in (1,2,4,8):
        b=a^bit
        if b in vs:
            for tail in short_pairings(vs-{a,b}): yield tail|{edge(a,b)}

def check_short_degrees():
    counts={}
    for u in (3,5,6):
        support=V-{0}; patterns=set()
        for a,b in combinations(sorted({u^bit for bit in (1,2,4,8)}&support),2):
            for f in short_pairings(support-{u,a,b}):
                n=f|{edge(u,a),edge(u,b)}
                degree=Counter(x for e in n for x in e)
                assert len(n)==8 and all(degree[x]==(2 if x==u else 1) for x in support)
                patterns.add(n)
        assert len(patterns)==116
        counts[u]=len(patterns)
    partials={c:__import__('math').comb(12,c)*__import__('math').prod(range(1,12-c,2)) for c in range(0,13,2)}
    assert sum(partials.values())==140152
    return {'complete_short_degree_pattern_counts':counts,'A_partial_counts':partials,
            'spectrum_extrema_and_universal_positive_crossing_success':'NOT_VERIFIED'}

def main():
    result={'status':'PASS','geometry':check_geometry(),'c2_lifting':check_lifting(),
            'core0_short_degree_enumeration':check_short_degrees(),
            'review_independence':'same-family','acceptance_status':'provisional',
            'full_T15_proved':False,'full_eight_hole_proved':False,'full_P6_proved':False}
    result['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (R/'eight_new_partial_branches_independent_check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
