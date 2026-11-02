"""Complete five actual generator automorphisms from cached CSR/colors."""
from array import array
from collections import Counter
from pathlib import Path
import json
import math
import resource
import time

START=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(5,5))
OUT=Path(__file__).resolve().parent
BASE=OUT.parent
data=array('I');data.frombytes((BASE/'adjacency.csr.u32le.bin').read_bytes())
n,twom=data[0],data[1];m=twom//2
assert (n,m)==(20400,61200)
offsets=data[2:2+n+1];flat=data[2+n+1:]
assert len(flat)==twom and offsets[-1]==twom
adj=[list(flat[offsets[v]:offsets[v+1]]) for v in range(n)]
assert all(len(r)==6 for r in adj)
adjsets=[set(r) for r in adj]
neighbors=sorted(adj[0])
c0=array('I');c0.frombytes((BASE/'root0.colors.u32le.bin').read_bytes())
assert len(c0)==n and len(set(c0))==n
first=json.loads((BASE/'AUTOMORPHISM_CHECK.json').read_text())
assert first['status']=='ACTUAL_AUTOMORPHISM_VERIFIED' and first['expected_root_image']==850
first_pi=array('I');first_pi.frombytes((BASE/'automorphism.pi.u32le.bin').read_bytes())
maps={850:list(first_pi)}
meta={850:{'neighbor':850,'map_file':str(BASE/'automorphism.pi.u32le.bin'),
           'reused_prior_map_and_edgecheck':True,'new_WL_run':False,
           'root_WL_file':str(BASE/'root850.json'),'bijection':True,
           'root_image':850,'edges_checked':61200,'edge_failures':0}}
status='ALL_SIX_ACTUAL_AUTOMORPHISMS_VERIFIED'

def refine(root):
    began=time.process_time();colors=[0]*n;colors[root]=1;oldcount=2;rounds=[]
    stop='ROUND_LIMIT_NOT_DISCRETE'
    for step in range(1,21):
        if time.process_time()-START>4.4:
            stop='CPU_LIMIT_NOT_DISCRETE';break
        signatures=[(colors[v],tuple(sorted(colors[w] for w in adj[v]))) for v in range(n)]
        ordered=sorted(set(signatures));ids={sig:i for i,sig in enumerate(ordered)}
        colors=[ids[sig] for sig in signatures];sizes=Counter(colors);count=len(sizes)
        rounds.append({'round':step,'class_count':count,'max_cell':max(sizes.values())})
        if count==n:stop='DISCRETE';break
        if count==oldcount:stop='STABLE_NOT_DISCRETE';break
        oldcount=count
    record={'root':root,'status':stop,'rounds':rounds,'CPU_seconds':time.process_time()-began}
    (OUT/f'root{root}.json').write_text(json.dumps(record,indent=2)+'\n')
    return colors,record

for v in neighbors:
    if v==850:continue
    colors,wl=refine(v)
    if wl['status']!='DISCRETE':status='PARTIAL_RECOVERY_'+wl['status'];break
    invcolors=[0]*n
    for w,c in enumerate(colors):invcolors[c]=w
    pi=[invcolors[c] for c in c0]
    bijective=len(set(pi))==n;checked=0;failed=[]
    for u in range(n):
        for w in adj[u]:
            if u<w:
                checked+=1
                if pi[w] not in adjsets[pi[u]]:failed.append([u,w,pi[u],pi[w]])
    assert bijective and pi[0]==v and checked==m and not failed
    f=OUT/f'pi_0_to_{v}.u32le.bin';f.write_bytes(array('I',pi).tobytes())
    maps[v]=pi
    meta[v]={'neighbor':v,'map_file':str(f),'reused_prior_map_and_edgecheck':False,
             'new_WL_run':True,'root_WL_file':str(OUT/f'root{v}.json'),
             'WL_rounds':len(wl['rounds']),'WL_final_class_count':n,
             'bijection':True,'root_image':v,'edges_checked':checked,'edge_failures':0}

if len(maps)==6:
    for v in neighbors:
        pi=maps[v];seen=[False]*n;cycles=[];order=1
        for start in range(n):
            if seen[start]:continue
            w=start;length=0
            while not seen[w]:seen[w]=True;length+=1;w=pi[w]
            assert w==start
            cycles.append(length);order=math.lcm(order,length)
        inv=[0]*n
        for w,image in enumerate(pi):inv[image]=w
        inverse_neighbor=inv[0]
        assert inverse_neighbor in maps and maps[inverse_neighbor]==inv
        meta[v].update(element_order=order,cycle_length_histogram=dict(Counter(cycles)),
                       inverse_neighbor=inverse_neighbor,
                       inverse_generator_index=neighbors.index(inverse_neighbor),
                       full_inverse_permutation_binding_checked=True)
        assert n%order==0 and set(cycles)=={order}

result={'status':status,'source_n':n,'source_m':m,'degree':6,
        'source_CSR':str(BASE/'adjacency.csr.u32le.bin'),
        'source_CSR_layout':'little-endian uint32 n,2m,n+1offsets,then2mneighbors',
        'N0':neighbors,'actual_automorphisms':len(maps),'new_WL_runs':len(maps)-1,
        'first_automorphism_recomputed':False,'first_automorphism_edgecheck_repeated':False,
        'generators':[meta[v] for v in neighbors if v in meta],
        'group_generated_orbit_enumerated':False,'multiplication_table_built':False,
        'group_transitive_by_proof':len(maps)==6,
        'root_stabilizer_trivial_by_discrete_root0_WL':True,
        'generated_group_order':n if len(maps)==6 else None,
        'full_Aut_group_order':n if len(maps)==6 else None,
        'connectivity_basis':'Inherited published sourceD7, not a new BFS',
        'Cayley_convention':'Permutations act onleft; identifygwithg(0).Neighbors ofg(0)are(g composedwith pi_s)(0), so the sixmaps define rightgeneratorsteps undercomposition.',
        'source_sparse6_reparsed':False,'graph_BFS':0,'candidate_graphs':0,
        'CPU_seconds':time.process_time()-START,'running':False,'pending':[]}
(OUT/'GENERATORS.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
