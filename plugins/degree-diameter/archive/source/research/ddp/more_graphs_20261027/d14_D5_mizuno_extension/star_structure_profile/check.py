from pathlib import Path
import json,resource,time,collections
resource.setrlimit(resource.RLIMIT_CPU,(5,5));p=Path(__file__).resolve().parent;b=p.parent
p.joinpath('PREDICTION.json').write_text(json.dumps({'prediction':'The actual94186 source has a prototype with at mostone saturatedneighbor, allowing the successful13D5 star-repair mechanism to be tested directly.','frozen_before_this_new_saturated_neighbor_scan':True,'inheritance':'Reuse saved actualdegrees and literaledges; no degreeprofile or BFS repeated. Existing64covers and interruptedglobalMIP do not exclude this structuralquestion.'},indent=2)+'\n')
t0=time.process_time();degree=list((b/'degree14.u8.bin').read_bytes());N=94186
assert len(degree)==N
sat=[0]*N;adj=[[] for _ in range(N)];edges=0
for line in (b/'source94186.edges').open():
 if line.startswith('#'):continue
 u,v=map(int,line.split());sat[u]+=degree[v]==14;sat[v]+=degree[u]==14;adj[u].append(v);adj[v].append(u);edges+=1
assert edges==657452
minimum=min(sat);prototypes=[{'vertex':v,'degree':degree[v],'saturated_neighbors':[u for u in adj[v] if degree[u]==14],'free_neighbors':[u for u in adj[v] if degree[u]<14]} for v in range(N) if sat[v]==minimum]
result={'status':'COMPLETE_NEW_STAR_SATURATION_SCAN','prediction':'SUPPORTED' if minimum<=1 else 'REFUTED','source_n':N,'source_m':edges,'degree_data_reused':True,'minimum_saturated_neighbors':minimum,'minimum_prototype_count':len(prototypes),'saturated_neighbor_histogram':dict(sorted(collections.Counter(sat).items())),'zero_fault_prototypes':sat.count(0),'one_fault_prototypes':sat.count(1),'minimum_prototypes':prototypes,'source_BFS':0,'degree_reprofiling':0,'new_graphs':0,'solver_calls':0,'CPU_seconds':time.process_time()-t0}
p.joinpath('RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='minimum_prototypes'}));print('first_prototype',prototypes[:1])
