#!/usr/bin/env python3
"""Only saved312boundary survivors: new70controllerD3 and necessary map gates.
At mostone interface saved; no fiber graph, SAT or old-source BFS.
"""
import itertools
import json
import time
from collections import Counter,defaultdict
from pathlib import Path
HERE=Path(__file__).resolve().parent
PARENT=HERE.parent

def save(path,data):path.write_text(json.dumps(data,indent=2)+'\n')
def radius3(N,root):
    reach=1<<root
    for depth in range(3):
        new=reach;scan=reach
        while scan:
            bit=scan&-scan;scan-=bit;new|=N[bit.bit_length()-1]
        reach=new
    return reach

def route_gate(C,perms,conic_index):
    n=len(C);reverse=[[C[v].index(u) for v in row] for u,row in enumerate(C)]
    edges=[];dart={}
    for u,row in enumerate(C):
        for p,v in enumerate(row):
            if u>=v:continue
            r=reverse[u][p];ei=len(edges)
            edges.append({'edge':ei,'source':u,'target':v,'port':p,'reverse_port':r})
            dart[u,p]=(ei,False);dart[v,r]=(ei,True)
    assert len(edges)==175
    close=[];words=defaultdict(list)
    for u in range(n):
        low={u,*C[u]};low.update(C[a][q] for a in C[u] for q in range(5));close.append(low)
        for p,a in enumerate(C[u]):
            i=reverse[u][p]
            for q,b in enumerate(C[a]):
                if q==i:continue
                ei,rev=dart[a,q]
                for r,v in enumerate(C[b]):
                    if r==reverse[a][q] or v in low:continue
                    pair=(r,i) if rev else (i,r)
                    words[u,v].append({'vertices':[u,a,b,v],'ports':[p,q,r],'central_edge':ei,'reverse':rev,'normalized_forbidden_entry':pair})
    constraints=[{} for _ in edges];unique=0
    for (u,v),ws in words.items():
        if len(ws)==1:
            unique+=1;w=ws[0];key=tuple(w['normalized_forbidden_entry'])
            constraints[w['central_edge']].setdefault(key,{'source':u,'target':v,'word':w})
    conicempty=[];generalempty=[];hc=Counter();hg=Counter()
    for e,cs in zip(edges,constraints):
        p,r=e['port'],e['reverse_port']
        good=[pi for pi in perms if all(pi[i]!=j for i,j in cs)]
        cg=[conic_index[pi] for pi in good if pi[p]==r]
        e['unique_forbidden_entries']=[{'entry':key,'witness':w} for key,w in sorted(cs.items())]
        e['conic24_allowed_map_indices']=cg;e['general120_allowed_quotient_permutations']=good
        hc[len(cg)]+=1;hg[len(good)]+=1
        if not cg:conicempty.append(e['edge'])
        if not good:
            generalempty.append(e['edge']);I=[i for i in range(5) if i!=p];hall=None
            for size in range(1,5):
                for S in itertools.combinations(I,size):
                    J=sorted({j for i in S for j in range(5) if (i,j) not in cs})
                    if len(J)<len(S):hall={'rows':S,'columns':J,'joker_column':r};break
                if hall:break
            assert hall;e['general_Hall_obstruction']=hall
    summary={'ordered_distance3_pairs':len(words),'unique_ordered_distance3_pairs':unique,'distance3_word_count_histogram':dict(sorted(Counter(len(v) for v in words.values()).items())),'conic24_empty_edges':conicempty,'general120_empty_edges':generalempty,'conic_domain_size_histogram':dict(sorted(hc.items())),'general_domain_size_histogram':dict(sorted(hg.items()))}
    return summary,edges,words,reverse

def main():
    start=time.process_time()
    previous=json.loads((HERE/'PREFLIGHT_RESULT.json').read_text())
    source=json.loads((PARENT/'Exoo72/INPUT.json').read_text())['controller']
    survivors=json.loads((HERE/'BOUNDARY_SURVIVORS.json').read_text())
    perms=list(itertools.permutations(range(5)))
    maps=json.loads((PARENT/'SEMILINEAR_MAPS.json').read_text())
    conic_index={tuple(T['conic_permutation']):i for i,T in enumerate(maps)};assert len(conic_index)==120
    outcomes=[];first_failure_root=Counter();d3count=0;generalcount=0;coniccount=0;selected=None;selection_kind=None;complete=True
    for ix,s in enumerate(survivors):
        if time.process_time()-start+previous['CPU_seconds']>19:
            complete=False;break
        u,v=s['deleted'];old=[x for x in range(72) if x not in (u,v)];label={x:i for i,x in enumerate(old)}
        C=[{label[y] for y in source[x] if y not in (u,v)} for x in old]
        for i,j in enumerate(s['sigma']):
            a,b=label[s['A'][i]],label[s['B'][j]];assert b not in C[a];C[a].add(b);C[b].add(a)
        C=[sorted(row) for row in C]
        assert all(len(row)==5 and i not in row for i,row in enumerate(C))
        assert all(i in C[j] for i,row in enumerate(C) for j in row)
        assert sum(map(len,C))==350
        N=[sum(1<<y for y in row) for row in C];allbits=(1<<70)-1;bad=None;coverage=[]
        for root in range(70):
            reach=radius3(N,root);coverage.append(reach.bit_count())
            if reach!=allbits:
                missing=next(y for y in range(70) if not(reach>>y&1));bad={'root':root,'missing_target':missing,'old_root':old[root],'old_missing_target':old[missing],'root_R3_cardinality':reach.bit_count()};break
        row={'boundary_survivor_index':ix,**s,'literal_simple5regular':True,'controller_D3':bad is None,'first_R3_failure':bad}
        if bad:
            first_failure_root[bad['root']]+=1;outcomes.append(row);continue
        d3count+=1
        summary,edge_domains,words,reverse=route_gate(C,perms,conic_index)
        row['unique_route_gate']=summary
        general_ok=not summary['general120_empty_edges'];conic_ok=not summary['conic24_empty_edges']
        generalcount+=int(general_ok);coniccount+=int(conic_ok)
        kind='conic24_all_nonempty' if conic_ok else ('general120_all_nonempty' if general_ok else 'first_literalD3_example_all_map_gates_fail')
        priority={'first_literalD3_example_all_map_gates_fail':0,'general120_all_nonempty':1,'conic24_all_nonempty':2}
        if selected is None or priority[kind]>priority[selection_kind]:
            selected={'boundary_survivor_index':ix,**s,'retained_old_labels':old,'controller':C,'reverse_ports':reverse,'all70_root_R3_cardinalities':coverage,'unique_route_gate':summary,'edge_domains':edge_domains,'distance3_routes':[{'source':a,'target':b,'words':ws} for (a,b),ws in sorted(words.items())]}
            selection_kind=kind
        outcomes.append(row)
        if conic_ok:
            complete=ix+1==len(survivors);break
    if selected is not None:
        folder=HERE/'selected_controller';folder.mkdir(exist_ok=True)
        save(folder/'INPUT.json',{k:v for k,v in selected.items() if k not in ['edge_domains','distance3_routes']})
        save(folder/'EDGE_DOMAINS.json',selected['edge_domains'])
        save(folder/'DISTANCE3_ROUTES.json',selected['distance3_routes'])
        C=selected['controller']
        with (folder/'controller_d5_D3_n70.edges').open('w') as f:
            f.write('70 175\n')
            for u,row in enumerate(C):
                for v in row:
                    if u<v:f.write(f'{u} {v}\n')
    save(HERE/'SURVIVOR_OUTCOMES.json',outcomes)
    status='CONIC24_CONTROLLER_INTERFACE_FOUND' if coniccount else ('GENERAL120_CONTROLLER_INTERFACE_FOUND' if generalcount else ('COMPLETE_SURGERY_NO_CONTROLLER_D3' if d3count==0 and complete else ('COMPLETE_SURGERY_ALL_D3_CONTROLLERS_HALL_OBSTRUCTED' if complete else 'PARTIAL_BUDGET_NO_FULL_FAMILY_CLAIM')))
    result={'status':status,'source_parameter_assignments':4320,'boundary_survivors_total':len(survivors),'boundary_survivors_processed':len(outcomes),'all_boundary_survivors_processed':complete,'literal_simple5regular_checked':len(outcomes),'new_D3_controllers':d3count,'general120_all_edges_nonempty_controllers':generalcount,'conic24_all_edges_nonempty_controllers':coniccount,'first_R3_failure_root_histogram':dict(first_failure_root),'selected_controller_kind':selection_kind,'source_BFS':0,'new_fiber_graphs':0,'solver_calls':0,'survivor_stage_CPU_seconds':time.process_time()-start,'preflight_CPU_seconds':previous['CPU_seconds'],'total_measured_CPU_seconds':time.process_time()-start+previous['CPU_seconds'],'CPU_budget_seconds':20,'workers':1,'active_handles':[],'scope':'Only literalExoo72adjacentpair deletion plus4crossmatching;controller/interface counts not4480fibergraphresults.'}
    save(HERE/'RESULT.json',result)
    save(HERE/'TERMINAL.json',{'status':status,'running':False,'solver_calls':0,'fibergraphs_added':0,'next':'Return actual controller/map interface if present;do not autoSAT or othercontroller/portseed/surgery ladder.'})
    print(json.dumps(result))

if __name__=='__main__':main()
