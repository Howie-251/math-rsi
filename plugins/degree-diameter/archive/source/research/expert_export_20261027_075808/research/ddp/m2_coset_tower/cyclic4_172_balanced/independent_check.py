"""Independent reconstruction and one all172root check of the saved cyclic lift."""
import json
import resource
import subprocess
import time
from pathlib import Path

start=time.process_time()
c0=resource.getrusage(resource.RUSAGE_CHILDREN)
out=Path(__file__).resolve().parent
project=out.parents[3]
saved=json.loads((out/'best.json').read_text())
edges=set()
for a,b,v in zip(saved['edge_u'],saved['edge_v'],saved['voltages']):
    assert 0<=a<b<4 and 0<=v<43
    for x in range(43):
        edges.add((43*a+x,43*b+(x+v)%43))
assert len(edges)==602
data=list(map(int,(out/'best.edges').read_text().split()))
assert data[:2]==[172,602] and len(data)==1206
actual=list(zip(data[2::2],data[3::2]))
assert len(set(actual))==602 and set(actual)==edges
run=subprocess.run([str(project/'computations/ddp/verify_graph'),str(out/'best.edges'),'7','3'],
                   capture_output=True,text=True)
assert run.returncode in (0,1),run.stderr
v=json.loads(run.stdout)
assert v['n']==v['roots_checked']==172 and v['m']==602
assert v['min_degree']==v['max_degree']==7
assert v['unreachable_unordered_pairs']==0
assert v['diameter']==saved['score']['diameter']==4
assert v['bad_unordered_pairs']==saved['score']['bad_unordered_pairs']==258
expected={str(d):43*sum(h.get(str(d),0) for h in saved['root_distance_histograms']) for d in range(5)}
assert v['ordered_distance_histogram']==expected
c1=resource.getrusage(resource.RUSAGE_CHILDREN)
own=time.process_time()-start
child=c1.ru_utime+c1.ru_stime-c0.ru_utime-c0.ru_stime
v.update(simple=True,connected=True,independent_edges_exactly_equal=True,
         independent_reconstruction_CPU_seconds=own,generic_checker_CPU_seconds=child,
         total_CPU_seconds=own+child,scope='One saved balanced322 cyclic4/172 best; one all172root check.')
(out/'best.independent_check.json').write_text(json.dumps(v,indent=2)+'\n')
print(json.dumps(v,indent=2))
