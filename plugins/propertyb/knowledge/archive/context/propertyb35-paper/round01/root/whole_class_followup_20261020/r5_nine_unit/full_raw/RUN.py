#!/usr/bin/env python3
"""Authorized remaining1322 colored orbit raw scan, at most600 CPU/720wall seconds."""
from pathlib import Path
from time import process_time,monotonic
from fractions import Fraction as Q
from collections import defaultdict,Counter
from itertools import combinations
import json,sys
P=Path(__file__).resolve().parent;B=P.parent;ROOT=next(p for p in P.parents if (p/'computations/independent_structure_bounds.py').exists())
sys.dont_write_bytecode=True;sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from bare_layout import BareLayout
from independent_structure_bounds import independent_rows
start=process_time();wall=monotonic()
def key(z):return (tuple(z['canonical_large']),z['canonical_lowmask'])
def serial(x):
 if isinstance(x,Q):return str(x)
 if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [serial(v) for v in x]
 return x
D=json.loads((B/'DOMAIN.json').read_text())['records'];G=defaultdict(list)
for i,z in enumerate(D):G[key(z)].append(i)
assert len(G)==1689 and len(D)==3107
old={k:next(i for i in ids if Q(D[i]['old_bound'])<1) for k,ids in G.items() if any(Q(D[i]['old_bound'])<1 for i in ids)}
assert len(old)==325
lookup={(z['base'],tuple(z['low'])):key(z) for z in D}
pilot={lookup[(z['base'],tuple(z['low']))]:z for z in json.loads((B/'PROFILE.json').read_text())['records'] if Q(z['raw_witness_bound'])<1}
newpilot={k:v for k,v in pilot.items() if k not in old};assert len(newpilot)==2
sample={key(z):z for z in json.loads((B/'diverse40/RESULT.json').read_text())['records']};assert len(sample)==40 and all(Q(z['raw_bound'])<1 for z in sample.values())
assert not(set(sample)&(set(old)|set(newpilot)))
covered=set(old)|set(newpilot)|set(sample)
plan=[]
for k,ids in G.items():
 if k in covered:continue
 i=min(ids,key=lambda j:(Q(D[j]['old_bound']),j));z=D[i]
 ns={int(t):n for t,n in z['counts'].items()};lm=sum(1<<i for i in z['low'])
 private=sorted(sum(n for t,n in ns.items() if t>>i&1 and (t&lm).bit_count()==1) for i in range(9) if not lm>>i&1)
 plan.append({**z,'domain_record':i,'orbit_records':ids,'orbit_size':len(ids),'seven_private_signature':private,'max_block':max(t.bit_count() for t in ns),'empty':ns.get(0,0)})
assert len(plan)==1322
(P/'PLAN.json').write_text(json.dumps({'old_at_least_one_strict_orbits':325,'new_old_pilot_orbits':2,'diverse40_orbits':40,'remaining':1322,'records':plan},indent=2)+'\n')
# Do not repeat completed work after an interruption.
journal=P/'RECORDS.jsonl';done=[]
if journal.exists():
 for line in journal.read_text().splitlines():
  if line.strip():done.append(json.loads(line))
assert all(key(z)==key(plan[i]) for i,z in enumerate(done))
if len(done)==1322 and (P/'RESULT.json').exists():
 previous=json.loads((P/'RESULT.json').read_text())
 assert previous['completed_new_orbits']==1322
 print(json.dumps({k:v for k,v in previous.items() if k!='residual'}),flush=True)
 raise SystemExit
priorcpu=sum(z['cpu_seconds'] for z in done);priorwall=sum(z['wall_seconds'] for z in done)
non=[z for z in done if not z['strict']];total_labels=sum(z['orbit_size'] for z in done)

def checkpoint(final=False):
 vals=[Q(z['raw_bound']) for z in done]
 status='COMPLETE_STRICT' if len(done)==1322 and not non else 'COMPLETE_WITH_RESIDUAL' if len(done)==1322 else 'STOPPED_20_NONSTRICT' if len(non)>=20 else 'PARTIAL'
 out={'status':status,'old_at_least_one_strict_orbits':325,'new_old_pilot_orbits':2,'diverse40_orbits':40,'planned_new_orbits':1322,'completed_new_orbits':len(done),'strict_new_orbits':len(done)-len(non),'nonstrict_new_orbits':len(non),'all_new_rows_replayed':25*len(done),'new_labels_represented':total_labels,'maximum':str(max(vals)) if vals else None,'cpu_seconds':priorcpu+process_time()-start,'wall_seconds':priorwall+monotonic()-wall,'covered_strict_orbits':367+len(done)-len(non),'total_required_orbits':1689,'remaining_unprocessed':1322-len(done),'residual':[{'base':z['base'],'low':z['low'],'canonical_large':z['canonical_large'],'canonical_lowmask':z['canonical_lowmask'],'seven_private_signature':z['seven_private_signature'],'max_block':z['max_block'],'empty':z['empty'],'raw_bound':z['raw_bound'],'positions':z['positions']} for z in non]}
 (P/'CHECKPOINT.json').write_text(json.dumps(out,indent=2)+'\n')
 if final:(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='residual'}),flush=True)
 return out
checkpoint()
with journal.open('a') as stream:
 for z in plan[len(done):]:
  if priorcpu+process_time()-start>=600 or priorwall+monotonic()-wall>=720 or len(non)>=20:break
  tm=process_time();wt=monotonic();ns={int(t):n for t,n in z['counts'].items()};low=set(z['low'])
  assert sum(ns.values())==35
  assert all(sum(n for t,n in ns.items() if t>>i&1)==(6 if i in low else 7) for i in range(9))
  assert all(sum(n for t,n in ns.items() if t>>i&1 and t>>j&1)==1 for i,j in combinations(range(9),2))
  assert all(sum(bool(t>>i&1) for i in low)<=2 for t in ns)
  eng=SubsetEngine(25,9,ns)
  for p in eng.inv:eng.inv[p]=(0,0,[])
  w=eng.solve();raw,abc=BareLayout(25,w['positions']).bound(ns,with_rows=True)
  stubs=[frozenset(i+1 for i in range(9) if t>>i&1) for t,n in ns.items() for _ in range(n)]
  rr=independent_rows(25,tuple(w['positions']),stubs)
  assert [(r['A'],r['B'],r['C']) for r in rr]==abc
  assert raw==w['bound']==sum((min(r['A'],r['B'],r['C']) for r in rr),Q())
  record=serial({**z,'plan_index':len(done),'raw_bound':raw,'strict':raw<1,'positions':w['positions'],'all_25_rows_independently_equal':True,'raw_rows':rr,'cpu_seconds':process_time()-tm,'wall_seconds':monotonic()-wt})
  stream.write(json.dumps(record)+'\n');stream.flush();done.append(record);total_labels+=record['orbit_size']
  if not record['strict']:non.append(record);print('NONSTRICT '+json.dumps({k:record[k] for k in ('base','low','seven_private_signature','raw_bound','positions')}),flush=True)
  if len(done)%50==0:checkpoint()
checkpoint(final=True)
