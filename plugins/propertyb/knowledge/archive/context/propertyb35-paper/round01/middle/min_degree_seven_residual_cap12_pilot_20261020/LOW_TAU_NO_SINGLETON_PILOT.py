"""One actual tau10 source from S90 with no singleton: eight7 pool avoids unique high-row lambda1 point; only old4 fifth-lock positions. Stop on first failure."""
from pathlib import Path
from itertools import product
from fractions import Fraction
import json,time,sys
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'));sys.dont_write_bytecode=True;from subset_position_dp import SubsetEngine
st=time.process_time();r=json.loads((P/'RESULT.json').read_text());f=next(z for z in r['all_nonstrict'] if not z['legacy'] and z['quad']==[9,10,10,11] and z['K6_tau_cost']==10 and sum(z['counts'][m] for m in (1,2,4,8))==0);mu=f['counts'];pairs=(3,5,6,9,10,12);high=f['degrees'].index(11);domain=[]
for cp in product(*(range(min(mu[m],2)+1) for m in pairs)):
 c=dict(zip(pairs,cp));row=[sum(n for m,n in c.items() if m>>i&1) for i in range(4)];c0=7-sum(cp)
 if not 0<=c0<=mu[0] or not all(1<=a<=2 for a in row) or row[high]!=2:continue
 ns={}
 for m,n in enumerate(mu):
  take=c.get(m,0) if m else c0
  if n-take:ns[2*m]=n-take
  if take:ns[2*m+1]=take
 domain.append({'cp':cp,'c0':c0,'row':row,'counts':ns})
result=[]
for d in domain:
 e=SubsetEngine(21,5,d['counts']);e.inv={m:(0,0,[]) for m in e.inv};vals=[]
 for zpos in (1,10,11,12):
  pos=(zpos,8,9,20,21);locks={k:1<<i for i,k in enumerate(pos)};left=0;u=0
  for at in range(1,22):pivot=locks.get(at,0);u+=e.value(at,left,pivot);left|=pivot
  vals.append({'positions':pos,'bound':str(Fraction(u,e.D)),'strict':u<e.D})
 d['menu']=vals;d['best']=min(vals,key=lambda z:Fraction(z['bound']));result.append(d)
 if not d['best']['strict']:break
out={'status':'FIRST_FAILURE_STOP' if not result[-1]['best']['strict'] else 'COMPLETE_ONE_SOURCE','scope':__doc__,'source_Kcounts':mu,'source_Kdegrees':f['degrees'],'actual_global_spectrum_id':90,'actual_tau':10,'K6_cost':10,'seven_pool':8,'avoid_singleton_union_at_most':0,'high_degree11_K_row_to_outside':33,'all_outside_lambda_le2':True,'complete_necessary_lift_domain_size':len(domain),'processed_prefix':len(result),'cases':result,'cpu_seconds':time.process_time()-st};(P/'LOW_TAU_NO_SINGLETON_PILOT.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],'DOMAIN',len(domain),'PREFIX',len(result),'LAST',result[-1]['best'],'CPU',out['cpu_seconds'])
