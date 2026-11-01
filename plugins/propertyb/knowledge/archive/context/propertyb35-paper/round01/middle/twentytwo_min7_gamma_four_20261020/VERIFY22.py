from pathlib import Path
from fractions import Fraction
from itertools import combinations
from collections import Counter
from math import comb
import json,sys,time
P=Path(__file__).resolve().parent;R=P.parents[4];start=time.process_time();sys.dont_write_bytecode=True;sys.path.insert(0,str(R/'computations'))
from independent_structure_bounds import independent_rows
five=json.loads((P/'FIXED_RESULT.json').read_text());star=json.loads((P/'CLEAN_RESULT.json').read_text());geom=json.loads((P.parent/'three_nonunit_direct_repair_20261020/RESULT.json').read_text())['orbits']
def C(n,r):return comb(n,r) if 0<=r<=n else 0
# Independently reconstruct all unsafe anchor attachment sets with n22 binomial counts.
cache={};domain={}
for row in geom:
 tr=tuple(row['traces']);hs=[sum(m>>v&1 for m in tr) for v in range(5)];allowed=[]
 for v in range(5):
  types=tuple(sorted(-1 if m>>v&1 else m.bit_count() for m in tr))
  if types not in cache:
   aa=[]
   for a in range(32):
    unsafe=True
    for red in range(18):
     extra=sum(0 if t==-1 else C(12,red-5)+C(12,red) if not t else C(12+t,red) for t in types)
     U=a*C(13,red-4)+(31-a)*C(13,red)-max(a-1,0)*C(9,red-8)+extra
     if U<C(17,red):unsafe=False;break
    if unsafe:aa.append(a)
   cache[types]=aa
  allowed.append([a for a in cache[types] if 1+a+hs[v]>=7 and 4*a+sum(5-m.bit_count() for m in tr if m>>v&1)>=17])
 def recurse(i,left,a):
  if i==5:
   if not left:domain[(tr,tuple(a))]=[1+x+h for x,h in zip(a,hs)]
   return
  if not allowed[i]:return
  lower=sum(min(z) for z in allowed[i+1:]) if all(allowed[i+1:]) else 100
  upper=sum(max(z) for z in allowed[i+1:]) if all(allowed[i+1:]) else -100
  for x in allowed[i]:
   if lower<=left-x<=upper:recurse(i+1,left-x,a+[x])
 recurse(0,31,[])
assert len(domain)==277 and domain=={(tuple(z['traces']),tuple(z['attachments'])):z['F_degrees'] for z in five['cases']}
expected={}
for sid,z in enumerate(five['nonstrict']):
 s=sum(m.bit_count() for m in z['traces']);cl=s+2;dirty=15-s;out=139-s;rmax=(out-7*dirty)//cl
 assert rmax==z['clean_degree_upper'] and 7*dirty+(rmax+1)*cl>out
 masks=[31]+z['traces']+[1<<v for v,a in enumerate(z['attachments']) for _ in range(a)]
 for r in range(7,rmax+1):
  for cuts in combinations(range(1,r),4):
   q=(0,)+cuts+(r,);ss=tuple(q[j+1]-q[j] for j in range(5))
   if any(x>a for x,a in zip(ss,z['attachments'])):continue
   rem=list(ss);lift=[]
   for m in masks:
    bit=0
    if m.bit_count()==1:
     v=m.bit_length()-1
     if rem[v]:rem[v]-=1;bit=1
    lift.append(2*m+bit)
   assert not any(rem)
   expected[(sid,r,ss)]=lift
assert len(expected)==1045
actual={(z['source'],z['degree_z'],tuple(z['s'])):Counter({int(m):n for m,n in z['counts'].items() if n}) for z in star['cases']}
assert {k:Counter(v) for k,v in expected.items()}==actual
count=0;replays=[]
for kind,zs in [('five',five['cases']),('six',star['cases'])]:
 for z in zs:
  if kind=='five':masks=[31]+z['traces']+[1<<v for v,a in enumerate(z['attachments']) for _ in range(a)];locks=5
  else:masks=expected[(z['source'],z['degree_z'],tuple(z['s']))];locks=6
  assert len(masks)==35
  stubs=[frozenset(v+1 for v in range(locks) if m>>v&1) for m in masks]
  ir=independent_rows(22,tuple(z['positions']),stubs);U=sum((min(x['A'],x['B'],x['C']) for x in ir),Fraction())
  assert U==Fraction(z['bound']) and (U<1)==z['strict'];count+=22
  replays.append({'kind':kind,'bound':str(U),'strict':U<1})
  if time.process_time()-start>4:raise RuntimeError('4CPU replay cutoff')
r={'status':'PASS_COMPLETE22_DOMAINS_AND1322_FIXED_REPLAYS','scope':'Fresh22 anchor threshold/min7/17outside cover reconstruction; independent cut-composition clean-star domain; exact expanded35 indices1190ordered pairs and22pivot rows, no quota. All primary best bounds including failures replayed.','N':22,'five_domain':277,'five_strict':247,'five_tails':30,'clean_domain':1045,'clean_strict':741,'clean_failed':304,'remaining_source_profiles':26,'replayed_inputs':len(replays),'replayed_rows':count,'cpu_seconds':time.process_time()-start,'bounds':replays}
(P/'VERIFY_RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print({k:v for k,v in r.items() if k!='bounds'})
