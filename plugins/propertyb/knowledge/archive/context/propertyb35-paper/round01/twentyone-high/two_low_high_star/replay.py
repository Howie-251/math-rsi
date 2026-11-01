"""Independent full-five inclusion-domain reconstruction, actual relabel maps, and exact fixed/joint witness replay."""
from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as Q
import importlib.util,sys,json,time
HERE=Path(__file__).parent;BASE=HERE.parent;ROOT=HERE.parents[4]
spec=importlib.util.spec_from_file_location('old_fixed_replay',ROOT/'context/propertyb35-paper/round01/twentyone-delta5/replay.py');old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)

def parts():
 for a in product(range(3),repeat=3):
  if a[0] or any(a[i]>max(a[:i])+1 for i in (1,2)):continue
  yield tuple(sum(1<<i for i,x in enumerate(a) if x==j) for j in range(max(a)+1))
def key(ns):return tuple(ns.get(str(m),ns.get(m,0)) for m in range(32))
def recover(inc):
 ns={}
 for m in sorted(range(32),key=int.bit_count,reverse=True):ns[m]=inc[m]-sum(v for u,v in ns.items() if u&m==m)
 return ns if min(ns.values())>=0 else None

def main():
 st=time.time();gates=[r for r in json.loads((BASE/'UNIT_PAIRS.json').read_text())['cases'] if r['degrees'][0]==6 and all(d in (8,9) for d in r['degrees'][1:])];lookup={(tuple(r['degrees'][1:]),r['codegrees'][2],r['triple']):r['strict'] for r in gates};gatevals=[old.verify(r) for r in gates]
 assert all(r['strict'] for r in gates if r['codegrees'][2]>=4)
 generated=set();prs=list(combinations(range(3),2))
 for c in (1,2):
  for ds in [(8,8,8),(8,8,9),(8,9,9),(9,9,9)]:
   for P,R in product(parts(),repeat=2):
    together=lambda T,A:int(any(B&A==A for B in T))
    for cs in product(range(1,4),repeat=3):
     if any(lookup[(tuple(ds[i] for i in ij),v,together(T,sum(1<<i for i in ij)))] for T in (P,R) for ij,v in zip(prs,cs)):continue
     for t in range(min(cs)+1):
      hi={1:ds[0],2:ds[1],4:ds[2],3:cs[0],5:cs[1],6:cs[2],7:t};inc={0:35}
      for m in range(1,32):
       A=m>>2;lo=m&3
       if lo==3:inc[m]=c if not A else 0
       elif lo==1:inc[m]=6 if not A else together(P,A)
       elif lo==2:inc[m]=6 if not A else together(R,A)
       else:inc[m]=hi[A]
      ns=recover(inc)
      if ns is not None:generated.add((c,ds,key(ns)))
 dom=json.loads((HERE/'UNPAIRED_THREE_DOMAIN.json').read_text());expected={(r['center_codegree'],tuple(r['neighbor_degrees']),key(r['counts'])) for r in dom['labelled']};assert generated==expected and len(expected)==5296
 reps=dom['orbits'];transports=0
 for r in dom['labelled']:
  rep=reps[r['orbit']];perm=r['from_representative_high_permutation'];swap=r['from_representative_center_swap'];ns={int(m):v for m,v in rep['counts'].items()}
  def move(m):return ((((m&1)<<1)|((m&2)>>1)) if swap else m&3)|sum(1<<(perm[i]+2) for i in range(3) if m>>(i+2)&1)
  moved={move(m):v for m,v in ns.items()};assert key(moved)==key(r['counts']);assert all(rep['degrees'][i+2]==rep['degrees'][perm[i]+2] for i in range(3));transports+=1
 dp=json.loads((HERE/'UNPAIRED_THREE_DP.json').read_text());assert dp['complete'];rr=dp['cases'];assert len(rr)==1416 and all(key(r['counts'])==key(reps[r['id']]['counts']) for r in rr);fixedvals=[old.verify(r) for r in rr]
 jsrc=json.loads((HERE/'UNPAIRED_THREE_JOINT.json').read_text());assert jsrc['complete'];byid={r['id']:r for r in rr};jointvals={};old.joint.check_profile=old.check35
 joint_verified=0
 for z in jsrc['results']:
  r=byid[z['source_id']]
  if Q(z['bound'])<1:
   old.joint.verify(z,v=21,s=5,expected_degrees=r['degrees']);joint_verified+=1
  jointvals[r['id']]=Q(z['bound'])
 assert set(jointvals)=={r['id'] for r in rr if not r['strict']}
 summary=[];residual=[]
 for c in (1,2):
  for ds in [(8,8,8),(8,8,9),(8,9,9),(9,9,9)]:
   rows=[r for r in rr if r['center_codegree']==c and tuple(r['degrees'][2:])==ds];vals={r['id']:jointvals.get(r['id'],Q(r['bound'])) for r in rows};rem=[r['id'] for r in rows if vals[r['id']]>=1];summary.append(dict(center_codegree=c,neighbor_degrees=ds,orbits=len(rows),fixed_strict=sum(r['strict'] for r in rows),final_strict=len(rows)-len(rem),residual_ids=rem))
   residual.extend(dict(byid[i],final_bound=str(vals[i])) for i in rem)
 result=dict(status='PASS',scope=__doc__,independent_domain_labels=len(generated),actual_transports=transports,replayed_pair_gate_profiles=len(gates),fixed_profiles=len(rr),joint_strict_profiles_verified=joint_verified,joint_nonstrict_diagnostics_not_used_as_proof=len(jointvals)-joint_verified,summary=summary,elapsed_seconds=time.time()-st)
 (HERE/'REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');(HERE/'RESIDUAL.json').write_text(json.dumps(dict(scope='Actual three-unpaired double-star necessary residuals after all stored strict certificates',complete=True,cases=residual),indent=2)+'\n');print(result)
if __name__=='__main__':main()
