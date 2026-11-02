from pathlib import Path
from itertools import product
import json,time
P=Path(__file__).resolve().parent;t=time.process_time()
q=3
A=[[[1,2,0,2,0],[1,2,1,2,0],[1,2,1,1,0],[2,0,0,0,0],[1,2,2,0,1]],
   [[0,0,0,2,0],[2,2,1,2,0],[2,1,0,0,0],[0,1,2,0,0],[1,0,1,0,1]],
   [[2,1,0,0,0],[0,1,1,0,0],[2,2,0,1,0],[2,0,1,0,0],[2,2,1,1,1]],
   [[1,2,0,1,0],[2,2,0,1,0],[1,2,0,2,0],[0,1,1,2,0],[2,1,2,1,1]]]
b=[[2,2,2,0,0],[0,1,0,0,1],[2,1,2,0,2],[1,0,1,0,2]]
def mv(M,v):return [sum(x*y for x,y in zip(row,v))%3 for row in M]
def mm(M,N):return [[sum(M[i][k]*N[k][j] for k in range(5))%3 for j in range(5)] for i in range(5)]
def rank(columns):
 M=[[columns[j][i]%3 for j in range(5)] for i in range(5)];r=0
 for c in range(5):
  pivot=next((i for i in range(r,5) if M[i][c]),None)
  if pivot is None:continue
  M[r],M[pivot]=M[pivot],M[r];scale=pow(M[r][c],-1,3);M[r]=[x*scale%3 for x in M[r]]
  for i in range(5):
   if i!=r:
    f=M[i][c];M[i]=[(x-f*y)%3 for x,y in zip(M[i],M[r])]
  r+=1
 return r
I=[[int(i==j) for j in range(5)] for i in range(5)]
for i in range(4):assert mm(A[i],A[i^1])==I and mv(A[i^1],b[i])==b[i^1]
records=[]
for w in product(range(4),repeat=5):
 if any(w[i+1]==(w[i]^1) for i in range(4)):continue
 columns=[]
 for c in w:columns=[mv(A[c],v) for v in columns]+[b[c]]
 r=rank(columns);assert r==5,(w,r)
 records.append(dict(word=w,rank=r))
assert len(records)==324
chart=dict(source='Mizuno arXiv2606.15860v1 Appendix A.6.1; locally supplied text literature/dd82/arxiv_2606.15860.txt',field=3,dimension=5,inverse_symbols=[1,0,3,2],matrices=A,vectors=b)
(P/'route_chart_F3_5.json').write_text(json.dumps(chart,indent=2)+'\n')
(P/'chart_check.json').write_text(json.dumps(dict(status='COMPLETE',inverse_matrix_and_vector_relations_verified=True,reduced_words_checked=324,minimum_rank=5,all_word_ranks=records,CPU_seconds=time.process_time()-t,large_graph_constructed=False),indent=2)+'\n')
print(json.dumps(dict(reduced_words=324,minimum_rank=5,CPU_seconds=time.process_time()-t)))
