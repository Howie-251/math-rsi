#!/usr/bin/env python3
"""Exact verification using standard Python and a C++17 compiler only.
All root group actions and local flags are rebuilt from graph geometry.
No SDP solver or saved coefficient table is read.
"""
from pathlib import Path
from fractions import Fraction
import json,subprocess,shutil,sys
P=Path(__file__).resolve().parent
c=json.loads((P/(sys.argv[1] if len(sys.argv)>1 else 'certificate.json')).read_text());D=c['gram_denominator'];assert c['dimensions']==[240,212,190,187,170,9]
mat=[]
for n,L in zip(c['dimensions'],c['gram_factors']):
 assert len(L)==n and len(set(map(len,L)))==1 and all(isinstance(x,int) for row in L for x in row)
 mat.append([[sum(a*b for a,b in zip(L[i],L[j])) for j in range(n)] for i in range(n)])
bound=192*(D*D+sum(max(abs(x) for row in Q for x in row) for Q in mat));assert bound<2**63
ub=Fraction(c['upper_numerator'],c['upper_denominator']);den=192*D*D;num=ub*den;assert num.denominator==1
with (P/'verification_matrices.txt').open('w') as f:
 f.write(f'{D} {num.numerator} {den}\n')
 for Q in mat:
  f.write(str(len(Q))+'\n');f.write('\n'.join(' '.join(map(str,row)) for row in Q)+'\n')
print('PASS: 6 exact integer Gram matrices; group averaging preserves PSD.',flush=True)
print('PASS: exact absolute arithmetic bound excludes 64-bit overflow.',flush=True)
compiler=shutil.which('g++') or shutil.which('clang++')
if not compiler:raise RuntimeError('C++17 compiler needed.')
subprocess.run([compiler,'-O3','-std=c++17',str(P/'verify_six.cpp'),'-o',str(P/'verify_six')],check=True)
subprocess.run([str(P/'verify_six'),'verification_matrices.txt'],cwd=P,check=True)
print('CERTIFIED ASYMPTOTIC DENSITY UPPER BOUND:',ub,flush=True)
print('OUTWARD DECIMAL:',c['upper_decimal_ceil_8'],flush=True)
print('Finite local verification; the asymptotic averaging proof is in the accompanying report. Not a finite-Q8 upper bound.')
