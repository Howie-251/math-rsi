#!/usr/bin/env python3
"""Exact matched reference envelope for k=5..11; no hypergraph enumeration."""
import argparse
import importlib.util
import json
from math import comb
from pathlib import Path
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE = ROOT / 'context/propertyb-general/bridge-12-16-20261021/numeric_bridge.py'
spec = importlib.util.spec_from_file_location('nb', SOURCE)
nb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(nb)
GL = {5:32, 6:64, 7:128, 8:263, 9:538}
HISTORICAL = {**GL, 10:1070, 11:2213}
NEW = dict(zip(range(5,12), [35,65,130,266,542,1112,2275]))

def ceildiv(a,b):
    return (a+b-1)//b

def gr(k):
    best = None
    rows = []
    v = 2*k-1
    while True:
        s = ceildiv(v*ceildiv(v-1,k-1),k)
        if best is not None and s >= best:
            return dict(lower_bound=best, minimizers=[r['v'] for r in rows if r['value']==best],
                        checked_v_min=2*k-1, checked_v_max=v-1,
                        first_omitted_v=v, first_omitted_S=s, rows=rows,
                        cutoff='S_k(v) is nondecreasing; every omitted value >= first omitted S >= attained minimum')
        denominator=comb(v//2,k)+comb((v+1)//2,k)
        numerator=comb(v,k)
        r=ceildiv(numerator,denominator) if denominator else None
        val=max(s,r) if r is not None else None
        rows.append(dict(v=v,S=s,R_numerator=numerator,R_denominator=denominator,
                         ceil_R=r,value=val))
        if val is not None:
            best=val if best is None else min(best,val)
        v+=1

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--verify',action='store_true')
    args=parser.parse_args();start=time.perf_counter()
    dest=HERE/'MATCHED_BASELINES.json'
    if args.verify:
        doc=json.loads(dest.read_text())
        for row in doc['rows']:
            k=row['k'];a=row['RS_acceptance']
            assert a==nb.feasible(k,a['budget'],nb.unpair(a['p'])) | {'local_real_threshold': a['local_real_threshold']}
            assert row['RS_next_all_p_rejection']==nb.global_rejection(k,a['budget']+1)
            assert row['GR']==gr(k)
            assert row['L_ref']==max(a['budget']+1,GL.get(k,0),row['GR']['lower_bound'])
            assert row['matched_gain']==NEW[k]-row['L_ref']
        print('PASS: seven strict RS witnesses, seven complete next-budget all-p rejections, seven exact full GR minima, matched envelopes.')
        print('Replay seconds:',time.perf_counter()-start)
        return
    rows=[]
    for k in range(5,12):
        if k==11:
            cached=json.loads((HERE.parent/'K11_MATCHED_BASELINE.json').read_text())
            acceptance=cached['old_RS_acceptance'];rejection=cached['old_RS_next_all_p_rejection']
        else:
            acceptance,_=nb.propose(k)
            rejection=nb.global_rejection(k,acceptance['budget']+1)
        g=gr(k);rs=acceptance['budget']+1
        ref=max(rs,GL.get(k,0),g['lower_bound'])
        rows.append(dict(k=k,RS_budget_maximum=rs-1,RS_lower_bound=rs,
                         RS_acceptance=acceptance,RS_next_all_p_rejection=rejection,
                         GL_Theorem1=GL.get(k),GR=g,L_ref=ref,new_lower_bound=NEW[k],
                         matched_gain=NEW[k]-ref,historical_GL_baseline=HISTORICAL[k],
                         historical_GL_gain=NEW[k]-HISTORICAL[k],
                         historical_GL_kind='Theorem 1' if k<=9 else 'strict rational substitution in formula (7), not a reported record'))
        print(k,rs,g['lower_bound'],ref,NEW[k]-ref,flush=True)
    dest.write_text(json.dumps(dict(scope='k=5..11; specified six-source reference envelope only',
          analytic_dominance='For every k>=2, B_RS>=d=2^(k-1) at p=1, since J_k(1)<1 and d(d-1)/d^2<1. For M>=d, Bernoulli convexity and J<=p prove cont and lin acceptance implies RS acceptance. For M<d this already lies below B_RS. Pair acceptance implies cont acceptance pointwise. Hence all three budgets are <=B_RS, without relying on the k>=12 growth theorem.',
          maximality='Every p is excluded at B_RS+1. For larger M, gamma=M(M-1) increases and a^(M/d) decreases (0<a<=1), so all larger budgets are excluded.',
          rows=rows,elapsed_seconds=time.perf_counter()-start),indent=2)+'\n')

if __name__=='__main__':main()
