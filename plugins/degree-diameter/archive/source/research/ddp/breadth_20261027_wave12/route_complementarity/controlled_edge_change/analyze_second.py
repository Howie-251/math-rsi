"""Second prescribed coordinated direction diagnostic; no graph or BFS."""
import json,resource,sys,time
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(1,1))
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[4]
sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen
started=time.process_time()
source=ROOT/'research/ddp/breadth_20261027_wave11/binary72_tight_words/best_parameters.json'
tight_source=ROOT/'research/ddp/breadth_20261027_wave10/binary1152_edge_local/unique4_controller_slots.json'
d=json.loads(source.read_text());gp=d['global_label_parameters'];assert gp['passer_id']==68
adj=d['controller_out'];mats=gp['matrix_columns'];bs=gp['b_codes'];inv=d['inverse_labels']
assert adj[36][1]==0 and adj[0][2]==36 and gp['offsets']==[0,0,0,0]
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
def route(src,word,second_b):
    u=src;columns=[];path=[src]
    for t in word:
        v=adj[u][t]
        if (u,v)==(0,18):b=3
        elif (u,v)==(18,0):b=maps[3][3]
        elif (u,v)==(36,0):b=second_b
        elif (u,v)==(0,36):b=maps[2][second_b]
        else:b=bs[t]
        columns=[maps[t][x] for x in columns]+[b]
        u=v;path.append(u)
    return dict(source=src,target=u,word=word,path=path,columns=columns,rank=rank(columns))
slots=json.loads(tight_source.read_text())['slots'];assert len(slots)==468
base=[route(s['source'],s['word'],3) for s in slots]
first=json.loads((HERE/'analysis.json').read_text());assert first['selected_b']==3
assert [(r['source'],r['target']) for r in base if r['rank']<4]==[(37,63),(63,37)]
diags=[]
for b in range(1,16):
    target=route(0,[0,0,2,0],b);assert target['rank']==4 and target['path']==[0,18,37,64,10]
    damaged=[];ranks=[];repair=[]
    for i,s in enumerate(slots):
        r=route(s['source'],s['word'],b);assert r['target']==s['target'];ranks.append(r['rank'])
        if (r['source'],r['target']) in ((37,63),(63,37)):repair.append(r)
        if r['rank']<4:
            damaged.append(dict(slot_index=i,source=r['source'],target=r['target'],word=r['word'],path=r['path'],
                                first_change_columns=base[i]['columns'],after_columns=r['columns'],
                                first_change_rank=base[i]['rank'],rank=r['rank'],
                                missing_per_source_fiber_root=16-(1<<r['rank']),
                                missing_ordered_fiber_pairs=16*(16-(1<<r['rank']))))
    assert len(repair)==2
    diags.append(dict(second_b=b,second_reverse_b=maps[2][b],repairs_37_to_63_and_reverse=all(r['rank']==4 for r in repair),
                      repair_routes=repair,critical_0_to_10_AACA=target,damage_count=len(damaged),damage_slots=damaged,
                      tight_slot_ranks=ranks))
fixers=[x for x in diags if x['repairs_37_to_63_and_reverse']]
assert fixers
best=min(fixers,key=lambda x:(x['damage_count'],x['second_b']))
x=dict(status='FROZEN_SECOND_EDGE_ROUTE_LINEAR_DIAGNOSTIC_NO_GRAPH',prediction_id='P3_COORDINATED_SECOND_BRANCH_DIRECTION',
       source=str(source.relative_to(ROOT)),tight_slots_source=str(tight_source.relative_to(ROOT)),passer_id=68,
       fixed_first_edge=dict(forward=[0,18],b=3,reverse_b=maps[3][3]),
       prescribed_second_edge=dict(undirected=[0,36],forward=[36,0],label=1,T_columns=mats[1],Tinv_columns=mats[2],old_b=bs[1]),
       selection_rule='repair37->63 and63->37 to rank4; minimum total damaged468 slots; then smallest integer b',
       selected_second_b=best['second_b'],selected_second_reverse_b=best['second_reverse_b'],selected_damage_count=best['damage_count'],
       selected_repair_routes=best['repair_routes'],selected_damage_slots=best['damage_slots'],
       first_change_target0_to_10_rank4_preserved_for_all15=True,
       selected_predicted_missing_ordered_tight_fiber_pairs=sum(v['missing_ordered_fiber_pairs'] for v in best['damage_slots']),
       directions_examined=15,repair_direction_count=len(fixers),all_repairs_still_damage_tight_slots=all(z['damage_count']>0 for z in fixers),
       diagnostics=diags,graph_generated=False,full_graph_score_computed=False,BFS_count=0,solver_calls=0,
       scope='Only fixed firstedge b3 plus this prescribed secondedge direction with all T and offsets0 fixed; no thirdedge, otheredge, coupledmatrix, or whole edge-local family exclusion',
       root_next_action='If selected_damage_count0, root may generate one frozen twoedge candidate; otherwise close this twoedge diagnostic without thirdedge expansion',
       CPU_seconds=time.process_time()-started)
def strings(x):
    if isinstance(x,str):return [x]
    if isinstance(x,dict):return [s for y in x.values() for s in strings(y)]
    if isinstance(x,list):return [s for y in x for s in strings(y)]
    return []
assert not screen('\n'.join(strings(x)))
(HERE/'second_edge_analysis.json').write_text(json.dumps(x,indent=2)+'\n')
print(json.dumps(dict(selected_second_b=x['selected_second_b'],reverse_b=x['selected_second_reverse_b'],damage=x['selected_damage_count'],
                     fixers=[(z['second_b'],z['damage_count']) for z in fixers],
                     selected_damage=[(z['source'],z['target'],z['rank']) for z in best['damage_slots']],CPU_seconds=x['CPU_seconds'])))
