"""Exactly three inverse-pair subsets on the actual regular permutation group."""
from array import array
from collections import Counter,deque
from itertools import combinations
from pathlib import Path
import json
import resource
import time

START=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(2,2))
OUT=Path(__file__).resolve().parent
META=OUT.parent/'rooted_wl_recovery/six_generators/GENERATORS.json'
source=json.loads(META.read_text());n=20400
assert source['generated_group_order']==source['full_Aut_group_order']==n
perms=[]
for r in source['generators']:
    a=array('I');a.frombytes(Path(r['map_file']).read_bytes());assert len(a)==n
    perms.append(a)
pairs=[(0,3),(1,4),(2,5)];rows=[];hits=[]
for ordinal,selected_pairs in enumerate(combinations(range(3),2)):
    began=time.process_time()
    indices=[s for p in selected_pairs for s in pairs[p]]
    adj=[sorted({perms[s][v] for s in indices}) for v in range(n)]
    assert all(len(a)==4 and v not in a for v,a in enumerate(adj))
    assert all(v in adj[w] for v,a in enumerate(adj) for w in a)
    m=sum(map(len,adj))//2;assert m==40800
    d=[-1]*n;d[0]=0;q=deque([0])
    while q:
        v=q.popleft()
        for w in adj[v]:
            if d[w]<0:d[w]=d[v]+1;q.append(w)
    reached=sum(x>=0 for x in d);connected=reached==n
    ecc=max(d);hit=connected and ecc<=10
    missing=[v for v,x in enumerate(d) if x<0 or x>10]
    tag=''.join(map(str,selected_pairs))
    row={'ordinal':ordinal,'pair_ids':selected_pairs,'generator_indices':indices,
         'generator_root_images':[source['generators'][s]['neighbor'] for s in indices],
         'n':n,'m':m,'simple':True,'degree_histogram':{'4':n},'root':0,
         'connected':connected,'root_reached':reached,'root_eccentricity':ecc,
         'global_D':ecc if connected else None,
         'global_D_basis':'Theactualsourcegroupisregular; itsabstractrightregularactionpreservesedges v--pi_s(v) ofthisleftCayleygraph, henceallrootseccentricitiesagree.',
         'root_distance_histogram':dict(sorted(Counter(d).items())),
         'root_targets_outside_R10':len(missing),
         'first_target_outside_R10':missing[0] if missing else None,
         'status':'PRODUCER_COMPLETE_NEW_GRAPH_D4_D10_20400' if hit else 'FIXED_SUBSET_NO_D10',
         'source_old_D7_BFS':0,'root_BFS_runs':1,'CPU_seconds':time.process_time()-began}
    if hit:
        graph=OUT/f'graph_d4_D10_n20400_pairs{tag}.edges'
        with graph.open('w') as f:
            f.write(f'{n} {m}\n')
            for v,a in enumerate(adj):
                for w in a:
                    if v<w:f.write(f'{v} {w}\n')
        dist=OUT/f'root0_pairs{tag}.distances.u8.bin';dist.write_bytes(bytes(d))
        recipe={'n':n,'m':m,'degree':4,'target_D':10,'source_group_order':n,
                'source_generator_receipt':str(META),'pair_ids':selected_pairs,
                'generator_indices':indices,'generator_maps':[source['generators'][s]['map_file'] for s in indices],
                'edge_rule':'Forallv andselecteds, addunorderededge{v,pi_s(v)}; leftCayley, not claimed oldgraphsubgraph inoldlabels',
                'inverse_closed':True,'actual_graph_file':str(graph),'root_distance_file':str(dist),
                'root0_eccentricity':ecc,'connected':connected,
                'diameter_proof':'IdentifyoldlabelswithregularGamma byuniqueg(0). pi_s(v)=s*g; rightmultiplicationg->g*h preservesallleftSedges and istransitive.ThereforeglobalD=root0ecc.',
                'new_parameter_parent_verification_pending':True}
        rf=OUT/f'RECIPE_pairs{tag}.json';rf.write_text(json.dumps(recipe,indent=2)+'\n')
        row.update(graph_file=str(graph),recipe_file=str(rf),distance_file=str(dist))
        hits.append(row)
        print('HIT '+json.dumps(row),flush=True)
    rows.append(row)
result={'status':'COMPLETE_THREE_FIXED_PAIR_SUBSETS','source_group_order':n,'target_Delta':4,'target_D':10,
        'savedL':19306,'cases':3,'cases_completed':len(rows),'unattempted':0,'UNKNOWN':0,
        'hits':hits,'rows':rows,'new_graphs':len(hits),'candidate_graphs_constructed_in_memory':3,
        'complete_target_D10_hits':len(hits),'exported_candidate_graphs':len(hits),
        'global_diameter_from_VT_proof':True,
        'oldsource_D7_BFS_runs':0,'candidate_root_BFS_runs':3,
        'new_source_downloads':0,'generator_tuning':False,'CPU_seconds':time.process_time()-START,
        'running':False,'pending':[]}
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print('TERMINAL '+json.dumps(result,indent=2))
