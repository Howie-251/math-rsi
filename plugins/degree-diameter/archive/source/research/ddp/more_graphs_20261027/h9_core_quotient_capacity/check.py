"""Only core-pair quotient capacity. No distances, optimization, or graph generation."""
import json
import lzma
import resource
import time
from array import array
from collections import Counter
from pathlib import Path

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
START=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(15,15))
assert json.loads((OUT/'PREDICTION.json').read_text())['frozen_before_capacity_check']
old=ROOT/'research/ddp/global_coverage_20261027'
fold=array('H');fold.frombytes((old/'h9_quadric_line_signature/point_to_core.u16.bin').read_bytes())
source=ROOT/'research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/tau.txt.xz'
with lzma.open(source,'rt') as stream:tau=list(map(int,stream.read().split()))
pairs=[]
originals=[]
for p in range(66430):
    q=tau[tau[p]]
    if p<q and fold[p]!=fold[q]:
        pairs.append(tuple(sorted((fold[p],fold[q]))))
        originals.append([p,q])
assert len(pairs)==len(set(pairs))==7959
partner={}
for a,b in pairs:
    assert a not in partner and b not in partner
    partner[a]=b;partner[b]=a
assert len(partner)==15918 and max(partner)<41356

adj=[]
path=ROOT/'research/ddp/breadth_20261027_wave4/pencil_source/deg12_diam5_n42342.txt'
with path.open() as stream:
    for line in stream:
        if not line.strip() or line.startswith('#'):continue
        r=list(map(int,line.split()));assert r[0]==len(adj);adj.append(r[1:])
assert len(adj)==42342
records=[]
for v in range(41356,42342):
    if len(adj[v])!=12:continue
    neighbors=set(adj[v])
    hits=sorted((u,partner[u]) for u in neighbors if u in partner and u<partner[u] and partner[u] in neighbors)
    records.append(dict(vertex=v,degree=12,neighbors=sorted(neighbors),
                        complete_mergeable_core_pairs=[list(x) for x in hits],
                        complete_pair_count=len(hits),degree_after_all_corepairs_merged=12-len(hits),
                        degree12_invariant=not hits))
bad=[r for r in records if r['degree12_invariant']]
result=dict(prediction_id='H9_CORE_ONLY_QUOTIENT_DELTA11',status='COMPLETE_NECESSARY_CAPACITY_CHECK',
            prediction_outcome='SUPPORTED_DEGREE12_INVARIANT_EXTRA_EXISTS' if bad else 'REFUTED_NO_SUCH_EXTRA',
            fixed_graph_n=42342,fixed_graph_m=sum(map(len,adj))//2,core_n=41356,
            allowed_disjoint_split_corepairs=7959,extras_total=986,degree12_extras=len(records),
            degree12_invariant_extras=len(bad),degree12_extras_with_at_least_one_mergeable_neighbor_pair=len(records)-len(bad),
            mergeable_neighbor_pair_count_histogram=dict(Counter(r['complete_pair_count'] for r in records)),
            first_invariant_witness=bad[0] if bad else None,
            core_only_quotient_retaining_all_extras_can_have_Delta11=False if bad else None,
            pairs=[dict(core_pair=list(pair),original_phi_pair=orig) for pair,orig in zip(pairs,originals)],
            records=records,BFS_performed=False,MIP_or_search_performed=False,
            new_graph_generated=False,pending=[],CPU_seconds=time.process_time()-START,
            scope='Original42342 source only; merge chosen subsets of7959 disjoint core phi-pairs, keep all extras distinct and retain all quotient edges.')
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['pairs','records']},indent=2))
