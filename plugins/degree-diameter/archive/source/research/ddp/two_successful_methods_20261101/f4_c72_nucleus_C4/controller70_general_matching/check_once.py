#!/usr/bin/env python3
"""Only new81boundarymatchings per deletededge;old24crossresults inherited.
15CPU hardguard,oneworker,noSAT,fibergraph,oldsourceBFS orold4320rerun.
"""
import importlib.util
import itertools
import json
import resource
import time
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
PARENT=HERE.parent
OLD=PARENT/'controller70_pair_surgery'

def save(name,data):(HERE/name).write_text(json.dumps(data,indent=2)+'\n')
def perfect_matchings(left):
    if not left:
        yield [];return
    a=left[0]
    for j in range(1,len(left)):
        b=left[j]
        for rest in perfect_matchings(left[1:j]+left[j+1:]):yield [(a,b),*rest]

def main():
    resource.setrlimit(resource.RLIMIT_CPU,(15,15));start=time.process_time()
    assert (HERE/'PRED.json').exists()
    old=json.loads((OLD/'BOUNDARY_CERTIFICATE.json').read_text());C=old['source_controller']
    assert C==json.loads((PARENT/'Exoo72/INPUT.json').read_text())['controller']
    unique=json.loads((PARENT/'Exoo72/EDGE_DOMAINS.json').read_text())
    oldresult=json.loads((OLD/'RESULT.json').read_text())
    assert oldresult['status']=='COMPLETE_SURGERY_NO_CONTROLLER_D3' and oldresult['all_boundary_survivors_processed']
    allm=list(perfect_matchings(list(range(8))));assert len(allm)==105
    new=[];typehist=Counter()
    for pairs in allm:
        aa=sum(a<4 and b<4 for a,b in pairs);bb=sum(a>=4 and b>=4 for a,b in pairs)
        assert aa==bb;typehist[aa]+=1
        if aa==0:continue
        mate=[None]*8
        for a,b in pairs:mate[a]=b;mate[b]=a
        new.append({'pairs':pairs,'mate':mate,'AA_pairs':aa,'BB_pairs':bb})
    assert dict(typehist)=={2:9,1:72,0:24} and len(new)==81
    # Cache binding: same-side R3 andcross R2 are inherited verbatim.
    # A crosspair has H<=3 unless its uniqueoldshortwordwas Ai-u-v-Bj.
    caches=[];survivors=[];attempts=[];failedpairhist=Counter()
    for ei,e in enumerate(old['per_source_edge']):
        u,v=e['deleted'];assert (unique[ei]['source'],unique[ei]['target'])==(u,v)
        A,B=e['A'],e['B'];boundary=A+B
        missing={(C[u][x['entry'][0]],C[v][x['entry'][1]]) for x in unique[ei]['unique_forbidden_entries']}
        R2=[[False]*8 for _ in range(8)];R3=[[False]*8 for _ in range(8)]
        for i in range(8):R2[i][i]=True
        for i in range(4):
            for j in range(4):
                R2[i][4+j]=R2[4+j][i]=e['D_commonneighbor_matrix'][i][j]
                R3[i][j]=e['existing_A_le3'][i][j];R3[4+i][4+j]=e['existing_B_le3'][i][j]
                R3[i][4+j]=R3[4+j][i]=(A[i],B[j]) not in missing
        assert all(not R2[i][j] or R3[i][j] for i in range(8) for j in range(8))
        caches.append({'source_edge_index':ei,'deleted':[u,v],'boundary_old_labels':boundary,'H_boundary_dist_le2':R2,'H_boundary_dist_le3':R3,'cross_R3_cache_bridge':'missingiffsaveduniqueAi-u-v-Bj,allothercrosspairsinheritalternativeH<=3'})
        for mi,m in enumerate(new):
            mate=m['mate'];fail=None
            for s in range(8):
                for t in range(s+1,8):
                    a,b,c=R3[s][t],R2[mate[s]][t],R2[s][mate[t]]
                    if not(a or b or c):
                        fail={'boundary_indices':[s,t],'old_vertex_pair':[boundary[s],boundary[t]],'existing_H_le3':a,'first_matching_then_Hle2':b,'Hle2_then_last_matching':c};break
                if fail:break
            row={'source_edge_index':ei,'new_matching_index':mi,'passes_boundary_gate':fail is None,'failure':fail}
            if fail:failedpairhist['AA' if fail['boundary_indices'][1]<4 else ('BB' if fail['boundary_indices'][0]>=4 else 'AB')]+=1
            else:survivors.append({'source_edge_index':ei,'new_matching_index':mi,'deleted':[u,v],'boundary_old_labels':boundary,**m})
            attempts.append(row)
    assert len(attempts)==14580
    save('H_BOUNDARY_CACHE.json',caches);save('BOUNDARY_ATTEMPTS.json',attempts);save('BOUNDARY_SURVIVORS.json',survivors)
    boundary_cpu=time.process_time()-start
    # Newcontrollers only, andonly when the full28pair gate passes.
    spec=importlib.util.spec_from_file_location('old_helper_readonly',OLD/'check_survivors.py')
    helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
    perms=list(itertools.permutations(range(5)))
    maps=json.loads((PARENT/'SEMILINEAR_MAPS.json').read_text());conic_index={tuple(T['conic_permutation']):i for i,T in enumerate(maps)}
    outcomes=[];D3=general=conic=0;selected=None;kind=None;complete=True
    priority={'literalD3_all_mapgates_fail':0,'general120_interface':1,'conic24_interface':2}
    for si,s in enumerate(survivors):
        if time.process_time()>14.0:
            complete=False;break
        u,v=s['deleted'];oldlabels=[x for x in range(72) if x not in (u,v)];label={x:i for i,x in enumerate(oldlabels)}
        G=[{label[y] for y in C[x] if y not in (u,v)} for x in oldlabels]
        boundary=s['boundary_old_labels']
        for a,b in s['pairs']:
            x,y=label[boundary[a]],label[boundary[b]];assert y not in G[x];G[x].add(y);G[y].add(x)
        G=[sorted(row) for row in G]
        assert all(len(row)==5 and i not in row for i,row in enumerate(G))
        assert all(i in G[j] for i,row in enumerate(G) for j in row)
        N=[sum(1<<j for j in row) for row in G];target=(1<<70)-1;bad=None;coverage=[]
        for root in range(70):
            r=helper.radius3(N,root);coverage.append(r.bit_count())
            if r!=target:
                j=next(j for j in range(70) if not(r>>j&1));bad={'root':root,'missing_target':j,'old_root':oldlabels[root],'old_missing_target':oldlabels[j],'R3_cardinality':r.bit_count()};break
        row={'boundary_survivor_index':si,**s,'literal70_175_simple5regular':True,'controller_D3':bad is None,'first_R3_failure':bad}
        if bad:outcomes.append(row);continue
        D3+=1;summary,domains,words,reverse=helper.route_gate(G,perms,conic_index)
        row['unique_route_gate']=summary
        goodgeneral=not summary['general120_empty_edges'];goodconic=not summary['conic24_empty_edges']
        general+=int(goodgeneral);conic+=int(goodconic)
        k='conic24_interface' if goodconic else ('general120_interface' if goodgeneral else 'literalD3_all_mapgates_fail')
        if selected is None or priority[k]>priority[kind]:
            kind=k;selected={'surgery':s,'retained_old_labels':oldlabels,'controller':G,'reverse_ports':reverse,'all70_root_R3_cardinalities':coverage,'unique_route_gate':summary,'edge_domains':domains,'distance3_routes':[{'source':a,'target':b,'words':ws} for (a,b),ws in sorted(words.items())]}
        outcomes.append(row)
        if goodconic:
            complete=si+1==len(survivors);break
    save('SURVIVOR_OUTCOMES.json',outcomes)
    if selected is not None:
        folder=HERE/'selected_controller';folder.mkdir(exist_ok=True)
        save('SELECTED_INTERFACE.json',{'kind':kind,'controller_folder':'selected_controller'})
        (folder/'INPUT.json').write_text(json.dumps({k:v for k,v in selected.items() if k not in ['edge_domains','distance3_routes']},indent=2)+'\n')
        (folder/'EDGE_DOMAINS.json').write_text(json.dumps(selected['edge_domains'],indent=2)+'\n')
        (folder/'DISTANCE3_ROUTES.json').write_text(json.dumps(selected['distance3_routes'],indent=2)+'\n')
        with (folder/'controller_d5_D3_n70.edges').open('w') as f:
            f.write('70 175\n')
            for i,row in enumerate(selected['controller']):
                for j in row:
                    if i<j:f.write(f'{i} {j}\n')
    if conic:status='CONIC24_NEW70_CONTROLLER_INTERFACE_FOUND'
    elif general:status='GENERAL120_NEW70_CONTROLLER_INTERFACE_FOUND'
    elif complete and D3==0:status='COMPLETE_ALL105_MATCHINGS_NO_D3_CONTROLLER'
    elif complete:status='D3_CONTROLLERS_EXIST_BUT_ALL_UNIQUE_MAP_GATES_FAIL'
    else:status='PARTIAL_BUDGET_NO_FULL_FAMILY_CLAIM'
    result={'status':status,'inherited_purecross_assignments_not_rerun':4320,'new_assignments_evaluated':14580,'combined_potential_assignments':18900,'new_matching_types_per_edge':81,'matching_type_counts_per_edge':dict(sorted(typehist.items())),'boundary_survivors':len(survivors),'boundary_failures_by_pair_type':dict(failedpairhist),'boundary_survivors_processed':len(outcomes),'all_survivors_processed':complete,'new_D3_controllers':D3,'general120_interface_controllers':general,'conic24_interface_controllers':conic,'selected_interface_kind':kind,'boundary_stage_CPU_seconds':boundary_cpu,'total_CPU_seconds':time.process_time()-start,'CPU_hard_budget_seconds':15,'oldsource_BFS':0,'oldcross_assignments_retested':0,'new_fiber_graphs':0,'solver_calls':0,'new_Lean':0,'active_handles':[],'scope':'OnlyExoo72deleteadjacent2points,retainotherHedges,maxdegree5edge-repair. Allpartialmatchingsmaycompleteonindependent8pointboundary. Otherdeletions/sources/general70controllersnotexcluded.'}
    save('RESULT.json',result)
    save('TERMINAL.json',{'status':status,'running':False,'fibergraphs_added':0,'solver_calls':0,'next':'Returnactualinterfaceifany;otherwisecloseonlythecompletedlocaledge-repairdomain. Noautomaticfurtherlocalsurgery/maps/seed/SAT.'})
    print(json.dumps(result))

if __name__=='__main__':main()
