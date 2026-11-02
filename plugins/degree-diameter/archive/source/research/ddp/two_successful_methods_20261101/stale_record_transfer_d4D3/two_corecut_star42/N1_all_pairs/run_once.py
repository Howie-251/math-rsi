#!/usr/bin/env python3
from pathlib import Path
from collections import Counter,deque
import csv,json,math,os,resource,time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[5]
SOURCE=ROOT/'research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate/source_N1.NORMALIZED_ADJ.json'
PRIOR=json.loads((HERE.parent/'source_interface/RESULT.json').read_text())['total_charged_CPU_seconds']
PREP=0.1
BUDGET=20.0
resource.setrlimit(resource.RLIMIT_CPU,(math.floor(BUDGET-PRIOR-PREP),math.floor(BUDGET-PRIOR-PREP)))
def save(name,data):(HERE/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def charged():return PRIOR+PREP+time.process_time()
def bfs(adj,root,stop_target=None):
    dist=[-1]*len(adj);parent=[-1]*len(adj);dist[root]=0;q=deque([root])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if dist[v]>=0:continue
            dist[v]=dist[u]+1;parent[v]=u;q.append(v)
        if stop_target is not None and dist[stop_target]>=0:break
    if stop_target is not None:target=stop_target
    else:target=next((v for v,d in enumerate(dist)if d<0 or d>3),max(range(len(adj)),key=lambda v:dist[v]))
    path=[]
    if dist[target]>=0:
        v=target
        while v>=0:path.append(v);v=parent[v]
        path.reverse()
    return {'root':root,'target':target,'distance':dist[target],
            'reached':sum(d>=0 for d in dist),'eccentricity':max(dist),
            'actual_path':path,'distance_histogram':dict(sorted(Counter(dist).items()))}
def passes(r):return r['reached']==42 and r['eccentricity']<=3

save('HANDLE.json',{'pid':os.getpid(),'phase':'one_cached_N1_JSON_input_parse','running':True,'worker_count':1,
                     'prior_case_CPU_seconds':PRIOR,'cumulative_CPU_budget_seconds':BUDGET})
data=json.loads(SOURCE.read_text())
assert data['original_labels']==list(range(41))
source=[set(row)for row in data['adjacency']]
assert len(source)==41
edges=sorted((u,v)for u,row in enumerate(source)for v in row if u<v)
assert len(edges)==82
configs=[]
for i,e in enumerate(edges):
    for j in range(i+1,len(edges)):
        f=edges[j]
        if len(set(e+f))==4:
            configs.append({'index':len(configs),'old_edge_indices':[i,j],
                            'old_cut_edges':[list(e),list(f)],'new_label':41,'four_pins':sorted(e+f)})
assert len(configs)==3075
with (HERE/'ALL3075_PAIR_PARAMETERS.tsv').open('w',newline='')as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['config','edge_i','edge_j','e0','e1','f0','f1','pin0','pin1','pin2','pin3'])
    for c in configs:w.writerow([c['index'],*c['old_edge_indices'],*c['old_cut_edges'][0],*c['old_cut_edges'][1],*c['four_pins']])
save('INPUT_BINDING.json',{'source':str(SOURCE.relative_to(ROOT)),'cached_JSON_parse_count':1,
                           'original_labels':'0..40','n41_m82_degree4_metadata_inherited':True,
                           'source_D3_or_allroot_revalidation':False,'eligible_edge_pair_count':3075,
                           'new_graph_candidate_count_before_evaluation':0})
save('HANDLE.json',{'pid':os.getpid(),'phase':'finite3075_finalcandidate_batch','running':True,'worker_count':1,
                     'cumulative_CPU_budget_seconds':BUDGET,'actual_eligible_pairs':len(configs)})
rows=[{'configuration':c['index'],'stage':'NOT_VISITED','failed_root':None,'failed_target':None,'distance':None}for c in configs]
first_new=None;first_old=None;diagnostic=None;diagnostic_count=0
newroot_checks=0;newroot_pass=0;oldroot_checks=0;oldold_fail=0;hit=None;completed=0;timed=False
for c in configs:
    if charged()>=BUDGET-0.5:timed=True;break
    adj=[set(row)for row in source]+[set(c['four_pins'])]
    for u,v in c['old_cut_edges']:adj[u].remove(v);adj[v].remove(u)
    for v in c['four_pins']:adj[v].add(41)
    r=bfs(adj,41);newroot_checks+=1;allroots=[r]
    failed=None;stage='NEWROOT_R3_FAIL'
    if not passes(r):
        failed=r
        if first_new is None:first_new={'configuration':c,'BFS':r}
    else:
        newroot_pass+=1;stage='OLDOLD_R3_FAIL'
        for root in range(41):
            if charged()>=BUDGET-0.5:timed=True;stage='CPU_CAP_DURING_OLDROOTS';break
            r=bfs(adj,root);oldroot_checks+=1;allroots.append(r)
            if passes(r):continue
            failed=r;oldold_fail+=1
            if first_old is None:
                both_nonpin=r['root']not in c['four_pins']and r['target']not in c['four_pins']
                first_old={'configuration':c,'BFS':r,'both_endpoints_nonpin':both_nonpin}
                if both_nonpin:
                    original=bfs(source,r['root'],r['target']);diagnostic_count=1
                    original['visited_when_target_first_found']=original.pop('reached')
                    original['partial_discovered_max_distance']=original.pop('eccentricity')
                    original['partial_discovery_histogram']=original.pop('distance_histogram')
                    original['traversal_stopped_after_target_discovery']=True
                    original['minus1_is_unvisited_not_unreachable']=True
                    original['global_source_eccentricity_or_D3_verified']=False
                    path_edges={tuple(sorted((a,b)))for a,b in zip(original['actual_path'],original['actual_path'][1:])}
                    diagnostic={'original_source_pair':original,'new_candidate_distance':r['distance'],
                                'cut_edges_on_this_one_original_route':[e for e in c['old_cut_edges']if tuple(e)in path_edges],
                                'all_original_geodesics_enumerated':False,'uniqueness_claimed':False,
                                'single_pair_only':True}
                    save('ONE_OLDPAIR_ROUTE_DIAGNOSTIC.json',diagnostic)
            break
        if failed is None and not timed:
            assert len(allroots)==42 and all(len(row)==4 for row in adj)
            output_edges=sorted((u,v)for u,row in enumerate(adj)for v in row if u<v)
            assert len(output_edges)==84
            with (HERE/'graph_d4_D3_n42.edges').open('w')as f:
                f.write('42 84\n')
                for u,v in output_edges:f.write(f'{u} {v}\n')
            actualD=max(r['eccentricity']for r in allroots)
            witness=next(r for r in allroots if r['eccentricity']==actualD)
            hit={'n':42,'m':84,'degree':4,'actual_diameter':actualD,'configuration':c,
                 'actual_distance_witness':witness,'ordinary_final_BFS_roots':42,
                 'original_source':str(SOURCE.relative_to(ROOT)),'source_D3_repeated':False,
                 'root_acceptance':'PENDING','latest_public_gate':'PENDING'}
            save('PARAMETERS.json',hit)
            with (HERE/'ALL42_FINAL_ROOT_HISTOGRAMS.csv').open('w',newline='')as f:
                w=csv.writer(f);w.writerow(['root','N0','N1','N2','N3','eccentricity'])
                for r in allroots:w.writerow([r['root'],*[r['distance_histogram'].get(k,0)for k in range(4)],r['eccentricity']])
            stage='COMPLETE_HIT_PENDING_ROOT'
    rows[c['index']].update(stage=stage,failed_root=failed['root']if failed else None,
                           failed_target=failed['target']if failed else None,distance=failed['distance']if failed else None)
    if not timed:completed+=1
    if hit or timed:break
with (HERE/'ALL3075_PAIR_STAGES.tsv').open('w',newline='')as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
counts=dict(Counter(r['stage']for r in rows))
status='FOUND42_COMPLETE_FINAL_GRAPH_PENDING_ROOT_ACCEPTANCE'if hit else 'UNKNOWN_FINITE_BATCH_CPU_CAP'if timed else 'COMPLETE_NO_N1_TWO_DISJOINT_EDGECUT_ONE4STAR_D3'
result={'status':status,'prediction':'AtleastoneconfigurationpassesnewrootR3;fullgraphnotpredicted.',
        'prediction_newroot_supported':newroot_pass>0,'source_id':'MessieresN1','source_n':41,'source_m':82,
        'target_n':42,'target_m':84,'target_degree':4,'target_D':3,'exact_domain':3075,
        'cached_source_JSON_parse_count':1,'finite_pair_parameters_listed':len(configs),'configurations_finished':completed,
        'pair_stage_counts':counts,'newroot_ordinary_BFS_checks':newroot_checks,'newroot_R3_passed':newroot_pass,
        'final_candidate_old_label_BFS_checks':oldroot_checks,'oldold_failures_after_newroot_pass':oldold_fail,
        'first_newroot_failure':first_new,'first_oldold_failure':first_old,
        'original_source_single_pair_diagnostic_checks':diagnostic_count,'one_oldpair_diagnostic':diagnostic,
        'hit':hit,'remaining_unvisited_pairs':sum(r['stage']=='NOT_VISITED'for r in rows),
        'exact_NO_scope':'OnlytheliteralMessieresN1,all3075unordereddisjointoldedgepairs,delete2edges/addone4star;notN2/N3orgeneral(4,3).',
        'source_D3_allroot_BFS_or_geodesic_enumeration':0,'solver_field_Lean_ARIS_network_hash':0,
        'root_Wiki_modified':False,'new_graph_parameter_Lean_increment_before_root_acceptance':[0,0,0],
        'prior_case_CPU_seconds':PRIOR,'new_preparation_charge_seconds':PREP,'actual_process_CPU_seconds':time.process_time(),
        'cumulative_charged_CPU_seconds':charged(),'CPU_budget_seconds':BUDGET,'worker_count':1,
        'next':'STOP_REPORT_NO_SOURCE_CUT_SEED_MODEL_OR_TIMER_EXTENSION'}
save('RESULT.json',result)
(HERE/'NOTE.md').write_text(f'''# N1 complete two-cut4star42 batch

Actualstatus:{status}. All3075matchingedgepairparametersarelisted;finished{completed};stagecounts{counts}. NewrootR3passes:{newroot_pass};subsequentold-oldfailures:{oldold_fail}. Firstactualnewrootandoldpairdistances/pathsandcompleteeditsareinRESULT. Thepredictionofnewrootcoveragewas{'supported'if newroot_pass else 'refutedforthecompleteN1domain'};thisdoesnotmeanfullgraphsuccess.

Eachcandidateis42/84all4regularbydegreereplacement;theoldsourceisparsedoncefromitscachednormalizedJSON,withD3inherited. OrdinaryBFSisrunonlyonfinal42candidates,startingnewroot41. NooldsourceallrootD3verificationorfieldworkisrepeated. Theoneconditionaloriginaloldpairdiagnosticcountis{diagnostic_count};itneverenumeratesalloldgeodesicsorclaimsuniqueness.

ForH=G−2cutsandfourpinsP,newrootcoverageisR2_H(P)=all41. Twononpinoldendpointsneedatleast4stepsthroughthenewstar;theirD3failurecannotberepairedbythatstar. ThisexplainsspecificdamagerouteclasseswithoutoverridingactualfinalgraphBFS. Old-oldcoverageisnotinferredfromnewrootcoverage.

Ifall3075finishandnonehit,thenonlythisN1/two-disjoint-oldedge/one4stararchitectureisclosed. N2/N3,othermodificationsandgeneral(4,3)graphsremainoutside. Afirsthitstopsandawaitsrootfreshacceptance/currentbaseline;untestedpairsarenotnegative. Noextrasource,timer,seed,cuts,MIPorLeanstarts.

Budgetinherits{PRIOR:.9f},addsconservativeprep{PREP}andthissingleprocess,withoutcompilationorinstallation. Cumulative{charged():.9f}/20CPU. No root/Wiki/HTML oroldartifactsmodified.
''')
terminal={'status':status,'running':False,'all_processes_terminal':True,'worker_count':1,
          'prior_case_CPU_seconds':PRIOR,'new_preparation_charge_seconds':PREP,
          'actual_process_CPU_seconds':time.process_time(),'cumulative_charged_CPU_seconds':charged(),
          'CPU_budget_seconds':BUDGET,'configurations_finished':completed,'no_timer_reset':True,'no_automatic_continuation':True}
save('TERMINAL.json',terminal);save('HANDLE.json',{'pid':os.getpid(),'phase':'terminal',**terminal})
print(json.dumps({'result':result,'terminal':terminal},ensure_ascii=False,indent=2))
