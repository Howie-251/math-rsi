"""Exact all-pairs adjacent two-line blocks on unchanged verified37631."""
import json
import resource
import time
from itertools import combinations
from pathlib import Path

OUT=Path(__file__).resolve().parent
BASE=OUT.parent
START=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(10,10))
plan=json.loads((OUT/'PREDICTION.json').read_text());assert plan['frozen_before_pair_checks']
load=lambda p:json.loads(p.read_text())
pool=load(BASE/'h9_d11_followups/frozen_pool_order.json')['records']
items=[r for r in pool if r['pool_index'] in plan['unused_canonical_indices']]
assert len(items)==21
source=BASE/'h9_d11_followups/graph_d11_D5_n37631.edges'
with source.open() as stream:
 n,m=map(int,stream.readline().split());adj=[[] for _ in range(n)]
 for line in stream:
  u,v=map(int,line.split());adj[u].append(v);adj[v].append(u)
assert (n,m)==(37631,205329)
old=load(BASE/'h9_d11_changed_base_retries/RESULT.json')
assert old['initial_n']==old['final_n']==37631 and old['accepted_count']==0
cached_missing={r['pool_index']:r['mandatory_missing_targets'] for r in old['rows']}
R3={};R4missing={};newR3=0;newR4=0
def balls(pins,radius):
 d=bytearray([255])*n;q=list(pins)
 for s in pins:d[s]=0
 for u in q:
  depth=d[u]+1
  if depth>radius:break
  for v in adj[u]:
   if d[v]==255:d[v]=depth;q.append(v)
 return d
for item in items:
 i=item['pool_index'];pins=item['pins'];assert len(pins)==10
 R3[i]=bytes(balls(pins,3));newR3+=1
 if i in cached_missing:R4missing[i]=cached_missing[i]
 else:
  d=balls(pins,4);newR4+=1;R4missing[i]=[v for v in range(n) if d[v]==255]

rows=[];success=None
for ia,ib in combinations(items,2):
 a,b=ia['pool_index'],ib['pool_index'];A,B=set(ia['pins']),set(ib['pins'])
 bad=[v for v in A|B if len(adj[v])+(v in A)+(v in B)>11]
 row=dict(A_index=a,B_index=b,shared_pins=sorted(A&B))
 if bad:row.update(status='DEGREE_INFEASIBLE',overloaded_old_pins=sorted(bad));rows.append(row);continue
 # All other targets are already covered by the corresponding completeR4 cache.
 miss_z=[t for t in R4missing[a] if R3[b][t]>3]
 miss_w=[t for t in R4missing[b] if R3[a][t]>3]
 row.update(z_uncovered_targets=miss_z,w_uncovered_targets=miss_w,
            z_uncovered_count=len(miss_z),w_uncovered_count=len(miss_w))
 if miss_z or miss_w:row['status']='EXACT_COVERAGE_FAIL';rows.append(row);continue
 row['status']='ACCEPTED_COMPLETE_TWO_POINT_BLOCK';rows.append(row)
 success=dict(source_n=n,source_m=m,new_vertices=[n,n+1],target_n=n+2,target_m=m+21,
              A_index=a,B_index=b,z_old_pins=sorted(A),w_old_pins=sorted(B),
              interedge=[n,n+1],new_vertex_degrees=[11,11],
              old_pin_loads=[dict(vertex=v,old_degree=len(adj[v]),added_degree=(v in A)+(v in B),
                                  new_degree=len(adj[v])+(v in A)+(v in B)) for v in sorted(A|B)],
              z_R4A_union_R3B_covered=n,w_R3A_union_R4B_covered=n,
              z_coverage_missing=[],w_coverage_missing=[],newnew_distance=1,
              oldold_edges_retained=True,intermediate37632_claimed=False,
              geometries=[ia['geometric_witnesses'],ib['geometric_witnesses']])
 (OUT/'first_complete_block.json').write_text(json.dumps(success,indent=2)+'\n')
 print('HIT '+json.dumps(success),flush=True);break

result=dict(status='COMPLETE_TWO_POINT_BLOCK_FOUND' if success else 'ALL210_ADJACENT_TWO_LINE_BLOCKS_EXCLUDED',
            source_n=n,source_m=m,pair_scope=210,pairs_tested=len(rows),pairs_unattempted=210-len(rows),
            degree_infeasible_pairs=sum(r['status']=='DEGREE_INFEASIBLE' for r in rows),
            exact_coverage_failed_pairs=sum(r['status']=='EXACT_COVERAGE_FAIL' for r in rows),
            complete_blocks=1 if success else 0,rows=rows,
            cached_current37631_R4_rows_reused=len(cached_missing),new_R3_checks=newR3,new_R4_checks=newR4,
            old_graph_reverification=0,allsource_BFS=0,solvers=0,newreview=0,
            extraanchors=0,thirdpoint=0,pending=[],CPU_seconds=time.process_time()-START)
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'line_R3_rows.u8.bin').write_bytes(b''.join(R3[r['pool_index']] for r in items))
(OUT/'cache_metadata.json').write_text(json.dumps(dict(source_n=n,source_m=m,
    pool_indices=[r['pool_index'] for r in items],R3_row_bytes=n,R4_missing_targets=R4missing),indent=2)+'\n')
print('TERMINAL '+json.dumps({k:v for k,v in result.items() if k!='rows'}),flush=True)
