"""Bind char3 cross conventions to actual F9 points/lines; no BFS."""
import resource
resource.setrlimit(resource.RLIMIT_CPU, (2, 2))
resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
from array import array
from collections import Counter
import json
from pathlib import Path
import time

HERE = Path(__file__).resolve().parent
BOUND = HERE.parent/'h9_exact_binding'
N = 66430
raw = (BOUND/'point_coords.u8.bin').read_bytes()
points = [tuple(raw[7*i:7*i+7]) for i in range(N)]
point_index = {p:i for i,p in enumerate(points)}
assert len(point_index) == N
line_array = array('i')
line_array.frombytes((BOUND/'line_points.i32.bin').read_bytes())
assert len(line_array) == 10*N
lines = [line_array[10*i:10*i+10] for i in range(N)]
incidence = [[] for _ in range(N)]
for line_id, line in enumerate(lines):
    for p in line:
        incidence[p].append(line_id)
assert all(len(row)==10 for row in incidence)

A = [[(a%3+b%3)%3+3*((a//3+b//3)%3) for b in range(9)] for a in range(9)]
M = [[((a%3)*(b%3)-(a//3)*(b//3))%3+
      3*(((a%3)*(b//3)+(a//3)*(b%3))%3) for b in range(9)] for a in range(9)]
neg = [(-a%3)+3*(-(a//3)%3) for a in range(9)]
inverse = [0]+[next(b for b in range(1,9) if M[a][b]==1) for a in range(1,9)]


def sum_field(values):
    result = 0
    for value in values:
        result = A[result][value]
    return result


def norm(p):
    return A[sum_field(M[p[i]][p[i+4]] for i in range(3))][neg[M[p[3]][p[3]]]]


def beta(p,q):
    return A[sum_field([M[p[i]][q[i+4]] for i in range(3)]+
                       [M[q[i]][p[i+4]] for i in range(3)])][M[p[3]][q[3]]]


def cross(p,q):
    output = []
    for i in range(3):
        j,k = (i+1)%3,(i+2)%3
        output.append(sum_field([M[p[3]][q[i]],neg[M[q[3]][p[i]]],
                                 M[p[j+4]][q[k+4]],neg[M[p[k+4]][q[j+4]]]]))
    output.append(sum_field([M[p[i]][q[i+4]] for i in range(3)]+
                            [neg[M[p[i+4]][q[i]]] for i in range(3)]))
    for i in range(3):
        j,k = (i+1)%3,(i+2)%3
        output.append(sum_field([M[q[3]][p[i+4]],neg[M[p[3]][q[i+4]]],
                                 M[p[j]][q[k]],neg[M[p[k]][q[j]]]]))
    return tuple(output)


def normalize(p):
    lead = next((a for a in p if a),None)
    return None if lead is None else tuple(M[inverse[lead]][a] for a in p)


assert all(norm(p)==0 and normalize(p)==p for p in points)
zero = (0,)*7
for line in lines:
    p,q = points[line[0]],points[line[1]]
    assert p!=q and beta(p,q)==0 and cross(p,q)==zero


def common_line(p,q):
    intersection = set(incidence[p]).intersection(incidence[q])
    assert len(intersection)==1
    return next(iter(intersection))


tests = []
for p in [0,1,2,8,9,80,81,728,729,7380,7381,16607,33215,44286,66429]:
    for line_id in [0,1,2,9,10,80,81,728,729,7381,16607,33215,44286,50000,60000,66429]:
        u,v = points[lines[line_id][0]],points[lines[line_id][1]]
        a,b = beta(points[p],u),beta(points[p],v)
        if a==0:
            q = lines[line_id][0]
        elif b==0:
            q = lines[line_id][1]
        else:
            q_coords = tuple(A[M[b][x]][neg[M[a][y]]] for x,y in zip(u,v))
            q = point_index[normalize(q_coords)]
        assert q in lines[line_id] and beta(points[p],points[q])==0
        witness = cross(points[p],points[q])
        r = None
        if p==q:
            path = [p,N+line_id]
        elif witness==zero:
            path = [p,N+common_line(p,q),q,N+line_id]
        else:
            assert norm(witness)==0
            r = point_index[normalize(witness)]
            assert r not in (p,q)
            assert cross(points[p],points[r])==cross(points[q],points[r])==zero
            path = [p,N+common_line(p,r),r,N+common_line(r,q),q,N+line_id]
        for x,y in zip(path,path[1:]):
            point,line = (x,y-N) if x<N else (y,x-N)
            assert point in lines[line]
        assert len(path)-1<=5
        tests.append(dict(point=p,line=line_id,orthogonal_point=q,cross_point=r,incidence_walk=path))
result = dict(status='ACTUAL_F9_COORDINATES_AND_EXPLICIT_ROUTES_PASS',
              raw_Q_points_checked=N, all_line_basis_pairs_checked=N,
              line_basis_cross_zero=True, fixed_point_line_cases=len(tests),
              walk_length_histogram=dict(Counter(len(x['incidence_walk'])-1 for x in tests)),
              source_BFS=0, geometry_rebuilt=False, new_graphs=0, Lean=0,
              CPU_seconds=time.process_time(), CPU_cap=2,
              scope='Exact all-line-basis coordinate binding and240 fixed route conventions; universal coverage comes from separately checked symbolic identities, not sampling.')
(HERE/'ROUTES.json').write_text(json.dumps(tests,indent=2)+'\n')
(HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
