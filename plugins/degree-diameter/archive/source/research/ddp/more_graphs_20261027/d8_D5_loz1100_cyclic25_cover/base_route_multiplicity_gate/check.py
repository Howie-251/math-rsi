from pathlib import Path
import collections,json,resource,time
resource.setrlimit(resource.RLIMIT_CPU,(3,3))
p=Path(__file__).resolve().parent
p.joinpath('PREDICTION.json').write_text(json.dumps({'prediction':'Some sourceLoz1100 target has fewer than5 reduced walks of length<=5; if true this explains and uniformly excludes every ordinary5fold D5 cover, not just the125 tested metacyclic lifts.','frozen_before_this_new_source_route_multiplicity_DP':True,'inherited_data':'All125 targetlift cases failed D5 but retained sourceR4 projection and internalfibre coverage. No sourceR5 route-multiplicity table was used to set this prediction.','source_BFS':0,'modified_graphs':0},indent=2)+'\n')
t0=time.process_time();positive=[(1,0),(12,33),(11,1),(16,19)]
g=positive+[((-j)%20,(-n*pow(2,(-j)%20,55))%55) for j,n in positive]
inv=[4,5,6,7,0,1,2,3];factors=[pow(2,j,55) for j,n in g]
for k,(j,n) in enumerate(g):
 h,m=g[inv[k]]
 assert (j+h)%20==0 and (n*pow(2,h,55)+m)%55==0
counts=[0]*1100;counts[0]=1;depth=[1];layer={(0,-1):1}
for length in range(1,6):
 nxt=collections.defaultdict(int)
 for (state,last),multiplicity in layer.items():
  j,n=divmod(state,55)
  for k,(h,m) in enumerate(g):
   if last>=0 and k==inv[last]:continue
   s=((j+h)%20)*55+(n*factors[k]+m)%55
   nxt[s,k]+=multiplicity;counts[s]+=multiplicity
 depth.append(sum(nxt.values()));layer=nxt
assert sum(depth)==22409 and sum(counts)==22409
minimum=min(counts);witnesses=[{'vertex':i,'phase':i//55,'normal55':i%55,'walks':c} for i,c in enumerate(counts) if c==minimum]
result={'status':'COMPLETE_SOURCE_WALK_COUNT_DIAGNOSTIC','prediction':'SUPPORTED' if minimum<5 else 'REFUTED','source_n':1100,'maximum_word_length':5,'minimum_reduced_walk_count':minimum,'minimum_targets':witnesses,'raw_count_histogram':dict(sorted(collections.Counter(counts).items())),'counts_phase_slow':counts,'depth_counts':depth,'prefixes':sum(depth),'ordinary_cover_sheets_uniformly_forbidden_by_this_count':f'>{minimum}' if minimum<5 else None,'source_BFS':0,'source_graphs_generated':0,'new_full_graphs':0,'CPU_seconds':time.process_time()-t0}
p.joinpath('RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['counts_phase_slow','minimum_targets']}))
print('first_minimum',witnesses[:3])
