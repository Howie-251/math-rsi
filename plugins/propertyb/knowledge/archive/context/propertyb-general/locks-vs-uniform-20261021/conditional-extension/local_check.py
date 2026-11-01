import sys,json
from pathlib import Path
from itertools import permutations
sys.path.insert(0,str(Path('context/collaborator-small-k-20261019/m10-m11').resolve()))
from propertyB_k10_k11_verified import FastExact,S
rows=[]
for M,v,d,e in [(9544,972,81,81),(9564,972,81,81),(9564,813,68,68)]:
    k=13; ex=12*d-(v-1); ey=12*e-(v-1); t=v-2-ex-ey
    assert t>0 and min(ex,ey)>=0
    F=d+(k*M-v*d-(e-d))//t
    calc=FastExact(k,M); worst=(-1,None); n=0
    for f in range(d,F+1):
        for triple in [False,True]:
            z=min(calc.three(v,ds,triple) for ds in set(permutations((d,e,f))))
            n+=1
            if z>worst[0]:worst=(z,(f,triple))
    rows.append(dict(k=k,M=M,v=v,d=d,e=e,common_lower=t,F=F,profiles=n,worst=worst,S=S,gap=S-worst[0]))
out=Path(__file__).with_name('LOCAL_CHECK.json');out.write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows))
