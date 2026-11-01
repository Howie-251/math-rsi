"""Expanded35-stub independent injection replay; exact nested quotas and joint duals, no DP/SciPy."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[3]
sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math')]
from independent_structure_bounds import independent_rows
import verify_joint_layout as joint

def deduction(ns,pos,i):
 bit=1<<i;ts=sorted(t for t,n in ns.items() if n and t&bit);inv=[]
 for j,t in enumerate(ts):
  for u in ts[j:]:
   cap=comb(ns[t],2) if t==u else ns[t]*ns[u]
   if cap:inv.append([joint.weight(21,pos,t,u,i)+joint.weight(21,pos,u,t,i),cap,t==u==bit])
 degree=sum(ns[t] for t in ts);qt=max(0,(4*degree-20+2)//3);qp=max(0,(4*ns.get(bit,0)-(21-len(pos))+2)//3);loss=Q();left=qp
 for z in sorted(inv):
  if z[2]:take=min(left,z[1]);left-=take;z[1]-=take;loss+=take*z[0]
 assert left==0;left=max(0,qt-qp)
 for z in sorted(inv):take=min(left,z[1]);left-=take;loss+=take*z[0]
 assert left==0
 return loss

def verify(r):
 ns={int(t):n for t,n in r['counts'].items() if n};pos=tuple(r['positions']);s=len(pos)
 assert sum(ns.values())==35 and all(n>0 and t.bit_count()<=5 for t,n in ns.items())
 stubs=[frozenset(i+1 for i in range(s) if t>>i&1) for t,n in ns.items() for _ in range(n)]
 ir=independent_rows(21,pos,stubs);losses={pos[i]:deduction(ns,pos,i) for i in range(s)}
 qs=r.get('quotas',r.get('certificates',None))
 if qs is not None:assert all(losses[pos[i]]==Q(c['loss']) for i,c in enumerate(qs))
 value=sum((min(z['A'],z['B'],z['C']-losses.get(z['k'],Q())) for z in ir),Q());assert value==Q(r['bound'])
 if 'rows' in r:assert all((a['A'],a['B'],a['C'])==(Q(b['A']),Q(b['B']),Q(b['C'])) for a,b in zip(ir,r['rows']))
 return value

def check35(ns,s,v,expected_degrees=None):
 assert v==21 and sum(ns.values())==35 and all(t.bit_count()<=5 and n>=0 for t,n in ns.items())
 assert len(expected_degrees)==s and all(sum(n for t,n in ns.items() if t>>i&1)==d for i,d in enumerate(expected_degrees))
 return [frozenset(i+1 for i in range(s) if t>>i&1) for t,n in ns.items() for _ in range(n)]

def main():
 st=time.time();out=[];total=0
 pilot=json.loads((HERE/'PILOT.json').read_text());sources=[('PILOT.pairs',pilot['pairs']),('PILOT.triples',pilot['triples'])]
 for f in ['STAR_THREE_DP.json','STAR_LOW_DP.json','SIX_SEVEN_FOUR_DP.json','SIX_EIGHTS_FOUR_DP.json','SIX_EIGHTS_FIVE_DP.json','FOUR_SEVENS_DP.json','FIVE_SEVENS_DP.json','FOUR_THREE_SEVENS_DP.json','GENERIC_7788_DP.json','GENERIC_77788_DP.json','GENERIC_7888_DP.json','GENERIC_77888_DP.json']:sources.append((f,json.loads((HERE/f).read_text())['cases']))
 for name,rr in sources:
  vals=[verify(r) for r in rr];out.append(dict(file=name,cases=len(vals),strict=sum(v<1 for v in vals),max_strict=str(max((v for v in vals if v<1),default=Q()))));total+=len(vals)
 joint.check_profile=check35;jouts=[];base=json.loads((HERE/'STAR_LOW_DP.json').read_text())['cases']
 for z in json.loads((HERE/'JOINT_LOW.json').read_text())['results']:
  if Q(z.get('bound','2'))>=1:continue
  r=base[z['source_id']];assert {int(t):n for t,n in z['counts'].items() if n}=={int(t):n for t,n in r['counts'].items() if n}
  one=joint.verify(z,v=21,s=4,expected_degrees=[5]+r['neighbor_degrees']);one['source_id']=z['source_id'];jouts.append(one)
 result=dict(status='PASS',scope=__doc__,fixed_profiles=total,expanded_stubs_per_profile=35,ordered_distinct_pairs_per_profile=1190,independent_rows=21*total,results=out,joint_results=jouts,elapsed_seconds=time.time()-st)
 (HERE/'REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items() if k not in ['results','joint_results']});print(out)
if __name__=='__main__':main()
