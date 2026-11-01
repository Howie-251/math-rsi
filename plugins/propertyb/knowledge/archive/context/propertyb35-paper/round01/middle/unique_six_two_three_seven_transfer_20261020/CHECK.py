from pathlib import Path
from math import comb
from itertools import combinations
import json,time
st=time.process_time();P=Path(__file__).resolve().parent
def partitions(n,lo=1):
 if n==0:yield ();return
 for v in range(lo,n+1):
  for tail in partitions(n-v,v):yield (v,)+tail
roles=[]
for a in (2,3):
 for r in range(a+1):
  for b in range(11-2*a,10-r):
   e=2*a+b-11;high_count=20-a-b
   spectra=[]
   for part in partitions(e):
    high=[9]*(high_count-len(part))+[9+v for v in part]
    deg=[6]+[7]*a+[8]*b+high
    assert len(deg)==21 and sum(deg)==175
    W=sum(comb(v,2) for v in deg)
    assert W==636+3*a+b+sum(comb(v,2) for v in part)
    spectra.append({'positive_high_excess_partition':part,'W':W,'Delta':max(deg)})
   roles.append({'a':a,'r_nonunit7':r,'b':b,'high_excess':e,
                 'star_slack':9-r-b,'spectra':spectra})
assert len(roles)==20
assert sum(len(r['spectra']) for r in roles if r['a']==2)==7
assert sum(len(r['spectra']) for r in roles if r['a']==3)==25
direct=[]
for n in (21,22):
 N=n-5;D=comb(N,10);R=comb(N-4,6);B=comb(N-4,10)
 isolated=6*R+28*B
 disjoint=6*R+27*B+comb(N-5,5)+comb(N-5,10)
 cases=[c*R+(33-c)*B+comb(n-10+j,10) for j,c in ((2,5),(3,4),(4,1))]
 assert all(v<D for v in [isolated,disjoint]+cases)
 direct.append({'n':n,'D':D,'R':R,'B':B,'isolated':isolated,
                'disjoint_exception':disjoint,'high_core_j234':cases})
assert direct[0]['high_core_j234']==[6754,6611,6039]
assert direct[1]['high_core_j234']==[17589,18161,18876]
assert 7*1716+26*286==19448 and comb(9,2)==36
assert 7*792+26*220<11440
out={'status':'PASS','scope':'degree-spectrum scalar domain and six explicit direct-coloring counts; no H or trace generation',
     'role_parameter_rows':roles,'parameter_rows':20,'A2_spectrum_role_rows':7,
     'A3_spectrum_role_rows':25,'direct_repair':direct,'cpu_seconds':time.process_time()-st}
(P/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='role_parameter_rows'},indent=2))
