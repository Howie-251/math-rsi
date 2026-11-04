"""Complete Q2-root/Q3 flags, preserving relative orientation of the two flags.
A flag state s = connector_mask + 16 * translated_square_mask.
No local information is lost by simultaneous orbit reduction of flag PAIRS.
"""
from pathlib import Path
import numpy as np, json
P=Path(__file__).resolve().parent
edges=[(0,1),(0,2),(1,3),(2,3)];ei={x:i for i,x in enumerate(edges)}
trans=[]
for p in [(0,1),(1,0)]:
 for t in range(4):
  vm=[t^sum(((x>>j)&1)<<p[j] for j in range(2)) for x in range(4)]
  em=[ei[tuple(sorted((vm[x],vm[y])))] for x,y in edges]
  cm=np.array([sum(((m>>x)&1)<<vm[x] for x in range(4)) for m in range(16)])
  fm=np.array([sum(((m>>x)&1)<<em[x] for x in range(4)) for m in range(16)])
  sm=np.array([cm[s&15]+16*fm[s>>4] for s in range(256)])
  trans.append((fm,sm))
roots=sorted({min(int(f[r]) for f,s in trans) for r in range(15)})
blocks=[];lookup=np.full((16,256,256),-1,dtype=np.int32); starts=[0]
for r in roots:
 valid=[]
 for s in range(240):
  con=s&15;top=s>>4
  if all(not((r>>e&1) and (top>>e&1) and(con>>u&1)and(con>>v&1)) for e,(u,v) in enumerate(edges)): valid.append(s)
 valid=np.array(valid,dtype=np.int32);vi={int(s):i for i,s in enumerate(valid)}
 perms=np.array([[vi[int(sm[s])] for s in valid] for fm,sm in trans if fm[r]==r],dtype=np.int32)
 n=len(valid); ii,jj=np.triu_indices(n);canon=np.minimum(ii[:,None]*n+jj[:,None],jj[:,None]*n+ii[:,None]).min(axis=1)
 canon=ii*n+jj
 for perm in perms:
  a=perm[ii];b=perm[jj];canon=np.minimum(canon,np.minimum(a,b)*n+np.maximum(a,b))
 cr,orb=np.unique(canon,return_inverse=True);count=np.bincount(orb);pairmap=np.zeros((n,n),dtype=np.int32);pairmap[ii,jj]=orb;pairmap[jj,ii]=orb
 # q_j = mean of Q_ij over unordered pairs in its group orbit.
 ordered_count=np.bincount(pairmap.ravel(),minlength=len(cr))
 # lookup arbitrary root in this orbit via any fixed canonicalizing transform.
 for rr in range(15):
  possible=[(fm,sm) for fm,sm in trans if fm[rr]==r]
  if not possible:continue
  sm=possible[0][1]; vv=np.array([s for s in range(256) if int(sm[s]) in vi],dtype=np.int32)
  dest=np.array([vi[int(sm[s])] for s in vv])
  lookup[rr][np.ix_(vv,vv)]=pairmap[np.ix_(dest,dest)]+starts[-1]
 np.savez(P/f'face_block_{r}.npz',root=r,valid=valid,perms=perms,pairmap=pairmap,ii=ii,jj=jj,orbit=orb,counts=count,ordered_counts=ordered_count)
 # flags taken modulo stabilizer separately -- old weaker model
 single=np.min(perms,axis=0);coarse=len(set(single.tolist()))
 blocks.append(dict(root=int(r),dimension=n,group_size=len(perms),single_orbits=coarse,pair_orbits=len(cr)))
 starts.append(starts[-1]+len(cr))
lookup.tofile(P/'face_pair_lookup.bin')
np.savez(P/'face_orbit_meta.npz',roots=roots,starts=starts,dims=[b['dimension'] for b in blocks],lookup=lookup)
(P/'face_orbit_summary.json').write_text(json.dumps(blocks,indent=2))
print(blocks,'total pair orbit columns',starts[-1],flush=True)
