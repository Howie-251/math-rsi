#!/usr/bin/env python3
import time
START=time.process_time()
from pathlib import Path
from collections import Counter,deque
import csv,json,math,os,resource

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[5]
SOURCE_DIR=ROOT/'research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate'
PRIOR=1.125664745
PREP=.1
BUDGET=5.
assert not(HERE/'TERMINAL.json').exists(),'One case,one batch,no restart.'
HARD=math.floor(BUDGET-PRIOR-PREP)
resource.setrlimit(resource.RLIMIT_CPU,(HARD,HARD))
def charged():return PRIOR+PREP+time.process_time()
def cap():return charged()>=min(BUDGET-.15,PRIOR+PREP+HARD-.15)
def save(name,obj):(HERE/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def bfs(adj,root,only=None):
    d=[-1]*len(adj);p=[-1]*len(adj);d[root]=0;q=deque([root])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if d[v]>=0:continue
            d[v]=d[u]+1;p[v]=u;q.append(v)
        if only is not None and d[only]>=0:break
    target=only if only is not None else next((v for v,x in enumerate(d)if x<0 or x>3),max(range(len(d)),key=lambda v:d[v]))
    route=[]
    if d[target]>=0:
        v=target
        while v>=0:route.append(v);v=p[v]
        route.reverse()
    return dict(root=root,target=target,distance=d[target],reached=sum(x>=0 for x in d),
        eccentricity=max(d),actual_path=route,distance_histogram=dict(sorted(Counter(d).items())))
def pass3(x):return x['reached']==42 and x['eccentricity']<=3
def pinrelation(x,pins):
    a=x['root']in pins;b=x['target']in pins
    return 'BOTH_NONPIN'if not a and not b else 'BOTH_PIN'if a and b else 'ONE_PIN'

save('HANDLE.json',dict(status='RUNNING',running=True,pid=os.getpid(),worker_count=1,
    phase='N2_N3_one_case',prior_readgate_CPU_seconds=PRIOR,CPU_budget_seconds=BUDGET))
results=[];diagnostic=None;hit=None;timed=False;started=0;finished=0;parses=0
for tag in ['N2','N3']:
    if hit or timed:break
    if cap():timed=True;break
    sourcepath=SOURCE_DIR/f'source_{tag}.NORMALIZED_ADJ.json'
    data=json.loads(sourcepath.read_text());parses+=1
    assert data['original_labels']==list(range(41)) and len(data['adjacency'])==41
    source=tuple(tuple(sorted(row))for row in data['adjacency'])
    edges=sorted((u,v)for u,row in enumerate(source)for v in row if u<v)
    assert len(edges)==82
    configs=[]
    for i,e in enumerate(edges):
        for j in range(i+1,len(edges)):
            f=edges[j]
            if len(set(e+f))==4:
                configs.append(dict(index=len(configs),old_edge_indices=[i,j],old_cut_edges=[list(e),list(f)],
                    new_label=41,four_pins=sorted(e+f)))
    with(HERE/f'{tag}_ALL_PAIR_PARAMETERS.tsv').open('w',newline='')as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['configuration','edge_i','edge_j','e0','e1','f0','f1','pin0','pin1','pin2','pin3'])
        for c in configs:w.writerow([c['index'],*c['old_edge_indices'],*c['old_cut_edges'][0],*c['old_cut_edges'][1],*c['four_pins']])
    stats=dict(source_id=tag,source=str(sourcepath.relative_to(ROOT)),cached_source_JSON_parse_count=1,
        source_n=41,source_m=82,source_degree_D3_nonisomorphism='INHERITED_NOT_REVALIDATED',
        actual_disjoint_edgepair_domain=len(configs),configurations_started=0,configurations_finished=0,
        newroot_BFS=0,newroot_R3_passed=0,final_oldlabel_BFS=0,oldold_failed_after_newrootpass=0,
        first_newroot_failure=None,first_oldold_failure=None,original_source_single_pair_diagnostic_checks=0)
    rows=[dict(configuration=c['index'],stage='NOT_VISITED',failed_root=None,failed_target=None,distance=None,pin_relation=None)for c in configs]
    save('HANDLE.json',dict(status='RUNNING',running=True,pid=os.getpid(),worker_count=1,phase=tag+'_all_disjointpairs',
        actual_source_domain=len(configs),charged_CPU_seconds=charged(),CPU_budget_seconds=BUDGET))
    for c in configs:
        if cap()or started>=6150:timed=True;break
        stats['configurations_started']+=1;started+=1
        adj=[set(row)for row in source]+[set(c['four_pins'])]
        for u,v in c['old_cut_edges']:adj[u].remove(v);adj[v].remove(u)
        for v in c['four_pins']:adj[v].add(41)
        adj=[tuple(sorted(row))for row in adj]
        current=bfs(adj,41);stats['newroot_BFS']+=1;measurements=[current]
        failed=None;stage='NEWROOT_R3_FAIL'
        if not pass3(current):
            failed=current
            if stats['first_newroot_failure']is None:stats['first_newroot_failure']=dict(configuration=c,BFS=current)
        else:
            stats['newroot_R3_passed']+=1;stage='OLDOLD_R3_FAIL'
            for oldroot in range(41):
                if cap():timed=True;stage='CPU_CAP_DURING_OLDROOTS';break
                current=bfs(adj,oldroot);stats['final_oldlabel_BFS']+=1;measurements.append(current)
                if pass3(current):continue
                failed=current;stats['oldold_failed_after_newrootpass']+=1
                relation=pinrelation(current,c['four_pins'])
                if stats['first_oldold_failure']is None:
                    stats['first_oldold_failure']=dict(configuration=c,BFS=current,pin_relation=relation,
                        old_original_route='NOT_MEASURED_UNLESS_THIS_IS_THE_ONE_GLOBAL_DIAGNOSTIC')
                if diagnostic is None:
                    old=bfs(source,current['root'],current['target']);stats['original_source_single_pair_diagnostic_checks']=1
                    old['visited_when_target_found']=old.pop('reached')
                    old['partial_discovery_max_distance']=old.pop('eccentricity')
                    old['partial_discovery_histogram']=old.pop('distance_histogram')
                    old.update(traversal_stopped_after_target_discovery=True,minus1_is_unvisited_not_unreachable=True,source_global_D3_verified=False)
                    oe={tuple(sorted(e))for e in zip(old['actual_path'],old['actual_path'][1:])}
                    diagnostic=dict(source_id=tag,configuration=c,pin_relation=relation,old_source_single_pair=old,
                        actual_new_shortest_path=current['actual_path'],actual_new_distance=current['distance'],
                        cuts_on_this_saved_old_route=[e for e in c['old_cut_edges']if tuple(e)in oe],
                        old_route_unique_claimed=False,all_oldgeodesics_enumerated=False,total_sourcepair_diagnostics=1)
                    stats['first_oldold_failure']['old_original_route']=old['actual_path']
                    save('ONE_OLDPAIR_ROUTE_DIAGNOSTIC.json',diagnostic)
                break
            if failed is None and not timed:
                assert len(measurements)==42 and all(len(row)==4 for row in adj)
                outedges=sorted((u,v)for u,row in enumerate(adj)for v in row if u<v)
                assert len(outedges)==84
                with(HERE/'graph_d4_D3_n42.edges').open('w')as f:
                    f.write('42 84\n')
                    for u,v in outedges:f.write(f'{u} {v}\n')
                hit=dict(source_id=tag,source=str(sourcepath.relative_to(ROOT)),n=42,m=84,max_degree=4,
                    actual_D=max(x['eccentricity']for x in measurements),configuration=c,ordinary_final_BFS_roots=42,
                    allroot_measurements=measurements,root_independent_acceptance='PENDING',latest_public_gate='PENDING')
                save('PARAMETERS.json',hit)
                with(HERE/'ALL42_FINAL_ROOT_HISTOGRAMS.csv').open('w',newline='')as f:
                    w=csv.writer(f);w.writerow(['root','R0','R1','R2','R3','eccentricity','reached'])
                    for x in measurements:w.writerow([x['root'],*[x['distance_histogram'].get(k,0)for k in range(4)],x['eccentricity'],x['reached']])
                stage='COMPLETE_HIT_PENDING_ROOT'
        rows[c['index']].update(stage=stage,failed_root=failed['root']if failed else None,
            failed_target=failed['target']if failed else None,distance=failed['distance']if failed else None,
            pin_relation=pinrelation(failed,c['four_pins'])if failed and stage=='OLDOLD_R3_FAIL'else None)
        if not timed:stats['configurations_finished']+=1;finished+=1
        if hit or timed:break
    stats['pair_stage_counts']=dict(Counter(row['stage']for row in rows))
    stats['remaining_unvisited_pairs']=sum(row['stage']=='NOT_VISITED'for row in rows)
    stats['whole_fixed_source_rule_excluded']=not hit and not timed and stats['configurations_finished']==len(configs)
    stats['status']='FOUND_COMPLETE42_PENDING_ROOT'if hit else 'UNKNOWN_INCOMPLETE_BATCH'if timed else 'COMPLETE_NO_THIS_SOURCE_TWO_CUT4STAR42'
    with(HERE/f'{tag}_ALL_PAIR_STAGES.tsv').open('w',newline='')as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
    save(tag+'_RESULT.json',stats);results.append(stats)
complete_no=not hit and not timed and len(results)==2 and all(s['whole_fixed_source_rule_excluded']for s in results)
status='FOUND_COMPLETE42_PENDING_ROOT_ACCEPTANCE'if hit else 'COMPLETE_NO_N2_AND_N3_ALL_TWO_DISJOINT_EDGECUT4STAR42'if complete_no else 'UNKNOWN_CPU_CAP_OR_INCOMPLETE_SOURCE_DOMAIN'
result=dict(status=status,prediction='AtleastoneofN2/N3hasanewrootR3pass;completegraphnotpredicted',
    prediction_newroot_supported=any(s['newroot_R3_passed']for s in results),source_results=results,
    configurations_started=started,configurations_finished=finished,source_cached_JSON_parses=parses,
    complete_fixed_N2_N3_rule_exclusion=complete_no,hit=hit,CPU_cap_reached=timed,
    one_original_source_pair_diagnostic=diagnostic,total_sourcepair_diagnostics=1 if diagnostic else 0,
    source_D3_allroot_or_nonisomorphism_or_field_validation=0,graph_scope='OnlyeachcachedMessieresN2/N3,two disjoint oldedge deletions plusone4star;notothercuts/sources/general4D3',
    prior_readgate_CPU_seconds=PRIOR,preparation_charge_seconds=PREP,actual_process_CPU_seconds=time.process_time(),
    cumulative_charged_CPU_seconds=charged(),CPU_budget_seconds=BUDGET,worker_count=1,no_timer_reset=True,
    new_graph_parameter_Lean_increment_before_root_acceptance=[0,0,0],solver_field_Lean_ARIS_network_install_hash=0,
    root_Wiki_HTML_modified=False,next='STOP_NOTIFY_ROOT_FRESH_ACCEPTANCE'if hit else 'STOP_NO_NEW_CUT_SOURCE_SEED_OR_TIMER')
save('RESULT.json',result)
summary='\n'.join(f"{s['source_id']}:domain{s['actual_disjoint_edgepair_domain']},finished{s['configurations_finished']},newrootpass{s['newroot_R3_passed']},oldoldfail{s['oldold_failed_after_newrootpass']},oldlabelBFS{s['final_oldlabel_BFS']}"for s in results)
(HERE/'NOTE.md').write_text(f'''# N2/N3 complete source comparison

Actualstatus:{status}. Prediction of at least one newrootR3 pass:
{result['prediction_newroot_supported']}. This is not a prediction or claim of
fullgraphsuccess. {summary}

SourcecachedJSONparses:{parses}. SourceD3/regularity/nonisomorphism facts are
inherited; no oldsourceallroot validation or field work. Every newroot and
old-labelled BFS here uses its actual edited42candidate. First failures and
pin relations are saved per source. There is only one original-source
singlepair diagnosis in the entire batch,notoneper source; all other oldroutes
remain unmeasured. It saves an actual shortest route,not route uniqueness.

{('Representative diagnostic:'+json.dumps(diagnostic,ensure_ascii=False))if diagnostic else 'No original-source pair diagnosis was reached.'}

All completednegative domains close only the stated source/twocut4star rule.
No N4,thirdcut,randomseed or continuation is authorized. A completehit must
receive rootfresh acceptance/public gate. The case inherits1.125664745CPU and
all preparation/failure/output costs under5CPU,oneworker,no timer reset.
No Wiki/rootHTML/state,old artifacts,solver,Lean,ARIS,install orhash touched.
''')
terminal=dict(status=status,running=False,all_processes_terminal=True,worker_count=1,
    prior_readgate_CPU_seconds=PRIOR,preparation_charge_seconds=PREP,
    actual_process_CPU_seconds=time.process_time(),cumulative_charged_CPU_seconds=charged(),
    CPU_budget_seconds=BUDGET,configurations_finished=finished,source_cached_JSON_parses=parses,
    total_sourcepair_diagnostics=1 if diagnostic else 0,no_timer_reset=True,no_automatic_continuation=True)
save('TERMINAL.json',terminal);save('HANDLE.json',dict(pid=os.getpid(),phase='terminal',**terminal))
print(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(terminal,indent=2))
