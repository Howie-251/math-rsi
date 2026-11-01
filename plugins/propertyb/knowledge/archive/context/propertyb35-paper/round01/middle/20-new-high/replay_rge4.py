"""Independent exact domain/orbit and fixed-certificate replay of delta7 r7>=4.
No SciPy, DP, or position search. Explicit Mobius inversion and old-trace capacities.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations,permutations,product
import json,time,sys
HERE=Path(__file__).parent;ROOT=HERE.parents[4];sys.dont_write_bytecode=True
sys.path[:0]=[str(HERE.parent/'twenty_remaining'),str(ROOT/'context/propertyb34/round01/middle-math')]
from audit_core import verify as verify_fixed
import verify_joint_layout as joint

def check35(ns,s,v,expected_degrees=None):
 assert v==20 and sum(ns.values())==35 and all(n>=0 and t.bit_count()<=5 for t,n in ns.items())
 assert all(sum(n for t,n in ns.items() if t>>i&1)==d for i,d in enumerate(expected_degrees))
 return [frozenset(i+1 for i in range(s) if t>>i&1) for t,n in ns.items() for _ in range(n)]
joint.check_profile=check35

def key(ns):return tuple(int(ns.get(t,ns.get(str(t),0))) for t in range(32))
def audit_transports(data,s,outsider=False):
 orbits=data.get('orbits');labelled=data['labelled']
 for r in labelled:
  p=r['from_representative_permutation'];base={int(t):n for t,n in orbits[r['orbit']]['counts'].items()}
  def move(t):return ((t&16) if outsider else 0)|sum(1<<p[i] for i in range(s) if t>>i&1)
  assert key({move(t):n for t,n in base.items()})==key(r['counts'])

def main():
 start=time.time();domain=json.loads((HERE/'FOUR_SEVENS_DOMAIN.json').read_text());expected=set();pairs=list(combinations(range(4),2));trips=list(combinations(range(4),3))
 for ps in product((1,2),repeat=6):
  for ts in product(range(3),repeat=4):
   for q in range(3):
    I={1<<i:7 for i in range(4)};I.update({sum(1<<i for i in S):a for S,a in zip(pairs,ps)});I.update({sum(1<<i for i in S):a for S,a in zip(trips,ts)});I[15]=q
    ns={t:sum((-1)**(u.bit_count()-t.bit_count())*n for u,n in I.items() if u&t==t) for t in range(1,16)};ns[0]=35-sum(ns.values())
    if min(ns.values())>=0:expected.add(key(ns))
 assert len(expected)==674 and expected=={key(r['counts']) for r in domain['labelled']};audit_transports(domain,4)
 dp=json.loads((HERE/'FOUR_SEVENS_DP.json').read_text())['cases'];assert len(dp)==70
 for r in dp:assert verify_fixed(dict(r,quotas=r['certificates']))==Q(r['bound'])
 jr=json.loads((HERE/'FOUR_SEVENS_JOINT.json').read_text())['results'];strictj=[]
 for z in jr:
  if Q(z.get('bound','2'))<1:strictj.append(joint.verify(z,v=20,s=4,expected_degrees=[7]*4))
 remaining={r['id'] for r in dp if Q(r['bound'])>=1}-{z['source_id'] for z in jr if Q(z.get('bound','2'))<1};assert remaining=={0}
 r0=domain['orbits'][0];assert all(c==1 for c in r0['pairs']) and all(c==0 for c in r0['triples']) and r0['four']==0
 five=json.loads((HERE/'FIVE_SEVEN_UNIT.json').read_text());assert verify_fixed(dict(five,quotas=five['certificates']))==Q('4978/5005')
 proj=json.loads((HERE/'R4_PROJECTIONS.json').read_text())['cases'];assert len(proj)==36;lookup={};projectjoint=0
 for r in proj:
  pure=verify_fixed(dict(r,quotas=r['certificates']));strict=pure<1
  if r.get('joint') and Q(r['joint'].get('bound','2'))<1:
   joint.verify(r['joint'],v=20,s=3,expected_degrees=[7,7,r['degree']]);strict=True;projectjoint+=1
  assert strict==r['strict'];lookup[(r['degree'],*r['cross'],r['triple'])]=strict
 ext=json.loads((HERE/'R4_OUTSIDE_DOMAIN.json').read_text());expectedext=set()
 for d in (8,9):
  for p2 in product((0,1),repeat=6):
   for p1 in product(range(5),repeat=4):
    lam=[p1[i]+sum(p for S,p in zip(pairs,p2) if i in S) for i in range(4)]
    if any(c<1 or c>3 for c in lam) or sum(lam)>9:continue
    p0=d-sum(p1)-sum(p2)
    if not 0<=p0<=13:continue
    if any(lookup[(d,lam[i],lam[j],p)] for (i,j),p in zip(pairs,p2)):continue
    ns={0:13-p0,16:p0}
    for i,p in enumerate(p1):ns[1<<i]=4-p;ns[(1<<i)|16]=p
    for S,p in zip(pairs,p2):m=sum(1<<i for i in S);ns[m]=1-p;ns[m|16]=p
    expectedext.add(key(ns))
 assert len(expectedext)==630 and expectedext=={key(r['counts']) for r in ext['labelled']};audit_transports(ext,4,True)
 extdp=json.loads((HERE/'R4_OUTSIDE_DP.json').read_text())['cases'];assert len(extdp)==64
 vals=[verify_fixed(dict(r,quotas=r['certificates'])) for r in extdp];assert all(z<1 for z in vals)
 result=dict(status='PASS',scope=__doc__,four_domain_labelled=674,four_orbits=70,four_dp_strict=66,four_joint_strict=len(strictj),unique_four_residue=0,five_seven_bound='4978/5005',outsider_projections=36,outsider_projection_strict=sum(lookup.values()),outsider_projection_joint_strict=projectjoint,outsider_labelled=630,outsider_orbits=64,outsider_all_strict=True,outsider_max=str(max(vals)),elapsed_seconds=time.time()-start)
 (HERE/'RGE4_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
