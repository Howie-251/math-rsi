"""Independent witness verification: stdlib only, no search-code imports."""
import itertools,json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def es(path):return {frozenset((a,b)) for a,b in zip(path,path[1:])}
def check_path(path,u,v,forced,long=()):
    assert len(path)==64 and set(path)==set(range(64))
    assert path[0]==u and path[-1]==v
    allowed={frozenset(e) for e in long}
    assert all((a^b).bit_count()==1 or frozenset((a,b)) in allowed for a,b in zip(path,path[1:]))
    assert {frozenset(e) for e in forced}<=es(path)
def check_matching(m):
    flat=[x for e in m for x in e]
    assert len(flat)==len(set(flat)) and all((a^b).bit_count()==1 for a,b in m)

data=json.loads((ROOT/'one_displaced_edge_results.json').read_text(encoding='utf8'))
for c in data['certificates']:
    m,l=c['matching'],c['completion'];u,v=c['u'],c['v']
    check_matching(m);check_matching(l)
    assert set(range(64))-{x for e in l for x in e}=={u,v}
    assert len({frozenset(e) for e in m}-{frozenset(e) for e in l})==1
for c in data['constructive_examples']:
    assert c['status']=='FOUND'
    m,l=c['matching'],c['completion'];u,v=c['u'],c['v'];a,b=c['removed_matching_edge']
    check_path(c['intermediate_path'],a,b,l+[[u,v]],[[u,v]])
    check_path(c['path'],u,v,m)
    assert es(c['path'])==(es(c['intermediate_path'])|{frozenset((a,b))})-{frozenset((u,v))}

surgeries=json.loads((ROOT/'four_hole_surgery.json').read_text(encoding='utf8'))
far=0
for c in surgeries:
    assert c['status']=='SURGERY_FOUND'
    m=c['matching'];u,v,z,w,t,x=(c[k] for k in ('u','v','z','w','t','x'))
    check_matching(m)
    assert set(range(64))-{a for e in m for a in e}=={u,z,w,t}
    assert v not in {u,z,w,t} and x not in {u,z,w,t}
    p=m+[[u,w],[z,t]]
    check_path(c['intermediate_path'],x,v,p,[[u,w],[z,t]])
    check_path(c['path'],u,v,m)
    cuts={frozenset(e) for e in c['cut_edges']}
    added={frozenset(e) for e in c['added_edges']}
    artificial={frozenset((u,w)),frozenset((z,t))}
    assert cuts<=es(c['intermediate_path'])-{frozenset(e) for e in p}
    assert es(c['path'])==(es(c['intermediate_path'])-artificial-cuts)|added
    assert c['extra_cuts']==len(cuts)
    lower=(min((z^w).bit_count(),(z^t).bit_count())-1)//2
    assert len(cuts)>=lower
    if c['kind']=='distance_five_holes':
        far+=1
        assert lower==2 and len(cuts)==2
        # No 3-edge cube route from z to either odd hole exists.
        for q in (w,t):
            assert all(((z^(1<<i))^(q^(1<<j))).bit_count()!=1 for i in range(6) for j in range(6))

abstract={}
for order in itertools.permutations('ABC'):
    event={'A':('u','w'),'B':('z','t'),'C':('a','b')}
    component_edges=[];previous='x'
    for tag in order:
        first,last=event[tag];component_edges.append((previous,first));previous=last
    component_edges.append((previous,'v'))
    graph={k:set() for k in ['x','u','w','z','t','a','b','v']}
    for a,b in component_edges+[('x','w'),('z','a'),('b','t')]:
        graph[a].add(b);graph[b].add(a)
    assert all(len(ns)==(1 if q in ('u','v') else 2) for q,ns in graph.items())
    seen={'u'};stack=['u']
    while stack:
        q=stack.pop()
        for nxt in graph[q]-seen:seen.add(nxt);stack.append(nxt)
    connected=len(seen)==8
    assert connected==(order.index('A')!=1)
    abstract[''.join(order)]=connected

files=['FOUR_HOLE_DERIVATION.md','four_hole_surgery.json','one_displaced_edge_results.json']
result={'status':'PASS','f1_completions':len(data['certificates']),
        'f1_constructed_paths':len(data['constructive_examples']),
        'covered_endpoint_surgeries':len(surgeries),'distance_five_cases':far,
        'f5_six_orders':abstract,'scope':'finite witnesses and abstract reconnection only; not full P6',
        'sha256':{f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in files}}
(ROOT/'four_hole_verification.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result,indent=2))
