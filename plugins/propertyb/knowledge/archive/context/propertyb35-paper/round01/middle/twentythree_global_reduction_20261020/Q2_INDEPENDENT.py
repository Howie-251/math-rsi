#!/usr/bin/env python3
"""Independent labeled trace/composition check, no group action or old profile import."""
from itertools import combinations_with_replacement
from math import comb
from pathlib import Path
from time import process_time
import json

def main():
    start=process_time()
    denominator=comb(18,11)
    red=comb(14,7)
    blue=comb(14,11)
    empty=comb(13,6)+comb(13,11)
    pair_counts=[comb(10+j,3+j) for j in range(4)]
    masks=[m for m in range(32) if m==0 or m.bit_count() in (2,3,4)]
    records=[]
    total=0
    worst=0
    witness=None
    for t,u in combinations_with_replacement(masks,2):
        h=[((t>>i)&1)+((u>>i)&1) for i in range(5)]
        low=[6-v for v in h]
        remaining=32-sum(low)
        ex=[]
        for i in range(5):
            count=0
            for m in (t,u):
                if m==0: count+=empty
                elif not (m>>i)&1: count+=comb(13+m.bit_count(),11)
            ex.append(count)
        local_total=0
        local_worst=0
        local_witness=None
        hard=0
        # Direct stars-and-bars with four cut positions, unlike the recursive old composition routine.
        for b0 in range(remaining+1):
            for b1 in range(b0,remaining+1):
                for b2 in range(b1,remaining+1):
                    for b3 in range(b2,remaining+1):
                        extra=(b0,b1-b0,b2-b1,b3-b2,remaining-b3)
                        a=[low[i]+extra[i] for i in range(5)]
                        bounds=[]
                        for i,k in enumerate(a):
                            deduction=(k-1)*pair_counts[0]
                            if k>=6: deduction=max(deduction,2616+(k-6)*pair_counts[0])
                            bounds.append(k*red+(32-k)*blue+ex[i]-deduction)
                        value=min(bounds)
                        local_total+=1
                        hard+=value>=denominator
                        if value>local_worst:
                            local_worst=value
                            local_witness={'a':a,'h':h,'d':[1+a[i]+h[i] for i in range(5)],'anchor_bounds':bounds}
                        if value>worst:
                            worst=value
                            witness={'T':[t,u],**local_witness}
        assert local_total==comb(remaining+4,4)
        records.append({'T':[t,u],'compositions':local_total,'hard':hard,'worst':local_worst,'witness':local_witness})
        total+=local_total
    assert len(records)==351
    assert total==150315
    assert sum(r['hard'] for r in records)==0
    assert worst==31808
    assert (denominator,red,blue,empty,pair_counts)==(31824,3432,364,1794,[120,330,792,1716])
    out={'status':'PASS_CONDITIONAL_ON_SIX_SET_LEMMA','review_independence':'same-family',
         'acceptance_status':'provisional','scope':'Fixed qGamma(F)=2, vertex minimum degree>=7; original23/35 input. Imports old q<=1 theorem only for Gamma-min3 consequence.',
         'method':'All labeled unordered exceptional trace pairs, repeated traces retained; direct four-cut composition loops; no S5 quotient, no profile import, no H enumeration.',
         'constants':{'D':denominator,'R':red,'B':blue,'empty':empty,'pair_intersections':pair_counts},
         'trace_pairs':len(records),'compositions':total,'hard':0,'worst':worst,'margin':denominator-worst,
         'worst_witness':witness,'trace_pair_records':records,'cpu_seconds':process_time()-start}
    (Path(__file__).with_suffix('.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='trace_pair_records'}))

if __name__=='__main__':main()
