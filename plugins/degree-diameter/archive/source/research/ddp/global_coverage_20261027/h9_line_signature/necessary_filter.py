from pathlib import Path
import json,time
from collections import Counter

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
started=time.process_time();K=41356
assert json.loads((OUT/'PREDICTION.json').read_text())['frozen_before_necessary_intersection_filter']
src=ROOT/'research/ddp/breadth_20261027_wave4/pencil_source/deg12_diam5_n42342.txt'
core=[]
with src.open() as f:
    for line in f:
        if not line.strip() or line.startswith('#'):continue
        z=list(map(int,line.split()))
        if z[0]>=K:break
        assert z[0]==len(core);core.append({v for v in z[1:] if v<K})
star=json.loads((ROOT/'research/ddp/global_coverage_20261027/h9_relation/star_containment.json').read_text())
records=[]
for r in star['records']:
    if r['category']!='non-star':continue
    Ai=set(r['A_i']);cand=set(Ai)
    for a in Ai:cand.update(core[a])
    centers=[];openmax=closedmax=0
    for v in sorted(cand):
        a=len(Ai&core[v]);b=a+(v in Ai)
        openmax=max(openmax,a);closedmax=max(closedmax,b)
        if b>=10:centers.append(dict(vertex=v,open_intersection=a,closed_intersection=b,
                                    core_degree=len(core[v]),center_in_Ai=v in Ai))
    records.append(dict(vertex=r['vertex'],A_i=sorted(Ai),pre165=r['vertex']<42177,
                        max_openstar_intersection=openmax,max_closedstar_intersection=closedmax,
                        necessary_closedstar_pass=closedmax>=10,necessary_openstar_pass=openmax>=10,
                        closedstar_candidate_centers=centers))
assert len(records)==810
def stats(rs):
    return dict(count=len(rs),closedstar_pass=sum(r['necessary_closedstar_pass'] for r in rs),
                openstar_pass=sum(r['necessary_openstar_pass'] for r in rs),
                open_intersection_histogram=dict(Counter(r['max_openstar_intersection'] for r in rs)),
                closed_intersection_histogram=dict(Counter(r['max_closedstar_intersection'] for r in rs)))
pre=[r for r in records if r['pre165']];post=[r for r in records if not r['pre165']]
bad=[r for r in pre if not r['necessary_openstar_pass']]
x=dict(status='COMPLETE_NECESSARY_LINE_IMAGE_SCREEN',prediction_id='P_line',
       prediction_outcome='FALSIFIED_BY_NECESSARY_CONDITION' if bad else 'NOT_FALSIFIED_NECESSARY_ONLY',
       all810=stats(records),pre165_675=stats(pre),final165_nonstar135=stats(post),
       first_pre165_failure=bad[0] if bad else None,
       records=records,geometric_line_signatures_reconstructed=False,
       incidence_graph_rebuilt=False,BFS_performed=False,default_verifier_imported=False,
       CPU_seconds=time.process_time()-started)
(OUT/'necessary_filter.json').write_text(json.dumps(x,indent=2)+'\n')
print(json.dumps({k:x[k] for k in ['prediction_outcome','all810','pre165_675','final165_nonstar135','CPU_seconds']},indent=2))
if bad:print('FIRST_FAILURE',json.dumps(bad[0]))
