"""One exact cover of four old involution edges; no graph search or BFS."""
from collections import Counter
from pathlib import Path
import json
import resource
import time

start=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(1,1))
out=Path(__file__).resolve().parent
data=json.loads((out.parent/'BLOCKS.json').read_text())
sigma=json.loads((out.parent/'involution_probe/sigma.json').read_text())['permutation']
adj=[set(map(int,line.split())) for line in (out.parent/'source585.implicit_adj.txt').read_text().splitlines() if line.strip()]
P=set(data['ports']);fixed=0
S={r['vertex']:set(r['ports']) for r in data['nonport_blocks']}
port_pairs=[(p,sigma[p]) for p in sorted(P) if p<sigma[p]]
pair_index={p:i for i,pair in enumerate(port_pairs) for p in pair}
records=[]
for v in sorted(S):
    w=sigma[v]
    if v<w and w in adj[v]:
        union=S[v]|S[w]
        invariant={sigma[p] for p in union}==union
        mask=0
        if fixed not in union:
            for p in union:mask|=1<<pair_index[p]
        records.append({'edge':[v,w],'intersection_ports':sorted(S[v]&S[w]),
                        'intersection_size':len(S[v]&S[w]),'union_ports':sorted(union),
                        'union_size':len(union),'contains_fixed_port':fixed in union,
                        'endpoint_outside_fixed_port_R2':[fixed not in S[v],fixed not in S[w]],
                        'sigma_invariant':invariant,'port_pair_mask':mask,
                        'port_pair_count':mask.bit_count()})
print('SIGMA_OLD_CORE_EDGES',len(records),flush=True)
signature_ok=all(r['union_size']==16 and r['intersection_size']==2 and not r['contains_fixed_port']
                 and all(r['endpoint_outside_fixed_port_R2']) and r['sigma_invariant'] and r['port_pair_count']==8
                 for r in records)
usable=[i for i,r in enumerate(records) if r['union_size']==16 and not r['contains_fixed_port'] and r['sigma_invariant']]
by_bit=[[] for _ in range(32)]
for i in usable:
    mask=records[i]['port_pair_mask']
    for b in range(32):
        if mask>>b&1:by_bit[b].append(i)
nodes=0
def search(remaining,chosen):
    global nodes
    nodes+=1
    if not remaining:return chosen if len(chosen)==4 else None
    if len(chosen)>=4:return None
    options=None
    for b in range(32):
        if remaining>>b&1:
            candidates=[i for i in by_bit[b] if records[i]['port_pair_mask']&remaining==records[i]['port_pair_mask']]
            if not candidates:return None
            if options is None or len(candidates)<len(options):options=candidates
    for i in options:
        result=search(remaining^records[i]['port_pair_mask'],chosen+[i])
        if result is not None:return result
    return None

solution=search((1<<32)-1,[])
selected=[records[i] for i in solution] if solution is not None else []
anchors=[v for r in selected for v in r['edge']]
cross_edges=[]
for i,a in enumerate(selected):
    for b in selected[i+1:]:
        cross_edges.extend([[v,w] for v in a['edge'] for w in b['edge'] if w in adj[v]])
result={'status':'FOUR_EDGE_SPREAD_FOUND' if solution is not None else 'COMPLETE_NO_FOUR_EDGE_SPREAD',
        'prediction_disposition':'SUPPORTED' if solution is not None else 'REFUTED',
        'source_n':585,'source_m':2600,'fixed_port':fixed,
        'sigma_old_core_edge_count':len(records),
        'all_edges_match_predicted_signature':signature_ok,
        'union_size_histogram':dict(Counter(r['union_size'] for r in records)),
        'intersection_size_histogram':dict(Counter(r['intersection_size'] for r in records)),
        'port_pair_universe':port_pairs,'selected_record_indices':solution,
        'selected_edges':[r['edge'] for r in selected],'anchors':anchors,
        'anchor_vertices_distinct':len(set(anchors))==8 if selected else None,
        'cross_edges_between_selected_edges':cross_edges,
        'selected_port_unions':[r['union_ports'] for r in selected],
        'selected_unions_exactly_partition_nonfixed_ports':len(set(p for r in selected for p in r['union_ports']))==64 if selected else False,
        'exactcover_search_nodes':nodes,
        'CPU_seconds':time.process_time()-start,
        'source_BFS':0,'new_aut_search':False,'graph_candidates_generated':0,'running':False,'pending':[]}
(out/'SIGMA_EDGES.json').write_text(json.dumps(records,indent=2)+'\n')
(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(out/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
