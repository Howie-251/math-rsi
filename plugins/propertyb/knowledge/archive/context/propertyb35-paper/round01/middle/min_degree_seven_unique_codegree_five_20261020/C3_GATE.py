"""Only missing unique-high-pair5 C3>=14 local families; old fixed3 menu.
Other selected degrees7/7,7/8,7/9,9/9; high pairs10/12 or11/11.
"""
from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction
import json,sys,time

P=Path(__file__).resolve().parent;ROOT=P.parents[4];START=time.process_time()
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
PP=(3,5,6,9,10,12);CROSS=(5,6,9,10);TM=(7,11,13,14)
MENU=((8,9,20,21),(9,10,20,21),(9,20,10,21))
families=[];keys={}
for du,dv in ((10,12),(11,11)):
    for da,db in ((7,7),(7,8),(7,9),(9,9)):
        for role in ('same','cross'):
            orders=[(da,db)] if role=='same' or da==db else [(da,db),(db,da)]
            for oa,ob in orders:
                ds=(du,dv,oa,ob) if role=='same' else (du,oa,dv,ob)
                mark=3 if role=='same' else 5
                fid=len(families);families.append({'degrees':ds,'marked_pair':mark,'role':role})
                caps={p:5 if p==mark else 4 for p in PP}
                crosscap=sum(caps[p] for p in CROSS)
                # t>=14 implies full4=0 and at most one triple, even with cap17.
                for tv in [(0,0,0,0)]+[tuple(int(i==j) for i in range(4)) for j in range(4)]:
                    if 14+2*sum(tv)>crosscap:continue
                    remainder={p:caps[p]-sum(n for m,n in zip(TM,tv) if m&p==p) for p in PP}
                    if min(remainder.values())<0:continue
                    ranges=[(remainder[p],) if p==mark else range(remainder[p]+1) for p in CROSS]
                    for cv in product(*ranges):
                        if sum(cv)<14:continue
                        sides=[(remainder[p],) if p==mark else range(1,remainder[p]+1) for p in (3,12)]
                        for side in product(*sides):
                            mu=[0]*16
                            for m,n in zip(TM,tv):mu[m]=n
                            for m,n in zip(CROSS,cv):mu[m]=n
                            mu[3],mu[12]=side
                            for v,d in enumerate(ds):mu[1<<v]=d-sum(n for m,n in enumerate(mu) if m.bit_count()>=2 and m>>v&1)
                            mu[0]=35-sum(mu)
                            if min(mu)<0:continue
                            assert sum(mu)==35 and [sum(n for m,n in enumerate(mu) if m>>v&1) for v in range(4)]==list(ds)
                            assert sum(n for m,n in enumerate(mu) if m&mark==mark)==5
                            keys.setdefault(tuple(mu),[]).append(fid)
assert len(families)==20
domain={'families':families,'family_count':len(families),'inventory_count':len(keys),
        'keys':[{'counts':list(k),'families':v} for k,v in sorted(keys.items())]}
(P/'C3_DOMAIN.json').write_text(json.dumps(domain,indent=2)+'\n')
cases=[]
for idx,(mu,fids) in enumerate(sorted(keys.items())):
    engine=SubsetEngine(21,4,{m:n for m,n in enumerate(mu) if n});engine.inv={p:(0,0,[]) for p in engine.inv}
    values=[]
    for pos in MENU:
        bp={k:1<<v for v,k in enumerate(pos)};left=0;value=0
        for k in range(1,22):
            p=bp.get(k,0);value+=engine.value(k,left,p);left|=p
        values.append({'positions':pos,'bound':str(Fraction(value,engine.D))})
    best=min(values,key=lambda z:Fraction(z['bound']))
    z={'counts':list(mu),'families':fids,'best':best,'all_fixed':values,'strict':Fraction(best['bound'])<1}
    cases.append(z)
    if idx==0:
        (P/'C3_SINGLE_PILOT.json').write_text(json.dumps({'case':z,'cpu_seconds':time.process_time()-START},indent=2)+'\n')
    assert time.process_time()-START<5,'five CPU primary cutoff'
out={'status':'COMPLETE_MISSING20_FAMILIES','families':20,'inventory_count':len(keys),
     'same_side_inventory_count':sum(1 for mu,fids in keys.items() if any(families[i]['role']=='same' for i in fids)),
     'strict_count':sum(z['strict'] for z in cases),'maximum':str(max(Fraction(z['best']['bound']) for z in cases)),
     'menu':MENU,'cases':cases,'nonstrict':[z for z in cases if not z['strict']],
     'cpu_seconds':time.process_time()-START}
(P/'C3_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k not in ('cases','nonstrict')})
print('NONSTRICT',len(out['nonstrict']))
