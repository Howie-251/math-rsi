"""One minimal surviving cohort, exact shared row relaxation, not H search."""
from pathlib import Path
from itertools import combinations_with_replacement
from time import process_time
import json

def rows(d, eight=False):
    ans=[]
    for b in range(11):
        for c in range(1,8):
            K=2*b+3*c-11
            if not 0<=K<=11 or b+c>d:
                continue
            if eight and K>b:
                continue
            charge=max((2*max(0,K-b)+2)//3, max(0,2-b) if K else 0)
            ans.append(dict(d=d,b=b,c=c,K=K,f=d-b-c,charge=charge))
    return ans

def main():
    t0=process_time()
    r8=rows(8,True);r9=rows(9);r11=rows(11)
    # For six degree-nine rows, minimize their required 9/11 F3 edges
    # at each exact total double/triple incidence. Retain an actual row witness.
    dp={(0,0):(0,[])}
    for _ in range(6):
        nd={}
        for (b,c),(cost,rs) in dp.items():
            for r in r9:
                nb=b+r['b'];nc=c+r['c']
                if nb>10 or nc>30:
                    continue
                val=cost+r['charge']
                if (nb,nc) not in nd or val<nd[nb,nc][0]:
                    nd[nb,nc]=(val,rs+[r])
        dp=nd
    raw=[];passed=[]
    for x,y in combinations_with_replacement(r8,2):
        N8=x['c']+y['c']
        for w in r11:
            if N8>min(w['K'],11-w['K'],w['c']):
                continue
            key=(10-x['b']-y['b']-w['b'],30-x['c']-y['c']-w['c'])
            if key not in dp:
                continue
            cost,rs=dp[key]
            item=dict(eights=[x,y],eleven=w,nines=rs,N8=N8,
                      required_nine_eleven_edges=cost,
                      available_nine_eleven_edges=w['c']-N8)
            raw.append(item)
            if cost<=w['c']-N8:
                passed.append(item)
    out=dict(scope='q0 a1 cohort 7^4 8^2 9^6 11; exact necessary row relaxation',
             row_counts=[len(r8),len(r9),len(r11)],
             row_conserved_cases=len(raw),shared_charge_survivors=passed,
             raw_min_gap=min((r['required_nine_eleven_edges']-r['available_nine_eleven_edges'] for r in raw),default=None),
             first_conserved=raw[:1],cpu_seconds=process_time()-t0)
    Path(__file__).with_name('A4_ROW_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('shared_charge_survivors','first_conserved')},indent=2))
    print('survivors',len(passed))

if __name__=='__main__': main()
