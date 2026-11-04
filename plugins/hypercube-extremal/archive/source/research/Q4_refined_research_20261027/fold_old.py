"""Absorb the six partial-observation blocks into full face-root PSD blocks.
This is a positive linear transformation (an average of Gram pullbacks).
It preserves the local score on every complete Q4, not merely in expectation.
"""
from model import Model,P
import numpy as np,json
from sdp_core import vec
edges=[(0,1),(0,2),(1,3),(2,3)];ei={e:i for i,e in enumerate(edges)}
tr=[]
for sw in range(2):
 for t in range(4):
  vm=[t^(((x&1)<<1)|((x&2)>>1) if sw else x) for x in range(4)]
  em=[ei[tuple(sorted((vm[u],vm[v])))] for u,v in edges]
  rm=np.array([sum(((r>>e)&1)<<em[e] for e in range(4)) for r in range(16)])
  sm=np.array([sum(((s>>v)&1)<<vm[v] for v in range(4))+sum(((s>>(e+4))&1)<<(em[e]+4) for e in range(4)) for s in range(256)])
  tr.append((rm,sm))
def fold(M,x):
 out=x.copy();out[:M.oldnv]=0;old=[M.matrix(x,b) for b in range(6)]
 for b,r in enumerate(M.roots):
  f=M.fb[b];states=f['valid'];Q=M.matrix(x,b+6).copy()
  for rm,sm in tr:
   rr=int(rm[r]);s=sm[states];sa=(s&1)+((s>>1)&1)*2+((s>>4)&1)*4
   sb=((s>>2)&1)+((s>>3)&1)*2+((s>>7)&1)*4
   tc=s&3;r0=rr&1;r1=(rr>>3)&1
   if r0+r1==0:k=3;ss=sa*8+sb
   elif r0+r1==2:k=5;ss=sa*7+sb
   elif r0==0:k=4;ss=sa*7+sb
   else:k=4;ss=sb*7+sa
   Q+=(old[r0][np.ix_(sa,sa)]+old[2][np.ix_(tc,tc)]+old[k][np.ix_(ss,ss)])/8
  z=np.bincount(f['orbit'],weights=Q[f['ii'],f['jj']])/f['counts'];out[M.oldnv+M.fs[b]:M.oldnv+M.fs[b+1]]=z
 return out
if __name__=='__main__':
 M=Model();x=np.load(P/'smooth_best.npz')['x'];y=fold(M,x);a=M.evaluate(x);b=M.evaluate(y);e=float(np.max(np.abs(a-b)));print('Full local identity error over',M.N,'graphs:',e,flush=True);assert e<1e-12
 np.savez(P/'folded_warm.npz',x=y,upper=float(b.max()))
 (P/'folding_audit.json').write_text(json.dumps({'complete_representatives':M.N,'max_absolute_error':e,'before':float(a.max()),'after':float(b.max()),'remaining_nonzero_block_dimensions':[240,212,190,187,170,9]},indent=2))
