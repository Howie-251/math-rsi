"""Round PSD Gram factors, then find and reverify the exact exhaustive bound.
No floating-point bound is accepted as a certificate.
"""
from pathlib import Path
from fractions import Fraction
import json,numpy as np,subprocess,re,argparse,hashlib,time
from model import Model,P
ap=argparse.ArgumentParser();ap.add_argument('--input',default='adaptive_best.npz');ap.add_argument('--out',default='certificate.json');args=ap.parse_args()
M=Model();data=np.load(P/args.input);x=data['x'];D=10**7;grams=[];mats=[];ab=D*D
assert np.max(np.abs(x[:M.oldnv]))==0
for b,n in enumerate(M.dims[6:]):
 q=M.matrix(x,b+6);w,U=np.linalg.eigh(q);keep=w>1e-12
 L=np.rint((U[:,keep]*np.sqrt(w[keep]))*D).astype(np.int64);L=L.tolist()
 if not np.any(keep):L=[[0] for _ in range(n)]
 Q=[[sum(a*b for a,b in zip(L[i],L[j])) for j in range(n)] for i in range(n)];grams.append(L);mats.append(Q);ab+=max(abs(z) for row in Q for z in row)
assert 192*ab<2**63
matpath=P/'certification_matrices.txt';den=192*D*D
with matpath.open('w') as f:
 f.write(f'{D} -1 {den}\n')
 for Q in mats:
  f.write(str(len(Q))+'\n');f.write('\n'.join(' '.join(map(str,row)) for row in Q)+'\n')
res=subprocess.run([str(P/'verify_six'),str(matpath)],cwd=P,check=True,capture_output=True,text=True);print(res.stdout,flush=True)
num=int(re.search(r'EXACT_MAX (\d+)',res.stdout).group(1));frac=Fraction(num,den);worst=int(re.search(r'WORST_GRAPH (\d+)',res.stdout).group(1));ceil=(num*10**8+den-1)//den
c={'description':'Full-Q4 local certificate with all five full face-root types, preserving relative flag orientation by simultaneous stabilizer averaging. Asymptotic C4-free hypercube density bound, not a finite-Q8 bound.','dimensions':list(map(int,M.dims[6:])),'gram_denominator':D,'gram_factors':grams,'face_root_masks':[0,1,3,6,7],'upper_numerator':frac.numerator,'upper_denominator':frac.denominator,'upper_decimal_ceil_8':f'{ceil/10**8:.8f}','exact_local_numerator':num,'exact_local_denominator':den,'worst_graph':worst,'rounding_source':args.input,'floating_upper_before_rounding':float(data['upper'])}
(P/args.out).write_text(json.dumps(c,ensure_ascii=False,separators=(',',':')))
(P/(args.out+'.log')).write_text(res.stdout+'\nCERTIFIED: '+str(frac)+'\nDECIMAL: '+c['upper_decimal_ceil_8']+'\n')
print('CERTIFIED',frac,float(frac),c['upper_decimal_ceil_8'],flush=True)
