"""Small graph coverage for choosing useful locks, never hypergraph enumeration."""
from pathlib import Path
from itertools import combinations,permutations
import json,time
HERE=Path(__file__).resolve().parent;start=time.perf_counter()
source=json.loads((HERE/'ALL_FIVE_GRAPH_RESULTS.json').read_text())
assert source['all_graphs_complete']
p5=list(combinations(range(5),2));p6=list(combinations(range(6),2))
def move(g,p,pairs):
 index={ij:i for i,ij in enumerate(pairs)}
 return sum(1<<index[tuple(sorted((p[a],p[b])))] for k,(a,b) in enumerate(pairs) if g&(1<<k))
good=set()
for r in source['results']:
 if r['all_pass']:good.update(move(r['graph'],p,p5) for p in permutations(range(5)))
maps=[]
for omit in range(6):
 vertices=[i for i in range(6) if i!=omit]
 maps.append([p6.index((vertices[a],vertices[b])) for a,b in p5])
uncovered=[];ncovered=0
for g in range(1<<15):
 if any(sum(((g>>old)&1)<<j for j,old in enumerate(mp)) in good for mp in maps):ncovered+=1
 else:uncovered.append(g)
seen=set();groups=[]
for g in uncovered:
 if g in seen:continue
 orbit={move(g,p,p6) for p in permutations(range(6))};seen.update(orbit)
 groups.append(dict(graph=g,pairs=[p6[i] for i in range(15) if g&(1<<i)],labelled=len(orbit)))
out=dict(scope=__doc__,good_five_labelled=len(good),covered_six_labelled=ncovered,uncovered_six_labelled=len(uncovered),residual_groups=groups,elapsed_seconds=time.perf_counter()-start)
(HERE/'SIX_GRAPH_COVER.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
