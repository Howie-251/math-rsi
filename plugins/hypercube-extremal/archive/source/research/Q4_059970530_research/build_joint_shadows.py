from pathlib import Path
import numpy as np,subprocess,time,json
P=Path(__file__).resolve().parent;z=np.load(P/'base_data.npz');keys=np.load(P/'full_meta.npz')['keys'];st=time.time()
idx=np.full(1<<24,-1,dtype=np.int32);a=keys//4096;b=keys%4096;rows=np.arange(len(keys),dtype=np.int32)
for tr in z['trans']:
 aa=tr[a];bb=tr[b];idx[aa*4096+bb]=rows;idx[bb*4096+aa]=rows
assert int((idx>=0).sum())==2902**2
idx.tofile(P/'pair_index.bin')
print('Pair lookup generated',time.time()-st,flush=True)
subprocess.run(['g++','-O3','-std=c++17',str(P/'joint_shadows.cpp'),'-o',str(P/'joint_shadows')],check=True)
subprocess.run([str(P/'joint_shadows')],cwd=P,check=True)
s=np.fromfile(P/'joint_shadows.bin',dtype=np.int32).reshape(-1,4)
np.save(P/'joint_shadows.npy',s)
from scipy import sparse
E=sparse.load_npz(P/'full_eq.npz');bad=0
for start in range(0,len(s),10000):
 rows=s[start:start+10000];T=E[rows[:,0]]+E[rows[:,1]]+E[rows[:,2]]+E[rows[:,3]];T.eliminate_zeros();bad+=T.nnz
assert bad==0
meta=np.load(P/'full_meta.npz');old=np.load(P/'warm_best.npz');C=sparse.load_npz(P/'full_C.npz')
v=meta['d']+C@old['x']/96
vals=v[s].mean(axis=1)
result={'joint_shadow_types':len(s),'old_certificate_partial_upper':float(old['upper']),'old_matrices_joint_upper':float(vals.max()),'exchange_identity_nonzeros':bad,'seconds':time.time()-st}
(P/'joint_shadow_summary.json').write_text(json.dumps(result,indent=2));print(result,flush=True)
