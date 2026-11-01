import json,sys,time
from pathlib import Path
from math import comb
P=Path(__file__).resolve().parent;data=json.loads((P/'COMPLETE.json').read_text());M=4663;K=12;S=2**52
sys.path.insert(0,str(Path('context/collaborator-small-k-20261019/m10-m11').resolve()))
from propertyB_k10_k11_certified import FixedCertificate
C=lambda n,k:comb(n,k) if n>=k>=0 else 0
ceil=lambda a,b:-(-a//b)
vs=[v for v in range(23,12*M+1) if v*ceil(v-1,11)<=12*M and M*(C(v//2,12)+C((v+1)//2,12))>=C(v,12)]
assert vs==data['candidate_v']==[r['v'] for r in data['rows']]
counts={};worst={};n=0

def add(mode,v,count,z,profile):
 global n
 assert 0<=z<S
 counts[mode]=counts.get(mode,0)+count;n+=count
 if mode not in worst or z>worst[mode]['z']:worst[mode]={'v':v,'z':z,'gap':S-z,'profile':profile}

for r in data['rows']:
 v=r['v'];low=ceil(v-1,11)
 if r['mode']=='none':add('none',v,1,r['worst_z'],[]);continue
 if r['mode']=='three-global':
  D=next(D for D in range(low,M+1) if (D+1)*v>12*M and 22*((D+1)*v-12*M)>(11*(D+1)-v+2)**2)
  assert D==r['D'];assert r['profiles']==2*C(D-low+3,3)
  add('three-global',v,r['profiles'],r['worst_z'],r['worst_profile']);continue
 assert [p['d'] for p in r['parts']]==list(range(low,12*M//v+1))
 subtotal=0
 for p in r['parts']:
  d=p['d']
  if p['mode']=='one':add('one',v,1,p['z'],[d]);subtotal+=1;continue
  sd=2*(v-1)-11*d;assert sd>0 and sd==p['sd']
  # Independent integer inequality establishes both endpoints of the full second-degree range.
  B=p['B'];assert v*d+sd*(B-d)<=12*M<v*d+sd*(B+1-d)
  assert [q['e'] for q in p['sub']]==list(range(d,B+1))
  for q in p['sub']:
   e=q['e']
   if q['mode']=='two':add('two',v,1,q['z'],[d,e]);subtotal+=1;continue
   pool=v-2-(11*d-(v-1))-(11*e-(v-1));R=12*M-v*d-(e-d);F=q['F']
   assert q['pool']==pool>0 and q['R']==R>=0
   assert pool*(F-d)<=R<pool*(F+1-d)
   ct=2*(F-d+1);assert ct==q['profiles'];subtotal+=ct
   w=q['worst_profile'];assert d<=w['f']<=F and w['sorted']==sorted([d,e,w['f']])
   add('three-conditional',v,ct,q['worst_z'],w)
 assert subtotal==r['profiles']
assert n==sum(r['profiles'] for r in data['rows'])
t=time.process_time();replays=[]
for mode,w in worst.items():
 cal=FixedCertificate(12,M);v=w['v'];p=w['profile']
 if mode=='none':z=cal.unlocked(v)
 elif mode in ['one','two']:z=getattr(cal,mode)(v,*p)
 elif mode=='three-global':z=cal.three(v,*p)
 else:z=cal.three(v,p['sorted'],p['triple'])
 assert z==w['z'];replays.append({'mode':mode,**w,'pure_python_matches':True})
summary={'status':'PASS','M':M,'m_lower_bound_candidate':M+1,'baseline':4633,'gain':M+1-4633,'candidate_v':[min(vs),max(vs)],'candidate_v_count':len(vs),'counts':counts,'total_profiles':n,'worst_by_mode':worst,'global_worst':max(worst.values(),key=lambda w:w['z']),'domain_reconstructed_without_driver_import':True,'scalar_replays':replays,'scalar_replay_cpu_seconds':time.process_time()-t,'full_independent_probability_replay':False,'accepted_driver_cpu_seconds':data['cpu_seconds_accepted_drivers']}
(P/'SUMMARY.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
