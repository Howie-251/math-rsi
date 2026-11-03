"""Independently rebuild and fully verify only the saved AGL(1,19) graph."""
import json
import resource
import subprocess
import time
from pathlib import Path

t0 = time.process_time()
c0 = resource.getrusage(resource.RUSAGE_CHILDREN)
out = Path(__file__).resolve().parent
project = out.parents[3]
saved = json.loads((out / 'production.best.json').read_text())
S = saved['S']
assert len(S) == len(set(S)) == 8 and 0 not in S
assert len({pow(2,j,19) for j in range(18)}) == 18

def multiply(a,b):
    x,j = a%19,a//19
    y,k = b%19,b//19
    return (x+pow(2,j,19)*y)%19 + 19*((j+k)%18)

def inverse(a):
    x,j = a%19,a//19
    return (-pow(2,-j,19)*x)%19 + 19*((-j)%18)

assert {inverse(a) for a in S} == set(S)
expected = {tuple(sorted((v,multiply(v,s)))) for v in range(342) for s in S}
data = list(map(int,(out/'production.best.edges').read_text().split()))
assert data[:2] == [342,1368] and len(data) == 2+2*1368
edges = list(zip(data[2::2],data[3::2]))
actual = {tuple(sorted(e)) for e in edges}
assert len(actual) == len(edges) == 1368
assert all(0 <= u < v < 342 for u,v in actual)
assert actual == expected

result = subprocess.run([str(project/'computations/ddp/verify_graph'),
                         str(out/'production.best.edges'),'8','3'],
                        capture_output=True,text=True)
assert result.returncode in (0,1), result.stderr
verified = json.loads(result.stdout)
assert verified['n'] == verified['roots_checked'] == 342
assert verified['m'] == 1368
assert verified['min_degree'] == verified['max_degree'] == 8
assert verified['unreachable_unordered_pairs'] == 0
assert verified['diameter'] == saved['graph']['diameter'] == 4
assert verified['bad_unordered_pairs'] == saved['graph']['bad_unordered_pairs'] == 7866
assert {int(d):n for d,n in verified['ordered_distance_histogram'].items()} == {
    int(d):342*n for d,n in saved['graph']['root_distance_histogram'].items()}
c1 = resource.getrusage(resource.RUSAGE_CHILDREN)
own = time.process_time()-t0
child = c1.ru_utime+c1.ru_stime-c0.ru_utime-c0.ru_stime
verified.update(simple=True,connected=True,independent_edges_exactly_equal=True,
                target_diameter=3,independent_reconstruction_CPU_seconds=own,
                generic_checker_CPU_seconds=child,total_CPU_seconds=own+child,
                scope='Only the saved best graph; one generic all342root BFS, no search or other graph.')
(out/'best.independent_verify.json').write_text(json.dumps(verified,indent=2)+'\n')
details = dict(verified,status='COMPLETE_ONE_SAVED_CAYLEY342_FULL_SOURCE_VERIFICATION',
               S=sorted(S),encoding='x+19*j',
               product='(x,j)(y,k)=(x+2^j*y mod19,j+k mod18)',
               all_root_ordered_histogram_matches_Cayley_root_weighting=True)
(out/'production.best.independent_check.json').write_text(json.dumps(details,indent=2)+'\n')
print(json.dumps(verified,indent=2))
