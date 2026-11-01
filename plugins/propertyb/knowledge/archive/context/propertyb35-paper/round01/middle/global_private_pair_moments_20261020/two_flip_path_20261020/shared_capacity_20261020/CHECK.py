#!/usr/bin/env python3
"""Exact shared-capacity arithmetic and import-scope audit. No H generation."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import importlib.util
import json
import time

ROOT=Path(__file__).resolve().parent
PROJECT=next(p for p in ROOT.parents if (p/'FORMAL_SPEC_PROPERTYB_35_PAPER.md').exists())

def enc(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [enc(v) for v in x]
    return x

def main():
    start=time.process_time()
    degrees=[6,7]+[8]*9+[9]*10
    W=sum(comb(d,2) for d in degrees)
    weighted=sum(d*comb(d,2) for d in degrees)
    assert len(degrees)==21 and sum(degrees)==175
    assert (W,weighted,9*W-weighted)==(648,5493,339)
    # C1 <=35*n1-[5493-9*(648-n1)]=26*n1+339.
    qnum=1716;rnum=[36,120,330,792,1716]
    capacities=[33,26,24,16,4]
    coeff=[F(capacities[j]*rnum[j],2)+(2*qnum if j==1 else 0)
           for j in range(5)]
    constant=F(339*rnum[1],2)
    assert coeff==[594,4992,3960,6336,3432] and constant==20340
    base=87*coeff[0]+368*coeff[1]+140*coeff[2]+constant
    c3=-coeff[0]+3*coeff[1]-3*coeff[2]+coeff[3]
    c4=-3*coeff[0]+8*coeff[1]-6*coeff[2]+coeff[4]
    ctau=coeff[0]-2*coeff[1]+coeff[2]
    assert (base,c3,c4,ctau)==(2463474,8838,17826,-5430)
    threshold=F(2722720)-base
    assert threshold==259246
    assert -(-threshold.numerator//6)*6==259248
    high=PROJECT/'context/propertyb35-paper/round01/middle/high_edge_intersection_repair_20261020'
    verified=json.loads((high/'VERIFY.json').read_text())
    discovered=json.loads((high/'RESULT.json').read_text())
    assert verified['status']=='PASS'
    gates=verified['imported_pair_gates']+discovered['extra_pair_gates']
    found={}
    for item in gates:
        ds=tuple(sorted(item['degrees']));c=item['codegree']
        bound=F(item['bound']);assert bound<1
        if ds==(9,9):assert item['strict']
        found[ds,c]=bound
    for ds,lower in [((7,8),4),((7,9),5),((8,8),5),((8,9),5),((9,9),5)]:
        for c in range(lower,min(ds)+1):assert (ds,c) in found
    assert len(found)==20
    hist=[F(17),F(1664,3),F(0),F(0),F(70,3)]
    Lprime=sum(hist[j]*coeff[j] for j in range(5))+constant
    assert Lprime==2879414 and Lprime>=2722720
    old=ROOT.parent.parent/'CHECK.py'
    spec=importlib.util.spec_from_file_location('first_exact_kernels',old)
    previous=importlib.util.module_from_spec(spec);spec.loader.exec_module(previous)
    psd=[35*row[5]+2*sum(hist[j]*row[j] for j in range(5))
         for row in previous.kernels(21)]
    assert all(x>=0 for x in psd)
    out=dict(status='PASS',W=W,degree_weighted_moment=weighted,
             shared_C1_linear_bound='26*n1+339',coefficients=coeff,constant=constant,
             A1_substitution=[base,c3,c4,ctau],unrounded_necessary_threshold=threshold,
             rounded_necessary_threshold=259248,
             import_scope='20 saved strict pair gates; saved independent VERIFY PASS; not rerun here',
             imported_pair_gates=[dict(degrees=list(ds),codegree=c,bound=b)
                                  for (ds,c),b in sorted(found.items())],
             old_max_n1_abstract_distribution=hist,Lprime=Lprime,
             PSD_quadratic_forms=psd,CPU_seconds=time.process_time()-start)
    (ROOT/'CHECK.json').write_text(json.dumps(enc(out),indent=2)+'\n')
    print(f'PASS shared C1/C4 arithmetic, 20-gate import-scope audit, old PSD witness; CPU {out["CPU_seconds"]:.6f}s')

if __name__=='__main__':main()
