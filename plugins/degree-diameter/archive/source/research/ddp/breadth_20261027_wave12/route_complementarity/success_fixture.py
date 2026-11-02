"""Targeted certificate comparison, not a rerun of graph BFS or chart search."""
from pathlib import Path
from itertools import product
import json
import time

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
SOURCE = ROOT/'research/ddp/breadth_20261027_wave5/mizuno_d4_source'
started = time.process_time()
d = json.loads((SOURCE/'construction.json').read_text())
routes = json.loads((SOURCE/'controller_routes.json').read_text())['representatives']
fixture = min((r['source'],t['target'],t['word']) for r in routes for t in r['targets'] if t['type']=='pencil')
u,v,w2 = fixture
pencil = next(p for p in json.loads((SOURCE/'pencil_routes.json').read_text()) if p['reduced_word']==w2)
controller = json.loads((SOURCE/'controller72.labels.json').read_text())['out']

def points(q):
    return list(product(range(q),repeat=4))

def add(x,y,q):
    return tuple((a+b)%q for a,b in zip(x,y))

def encode(x,q):
    return sum(c*q**i for i,c in enumerate(x))

def mv(A,x,q):
    return tuple(sum(a*b for a,b in zip(row,x))%q for row in A)

def endpoints(word,q,A,b,x):
    states = {tuple(x)}
    for t in word:
        states = {add(mv(A[t],z,q),tuple(lam*c%q for c in b[t]),q)
                  for z in states for lam in range(q)}
    return states

wordnums = lambda word:tuple('ABCD'.index(t) for t in word)
words = [wordnums(w) for w in pencil['four_route_words']]
for word in words:
    a = u
    for t in word:
        a = controller[a][t]
    assert a==v
A,b = d['matrices'],d['control_vectors']
zero = (0,)*4
spaces = [endpoints(w,3,A,b,zero) for w in words]
assert [len(s) for s in spaces]==[27]*4
assert all({encode(x,3) for x in s}==set(c) for s,c in zip(spaces,pencil['hyperplane_points']))
core = set.intersection(*spaces)
assert len(core)==9 and len(set.union(*spaces))==81
all_source_union_sizes = []
same_drift = True
for x in points(3):
    drift = x
    for t in wordnums(w2):
        drift = mv(A[t],drift,3)
    route_sets = [endpoints(w,3,A,b,x) for w in words]
    all_source_union_sizes.append(len(set.union(*route_sets)))
    for S,R in zip(spaces,route_sets):
        same_drift &= R=={add(drift,z,3) for z in S}
assert set(all_source_union_sizes)=={81} and same_drift
out = dict(status='INHERITED_SUCCESS_PENCIL_CONFIRMED_IN_TARGETED_FIXTURE',
    selection_rule='lexicographically first source/target marked pencil in original controller_routes.json',
    source_base=u,target_base=v,reduced_word=w2,route_words=pencil['four_route_words'],
    field=3,dimension=4,image_cardinalities=[len(s) for s in spaces],
    intersection_cardinality=len(core),zero_source_union_cardinality=81,
    all81_start_fibers_union_cardinalities=all_source_union_sizes,
    route_linear_drift_equals_reduced_word_drift=same_drift,
    interpretation='Four distinct hyperplanes through a shared two-dimensional core cover the two-dimensional quotient, not merely four paths counted with multiplicity.',
    inherited_fact_not_claimed_new=True,graph_BFS_performed=False,chart_search_performed=False,
    CPU_seconds=time.process_time()-started)
(OUT/'ternary_success_fixture.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='all81_start_fibers_union_cardinalities'},ensure_ascii=False))
