from pathlib import Path
import numpy as np,itertools,time,json
P=Path(__file__).resolve().parent
z=np.load(P/'completion_features.npz');ptr=z['ptr'];f=z['features'].astype(np.int16)
w=np.array([x for x in itertools.product((-1,0,1),repeat=4) if any(x)],dtype=np.int16)
U=np.empty((len(ptr)-1,len(w)),dtype=np.int16);st=time.time()
for j,v in enumerate(w):
 U[:,j]=np.maximum.reduceat(f@v,ptr[:-1])
np.savez_compressed(P/'completion_support.npz',weights=w,U=U)
print('SUPPORT',U.shape,'negative entries',int((U<0).sum()),'minima',U.min(axis=0).tolist(),'sec',time.time()-st,flush=True)
