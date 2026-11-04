"""Construct canonical A4 witnesses using the proved completion choices.
MILP only supplies individual local positive witnesses; universal existence
rests on CANONICAL_A4_CLOSURE.md and finite table verification.
"""
import itertools
import json
import random
from collections import Counter
from pathlib import Path
import networkx as nx
from avoided_vertex_transfer import cycle_on
ROOT=Path(__file__).resolve().parent
def edge(a,b):return tuple(sorted((a,b)))
def mates(f):return {a:b for e in f for a,b in (e,e[::-1])}
def edges(path,closed=False):
    return {edge(a,b) for a,b in zip(path,path[1:]+(path[:1] if closed else []))}
def pairs(xs):
    if not xs:
        yield set();return
    a=xs[0]
    for i,b in enumerate(xs[1:],1):
        for rest in pairs(xs[1:i]+xs[i+1:]):yield rest|{edge(a,b)}

BAD={}
for y in range(16):
    if not y.bit_count()%2:continue
    perm=[i for i in range(4) if y>>i&1]+[i for i in range(4) if not y>>i&1]
    def tr(x):return sum(1<<perm[i] for i in range(4) if x>>i&1)
    data=json.loads((ROOT/f'q4_distance{y.bit_count()}_avoided_table_verification.json').read_text())
    BAD[y]={frozenset(edge(tr(a),tr(b)) for a,b in row['matching']) for row in data['exceptions']}
STALL={}
for level in json.loads((ROOT/'a4_completion_endpoint_probe.json').read_text())['levels']:
    STALL[level['crossings']]={frozenset(map(tuple,s['matching'])):s for s in level['stalls']}

def path_from_cycle(c,d,k):
    i=c.index(d);step=-1 if c[(i+1)%len(c)]==k else 1
    assert c[(i-step)%len(c)]==k
    return [c[(i+step*j)%len(c)] for j in range(len(c))]

def construct(original):
    f={edge(*e) for e in original};assert len(f)==14
    assert set(range(32))-{x for e in f for x in e}=={0,1,14,22}
    fa={edge(a//2,b//2) for a,b in f if a%2 and b%2}
    fb={edge(a//2,b//2) for a,b in f if not a%2 and not b%2}
    cross={e for e in f if (e[0]^e[1])&1}
    amap={a//2:b//2 for e in cross for a,b in (e,e[::-1]) if a%2}
    bmap={b:a for a,b in amap.items()};xa=set(amap);xb=set(bmap);c=len(cross)
    stall=STALL[c].get(frozenset(fa))
    if stall is None:
        targets=[7,11];roots=sorted(xa);mode='fixed_free_target'
    else:
        outside=[y for y in stall['good_endpoints'] if y not in xb]
        if outside:targets=outside;roots=sorted(xa);mode='safe_flexible_target'
        else:
            targets=[stall['good_endpoints'][0]];roots=[bmap[targets[0]]];mode='occupied_target_prescribed_root'
    chosen=None
    for y in targets:
        for d in roots:
            if d==y:continue
            for auxiliary in pairs(sorted(xa-{d})):
                la=fa|auxiliary;k=mates(la)[y]
                ta=(la-{edge(y,k)})|{edge(d,k)}
                if frozenset(ta) not in BAD[y]:chosen=(y,d,auxiliary,k,ta);break
            if chosen:break
        if chosen:break
    assert chosen is not None
    y,d,auxiliary,k,ta=chosen
    solved=cycle_on(set(range(16))-{0,y},ta,seconds=15)
    assert solved['status']=='FOUND',solved
    local_path=path_from_cycle(solved['cycle'],d,k)+[y]
    apath=[2*x+1 for x in local_path]
    de={edge(2*a+1,2*b+1) for a,b in auxiliary}
    transfer=edges(apath)-de|cross|{edge(2*y+1,2*y)}
    graph=nx.Graph();graph.add_nodes_from(apath);graph.add_edges_from(transfer)
    paths=[];rpaths={}
    for component in nx.connected_components(graph):
        ends=sorted(x for x in component if graph.degree[x]==1)
        assert len(ends)==2 and all(x%2==0 for x in ends)
        p=nx.shortest_path(graph,*ends);assert set(p)==component
        paths.append(p);rpaths[edge(ends[0]//2,ends[1]//2)]=p
    rr=set(rpaths);special=None
    if y in xb:
        lb=fb|rr;vertices=set(range(16))-{y}
    elif y in (7,11):
        lb=fb|rr;vertices=set(range(16))
    else:
        kb=mates(fb)[y];q=mates(rr)[y]
        lb=(fb-{edge(y,kb)})|(rr-{edge(y,q)})|{edge(kb,q)}
        special=(edge(kb,q),kb,q);vertices=set(range(16))-{y}
    solved_b=cycle_on(vertices,lb,seconds=15)
    assert solved_b['status']=='FOUND',solved_b
    bc=solved_b['cycle']
    def orient(p,start,end):
        if p[0]!=start:p=p[::-1]
        assert p[0]==start and p[-1]==end
        return p
    final=[]
    for a,b in zip(bc,bc[1:]+bc[:1]):
        e=edge(a,b)
        if special and e==special[0]:
            _,kb,q=special
            rp=orient(rpaths[edge(y,q)],2*y,2*q)
            p=orient([2*kb]+rp,2*a,2*b)
        elif e in rr:p=orient(rpaths[e],2*a,2*b)
        else:p=[2*a,2*b]
        final.extend(p[:-1])
    assert len(final)==len(set(final))==31 and set(final)==set(range(32))-{1}
    assert f<=edges(final,True)
    assert all((a^b).bit_count()==1 for a,b in edges(final,True)-f)
    return {'matching':sorted(f),'crossings':c,'mode':mode,'root':d,'target':y,
            'auxiliary':sorted(auxiliary),'a_path':apath,'transfer_paths':paths,
            'b_matching':sorted(lb),'b_cycle':bc,'cycle':final,
            'isolated_A_target_after_D_removal':y in xa and y!=d}

def random_case(c,rng,stall=None,force_port=False):
    if stall:
        fa={tuple(e) for e in stall['matching']};xa=set(stall['ports'])
    else:
        values=list(range(1,16));rng.shuffle(values);xa=set(values[:c])
        rest=values[c:];fa={edge(a,b) for a,b in zip(rest[::2],rest[1::2])}
    available=set(range(16))-{0,7,11}
    required=set(stall['good_endpoints']) if force_port else set()
    xb=required|set(rng.sample(sorted(available-required),c-len(required)))
    remaining=sorted(set(range(16))-{0,7,11}-xb);rng.shuffle(remaining)
    fb={edge(a,b) for a,b in zip(remaining[::2],remaining[1::2])}
    aa=sorted(xa);bb=sorted(xb);rng.shuffle(bb)
    f={edge(2*a+1,2*b+1) for a,b in fa}|{edge(2*a,2*b) for a,b in fb}
    f|={edge(2*a+1,2*b) for a,b in zip(aa,bb)}
    return f

def main():
    rng=random.Random(20261102);cases=[]
    for c in (1,3,5,7,9,11,13):
        for _ in range(4):cases.append(construct(random_case(c,rng)))
    for c in (1,3):
        samples=list(STALL[c].values())
        for _ in range(4):cases.append(construct(random_case(c,rng,rng.choice(samples))))
    for c in (5,7):
        samples=list(STALL[c].values())
        for _ in range(8):cases.append(construct(random_case(c,rng,rng.choice(samples),True)))
    result={'scope':'52 canonical A4 positive construction certificates; not exhaustive Q5 matching verification',
            'count':len(cases),'modes':dict(Counter(c['mode'] for c in cases)),
            'isolated_endpoint_cases':sum(c['isolated_A_target_after_D_removal'] for c in cases),
            'cases':cases,'full_p6_proved':False}
    (ROOT/'canonical_a4_construction_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['count','modes','isolated_endpoint_cases']}))
if __name__=='__main__':main()
