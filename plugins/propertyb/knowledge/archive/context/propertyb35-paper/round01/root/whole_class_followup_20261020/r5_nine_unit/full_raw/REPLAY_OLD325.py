#!/usr/bin/env python3
"""Replay original corrected ordinary-ABC witnesses; preserve nested quota import."""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction as Q
from time import process_time
import json,sys
P=Path(__file__).resolve().parent;B=P.parent;ROOT=next(p for p in P.parents if (p/'computations/independent_structure_bounds.py').exists())
sys.dont_write_bytecode=True;sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'computations/propertyb33/round01')]
from independent_structure_bounds import independent_rows
from multilock import Profile
from pure_quota import certificate
start=process_time();D=json.loads((B/'DOMAIN.json').read_text())['records'];G=defaultdict(list)
for i,z in enumerate(D):G[(tuple(z['canonical_large']),z['canonical_lowmask'])].append(i)
out=[]
for k,ids in G.items():
 good=[i for i in ids if Q(D[i]['old_bound'])<1]
 if not good:continue
 i=min(good,key=lambda j:(Q(D[j]['old_bound']),j));z=D[i];ns={int(t):n for t,n in z['counts'].items()};pos=tuple(z['positions'])
 stubs=[frozenset(j+1 for j in range(9) if t>>j&1) for t,n in ns.items() for _ in range(n)]
 rr=independent_rows(25,pos,stubs);p=Profile(25,5,pos,ns);cs=[certificate(p,j) for j in range(9)];losses={pos[j]:c['loss'] for j,c in enumerate(cs)}
 total=Q();rows=[]
 for r in rr:
  loss=losses.get(r['k'],Q());corrected=r['C']-loss;assert corrected>=0
  bound=min(r['A'],r['B'],corrected);total+=bound
  rows.append({**{k:str(r[k]) for k in ('A','B','C')},'k':r['k'],'deduction':str(loss),'corrected_C':str(corrected),'bound':str(bound)})
 assert total==Q(z['old_bound']) and total<1
 out.append({'domain_record':i,'base':z['base'],'low':z['low'],'positions':pos,'bound':str(total),'quota_import':'Original total/pure nested quota certificate, no new lower bound','certificates':[{k:str(v) if isinstance(v,Q) else v for k,v in c.items()} for c in cs],'rows':rows})
assert len(out)==325
r={'status':'PASS_ORIGINAL_CORRECTED_CERTIFICATES','orbits':325,'rows':8125,'maximum':str(max(Q(z['bound']) for z in out)),'all_frozen_affine_values_equal_direct_corrected_ABC':True,'cpu_seconds':process_time()-start,'records':out}
(P/'OLD325_REPLAY_RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k!='records'}))
