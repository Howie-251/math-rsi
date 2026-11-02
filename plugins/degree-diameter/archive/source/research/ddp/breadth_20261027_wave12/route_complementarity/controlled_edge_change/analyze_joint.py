"""Exactly one complete225-assignment joint diagnostic on the prescribed two edges."""
import json,resource,sys,time
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(1,1))
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[4]
sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen
start=time.process_time()
source=ROOT/'research/ddp/breadth_20261027_wave11/binary72_tight_words/best_parameters.json'
tight_source=ROOT/'research/ddp/breadth_20261027_wave10/binary1152_edge_local/unique4_controller_slots.json'
d=json.loads(source.read_text());gp=d['global_label_parameters'];assert gp['passer_id']==68
adj=d['controller_out'];mats=gp['matrix_columns'];bs=gp['b_codes'];inv=d['inverse_labels']
assert gp['offsets']==[0,0,0,0] and adj[0][0]==18 and adj[36][1]==0

def action(cols,x):
    y=0
    for i in range(4):
        if x&(1<<i):y^=cols[i]
    return y
maps=[[action(c,x) for x in range(16)] for c in mats]
def rank(cols):
    piv=[0]*4
    for x in cols:
        for i in range(3,-1,-1):
            if x&(1<<i):
                if piv[i]:x^=piv[i]
                else:piv[i]=x;break
    return sum(bool(x) for x in piv)
def route(src,word,bfirst,bsecond):
    u=src;cols=[];path=[src]
    for t in word:
        v=adj[u][t]
        if (u,v)==(0,18):b=bfirst
        elif (u,v)==(18,0):b=maps[3][bfirst]
        elif (u,v)==(36,0):b=bsecond
        elif (u,v)==(0,36):b=maps[2][bsecond]
        else:b=bs[t]
        cols=[maps[t][x] for x in cols]+[b]
        u=v;path.append(u)
    return dict(source=src,target=u,word=word,path=path,columns=cols,rank=rank(cols))
slots=json.loads(tight_source.read_text())['slots'];assert len(slots)==468
baseline=[route(s['source'],s['word'],1,3) for s in slots]
assert all(r['rank']==4 for r in baseline)
changed={frozenset((0,18)),frozenset((36,0))}
affected=[i for i,r in enumerate(baseline) if any(frozenset(e) in changed for e in zip(r['path'],r['path'][1:]))]
records=[]
for bfirst in range(1,16):
    target=route(0,[0,0,2,0],bfirst,3)
    for bsecond in range(1,16):
        damage=[]
        for i in affected:
            s=slots[i];r=route(s['source'],s['word'],bfirst,bsecond)
            assert r['target']==s['target']
            if r['rank']<4:
                damage.append(dict(slot_index=i,source=r['source'],target=r['target'],word=r['word'],path=r['path'],
                                   original_columns=baseline[i]['columns'],columns=r['columns'],rank=r['rank'],
                                   missing_per_source_fiber_root=16-(1<<r['rank']),missing_ordered_fiber_pairs=16*(16-(1<<r['rank']))))
        records.append(dict(bfirst=bfirst,bsecond=bsecond,reverse_bfirst=maps[3][bfirst],reverse_bsecond=maps[2][bsecond],
                            target_AACA_columns=target['columns'],target_AACA_rank=target['rank'],damage_count=len(damage),damage_slots=damage))
assert len(records)==225
fixers=[r for r in records if r['target_AACA_rank']==4]
feasible=[r for r in fixers if r['damage_count']==0]
selected=min(feasible,key=lambda r:(r['bfirst'],r['bsecond'])) if feasible else None
best=min(fixers,key=lambda r:(r['damage_count'],r['bfirst'],r['bsecond']))
x=dict(status='COMPLETE_JOINT225_LINEAR_DIAGNOSTIC_NO_GRAPH',prediction_id='P4_JOINT_TWO_EDGE_TIGHT_PRESERVATION',
       source=str(source.relative_to(ROOT)),tight_slots_source=str(tight_source.relative_to(ROOT)),passer_id=68,
       changed_edges=[dict(forward=[0,18],label=0,T_columns=mats[0],Tinv_columns=mats[3],original_b=1),
                      dict(forward=[36,0],label=1,T_columns=mats[1],Tinv_columns=mats[2],original_b=3)],
       fixed_scope='All144 matrices, all offsets0, and other142 edge branch relations retained; only these two nonzero branch vectors vary',
       assignments_examined=225,all_tight_slots=468,affected_tight_slots=len(affected),affected_tight_slot_indices=affected,
       unaffected_slot_proof='A route whose controller path contains neither prescribed undirected edge has identical branch columns for every assignment and retains original rank4',
       target_rank4_assignments=len(fixers),feasible_count=len(feasible),selected_feasible=selected,
       minimum_damage_given_target_rank4=best['damage_count'],best_damage_assignment=best,
       selection_rule='If feasible, lexicographically first bfirst,bsecond with target rank4 and all468tight rank4. If none, minimum damage then same lexicographic tie-break for diagnosis only.',
       target_prediction_all256_covered=True if selected else None,tight_prediction_all468_preserved=True if selected else None,
       records=records,graph_generated=False,full_graph_score_computed=False,BFS_count=0,solver_calls=0,
       general_edge_local_excluded=False,third_edge_considered=False,
       next_action='root may freeze and generate only the selected feasible twoedge graph' if selected else 'close prescribed225slice without thirdedge expansion',
       CPU_seconds=time.process_time()-start)
def strings(x):
    if isinstance(x,str):return [x]
    if isinstance(x,dict):return [s for y in x.values() for s in strings(y)]
    if isinstance(x,list):return [s for y in x for s in strings(y)]
    return []
assert not screen('\n'.join(strings(x)))
(HERE/'joint_two_edge_analysis.json').write_text(json.dumps(x,indent=2)+'\n')
if selected:
    params=dict(source=str(source.relative_to(ROOT)),selection='lexicographic first feasible of complete225joint assignments',
                edge_changes=[dict(forward=[0,18],b=selected['bfirst'],reverse_b=selected['reverse_bfirst']),
                              dict(forward=[36,0],b=selected['bsecond'],reverse_b=selected['reverse_bsecond'])],
                all_other_T_b_offsets_unchanged=True,prediction_target0_to10_missing0=True,prediction_all468tight_missing0=True)
    (HERE/'joint_selected_parameters.json').write_text(json.dumps(params,indent=2)+'\n')
print(json.dumps(dict(examined=225,affected=len(affected),target_rank4=len(fixers),feasible=len(feasible),
                     selected=None if selected is None else (selected['bfirst'],selected['bsecond']),
                     min_damage=best['damage_count'],best=(best['bfirst'],best['bsecond']),
                     best_damage=[(z['source'],z['target'],z['rank']) for z in best['damage_slots']],CPU_seconds=x['CPU_seconds'])))
