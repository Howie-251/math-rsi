"""Finite sanity checks for N1; exact completion classification of existing samples.
No claim of full Q6 enumeration. No solver infeasibility is used as a certificate.
"""
import json
from pathlib import Path
from collections import Counter
import networkx as nx
ROOT=Path(__file__).resolve().parent

def cube_edges(n):
    return [(a,a^(1<<i)) for a in range(1<<n) for i in range(n) if not a&(1<<i)]

def completions(n,holes):
    neighbors={a:[a^(1<<i) for i in range(n)] for a in range(1<<n)}
    def rec(free,chosen):
        if not free:
            yield tuple(chosen); return
        x=min(free,key=lambda a:sum(b in free for b in neighbors[a]))
        for y in neighbors[x]:
            if y in free:
                yield from rec(free-{x,y},chosen+[tuple(sorted((x,y)))])
    yield from rec(set(range(1<<n))-set(holes),[])

def rigidity_check(n,w):
    halves=[]
    for i in range(n):
        for parity in (0,1):
            halves.append({(a,a^(1<<i)) for a in range(1<<n)
                           if not a&(1<<i) and a.bit_count()%2==parity})
    totals=Counter()
    for short in completions(n,{0,w}):
        perfect=set(short)|{(0,w)}
        mate={a:b for edge in perfect for a,b in (edge,edge[::-1])}
        totals['perfect_matchings']+=1
        for x in range(1<<n):
            if x.bit_count()%2:continue
            for y in range(1<<n):
                if y.bit_count()%2!=1 or mate[x]==y:continue
                a,b=mate[x],mate[y]
                reduced=(perfect-{tuple(sorted((x,a))),tuple(sorted((y,b)))})|{tuple(sorted((a,b)))}
                totals['endpoint_pairs']+=1
                if any(half<=reduced for half in halves):
                    totals['half_layer_obstructions']+=1
                    assert w.bit_count()==3
                    assert len({a^b for a,b in short})<=3
                    assert (0,w) not in {tuple(sorted((x,a))),tuple(sorted((y,b)))}
    return dict(totals)

def complete(m,u,n=6,avoid_root=False):
    covered={x for e in m for x in e}
    free=set(range(1<<n))-covered
    allowed=free-{u} if avoid_root else free
    graph=nx.Graph();graph.add_nodes_from(allowed)
    graph.add_edges_from((a,b) for a,b in cube_edges(n) if a in allowed and b in allowed)
    extra=sorted(tuple(sorted(e)) for e in nx.max_weight_matching(graph,maxcardinality=True))
    missing=free-{z for e in extra for z in e}
    return extra,sorted(missing)

def main():
    rigidity={f'Q{n}_holes_0_{w}':rigidity_check(n,w) for n,w in [(3,7),(4,7)]}
    data=json.loads((ROOT/'pilot_results_retry.json').read_text(encoding='utf8'))
    counts=Counter(); templates={}; remaining=[]
    for c in data['cases']:
        if c['n']!=6:continue
        m,u,v=c['matching'],c['u'],c['v']
        key=tuple(tuple(e) for e in m)
        if key not in templates:
            ep,hp=complete(m,u)
            en,hn=complete(m,u,avoid_root=True)
            templates[key]={'perfect':not hp,'near_perfect':len(hn)==2 and u in hn,
                            'near_holes':hn,'near_extra':en,'perfect_extra':ep}
        test=templates[key]
        if len({a^b for a,b in m})<=5:label='known_five_directions'
        elif test['perfect']:label='D2_perfect_completion'
        elif test['near_perfect']:label='N3_near_perfect_completion'
        else:
            label='remaining'
            for i in range(6):
                if not ((u^v)&(1<<i)):continue
                cross=[(a,b) if (a&(1<<i))==(u&(1<<i)) else (b,a)
                       for a,b in m if (a^b)==1<<i]
                if len(cross)==1 and (cross[0][0].bit_count()-u.bit_count())%2:
                    label='D5_single_bridge';break
        counts[label]+=1
        if label=='remaining':remaining.append(c)
    probe=json.loads((ROOT/'single_bridge_probe.json').read_text(encoding='utf8'))
    for c in probe:
        path=c['path'];m=c['matching']
        assert c['status']=='FOUND' and len(path)==64 and set(path)==set(range(64))
        assert path[0]==c['u'] and path[-1]==c['v']
        edge_set={frozenset((a,b)) for a,b in zip(path,path[1:])}
        assert all((a^b).bit_count()==1 for a,b in zip(path,path[1:]))
        assert all(frozenset(e) in edge_set for e in m)
        assert sum((a^b)==32 for a,b in zip(path,path[1:]))==3
        assert len(m)<=30
    construction_path=ROOT/'near_perfect_constructions.json'
    construction_count=0
    if construction_path.exists():
        for c in json.loads(construction_path.read_text(encoding='utf8')):
            k,h,m=c['intermediate_path'],c['path'],c['matching']
            u,v,w,x=c['u'],c['v'],c['w'],c['x']
            assert len(k)==64 and set(k)==set(range(64)) and k[0]==x and k[-1]==v
            assert len(h)==64 and set(h)==set(range(64)) and h[0]==u and h[-1]==v
            long=[(a,b) for a,b in zip(k,k[1:]) if (a^b).bit_count()!=1]
            assert long==[(u,w)] and (x^w).bit_count()==1
            assert all((a^b).bit_count()==1 for a,b in zip(h,h[1:]))
            ke={frozenset(e) for e in zip(k,k[1:])}
            he={frozenset(e) for e in zip(h,h[1:])}
            assert he==(ke-{frozenset((u,w))})|{frozenset((x,w))}
            assert all(frozenset(e) in he for e in m)
            construction_count+=1
    # A concrete four-hole failure of completion, with an existing Hamilton witness.
    example=probe[0]
    holes=set(range(64))-{z for edge in example['matching'] for z in edge}
    s={z for z in holes if z!=0 and z.bit_count()%2==0}
    neighbors={y for z in s for y in holes if (z^y).bit_count()==1}
    assert len(example['matching'])==30 and holes=={0,13,21,60}
    assert len(neighbors)<len(s)
    (ROOT/'remaining_four_holes.json').write_text(json.dumps({**example,
        'uncovered':sorted(holes),'hall_set':sorted(s),'hall_neighbors':sorted(neighbors),
        'meaning':'not N3-completable, not a counterexample; valid path included'},indent=2),encoding='utf8')
    result={'scope':'N1 small finite checks, previous Q6 sample classification, independent 96 path checks',
            'rigidity':rigidity,'old_sample_classification':dict(counts),
            'template_count':len(templates),'templates_completable_near_perfect':sum(t['near_perfect'] for t in templates.values()),
            'single_bridge_paths_checked':len(probe),
            'near_perfect_splices_independently_checked':construction_count,
            'first_remaining':remaining[0] if remaining else None}
    (ROOT/'near_perfect_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8')
    print(json.dumps({k:v for k,v in result.items() if k!='first_remaining'},indent=2))

if __name__=='__main__':main()
