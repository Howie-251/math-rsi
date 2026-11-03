from pathlib import Path
from collections import Counter
import json

P=Path(__file__).resolve().parent
PATTERNS=P.parent.parent/'breadth_20261027_wave4/mizuno_d3_source/q3_local_patterns.json'
INV=[1,0,3,2]
L=[(1,0,0),(0,1,0),(0,0,1),(1,1,1)]

def read_graph(path):
 path=Path(path)
 if path.suffix=='.json':
  d=json.loads(path.read_text());edges=d['edges'];n=d.get('n',max(max(e) for e in edges)+1)
 else:
  rows=[list(map(int,line.split())) for line in path.read_text().splitlines() if line.strip() and not line.lstrip().startswith('#')]
  if len(rows[0])==2 and len(rows)-1==rows[0][1]:n=rows[0][0];edges=rows[1:]
  else:edges=rows;n=max(max(e) for e in edges)+1
 return int(n),[tuple(map(int,e)) for e in edges]

def label_graph(n,edges):
 assert all(0<=u<n and 0<=v<n and u!=v for u,v in edges),'bad vertex or loop'
 edges=sorted(tuple(sorted(e)) for e in edges)
 assert len(set(edges))==len(edges),'parallel edge'
 adj=[[] for _ in range(n)]
 for e,(u,v) in enumerate(edges):adj[u].append((v,e));adj[v].append((u,e))
 for row in adj:row.sort()
 assert all(len(row)==4 for row in adj),'not quartic'
 used=[False]*len(edges);cursor=[0]*n;colors=[-1]*len(edges);tours=[]
 for start in range(n):
  if all(used[e] for v,e in adj[start]):continue
  stack=[start];estack=[];tour=[]
  while stack:
   u=stack[-1]
   while cursor[u]<4 and used[adj[u][cursor[u]][1]]:cursor[u]+=1
   if cursor[u]<4:
    v,e=adj[u][cursor[u]];used[e]=True;stack.append(v);estack.append(e)
   else:
    stack.pop()
    if estack:tour.append(estack.pop())
  tour.reverse();assert len(tour)%2==0
  for i,e in enumerate(tour):colors[e]=i%2
  tours.append(tour)
 ports=[[-1]*4 for _ in range(n)];factor_cycles=[]
 for color in (0,1):
  fa=[[v for v,e in row if colors[e]==color] for row in adj]
  assert all(len(row)==2 for row in fa)
  seen=set();cycles=[]
  for start in range(n):
   if start in seen:continue
   cycle=[start];prev=start;u=min(fa[start]);seen.add(start)
   while u!=start:
    assert u not in seen;seen.add(u);cycle.append(u);nxt=next(v for v in fa[u] if v!=prev);prev,u=u,nxt
   for u,v in zip(cycle,cycle[1:]+cycle[:1]):ports[u][2*color]=v;ports[v][2*color+1]=u
   cycles.append(cycle)
  factor_cycles.append(cycles)
 assert all(len(set(row))==4 for row in ports)
 assert all(ports[v][INV[p]]==u for u,row in enumerate(ports) for p,v in enumerate(row))
 return dict(n=n,edges=edges,ports=ports,euler_tours_edge_ids=tours,edge_factor_colors=colors,factor_cycles=factor_cycles)

def make_problem(n,edges,require31=True):
 G=label_graph(n,edges);C=G['ports'];neighbors=[set(row) for row in C]
 pairs=[(u,v) for u in range(n) for v in range(u,n)];pair_id={p:i for i,p in enumerate(pairs)}
 targets=[int(u==v or v not in neighbors[u]) for u,v in pairs]
 Pdata=json.loads(PATTERNS.read_text());Popt=[rec['valid_pencil_patterns'] for rec in Pdata['ports']]
 pathrows=[];k=[0]*len(pairs);edge_paths=[];edge_options=[];selected_norm=set()
 for e,(u,v) in enumerate(G['edges']):
  p=C[u].index(v);q=INV[p];ids=[]
  for i,x in enumerate(C[u]):
   if i==p:continue
   for j,y in enumerate(C[v]):
    if j==q:continue
    walk=(x,u,v,y);rev=tuple(reversed(walk));normalized=min(walk,rev) if x==y else walk if x<y else rev
    assert normalized not in selected_norm;selected_norm.add(normalized)
    row=pair_id[tuple(sorted((x,y)))];pid=len(pathrows)
    pathrows.append(dict(edge=e,turn=[i,j],endpoint_row=row,vertices=list(normalized)));ids.append(pid);k[row]+=1
  assert len(ids)==9;edge_paths.append(ids);opts=[]
  for oi,opt in enumerate(Popt[p]):
   bad=set(map(tuple,opt['bad_turns']));badids=[pid for pid in ids if tuple(pathrows[pid]['turn']) in bad];assert len(badids)==2
   counts=Counter(pathrows[pid]['endpoint_row'] for pid in badids)
   opts.append(dict(source_option=oi,bad_path_ids=badids,bad_endpoint_counts=sorted(counts.items()),matrix=opt['matrix'],inverse_matrix=opt['inverse_matrix']))
  assert len(opts)==18;edge_options.append(opts)
 assert len(pathrows)==9*len(edges)
 problem=dict(graph=G,pairs=[list(x) for x in pairs],targets=targets,raw_counts=k,paths=pathrows,edge_paths=edge_paths,edge_options=edge_options)
 missing=[pairs[i] for i in range(len(pairs)) if k[i]<targets[i]]
 if require31 and n!=31:return problem,dict(status='REJECT_ORDER_NOT31',n=n)
 if missing:return problem,dict(status='REJECT_RAW_SHORTWALK_GAP',missing_unordered_pairs=[list(x) for x in missing],missing_ordered_pairs=sum(1 if u==v else 2 for u,v in missing))
 demands=[a-b for a,b in zip(k,targets)];allowed=[]
 for e,opts in enumerate(edge_options):
  must_bad={pid for pid in edge_paths[e] if targets[pathrows[pid]['endpoint_row']]==0}
  must_good={pid for pid in edge_paths[e] if k[pathrows[pid]['endpoint_row']]==1 and targets[pathrows[pid]['endpoint_row']]==1}
  aa=[oi for oi,opt in enumerate(opts) if must_bad<=set(opt['bad_path_ids']) and not(must_good&set(opt['bad_path_ids']))]
  if not aa:return problem,dict(status='REJECT_EMPTY_EDGE_OPTIONS',edge=e,edge_vertices=list(G['edges'][e]),must_bad_path_ids=sorted(must_bad),must_good_path_ids=sorted(must_good))
  allowed.append(aa)
 if sum(demands)!=2*len(edges):return problem,dict(status='REJECT_TOTAL_BAD_DEMAND',total_demand=sum(demands),fixed_bad_paths=2*len(edges),note='Saturated exact counts are necessary specifically for n31, not a general n30 feasibility test.')
 problem.update(demands=demands,allowed_options=allowed)
 columns=[]
 for e,aa in enumerate(allowed):
  for oi in aa:columns.append(dict(edge=e,option=oi))
 problem['columns']=columns
 return problem,dict(status='READY_FOR_PATTERN_MILP',vertices=n,edges=len(edges),paired_NB3_paths=len(pathrows),endpoint_rows=len(pairs),variables=len(columns),options_after_local_elimination=[len(x) for x in allowed],total_bad_demand=sum(demands),onehot_rows=len(edges),max_endpoint_rows_per_column=max(len(edge_options[c['edge']][c['option']]['bad_endpoint_counts']) for c in columns))

def mv(T,x):return tuple(sum(a*b for a,b in zip(row,x))%3 for row in T)
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(3))%3 for j in range(3)] for i in range(3)]
def rank(cols):
 a=[list(row) for row in zip(*cols)];r=0
 for j in range(len(cols)):
  pivot=next((i for i in range(r,3) if a[i][j]),None)
  if pivot is None:continue
  a[r],a[pivot]=a[pivot],a[r];a[r]=[(x*(1 if a[r][j]==1 else 2))%3 for x in a[r]]
  for i in range(3):
   if i!=r:
    f=a[i][j];a[i]=[(x-f*y)%3 for x,y in zip(a[i],a[r])]
  r+=1
  if r==3:break
 return r
def span(cols):
 from itertools import product
 return frozenset(tuple(sum(c*v[j] for c,v in zip(co,cols))%3 for j in range(3)) for co in product(range(3),repeat=len(cols)))

def production(problem,choice,outdir):
 outdir=Path(outdir);G=problem['graph'];n=G['n'];C=G['ports'];Ts=[[None]*4 for _ in range(n)];I=[[1,0,0],[0,1,0],[0,0,1]]
 for e,oi in enumerate(choice):
  u,v=G['edges'][e];p=C[u].index(v);opt=problem['edge_options'][e][oi];Ts[u][p]=opt['matrix'];Ts[v][INV[p]]=opt['inverse_matrix']
 for u in range(n):
  for p,v in enumerate(C[u]):
   assert mm(Ts[v][INV[p]],Ts[u][p])==I and mv(Ts[u][p],L[p])==L[INV[p]]
   planes={span([mv(Ts[u][p],L[i]),L[INV[p]]]) for i in range(4) if i!=p}|{span([L[INV[p]],L[j]]) for j in range(4) if j!=INV[p]}
   assert len(planes)==4 and len(set().union(*planes))==27
 good=[[0]*n for _ in range(n)];cert={};rankhist=Counter()
 for u in range(n):
  for a in range(4):
   for b in range(4):
    if b==INV[a]:continue
    for c in range(4):
     if c==INV[b]:continue
     v=u;cols=[]
     for t in (a,b,c):cols=[mv(Ts[v][t],x) for x in cols]+[L[INV[t]]];v=C[v][t]
     rr=rank(cols);rankhist[rr]+=1
     if rr==3:good[u][v]+=1;cert.setdefault((u,v),[a,b,c])
 for u in range(n):
  for v in range(n):assert good[u][v]==(2 if u==v else 0 if v in C[u] else 1)
 records=[dict(u=u,v=v,kind='edge_pencil',word=[C[u].index(v)]) if v in C[u] else dict(u=u,v=v,kind='full_rank',word=cert[u,v]) for u in range(n) for v in range(n)]
 edges=[]
 for e,(u,v) in enumerate(G['edges']):
  p=C[u].index(v);T=Ts[u][p];ell=L[INV[p]]
  for xcode in range(27):
   x=(xcode%3,xcode//3%3,xcode//9);tx=mv(T,x)
   for lam in range(3):
    y=tuple((a+lam*b)%3 for a,b in zip(tx,ell));ycode=y[0]+3*y[1]+9*y[2];edges.append((27*u+xcode,27*v+ycode))
 assert len(edges)==5022 and len(set(edges))==5022
 degrees=[0]*837
 for u,v in edges:assert u!=v;degrees[u]+=1;degrees[v]+=1
 assert set(degrees)=={12}
 (outdir/'graph837.edges').write_text('837 5022\n'+''.join(f'{u} {v}\n' for u,v in edges))
 (outdir/'construction.json').write_text(json.dumps(dict(q=3,dimension=3,controller=C,inverse_ports=INV,outgoing_return_directions=L,matrices=Ts,chosen_source_option_per_edge=choice,pair_certificate=records),separators=(',',':'))+'\n')
 result=dict(status='PRODUCTION_LOCAL_CERTIFICATE_AND_DEGREES_PASS',vertices=837,edges=5022,degree_histogram=dict(Counter(degrees)),directed_pencils_checked=4*n,rank_histogram=dict(rankhist),good_matrix_is_J_minus_A_plus_I=True,all_controller_pairs_certified=len(records),diameter_upper_bound=3,full_graph_BFS_performed=False,root_final_BFS_pending=True)
 (outdir/'production_check.json').write_text(json.dumps(result,indent=2)+'\n');return result
