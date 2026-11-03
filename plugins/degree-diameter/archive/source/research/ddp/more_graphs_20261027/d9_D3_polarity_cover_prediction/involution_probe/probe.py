"""One intrinsic derived-affine-plane translation; no automorphism search."""
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import json
import resource
import time

start=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(3,3))
out=Path(__file__).resolve().parent
data=json.loads((out.parent/'BLOCKS.json').read_text())
adj=[set(map(int,line.split())) for line in (out.parent/'source585.implicit_adj.txt').read_text().splitlines() if line.strip()]
ports=data['ports'];portset=set(ports);fixed=0
blocks={r['vertex']:frozenset(r['ports']) for r in data['nonport_blocks']}
by_block={v:k for k,v in blocks.items()}
affine_points=portset-{fixed}
lines=[frozenset(b-{fixed}) for b in blocks.values() if fixed in b]
assert len(lines)==72 and all(len(l)==8 for l in lines)
pair_line={}
through=defaultdict(list)
for l in lines:
    for a in l:through[a].append(l)
    for a,b in combinations(sorted(l),2):
        assert (a,b) not in pair_line
        pair_line[a,b]=l
assert len(pair_line)==2016
special=[frozenset(blocks[t]-{fixed}) for t in sorted(adj[fixed])]
assert len(special)==8 and set.union(*(set(l) for l in special))==affine_points
assert sum(len(l) for l in special)==64
O=min(affine_points)
axis=next(l for l in special if O in l)
B=min(axis-{O})
C=min(affine_points-axis)

def line(a,b):
    return pair_line[min(a,b),max(a,b)]

def parallel_through(x,l):
    result=[m for m in through[x] if m==l or not m.intersection(l)]
    assert len(result)==1
    return result[0]

def intersection(l,m):
    meet=l.intersection(m)
    assert len(meet)==1
    return next(iter(meet))

def off_axis_translation(x):
    return intersection(parallel_through(x,axis),parallel_through(B,line(O,x)))

Cimage=off_axis_translation(C)
sigma_port={fixed:fixed}
for x in sorted(affine_points):
    if x not in axis:
        sigma_port[x]=off_axis_translation(x)
    else:
        sigma_port[x]=intersection(parallel_through(x,axis),parallel_through(Cimage,line(C,x)))

port_bijective=len(set(sigma_port.values()))==65
port_involution=all(sigma_port[sigma_port[x]]==x for x in ports)
fixed_ports=[x for x in ports if sigma_port[x]==x]
lift_missing=[]
sigma=list(range(585))
for x,y in sigma_port.items():sigma[x]=y
for t,b in blocks.items():
    transformed=frozenset(sigma_port[x] for x in b)
    if transformed not in by_block:
        lift_missing.append({'vertex':t,'transformed_ports':sorted(transformed)})
    else:sigma[t]=by_block[transformed]
bijective=len(set(sigma))==585 and not lift_missing
involution=bijective and all(sigma[sigma[x]]==x for x in range(585))
edge_failures=[]
if bijective:
    for u in range(585):
        for v in adj[u]:
            if u<v and sigma[v] not in adj[sigma[u]]:
                edge_failures.append([u,v,sigma[u],sigma[v]])
accepted=bijective and involution and not edge_failures and fixed_ports==[0]
result={'status':'VERIFIED_NONTRIVIAL_INVOLUTION' if accepted else 'SINGLE_GEOMETRIC_CANDIDATE_REFUTED',
        'prediction_disposition':'SUPPORTED' if accepted else 'REFUTED',
        'coordinate_method':'Parallelogram translation in the affineplane derived from actual Steinerblocks; no originalGF8 label assumption.',
        'fixed_port':fixed,'origin':O,'origin_image':B,'auxiliary_origin':C,'auxiliary_image':Cimage,
        'special_parallel_class_vertices':sorted(adj[fixed]),
        'special_axis_ports':sorted(axis),
        'port_bijective':port_bijective,'port_involution':port_involution,
        'fixed_ports':fixed_ports,
        'port_transpositions':[[x,sigma_port[x]] for x in ports if x<sigma_port[x]],
        'block_lift_failure_count':len(lift_missing),
        'first_block_lift_failure':lift_missing[0] if lift_missing else None,
        'graph_bijective':bijective,'graph_involution':involution,
        'fixed_graph_vertices':[x for x in range(585) if sigma[x]==x] if bijective else None,
        'edges_checked':2600 if bijective else 0,
        'edge_failure_count':len(edge_failures),'first_edge_failure':edge_failures[0] if edge_failures else None,
        'sigma':sigma if accepted else None,
        'graph_BFS':0,'automorphism_group_enumeration':False,'candidates_tested':1,
        'CPU_seconds':time.process_time()-start,'running':False,'pending':[]}
(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
if accepted:
    (out/'sigma.json').write_text(json.dumps({'fixed_port':fixed,'permutation':sigma,'port_transpositions':result['port_transpositions']},indent=2)+'\n')
(out/'terminal.json').write_text(json.dumps({k:v for k,v in result.items() if k!='sigma'},indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['sigma','port_transpositions']},indent=2))
