"""Reuse the actual three-low gate and monochromatic four-set deductions."""
from pathlib import Path
from time import process_time
import json

def red(m):
    return 2035 if m>=7 else 1595 if m==6 else max(0,55*(m-1))
def blue(m):
    return 616 if m>=7 else max(0,11*(m-1))

def main():
    t0=process_time(); rs=[]
    for p in (0,1):
        for su in range(4-2*p):
            for sv in range(4-2*p-su):
                for alpha in range(9):
                    if min(8-su-alpha,8-sv-alpha)<0:
                        continue
                    vals=[]
                    for s,t in ((su,sv),(sv,su)):
                        raw=77681+243*p+2002*9-1822*s+948*t-5005*alpha
                        vals.append(raw-red(8-s-alpha)-blue(8-t-alpha))
                    rs.append(dict(p=p,su=su,sv=sv,alpha=alpha,bound=min(vals),
                                   implies_coloring=(su+sv>0 or alpha>0)))
    relevant=[r for r in rs if r['implies_coloring']]
    assert all(r['bound']<92378 for r in relevant)
    out=dict(status='PASS',scope='degree-nine degree-nine high endpoints; some spoke or alpha positive',
             rows=rs,maximum=max(r['bound'] for r in relevant),
             count=len(relevant),cpu_seconds=process_time()-t0)
    Path(__file__).with_name('NINE_NINE_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
if __name__=='__main__': main()
