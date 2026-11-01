#!/usr/bin/env python3
"""Bounded actual G-trace inventories plus exact fixed-edge costs; no H search."""
from pathlib import Path
from itertools import combinations,product
from collections import Counter
from math import comb
from time import process_time
from fractions import Fraction
import json,sys
P=Path(__file__).resolve().parent
from INVENTORY_PROFILE import inventories

def choose(n,k):return comb(n,k) if 0<=k<=n else 0

def price(q,size,color):return choose(18-size,q-size if color=='B' else q)

PRICES={8:{'w0':3186,'w1_R':2910,'w1_B':3567,'w2_double_RR':3486,'w2_double_BB':5598,'w2_double_RB':2334,
           'w2_two_RR':2568,'w2_two_BB':3726,'w2_two_RB':3906},
        9:{'w0':3996,'w1_R':3984,'w1_B':3984,'w2_double_RR':5388,'w2_double_BB':5388,'w2_double_RB':2892,
           'w2_two_RR':3816,'w2_two_BB':3816,'w2_two_RB':4764}}

def free_type(z,trace,colors):
    incident=[t for t in trace if z in t]
    pins=[[i for i in t if i!=z] for t in incident]
    weight=sum(map(len,pins))
    if weight==0:return 'w0'
    if weight==1:return 'w1_'+colors[pins[0][0]]
    assert weight==2
    chars=sorted([colors[i] for group in pins for i in group],reverse=True) # R before B
    signature=''.join(chars)
    return 'w2_'+('double_' if len(pins)==1 else 'two_')+signature

def options(trace):
    inc=[sum(i in t for t in trace) for i in range(5)]
    low_single=[5-inc[i] for i in range(4)]
    empty_constant=15+sum(len(t)-1 for t in trace)
    dmin=max(6,inc[4]+1);dmax=empty_constant
    answer=[]
    for a,b in combinations(range(4),2):
        if any(a in t and b in t for t in trace):continue
        fixed=[i for i in range(5) if i not in (a,b)]
        fixedtraces=[t for t in trace if a not in t and b not in t]
        for bits in product('RB',repeat=3):
            if len(set(bits))==1:continue
            colors=dict(zip(fixed,bits))
            ta,tb=free_type(a,trace,colors),free_type(b,trace,colors)
            for q in (8,9):
                pure=price(q,5,'R')+price(q,5,'B')
                slope=price(q,4,colors[4])-pure
                const=empty_constant*pure-(1+inc[4])*price(q,4,colors[4])
                const+=sum(low_single[i]*price(q,4,colors[i]) for i in fixed if i<4)
                for t in fixedtraces:
                    cs={colors[i] for i in t}
                    if len(cs)==1:const+=price(q,5-len(t),next(iter(cs)))
                const+=PRICES[q][ta]+PRICES[q][tb]
                # Check real fixed-edge index count at both ends of degree interval.
                for d in (dmin,dmax):
                    assert len(fixedtraces)+sum(low_single[i] for i in fixed if i<4)+(d-1-inc[4])+(empty_constant-d)==24
                answer.append({'free':[a,b],'fixed_colors':colors,'quota':q,'component_types':[ta,tb],
                               'intercept':const,'slope':slope})
    assert answer
    return dmin,dmax,answer

def assess(trace):
    dmin,dmax,opts=options(trace)
    totals=[]
    for d in range(dmin,dmax+1):
        candidates=[(Fraction(o['intercept']+o['slope']*d,comb(18,o['quota'])),i) for i,o in enumerate(opts)]
        v,idx=min(candidates);o=opts[idx]
        totals.append({'d':d,'bound':str(v),'total':o['intercept']+o['slope']*d,
                       'sample_space':comb(18,o['quota']),'option':o,'strict':v<1})
    weighted=[sum((len(t)-1) for t in trace if i in t) for i in range(4)]
    external_gate=sum(w==0 for w in weighted)>=3
    counts=Counter(trace)
    doublepairs=(len(counts)==2 and all(len(t)==2 and max(t)<4 and n==2 for t,n in counts.items())
                 and len(set(sum((list(t) for t in counts),[])))==4)
    return {'traces':trace,'degree_interval':[dmin,dmax],'weighted_low_internal_degrees':weighted,
            'external_three_free_gate':external_gate,'double_lambda3_gate':doublepairs,
            'degree_results':totals}

def main():
    start=process_time();domain=list(inventories())
    if '--profile' in sys.argv:
        part=[assess(t) for t in domain[:20]]
        out={'status':'PROFILE_COMPLETE','inventories':len(domain),'profile_inventories':20,
             'cpu_seconds':process_time()-start,'estimated_all_cpu_seconds':(process_time()-start)*len(domain)/20}
        (P/'INVENTORY_COST_PROFILE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out));return
    records=[]
    for t in domain:
        assert process_time()-start<30,'30CPU budget'
        records.append(assess(t))
    residual=[];coveredbyold=0;direct=0
    for idx,r in enumerate(records):
        for z in r['degree_results']:
            if z['strict']:direct+=1
            elif r['external_three_free_gate'] or r['double_lambda3_gate']:coveredbyold+=1
            else:residual.append({'inventory':idx,'traces':r['traces'],**z})
    out={'status':'DIAGNOSTIC_COMPLETE','inventories':len(domain),'degree_keys':sum(len(r['degree_results']) for r in records),
         'direct_strict_keys':direct,'remaining_covered_by_old_gates':coveredbyold,
         'unresolved_degree_keys':len(residual),'unresolved_inventories':len({r['inventory'] for r in residual}),
         'cpu_seconds':process_time()-start,'residual':residual,'records':records}
    (P/'INVENTORY_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('records','residual')}))
    print('first residual',json.dumps(residual[:3]))
if __name__=='__main__':main()
