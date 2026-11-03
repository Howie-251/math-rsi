"""The sole frozen C9/action4 transfer, with no parameter or chart search."""
from collections import Counter, deque
from itertools import product
from pathlib import Path
import json
import resource
import time

started = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
out = Path(__file__).resolve().parent
source_recipe = json.loads((out.parent/'construction.json').read_text())
charts = source_recipe['construction']['charts']
vectors = [tuple(x//3**i%3 for i in range(4)) for x in range(81)]
symbols = 'aAbBz'
inverse = [1,0,3,2,4]

def apply(M,x):
    return tuple(sum(a*b for a,b in zip(row,x))%3 for row in M)

def encode(x):
    return sum(a*3**i for i,a in enumerate(x))

relations = []
for chart in charts:
    rows=[]
    for x in vectors:
        center=apply(chart['M'],x)
        if chart['kind']=='plain':
            row={encode(tuple((a+b)%3 for a,b in zip(center,chart['d'])))}
        else:
            row={encode(tuple((a+k*b)%3 for a,b in zip(center,chart['d']))) for k in range(3)}
        rows.append(row)
    relations.append(rows)

def inverse_matrix(M):
    a=[list(row)+[int(i==j) for j in range(4)] for i,row in enumerate(M)]
    for j in range(4):
        pivot=next(i for i in range(j,4) if a[i][j])
        a[j],a[pivot]=a[pivot],a[j]
        z=pow(a[j][j],-1,3)
        a[j]=[z*x%3 for x in a[j]]
        for i in range(4):
            if i!=j:
                z=a[i][j]
                a[i]=[(x-z*y)%3 for x,y in zip(a[i],a[j])]
    return [row[4:] for row in a]

# Line-relation representatives normalized to genuinely inverse matrices.
# This is needed to justify freely reduced I/R2 packets for every fiber source.
for s,t in [(0,1),(2,3)]:
    invM=inverse_matrix(charts[s]['M'])
    direction=apply(invM,charts[s]['d'])
    for x in range(81):
        c=apply(invM,vectors[x])
        normalized={encode(tuple((a+k*b)%3 for a,b in zip(c,direction))) for k in range(3)}
        assert normalized==relations[t][x]
for s in range(5):
    assert all(x in relations[inverse[s]][y] for x in range(81) for y in relations[s][x])

line_words=[()] + [w for length in range(1,5) for w in product(range(4),repeat=length)]
images={():{0}}
for w in line_words[1:]:
    images[w]=set().union(*(relations[w[-1]][x] for x in images[w[:-1]]))

def reduce(w):
    result=[]
    for s in w:
        if result and inverse[s]==result[-1]:
            result.pop()
        else:
            result.append(s)
    return tuple(result)

short_packets={}
for w in line_words:
    r=reduce(w)
    if len(r) in [0,2]:
        short_packets.setdefault(r,set()).update(images[w])
certified_short=[w for w,p in short_packets.items() if len(p)==81]
reduced4=[w for w in product(range(4),repeat=4) if reduce(w)==w]
good4=[w for w in reduced4 if len(images[w])==81]
full_packets=json.loads((out.parent/'central_matching_packets/RESULT.json').read_text())['full_packets']

def multiply(g,h):
    i,j=g
    k,l=h
    return ((i+pow(4,j,9)*k)%9,(j+l)%12)

def inv(g):
    i,j=g
    return (-pow(4,-j,9)*i%9,-j%12)

a,b,z=(1,1),(0,4),(0,6)
generators=[a,inv(a),b,inv(b),z]
elements=[(i,j) for j in range(12) for i in range(9)]
indices={g:i for i,g in enumerate(elements)}
assert pow(4,3,9)==1 and multiply(z,z)==(0,0)
assert multiply(multiply(multiply(a,a),multiply(a,a)),inv(b))==(4,0)
assert all(multiply(z,g)==multiply(g,z) for g in elements)

def endpoint(w):
    g=(0,0)
    for s in w:
        g=multiply(g,generators[s])
    return g

certified={endpoint(w) for w in certified_short+good4}
for word in full_packets:
    certified.add(multiply(endpoint(tuple(symbols.index(s) for s in word)),z))
missing_cert=sorted(set(elements)-certified,key=indices.get)
certificate={
 'identity_short_packet_full':() in certified_short,
 'certified_reduced2_word_count':sum(len(w)==2 for w in certified_short),
 'good_reduced4_word_count':len(good4),
 'full_central_insertion_packet_count':len(full_packets),
 'controller_vertices_certified':len(certified),
 'controller_vertices':108,'missing_controller_elements':missing_cert,
 'scope':'Sufficient all-fiber-start I/R2/G4/central-insertion certificates. Inverse-consistent matrix representatives were checked against actual line relations.'}
(out/'CONTROLLER_CERTIFICATE.json').write_text(json.dumps(certificate,indent=2)+'\n')

transitions=[[indices[multiply(g,s)] for s in generators] for g in elements]
seen={0}
q=deque([0])
while q:
    for h in transitions[q.popleft()]:
        if h not in seen:
            seen.add(h)
            q.append(h)
assert len(seen)==108

n=108*81
edges=set()
for g in range(108):
    for x in range(81):
        u=81*g+x
        for s in range(5):
            for y in relations[s][x]:
                v=81*transitions[g][s]+y
                assert u!=v
                edges.add((min(u,v),max(u,v)))
adj=[[] for _ in range(n)]
for u,v in edges:
    adj[u].append(v)
    adj[v].append(u)
degree_hist=Counter(map(len,adj))
assert max(degree_hist)<=13

results=[]
witness=None
for source in range(81):
    d=[-1]*n
    parent=[-1]*n
    d[source]=0
    queue=deque([source])
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if d[v]<0:
                d[v]=d[u]+1
                parent[v]=u
                queue.append(v)
    missing=[v for v in range(n) if d[v]<0 or d[v]>4]
    reached=n-d.count(-1)
    results.append({'source':source,'reached':reached,'eccentricity':max(d) if reached==n else None,
                    'R4_missing_count':len(missing)})
    if missing:
        target=missing[0]
        path=[]
        if d[target]>=0:
            v=target
            while v!=source:
                path.append(v)
                v=parent[v]
            path.append(source)
            path.reverse()
        witness={'source':source,'source_controller':[0,0],'source_fiber':vectors[source],
                 'target':target,'target_controller':elements[target//81],
                 'target_fiber':vectors[target%81],'distance':d[target] if d[target]>=0 else None,
                 'shortest_path':path,'root_R4_missing_count':len(missing)}
        break

full=len(results)==81 and witness is None
if full:
    with (out/'candidate8748.edges').open('w') as f:
        for u,v in sorted(edges):
            f.write(f'{u} {v}\n')
    recipe=json.loads(json.dumps(source_recipe))
    recipe['order']=n
    recipe['construction']['controller']['group'].update(N=9,r=4)
    (out/'construction.json').write_text(json.dumps(recipe,indent=2)+'\n')

result={'status':'FULL_D4_GRAPH' if full else 'FIRST_ROOT_COUNTEREXAMPLE',
        'n':n,'m':len(edges),'simple':True,'degree_histogram':dict(degree_hist),
        'max_degree':max(degree_hist),'controller_connected':len(seen)==108,
        'graph_connected':results[0]['reached']==n,
        'root_checks':results,'roots_checked':len(results),'counterexample':witness,
        'actual_D':max(r['eccentricity'] for r in results) if full else None,
        'actual_D_lower_bound':witness['distance'] if witness and witness['distance'] else None,
        'representative_soundness':'Left multiplication L_h(g,x)=(h*g,x) preserves all right-generator transitions and the constant fiber chart. It moves every graph root to one of81 identity-fiber roots; thus81 complete checks suffice for all roots.',
        'source6804_BFS':0,'parameter_candidates_tested':1,
        'all_source_BFS':False,'edge_file_exported':full,
        'certificate_summary':{k:v for k,v in certificate.items() if k!='missing_controller_elements'},
        'CPU_seconds':time.process_time()-started,'running':False,'pending':[]}
(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(out/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
