"""Only port R2 and incidence triples; no source all-pairs BFS."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import resource
import time

start=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(3,3))
out=Path(__file__).resolve().parent
source=out.parents[1]/'polarity585_replication'
partition=json.loads((source/'SOURCE_PARTITION_CHECK.json').read_text())
adj=[set(map(int,line.split())) for line in (out/'source585.implicit_adj.txt').read_text().splitlines() if line.strip()]
P=partition['low_degree_vertices']
pset=set(P)
B=sorted(set(range(585))-pset)
r2={p:{p}|adj[p]|set().union(*(adj[v] for v in adj[p])) for p in P}
port_separation=all(r2[p]&pset=={p} for p in P)
closed1_counts=Counter(v for p in P for v in ({p}|adj[p]))
blocks=[{'vertex':t,'ports':[p for p in P if t in r2[p]]} for t in B]
triple_counts=Counter(triple for row in blocks for triple in combinations(row['ports'],3))
universe=set(combinations(P,3))
first_bad=next(({'ports':list(t),'count':triple_counts[t]} for t in sorted(universe) if triple_counts[t]!=1),None)
size_hist=Counter(len(row['ports']) for row in blocks)
perfect=len(closed1_counts)==585 and set(closed1_counts.values())=={1}
steiner=size_hist==Counter({9:520}) and first_bad is None
result={'status':'COMPLETE_PORT_R2_TRIPLE_COUNT',
        'inherited_n':585,'inherited_m':2600,'inherited_degree_histogram':partition['degree_histogram'],
        'ports_count':len(P),'nonports_count':len(B),
        'ports_pairwise_not_within2':port_separation,
        'ports_pairwise_distance3':'SUPPORTED using freshR2 separation plus inherited sourceD3' if port_separation else 'REFUTED',
        'perfect1code':perfect,
        'closed1_cover_multiplicity_histogram':dict(Counter(closed1_counts.values())),
        'S_size_histogram':dict(size_hist),
        'distinct_blocks':len({tuple(row['ports']) for row in blocks}),
        'triple_universe_size':len(universe),
        'triple_multiplicity_histogram':dict(Counter(triple_counts[t] for t in universe)),
        'first_bad_triple':first_bad,
        'Steiner_3_65_9_1':steiner,
        'prediction_disposition':'SUPPORTED' if port_separation and perfect and steiner else 'REFUTED',
        'CPU_seconds':time.process_time()-start,'source_full_BFS':0,
        'new_graphs':0,'helpers_searched':False,'running':False,'pending':[]}
(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(out/'BLOCKS.json').write_text(json.dumps({'ports':P,'nonport_blocks':blocks},indent=2)+'\n')
(out/'PORT_R2.json').write_text(json.dumps([{'port':p,'R2':sorted(r2[p])} for p in P],indent=2)+'\n')
(out/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
