from pathlib import Path
from collections import Counter,defaultdict
import json,itertools,time
P=Path(__file__).parent;start=time.process_time()
I=(1,0,0,1);a=(0,1,2,2);b=(0,1,2,1)
def inv(X):aa,bb,cc,dd=X;return (dd,-bb%3,-cc%3,aa)
def mul(X,Y):return tuple(sum(X[2*i+k]*Y[2*k+j] for k in range(2))%3 for i in range(2) for j in range(2))
xs=[a,inv(a),b,inv(b)];names=['a','A','b','B'];per=defaultdict(lambda:[[] for _ in range(5)]);total=0
for length in range(5):
 for w in itertools.product(range(4),repeat=length):
  X=I
  for i in w:X=mul(X,xs[i])
  per[X][length].append(''.join(names[i] for i in w));total+=1
assert total==341 and len(per)==24
rows=[];witnesses=[]
for X,levels in sorted(per.items()):
 distance=next(i for i,v in enumerate(levels) if v)
 row={'SL2_matrix':list(X),'distance_from_identity':distance,'wide_word_counts_by_length':[len(v) for v in levels]}
 rows.append(row)
 if distance==4 and len(levels[4])<9:witnesses.append(dict(row,complete_length4_words=levels[4]))
r={'status':'FIXED_SL2_PROJECTION_CAPACITY_EXCLUDES_M9' if witnesses else 'NO_REQUESTED_SMALL_CAPACITY_OBSTRUCTION_FOUND','wide_words':total,'SL2_elements':24,'distance_histogram':dict(Counter(x['distance_from_identity'] for x in rows)),'rows':rows,'witnesses':witnesses,'prediction':'SUPPORTED' if witnesses else 'REFUTED','minimum_distance4_word_count':min((x['wide_word_counts_by_length'][4] for x in rows if x['distance_from_identity']==4),default=None),'scope':'Any graph retaining these fixed SL2 wide projections and only identity-SL2 plain shortcuts. A distance4 target permits exactly4 wide steps and no plain step; K words yield at mostK cyclic endpoints for any phases. No claim about altered SL2 wide parts, noncentral/nonidentity-SL2 shortcuts, or arbitrary degree16D4 graphs.','new_graphs':0,'BFS':0,'phase_frame_evaluations':0,'CPU_seconds':time.process_time()-start}
(P/'ANALYSIS_SL2_CAPACITY.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({k:v for k,v in r.items() if k!='rows'}))
