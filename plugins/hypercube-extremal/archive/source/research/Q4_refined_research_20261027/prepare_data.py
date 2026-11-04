"""Rebuild geometric indexing from the supplied, exhaustively audited keys.bin.
NumPy only. This is for optional optimization reproduction, not certificate checking.
"""
from pathlib import Path
from itertools import permutations
import numpy as np
P=Path(__file__).resolve().parent
edges=[(x,x^(1<<i)) for x in range(8) for i in range(3) if not(x>>i&1)]
np.array(edges,dtype=np.int32).tofile(P/'edges.bin')
ei={tuple(sorted(e)):j for j,e in enumerate(edges)}
tr=[]
for per in permutations(range(3)):
 for t in range(8):
  vm=[t^sum(((x>>j)&1)<<per[j] for j in range(3)) for x in range(8)]
  em=[ei[tuple(sorted((vm[u],vm[v])))] for u,v in edges]
  a=np.zeros(4096,dtype=np.int32)
  for e in range(12):a|=((np.arange(4096,dtype=np.int32)>>e)&1)<<em[e]
  tr.append(a)
tr=np.array(tr);keys=np.fromfile(P/'keys.bin',dtype=np.int32);assert len(keys)==90179
idx=np.full(1<<24,-1,dtype=np.int32)
for h,key in enumerate(keys):
 a,b=divmod(int(key),4096);z=tr[:,a]*4096+tr[:,b];w=tr[:,b]*4096+tr[:,a]
 assert min(z.min(),w.min())==key
 assert np.all((idx[z]<0)|(idx[z]==h)) and np.all((idx[w]<0)|(idx[w]==h))
 idx[z]=h;idx[w]=h
idx.tofile(P/'pair_index.bin')
canon=lambda s:min(s,((s&1)<<1)|((s&2)>>1)|((s&4)<<1)|((s&8)>>1))
reps=sorted({canon(s) for s in range(15)});assert len(reps)==9
vc=np.array([reps.index(canon(s)) for s in range(15)]+[-1],dtype=np.int32);vc.tofile(P/'vertex_flag_codes.bin')
print('Prepared Q3 indexing and vertex flags. Full coverage is independently checked by verify_six.cpp.')
