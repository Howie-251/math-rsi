"""Reevaluate saved8/10/10 fixed positions on8/10/11, not a monotonicity assumption.
Lower the11 singleton trace by1 and increase empty trace by1 only to retrieve a source layout;
then recompute every target weight/quota exactly. No full target DP unless a transferred witness fails.
"""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[6];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from multilock import json_value
start=time.time();source=json.loads((HERE/'u8_10_10_DOMAIN.json').read_text());dp=json.loads((HERE/'u8_10_10_DP.json').read_text())['cases'];target=json.loads((HERE/'u8_10_11_DOMAIN.json').read_text())
key=lambda n:tuple(n.get(t,n.get(str(t),0)) for t in range(32));lookup={key(r['counts']):r for r in source['labelled']};out=[]
for r in target['orbits']:
 ns={int(t):n for t,n in r['counts'].items()};lower=dict(ns);lower[16]-=1;lower[0]+=1;assert min(lower.values())>=0
 row=lookup[key(lower)];sr=dp[row['orbit']];positions=[0]*5;perm=row['from_representative_high_permutation'];swap=row['from_representative_low_swap']
 for i in range(5):dest=(1-i if swap else i) if i<2 else perm[i-2]+2;positions[dest]=sr['positions'][i]
 eng=SubsetEngine(20,5,ns);at={p:1<<i for i,p in enumerate(positions)};left=0;num=0
 for k in range(1,21):
  p=at.get(k,0);v=eng.value(k,left,p);assert v is not None;num+=v;left|=p
 z=eng.verify(dict(bound=Q(num,eng.D),positions=positions,counts=ns));z.update(r);z['strict']=z['bound']<1;z['source_10_orbit']=sr['id'];z['source_high_transport']=perm;z['source_low_swap']=swap;out.append(z)
print('transferred',len(out),'strict',sum(z['strict'] for z in out),'max',max(z['bound'] for z in out),'seconds',time.time()-start,flush=True)
(HERE/'u8_10_11_TRANSFER.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
if any(not z['strict'] for z in out):
 failed=[]
 for z in out:
  if z['strict']:continue
  eng=SubsetEngine(20,5,z['counts']);new=eng.verify(eng.solve());new.update(id=z['id'],degrees=z['degrees']);failed.append(new)
 (HERE/'u8_10_11_FAILED_TRANSFER_DP.json').write_text(json.dumps(json_value(dict(cases=failed)),indent=2)+'\n');print('newDP failures',len(failed),'strict',sum(z['bound']<1 for z in failed),flush=True)
