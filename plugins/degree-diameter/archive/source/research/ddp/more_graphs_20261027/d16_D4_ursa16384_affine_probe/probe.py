"""One label-bound affine GF4 relation probe; no graph BFS or search."""
from collections import Counter, defaultdict
from pathlib import Path
import json
import resource
import time

start=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
out=Path(__file__).resolve().parent
n=16384
adj=[set() for _ in range(n)]
edge_count=0
for line in (out/'source16384.edges').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    u,v=map(int,line.split())
    adj[u].add(v);adj[v].add(u);edge_count+=1

mul2=[sum(([0,2,3,1][x//4**j%4])*4**j for j in range(4)) for x in range(256)]
mul=[[0]*256,list(range(256)),mul2,[x^mul2[x] for x in range(256)]]
rows={}
fiber_neighborhoods=[]
bad_vertex=None
for g in range(64):
    targets=set()
    for x in range(256):
        grouped=defaultdict(set)
        for v in adj[256*g+x]:grouped[v//256].add(v%256)
        targets.update(grouped)
        if len(grouped)!=4 or any(len(y)!=4 for y in grouped.values()):
            if bad_vertex is None:bad_vertex={'vertex':256*g+x,'fiber_counts':{str(h):len(y) for h,y in grouped.items()}}
        for h,y in grouped.items():
            rows.setdefault((g,h),[None]*256)[x]=y
    fiber_neighborhoods.append(sorted(targets))

ports=[]
signatures={}
types=[]
affine_failures=[]
line_failure_count=0
for (g,h),table in sorted(rows.items()):
    if any(y is None for y in table):
        affine_failures.append({'g':g,'h':h,'reason':'missing rows'})
        continue
    c=min(table[0]);D=tuple(sorted(v^c for v in table[0]))
    first=next((v for v in D if v),None)
    is_line=first is not None and set(D)=={0,first,mul2[first],mul2[mul2[first]]}
    same_direction=is_line and all({v^min(y) for v in y}==set(D) for y in table)
    cols=[min(table[4**j])^c for j in range(4)]
    counterexample=None
    if same_direction:
        for x in range(256):
            predicted=c
            for j,col in enumerate(cols):predicted^=mul[x//4**j%4][col]
            if {predicted^d for d in D}!=table[x]:
                counterexample={'source_fiber':x,'actual':sorted(table[x]),'predicted':sorted(predicted^d for d in D)}
                break
    else:
        line_failure_count+=1
    affine=same_direction and counterexample is None
    record={'source_controller':g,'target_controller':h,'is_affine_F4_line_relation':affine,
            'D':D,'constant':c,'canonical_columns':cols}
    if not affine:
        record['counterexample']=counterexample
        affine_failures.append(record)
    signature=(D,c,tuple(cols))
    if signature not in signatures:
        signatures[signature]=len(types)
        types.append({'id':signatures[signature],'D':D,'constant':c,'canonical_columns':cols})
    record['relation_type']=signatures[signature]
    ports.append(record)

per_vertex_types=[[] for _ in range(64)]
for p in ports:per_vertex_types[p['source_controller']].append(p['relation_type'])
result={'status':'COMPLETE_AFFINE_INTERFACE_PROBE','n':n,'m_input_rows':edge_count,
        'degree_histogram':dict(Counter(map(len,adj))),
        'fiber_count':64,'fiber_size':256,'directed_controller_edges':len(rows),
        'controller_degree_histogram':dict(Counter(map(len,fiber_neighborhoods))),
        'vertex_partition_counterexample':bad_vertex,
        'all_directed_ports_affine_F4_lines':not affine_failures,
        'affine_relation_failure_count':len(affine_failures),
        'line_direction_failure_count':line_failure_count,
        'relation_type_count':len(types),
        'relation_type_histogram':dict(Counter(p['relation_type'] for p in ports)),
        'outgoing_type_set_histogram':dict(Counter(','.join(map(str,sorted(y))) for y in per_vertex_types)),
        'first_affine_counterexample':affine_failures[0] if affine_failures else None,
        'prediction_disposition':'SUPPORTED' if not affine_failures and bad_vertex is None else 'REFUTED',
        'field_encoding':'F4={0,1,alpha,alpha+1};alpha^2=alpha+1. Fiber byte=x0+4x1+16x2+64x3; characteristic2 addition XOR.',
        'source_D_reported':4,'source_D_BFS_repeated':False,
        'graph_BFS':0,'search':False,'CPU_seconds':time.process_time()-start,
        'running':False,'pending':[]}
(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(out/'INTERFACE.json').write_text(json.dumps({'controller_adjacency':fiber_neighborhoods,'relation_types':types,'directed_ports':ports},indent=2)+'\n')
(out/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
