"""Independent tiny symbolic audit; not a signed-family or H search."""
from itertools import combinations, combinations_with_replacement
from fractions import Fraction
from pathlib import Path
import json
import time

start=time.process_time()
geometry={}
for r in (2,3):
    failures=[]
    for fsize in range(r+1):
        F=set(range(fsize))
        subsets=[set(c) for k in range(fsize+1) for c in combinations(F,k)]
        for Uf in subsets:
            for Vf in subsets:
                a,b=4-len(Uf),4-len(Vf)
                if a*b > 9-2*r: continue
                failures.append([fsize,sorted(Uf),sorted(Vf),a,b])
                if r==2:
                    assert fsize==2 and Uf==Vf==F and a==b==2
                else:
                    assert fsize==3 and len(Uf & Vf)>=1
    geometry[str(r)]=failures

# f=0,g=1; at most four further points suffice for two arbitrary 2-edges.
edges=list(combinations(range(6),2))
counts={'v0':0,'v1_fg':0,'v1_no_fg':0,'v2':0}
total=0
for size in range(3):
    for K in combinations_with_replacement(edges,size):
        total+=1
        deg=[sum(v in e for e in K) for v in (0,1)]
        f,g=(0,1) if deg[0]<=deg[1] else (1,0)
        v=min(deg)
        fg=tuple(sorted((f,g)))
        if v==0:
            assert all(f not in e for e in K)
            counts['v0']+=1
        elif v==1 and fg in K:
            assert sum(f in e for e in K)==1
            counts['v1_fg']+=1
        elif v==1:
            assert len(K)==2
            fe=[e for e in K if f in e]
            ge=[e for e in K if g in e]
            assert len(fe)==len(ge)==1 and fe[0]!=ge[0]
            assert g not in fe[0] and f not in ge[0]
            counts['v1_no_fg']+=1
        else:
            assert v==2 and len(K)==2 and all(e==fg for e in K)
            counts['v2']+=1

strict=[('r0',16,9),('r1',9,7),('r3_no_f',9,5),('r3_f',4,3),
        ('r2_v0',9,6),('r2_v1_fg',9,4),('r2_v1_no_fg',4,3),('r2_v2',9,2)]
assert all(a>b for _,a,b in strict)
assert Fraction(544,3)<256 and 4*(7-1)<3*3**2
result={'status':'PASS','F_geometry':geometry,'K_multifamilies':total,'K_cases':counts,
        'strict_comparisons':strict,'disjoint_bound':str(Fraction(544,3)),
        'cpu_seconds':time.process_time()-start,
        'scope':'F intersections and complete <=2-edge marked K multigraphs only'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='F_geometry'}))
