"""Independent RGS partitions and explicit Mobius domain for center8+three/four unit9 neighbors.
Replays the minimal complete branch only: no DP, LP, SciPy or position search.
"""
from pathlib import Path
from itertools import combinations,product,permutations
from fractions import Fraction as Q
import json,time,sys
HERE=Path(__file__).parent;sys.dont_write_bytecode=True;sys.path.insert(0,str(HERE.parents[1]/'20-new-high/low_seven_r23'))
from replay_r3 import fixed,joint

def parts(n):
 for a in product(range(n),repeat=n):
  if a[0] or any(a[i]>1+max(a[:i]) for i in range(1,n)):continue
  yield tuple(tuple(i for i in range(n) if a[i]==j) for j in range(max(a)+1))
def inventory(s,part,inc):
 inc=dict(inc);J={0:27}
 for A in range(1,1<<s):J[A]=inc[A]-int(any(all(i in B for i in range(s) if A>>i&1) for B in part))
 ns={1:8-len(part)}
 for B in part:ns[1|sum(1<<(i+1) for i in B)]=1
 for T in range(1<<s):ns[T<<1]=sum((-1)**((A^T).bit_count())*j for A,j in J.items() if A&T==T)
 return ns if min(ns.values())>=0 else None
def key(ns,s):return tuple(ns.get(t,ns.get(str(t),0)) for t in range(1<<(s+1)))
def load(f):return json.loads((HERE/f).read_text())
def main():
 start=time.time();cores=json.loads((HERE.parent/'five_join/FIVE_REMAINDERS.json').read_text())['cases'];energies=[sum(n*int(t).bit_count()*(int(t).bit_count()-1)//2 for t,n in r['counts'].items()) for r in cores];assert len(cores)==49 and min(energies)==14 and max(energies)==21
 old=json.loads((HERE.parents[1]/'20-new-high/DIAGNOSIS.json').read_text())['pairs'];strong=[r for r in old if r['degrees']==[9,9] and r['codegree']>=5];assert len(strong)==5 and all(fixed(r)<1 for r in strong)
 two=[r for r in load('UNIT_TWO.json')['cases'] if r['neighbor_degrees']==[9,9]];assert {(r['neighbor_codegree'],tuple(tuple(B) for B in r['partition'])) for r in two}=={(c,p) for c,p in product(range(1,5),list(parts(2)))};tworel=set();twostrict=0
 for r in two:
  v=fixed(r)
  if r.get('joint') and Q(r['joint'].get('bound','2'))<1:v=Q(joint.verify(r['joint'],v=20,s=3,expected_degrees=[8,9,9])['bound'])
  c=r['neighbor_codegree'];p=tuple(tuple(B) for B in r['partition']);assert key(inventory(2,p,{1:9,2:9,3:c}),2)==key(r['counts'],2);strict=v<1;assert strict==r['strict'] and strict==(c==1 or c==4 and len(p)==1)
  if not strict:tworel.add((c,p))
  else:twostrict+=1
 expected3=set();metadata={}
 for p in parts(3):
  pairs=list(combinations(range(3),2))
  for cc in product(range(2,5),repeat=3):
   if any((c,((0,1),) if any(i in B and j in B for B in p) else ((0,),(1,))) not in tworel for (i,j),c in zip(pairs,cc)):continue
   for t in range(min(cc)+1):
    inc={1<<i:9 for i in range(3)};inc.update({(1<<i)|(1<<j):c for (i,j),c in zip(pairs,cc)});inc[7]=t;ns=inventory(3,p,inc)
    if ns is not None:expected3.add(key(ns,3));metadata[key(ns,3)]=(p,cc,t)
 dp3=[r for r in load('THREE_DP.json')['cases'] if r['neighbor_degrees']==[9]*3];assert len(dp3)==242 and expected3=={key(r['counts'],3) for r in dp3};vals={r['id']:fixed(r) for r in dp3};fixed3=sum(v<1 for v in vals.values());j3=0
 for z in load('THREE_JOINT.json')['results']:
  if z['source_id'] in vals and Q(z.get('bound','2'))<1:vals[z['source_id']]=Q(joint.verify(z,v=20,s=4,expected_degrees=[8,9,9,9])['bound']);j3+=1
 residual={metadata[key(r['counts'],3)] for r in dp3 if vals[r['id']]>=1};assert len(residual)==24
 expected4=set();pairs=list(combinations(range(4),2));triples=list(combinations(range(4),3))
 for p in parts(4):
  for cc in product(range(2,5),repeat=6):
   cp=dict(zip(pairs,cc));opts=[]
   for S in triples:
    ren={i:j for j,i in enumerate(S)};pp=tuple(sorted(tuple(ren[i] for i in B if i in S) for B in p if any(i in S for i in B)));ccc=tuple(cp[ij] for ij in combinations(S,2));opts.append([t for part,cs,t in residual if part==pp and cs==ccc])
   if any(not x for x in opts):continue
   for tt in product(*opts):
    for q in range(min(tt)+1):
     inc={1<<i:9 for i in range(4)};inc.update({(1<<i)|(1<<j):c for (i,j),c in zip(pairs,cc)});inc.update({sum(1<<i for i in S):t for S,t in zip(triples,tt)});inc[15]=q;ns=inventory(4,p,inc)
     if ns is not None:expected4.add(key(ns,4))
 dom=load('FOUR_DOMAIN.json');labelled=[r for r in dom['labelled'] if r['neighbor_degrees']==[9]*4];orbits={r['id']:r for r in dom['orbits'] if r['neighbor_degrees']==[9]*4};assert len(expected4)==733 and len(orbits)==78 and expected4=={key(r['counts'],4) for r in labelled}
 for r in labelled:
  ns=orbits[r['orbit']]['counts'];p=r['from_representative_neighbor_permutation'];move=lambda t:(t&1)|sum(1<<(p[i]+1) for i in range(4) if t>>(i+1)&1);assert key({move(int(t)):n for t,n in ns.items()},4)==key(r['counts'],4)
 maps=[[((t&1)|sum(1<<(p[i]+1) for i in range(4) if t>>(i+1)&1)) for t in range(32)] for p in permutations(range(4))]
 def canonical(ns):
  vv=key(ns,4);return min(tuple(vv[m.index(t)] for t in range(32)) for m in maps)
 assert len({canonical(r['counts']) for r in orbits.values()})==78
 four=[r for r in load('FOUR_DP.json')['cases'] if r['neighbor_degrees']==[9]*4];assert {key(r['counts'],4) for r in four}=={key(r['counts'],4) for r in orbits.values()};v4=[fixed(r) for r in four];assert len(v4)==78 and max(v4)<1
 result=dict(status='PASS',scope=__doc__,old_strong99_double_certificates=5,two_domain=8,two_strict=twostrict,independent_three_domain=len(expected3),three_fixed_strict=fixed3,three_joint_strict=j3,three_residual=24,max_three_accepted_bound=str(max(v for v in vals.values() if v<1)),source_five_core_energy_range=[min(energies),max(energies)],independent_four_labelled=len(expected4),true_neighbor_S4_orbits=78,transport_checks=733,four_fixed_strict=78,max_four_bound=str(max(v4)),elapsed_seconds=time.time()-start)
 (HERE/'NINES_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
