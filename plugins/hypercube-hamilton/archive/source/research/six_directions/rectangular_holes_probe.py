"""Reproduce the 44 Z3 construction certificates; not exhaustive."""
import json,random
from pathlib import Path
from single_bridge_probe import random_maximum
from split_transfer import construct,criterion
ROOT=Path(__file__).resolve().parent

def main():
    out=[];rng=random.Random(20261103)
    for j in range(4):
        m=random_maximum(6,{0,3,28,31},rng);assert len(m)==30
        mate={a:b for e in m for a,b in (e,e[::-1])}
        for v in range(32):
            if not v&3 or v.bit_count()%2==0 or v==31:continue
            i=0 if v&1 else 1;bit=1<<i;w,t,z=28,31,3
            a,b,y=z^bit,t^bit,w^bit
            cert=dict(cut=i,z=z,w=w,t=t,a=a,b=b,y=y,r=mate[y])
            result=construct(m,0,v,cert)
            out.append(dict(n=6,u=0,v=v,matching=m,template=j,
                            Z1_applicable=criterion(m,0,v) is not None,**cert,**result))
            (ROOT/'rectangular_holes_results.json').write_text(json.dumps(out,indent=2),encoding='utf8')
    print('TOTAL',len(out),'FOUND',sum(c['status']=='FOUND' for c in out))

if __name__=='__main__':main()
