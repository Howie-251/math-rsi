from pathlib import Path
from collections import Counter
from itertools import product
import json,time
P=Path(__file__).resolve().parent;started=time.process_time();D=json.loads((P/'construction.json').read_text());C=D['controller'];Ts=D['matrices'];L=D['outgoing_return_directions'];inv=[1,0,3,2]
def plus(a,b,q):return a^b if q==4 else (a+b)%3
def times(a,b,q):
 if q==3:return a*b%3
 c=0
 for k in range(2):
  if b>>k&1:c^=a<<k
 return c^7 if c&4 else c
def sumf(xs,q):
 a=0
 for b in xs:a=plus(a,b,q)
 return a
def mv(T,x,q):return tuple(sumf((times(a,b,q) for a,b in zip(row,x)),q) for row in T)
def mm(A,B,q):return [[sumf((times(A[i][k],B[k][j],q) for k in range(3)),q) for j in range(3)] for i in range(3)]
def rank(cols,q):
 a=[list(row) for row in zip(*cols)];r=0
 for j in range(len(cols)):
  pivot=next((i for i in range(r,3) if a[i][j]),None)
  if pivot is None:continue
  a[r],a[pivot]=a[pivot],a[r];iv=next(z for z in range(1,q) if times(a[r][j],z,q)==1);a[r]=[times(z,iv,q) for z in a[r]]
  for i in range(3):
   if i!=r and a[i][j]:
    f=a[i][j];a[i]=[plus(x,times(f,y,q) if q==4 else -times(f,y,q)%3,q) for x,y in zip(a[i],a[r])]
  r+=1
  if r==3:break
 return r
def span(cols,q):
 return frozenset(tuple(sumf((times(c,v[j],q) for c,v in zip(co,cols)),q) for j in range(3)) for co in product(range(q),repeat=len(cols)))
def bad_turns(T,p,q):
 return tuple((i,j) for i in range(4) if i!=p for j in range(4) if j!=inv[p] if rank([mv(T,L[i],q),L[inv[p]],L[j]],q)<3)
I=[[1,0,0],[0,1,0],[0,0,1]]
gf4bad=Counter();route_rank=Counter();pairkind=Counter()
for u in range(30):
 for p in range(4):
  v=C[u][p];assert C[v][inv[p]]==u and mm(Ts[v][inv[p]],Ts[u][p],4)==I
  assert mv(Ts[u][p],L[p],4)==tuple(L[inv[p]])
  b=bad_turns(Ts[u][p],p,4);gf4bad[len(b)]+=1;assert len(b)==1
def route(start,word,q):
 cols=[];u=start
 for p in word:
  cols=[mv(Ts[u][p],x,q) for x in cols]+[tuple(L[inv[p]])];u=C[u][p]
 return u,rank(cols,q)
for rec in D['pair_certificate']:
 end,r=route(rec['u'],rec['word'],4);assert end==rec['v'];pairkind[rec['kind']]+=1
 if rec['kind']=='full_rank':assert len(rec['word'])==3 and r==3
 else:assert rec['kind']=='edge_pencil' and len(rec['word'])==1
for u in range(30):
 for a in range(4):
  for b in range(4):
   if b==inv[a]:continue
   for c in range(4):
    if c!=inv[b]:route_rank[route(u,[a,b,c],4)[1]]+=1

patterns=[{} for _ in range(4)];counts=[Counter() for _ in range(4)];gl=0;fixcounts=[0]*4
for entries in product(range(3),repeat=9):
 T=[list(entries[j:j+3]) for j in (0,3,6)]
 if rank(list(zip(*T)),3)!=3:continue
 gl+=1
 for p in range(4):
  if mv(T,L[p],3)!=tuple(L[inv[p]]):continue
  fixcounts[p]+=1;b=bad_turns(T,p,3);counts[p][len(b)]+=1
  if len(b)==2:
   assert len({i for i,j in b})==2 and len({j for i,j in b})==2
   patterns[p].setdefault(b,T)
assert gl==11232 and fixcounts==[432]*4
records=[]
for p in range(4):
 assert len(patterns[p])==18 and counts[p]=={2:324,3:108}
 pp=[]
 for b,T in sorted(patterns[p].items()):
  planes={span([mv(T,L[i],3),L[inv[p]]],3) for i in range(4) if i!=p}|{span([L[inv[p]],L[j]],3) for j in range(4) if j!=inv[p]}
  assert len(planes)==4 and len(set().union(*planes))==27
  Ti=[[0]*3 for _ in range(3)]
  pre={mv(T,x,3):x for x in product(range(3),repeat=3)}
  for j in range(3):
   e=tuple(int(i==j) for i in range(3));v=pre[e]
   for i in range(3):Ti[i][j]=v[i]
  reverse=bad_turns(Ti,inv[p],3);assert set(reverse)=={(j,i) for i,j in b}
  pp.append(dict(bad_turns=b,matrix=T,inverse_matrix=Ti,reverse_bad_turns=reverse,pencil_planes=4,pencil_union_size=27))
 records.append(dict(port=p,reverse_port=inv[p],matrices_fixing_direction=432,rank_bad_count_histogram=dict(counts[p]),valid_pencil_patterns=pp))
(P/'q3_local_patterns.json').write_text(json.dumps(dict(q=3,dimension=3,directions=L,inverse=inv,GL3_count=gl,ports=records),indent=2)+'\n')
result=dict(status='SOURCE_F4_LOCAL_RULES_AND_CERTIFICATE_CHECKED_Q3_LOCAL_RULES_PREPARED',source_controller_vertices=30,source_GF4_inverse_direction_edges_checked=120,source_GF4_bad_turn_histogram=dict(gf4bad),source_GF4_pair_certificate_counts=dict(pairkind),source_GF4_NB3_rank_histogram=dict(route_rank),q3_GL3_count=gl,q3_edge_matrix_counts_per_port=fixcounts,q3_patterns_per_port=[len(p) for p in patterns],q3_valid_pencil_planes=4,q3_pencil_union_size=27,q3_bad_turns_per_directed_edge=2,q3_good_turns_per_directed_edge=7,q3_reverse_rank_pattern_consistent=True,q3_global_certificate_solved=False,q3_source_810_graph_not_constructed_or_verified=True,controller31_not_searched=True,total_CPU_seconds=time.process_time()-started,large_graph_generated=False,large_graph_BFS=False)
(P/'local_check.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
