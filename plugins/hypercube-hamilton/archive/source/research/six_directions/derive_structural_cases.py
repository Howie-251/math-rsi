"""Exact structural checks on existing witnesses, not exhaustive P6 verification."""
import json
from pathlib import Path
import networkx as nx
ROOT=Path(__file__).resolve().parent
data=json.loads((ROOT/'pilot_results_retry.json').read_text(encoding='utf8'))

def residual_completion(m,omit=()):
    used={z for e in m for z in e}|set(omit)
    free=set(range(64))-used
    g=nx.Graph();g.add_nodes_from(free)
    g.add_edges_from((a,b) for a in free for b in free if a<b and (a^b).bit_count()==1)
    return len(nx.max_weight_matching(g,maxcardinality=True))*2==len(free)

counts={}; residual=[]
for c in data['cases']:
    if c['n']!=6:continue
    m=c['matching'];v=c['v'];used={z for e in m for z in e}
    if len({a^b for a,b in m})<=5:label='known_at_most_five_directions'
    elif residual_completion(m):label='perfect_completion_lemma'
    elif v not in used and residual_completion(m,(0,v)):label='both_endpoints_uncovered_completion'
    else:
        label='not_closed_by_derived_lemmas'
        for i in range(6):
            if not(v>>i&1):continue
            cross=[(a,b) if not(a>>i&1) else (b,a) for a,b in m if (a^b)==1<<i]
            if len(cross)==1 and cross[0][0].bit_count()%2:
                label='single_bridge_lemma';break
    counts[label]=counts.get(label,0)+1
    if label=='not_closed_by_derived_lemmas':residual.append({'matching':m,'v':v})

gray=[i^(i>>1) for i in range(32)]
p=[0]
for j,x in enumerate(gray[1:],1):p+=([x,x+32] if j%2 else [x+32,x])
p.append(32)
m=[(a,a+32) for a in (3,5,6,9,10)]
used={z for e in m for z in e}
for i in range(5):
    eligible=[(a,b) for a,b in zip(p,p[1:]) if (a^b)==1<<i and a not in used and b not in used and a!=0 and b!=0]
    assert eligible
    e=eligible[0];m.append(e);used.update(e)
cross=[a if a<32 else b for a,b in m if (a^b)==32]
assert len(cross)==5 and all(a.bit_count()%2==0 for a in cross)
example={'n':6,'u':0,'v':32,'matching':m,'path':p,'status':'FOUND',
         'cut_direction_zero_based':5,'mandatory_even_crossings':5,
         'proved_lower_bound_on_cut_crossings':11}
(ROOT/'bridge_parity_example.json').write_text(json.dumps({'cases':[example]},indent=2),encoding='utf8')
summary={'scope':'classification of previous 1152 sampled Q6 cases only',
         'counts':counts,'first_residual_case':residual[0] if residual else None,
         'bridge_example_matching':m}
(ROOT/'structural_case_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf8')
print(json.dumps(summary))
