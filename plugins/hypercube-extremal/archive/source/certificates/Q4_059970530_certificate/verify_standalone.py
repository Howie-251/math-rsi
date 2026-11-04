#!/usr/bin/env python3
"""Check the rational PSD certificate without any SDP solver or precomputed coefficient table.
Requires Python >=3.10 and a C++17 compiler. No NumPy/SciPy dependency.
Reads only certificate.json and keys.bin, then reconstructs all local objects.
"""
from pathlib import Path
from fractions import Fraction
import json,subprocess,shutil,sys
P=Path(__file__).resolve().parent
c=json.loads((P/(sys.argv[1] if len(sys.argv)>1 else 'certificate.json')).read_text());D=int(c['gram_denominator']);assert c['dimensions']==[8,7,4,64,56,49,45,9]
mat=[]
for n,L in zip(c['dimensions'],c['gram_factors']):
 assert len(L)==n and len({len(row) for row in L})==1
 assert all(isinstance(x,int) for row in L for x in row)
 # An integer Gram matrix is exactly PSD, including in rank-deficient cases.
 Q=[[sum(a*b for a,b in zip(L[i],L[j])) for j in range(n)] for i in range(n)];mat.append(Q)
bound=384*(D*D+sum(max(abs(x) for row in Q for x in row) for Q in mat));assert bound<2**63
ub=Fraction(int(c['upper_numerator']),int(c['upper_denominator']));den=384*D*D;num=ub*den;assert num.denominator==1
with (P/'verification_matrices.txt').open('w') as f:
 f.write(f'{D} {num.numerator} {den}\n')
 for Q in mat:
  f.write(str(len(Q))+'\n')
  for row in Q:f.write(' '.join(map(str,row))+'\n')
print('PASS: 8 PSD blocks reconstructed as exact integer Gram matrices.',flush=True)
print('PASS: rigorous absolute integer bound excludes 64-bit overflow.',flush=True)
compiler=shutil.which('g++') or shutil.which('clang++')
if not compiler:raise RuntimeError('A C++17 compiler (g++ or clang++) is required.')
subprocess.run([compiler,'-O3','-std=c++17',str(P/'verify_direct.cpp'),'-o',str(P/'verify_direct')],check=True)
subprocess.run([str(P/'verify_direct'),'verification_matrices.txt'],cwd=P,check=True)
print('CERTIFIED ASYMPTOTIC DENSITY UPPER BOUND:',ub,flush=True)
print('OUTWARD DECIMAL:',c['upper_decimal_ceil_8'],flush=True)
print('This verifies the finite local certificate. The high-dimensional averaging proof is stated in the report; this is not a Lean formalization.',flush=True)
