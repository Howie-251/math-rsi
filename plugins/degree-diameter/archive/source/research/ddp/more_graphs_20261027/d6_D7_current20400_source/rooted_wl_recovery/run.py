"""Decode only the sparse6 literal; canonical rooted1WL, at most two roots."""
from array import array
from collections import Counter
from pathlib import Path
import json
import re
import resource
import time

START=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(10,10))
import networkx as nx

OUT=Path(__file__).resolve().parent
SCRIPT=OUT.parent/'20400_d6D7_SageMath.author.txt'
text=SCRIPT.read_text()
literals=re.findall(r'Graph\(\s*[rR]?["\'](:[^"\']+)["\']\s*\)',text)
assert literals
literal=max(literals,key=len)
# Do not evaluate/import/run any part of the primary script.
G=nx.from_sparse6_bytes(literal.encode('ascii'))
n=G.number_of_nodes();m=G.number_of_edges()
assert (n,m)==(20400,61200) and set(G)==set(range(n))
adj=[sorted(G[v]) for v in range(n)]
assert Counter(map(len,adj))==Counter({6:n})
assert nx.number_of_selfloops(G)==0
decode_cpu=time.process_time()-START

csr=array('I',[n,2*m]);offsets=[0]
for row in adj:offsets.append(offsets[-1]+len(row))
csr.extend(offsets)
for row in adj:csr.extend(row)
(OUT/'adjacency.csr.u32le.bin').write_bytes(csr.tobytes())

def refine(root):
    began=time.process_time()
    colors=[0]*n;colors[root]=1
    rounds=[];old_count=2;status='ROUND_LIMIT_NOT_DISCRETE'
    for step in range(1,21):
        if time.process_time()-START>9.2:
            status='CPU_LIMIT_NOT_DISCRETE';break
        signatures=[(colors[v],tuple(sorted(colors[w] for w in adj[v]))) for v in range(n)]
        ordered=sorted(set(signatures))
        ids={sig:i for i,sig in enumerate(ordered)}
        colors=[ids[sig] for sig in signatures]
        sizes=Counter(colors)
        count=len(sizes);maximum=max(sizes.values())
        rounds.append({'round':step,'class_count':count,'max_cell':maximum,
                       'singleton_cells':sum(s==1 for s in sizes.values())})
        if count==n:
            status='DISCRETE';break
        if count==old_count:
            status='STABLE_NOT_DISCRETE';break
        old_count=count
    sizes=Counter(colors)
    result={'root':root,'status':status,'rounds':rounds,'final_class_count':len(sizes),
            'max_cell':max(sizes.values()),'cell_size_histogram':dict(Counter(sizes.values())),
            'initial_colors':'root1/allother0','canonical_signature_order':'wholegraphlex(oldcolor,sortedneighborcolors)',
            'CPU_seconds':time.process_time()-began}
    (OUT/f'root{root}.colors.u32le.bin').write_bytes(array('I',colors).tobytes())
    (OUT/f'root{root}.json').write_text(json.dumps(result,indent=2)+'\n')
    return colors,result

colors0,res0=refine(0)
result={'status':'ROOT0_NOT_DISCRETE_STOP','source_script':str(SCRIPT),'sparse6_literal_count':len(literals),
        'selected_literal_characters':len(literal),'author_script_executed':False,
        'source_n':n,'source_m':m,'degree_histogram':{'6':n},'simple':True,
        'source_reported_D':7,'source_D7_BFS_repeated':False,'decode_import_CPU_seconds':decode_cpu,
        'root0':res0,'second_root_attempted':False,'graph_BFS':0,'candidate_graphs':0,
        'group_search':False,'additional_anchors_or_2WL':False,
        'prediction_disposition':'SUPPORTED' if res0['status']=='DISCRETE' else 'REFUTED' if res0['status']=='STABLE_NOT_DISCRETE' else 'UNKNOWN'}
if res0['status']=='DISCRETE':
    neighbor=min(adj[0])
    colors1,res1=refine(neighbor)
    result.update(second_root_attempted=True,second_root=res1,first_neighbor=neighbor)
    if res1['status']=='DISCRETE':
        inverse_colors=[0]*n
        for v,c in enumerate(colors1):inverse_colors[c]=v
        pi=[inverse_colors[c] for c in colors0]
        bijective=len(set(pi))==n
        root_image=pi[0]
        failures=[];checked=0
        for u in range(n):
            for v in adj[u]:
                if u<v:
                    checked+=1
                    if not G.has_edge(pi[u],pi[v]):failures.append([u,v,pi[u],pi[v]])
        valid=bijective and root_image==neighbor and not failures and checked==m
        (OUT/'automorphism.pi.u32le.bin').write_bytes(array('I',pi).tobytes())
        check={'status':'ACTUAL_AUTOMORPHISM_VERIFIED' if valid else 'CANDIDATE_MAP_REJECTED',
               'n':n,'m':m,'bijection':bijective,'root':0,'expected_root_image':neighbor,
               'actual_root_image':root_image,'undirected_edges_checked':checked,
               'edge_failures':failures,'permutation_file':str(OUT/'automorphism.pi.u32le.bin'),
               'first20_images':pi[:20],'construction':'Match identical canonical singleton colors from rooted0 and rootedfirstneighbor runs'}
        (OUT/'AUTOMORPHISM_CHECK.json').write_text(json.dumps(check,indent=2)+'\n')
        result.update(status=check['status'],automorphism_check=check)
    else:result['status']='SECOND_ROOT_NOT_DISCRETE_STOP'
result.update(CPU_seconds=time.process_time()-START,running=False,pending=[])
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
