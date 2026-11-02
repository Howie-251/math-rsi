#!/usr/bin/env python3
"""Exact183 projective assignments of the best saved degree5 quotient skeleton."""
from collections import Counter,deque
from itertools import product
from pathlib import Path
import json
import subprocess
import time

OUT=Path(__file__).resolve().parent
PROJECT=OUT.parents[2]
P=13;K=27;Q=P*K
POW=tuple(pow(3,i,P)for i in range(K))

def vector(residues):return tuple((1-POW[i])%P for i in residues)

def canonical(values,residues):
 v=vector(residues);pivot=next(i for i,x in enumerate(v)if x)
 t=-values[pivot]*pow(v[pivot],-1,P)%P
 w=tuple((x+t*d)%P for x,d in zip(values,v))
 if not any(w):return None,t,None
 scale=pow(next(x for x in w if x),-1,P)
 return tuple(x*scale%P for x in w),t,scale

def representatives(residues):
 v=vector(residues);pivot=next(i for i,x in enumerate(v)if x)
 free=[i for i in range(4)if i!=pivot]
 out=[]
 for first in range(3):
  for tail in product(range(P),repeat=2-first):
   values=[0]*4;values[free[first]]=1
   for i,x in zip(free[first+1:],tail):values[i]=x
   out.append(tuple(values))
 assert len(out)==183 and len(set(out))==183
 return out

def legal(values,residues):
 if any(x==0 and i==0 for x,i in zip(values[:2],residues[:2])):return False
 return len({(0,0),(values[2],residues[2]),(values[3],residues[3])})==3

def mul(g,h):
 x,i=divmod(g,K);y,j=divmod(h,K)
 return ((x+POW[i]*y)%P)*K+(i+j)%K

def inverse(g):
 x,i=divmod(g,K);j=-i%K
 return (-POW[j]*x%P)*K+j

def graph(values,residues):
 a,b,s,t=[x*K+i for x,i in zip(values,residues)]
 A=[a,inverse(a)];B=[b,inverse(b)];S=[0,s,t];SI=list(map(inverse,S))
 return [[mul(g,h)for h in A]+[Q+mul(g,h)for h in S]for g in range(Q)]+[[Q+mul(g,h)for h in B]+[mul(g,h)for h in SI]for g in range(Q)]

def roots(adj):
 out=[]
 for root in [0,Q]:
  ds=[-1]*(2*Q);ds[root]=0;todo=deque([root])
  while todo:
   u=todo.popleft()
   for v in adj[u]:
    if ds[v]<0:ds[v]=ds[u]+1;todo.append(v)
  out.append({'missing_gt5':sum(x<0 or x>5 for x in ds),
              'eccentricity':max(ds)if min(ds)>=0 else None,
              'distance_histogram':dict(sorted(Counter(ds).items()))})
 return out

def edges(adj):return {(u,v)for u,neighbors in enumerate(adj)for v in neighbors if u<v}

def main():
 started=time.monotonic()
 source=PROJECT/'research/ddp/m1_degree5_transfer/n702_a0_b1.json'
 record=json.loads(source.read_text());a=divmod(record['A'][0],K);b=divmod(record['B'][0],K)
 S=sorted([divmod(s,K)for s in record['S']if s],key=lambda pair:pair[1])
 values=tuple(x for x,i in [a,b]+S);residues=tuple(i for x,i in [a,b]+S)
 original_graph=graph(values,residues);original_edges=edges(original_graph)
 assert original_edges=={tuple(map(int,line.split()))for line in source.with_suffix('.edges').read_text().splitlines()[1:]}
 canonical_values,translation,scale=canonical(values,residues)
 canonical_graph=graph(canonical_values,residues)
 def transform_vertex(vertex):
  side,g=divmod(vertex,Q);x,i=divmod(g,K)
  return side*Q+(scale*(x+(1-POW[i])*translation)%P)*K+i
 mapped={tuple(sorted((transform_vertex(u),transform_vertex(v))))for u,v in original_edges}
 assert mapped==edges(canonical_graph)
 canonical_roots=roots(canonical_graph)
 assert [r['missing_gt5']for r in canonical_roots]==[r['missing_gt5']for r in record['representative_BFS']]
 # Independently confirm that all13^4 raw assignments map into these183 classes,
 # each with13*12 members; the13 discarded assignments havezero projection.
 multiplicity=Counter();zero=0
 for raw in product(range(P),repeat=4):
  c,_,_=canonical(raw,residues)
  if c is None:zero+=1
  else:multiplicity[c]+=1
 reps=representatives(residues)
 assert set(multiplicity)==set(reps)and set(multiplicity.values())=={156}and zero==13
 check_start=time.monotonic();results=[];best=None
 for c in reps:
  if not legal(c,residues):results.append({'values':c,'status':'ILLEGAL'});continue
  adj=graph(c,residues);assert all(len(set(row))==5 for row in adj)
  rr=roots(adj);score=sum(r['missing_gt5']for r in rr)
  row={'values':c,'status':'LEGAL','missing_sum':score,'root_missing':[r['missing_gt5']for r in rr]}
  results.append(row)
  if best is None or score<best['missing_sum']:best={**row,'roots':rr}
 enumeration_seconds=time.monotonic()-check_start
 best_graph=graph(best['values'],residues);best_edges=edges(best_graph)
 edgepath=OUT/'best.edges';edgepath.write_text(f'{2*Q} {len(best_edges)}\n'+''.join(f'{u} {v}\n'for u,v in sorted(best_edges)))
 verified=subprocess.run([str(PROJECT/'computations/ddp/verify_graph'),str(edgepath),'5','5'],text=True,capture_output=True)
 assert verified.returncode in [0,1],verified.stderr
 bfs=json.loads(verified.stdout);assert bfs['bad_unordered_pairs']==Q*best['missing_sum']//2
 output={'status':'FIXED_SKELETON_COMPLETE','scope':{'alpha_beta_sigma_tau':residues},
  'source':str(source.relative_to(PROJECT)),'source_values':values,
  'conjugation_vector':vector(residues),'canonical_source_values':canonical_values,
  'normalization':{'inner_translation':translation,'scaling':scale,'full_edge_permutation_matches':True},
  'raw_normalization_check':{'raw_assignments':P**4,'discarded_zero_class':zero,'nonzero_classes':len(multiplicity),'members_per_nonzero_class':156},
  'projective_assignments':len(reps),'legal_assignments':sum(r['status']=='LEGAL'for r in results),
  'illegal_assignments':sum(r['status']=='ILLEGAL'for r in results),
  'best':best,'best_independent_all_source_bfs':bfs,
  'full_scoring_enumeration_seconds':enumeration_seconds,'total_seconds':time.monotonic()-started,
  'assignments':results,'nonclaim':'No quotient-skeleton sweep performed by this script.'}
 (OUT/'result.json').write_text(json.dumps(output,indent=2)+'\n')
 print(json.dumps({k:output[k]for k in ['status','scope','source_values','canonical_source_values','projective_assignments','legal_assignments','best','full_scoring_enumeration_seconds','total_seconds']}))

if __name__=='__main__':main()
