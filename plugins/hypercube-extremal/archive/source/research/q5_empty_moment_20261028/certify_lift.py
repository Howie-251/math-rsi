"""Round and certify the joint PSD + compressed-Q5 candidate."""
from pathlib import Path
from fractions import Fraction
import json,sys,subprocess,re,shutil,argparse
import numpy as np
P=Path(__file__).resolve().parent
BASE=P.parent/'optimization_20261028_q4'
sys.path.insert(0,str(BASE))
from model import Model
from verify_q5 import prepare
ap=argparse.ArgumentParser();ap.add_argument('--input',default='lift_best.npz');args=ap.parse_args()
M=Model();z=np.load(P/args.input);x=z['x_psd'];weights=z['weights']
cuts=[dict(labels=row.tolist()) for row in z['labels']] if 'labels' in z else json.loads((P/'selected_cuts.json').read_text())
D=5*10**7;grams=[]
assert np.max(np.abs(x[:M.oldnv]))==0 and np.all(weights>=0)
for b,n in enumerate(M.dims[6:]):
    q=M.matrix(x,b+6);w,U=np.linalg.eigh(q);keep=w>1e-12
    L=np.rint(U[:,keep]*np.sqrt(w[keep])*D).astype(np.int64).tolist()
    if not np.any(keep):L=[[0] for _ in range(n)]
    grams.append(L)
c=dict(proof_type='Q5_EMPTY_CUBIC_PARTITION_IDENTITY_V1',dimensions=list(map(int,M.dims[6:])),
       gram_denominator=D,gram_factors=grams,face_root_masks=[0,1,3,6,7],
       q5_cuts=[dict(labels=cut['labels'],weight_numerator=int(round(float(w)*D*D)))
                for cut,w in zip(cuts,weights) if w>0],
       floating_upper_before_rounding=float(z['upper']))
shutil.copy2(BASE/'keys.bin',P/'keys.bin')
shutil.copy2(BASE/'verify_six.cpp',P/'verify_local.cpp')
matrices=prepare(c,P/'certification_matrices.txt',-1)
compiler=shutil.which('g++') or shutil.which('clang++');assert compiler
subprocess.run([compiler,'-O3','-std=c++17',str(P/'verify_local.cpp'),'-o',str(P/'verify_local')],check=True)
r=subprocess.run([str(P/'verify_local'),'certification_matrices.txt'],cwd=P,check=True,capture_output=True,text=True)
print(r.stdout,flush=True)
num=int(re.search(r'EXACT_MAX (\d+)',r.stdout).group(1));den=192*D*D;bound=Fraction(num,den)
c.update(upper_numerator=bound.numerator,upper_denominator=bound.denominator,
         upper_decimal_ceil_8=f'{((num*10**8+den-1)//den)/10**8:.8f}',
         exact_local_numerator=num,exact_local_denominator=den,
         worst_graph=int(re.search(r'WORST_GRAPH (\d+)',r.stdout).group(1)))
(P/'certificate.json').write_text(json.dumps(c,separators=(',',':')),encoding='utf-8')
(P/'certification.log').write_text(r.stdout+'\nCERTIFIED '+str(bound)+'\n',encoding='utf-8')
total=z['x'];ablation=float(M.evaluate(x).max());eigs=np.linalg.eigvalsh(M.matrix(total,6))
mf=max(Fraction(matrices[b][i][i],D*D) for b in range(5) for i in range(len(matrices[b])))
mv=max(Fraction(matrices[5][i][i],D*D) for i in range(9))
report=dict(certified_bound=str(bound),certified_decimal=float(bound),
            outward_decimal=c['upper_decimal_ceil_8'],
            previous_q4_certified_bound='236634773493897/400000000000000',
            improvement_vs_previous=float(Fraction(236634773493897,400000000000000)-bound),
            below_059=bound<Fraction(59,100),cut_count=len(c['q5_cuts']),
            cut_weight_sum=float(weights.sum()),fixed_psd_remove_cuts_upper=ablation,
            total_empty_matrix_min_eig_float=float(eigs[0]),
            max_face_diagonal_bound=str(mf),max_vertex_diagonal_bound=str(mv),
            note='Ablation fixes old matrices; not a reoptimized comparison. New constraints are a compressed Q5 moment family, not full Q5 geometry.')
(P/'result.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2),flush=True)
