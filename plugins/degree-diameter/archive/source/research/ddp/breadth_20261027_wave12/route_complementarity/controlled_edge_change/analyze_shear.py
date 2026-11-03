"""One fixed output shear of T and b on one edge; no matrix/direction grid."""
import json,resource,sys,time
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(1,1))
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[4]
sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen
started=time.process_time()
source=ROOT/'research/ddp/breadth_20261027_wave11/binary72_tight_words/best_parameters.json'
tight_source=ROOT/'research/ddp/breadth_20261027_wave10/binary1152_edge_local/unique4_controller_slots.json'
d=json.loads(source.read_text());gp=d['global_label_parameters'];assert gp['passer_id']==68
adj=d['controller_out'];cols=gp['matrix_columns'];bs=gp['b_codes'];assert gp['offsets']==[0,0,0,0]
def action(c,x):
    y=0
    for i in range(4):
        if x&(1<<i):y^=c[i]
    return y
def shear(x):return x^((x&1)<<1)
new_T=[shear(x) for x in cols[0]]
new_Tinv=[action(cols[3],shear(1<<i)) for i in range(4)]
assert new_T==[2,4,8,3] and new_Tinv==[9,1,2,4]
assert all(action(new_Tinv,action(new_T,x))==x for x in range(16))
new_b=shear(bs[0]);new_reverse_b=action(new_Tinv,new_b)
assert new_b==3 and new_reverse_b==bs[3]==8

def rank(c):
    piv=[0]*4
    for x in c:
        for i in range(3,-1,-1):
            if x&(1<<i):
                if piv[i]:x^=piv[i]
                else:piv[i]=x;break
    return sum(bool(x) for x in piv)
def route(src,word,changed):
    u=src;c=[];path=[u]
    for t in word:
        v=adj[u][t];T,b=cols[t],bs[t]
        if changed and (u,v)==(0,18):T,b=new_T,new_b
        elif changed and (u,v)==(18,0):T,b=new_Tinv,new_reverse_b
        c=[action(T,x) for x in c]+[b];u=v;path.append(u)
    return dict(source=src,target=u,word=word,path=path,columns=c,rank=rank(c))
target_before=route(0,[0,0,2,0],False);target_after=route(0,[0,0,2,0],True)
slots=json.loads(tight_source.read_text())['slots'];assert len(slots)==468
records=[]
for i,s in enumerate(slots):
    old=route(s['source'],s['word'],False);new=route(s['source'],s['word'],True)
    assert old['target']==new['target']==s['target'] and old['rank']==4
    records.append(dict(slot_index=i,source=s['source'],target=s['target'],word=s['word'],path=old['path'],
                        original_columns=old['columns'],after_columns=new['columns'],original_rank=4,rank=new['rank'],
                        missing_per_source_fiber_root=16-(1<<new['rank']),missing_ordered_fiber_pairs=16*(16-(1<<new['rank']))))
damaged=[r for r in records if r['rank']<4]
repaired=[r for r in records if (r['source'],r['target']) in ((37,63),(63,37))]
x=dict(status='FROZEN_SINGLE_MATRIX_SHEAR_LINEAR_PREDICTION_NO_GRAPH',prediction_id='P5_COUPLED_OUTPUT_SHEAR_PRESERVES_TIGHT_RANKS',
       frozen_candidate=dict(edge=[0,18],S_columns=[3,2,4,8],S_rule='output bit1 ^= bit0',
                             original_T_columns=cols[0],original_b=bs[0],original_reverse_b=bs[3],
                             new_T_columns=new_T,new_b=new_b,new_Tinv_columns=new_Tinv,new_reverse_b=new_reverse_b,
                             all_other143_relations_original=True,all_offsets_zero=True),
       source=str(source.relative_to(ROOT)),tight_slots_source=str(tight_source.relative_to(ROOT)),
       target_before=target_before,target_after=target_after,
       target_all256_fiber_pairs_predicted_at_most4=target_after['rank']==4,
       repaired_37_63_slots=repaired,tight_slots=468,damage_count=len(damaged),damage_slots=damaged,
       all468tight_rank4=len(damaged)==0,
       P3_hypothesis_result='SUPPORTED_BY_LINEAR_CHECK' if not damaged else 'REFUTED_BY_EXPLICIT_TIGHT_SLOT',
       tight_slot_records=records,predicted_missing_ordered_tight_fiber_pairs=sum(r['missing_ordered_fiber_pairs'] for r in damaged),
       candidate_count=1,matrix_grid_assignments=0,graph_generated=False,full_graph_score_computed=False,BFS_count=0,solver_calls=0,
       gauge_scope='This changes only the edge0->18 relation. A full coordinate gauge at vertex18 would transform all four incident port relations, which are not changed here.',
       scope='Only this one coupledT/b edge shear; no other matrix, direction, edge, or affine offset varied',
       next_action='root generates exactly this one graph and independently checks frozen predictions',
       CPU_seconds=time.process_time()-started)
def strings(x):
    if isinstance(x,str):return [x]
    if isinstance(x,dict):return [s for v in x.values() for s in strings(v)]
    if isinstance(x,list):return [s for v in x for s in strings(v)]
    return []
assert not screen('\n'.join(strings(x)))
(HERE/'matrix_shear_prediction.json').write_text(json.dumps(x,indent=2)+'\n')
print(json.dumps(dict(target_before=target_before['columns'],target_after=target_after['columns'],target_rank=target_after['rank'],
                     damage_count=len(damaged),damage=[(r['source'],r['target'],r['rank']) for r in damaged],
                     repaired=[(r['source'],r['target'],r['after_columns'],r['rank']) for r in repaired],CPU_seconds=x['CPU_seconds'])))
