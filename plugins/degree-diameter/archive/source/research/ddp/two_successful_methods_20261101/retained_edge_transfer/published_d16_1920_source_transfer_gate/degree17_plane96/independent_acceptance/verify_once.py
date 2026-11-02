"""Fresh literal/source-recipe acceptance; only96newroot ordinary BFS."""
import time
import json, resource, os, csv
from pathlib import Path
from collections import Counter, deque
resource.setrlimit(resource.RLIMIT_CPU,(29,30))
D=Path(__file__).resolve().parent
assert not (D/'TERMINAL.json').exists(), 'One-shot acceptance already terminal; no restart.'
G=D.parent
ROOT=next(p for p in D.parents if (p/'formal/DegreeDiameter/Portfolio').is_dir())
SRC=ROOT/'research/ddp/breadth_20261027_wave4/mizuno_d3_source/construction.json'
phase='input_recipe'
def cpu(): return time.process_time()
def save(name,obj): (D/name).write_text(json.dumps(obj,indent=2)+'\n')
def need(ok,why):
 if not ok: raise AssertionError(why)
def mul(x,y):
 a=x&1;b=x>>1;c=y&1;d=y>>1
 return ((a*c)^(b*d)) | (((a*d)^(b*c)^(b*d))<<1)
def act(M,x):
 return tuple(mul(r[0],x[0])^mul(r[1],x[1])^mul(r[2],x[2]) for r in M)
def read_literal(path,n,m):
 edges=[];adj=[set() for _ in range(n)];previous=(-1,-1)
 with path.open() as f:
  need(tuple(map(int,f.readline().split()))==(n,m),'literal header')
  for line in f:
   a,b=map(int,line.split())
   need(0<=a<b<n and previous<(a,b),'strictlex simple literal body')
   edges.append((a,b));adj[a].add(b);adj[b].add(a);previous=(a,b)
 need(len(edges)==m,'complete literal body count')
 return edges,adj
save('HANDLE.json',dict(status='RUNNING',pid=os.getpid(),phase=phase,CPU_budget_seconds=30,single_worker=True))
try:
 recipe=json.loads(SRC.read_text());C=recipe['controller'];L=recipe['outgoing_return_directions'];M=recipe['matrices'];rev=[1,0,3,2]
 need(recipe['q']==4 and recipe['dimension']==3 and len(C)==30,'actual source recipe identity')
 need(L==[[1,0,0],[0,1,0],[0,0,1],[1,1,1]],'actual four directions binding')
 phase='independent_formula_to_single_parent_stream'
 expected=set()
 for u in range(30):
  for i in range(64):
   x=(i%4,(i//4)%4,i//16);a=64*u+i
   for p in range(4):
    y=act(M[u][p],x);ell=L[rev[p]]
    for t in range(4):
     z=tuple(y[k]^mul(t,ell[k]) for k in range(3))
     b=64*C[u][p]+z[0]+4*z[1]+16*z[2]
     need(a!=b,'source recipe contains no loops')
     expected.add((min(a,b),max(a,b)))
 source_edges,S=read_literal(G/'source_d16_D3_n1920.edges',1920,15360)
 need(source_edges==sorted(expected),'every literal source edge exactly bound to independentGF4 actualauthor relation')
 need(all(len(n)==16 for n in S),'literal bound parent16regular')
 source_binding_CPU=cpu()
 I=[0,3,5,7,9,16]
 centers=[64*u+a+4*b+16*(a^b) for u in I for a in range(4) for b in range(4)]
 need(len(set(centers))==96,'ordered96distinct centers')
 Ns=[S[c] for c in centers]
 load=Counter(v for ns in Ns for v in ns)
 need(len(load)==1536 and set(load.values())=={1},'complete actualparent N96 pairwise disjoint/1536pins/load1')
 phase='single_candidate_literal_stream_and_complete_binding'
 edges,A=read_literal(G/'graph_d17_D3_n2016.edges',2016,16896)
 old=[e for e in edges if e[1]<1920];new=[e for e in edges if e[1]>=1920]
 need(old==source_edges,'all15360oldbody retained exact')
 need(len(new)==1536 and all(a<1920 for a,b in new),'1536newold and0newnew')
 for j,ns in enumerate(Ns): need(A[1920+j]==ns,'actual newrole has complete immutable source N16')
 need(all(len(A[v])==16+load[v] for v in range(1920)),'complete old degree andload binding')
 hist=Counter(map(len,A));need(hist=={16:480,17:1536},'complete actualdegree histogram')
 with (D/'ACTUAL_LITERAL_ROLE_BINDINGS.tsv').open('w',newline='') as f:
  w=csv.writer(f,delimiter='\t');w.writerow(['j','controller','a','b','source_center_label','new_label','literal_N_size','actual_N_equal','actual_parent_neighbors'])
  for j,c in enumerate(centers):
   w.writerow([j,I[j//16],(j%16)//4,j%4,c,1920+j,len(Ns[j]),True,' '.join(map(str,sorted(Ns[j])))])
 binding_CPU=cpu()-source_binding_CPU
 phase='only96newroot_BFS'
 save('HANDLE.json',dict(status='RUNNING',pid=os.getpid(),phase=phase,CPU_budget_seconds=30,single_worker=True,source_parses=1,candidate_parses=1))
 begun=cpu();rows=[];distribution=Counter();witness=None;failures=[]
 for j,center in enumerate(centers):
  need(cpu()<29,'single total CPU budget')
  root=1920+j;dist=[-1]*2016;prev=[-1]*2016;dist[root]=0;q=deque([root]);dh=[1,0,0,0]
  while q:
   v=q.popleft()
   if dist[v]==3:continue
   for z in sorted(A[v]):
    if dist[z]<0:
     dist[z]=dist[v]+1;prev[z]=v;dh[dist[z]]+=1;q.append(z)
  reached=sum(d>=0 for d in dist);new3=sum(dist[z]==3 for z in range(1920,2016) if z!=root)
  matched=(reached==2016 and dh[1]==16 and dist[center]==2 and new3==95)
  if not matched:failures.append(dict(root=root,reached=reached,old_center_distance=dist[center],othernew_distance3=new3))
  distribution[tuple(dh)]+=1
  rows.append([root,j,center,2016,reached,16,dh[1],2,dist[center],95,new3,*dh,matched])
  if j==0:
   target=1921;path=[];v=target
   while v>=0:path.append(v);v=prev[v]
   path.reverse();need(dist[target]==3 and len(path)==4,'firstnewroot actual nonD2 witness')
   witness=dict(root=root,target=target,distance=3,genuine_walk=path,within_authorized96newroots=True,oldroot_BFS=0)
 bfs_CPU=cpu()-begun
 with (D/'ALL_96_NEW_ROOT_BFS.csv').open('w',newline='') as f:
  w=csv.writer(f);w.writerow(['root','j','old_center','pred_reached','actual_reached','pred_R1','actual_R1','pred_oldcenter_distance','actual_oldcenter_distance','pred_othernew_R3','actual_othernew_R3','R0','R1','R2','R3','all_predictions_match']);w.writerows(rows)
 need(not failures,'perroot structural prediction failure')
 save('NON_D2_ACTUAL_NEW_ROOT_WITNESS.json',witness)
 result=dict(status='PASS_COMPLETE_LITERAL_D17_N2016_EXACT_D3',Delta=17,D=3,n=2016,m=16896,source_n=1920,source_m=15360,
  source_literal_parse_count=1,candidate_literal_parse_count=1,source_full_body_bound_to_independent_actual_author_formula=True,
  source_field='GF4 using explicit coefficient multiplication andXOR, not integer mod4',source_old_field_inverse_rank_pencil_checks_repeated=False,
  source_D3='inherited prior complete source and route certificate; no sourceBFS',old_edges_retained_exact=15360,new_edges=1536,new_new_edges=0,simple=True,header_body_match=True,
  ordered_controller_layers=I,new_roles_bound=96,role_binding_file='ACTUAL_LITERAL_ROLE_BINDINGS.tsv',immutable_source_fullN_size=16,
  distinct_old_pins=1536,old_maximum_load=1,degree_histogram=dict(hist),allpair_and_everyprefix_old_source_interior_proof=True,
  actual_newroot_BFS_count=96,unmeasured_newroot_count=0,oldroot_BFS_count=0,all_actual2016_reached_per_root=True,
  all95othernew_vertices_distance3_per_root=True,all_own_old_centers_distance2=True,prediction_mismatch_count=0,
  actual_distance_hist_distributions=[dict(hist=list(h),roots=c) for h,c in sorted(distribution.items())],
  nonD2_witness='NON_D2_ACTUAL_NEW_ROOT_WITNESS.json',exact_diameter=3,source_formula_and_parent_binding_CPU_seconds=source_binding_CPU,
  candidate_binding_CPU_seconds=binding_CPU,new96_BFS_CPU_seconds=bfs_CPU,total_process_CPU_seconds=cpu(),CPU_budget_seconds=30,single_worker=True,
  producer_neighbor_logic_or_caches_imported=False,old1920root_BFS_fieldlaw_rank_pencil_solver_Lean_paidreview_runs=0,
  global_priority='UNKNOWN',global_record_claim=False,root_counts_or_frozen_packets_modified=False,portfolio_increment_by_this_reviewer=0)
 save('RESULT.json',result)
 terminal=dict(status=result['status'],running=False,active_processes=[],CPU_seconds=cpu(),CPU_budget_seconds=30,single_worker=True,
  source_parses=1,candidate_parses=1,newroot_BFS_count=96,oldroot_BFS_count=0,all_children_terminal=True,no_automatic_continuation=True)
 save('TERMINAL.json',terminal);save('HANDLE.json',dict(status='TERMINAL',running=False,pid=os.getpid()))
 print(json.dumps(result,indent=2))
except Exception as e:
 save('TERMINAL.json',dict(status='FAIL_OR_BUDGET_UNKNOWN',phase=phase,error=str(e),CPU_seconds=cpu(),running=False,no_automatic_continuation=True))
 raise
