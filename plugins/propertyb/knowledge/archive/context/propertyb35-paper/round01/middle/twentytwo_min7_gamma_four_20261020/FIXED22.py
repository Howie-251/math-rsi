from pathlib import Path
from fractions import Fraction
import json,sys,time
P=Path(__file__).resolve().parent;R=P.parents[4];start=time.process_time();sys.dont_write_bytecode=True;sys.path.insert(0,str(R/'context/propertyb34/round01/high-math'))
from subset_position_dp import SubsetEngine
rows=json.loads((P/'DOMAIN.json').read_text())['profiles'];menu=[tuple(z['positions']) for z in json.loads((P/'PILOT_RESULT.json').read_text())['all_fixed']];out=[]
for i,z in enumerate(rows):
 e=SubsetEngine(22,5,z['counts']);e.inv={p:(0,0,[]) for p in e.inv};vs=[]
 for pos in menu:
  lock={k:1<<v for v,k in enumerate(pos)};left=0;U=0
  for k in range(1,23):bit=lock.get(k,0);U+=e.value(k,left,bit);left|=bit
  vs.append((Fraction(U,e.D),pos))
 U,pos=min(vs);out.append({**z,'bound':str(U),'positions':pos,'strict':U<1,'all_fixed':[{'positions':p,'bound':str(v)} for v,p in vs]})
 if time.process_time()-start>4:break
remaining=[z for z in out if not z['strict']]
r={'status':'COMPLETE_OLD16_FIXED22' if len(out)==len(rows) else 'PARTIAL_CPU_CUTOFF','scope':'Actual22 points/free17 zero-quota evaluation of exactly the old16 five-lock positions; no solve/search/new layouts.','input_profiles':len(rows),'checked':len(out),'strict':len(out)-len(remaining),'remaining':len(remaining),'maximum_strict_bound':str(max((Fraction(z['bound']) for z in out if z['strict']),default=0)),'cpu_seconds':time.process_time()-start,'cases':out,'nonstrict':remaining}
(P/'FIXED_RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print({k:v for k,v in r.items() if k not in ['cases','nonstrict']})
for z in remaining:print(z['traces'],z['attachments'],z['F_degrees'],z['bound'],'clean',z['clean_lower'],z['clean_degree_upper'])
