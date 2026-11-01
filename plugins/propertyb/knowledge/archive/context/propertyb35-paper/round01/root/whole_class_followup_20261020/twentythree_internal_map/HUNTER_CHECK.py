#!/usr/bin/env python3
from pathlib import Path
from time import process_time
from fractions import Fraction
from math import comb
import json
from INVENTORY_PROFILE import inventories
from INVENTORY_CHECK import options
P=Path(__file__).resolve().parent

def deduction(q,color,n):
    if n<=1:return 0
    base=({2:45,3:126,4:234,5:600,6:1125} if q==8 and color=='R' else
          {2:1,3:3,4:6,5:30,6:75} if q==8 else
          {2:10,3:29,4:56,5:180,6:400})
    step=(45 if q==8 and color=='R' else 1 if q==8 else 10)
    return base[n] if n<=6 else base[6]+step*(n-6)

def main():
    start=process_time();records=[];residual=[]
    for idx,trace in enumerate(inventories()):
        dmin,dmax,opts=options(trace);inc=[sum(i in t for t in trace) for i in range(5)]
        for d in range(dmin,dmax+1):
            candidates=[]
            for o in opts:
                counts={'R':0,'B':0}
                for i,c in o['fixed_colors'].items():counts[c]+=(5 if i<4 else d-1)-inc[i]
                discounts={c:deduction(o['quota'],c,n) for c,n in counts.items()}
                total=o['intercept']+o['slope']*d-sum(discounts.values())
                candidates.append((Fraction(total,comb(18,o['quota'])),total,o,counts,discounts))
            bound,total,o,counts,discounts=min(candidates,key=lambda r:r[0])
            row={'inventory':idx,'traces':trace,'d':d,'bound':str(bound),'total':total,
                 'sample_space':comb(18,o['quota']),'option':o,'singleton_counts':counts,'deductions':discounts}
            records.append(row)
            if bound>=1:residual.append(row)
    out={'status':'DIAGNOSTIC_COMPLETE','degree_keys':len(records),'strict':len(records)-len(residual),
         'unresolved':len(residual),'cpu_seconds':process_time()-start,'residual':residual,'records':records}
    (P/'HUNTER_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('records','residual')}));print(json.dumps(residual[:5]))
if __name__=='__main__':main()
