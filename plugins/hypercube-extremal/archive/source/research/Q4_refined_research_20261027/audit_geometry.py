"""Audit symmetry and the local-to-high-dimensional normalization on Q5/Q6.
These tests supplement, and do not replace, exhaustive integer verification.
"""
from itertools import combinations,permutations
import numpy as np,json,time
from model import Model,P
M=Model();x=np.load(P/'adaptive_best.npz')['x'];fq=x[M.oldnv:M.oldnv+M.fnv];vq=M.matrix(x,11);look=M.fm['lookup'];vcode=np.fromfile(P/'vertex_flag_codes.bin',dtype=np.int32);rng=np.random.default_rng(20261027)
qe=[(0,1),(0,2),(1,3),(2,3)]
def edges(n):return [(x,x^(1<<i)) for x in range(1<<n) for i in range(n) if not(x>>i&1)]
def has(E,u,v):return (min(u,v),max(u,v)) in E
def faces(n):
 for i,j in combinations(range(n),2):
  for z in range(1<<n):
   if z&((1<<i)|(1<<j)):continue
   yield i,j,[z,z^(1<<i),z^(1<<j),z^(1<<i)^(1<<j)]
def fstates(E,n):
 for i,j,v in faces(n):
  r=sum(int(has(E,v[u],v[w]))<<a for a,(u,w) in enumerate(qe));assert r!=15
  s=[]
  for k in range(n):
   if k in (i,j):continue
   s.append(sum(int(has(E,v[a],v[a]^(1<<k)))<<a for a in range(4))+sum(int(has(E,v[u]^(1<<k),v[w]^(1<<k)))<<(a+4) for a,(u,w) in enumerate(qe)))
  yield r,s

def score(E,n):
 vals=[];diag=[];prod=[];err=0
 for r,s in fstates(E,n):
  q=len(s);z=np.array([[fq[look[r,a,b]] for b in s] for a in s]);rr=(z.sum()-np.trace(z))/(q*(q-1));pp=z.mean();dd=np.diag(z).mean();err=max(err,abs(pp-(q-1)/q*rr-dd/q));vals.append(rr);diag.append(dd);prod.append(pp)
 # Vertex-root joint density for two disjoint direction pairs.
 pairs=list(combinations(range(n),2));vterms=[]
 for z in range(1<<n):
  states=[]
  for i,j in pairs:
   v=[z,z^(1<<i),z^(1<<j),z^(1<<i)^(1<<j)];code=sum(int(has(E,v[u],v[w]))<<a for a,(u,w) in enumerate(qe));states.append(vcode[code])
  vals2=[vq[states[a],states[b]] for a in range(len(pairs)) for b in range(a+1,len(pairs)) if len(set(pairs[a]+pairs[b]))==4]
  vterms.append(np.mean(vals2))
 return float(np.mean(vals)),float(np.mean(vterms)),float(min(prod)),float(err)

def greedy(n):
 ee=edges(n);sq=[]
 for i,j,v in faces(n):sq.append({tuple(sorted((v[u],v[w]))) for u,w in qe})
 by={e:[] for e in ee}
 for f in sq:
  for e in f:by[e].append(f)
 E=set()
 for k in rng.permutation(len(ee)):
  e=ee[k]
  if rng.uniform()<.07:continue
  if all(not((f-{e})<=E) for f in by[e]):E.add(e)
 return E
results=[]
for n in (5,6):
 for trial in range(3):
  E=greedy(n);global_s=score(E,n);local=[]
  for ds in combinations(range(n),4):
   dm=sum(1<<i for i in ds)
   for b in range(1<<n):
    if b&dm:continue
    vm=[b^sum(((z>>j)&1)<<ds[j] for j in range(4)) for z in range(16)]
    EE={e for e in edges(4) if has(E,vm[e[0]],vm[e[1]])};local.append(score(EE,4)[:2])
  err=float(np.max(np.abs(np.mean(local,axis=0)-np.array(global_s[:2]))));assert err<1e-12 and global_s[2]>-1e-10 and global_s[3]<1e-12
  results.append(dict(n=n,trial=trial,edges=len(E),restrictions=len(local),averaging_error=err,minimum_root_square=global_s[2],collision_identity_error=global_s[3]))
# All 384 geometric symmetries on three independently generated Q4 graphs.
symerr=0.;checks=0
for trial in range(3):
 E=greedy(4);base=np.array(score(E,4)[:2])
 for p in permutations(range(4)):
  for t in range(16):
   vm=[t^sum(((z>>j)&1)<<p[j] for j in range(4)) for z in range(16)]
   EE={tuple(sorted((vm[u],vm[v]))) for u,v in E};a=np.array(score(EE,4)[:2]);symerr=max(symerr,float(np.max(np.abs(a-base))));checks+=1
assert symerr<1e-12
out=dict(high_dimensional_tests=results,symmetry_checks=checks,symmetry_max_error=symerr,description='Random Q5/Q6 normalization audit plus all 384 automorphisms of three Q4 samples. Exhaustive certificate verification is separate.')
(P/'geometry_audit.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2),flush=True)
