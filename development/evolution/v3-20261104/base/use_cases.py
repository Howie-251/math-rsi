"""Bounded consumption of v3 interfaces; reads archives, never writes them."""
from pathlib import Path
from fractions import Fraction
import argparse
import json

parser = argparse.ArgumentParser()
root = Path(__file__).resolve().parents[4]
parser.add_argument('--erdos', type=Path, default=root/'plugins/hypercube-extremal/archive/source')
parser.add_argument('--hamilton', type=Path, default=root/'plugins/hypercube-hamilton/archive/source')
parser.add_argument('--ecc', type=Path, default=root/'plugins/ecc/archive/source')
a = parser.parse_args()

history = json.loads((a.erdos/'research/Q4_059970530_research/full_flags_history.json').read_text())
best = min(history, key=lambda row: row['full_upper'])
last = history[-1]
assert best['iteration'] == 178 and last['iteration'] == 179
assert best['full_upper'] < last['full_upper']
assert last['best_upper'] == best['full_upper']
deep = json.loads((a.erdos/'research/Q4_refined_research_20261027/deep_history.json').read_text())[0]
assert deep['upper'] > deep['best'] and deep['added'] == 800
result = json.loads((a.erdos/'certificate_final_q4/result_control.json').read_text())
assert Fraction(result['certified_bound']) < Fraction(result['outward_decimal'])

# Reproduce the pointed-domain omission with actual SOURCE_AUDIT input.
verts = set(range(4))
edges = {frozenset((u,v)) for u in verts for v in verts if u<v and (u^v).bit_count()==1}
m = {frozenset((2,3))}
covered = set().union(*m)
assert not any(not (set(e)&covered) for e in edges if 0 not in e)
assert any(not (set(e)&covered) for e in edges)
for path in [(0,1,3,2),(0,2,3,1)]:
    path_edges = {frozenset((x,y)) for x,y in zip(path,path[1:])}
    assert path_edges <= edges and m <= path_edges

# Read a real frozen A10 forest and find a compatible real matching column.
s = a.hamilton/'research/six_directions'
raw = (s/'A10_ORBIT3_UNIVERSAL_rank_selected_forests.bin').read_bytes()
pairs = (s/'A10_ORBIT3_UNIVERSAL_rank_selected_pairs.bin').read_bytes()
columns = (s/'A10_ORBIT3_UNIVERSAL_rank_columns.bin').read_bytes()
assert len(raw)==1024*40 and len(pairs)==len(columns)==1024*22
forest = list(zip(raw[:40:2],raw[1:40:2]))
assert len(set(forest))==20 and all((u^v).bit_count()==1 for u,v in forest)
adj = {v:[] for v in range(1,32)}
for u,v in forest:
    adj[u].append(v);adj[v].append(u)
holes = {0,1,2,4,8,15,23,27,29,30}
endpoints = set(range(32))-holes
assert all(len(adj[v])==(1 if v in endpoints else 2) for v in adj)
seen=set();computed=[]
for v in sorted(endpoints):
    if v in seen:continue
    component=set();stack=[v]
    while stack:
        x=stack.pop()
        if x in component:continue
        component.add(x);stack.extend(adj[x])
    assert component.isdisjoint(seen)
    seen |= component
    ends=sorted(component&endpoints)
    assert len(ends)==2
    assert sum(len(adj[x]) for x in component)//2==len(component)-1
    computed.append(tuple(ends))
assert seen == set(range(1,32))
stored=list(zip(pairs[:22:2],pairs[1:22:2]))
assert sorted(computed)==sorted(stored)
compatible=None
for j in range(1024):
    col=columns[j*22:(j+1)*22]
    f=list(zip(col[::2],col[1::2]))
    assert set(col)==endpoints and len(set(col))==22
    union={v:[] for v in endpoints}
    for u,v in computed+f:
        union[u].append(v);union[v].append(u)
    reached=set();todo=[min(endpoints)]
    while todo:
        x=todo.pop()
        if x not in reached:reached.add(x);todo.extend(union[x])
    if reached==endpoints:
        compatible=j;break
assert compatible is not None
review=json.loads((s/'A10_ORBIT3_UNIVERSAL_REVIEW_check.json').read_text())
assert review['GF2_rank_low_column_gauss']==1024
assert review['complete_spectrum_exhaustiveness_checked'] is False

lean=(a.ecc/'formal/ecc42/ECC42/Main.lean').read_text()
assert 'theorem nonexistence_of_proposition2 (hProp2 : Proposition2)' in lean
assert 'theorem nonexistence_explicit' in lean
assert '(hProp2 : ¬ ∃ D : Submodule F2 (Fin 41 → F2)' in lean
assert 'exact hProp2 (reduction_42_16_to_41_14 h)' in lean
print(json.dumps({
 'erdos':{'rows':len(history),'best_iteration':best['iteration'],'best_full':best['full_upper'],
          'last_iteration':last['iteration'],'last_full':last['full_upper'],
          'rejected_full':deep['upper'],'retained_exploration_best':deep['best'],'added_rows':deep['added'],
          'final_exact':result['certified_bound'],'outward_decimal':result['outward_decimal'],
          'caller_return':'Select iteration178 for that historical exploration; retain accepted certificate separately. Reject run0 threshold and request its violating row identities before continuing. Exact fraction outward rounding checked only; no full scan rerun.'},
 'q6':{'q2_omitted_matching':[[2,3]],'a10_forest_index':0,'forest_edges':len(forest),
       'compatible_saved_column':compatible,'historical_rank':review['GF2_rank_low_column_gauss'],
       'caller_return':'Q2 generator domain misses a valid pointed input, not a theorem counterexample. Actual A10 row0 is a legal short forest with stored endpoint map and compatible saved F; local positive caller checked. Universal span uses historical independent rank and explicit imported theorem, not this small run.'},
 'ecc42':{'explicit_parameter':'hProp2 : Proposition2','expanded_parameter_found':True,
          'caller_return':'Lean reduction accepts published Proposition2 as explicit input; standard axiom list cannot discharge it. Static type consumption only; no Lean build.'}
},ensure_ascii=False,indent=2))
