import resource
resource.setrlimit(resource.RLIMIT_CPU,(5,5))
from pathlib import Path
import json,time
from collections import Counter
OUT=Path(__file__).resolve().parent;P=OUT.parent;START=time.process_time()
def save(n,x):(OUT/n).write_text(json.dumps(x,indent=2)+'\n')
sel=json.loads((P/'MATCHING_SELECTORS.json').read_text());atoms={a['variable']:a for a in sel['selectors']};inc=sel['orbit_incident_variables'];girth=json.loads((P/'GIRTH_CONSTRAINTS.json').read_text());forbidden={x['variable'] for x in girth['self_conflicts']};conflict={v:set() for v in atoms}
for rec in girth['pair_conflicts']:
 a,b=rec['variables'];conflict[a].add(b);conflict[b].add(a)
nodes=0;trials=0;limited=False;solution=None

def dfs(used,chosen,cross):
 global nodes,trials,limited,solution
 nodes+=1
 if nodes%32==0 and time.process_time()-START>=4.5:limited=True;return False
 if used==(1<<18)-1:
  if cross in [1,3,5,7]:solution=list(chosen);return True
  return False
 r=next(i for i in range(18) if not(used>>i&1))
 for v in inc[r]:
  trials+=1
  if v in forbidden or any(c in conflict[v] for c in chosen):continue
  a,b=atoms[v]['orbit_pair']
  if used>>a&1 or used>>b&1:continue
  c=cross+int(a%2!=b%2)
  if c>7:continue
  if dfs(used|(1<<a)|(1<<b),chosen+[v],c):return True
  if limited:return False
 return False
found=dfs(0,[],0)
save('DFS_RECEIPT.json',{'found':found,'nodes':nodes,'selector_trials':trials,'limited':limited,'CPU_seconds':time.process_time()-START,'selection':'lexlowestunmatchedorbit/ascendingselector, noD4coverageinselection'})
if not found:
 r={'status':'CONTROL_UNKNOWN_NO_LEGAL_OBJECT_WITHIN_BUDGET' if limited else 'CONTROL_NO_MIXED_DEGREE_GIRTH_OBJECT_IN_DFS_SCOPE','found':False,'solver_calls':0,'graphs_generated':0,'BFS':0,'CPU_seconds':time.process_time()-START};save('WORKER_RESULT.json',r);print(json.dumps(r));raise SystemExit(0)
source=json.loads((P/'INPUT.json').read_text());old={tuple(e) for e in source['source_edges']};new={tuple(e) for v in solution for e in atoms[v]['actual_edges']};assert len(solution)==9 and len(new)==63 and not old&new and len({u for e in new for u in e})==126
assert all(v not in forbidden for v in solution) and all(b not in conflict[a] for i,a in enumerate(solution) for b in solution[i+1:])
edges=old|new;assert len(edges)==252;adj=[[] for _ in range(126)]
for u,v in edges:adj[u].append(v);adj[v].append(u)
for a in adj:a.sort()
assert all(len(a)==len(set(a))==4 for a in adj)
# One fresh controlgraphgirthcheck, not a diameter traversal.
def shortcycle(root,u,path):
 for v in adj[u]:
  if v==root and len(path)>=3:return path+[root]
  if len(path)<5 and v>root and v not in path:
   w=shortcycle(root,v,path+[v])
   if w:return w
 return None
assert all(shortcycle(root,root,[root]) is None for root in range(126))
(OUT/'control126.edges').write_text('126 252\n'+''.join(f'{u} {v}\n' for u,v in sorted(edges)))
D=(P/'old_distance_to4.u8.bin').read_bytes();far={v for v in range(126) if D[v]==255};assert len(far)==80
byM=[set(),set(),set()];firstpaths=[{}, {}, {}];B2=set();prefixes=0;depths=[0]*5;stack=[(0,-1,0,0,(0,),())]
while stack:
 u,prev,depth,nM,path,kinds=stack.pop();prefixes+=1;depths[depth]+=1;assert nM<=2
 byM[nM].add(u);firstpaths[nM].setdefault(u,{'vertices':path,'edge_kinds':kinds})
 if depth<=2:B2.add(u)
 if depth==4:continue
 for v in adj[u]:
  if v!=prev:
   ism=int(tuple(sorted((u,v))) in new);stack.append((v,u,depth+1,nM+ism,path+(v,),kinds+('M' if ism else 'G',)))
assert prefixes==161 and depths==[1,4,12,36,108]
farsets=[s&far for s in byM];onlytwo=farsets[2]-(farsets[0]|farsets[1]);witness=None
if onlytwo:
 target=min(onlytwo);witness={'target':target,**firstpaths[2][target],'new_matching_edges_in_path':2,'notreachable_with0or1Mwithin4':True}
cross=sum(atoms[v]['orbit_pair'][0]%2!=atoms[v]['orbit_pair'][1]%2 for v in solution)
params={'selected_variables':solution,'selected_atoms':[atoms[v] for v in solution],'crossorbitpairs':cross,'withinorbitpairs':9-cross,'n':126,'m':252,'degree':4,'girth_atleast6_checked':True,'scope':'Onefirstdegree/girthlegalmixedobject;notselectedbycoverageandnotarecordclaim'}
save('CONTROL_PARAMETERS.json',params)
r={'status':'COMPLETE_ONE_LEGAL_MIXED_MATCHING_CONTROL','found':True,'n':126,'m':252,'degree':4,'actual_global_D':None,'ordinary_bad_unordered_pairs':None,'selected_variables':solution,'cross_orbit_pair_count':cross,'girth_atleast6_checked':True,'root':0,'root0_closedB2':sorted(B2),'B2_size':len(B2),'B2_prediction':'SUPPORTED' if len(B2)==17 else 'REFUTED','route_enumeration':'allnonbacktrackingprefixes0..4, withoriginalG/newMedgeclassification','prefix_count':prefixes,'depth_prefix_counts':depths,'oldfar_targets':sorted(far),'oldfar_covered_by_exact0M':sorted(farsets[0]),'oldfar_covered_by_exact1M':sorted(farsets[1]),'oldfar_covered_by_exact2M':sorted(farsets[2]),'only_twoM_targets':sorted(onlytwo),'exclusive_twoM_prediction':'SUPPORTED' if onlytwo else 'REFUTED','one_onlytwoM_path':witness,'root0_R4_covered':len(set.union(*byM)),'root0_R4_missing':126-len(set.union(*byM)),'count_type':'root0endpointsets,notordinaryunorderedbadpairs','DFS_nodes':nodes,'DFS_selector_trials':trials,'CPU_seconds':time.process_time()-START,'solver_calls':0,'graphs_generated':1,'graph_BFS':0,'other17_rootchecks':0,'new_lower_bounds':0}
save('WORKER_RESULT.json',r);print(json.dumps(r))
