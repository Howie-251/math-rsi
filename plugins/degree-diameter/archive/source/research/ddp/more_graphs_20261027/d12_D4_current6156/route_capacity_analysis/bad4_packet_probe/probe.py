"""One frozen four-word packet; no controller or voltage-grid search."""
from collections import Counter
from itertools import product
from pathlib import Path
import json
import resource
import time

started = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (1, 1))
out = Path(__file__).resolve().parent
recipe = json.loads((out.parent.parent / 'construction.json').read_text())['construction']
charts = recipe['charts']
symbols = 'aAbB'
words = ['AABa', 'Abaa', 'Babb', 'BBAb']
vectors = [tuple(i // (3 ** j) % 3 for j in range(4)) for i in range(81)]
relations = []
for chart in charts:
    M, d = chart['M'], chart['d']
    rows = []
    for x in vectors:
        center = [sum(M[i][j] * x[j] for j in range(4)) % 3 for i in range(4)]
        rows.append({sum(((center[i] + k*d[i]) % 3) * 3**i for i in range(4)) for k in range(3)})
    relations.append(rows)

def image(word, x):
    reached = {x}
    for symbol in word:
        table = relations[symbols.index(symbol)]
        reached = set().union(*(table[y] for y in reached))
    return reached

def rank(rows):
    a = [list(r) for r in rows]
    k = 0
    for j in range(4):
        pivot = next((i for i in range(k, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[k], a[pivot] = a[pivot], a[k]
        z = pow(a[k][j], -1, 3)
        a[k] = [(z * v) % 3 for v in a[k]]
        for i in range(len(a)):
            if i != k:
                z = a[i][j]
                a[i] = [(x-z*y) % 3 for x, y in zip(a[i], a[k])]
        k += 1
        if k == len(a):
            break
    return k

perms = [s['perm'] for s in recipe['controller']['symbols']]
inverse = [[p.index(i) for i in range(4)] for p in perms]
def endpoint(word):
    current, coeff = 0, [0] * 8
    for char in word:
        symbol = symbols.index(char)
        kind = symbol // 2
        if symbol % 2:
            current = inverse[kind][current]
            coeff[4*kind+current] -= 1
        else:
            coeff[4*kind+current] += 1
            current = perms[kind][current]
    # va=(0,x,y,0), vb=(z,0,0,1)
    return {'target_base':current, 'full_8_coefficients':coeff,
            'x_y_z_constant':[coeff[1], coeff[2], coeff[4], coeff[7]],
            'm20_y9_phase':(9*coeff[2]+coeff[7]) % 20}

zero_images = [image(word, 0) for word in words]
normals = []
for reached in zero_images:
    choices = [n for n in vectors[1:]
               if all(sum(x*y for x,y in zip(n,vectors[z])) % 3 == 0 for z in reached)]
    assert len(reached) == 27 and len(choices) == 2
    n = choices[0]
    first = next(z for z in n if z)
    normals.append(tuple(x * pow(first,-1,3) % 3 for x in n))

rows = []
for x in range(81):
    route_images = [image(word,x) for word in words]
    reached = set().union(*route_images)
    constants = [next(iter({sum(a*b for a,b in zip(n,vectors[y])) % 3 for y in ys}))
                 for n,ys in zip(normals,route_images)]
    rows.append({'source_id':x,'source_coordinates':vectors[x],
                 'union_size':len(reached),'hyperplane_constants':constants,
                 'missing_ids':sorted(set(range(81))-reached)})

result = {
    'status':'COMPLETE_SINGLE_PACKET_PROBE',
    'packet':words,
    'controller_endpoints':[endpoint(word) for word in words],
    'normal_coordinate_order':['x0','x1','x2','x3'],
    'normalized_normals':normals,
    'normal_span_rank':rank(normals),
    'distinct_projective_normals':len(set(normals)),
    'each_zero_image_size':[len(r) for r in zero_images],
    'zero_source_union_size':rows[0]['union_size'],
    'all_source_union_size_histogram':dict(Counter(r['union_size'] for r in rows)),
    'all_81_source_union_full':all(r['union_size']==81 for r in rows),
    'prediction_disposition':'SUPPORTED' if all(r['union_size']==81 for r in rows) else 'REFUTED',
    'first_counterexample':next((r for r in rows if r['union_size']!=81),None),
    'sources':rows,
    'CPU_seconds':time.process_time()-started,
    'graph_generated':False,'BFS':0,'voltage_grid_assignments':0,
    'old_universal_wide_meaning':'Hypothetical all108 full-rank reduced4 chart coverage; not an actual current-chart packet certificate.'}
(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='sources'},indent=2))
