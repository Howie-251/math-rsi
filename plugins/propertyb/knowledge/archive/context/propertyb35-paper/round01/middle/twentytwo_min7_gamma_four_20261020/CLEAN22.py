from pathlib import Path
from collections import Counter
from fractions import Fraction
import json,sys,time
P=Path(__file__).resolve().parent;R=P.parents[4];sys.dont_write_bytecode=True;sys.path.insert(0,str(R/'context/propertyb34/round01/high-math'))
from subset_position_dp import SubsetEngine
start=time.process_time();src=json.loads((P/'FIXED_RESULT.json').read_text())['nonstrict']
def comps(n,k):
 if k==1:yield(n,);return
 for a in range(n+1):
  for t in comps(n-a,k-1):yield(a,)+t
out=[];allcount=0;by=[]
for sid,z in enumerate(src):
 counts=Counter();fails=[];checked=0
 for d in range(7,z['clean_degree_upper']+1):
  for inc in comps(d-5,5):
   s=[a+1 for a in inc]
   if any(a>b for a,b in zip(s,z['attachments'])):continue
   allcount+=1;counts[d]+=1
   ns=Counter({int(m)<<1:n for m,n in z['counts'].items()})
   for v,n in enumerate(s):ns[1<<(v+1)]-=n;ns[(1<<(v+1))|1]+=n
   assert min(ns.values())>=0 and sum(ns.values())==35
   e=SubsetEngine(22,6,ns);e.inv={p:(0,0,[]) for p in e.inv};vals=[]
   for slot in (1,9,10,11,20,21):
    if slot in z['positions']:continue
    pos=(slot,)+tuple(z['positions']);lock={k:1<<v for v,k in enumerate(pos)};left=0;U=0
    for k in range(1,23):bit=lock.get(k,0);U+=e.value(k,left,bit);left|=bit
    vals.append((Fraction(U,e.D),pos))
   U,pos=min(vals);entry={'source':sid,'degree_z':d,'s':s,'counts':dict(ns),'positions':pos,'bound':str(U),'strict':U<1};out.append(entry);checked+=1
   if U>=1:fails.append(entry)
   if len(out)==1:
    (P/'CLEAN_PILOT.json').write_text(json.dumps({'status':'ONE_OLD_SLOT22_PILOT','case':entry,'cpu_seconds':time.process_time()-start},indent=2)+'\n');print('PILOT',U,time.process_time()-start,flush=True)
   if time.process_time()-start>3:raise RuntimeError('3CPU limit')
 by.append({'source':sid,'traces':z['traces'],'attachments':z['attachments'],'F_degrees':z['F_degrees'],'clean_lower':z['clean_lower'],'degree_upper':z['clean_degree_upper'],'counts_by_degree':dict(counts),'checked':checked,'nonstrict':len(fails)})
r={'status':'COMPLETE_CLEAN22_NECESSARY_DOMAIN','scope':'Only the30 fixed-five failures; guaranteed clean degree7..rmax, full positive star compositions with s<=a; N22/free16 zero-quota, z in old6 slots excluding occupied positions. No solve/search/new layouts.','sources':by,'domain':allcount,'strict':sum(z['strict'] for z in out),'nonstrict':sum(not z['strict'] for z in out),'all_source_clean_stars_strict':[z['source'] for z in by if not z['nonstrict']],'remaining_sources':[z['source'] for z in by if z['nonstrict']],'cases':out,'cpu_seconds':time.process_time()-start}
(P/'CLEAN_RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print({k:v for k,v in r.items() if k not in ['sources','cases']})
for z in by:
 if z['nonstrict']:print('TAIL',z)
