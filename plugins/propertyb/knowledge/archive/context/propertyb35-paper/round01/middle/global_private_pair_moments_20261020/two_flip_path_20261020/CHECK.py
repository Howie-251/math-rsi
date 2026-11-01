#!/usr/bin/env python3
"""Small color-type and exact arithmetic checks. Never generates a hypergraph."""
from fractions import Fraction as F
from math import comb
from itertools import product
from pathlib import Path
import importlib.util
import json
import time

ROOT=Path(__file__).resolve().parent

def C(n,r):
    return comb(n,r) if 0<=r<=n else 0

def encode(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [encode(v) for v in x]
    return x

def local_checks():
    cases=0
    # g originally red (1), h originally blue (0); every tested edge starts proper.
    for k in range(2,7):
        for hasg,hash in product((0,1),repeat=2):
            for other in product((0,1),repeat=k-hasg-hash):
                original=([1] if hasg else [])+([0] if hash else [])+list(other)
                after=([0] if hasg else [])+([1] if hash else [])+list(other)
                if len(set(original))<2: continue
                newmono=len(set(after))==1
                classification=(hasg and not hash and all(v==0 for v in other)) or (
                    hash and not hasg and all(v==1 for v in other))
                assert newmono==classification
                cases+=1
        # G remains proper; its unique private F remains proper after flipping g,h.
        assert len(set([0]+[1]*(k-1)))==2
        assert len(set([0,1]+[0]*(k-2)))==2
        for multiplicities in product(range(1,5),repeat=k):
            S=sum(multiplicities)
            unique=multiplicities.count(1)
            assert unique>=2*k-S
            Z=(k-1)*unique
            assert F(1,2)+(F(S)+F(Z,k-1))/(4*k)>=1
    return cases

def parameters(n,Delta):
    a=n//2;den=C(n,a)
    p=F(C(n-5,a-5)+C(n-5,a),den)
    q=F(C(n-9,a-5)+C(n-9,a-4),den)
    r=[F(C(n-13+j,a-9+j)+C(n-13+j,a-4),den) for j in range(5)]
    caps=[min(33,(5-j)*(Delta-1)) for j in range(5)]
    # The condition is sum(coeff_j*n_j) < rhs.
    coeff=[F(caps[j],2)*r[j]+(2*q if j==1 else 0) for j in range(5)]
    rhs=10*(2-35*p)
    return dict(n=n,Delta=Delta,a=a,p=p,q=q,r=r,caps=caps,coeff=coeff,rhs=rhs)

def main():
    started=time.process_time()
    cases=local_checks()
    p21=parameters(21,9);p22=parameters(22,9);p23=parameters(23,8)
    assert p21['p']==p22['p'] and p21['q']==p22['q'] and p21['r']==p22['r']
    D=352716
    assert [x*D for x in p21['r']]==[36,120,330,792,1716]
    assert [x*D for x in p21['coeff']]==[594,5352,3960,6336,6864]
    assert p21['rhs']*D==2722720
    L=[594,5352,3960,6336,6864]
    base=87*L[0]+368*L[1]+140*L[2]
    n3=-L[0]+3*L[1]-3*L[2]+L[3]
    n4=-3*L[0]+8*L[1]-6*L[2]+L[4]
    tau=L[0]-2*L[1]+L[2]
    assert [base,n3,n4,tau]==[2575614,9918,24138,-6150]
    old=[78,397,110,9,1]
    assert sum(a*b for a,b in zip(L,old))==2670564<2722720
    coeff23=[x*2*C(23,11) for x in p23['coeff']]
    assert coeff23==[5445,39600,27027,42042,45045]
    assert p23['rhs']*2*C(23,11)==18811520
    spec=importlib.util.spec_from_file_location('previous_exact_kernel',ROOT.parent/'CHECK.py')
    previous=importlib.util.module_from_spec(spec);spec.loader.exec_module(previous)
    witnesses=[]
    for par,W,hist in [(p21,648,[72,413,95,15,0]),(p23,581,[105,403,85,0,2])]:
        n=par['n'];rows=previous.kernels(n)
        assert sum(hist)==595 and sum(j*hist[j] for j in range(5))==W
        T=sum(C(j,2)*hist[j] for j in range(5))
        assert T>=350-C(n,2)
        assert 2*hist[1]*par['q']>=5*(2-35*par['p'])
        gap=sum(hist[j]*par['coeff'][j] for j in range(5))-par['rhs']
        psd=[35*row[5]+2*sum(hist[j]*row[j] for j in range(5)) for row in rows]
        assert gap>=0 and all(x>=0 for x in psd)
        witnesses.append(dict(n=n,Delta=par['Delta'],W=W,T=T,histogram=hist,
                              new_necessary_gap=gap,PSD_quadratic_forms=psd))
    out=dict(status='PASS',local_proper_edge_color_types_checked=cases,
             multiplicity_vectors_scope='k2..6, each private multiplicity1..4',
             parameters=[p21,p22,p23],A1_substitution=[base,n3,n4,tau],
             old_A1_integer_witness_L=2670564,A1_necessary_RHS=2722720,
             abstract_PSD_feasible_witnesses=witnesses,
             CPU_seconds=time.process_time()-started)
    (ROOT/'CHECK.json').write_text(json.dumps(encode(out),indent=2)+'\n')
    print(f'PASS {cases} local proper-edge color types; exact 21/22/23 arithmetic; two PSD distributions')
    print(f'CPU {out["CPU_seconds"]:.6f}s')
if __name__=='__main__': main()
