"""One prescribed edge, all 15 branch directions, route-linear predictions only."""
import json,resource,sys,time
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(1,1))
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
sys.path.insert(0,str(ROOT/'aris_repo/tools'))
from capture_filter import screen
start=time.process_time()
source=ROOT/'research/ddp/breadth_20261027_wave11/binary72_tight_words/best_parameters.json'
tight_source=ROOT/'research/ddp/breadth_20261027_wave10/binary1152_edge_local/unique4_controller_slots.json'
d=json.loads(source.read_text());gp=d['global_label_parameters'];assert gp['passer_id']==68
assert gp['offsets']==[0,0,0,0]
adj=d['controller_out'];mats=gp['matrix_columns'];bs=gp['b_codes'];inverse=d['inverse_labels']
assert mats[0]==[2,4,8,1] and bs[0]==1 and adj[0][0]==18 and adj[18][3]==0

def action(cols,x):
    z=0
    for j in range(4):
        if x&(1<<j):z^=cols[j]
    return z
maps=[[action(c,x) for x in range(16)] for c in mats]
assert all(maps[inverse[t]][maps[t][x]]==x for t in range(4) for x in range(16))

def rank(cols):
    piv=[0]*4
    for x in cols:
        for j in range(3,-1,-1):
            if x&(1<<j):
                if piv[j]:x^=piv[j]
                else:piv[j]=x;break
    return sum(bool(x) for x in piv)

def route(src,word,b):
    u=src;cols=[];path=[u]
    for t in word:
        v=adj[u][t]
        branch=b if (u,v)==(0,18) else maps[3][b] if (u,v)==(18,0) else bs[t]
        cols=[maps[t][x] for x in cols]+[branch]
        u=v;path.append(u)
    return dict(source=src,target=u,word=word,path=path,columns=cols,rank=rank(cols))

target_word=[0,0,2,0];other_word=[3,2,2]
original_target=route(0,target_word,1);other=route(0,other_word,1)
assert original_target['path']==[0,18,37,64,10] and other['path']==[0,54,29,10]
assert original_target['rank']==other['rank']==3
slots=json.loads(tight_source.read_text())['slots'];assert len(slots)==468
baseline=[]
for slot in slots:
    r=route(slot['source'],slot['word'],1)
    assert r['target']==slot['target'] and r['rank']==4
    baseline.append(r)
diags=[]
for b in range(1,16):
    target=route(0,target_word,b);damage=[];ranks=[]
    for i,slot in enumerate(slots):
        r=route(slot['source'],slot['word'],b)
        assert r['target']==slot['target']
        ranks.append(r['rank'])
        if r['rank']<4:
            damage.append(dict(slot_index=i,source=r['source'],target=r['target'],word=r['word'],path=r['path'],
                               before_columns=baseline[i]['columns'],after_columns=r['columns'],before_rank=4,rank=r['rank'],
                               missing_per_source_fiber_root=16-(1<<r['rank']),
                               missing_ordered_fiber_pairs=16*(16-(1<<r['rank']))))
    diags.append(dict(b=b,reverse_b=maps[3][b],target_rank=target['rank'],target_columns=target['columns'],
                      damage_count=len(damage),damage_slots=damage,tight_slot_ranks=ranks))
fixers=[r for r in diags if r['target_rank']==4]
assert fixers
selected=min(fixers,key=lambda r:(r['damage_count'],r['b']))
assert route(0,other_word,selected['b'])==other
r=dict(status='FROZEN_ROUTE_LINEAR_PREDICTION_NO_GRAPH',prediction_id='P2_ONE_EDGE_DIRECTION_REPAIRS_0_TO_10_BUT_MAY_DAMAGE_TIGHT_ROUTES',
       source=str(source.relative_to(ROOT)),tight_slots_source=str(tight_source.relative_to(ROOT)),passer_id=68,
       selection_rule='target AACA rank4; then minimum damaged unique4 slots; then smallest integer b',
       changed_edge=[0,18],forward_T_columns=mats[0],reverse_T_columns=mats[3],old_b=1,new_b=selected['b'],
       selected_b=selected['b'],selected_reverse_b=selected['reverse_b'],selected_damage_count=selected['damage_count'],
       changed_parameter_scope='Only b on edge0->18 and inverse-consistent reverse_b; all T, all offsets0, and every other control edge relation unchanged',
       original_target=original_target,other_target_route_unchanged=other,
       selected_target_after=route(0,target_word,selected['b']),
       target_prediction=dict(source=0,target=10,all_256_ordered_fiber_pairs_distance_at_most4=True,
                              missing_ordered_fiber_pairs=0,reason='AACA alone has four independent branch columns and covers all16 output coordinates from each fixed input'),
       selected_damage_slots=selected['damage_slots'],
       tight_slots_before_all_rank4=True,tight_ordered_controller_slots=468,
       selected_predicted_missing_ordered_tight_fiber_pairs=sum(v['missing_ordered_fiber_pairs'] for v in selected['damage_slots']),
       directions_examined=15,target_fix_direction_count=len(fixers),all_target_fixes_damage_tight_slots=all(r['damage_count']>0 for r in fixers),
       diagnostics=diags,graph_generated=False,BFS_count=0,full_graph_score_computed=False,solver_calls=0,
       scope='Only this cachedbest68 single prescribed edge b-only repair; not an exclusion of other edges, coupled changes, or the edge-local family',
       root_next_action='Generate and independently check exactly the one selected graph against the frozen target and damage predictions',
       CPU_seconds=time.process_time()-start)
# Numeric route data are not operational prose; screen only the narrative strings.
def strings(x):
    if isinstance(x,str):return [x]
    if isinstance(x,dict):return [s for y in x.values() for s in strings(y)]
    if isinstance(x,list):return [s for y in x for s in strings(y)]
    return []
assert not screen('\n'.join(strings(r)))
(HERE/'analysis.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(dict(selected_b=r['selected_b'],reverse_b=r['selected_reverse_b'],damage=r['selected_damage_count'],
                     target_before=original_target['columns'],target_after=r['selected_target_after']['columns'],
                     target_fix_directions=[(z['b'],z['damage_count']) for z in fixers],
                     predicted_missing_tight=r['selected_predicted_missing_ordered_tight_fiber_pairs'],CPU_seconds=r['CPU_seconds'])))
