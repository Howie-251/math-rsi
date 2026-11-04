from pathlib import Path
from fractions import Fraction
import numpy as np,json
from scipy import sparse
from sdp_core import pairs,unpack
P=Path(__file__).resolve().parent;m=np.load(P/'full_meta.npz');C=sparse.load_npz(P/'full_C.npz').astype(np.int64);D=10**7
sh=np.load(P/'full_flags_shadows.npy');g=np.load(P/'full_flags_graphs.npy');counts=np.array([int(k//4096).bit_count()+int(k%4096).bit_count() for k in m['keys']],dtype=np.int64)
old=np.load(P/'joint_best.npz');factors=[];q=[]
for b,n in enumerate(m['dims']):
 Q=unpack(old['x'][m['starts'][b]:m['starts'][b+1]],n);w,V=np.linalg.eigh(Q);L=np.rint(V[:,w>1e-13]*np.sqrt(w[w>1e-13])*D).astype(np.int64);R=L@L.T;factors.append(L.tolist());q.extend(int(R[i,j]) for i,j in pairs(n))
factors.extend([[[] for _ in range(45)],[[] for _ in range(9)]])
v=4*counts*D**2+C@np.array(q,dtype=np.int64);s=v[sh].sum(axis=1);r=int(s.argmax());ub=Fraction(int(s[r]),384*D**2);ceil=(ub.numerator*10**8+ub.denominator-1)//ub.denominator
cert={'description':'Six-block control: full-Q4 joint completion but no new full-root PSD terms; feasible certificate, not optimality','gram_denominator':D,'dimensions':[8,7,4,64,56,49,45,9],'gram_factors':factors,'upper_numerator':str(ub.numerator),'upper_denominator':str(ub.denominator),'upper_decimal_ceil_8':f'{ceil/1e8:.8f}','representatives_checked':len(sh),'worst_graph_code':str(int(g[r]))}
(P/'certificate_six.json').write_text(json.dumps(cert,separators=(',',':')))
main=json.loads((P/'certificate.json').read_text());Q=[]
for n,L in zip(main['dimensions'],main['gram_factors']):
 L=np.array(L,dtype=np.int64).reshape(n,-1);R=L@L.T;Q.append(np.array([R[i,j] for i,j in pairs(n)],dtype=np.int64))
v=4*counts*D**2+C@np.concatenate(Q[:6]);v=v[sh].sum(axis=1)
F=sparse.csr_matrix((np.memmap(P/'new_flags_vals.bin',dtype=np.int16,mode='r'),np.memmap(P/'new_flags_cols.bin',dtype=np.int32,mode='r'),np.memmap(P/'new_flags_ptr.bin',dtype=np.int64,mode='r')),shape=(3312331,1080))
a=8*(F[:,:1035]@Q[6]);b=8*(F[:,1035:]@Q[7]);out={'six_block_control':str(ub),'six_block_control_decimal':float(ub),'six_block_control_ceil8':cert['upper_decimal_ceil_8'],'fixed_certificate_ablation':{}}
for label,x in [('complete',v+a+b),('empty45_zeroed',v+b),('vertex9_zeroed',v+a),('both_new_blocks_zeroed',v)]:
 u=Fraction(int(x.max()),384*D**2);out['fixed_certificate_ablation'][label]={'exact':str(u),'decimal':float(u)}
(P/'variant_audit.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
