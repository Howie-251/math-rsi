"""Independently reconstruct the sole saved surgery result and check all172 roots once."""
from pathlib import Path
import json,resource,subprocess,time
HERE=Path(__file__).resolve().parent
assert not (HERE/'best.independent_check.json').exists(), 'Saved final graph already checked'
P=HERE.parents[3]
t=time.process_time();c0=resource.getrusage(resource.RUSAGE_CHILDREN)
s=json.loads((HERE/'best.json').read_text());expected=set()
for a,b,z in zip(s['edge_u'],s['edge_v'],s['voltages']):
    assert 0<=a<=b<4 and 0<=z<43 and (a!=b or z!=0)
    for x in range(43):expected.add(tuple(sorted((43*a+x,43*b+(x+z)%43))))
data=list(map(int,(HERE/'best.edges').read_text().split()))
assert data[:2]==[172,602] and len(data)==1206
actual=list(zip(data[2::2],data[3::2]))
assert len(actual)==len(set(actual))==len(expected)==602 and set(actual)==expected
result=subprocess.run([str(P/'computations/ddp/verify_graph'),str(HERE/'best.edges'),'7','3'],capture_output=True,text=True)
assert result.returncode in (0,1),result.stderr
r=json.loads(result.stdout)
assert r['n']==r['roots_checked']==172 and r['m']==602
assert r['min_degree']==r['max_degree']==7
assert r['unreachable_unordered_pairs']==0
assert r['bad_unordered_pairs']==s['score']['bad_unordered_pairs']==473
assert r['diameter']==s['score']['diameter']==4
hist={str(d):43*sum(h.get(str(d),0) for h in s['root_distance_histograms']) for d in range(5)}
assert r['ordered_distance_histogram']==hist
c1=resource.getrusage(resource.RUSAGE_CHILDREN)
r.update(simple=True,connected=True,independent_edges_exactly_equal=True,
         CPU_seconds=time.process_time()-t+c1.ru_utime+c1.ru_stime-c0.ru_utime-c0.ru_stime,
         scope='Only sole saved final surgery graph; independent edge reconstruction and172-root BFS')
(HERE/'best.independent_check.json').write_text(json.dumps(r,indent=2)+'\n')
term=json.loads((HERE/'terminal.json').read_text());term['pending']=[];term['final_verification']='best.independent_check.json'
(HERE/'terminal.json').write_text(json.dumps(term,indent=2)+'\n')
print(json.dumps(r,indent=2))
