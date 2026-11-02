"""Reconstruct the saved nonregular affine graph and independently check all172 roots once."""
from pathlib import Path
from collections import Counter
import json,resource,subprocess,time
HERE=Path(__file__).resolve().parent
assert not (HERE/'best.independent_check.json').exists()
P=HERE.parents[3];Q=43;N=172
t=time.process_time();c0=resource.getrusage(resource.RUSAGE_CHILDREN)
s=json.loads((HERE/'best.json').read_text());expected=set()
for u,v,a,b in zip(s['edge_u'],s['edge_v'],s['slopes'],s['fixed_intercepts']):
    assert 0<=u<v<4 and 0<a<Q and 0<=b<Q
    for x in range(Q):expected.add(tuple(sorted((Q*u+x,Q*v+(a*x+b)%Q))))
data=list(map(int,(HERE/'best.edges').read_text().split()))
assert data[:2]==[172,601] and len(data)==1204
actual=list(zip(data[2::2],data[3::2]))
assert len(actual)==len(set(actual))==len(expected)==601 and set(actual)==expected
degree=Counter(x for e in expected for x in e)
assert Counter(degree.values())=={6:2,7:170}
proc=subprocess.run([str(P/'computations/ddp/verify_graph'),str(HERE/'best.edges'),'7','3'],capture_output=True,text=True)
assert proc.returncode in (0,1),proc.stderr
r=json.loads(proc.stdout)
assert r['n']==r['roots_checked']==172 and r['m']==601
assert r['min_degree']==6 and r['max_degree']==7
assert r['unreachable_unordered_pairs']==0
assert r['bad_unordered_pairs']==s['score']['bad_unordered_pairs']==666
assert r['diameter']==s['score']['diameter']==4
assert r['ordered_distance_histogram']==s['ordered_distance_histogram']
c1=resource.getrusage(resource.RUSAGE_CHILDREN)
r.update(simple=True,connected=True,independent_edges_exactly_equal=True,
         degree_histogram={str(k):v for k,v in Counter(degree.values()).items()},
         degree6_vertices=sorted(k for k,v in degree.items() if v==6),
         CPU_seconds=time.process_time()-t+c1.ru_utime+c1.ru_stime-c0.ru_utime-c0.ru_stime,
         scope='Only sole final nonregular graph; affine edge reconstruction and172-root BFS')
(HERE/'best.independent_check.json').write_text(json.dumps(r,indent=2)+'\n')
term=json.loads((HERE/'terminal.json').read_text());term['pending']=[];term['final_verification']='best.independent_check.json'
(HERE/'terminal.json').write_text(json.dumps(term,indent=2)+'\n')
print(json.dumps(r,indent=2))

