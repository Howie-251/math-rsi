"""Independent Python audit of the added Q4 coefficients and their high-dimensional averaging."""
from pathlib import Path
from itertools import combinations
import numpy as np,json
from scipy import sparse
P=Path(__file__).resolve().parent;z=np.load(P/'new_flags_meta.npz');ec=z['empty_codes'];vc=z['vertex_codes']
qs=[(0,1),(0,2),(1,3),(2,3)]
def pairs(n):return [(i,j) for i in range(n) for j in range(i,n)]
def tri(n):
 a=np.zeros((n,n),int)
 for k,(i,j) in enumerate(pairs(n)):a[i,j]=a[j,i]=k
 return a
te,tv=tri(45),tri(9)
def has(G,x,y):return int(tuple(sorted((x,y))) in G)
def squarecode(G,x,i,j):
 vm=[x,x^(1<<i),x^(1<<j),x^(1<<i)^(1<<j)]
 return sum(has(G,vm[a],vm[b])<<k for k,(a,b) in enumerate(qs))
def emptyflag(G,x,i,j,k):
 vm=[x,x^(1<<i),x^(1<<j),x^(1<<i)^(1<<j)]
 s=sum(has(G,v,v^(1<<k))<<a for a,v in enumerate(vm))
 s+=16*squarecode(G,x^(1<<k),i,j)
 return int(ec[s])
def local(G):
 a=np.zeros(1080,np.int64)
 for i,j in combinations(range(4),2):
  for x in range(16):
   if x&((1<<i)|(1<<j)) or squarecode(G,x,i,j):continue
   k,l=[k for k in range(4) if k not in (i,j)]
   u=emptyflag(G,x,i,j,k);v=emptyflag(G,x,i,j,l);assert u>=0 and v>=0;a[te[u,v]]+=2
 ds=list(combinations(range(4),2))
 for x in range(16):
  for h,(i,j) in enumerate(ds):
   for k,l in ds[h+1:]:
    if len({i,j,k,l})<4:continue
    u=int(vc[squarecode(G,x,i,j)]);v=int(vc[squarecode(G,x,k,l)]);assert u>=0 and v>=0;a[1035+tv[u,v]]+=1
 return a
bd=np.load(P/'base_data.npz');edges=[tuple(e) for e in bd['edges']]
F=sparse.csr_matrix((np.memmap(P/'new_flags_vals.bin',dtype=np.int16,mode='r'),np.memmap(P/'new_flags_cols.bin',dtype=np.int32,mode='r'),np.memmap(P/'new_flags_ptr.bin',dtype=np.int64,mode='r')),shape=(3312331,1080))
graphs=np.load(P/'full_flags_graphs.npy');rng=np.random.default_rng(20261027)
for r in rng.choice(len(graphs),500,replace=False):
 m=int(graphs[r]);G=set()
 for e,(x,y) in enumerate(edges):
  if m>>e&1:G.add((x,y))
  if m>>(e+12)&1:G.add((x+8,y+8))
 for x in range(8):
  if m>>(24+x)&1:G.add((x,x+8))
 assert np.array_equal(local(G),F[r].toarray().ravel()),('local coefficient mismatch',r)
print('PASS: 500 independent Python local reconstructions',flush=True)
def trial(n,seed):
 rng=np.random.default_rng(seed);G=set();eds=[(x,x^(1<<i)) for x in range(1<<n) for i in range(n) if not (x>>i&1)]
 for e in rng.permutation(len(eds)):
  x,y=eds[e];i=(x^y).bit_length()-1
  if all(not(has(G,x,x^(1<<j)) and has(G,y,y^(1<<j)) and has(G,x^(1<<j),y^(1<<j))) for j in range(n) if j!=i):G.add((x,y))
 # Direct distinct-direction moments.
 direct=np.zeros(1080);gram=np.zeros((45,45));marg=np.zeros(45);gramv=np.zeros((9,9));nr=(1<< (n-2))*n*(n-1)//2
 for i,j in combinations(range(n),2):
  for x in range(1<<n):
   if x&((1<<i)|(1<<j)) or squarecode(G,x,i,j):continue
   ss=[emptyflag(G,x,i,j,k) for k in range(n) if k not in (i,j)];q=len(ss);u=np.bincount(ss,minlength=45)/q;gram+=np.outer(u,u)/nr;marg+=u/nr
   for a in range(q):
    for b in range(q):
     if a!=b:direct[te[ss[a],ss[b]]]+=1/(nr*q*(q-1))
 ds=list(combinations(range(n),2));D=len(ds);dis=(n-2)*(n-3)//2
 for x in range(1<<n):
  ss=[int(vc[squarecode(G,x,i,j)]) for i,j in ds];u=np.bincount(ss,minlength=9)/D;gramv+=np.outer(u,u)/(1<<n)
  for a,(i,j) in enumerate(ds):
   for b,(k,l) in enumerate(ds):
    if len({i,j,k,l})==4:direct[1035+tv[ss[a],ss[b]]]+=1/((1<<n)*D*dis)
 # All Q4 restrictions, computed directly, not through the new C++ table.
 total=np.zeros(1080);num=0
 for ds4 in combinations(range(n),4):
  mask=sum(1<<j for j in ds4)
  for x in range(1<<n):
   if x&mask:continue
   vm=[x^sum(((v>>h)&1)<<j for h,j in enumerate(ds4)) for v in range(16)]
   H={(v,v^(1<<h)) for v in range(16) for h in range(4) if not(v>>h&1) and has(G,vm[v],vm[v^(1<<h)])}
   total+=local(H);num+=1
 pred=total/(48*num);err=float(np.max(np.abs(pred-direct)));assert err<1e-12
 R=np.zeros((45,45))
 for k,(i,j) in enumerate(pairs(45)):R[i,j]=R[j,i]=pred[k] if i==j else pred[k]/2
 exact=(n-3)/(n-2)*R+np.diag(marg)/(n-2);ge=float(np.max(np.abs(exact-gram)));assert ge<1e-12
 ev=float(np.linalg.eigvalsh(gramv).min());assert ev>=-1e-12
 return dict(n=n,seed=seed,edges=len(G),local_to_global_error=err,empty_Gram_error=ge,vertex_Gram_min_eigenvalue=ev)
res=[trial(n,s) for n in [5,6] for s in [11,29,53]]
(P/'new_flags_audit.json').write_text(json.dumps({'random_local_rows_checked':500,'high_dimensional_tests':res},indent=2));print(json.dumps(res,indent=2),flush=True)
