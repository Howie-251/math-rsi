#!/usr/bin/env python3
"""Portable, standard-library-only exact Q4 checker. Never runs optimization."""
from pathlib import Path
from fractions import Fraction
import argparse,hashlib,json,os,shutil,subprocess,tempfile,time

ROOT=Path(__file__).resolve().parents[1]
def require(condition,message):
    if not condition:raise ValueError(message)
def prepare(out):
    p=ROOT/'certificate_final_q4'
    raw=(p/'certificate_control.json').read_bytes();c=json.loads(raw)
    dims=[240,212,190,187,170,9]
    require(c['dimensions']==dims and len(c['gram_factors'])==6,'Expected exactly the six Q4 Gram blocks')
    require(c['q5_cuts']==[],'Q5 cuts are forbidden in this Q4-only entry point')
    require(c['face_root_masks']==[0,1,3,6,7],'Wrong root masks')
    D=c['gram_denominator'];require(type(D) is int and D>0,'Invalid denominator')
    mats=[]
    for n,L in zip(dims,c['gram_factors']):
        require(len(L)==n and len(L[0])>0 and all(len(row)==len(L[0]) for row in L),'Invalid factor shape')
        require(all(type(a) is int for row in L for a in row),'Factors must be integers')
        mats.append([[sum(a*b for a,b in zip(L[i],L[j])) for j in range(n)] for i in range(n)])
    safe=192*(D*D+sum(max(abs(a) for row in Q for a in row) for Q in mats))
    require(safe<2**63,'64-bit arithmetic safety failed')
    bound=Fraction(c['upper_numerator'],c['upper_denominator'])
    require(bound==Fraction(23662061277957791,40000000000000000),'Unexpected final bound')
    require(bound<=Fraction(c['upper_decimal_ceil_8'])<bound+Fraction(1,10**8),'Invalid outward decimal')
    den=192*D*D;target=bound*den
    require(target.denominator==1,'Bound does not have the local integer denominator')
    require(c['exact_local_numerator']==target.numerator and c['exact_local_denominator']==den,'Local maximum metadata mismatch')
    with (out/'verification_matrices.txt').open('w',encoding='ascii') as f:
        f.write(f'{D} {target.numerator} {den}\n')
        for Q in mats:
            f.write(str(len(Q))+'\n'+'\n'.join(' '.join(map(str,row)) for row in Q)+'\n')
    shutil.copy2(p/'keys.bin',out/'keys.bin')
    mf=max(Fraction(mats[b][i][i],D*D) for b in range(5) for i in range(dims[b]))
    mv=max(Fraction(mats[5][i][i],D*D) for i in range(9))
    require(mf==Fraction(1288810336780277,1250000000000000),'Face diagonal constant mismatch')
    require(mv==Fraction(324664893404033,625000000000000),'Vertex diagonal constant mismatch')
    print('CERTIFICATE_SHA256',hashlib.sha256(raw).hexdigest(),flush=True)
    print('PASS: exactly six integer Gram blocks, zero Q5 cuts, PSD by LL^T, 64-bit safety.',flush=True)
    print('EXACT_BOUND',bound,'OUTWARD',c['upper_decimal_ceil_8'],flush=True)
    print('FINITE_DIMENSION_CONSTANTS M_F=',mf,'M_v=',mv,flush=True)
    return p
def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--compiler',help='Existing g++ or clang++ executable; defaults to CXX or PATH')
    ap.add_argument('--work-dir',type=Path,help='Keep generated matrices and executable here; otherwise use a temporary directory')
    ap.add_argument('--prepare-only',action='store_true',help='Check factors and constants only; NOT a complete local certificate verification')
    a=ap.parse_args();start=time.time()
    temp=None
    if a.work_dir:
        out=a.work_dir.resolve();out.mkdir(parents=True,exist_ok=True)
    else:
        temp=tempfile.TemporaryDirectory(prefix='erdos86_q4_');out=Path(temp.name)
    try:
        p=prepare(out)
        if a.prepare_only:
            print('PREPARATION ONLY: full-domain C++ enumeration has not been run.');return
        compiler=a.compiler or os.environ.get('CXX') or shutil.which('g++') or shutil.which('clang++')
        require(bool(compiler),'Set --compiler to an existing C++17 g++/clang++ executable, or set CXX')
        exe=out/('verify_q4.exe' if os.name=='nt' else 'verify_q4')
        command=[compiler,'-O3','-std=c++17','-UNDEBUG',str(p/'verify_local.cpp'),'-o',str(exe)]
        print('COMPILE',json.dumps(command),flush=True)
        subprocess.run(command,check=True)
        subprocess.run([str(exe),'verification_matrices.txt'],cwd=out,check=True)
        print('FULL_DOMAIN_VERIFICATION_PASS elapsed_seconds=',round(time.time()-start,3),flush=True)
        print('Asymptotic Q4 certificate only; see the averaging proof for the n-dependent correction.',flush=True)
    finally:
        if temp:temp.cleanup()
if __name__=='__main__':main()
