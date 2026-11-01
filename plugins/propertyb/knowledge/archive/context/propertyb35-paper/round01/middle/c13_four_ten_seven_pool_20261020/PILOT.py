"""S2 genuine nine degree-seven pool, first worst10^4 tail and one feasible lift."""
from pathlib import Path
from itertools import product
from fractions import Fraction
import sys,time,json
P=Path(__file__).resolve().parent;ROOT=P.parents[4];st=time.process_time()
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'));sys.path.insert(0,str(ROOT/'computations'))
from subset_position_dp import SubsetEngine
from independent_structure_bounds import independent_rows
source=json.loads((P.parent/'generic_c3_thirteen_pilot_20261020/RESULT.json').read_text())
tails=[z for z in source['cases'] if not z['strict']];assert len(tails)==6
for z in tails:assert sum(z['counts'][1<<v] for v in range(4))==2
pairsource=json.loads((P.parent/'two_six_transfer_20261020/PAIR_RESULT.json').read_text())
gates=[z for z in pairsource['cases'] if z['degrees']==[7,10]]
assert {z['codegree'] for z in gates}=={5,6,7} and all(z['strict'] for z in gates)
PP=(3,5,6,9,10,12);mu=tuple(tails[0]['counts']);domain=[]
for cp in product(*(range(mu[p]+1) for p in PP)):
 total=sum(cp)
 if total>7:continue
 rows=tuple(sum(n for p,n in zip(PP,cp) if p>>v&1) for v in range(4))
 if any(not 1<=r<=4 for r in rows):continue
 c0=7-total
 if not 0<=c0<=mu[0]:continue
 ns={m<<1:n for m,n in enumerate(mu) if n};ns[0]-=c0;ns[1]=c0
 for p,n in zip(PP,cp):ns[p<<1]-=n;ns[(p<<1)|1]=n
 assert sum(ns.values())==35 and min(ns.values())>=0
 degrees=[sum(n for m,n in ns.items() if m>>v&1) for v in range(5)]
 assert degrees==[7,10,10,10,10]
 domain.append(dict(pair_masks=PP,c_pair=cp,c0=c0,inclusive_z_to_K=rows,counts=ns,degrees=degrees))
(P/'WORST_SOURCE_DOMAIN.json').write_text(json.dumps(dict(source_counts=mu,domain_size=len(domain),cases=domain),indent=2)+'\n')
assert domain
z=domain[0];e=SubsetEngine(21,5,z['counts']);e.inv={p:(0,0,[]) for p in e.inv};vals=[]
for slot in (1,10,11,12):
 pos=(slot,8,9,20,21);lock={k:1<<v for v,k in enumerate(pos)};left=0;U=0
 for at in range(1,22):p=lock.get(at,0);U+=e.value(at,left,p);left|=p
 vals.append((Fraction(U,e.D),pos))
U,pos=min(vals)
masks=[m for m,n in z['counts'].items() for _ in range(n)];ts=[frozenset(v+1 for v in range(5) if m>>v&1) for m in masks]
ir=independent_rows(21,pos,ts);own=sum((min(r['A'],r['B'],r['C']) for r in ir),Fraction());assert own==U
res=dict(status='FIRST_PILOT_STRICT' if U<1 else 'STOPPED_FIRST_PILOT_NONSTRICT',scope=__doc__,six_source_singleton_sums=[sum(z['counts'][1<<v] for v in range(4)) for z in tails],actual_source_pair_caps=[[z['counts'][p] for p in PP] for z in tails],imported_7_10_gates=[dict(codegree=z['codegree'],bound=z['bound'],positions=z['positions']) for z in gates],worst_source_domain=len(domain),pilot=z,all_fixed=[dict(positions=p,bound=str(v)) for v,p in vals],best=dict(positions=pos,bound=str(U),strict=U<1),independent35_masks=masks,independent_rows=[{k:str(v) if isinstance(v,Fraction) else v for k,v in r.items()} for r in ir],cpu_seconds=time.process_time()-st)
(P/'PILOT_RESULT.json').write_text(json.dumps(res,indent=2)+'\n');print({k:v for k,v in res.items() if k not in ('independent_rows','independent35_masks')})
