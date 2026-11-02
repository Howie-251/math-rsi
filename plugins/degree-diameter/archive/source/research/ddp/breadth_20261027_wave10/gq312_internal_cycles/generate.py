"""Construct W(3,5) incidence from coordinates; no graph BFS or optimization."""
from itertools import product, combinations
from pathlib import Path
from collections import Counter
import json
import time

HERE = Path(__file__).resolve().parent
Q = 5

def normalize(x):
    lead = next(a for a in x if a)
    inv = pow(lead, -1, Q)
    return tuple(a * inv % Q for a in x)

def symplectic(x, y):
    return (x[0]*y[1]-x[1]*y[0]+x[2]*y[3]-x[3]*y[2]) % Q

def generate():
    started = time.process_time()
    points = sorted({normalize(x) for x in product(range(Q), repeat=4) if any(x)})
    index = {x:i for i,x in enumerate(points)}
    lines = set()
    for u,v in combinations(points, 2):
        if symplectic(u,v):
            continue
        line = tuple(sorted({index[normalize(tuple((a*u[k]+b*v[k])%Q for k in range(4)))]
                             for a,b in product(range(Q), repeat=2) if a or b}))
        lines.add(line)
    lines = sorted(lines)
    incidence = [(p, 156+j) for j,line in enumerate(lines) for p in line]
    point_lines = [set() for _ in points]
    for p,l in incidence:
        point_lines[p].add(l-156)
    closed = [{j for j,v in enumerate(points) if symplectic(u,v)==0} for u in points]
    assert len(points)==len(lines)==156 and len(incidence)==936
    assert all(len(x)==6 for x in lines) and all(len(x)==6 for x in point_lines)
    assert all(len(x)==31 for x in closed)
    assert all(len(closed[i]&closed[j])==6 for i,j in combinations(range(156),2))
    assert all(sum(p in closed[u] for p in line)==1
               for u in range(156) for line in lines if u not in line)
    result = dict(field=5, dimension=4,
                  symplectic_form='x0*y1-x1*y0+x2*y3-x3*y2 mod5',
                  point_normalization='first nonzero coordinate is1; lex sorted',
                  line_normalization='sorted6 point IDs; lex sorted lines',
                  vertex_encoding='points0..155; lines156..311',
                  points=points, lines=lines, point_count=156, line_count=156,
                  incidence_edges=936, incidence_degree=6,
                  closed_collinearity_size=31,
                  closed_collinearity_pair_intersection=6,
                  same_part_noncollinear_unordered_pairs_each=9750,
                  nonincident_point_line_unique_collinear=True,
                  graph_BFS_performed=False,
                  CPU_seconds=time.process_time()-started)
    (HERE/'geometry.json').write_text(json.dumps(result, indent=2)+'\n')
    with (HERE/'incidence.edges').open('w') as f:
        f.write('312 936\n')
        for u,v in incidence:
            f.write(f'{u} {v}\n')
    return result

if __name__=='__main__':
    d=generate()
    print(json.dumps({k:v for k,v in d.items() if k not in ['points','lines']}))
