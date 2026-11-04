from pathlib import Path
import json,numpy as np
from model import Model,P
from sdp_core import vec
c=json.loads((P/'certificate.json').read_text());D=c['gram_denominator'];M=Model();x=np.zeros(M.nv);qs=[]
for j,L in enumerate(c['gram_factors']):
 L=np.array(L,dtype=float)/D;q=L@L.T
 if j<5:
  f=M.fb[j];z=np.bincount(f['orbit'],weights=q[f['ii'],f['jj']],minlength=len(f['counts']))/f['counts'];x[M.oldnv+M.fs[j]:M.oldnv+M.fs[j+1]]=z;q=z[f['pairmap']]
 else:x[-45:]=vec(q)
 qs.append(q)
base=float(M.evaluate(x).max());abl={}
for j,label in [(0,'remove_empty_block'),(5,'remove_vertex_block')]:
 z=x.copy()
 if j<5:z[M.oldnv+M.fs[j]:M.oldnv+M.fs[j+1]]=0
 else:z[-45:]=0
 abl[label]=float(M.evaluate(z).max())
z=x.copy()
for j in range(5):
 f=M.fb[j];group=f['perms'];B=np.zeros_like(qs[j])
 for pm in group:B[np.arange(len(pm)),pm]+=1/len(group)
 q=B@qs[j]@B;z[M.oldnv+M.fs[j]:M.oldnv+M.fs[j+1]]=np.bincount(f['orbit'],weights=q[f['ii'],f['jj']],minlength=len(f['counts']))/f['counts']
abl['project_each_flag_separately_all_faces']=float(M.evaluate(z).max())
f=M.fb[0];ids=[list(f['valid']).index(i) for i in [1,2,8]]
out=dict(certified_value=float(c['upper_numerator']/c['upper_denominator']),floating_recheck=base,max_face_diagonal=max(float(np.diag(q).max()) for q in qs[:5]),max_vertex_diagonal=float(np.diag(qs[-1]).max()),block_traces=[float(np.trace(q)) for q in qs],block_min_eigenvalues_float=[float(np.linalg.eigvalsh(q)[0]) for q in qs],empty_connector_sample_codes=[1,2,8],empty_connector_sample_matrix=qs[0][np.ix_(ids,ids)].tolist(),fixed_certificate_ablations=abl,warning='Ablations keep every other matrix fixed. They are not reoptimized bounds or optimal-value comparisons.')
(P/'final_metrics.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
