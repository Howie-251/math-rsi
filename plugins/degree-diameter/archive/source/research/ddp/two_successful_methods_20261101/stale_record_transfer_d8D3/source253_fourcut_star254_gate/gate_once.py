#!/usr/bin/env python3
"""Project cached unique3 witnesses; no uniqueness/BFS/source revalidation."""
from collections import Counter
import csv
import json
import os
from pathlib import Path
import resource
import time
import traceback

START=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(8,8))
HERE=Path(__file__).resolve().parent
REPO=next(p for p in HERE.parents if (p/'AGENTS.md').is_file())
BASE=REPO/'context/DD_PORTFOLIO_START_20261026'
SCOUT=REPO/'research/ddp/breadth_20261027_wave10/degree_reduction_scout'
PRIOR=.8
PREPARATION=.2
INDEPENDENT_READ=.25

def write(name,data):
    (HERE/name).write_text(json.dumps(data,indent=2)+'\n')

write('GATE_HANDLE.json',{'status':'RUNNING','pid':os.getpid(),'single_worker':True,
    'stage':'cachedwitness projection then fourcompleteotheredge capacity profiles',
    'prior_read_CPU_seconds':PRIOR,'new_preparation_charge_CPU_seconds':PREPARATION,
    'independent_scope_reader_CPU_seconds':INDEPENDENT_READ,'process_hard_CPU_seconds':8,
    'wholecase_CPU_cap_seconds':10})
try:
    spec=next(s for s in json.loads((BASE/'baselines/generator_specs.json').read_text()) if s['id']=='d8_D3')
    assert (spec['m'],spec['n'],spec['a'])==(11,23,9)
    positives=[tuple(g) for g in spec['generators']]
    encode=lambda g:23*g[0]+g[1]
    decode=lambda u:divmod(u,23)
    factors=[pow(9,j,23) for j in range(11)]
    def mul(u,v):
        x,y=decode(u);a,b=decode(v)
        return ((x+a)%11)*23+(y*factors[a]+b)%23
    def inverse(u):
        x,y=decode(u);a=(-x)%11
        return 23*a+(-y*factors[a])%23
    gens=[encode(g) for g in positives]
    with (BASE/'baselines/d8_D3_known.edges').open() as stream:
        assert tuple(map(int,next(stream).split()))==(253,1012)
        source={tuple(map(int,line.split())) for line in stream if line.strip()}
    assert len(source)==1012 and all(0<=u<v<253 for u,v in source)
    adj=[set() for _ in range(253)]
    for u,v in source:
        adj[u].add(v);adj[v].add(u)
    edge_parameters=[]
    orientation={}
    for h in range(253):
        for kind,s in enumerate(gens):
            v=mul(h,s)
            edge=tuple(sorted((h,v)))
            assert edge not in orientation
            record={'source_positive_edge_index':len(edge_parameters),'h':h,'type':kind,'hs':v,'edge':list(edge)}
            edge_parameters.append(record)
            orientation[edge]=record
    assert set(orientation)==source and len(edge_parameters)==1012
    old=json.loads((SCOUT/'source253_to_degree7.forced_edges.json').read_text())
    assert len(old)==1012
    normalized=[{} for _ in range(4)]
    projection_records=[]
    raw_position_counts=[Counter() for _ in range(4)]
    for cache_index,row in enumerate(old):
        cut=tuple(row['edge'])
        orient=orientation[tuple(sorted(cut))]
        h,kind,hs=orient['h'],orient['type'],orient['hs']
        path=list(row['unique3_path'])
        assert len(path)==4 and len(set(path))==4
        assert all(tuple(sorted(e)) in source for e in zip(path,path[1:]))
        positions=[i for i,e in enumerate(zip(path,path[1:])) if tuple(sorted(e))==tuple(sorted(cut))]
        assert len(positions)==1
        old_position=positions[0]
        reversed_whole=path[old_position]!=h
        if reversed_whole:
            path.reverse()
        position=2-old_position if reversed_whole else old_position
        assert path[position:position+2]==[h,hs]
        translated=[mul(inverse(h),u) for u in path]
        assert translated[position:position+2]==[0,gens[kind]]
        assert all(tuple(sorted(e)) in source for e in zip(translated,translated[1:]))
        if position==1:
            hitset=sorted({translated[0],translated[3]})
        elif position==0:
            hitset=sorted(adj[translated[3]]|{translated[3]})
        else:
            hitset=sorted(adj[translated[0]]|{translated[0]})
        assert not ({0,gens[kind]}&set(hitset))
        raw_position_counts[kind][position]+=1
        evidence={'cached_edge_record_index':cache_index,'old_edge':list(cut),'positive_h':h,
                  'positive_type':kind,'path_before_orientation':row['unique3_path'],
                  'whole_path_reversed':reversed_whole,'old_cut_position':old_position,
                  'canonical_cut_position':position,'normalized_path':translated,'hitset':hitset}
        projection_records.append(evidence)
        key=tuple(translated)
        if key not in normalized[kind]:
            normalized[kind][key]={'normalized_path':translated,'cut_position':position,'hitset':hitset,'cached_record_indices':[]}
        normalized[kind][key]['cached_record_indices'].append(cache_index)
    write('GATE_ALL1012_WITNESS_PROJECTIONS.json',{'source_cache':str((SCOUT/'source253_to_degree7.forced_edges.json').relative_to(REPO)),
        'original_unique3_geodesic_status':'INHERITED_NOT_RECHECKED','records':projection_records,
        'RIGHT_rule':'h*s','normalization':'reversewholepathifneeded then leftmultiplyh^-1',
        'literal_source_parse_count':1,'literal_source_edges_equal_actual_positive_recipe':True})
    profiles=[]
    for kind in range(4):
        obligations=sorted(normalized[kind].values(),key=lambda r:tuple(r['normalized_path']))
        vertex_masks=[0]*253
        for i,obligation in enumerate(obligations):
            obligation['obligation_id']=i
            for v in obligation['hitset']:
                vertex_masks[v]|=1<<i
        s=gens[kind]
        excluded=0
        admitted=[]
        classes={}
        maxhit=0
        maxedge=None
        for record in edge_parameters:
            h,v=record['h'],record['hs']
            if 0 in (h,v) or s in (h,v):
                excluded+=1
                continue
            mask=vertex_masks[h]|vertex_masks[v]
            covered=mask.bit_count()
            item={**record,'obligation_mask_hex':hex(mask),'obligations_hit':covered}
            admitted.append(item)
            classes.setdefault(mask,[]).append(record['source_positive_edge_index'])
            if covered>maxhit or maxedge is None:
                maxhit=covered;maxedge=item
        assert excluded==15 and len(admitted)==997
        with (HERE/f'GATE_TYPE{kind}_ALL997_EDGE_MASKS.tsv').open('w',newline='') as stream:
            out=csv.writer(stream,delimiter='\t')
            out.writerow(['source_positive_edge_index','h','type','hs','obligations_hit','mask_hex'])
            for row in admitted:
                out.writerow([row['source_positive_edge_index'],row['h'],row['type'],row['hs'],row['obligations_hit'],row['obligation_mask_hex']])
        middle=[r for r in obligations if r['cut_position']==1]
        left=sorted(adj[0]-{s});right=sorted(adj[s]-{0})
        middle_edges=sorted({(r['normalized_path'][0],r['normalized_path'][3]) for r in middle})
        graph={u:[] for u in left}
        for u,v in middle_edges:
            assert u in left and v in right
            graph[u].append(v)
        owner={}
        def augment(u,seen):
            for v in graph[u]:
                if v in seen:continue
                seen.add(v)
                if v not in owner or augment(owner[v],seen):
                    owner[v]=u
                    return True
            return False
        for u in left:
            augment(u,set())
        matching=sorted((u,v) for v,u in owner.items())
        assert len({x for e in matching for x in e})==2*len(matching)
        position_counts=Counter(r['cut_position'] for r in obligations)
        capacity_no=3*maxhit<len(obligations)
        profile={'first_type':kind,'positive_generator':positives[kind],'positive_label':s,
            'raw_cached_projected_records':sum(raw_position_counts[kind].values()),
            'raw_position_counts':dict(sorted(raw_position_counts[kind].items())),
            'distinct_normalized_path_obligations':len(obligations),
            'distinct_hitsets':len({tuple(r['hitset']) for r in obligations}),
            'normalized_position_counts':dict(sorted(position_counts.items())),
            'valid_witness_subset_only':True,'all1012_edge_parameters_considered':True,
            'firstcut_incident_edges_excluded_before_mask':excluded,'admissible_otheredges':997,
            'edge_mask_classes':len(classes),'zero_mask_edges':len(classes.get(0,[])),
            'maximum_single_otheredge_hits':maxhit,'three_otheredges_upper_bound':3*maxhit,
            'strict_three_edge_capacity_NO':capacity_no,'first_maxhit_edge':maxedge,
            'middle_subset':{'left_labels':left,'right_labels':right,'edges':middle_edges,
                'maximum_matching_size':len(matching),'matching_real_vertex_labels':matching,
                'seven_matching_obstruction':len(matching)==7,'not_a_complete_critical_graph':True}}
        profiles.append(profile)
        write(f'GATE_TYPE{kind}_OBLIGATIONS_AND_CLASSES.json',{
            'profile':profile,'obligations':obligations,
            'edge_mask_classes':[{'mask_hex':hex(mask),'hit_count':mask.bit_count(),
                                 'edge_count':len(ids),'all_source_positive_edge_indices':ids}
                                 for mask,ids in sorted(classes.items())],
            'position_hit_rules':{'0':'closedB1(pathlast)','1':'{pathfirst,pathlast}','2':'closedB1(pathfirst)'},
            'all_otheredge_data':f'GATE_TYPE{kind}_ALL997_EDGE_MASKS.tsv'})
    all_capacity=all(p['strict_three_edge_capacity_NO'] for p in profiles)
    result={'status':'COMPLETE_NO_FIXED_CM253_FOURCUT8STAR_BY_CACHED_WITNESS_CAPACITY' if all_capacity else
                     'CACHED_WITNESS_CAPACITY_PREDICTION_REFUTED_FOURCUT_STAR_NOT_CLOSED_BY_THIS_CAPACITY_TEST',
        'profiles':profiles,'all_four_classes_strict_three_edge_capacity_NO':all_capacity,
        'capacity_prediction_supported':all_capacity,
        'actual_source':'CM253/rightC11semidirect9C23/literalbound',
        'cached_input_records':1012,'literal_source_parse_count':1,
        'old_unique3_status':'INHERITED; no unique3revalidation or fullword enumeration',
        'new_BFS_field_sourcevalidation_or_fourcutenumeration':0,'new_graphs':0,
        'scope':'Only actualsourcefourvertexdisjointoldcuts+one8star; validcachedwitnesssubset, not fullcriticalmatrix',
        'next':'STOP; rootdispositions fullcapacityNO or chooses newfullword/cutjoin fromactualfeedback; noautomaticextension'}
except Exception as exc:
    result={'status':'UNKNOWN_CACHED_WITNESS_GATE_INPUT_OR_PROCESS_FAILURE','error_type':type(exc).__name__,
        'error':str(exc),'traceback':traceback.format_exc(),'scope':'No mathematicalfamilyNO','next':'STOP preservefailure'}
actual=time.process_time()-START
total=PRIOR+PREPARATION+INDEPENDENT_READ+actual
result.update({'prior_source_read_CPU_seconds':PRIOR,'new_preparation_charge_CPU_seconds':PREPARATION,
    'independent_reader_charge_CPU_seconds':INDEPENDENT_READ,'actual_process_CPU_seconds':actual,
    'wholecase_CPU_seconds':total,'wholecase_CPU_cap_seconds':10})
write('GATE_RESULT.json',result)
write('GATE_TERMINAL.json',{**result,'terminal':True,'active_processes':0})
write('GATE_HANDLE.json',{'status':result['status'],'pid':os.getpid(),'terminal':True,'active_processes':0,
    'wholecase_CPU_seconds':total})
print(json.dumps(result))
