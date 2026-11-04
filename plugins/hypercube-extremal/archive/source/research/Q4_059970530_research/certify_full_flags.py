"""Round PSD matrices to exact rational Gram matrices; verify all stored exhaustive rows.
No floating eigenvalue is used as the final PSD test.
"""
from pathlib import Path
from fractions import Fraction
import numpy as np,json,time,io
from scipy import sparse
from sdp_core import pairs,unpack
P=Path(__file__).resolve().parent;z0=np.load(io.BytesIO((P/'full_flags_best.npz').read_bytes()));z={k:z0[k] for k in z0.files};dims=z['dims'];starts=z['starts'];D=10**7
# Retain this exact optimization snapshot.
np.savez(P/'certified_search_snapshot.npz',**z)
factors=[];q=[];mats=[];summaries=[]
for b,n in enumerate(dims):
 Q=unpack(z['x'][starts[b]:starts[b+1]],int(n));w,V=np.linalg.eigh(Q)
 F=V[:,w>1e-13]*np.sqrt(w[w>1e-13]);L=np.rint(F*D).astype(np.int64)
 # Python integers independently guarantee no overflow in Gram calculation.
 R=np.array([[sum(int(a)*int(b) for a,b in zip(L[i],L[j])) for j in range(n)] for i in range(n)],dtype=np.int64)
 assert np.array_equal(R,L@L.T)
 factors.append(L.tolist());q.extend(int(R[i,j]) for i,j in pairs(n));mats.append(R)
 summaries.append({'block':b,'dimension':int(n),'rank_factor_columns':L.shape[1],'trace':float(np.trace(R.astype(float))/D**2),'largest_diagonal':float(np.max(np.diag(R))/D**2)})
# Absolute triangle bound valid for every intermediate integer dot product and row sum.
absbound=384*(D**2+sum(int(np.max(np.abs(M))) for M in mats));assert absbound<2**63
q=np.array(q,dtype=np.int64);meta=np.load(P/'full_meta.npz');keys=meta['keys'];oldnv=int(meta['starts'][-1])
C=sparse.load_npz(P/'full_C.npz').astype(np.int64)
pn=np.array([4*(int(k//4096).bit_count()+int(k%4096).bit_count())*D**2 for k in keys],dtype=np.int64)+C@q[:oldnv]
F=sparse.csr_matrix((np.memmap(P/'new_flags_vals.bin',dtype=np.int16,mode='r'),np.memmap(P/'new_flags_cols.bin',dtype=np.int32,mode='r'),np.memmap(P/'new_flags_ptr.bin',dtype=np.int64,mode='r')),shape=(3312331,1080))
sh=np.load(P/'full_flags_shadows.npy');vals=pn[sh].sum(axis=1)+8*(F@q[oldnv:]);worst=int(vals.argmax());num=int(vals[worst]);den=384*D**2;ub=Fraction(num,den);ceil8=(num*10**8+den-1)//den
cert={'description':'Computer-assisted asymptotic C4-free hypercube upper certificate; exhaustive full-Q4 completion consistency; eight exact Gram blocks; not a proof of SDP optimality', 'gram_denominator':D,'dimensions':list(map(int,dims)),'gram_factors':factors,'upper_numerator':str(ub.numerator),'upper_denominator':str(ub.denominator),'common_numerator':str(num),'common_denominator':str(den),'upper_decimal_ceil_8':f'{ceil8/1e8:.8f}','representatives_checked':len(sh),'partial_types':len(keys),'worst_representative_row':worst,'worst_graph_code':str(int(np.load(P/'full_flags_graphs.npy')[worst])),'safe_integer_absolute_bound':str(absbound),'matrix_summaries':summaries,'numerical_search_upper':float(z['upper']),'iteration':int(z['iteration'])}
(P/'certificate.json').write_text(json.dumps(cert,separators=(',',':')))
# Matrices used by independent C++ checker; factors in JSON remain the authoritative PSD witness.
with open(P/'exact_matrices.txt','w') as f:
 f.write(f'{D} {num} {den}\n')
 for M in mats:
  f.write(str(len(M))+'\n')
  for row in M:f.write(' '.join(map(str,row))+'\n')
for b,M in enumerate(mats):np.savetxt(P/f'matrix_{b}_{len(M)}x{len(M)}.txt',M.astype(float)/D**2,fmt='%.14g')
print(json.dumps({k:v for k,v in cert.items() if k!='gram_factors'},indent=2),flush=True)
print('EXACT CERTIFICATE',ub,float(ub),'outward',cert['upper_decimal_ceil_8'],flush=True)
