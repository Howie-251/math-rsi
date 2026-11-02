"""Two fixed actual-adjacency controls; no original-source BFS."""
from collections import Counter, deque
from pathlib import Path
import json
import resource
import time

START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (2, 2))
OUT = Path(__file__).resolve().parent
SOURCE = OUT.parent / 'source6804.edges'
N = 6804
F = 81
vectors = [tuple(x//3**i % 3 for i in range(4)) for x in range(F)]

def encode(x):
    return sum(c*3**i for i,c in enumerate(x))

def point(v):
    g,x = divmod(v,F)
    return {'vertex':v,'controller_id':g,'controller_element':[g%7,g//7],
            'fiber_id':x,'fiber_coordinates':vectors[x]}

# Parse the author's original edge file exactly once, separating its actual z edges.
original_edges = set()
line_edges = set()
old_matching = set()
for row in SOURCE.read_text().splitlines():
    if not row.strip() or row.startswith('#'):
        continue
    u,v = sorted(map(int,row.split()))
    assert 0 <= u < v < N and (u,v) not in original_edges
    original_edges.add((u,v))
    gu,x = divmod(u,F)
    gv,y = divmod(v,F)
    if gv == gu+42:
        expected = encode(tuple((int(i==2)-c)%3 for i,c in enumerate(vectors[x])))
        assert y == expected
        old_matching.add((u,v))
    else:
        line_edges.add((u,v))
assert len(original_edges)==44226 and len(old_matching)==3402 and len(line_edges)==40824
matching_degrees = Counter(v for e in old_matching for v in e)
assert len(matching_degrees)==N and set(matching_degrees.values())=={1}

new_matching = set()
for g in range(42):
    for x in range(F):
        y = encode(tuple(-c%3 for c in vectors[x]))
        e = (F*g+x,F*(g+42)+y)
        assert e not in line_edges
        new_matching.add(e)
assert len(new_matching)==3402

def adjacency(edges):
    result = [[] for _ in range(N)]
    for u,v in edges:
        result[u].append(v)
        result[v].append(u)
    return result

def depth4(adj,root):
    dist = [-1]*N
    dist[root]=0
    q=deque([root])
    while q:
        u=q.popleft()
        if dist[u]==4:
            continue
        for v in adj[u]:
            if dist[v]<0:
                dist[v]=dist[u]+1
                q.append(v)
    missing=[v for v,d in enumerate(dist) if d<0]
    classes=[]
    for g in range(84):
        fibers=[x for x in range(F) if dist[F*g+x]<0]
        if fibers:
            classes.append({'controller_id':g,'controller_element':[g%7,g//7],
                            'missing_fiber_ids':fibers,'missing_count':len(fibers),
                            'covered_fiber_count':F-len(fibers)})
    return {'root':point(root),'covered_count':N-len(missing),'missing_count':len(missing),
            'R4_layer_histogram':dict(Counter(d for d in dist if d>=0)),
            'first_missing_target':point(missing[0]) if missing else None,
            'missing_controller_fiber_classes':classes}

results=[]
for name,edges,degree,scope in [
    ('A_delete_all_z',line_edges,12,'FIRST_ROOT_THEN_81_REPRESENTATIVES_ONLY_IF_FIRST_FULL'),
    ('B_zero_affine_offset',line_edges|new_matching,13,'ONE_FIXED_IDENTITY_ZERO_ROOT')]:
    began=time.process_time()
    adj=adjacency(edges)
    hist=Counter(map(len,adj))
    assert hist==Counter({degree:N})
    checks=[depth4(adj,0)]
    full=False
    limited=False
    if name.startswith('A') and checks[0]['missing_count']==0:
        for root in range(1,F):
            if time.process_time()-START > 1.8:
                limited=True
                break
            checks.append(depth4(adj,root))
            if checks[-1]['missing_count']:
                break
        full=len(checks)==F and all(not c['missing_count'] for c in checks)
    counterexample=next((c for c in checks if c['missing_count']),None)
    result={'control':name,'scope':scope,'n':N,'m':len(edges),'simple':True,
            'degree_histogram':dict(hist),'max_degree':degree,
            'source_original_edges_parsed_once':True,'original_source_BFS':0,
            'root_checks':checks,'roots_checked':len(checks),
            'status':'FIRST_CHECKED_ROOT_REFUTES_D4' if counterexample else
                     'ALL_81_REPRESENTATIVES_FULL_D4' if full else
                     'CPU_LIMIT_UNKNOWN' if limited else 'FIXED_ROOT_FULL_ONLY',
            'prediction_disposition':'SUPPORTED' if counterexample else 'REFUTED' if full else 'UNDECIDED',
            'actual_D':None,'target_D':4,'finite_D4_property_refuted':counterexample is not None,
            'missing_targets_relative_to_original':'Original D4 is inherited, so every listed modified-root missing target was originally within4; original BFS not repeated.',
            'representative_soundness':'Left multiplication L_h(g,x)=(h*g,x) preserves right-generator controller edges and the constant fiber relation. Deleting z, or replacing its constant map by -I, preserves this action. Every root moves to one of81 identity-controller fiber roots.',
            'CPU_seconds':time.process_time()-began}
    if full:
        path=OUT/'control_A_degree12_D4_n6804.edges'
        with path.open('w') as f:
            f.write(f'{N} {len(edges)}\n')
            for u,v in sorted(edges):
                f.write(f'{u} {v}\n')
        result['edge_file']=str(path)
    (OUT/(name+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    results.append(result)

terminal={'status':'COMPLETE_TWO_FIXED_CONTROLS','source_file':str(SOURCE),
          'source_n':N,'source_m':len(original_edges),'source_D':4,
          'source_D_reused':True,'original_source_parse_count':1,'original_source_BFS':0,
          'old_z_matching_edges':len(old_matching),'new_c0_matching_edges':len(new_matching),
          'unchanged_line_edges':len(line_edges),'controls':[
              {k:r[k] for k in ['control','n','m','degree_histogram','roots_checked','status','prediction_disposition','actual_D','CPU_seconds']}
              | {'first_root_missing_count':r['root_checks'][0]['missing_count'],
                 'first_missing_target':r['root_checks'][0]['first_missing_target']} for r in results],
          'total_CPU_seconds':time.process_time()-START,'running':False,'pending':[]}
(OUT/'RESULT.json').write_text(json.dumps(terminal,indent=2)+'\n')
(OUT/'terminal.json').write_text(json.dumps(terminal,indent=2)+'\n')
print(json.dumps(terminal,indent=2))
