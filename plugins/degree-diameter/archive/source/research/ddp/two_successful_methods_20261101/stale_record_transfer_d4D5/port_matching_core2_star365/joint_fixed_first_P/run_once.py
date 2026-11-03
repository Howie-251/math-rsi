"""Exact fixed-P newroot coverage via allowed port matching."""
import time
START=time.process_time()
from pathlib import Path
from collections import deque
import json
import resource
resource.setrlimit(resource.RLIMIT_CPU,(16,16))
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[5]
SOURCE=ROOT/'research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/source_and_single'
P=[43,58,151,314]
CUTS=[(43,58),(151,314)]
PRIOR=1.537876879+.3+.3

def save(name,obj):
    (HERE/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

if (HERE/'ATTEMPT.json').exists(): raise RuntimeError('one-shot fixedP already attempted')
save('ATTEMPT.json',{'status':'STARTED','old_read_prep_CPU':PRIOR,'case_cap':20})
lines=(SOURCE/'source364.edges').read_text().splitlines()
assert list(map(int,lines[0].split()))==[364,714]
es=[tuple(map(int,x.split())) for x in lines[1:] if x.strip()]
adj=[[] for _ in range(364)]
for u,v in es:adj[u].append(v);adj[v].append(u)
ports=json.loads((SOURCE/'PORT_BINDING.json').read_text())['eligible_ports']
classes=json.loads((SOURCE/'PORT_CLASSES.json').read_text())['R2_class_members']
# Four new support queries, not full sourceD5 or renewed28port balls.
rows=[]
for root in P:
    dist=[-1]*364;dist[root]=0;q=deque([root])
    while q:
        u=q.popleft()
        if dist[u]==4:continue
        for v in adj[u]:
            if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
    rows.append(dist)
dP=[min([row[t] for row in rows if row[t]>=0],default=5) for t in range(364)]
holes=[t for t in range(364) if dP[t]>4]
threshold=[];holeclasses=[]
for b,members in zip(ports,classes):
    hs=[t for t in members if dP[t]>4]
    beta=[0 if t==b else (1 if t in adj[b] else 2) for t in hs]
    threshold.append(3-max(beta) if beta else 99)
    holeclasses.append({'port':b,'holes':hs,'beta':beta,'required_max_dP_mate':threshold[-1]})
allowed={b:[] for b in ports}
for i,a in enumerate(ports):
    for j,b in enumerate(ports):
        if i!=j and dP[a]<=threshold[j] and dP[b]<=threshold[i]:allowed[a].append(b)
hard=[b for b,th in zip(ports,threshold) if th==1]
near=[a for a in ports if dP[a]<=1]
hard_neighbors=sorted({a for b in hard for a in allowed[b]})
hall_fail=len(hard_neighbors)<len(hard)
save('FOUR_CORE_R4_SUPPORTS.json',{'P':P,'source_partial_BFS_depth':4,'queries':4,'rows_distances0_to4_else_minus1':rows,'dP_cap5':dP,'holes':holes,'source_D5_revalidation':0,'old28portballs_rerun':0})
save('ALLOWED_MATCHING_MODEL.json',{'P':P,'cuts':CUTS,'ports':ports,'dP_ports':{a:dP[a] for a in ports},'hole_classes':holeclasses,'allowed_neighbors':allowed,'hard_beta2_owner_ports':hard,'near_ports_dP_atmost1':near,'hard_owner_allowed_neighbors_union':hard_neighbors,'Hall_cardinality_failure':hall_fail})
matching=None
if hall_fail:
    status='COMPLETE_NO_FIXED_P_ALL_MATCHINGS_BY_HALL'
else:
    import networkx as nx
    graph=nx.Graph();graph.add_nodes_from(ports)
    graph.add_edges_from((a,b) for a in ports for b in allowed[a] if a<b)
    mat=nx.max_weight_matching(graph,maxcardinality=True)
    save('MAXIMUM_MATCHING.json',{'size':len(mat),'edges':[sorted(x) for x in mat],'portcount':28,'perfect':len(mat)==14})
    if len(mat)==14:
        matching=[tuple(sorted(x)) for x in mat]
        status='NEWROOT_COVER_MATCHING_FOUND_PENDING_FINAL_GRAPH'
    else:
        status='COMPLETE_NO_FIXED_P_ALL_MATCHINGS_MAXIMUM_MATCHING'
producer_roots=0;valid=False
if matching is not None:
    final=[(u,v) for u,v in es if tuple(sorted((u,v))) not in CUTS]+matching+[(364,p) for p in P]
    assert len(final)==len(set(tuple(sorted(x)) for x in final))==730
    with (HERE/'candidate_d4_D5_n365.edges').open('w')as f:
        f.write('365 730\n')
        for u,v in sorted(tuple(sorted(x))for x in final):f.write(f'{u} {v}\n')
    jadj=[[]for _ in range(365)]
    for u,v in final:jadj[u].append(v);jadj[v].append(u)
    assert all(len(z)==len(set(z))==4 for z in jadj)
    valid=True
    with (HERE/'FINAL_ROOT_STATS.tsv').open('w')as f:
        for root in [364]+list(range(364)):
            if time.process_time()-START>15:valid=False;status='UNKNOWN_PRODUCER_CPU_LIMIT';break
            d=[-1]*365;d[root]=0;q=deque([root])
            while q:
                u=q.popleft()
                for v in jadj[u]:
                    if d[v]<0:d[v]=d[u]+1;q.append(v)
            ecc=max(d)if -1 not in d else 365
            producer_roots+=1;f.write(f'{root}\t{ecc}\n')
            if ecc>5:
                valid=False
                save('FINAL_GRAPH_FIRST_BAD.json',{'root':root,'firstbad':next(i for i,x in enumerate(d)if x>5 or x<0),'ecc':ecc})
                status='NEWROOT_MATCHING_PASS_FINAL_GRAPH_FAIL';break
    if valid:status='CANDIDATE_D4_D5_N365_PRODUCER_PASS_PENDING_FRESH'
    save('PARAMETERS.json',{'n':365,'m':730,'degree':4,'cuts':CUTS,'P':P,'portmatching':matching,'newroot_exactcover':True,'producer_fullpass':valid,'producer_roots':producer_roots,'fresh_Lean_ARIS':'PENDING' if valid else 'NOT_TRIGGERED'})
result={'status':status,'P':P,'holes_count':len(holes),'hard_owner_count':len(hard),'near_port_count':len(near),'hard_neighbor_union_count':len(hard_neighbors),'Hall_fail':hall_fail,'matching_found':matching is not None,'producer_fullpass':valid,'producer_roots':producer_roots,'new_source_support_queries':4,'support_radius':4,'source_D5_BFS_or_old28balls_rerun':0,'graph_generated':matching is not None,'actual_process_CPU':time.process_time()-START,'prior_sample_read_prep_CPU':PRIOR,'case_CPU':PRIOR+time.process_time()-START,'case_cap':20,'scope':'fixed two originalcuts and fourP; arbitraryperfectmatching of28ports; no otheredits','new_accepted_graph_parameter_Lean':[0,0,0],'terminal':True,'next':'STOP_FIXED_P_NO_ALLCUTPAIR_OR_SEED_AUTOMATIC'}
save('RESULT.json',result);save('TERMINAL.json',result)
print(json.dumps(result,ensure_ascii=False),flush=True)
