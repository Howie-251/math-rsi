"""Two accepted final sources: one complete free-neighborhood scan, no distances."""
import collections,json,pathlib,pickle,resource,time
from datetime import datetime,timezone
P=pathlib.Path(__file__).resolve().parent;ROOT=pathlib.Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');BASE=P.parent
START=time.process_time();WALL=time.monotonic();resource.setrlimit(resource.RLIMIT_CPU,(10,10))
pred=json.loads((P/'PREDICTION.json').read_text());assert len(pred['targets'])==2 and not (P/'SCAN_RESULT.json').exists()
profiles=[]
for target in pred['targets']:
 delta=target['Delta'];source=BASE/target['source'];perstart=time.process_time()
 with source.open() as stream:
  n,m=map(int,next(stream).split());assert(n,m)==(target['source_n'],target['source_m'])
  adj=[set() for _ in range(n)];edge_count=0
  for line in stream:
   if line.strip():
    a,b=map(int,line.split());assert a!=b and b not in adj[a]
    adj[a].add(b);adj[b].add(a);edge_count+=1
 assert edge_count==m
 degree=[len(ns) for ns in adj];assert max(degree)<=delta and min(degree)>0
 satcount=[sum(degree[x]>=delta for x in adj[v]) for v in range(n)]
 eligible=[v for v in range(n) if not satcount[v] and degree[v]<=delta]
 hist=dict(sorted(collections.Counter(satcount).items()));dhist=dict(sorted(collections.Counter(degree).items()))
 out={'Delta':delta,'D':5,'source_n':n,'source_m':m,'source_file':str(source.relative_to(ROOT)),'source_D5':'inherited accepted source; not rechecked','degree_histogram':dhist,'free_vertices':sum(d<delta for d in degree),'spare_degree_slots':sum(delta-d for d in degree),'minimum_saturated_neighbors':min(satcount),'saturated_neighbor_count_histogram':hist,'eligible_count':len(eligible),'eligible_prototypes':eligible,'eligible_literal_neighborhoods':[{'prototype':v,'neighbors':sorted(adj[v]),'neighbor_current_degrees':[degree[x] for x in sorted(adj[v])]} for v in eligible],'first_minimum_witness':{'prototype':satcount.index(min(satcount)),'neighbors':sorted(adj[satcount.index(min(satcount))]),'saturated_neighbors':sorted(x for x in adj[satcount.index(min(satcount))] if degree[x]>=delta)},'CPU_seconds':time.process_time()-perstart,'BFS':0,'R4_checks':0,'solver_calls':0,'graph_appends':0}
 (P/f'PROFILE_D{delta}.json').write_text(json.dumps(out,indent=2)+'\n');(P/f'saturated_neighbor_counts_d{delta}.u8.bin').write_bytes(bytes(satcount));(P/f'source_degrees_d{delta}.u8.bin').write_bytes(bytes(degree))
 if eligible:
  with (P/f'source_d{delta}.pkl').open('wb') as cache:pickle.dump({'adj':adj,'source':str(source),'n':n,'m':m,'delta':delta,'frozen_prototypes':eligible},cache,protocol=4)
 profiles.append(out)
 print(json.dumps({k:out[k] for k in ['Delta','source_n','source_m','minimum_saturated_neighbors','saturated_neighbor_count_histogram','eligible_count','free_vertices','CPU_seconds']}),flush=True)
r={'status':'COMPLETE_TWO_SOURCE_FULL_NEIGHBORHOOD_SCAN','timestamp_UTC':datetime.now(timezone.utc).isoformat(),'profiles':profiles,'eligible_sources':sum(p['eligible_count']>0 for p in profiles),'eligible_prototypes_total':sum(p['eligible_count'] for p in profiles),'CPU_seconds':time.process_time()-START,'wall_seconds':time.monotonic()-WALL,'source_BFS':0,'R4_checks':0,'solver_calls':0,'D13_rescan':0,'graph_appends':0}
(P/'SCAN_RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:r[k] for k in ['status','eligible_sources','eligible_prototypes_total','CPU_seconds','wall_seconds']}),flush=True)
