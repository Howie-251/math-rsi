"""Independent direct-count audit in Q5 and Q6 of the Q4-to-high-dimensional lift."""
import os,itertools,json,numpy as np
from scipy import sparse
from sdp_core import pairs,unpack
P=os.path.dirname(__file__);bd=np.load(P+'/base_data.npz');meta=np.load(P+'/full_meta.npz');C=sparse.load_npz(P+'/full_C.npz');E=sparse.load_npz(P+'/full_eq.npz')
dims=meta['dims'];starts=meta['starts'];lookup={int(k):i for i,k in enumerate(meta['keys'])};trans=bd['trans'];edge3=[tuple(e) for e in bd['edges']]
luts=[]
for n in dims:
 t=np.zeros((n,n),int)
 for h,(i,j) in enumerate(pairs(n)):t[i,j]=t[j,i]=h
 luts.append(t)
def idxroot(r0,r1,s0,s1):
 if r0+r1==0:return 3,s0*8+s1
 if r0+r1==2:return 5,s0*7+s1
 return 4,(s0*7+s1 if r0==0 else s1*7+s0)
def trial(n,seed):
 rng=np.random.default_rng(seed);edges=[(x,x^(1<<i)) for x in range(1<<n) for i in range(n) if not x>>i&1];G=set()
 def has(x,y):return int(tuple(sorted((x,y))) in G)
 for e in rng.permutation(len(edges)):
  x,y=edges[e];i=(x^y).bit_length()-1
  if all(not(has(x,x^(1<<j)) and has(y,y^(1<<j)) and has(x^(1<<j),y^(1<<j))) for j in range(n) if j!=i):G.add((x,y))
 # Direct moments over oriented roots and distinct external directions.
 direct=np.zeros(starts[-1]);marg=[np.zeros(d) for d in dims];grams=[np.zeros((d,d)) for d in dims]
 def triple(x,i,k):
  y=x^(1<<i)
  return has(x,x^(1<<k))+2*has(y,y^(1<<k))+4*has(x^(1<<k),y^(1<<k))
 def accumulate(b,ss,denroots):
  q=len(ss);v=np.bincount(ss,minlength=dims[b])/q;marg[b][:]+=v/denroots;grams[b][:]+=np.outer(v,v)/denroots
  for j in range(q):
   for k in range(q):
    if j!=k:direct[starts[b]+luts[b][ss[j],ss[k]]]+=1/(denroots*q*(q-1))
 for x in range(1<<n):
  for i in range(n):
   b=has(x,x^(1<<i));ss=[triple(x,i,k) for k in range(n) if k!=i]
   accumulate(b,ss,(1<<n)*n)
  for g in range(n):
   ss=[has(x,x^(1<<k))+2*has(x^(1<<g),x^(1<<g)^(1<<k)) for k in range(n) if k!=g]
   accumulate(2,ss,(1<<n)*n)
   for i in range(n):
    if i==g:continue
    r0=has(x,x^(1<<i));r1=has(x^(1<<g),x^(1<<g)^(1<<i));ss=[]
    for k in range(n):
     if k in [g,i]:continue
     b,s=idxroot(r0,r1,triple(x,i,k),triple(x^(1<<g),i,k));ss.append(s)
    accumulate(b,ss,(1<<n)*n*(n-1))
 # Independently enumerate every Q4 and every choice of its grey direction.
 hist=np.zeros(len(lookup));num=0
 for ds in itertools.combinations(range(n),4):
  mask=sum(1<<i for i in ds)
  for x in range(1<<n):
   if x&mask:continue
   for g in ds:
    vis=[i for i in ds if i!=g]
    A=[]
    for bit in range(2):
     def embed(v):return x^(bit<<g)^sum(((v>>j)&1)<<vis[j] for j in range(3))
     m=sum(has(embed(u),embed(v))<<j for j,(u,v) in enumerate(edge3));A.append(m)
    key=int(min(np.min(4096*trans[:,A[0]]+trans[:,A[1]]),np.min(4096*trans[:,A[1]]+trans[:,A[0]])))
    hist[lookup[key]]+=1;num+=1
 hist/=num;pred=np.asarray(C.T@hist).ravel()/96
 err=float(np.max(np.abs(pred-direct)));eqerr=float(np.max(np.abs(E.T@hist)))
 gramerr=0;mineig=0
 for b,d in enumerate(dims):
  M=unpack(pred[starts[b]:starts[b+1]],d);M=(M+np.diag(np.diag(M)))/2
  q=n-1 if b<3 else n-2
  exact=(q-1)/q*M+np.diag(marg[b])/q
  gramerr=max(gramerr,float(np.max(np.abs(exact-grams[b]))));mineig=min(mineig,float(np.linalg.eigvalsh(exact)[0]))
 assert err<2e-12 and eqerr<2e-12 and gramerr<2e-12 and mineig>-2e-12
 return dict(n=n,seed=seed,edges=len(G),density=len(G)/(n*2**(n-1)),moment_error=err,consistency_error=eqerr,Gram_error=gramerr,min_eigenvalue=mineig)
results=[trial(n,s) for n in [5,6] for s in [11,29,53]]
with open(P+'/lift_audit.json','w') as f:json.dump(results,f,indent=2)
print(json.dumps(results,indent=2))
