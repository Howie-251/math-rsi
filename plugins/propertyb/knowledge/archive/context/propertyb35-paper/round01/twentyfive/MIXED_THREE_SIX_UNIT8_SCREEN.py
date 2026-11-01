"""All65 unit8 families, all56 three-low markings, true low-set canonicalization.
Raw fixed layouts only:18 consecutive plus the35 earlier two-low DP layouts.
The degree-six singles are reduced by1 each and empty increased by3; old
negative-empty families are reconsidered. No new point or whole H is generated.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent;root=P.parents[3];S=root/'context/propertyb34/round01/high-math';sys.dont_write_bytecode=True;sys.path[:0]=[str(S),str(root/'computations')]
from unit_catalogue import fullblocks,canonical
from bare_layout import BareLayout
from multilock import json_value
st=time.perf_counter();src=json.loads((S/'UNIT_CATALOGUE_8.json').read_text());prior=json.loads((P/'MIXED_TWO_SIX_UNIT8_PILOT.json').read_text());positions=list(dict.fromkeys([tuple(range(a,a+8)) for a in range(1,19)]+[tuple(z['positions']) for z in prior['results']]));engines=[BareLayout(25,p) for p in positions];domain=[];new=[];groups={}
for base,big in enumerate(src['orbits']):
 bs=fullblocks(big,8);ss=[7-sum(t>>i&1 for t in bs) for i in range(8)];oldempty=35-len(bs)-sum(ss);lows=[]
 for low in combinations(range(8),3):
  singles=[v-int(i in low) for i,v in enumerate(ss)]
  if min(singles)<0 or oldempty+3<0:continue
  ns={t:1 for t in bs};ns.update({1<<i:v for i,v in enumerate(singles) if v})
  if oldempty+3:ns[0]=oldempty+3
  assert sum(ns.values())==35 and all(sum(n for t,n in ns.items() if t>>i&1)==7-int(i in low) for i in range(8))
  k,m=canonical(big,8,extra=[int(i in low) for i in range(8)],with_perm=True);lm=sum(1<<m[i] for i in low);key=(k,lm);z=dict(base=base,low=list(low),counts=ns,old_empty=oldempty,canonical_large=k,canonical_lowmask=lm,old_to_canonical=m);j=len(domain);domain.append(z);groups.setdefault(key,[]).append(j);lows.append(low)
 if oldempty<0 and lows:new.append(dict(base=base,old_empty=oldempty,new_empty=oldempty+3,markings=len(lows),large=big))
q2=json.loads((P/'MIXED_TWO_SIX_UNIT8_CERTIFICATE.json').read_text());q2cache={}
for z in q2['results']:
 ns={int(t):n for t,n in z['counts'].items()};k,m=canonical([t for t in ns if t.bit_count()>=3],8,extra=[int(i in z['low']) for i in range(8)],with_perm=True);lm=sum(1<<m[i] for i in z['low']);cp=[0]*8
 for i,j in enumerate(m):cp[j]=z['positions'][i]
 q2cache.setdefault((k,lm),set()).add(tuple(cp))
results=[];orbits=[]
for key,js in groups.items():
 z=domain[js[0]];ns=z['counts'];pp=list(positions)
 for L in combinations(z['low'],2):
  k,m=canonical([t for t in ns if t.bit_count()>=3],8,extra=[int(i in L) for i in range(8)],with_perm=True);lm=sum(1<<m[i] for i in L)
  for cp0 in q2cache[(k,lm)]:pp.append(tuple(cp0[m[i]] for i in range(8)))
 pp=list(dict.fromkeys(pp));vals=[BareLayout(25,p).bound(ns) if p not in positions else engines[positions.index(p)].bound(ns) for p in pp];v=min(vals);pos=pp[vals.index(v)];cp=[0]*8
 for i,j in enumerate(z['old_to_canonical']):cp[j]=pos[i]
 for j in js:
  zz=domain[j];pp=[cp[zz['old_to_canonical'][i]] for i in range(8)];assert BareLayout(25,pp).bound(zz['counts'])==v;results.append(dict(**zz,positions=pp,raw_ABC_bound=v))
 orbits.append(dict(base=z['base'],low=z['low'],low_labels=[domain[j]['low'] for j in js],canonical_large=key[0],canonical_lowmask=key[1],positions=pos,raw_ABC_bound=v))
summary=dict(scope=__doc__,complete=True,source_families=65,feasible_families=len({z['base'] for z in domain}),marked_inputs=len(domain),marked_orbits=len(groups),layouts=len(positions),strict=sum(z['raw_ABC_bound']<1 for z in results),residual=sum(z['raw_ABC_bound']>=1 for z in results),residual_orbits=sum(z['raw_ABC_bound']>=1 for z in orbits),maximum_raw=max(z['raw_ABC_bound'] for z in results),elapsed_seconds=time.perf_counter()-st)
(P/'MIXED_THREE_SIX_UNIT8_SCREEN.json').write_text(json.dumps(json_value(dict(summary=summary,new_old_negative_empty=new,residual_orbits=[z for z in orbits if z['raw_ABC_bound']>=1],orbits=orbits,results=results)),indent=2)+'\n');print(json.dumps(json_value(summary),indent=2));print('new',json.dumps(new));print('residual summary',[(z['base'],z['low'],str(z['raw_ABC_bound'])) for z in orbits if z['raw_ABC_bound']>=1])
