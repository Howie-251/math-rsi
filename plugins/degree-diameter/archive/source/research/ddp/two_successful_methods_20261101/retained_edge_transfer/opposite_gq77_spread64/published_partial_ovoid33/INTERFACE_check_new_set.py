import collections,csv,itertools,json,resource,time
from pathlib import Path

start=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(5,6))
D=Path(__file__).resolve().parent
source=json.loads((D.parent/'PARAMETERS.json').read_text())
declared=json.loads((D/'ACTUAL_POINTS.json').read_text())
P=declared['point_ids']
assert len(P)==33 and len(set(P))==33 and all(0<=p<400 for p in P)
points=source['points'];Gram=source['alternating_form_matrix'];lines={r['line']:r['points'] for r in source['lines']}
through=source['point_incident_lines'];spread=source['spread_line_labels'];owners=source['point_spread_owner']
assert [points[p] for p in P]==declared['points_mod7']
pairvalues=[]
for i,j in itertools.combinations(range(33),2):
    x,y=points[P[i]],points[P[j]]
    B=sum(x[a]*Gram[a][b]*y[b] for a in range(4) for b in range(4))%7
    assert B!=0
    pairvalues.append((i,j,P[i],P[j],B))
assert len(pairvalues)==528
newowners=[owners[p] for p in P]
assert len(set(newowners))==33 and newowners==declared['point_spread_owners']
linecounts=collections.Counter()
for p in P:
    for line in through[p]:linecounts[line]+=1
assert all(n==1 for n in linecounts.values()) and len(linecounts)==264
for p,owner in zip(P,newowners):assert p in lines[spread[owner]]
ownerof=[-1]*160050;centers=[];pinlists=[];rows=[];flagcenters=0;oldpins=0;fillpins=0
with (D/'INTERFACE_PINS.tsv').open('w') as pinout:
    pinout.write('center_index\tsource_pin_label\n')
    for i,p in enumerate(P):
        for j,line in enumerate(spread):
            index=50*i+j;center=400*p+line;centers.append(center)
            N=[400*x+m for x in lines[line] for m in through[p] if not(x==p and m==line)]
            flag=p in lines[line];bonus=-1
            if flag:
                assert newowners[i]==j
                bonus=160000+j;N.append(bonus);flagcenters+=1
            N.sort()
            assert len(N)==64 and len(set(N))==64
            for v in N:
                assert ownerof[v]==-1
                ownerof[v]=index
                oldpins+=v<160000;fillpins+=v>=160000
                pinout.write(f'{index}\t{v}\n')
            pinlists.append(N)
            rows.append([index,i,j,p,line,center,int(flag),bonus,64-int(flag),int(flag)])
assert len(centers)==1650 and len(set(centers))==1650
assert flagcenters==33 and oldpins==105567 and fillpins==33
used=sum(x>=0 for x in ownerof)
assert used==105600 and 160050-used==54450
center_set=set(centers);induced_edges=[];induced_degrees=collections.Counter()
for c,N in zip(centers,pinlists):
    induced=[v for v in N if v in center_set];induced_degrees[len(induced)]+=1
    induced_edges.extend((c,v) for v in induced if c<v)
assert induced_degrees=={0:594,1:1056} and len(induced_edges)==528
with (D/'INTERFACE_ORDERED_CENTERS.csv').open('w') as out:
    w=csv.writer(out);w.writerow(['center_index','point_index','spread_index','point_label','line_label','source_center_label','flag','original_fill_bonus_label','old_pins','fill_pins']);w.writerows(rows)
with (D/'INTERFACE_SELECTED_PAIR_VALUES.tsv').open('w') as out:
    w=csv.writer(out,delimiter='\t');w.writerow(['i','j','point_i','point_j','accepted_Gram_value_mod7']);w.writerows(pairvalues)
result={'status':'PASS_ACTUAL_P33_PARTIAL_OVOID_AND_FILLED_SOURCE_FULLN_BINDING','point_ids':P,'point_labels_and_coordinates_bound_to_original400_order':True,'selected_new_pairs_tested':528,'accepted_Gram_nonzero_for_all_selected_pairs':True,'old400_geometry_or_field_checks_repeated':False,'line_occupancy_histogram':{'0':136,'1':264},'distinct_spread_owners':33,'point_spread_owners':newowners,'source_n':160050,'source_m':5121600,'source_degree':64,'source_literal_big_edgefile_reads':0,'centers':1650,'source_flag_centers':33,'source_nonflag_centers':1617,'each_immutable_filled_source_fullN_size':64,'all_fullN_sets_pairwise_disjoint':True,'total_distinct_pins':105600,'old160000_pins':105567,'original_fill50_pins':33,'source_load_histogram':{'0':54450,'1':105600},'center_induced_graph':{'K2':528,'isolates':594},'P33_extra_structure_required':False,'complete_new_graphs_generated_or_accepted_here':0,'conditional_targets':[{'Delta':65,'D':3,'copies':1,'n':161700,'m':5227200,'degree_histogram':{'64':56100,'65':105600},'baseline_parent_updated':161650,'conditional_margin':50},{'Delta':70,'D':3,'copies':6,'n':169950,'m':5755200,'degree_histogram':{'64':64350,'70':105600},'baseline_parent_updated':169900,'conditional_margin':50}],'BFS_Lean_external_review_solver_calls':0,'other_pointsets_searched':0,'CPU_seconds':time.process_time()-start,'CPU_budget_seconds':5,'all_local_processes_terminal':True,'evidence':['INTERFACE_NEW_SET_PRED.md','INTERFACE_ORDERED_CENTERS.csv','INTERFACE_PINS.tsv','INTERFACE_SELECTED_PAIR_VALUES.tsv','INTERFACE_NOTE.md']}
(D/'INTERFACE_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
