from pathlib import Path
from time import process_time,monotonic
from fractions import Fraction as Q
from itertools import combinations
import json,sys
P=Path(__file__).resolve().parent;ROOT=next(p for p in P.parents if (p/'computations/independent_structure_bounds.py').exists())
sys.dont_write_bytecode=True;sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from bare_layout import BareLayout
from independent_structure_bounds import independent_rows
selection=json.loads((P/'SELECTION.json').read_text())['records'];target=5 if '--pilot' in sys.argv else 40
previous=json.loads((P/'RESULT.json').read_text()) if (P/'RESULT.json').exists() else {'records':[],'cpu_seconds':0,'wall_seconds':0}
records=previous['records'];initialcpu=previous['cpu_seconds'];initialwall=previous['wall_seconds'];start=process_time();wallstart=monotonic()

def serial(x):
 if isinstance(x,Q):return str(x)
 if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [serial(v) for v in x]
 return x

def save():
 vals=[Q(r['raw_bound']) for r in records]
 out={'status':'COMPLETE_40' if len(records)==40 else 'PILOT_5' if len(records)==5 else 'PARTIAL_BUDGET','scope':'Forty selected colored orbits only. Exact all-order all-position raw ABC DP, no quota deductions. Independent falling-factorial rows.','completed':len(records),'strict':sum(v<1 for v in vals),'nonstrict':sum(v>=1 for v in vals),'maximum':str(max(vals)) if vals else None,'cpu_seconds':initialcpu+process_time()-start,'wall_seconds':initialwall+monotonic()-wallstart,'records':records}
 (P/'RESULT.json').write_text(json.dumps(serial(out),indent=2)+'\n');return out
for z in selection[len(records):target]:
 if initialcpu+process_time()-start>=60 or initialwall+monotonic()-wallstart>=180:break
 tm=process_time();wt=monotonic();ns={int(t):n for t,n in z['counts'].items()};low=set(z['low'])
 assert sum(ns.values())==35
 assert all(sum(n for t,n in ns.items() if t>>i&1)==(6 if i in low else 7) for i in range(9))
 assert all(sum(n for t,n in ns.items() if t>>i&1 and t>>j&1)==1 for i,j in combinations(range(9),2))
 assert all(sum(bool(t>>i&1) for i in low)<=2 for t in ns)
 engine=SubsetEngine(25,9,ns)
 for p in engine.inv:engine.inv[p]=(0,0,[])
 w=engine.solve();raw,abc=BareLayout(25,w['positions']).bound(ns,with_rows=True)
 stubs=[frozenset(i+1 for i in range(9) if t>>i&1) for t,n in ns.items() for _ in range(n)]
 independent=independent_rows(25,tuple(w['positions']),stubs)
 assert [(v['A'],v['B'],v['C']) for v in independent]==abc
 assert raw==w['bound']==sum((min(v['A'],v['B'],v['C']) for v in independent),Q())
 record={**z,'selection_index':len(records),'raw_bound':raw,'strict':raw<1,'positions':w['positions'],'all_25_rows_independently_equal':True,'raw_rows':independent,'cpu_seconds':process_time()-tm,'wall_seconds':monotonic()-wt}
 records.append(record);out=save();print(json.dumps({'completed':len(records),'base':z['base'],'low':z['low'],'signature':z['seven_private_signature'],'bound':str(raw),'cpu':record['cpu_seconds']}),flush=True)
out=save()
if '--pilot' in sys.argv:(P/'PILOT.json').write_text(json.dumps(serial(out),indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='records'}),flush=True)
