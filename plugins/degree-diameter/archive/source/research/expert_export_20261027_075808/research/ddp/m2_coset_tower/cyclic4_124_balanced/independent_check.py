"""One independent final check of the124-point saved balanced lift."""
from pathlib import Path
import json,resource,subprocess,time
HERE=Path(__file__).resolve().parent
assert not (HERE/'best.independent_check.json').exists(), 'Final graph already checked'
P=HERE.parents[3];Q=31;N=124;D=6;M=372
t=time.process_time();c0=resource.getrusage(resource.RUSAGE_CHILDREN)
s=json.loads((HERE/'best.json').read_text());expected=set()
for a,b,z in zip(s['edge_u'],s['edge_v'],s['voltages']):
    assert 0<=a<b<4 and 0<=z<Q
    for x in range(Q):expected.add(tuple(sorted((Q*a+x,Q*b+(x+z)%Q))))
data=list(map(int,(HERE/'best.edges').read_text().split()))
assert data[:2]==[N,M] and len(data)==2+2*M
actual=list(zip(data[2::2],data[3::2]))
assert len(actual)==len(set(actual))==len(expected)==M and set(actual)==expected
proc=subprocess.run([str(P/'computations/ddp/verify_graph'),str(HERE/'best.edges'),str(D),'3'],capture_output=True,text=True)
assert proc.returncode in (0,1),proc.stderr
r=json.loads(proc.stdout)
assert r['n']==r['roots_checked']==N and r['m']==M
assert r['min_degree']==r['max_degree']==D
assert r['unreachable_unordered_pairs']==0
assert r['bad_unordered_pairs']==s['score']['bad_unordered_pairs']==279
assert r['diameter']==s['score']['diameter']==4
hist={str(d):Q*sum(h.get(str(d),0) for h in s['root_distance_histograms']) for d in range(5)}
assert r['ordered_distance_histogram']==hist
c1=resource.getrusage(resource.RUSAGE_CHILDREN)
r.update(simple=True,connected=True,independent_edges_exactly_equal=True,
         CPU_seconds=time.process_time()-t+c1.ru_utime+c1.ru_stime-c0.ru_utime-c0.ru_stime,
         scope='Sole saved124-point graph;independent edge reconstruction and all124-root BFS')
(HERE/'best.independent_check.json').write_text(json.dumps(r,indent=2)+'\n')
term=json.loads((HERE/'terminal.json').read_text());term['pending']=[];term['final_verification']='best.independent_check.json'
(HERE/'terminal.json').write_text(json.dumps(term,indent=2)+'\n')
print(json.dumps(r,indent=2))
