from pathlib import Path
import json,time

B=Path(__file__).resolve().parent
t0=time.process_time()
edges=sorted({tuple(sorted((i,(i+d)%14))) for i in range(14) for d in [1,2]})
assert len(edges)==28
tree=[edges.index((i,i+1)) for i in range(13)]
free=[e for e in range(28) if e not in tree]
findex={e:k for k,e in enumerate(free)}
assert len(free)==15
adj=[[] for _ in range(14)]
for e,(u,v) in enumerate(edges):
 adj[u].append((v,e,False));adj[v].append((u,e,True))
assert all(len(a)==4 for a in adj)

def toggle(poly,monomial):
 if monomial in poly:poly.remove(monomial)
 else:poly.add(monomial)

def signatures(word):
 c8=[0]*15
 # Q8 variables use i^a j^b (-1)^c. Every output low bit is
 # the same occurrence parity, applied to a- or b-variables.
 # The center is an exact multilinear Boolean polynomial.
 amask=bmask=0;center=set()
 for e,rev in word:
  if e not in findex:continue
  k=findex[e];c8[k]=(c8[k]+(-1 if rev else 1))%8
  a=1<<(3*k);b=1<<(3*k+1);c=1<<(3*k+2)
  toggle(center,c)
  if rev:
   for m in [a,b,a|b]:toggle(center,m)
  # c(x*y)=c(x)+c(y)+a(x)a(y)+b(x)b(y)+b(x)a(y).
  for prev,right in [(amask,a),(bmask,b),(bmask,a)]:
   bits=prev
   while bits:
    left=bits&-bits;bits-=left;toggle(center,left|right)
  amask^=a;bmask^=b
 return tuple(c8),(amask,bmask,tuple(sorted(center)))

raw=[[0]*14 for _ in range(14)]
c8=[[set() for _ in range(14)] for _ in range(14)]
q8=[[set() for _ in range(14)] for _ in range(14)]
for root in range(14):
 def dfs(v,word,last_edge,depth):
  raw[root][v]+=1;x,y=signatures(word);c8[root][v].add(x);q8[root][v].add(y)
  if depth==4:return
  for w,e,rev in adj[v]:
   if e!=last_edge:dfs(w,word+[(e,rev)],e,depth+1)
 dfs(root,[],-1,0)
assert all(sum(row)==161 for row in raw)
counts_c8=[[len(x) for x in row] for row in c8]
counts_q8=[[len(x) for x in row] for row in q8]
result=dict(status='COMPLETE_TWO_FIXED_GROUP_FUNCTION_CAPACITY_SCREEN',vertices=112,degree=4,target_D=4,base='square of C14, neighbors plus/minus1,plus/minus2',edges=edges,tree_edge_ids=tree,free_edge_ids=free,raw_short_word_counts=raw,C8_function_capacity=counts_c8,Q8_function_capacity=counts_q8,C8_min_capacity=min(map(min,counts_c8)),Q8_min_capacity=min(map(min,counts_q8)),C8_necessary_pass=all(x>=8 for row in counts_c8 for x in row),Q8_necessary_pass=all(x>=8 for row in counts_q8 for x in row),CPU_seconds=time.process_time()-t0,actual_graphs=0,BFS_runs=0)
(B/'CAPACITY.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['edges','raw_short_word_counts','C8_function_capacity','Q8_function_capacity']}))
