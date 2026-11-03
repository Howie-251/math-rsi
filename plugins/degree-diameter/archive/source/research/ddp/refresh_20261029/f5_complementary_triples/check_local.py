import itertools,json,time,os,resource
from pathlib import Path
D=Path(__file__).resolve().parent
ROOT=D.parents[3]
start=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(9,10))
Q=5;L=[(1,0,0),(0,1,0),(0,0,1),(1,1,1)];invport=[1,0,3,2]
def dump(name,x):(D/name).write_text(json.dumps(x,indent=2)+'\n')
dump('HANDLE.json',{'status':'RUNNING','pid':os.getpid()})
def add(x,y):return tuple((a+b)%5 for a,b in zip(x,y))
def scale(a,x):return tuple(a*t%5 for t in x)
def mv(T,x):return tuple(sum(a*b for a,b in zip(row,x))%5 for row in T)
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(3))%5 for j in range(3)] for i in range(3)]
I=[[int(i==j) for j in range(3)] for i in range(3)]
def inverse(T):
 a=[row[:]+I[i][:] for i,row in enumerate(T)]
 for j in range(3):
  k=next(i for i in range(j,3) if a[i][j]);a[j],a[k]=a[k],a[j]
  a[j]=[x*pow(a[j][j],-1,5)%5 for x in a[j]]
  for i in range(3):
   if i!=j:
    c=a[i][j];a[i]=[(x-c*y)%5 for x,y in zip(a[i],a[j])]
 return [row[3:] for row in a]
def rank(cols):
 a=[list(x) for x in zip(*cols)];r=0
 for j in range(len(cols)):
  k=next((i for i in range(r,3) if a[i][j]),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r];a[r]=[x*pow(a[r][j],-1,5)%5 for x in a[r]]
  for i in range(3):
   if i!=r:
    c=a[i][j];a[i]=[(x-c*y)%5 for x,y in zip(a[i],a[r])]
  r+=1
  if r==3:break
 return r
def span(a,b):return frozenset(add(scale(i,a),scale(j,b)) for i in range(5) for j in range(5))
T0=[[0,2,4],[1,0,0],[0,1,3]]
S=[[0,4,1],[0,4,0],[1,4,0]]
assert all(mv(S,L[i])==scale(k,L[j]) for i,j,k in [(0,2,1),(1,3,4),(2,0,1),(3,1,4)])
T2=[[4*x%5 for x in row] for row in mm(mm(S,T0),inverse(S))]
Ts=[T0,inverse(T0),T2,inverse(T2)]
V=list(itertools.product(range(5),repeat=3));ALL=frozenset(V);records=[]
for p,T in enumerate(Ts):
 q=invport[p]
 assert mv(T,L[p])==L[q] and mm(Ts[q],T)==I
 turns=[{'i':i,'j':j,'rank':rank([mv(T,L[i]),L[q],L[j]])} for i in range(4) if i!=p for j in range(4) if j!=q]
 assert len(turns)==9 and all(x['rank']==3 for x in turns)
 planes=[span(mv(T,L[i]),L[q]) for i in range(4) if i!=p]+[span(L[q],L[j]) for j in range(4) if j!=q]
 assert len(set(planes))==6 and set.union(*(set(x) for x in planes))==ALL
 assert all(len(P)==25 for P in planes)
 assert all(len(planes[i]&planes[j])==5 for i in range(6) for j in range(i))
 for x in V:
  center=mv(T,x)
  union=set().union(*({add(center,y) for y in P} for P in planes))
  assert union==ALL
 records.append({'port':p,'reverse_port':q,'T':T,'direction_exact':True,'reverse_actual_inverse':True,'nine_turns':turns,'pencil_plane_count':6,'plane_sizes':[25]*6,'pairwise_intersection_sizes':[5]*15,'pencil_union_size':125,'starting_coordinates_checked':125,'all_starting_coordinates_full':True,'planes':[sorted(x) for x in planes]})
src=ROOT/'research/ddp/breadth_20261027_wave4/mizuno_d3_source'
con=json.load(open(src/'construction.json')); C=con['controller'];assert len(C)==30
arc_count=0
for u,row in enumerate(C):
 assert len(row)==4 and len(set(row))==4 and u not in row
 for p,v in enumerate(row):
  q=invport[p];assert C[v][q]==u and mm(Ts[q],Ts[p])==I and mv(Ts[p],L[p])==L[q];arc_count+=1
cached=json.load(open(src/'controller_structure.json'))['NB3_counts']
assert len(cached)==30 and all(len(row)==30 for row in cached)
missing=[];required=0;mincount=100
for u in range(30):
 for v in range(30):
  if v not in C[u]:
   required+=1;mincount=min(mincount,cached[u][v])
   if not cached[u][v]:missing.append([u,v])
assert required==780 and not missing and arc_count==120
dump('MATRICES_AND_PENCILS.json',{'field':5,'directions':L,'inverse_ports':invport,'frame_permutation_matrix':S,'frame_permutation':[2,3,0,1],'ports':records})
result={'status':'ALL_FOUR_PORTS_COMPLEMENTARY_TRIPLES_SUPPORTED','finite_prediction':'SUPPORTED','four_direction_bindings':True,'four_inverse_bindings':True,'central_turns_checked':36,'rank3_turns':36,'pencil_planes_per_port':6,'pencil_union_each':125,'source_coordinates_per_port':125,'total_translated_pencil_checks':500,'source_controller_darts_bound':arc_count,'cached_required_nonadjacent_or_equal_pairs':required,'cached_required_NB3_min':mincount,'cached_required_zero_slots':missing,'cached_directed_adjacent_pairs':120,'conditional_fullgraph_n':3750,'conditional_fullgraph_degree':20,'conditional_fullgraph_D_upper_bound':3,'actual_full_graph_generated':False,'new_graph_BFS':0,'old_source_BFS':0,'new_word_enumeration':0,'source_matrix_search':0,'record_claim':False,'actual_fullgraph_n':None,'actual_fullgraph_D':None,'cpu_seconds':time.process_time()-start,'pid':os.getpid()}
dump('RESULT.json',result);dump('HANDLE.json',{'status':'TERMINAL','pid':os.getpid()})
dump('TERMINAL.json',{'status':'COMPLETE_LOCAL_FINITE_CHECK','result':'SUPPORTED','pending':[],'cpu_seconds':result['cpu_seconds'],'new_graphs':0})
print(json.dumps(result),flush=True)
