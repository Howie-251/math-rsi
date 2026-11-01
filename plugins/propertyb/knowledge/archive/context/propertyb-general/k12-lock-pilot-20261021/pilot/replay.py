"""Pure-Python big-integer replay of selected exact certificate worst cases.
Not a second full-domain implementation. Imported scalar formulas are the
collaborator's original FixedCertificate, separate from NumPy contractions.
"""
import sys,json,time
from pathlib import Path
sys.path.insert(0,str(Path('context/collaborator-small-k-20261019/m10-m11').resolve()))
from propertyB_k10_k11_certified import FixedCertificate,S,CEIL,C
from propertyB_k10_k11_verified import FastExact
OUT=Path(__file__).resolve().parent
rows=[];t=time.monotonic()
for m in (4647,4660):
 p=OUT/f'M{m}.json'
 if not p.exists():continue
 data=json.loads(p.read_text())
 for mode in dict.fromkeys(r['mode'] for r in data['rows']):
  r=max((r for r in data['rows'] if r['mode']==mode),key=lambda r:r['worst_z'])
  cal=FixedCertificate(12,m)
  z=cal.unlocked(r['v']) if mode=='none' else getattr(cal,mode)(r['v'],*r['worst_profile'])
  assert z==r['worst_z']
  rows.append({'M':m,'v':r['v'],'mode':mode,'profile':r['worst_profile'],'scalar_z':z,'matches':True})
  print(rows[-1],flush=True)
# Exact witnesses why the four given certificate choices fail at M4670,v507.
m=4670;v=507;d0=CEIL(v-1,11)
invalid_two=next(({'d':d,'s_d':2*(v-1)-11*d} for d in range(d0,12*m//v+1) if 2*(v-1)-11*d<=0),None)
Dvals=[(22*((D+1)*v-12*m)-(11*(D+1)-v+2)**2,D,(D+1)*v-12*m) for D in range(d0,m+1) if (D+1)*v>12*m]
best=max(Dvals)
failure={'M':m,'v':v,'two_first_invalid':invalid_two,'three_max_strict_difference':best[0],'three_best_D':best[1],'Z':best[2],'D_domain':[d0,m]}
assert invalid_two and best[0]<=0
# Independently inspect each (v,s) actually accepted for overflow extrema.
safety=[]
for m in (4647,4660):
 p=OUT/f'M{m}.json'
 if not p.exists():continue
 data=json.loads(p.read_text());worstcrit=(0,None);worstend=(0,None);ct=0
 for r in data['rows']:
  s={'none':0,'one':1,'two':2,'three':3}[r['mode']]
  if not s:continue
  cal=FastExact(12,m);_,A,B,W,L=cal.table(r['v'],s)
  c=m*m*int(W.max());e=m*max(int(A.max()),int(B.max()))
  worstcrit=max(worstcrit,(c,[r['v'],s]));worstend=max(worstend,(e,[r['v'],s]));ct+=1
 safety.append({'M':m,'table_count':ct,'max_M_squared_Wmax':worstcrit,'max_M_endpointmax':worstend,'limit':2**63-1})
print('failure',failure,flush=True);print('safety',safety,flush=True)
(OUT/'scalar_replay.json').write_text(json.dumps({'rows':rows,'failure_4670':failure,'overflow':safety,'wall_seconds':time.monotonic()-t},indent=2))
