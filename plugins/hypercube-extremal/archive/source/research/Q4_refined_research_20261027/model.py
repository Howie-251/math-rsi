from pathlib import Path
import ctypes, numpy as np
from scipy import sparse
from sdp_core import unpack,vec
P=Path(__file__).resolve().parent
class Model:
 def __init__(self):
  self.meta=np.load(P/'full_meta.npz'); self.C=sparse.load_npz(P/'full_C.npz').astype(float)/96
  self.d=self.meta['d'];self.os=self.meta['starts'];self.oldnv=int(self.os[-1])
  self.fm=np.load(P/'face_orbit_meta.npz');self.fs=self.fm['starts'];self.fnv=int(self.fs[-1]);self.nv=self.oldnv+self.fnv+45
  self.roots=self.fm['roots'];self.fb=[np.load(P/f'face_block_{r}.npz') for r in self.roots]
  self.dims=list(self.meta['dims'])+list(self.fm['dims'])+[9]
  self.sh=np.memmap(P/'shadows.bin',dtype=np.int32,mode='r').reshape(-1,4);self.N=len(self.sh)
  self.fi=np.memmap(P/'face_indices.bin',dtype=np.uint16,mode='r').reshape(-1,24)
  self.vi=np.memmap(P/'vertex_indices.bin',dtype=np.uint8,mode='r').reshape(-1,48)
  self.dd=self.d[self.sh].mean(axis=1)
  self.lib=ctypes.CDLL(str(P/'evaluate.so'));self.lib.evaluate.argtypes=[ctypes.c_long]+[ctypes.c_void_p]*7
 def evaluate(self,x):
  p=np.asarray(self.d+self.C@x[:self.oldnv]);f=np.ascontiguousarray(x[self.oldnv:self.oldnv+self.fnv]);v=np.ascontiguousarray(x[-45:]);out=np.empty(self.N)
  self.lib.evaluate(self.N,*[a.ctypes.data for a in [self.sh,self.fi,self.vi,p,f,v,out]])
  return out
 def amat(self,rows):
  rows=np.asarray(rows);s=self.sh[rows];a=(self.C[s[:,0]]+self.C[s[:,1]]+self.C[s[:,2]]+self.C[s[:,3]])/4
  nr=len(rows)
  f=sparse.csr_matrix((np.full(nr*24,1/24),(np.repeat(np.arange(nr),24),self.fi[rows].ravel())),shape=(nr,self.fnv))
  v=sparse.csr_matrix((np.full(nr*48,1/48),(np.repeat(np.arange(nr),48),self.vi[rows].ravel())),shape=(nr,45))
  return sparse.hstack([a,f,v],format='csr')
 def ray(self,b,v):
  v=np.asarray(v);v=v/np.linalg.norm(v);a=np.zeros(self.nv)
  if b<6:a[self.os[b]:self.os[b+1]]=vec(np.outer(v,v))
  elif b<11:
   f=self.fb[b-6];q=np.bincount(f['orbit'],weights=v[f['ii']]*v[f['jj']],minlength=len(f['counts']))/f['counts']
   a[self.oldnv+self.fs[b-6]:self.oldnv+self.fs[b-5]]=q
  else:a[-45:]=vec(np.outer(v,v))
  return a
 def matrix(self,x,b):
  if b<6:return unpack(x[self.os[b]:self.os[b+1]],self.dims[b])
  if b<11:return x[self.oldnv+self.fs[b-6]:self.oldnv+self.fs[b-5]][self.fb[b-6]['pairmap']]
  return unpack(x[-45:],9)
 def moment(self,m,b):
  if b<6:M=unpack(m[self.os[b]:self.os[b+1]],self.dims[b]);return (M+np.diag(np.diag(M)))/2
  if b<11:
   f=self.fb[b-6];z=m[self.oldnv+self.fs[b-6]:self.oldnv+self.fs[b-5]]/f['ordered_counts'];return z[f['pairmap']]
  M=unpack(m[-45:],9);return (M+np.diag(np.diag(M)))/2
 def warm(self):
  old=np.load(P/'full_flags_best.npz');xold=old['x']; x=np.zeros(self.nv);x[:self.oldnv]=xold[:self.oldnv];x[-45:]=xold[-45:]
  f=self.fb[0];codes=f['valid'];canonical=codes[f['perms'].min(axis=0)];unique=sorted(set(canonical));ind={v:i for i,v in enumerate(unique)};idx=np.array([ind[c] for c in canonical]);assert len(unique)==45
  qe=unpack(xold[self.oldnv:self.oldnv+1035],45)[np.ix_(idx,idx)]
  x[self.oldnv:self.oldnv+self.fs[1]]=np.bincount(f['orbit'],weights=qe[f['ii'],f['jj']])/f['counts'];return x
if __name__=='__main__':
 import time
 M=Model();t=time.time();x=M.warm();v=M.evaluate(x);print('warm max',v.max(),'seconds',time.time()-t,'dims',M.dims,'coordinates',M.nv,flush=True)
 rng=np.random.default_rng(4);rows=rng.choice(M.N,200);A=M.amat(rows);print('row error',np.max(np.abs(v[rows]-(M.dd[rows]+A@x))))
 for b in range(12):
  ray=M.ray(b,rng.normal(size=M.dims[b]));p=rng.uniform(size=len(rows));mom=A.T@p;ev=np.linalg.eigvalsh(M.matrix(ray,b));
  vv=rng.normal(size=M.dims[b]);vv/=np.linalg.norm(vv);ray=M.ray(b,vv);print('b',b,'eig',ev[0],'dual error',float(mom@ray-vv@M.moment(mom,b)@vv))
 np.savez(P/'warm_12.npz',x=x)
