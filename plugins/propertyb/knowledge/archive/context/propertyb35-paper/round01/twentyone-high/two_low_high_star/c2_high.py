"""c2 small-Q rigid selections: three actual unpaired common-unit points of degrees8810/8910/9910/81010."""
from pathlib import Path
from itertools import product,permutations,combinations
from fractions import Fraction
import sys,json,time,argparse
HERE=Path(__file__).parent;BASE=HERE.parent;ROOT=HERE.parents[4]
sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'))
from subset_position_dp import SubsetEngine

def serial(x):
 if isinstance(x,Fraction):return str(x)
 if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [serial(v) for v in x]
 return x

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--pilot',type=int,default=0);args=parser.parse_args();st=time.time();src=json.loads((BASE/'UNIT_PAIRS.json').read_text())['cases'];gate={(tuple(r['degrees'][1:]),r['codegrees'][2],r['triple']):r['strict'] for r in src if r['degrees'][0]==6}
 parts=[(7,),(1,6),(2,5),(4,3),(1,2,4)];labelled=[];orbits=[];seen={};pairs=[(0,1),(0,2),(1,2)]
 for c in (2,):
  for ds in [(8,8,10),(8,9,10),(9,9,10),(8,10,10)]:
   perms=[p for p in permutations(range(3)) if all(ds[i]==ds[p[i]] for i in range(3))]
   for P,Q in product(parts,repeat=2):
    same=lambda R,ij:int(any(all(B>>i&1 for i in ij) for B in R))
    for cs in product(range(1,4),repeat=3):
     if any(gate[(tuple(ds[i] for i in ij),v,same(R,ij))] for R in (P,Q) for ij,v in zip(pairs,cs)):continue
     for t in range(min(cs)+1):
      inc={1:ds[0],2:ds[1],4:ds[2],3:cs[0],5:cs[1],6:cs[2],7:t};J={A:v-int(any(B&A==A for B in P))-int(any(B&A==A for B in Q)) for A,v in inc.items()};outside={A:sum((-1)**(B.bit_count()-A.bit_count())*v for B,v in J.items() if B&A==A) for A in range(1,8)};outside[0]=23+c-sum(outside.values())
      if min(outside.values())<0:continue
      ns={A<<2:v for A,v in outside.items()};ns[3]=c;ns[1]=6-c-len(P);ns[2]=6-c-len(Q)
      for B in P:ns[1|(B<<2)]=1
      for B in Q:ns[2|(B<<2)]=1
      assert sum(ns.values())==35
      key=(c,ds,tuple(ns.get(m,0) for m in range(32)))
      if key not in seen:
       oid=len(orbits);orbits.append(dict(id=oid,degrees=[6,6]+list(ds),center_codegree=c,partitions=[P,Q],high_codegrees=cs,high_triple=t,counts=ns))
       for perm in perms:
        for swap in (0,1):
         def move(m):return ((((m&1)<<1)|((m&2)>>1)) if swap else m&3)|sum(1<<(perm[i]+2) for i in range(3) if m>>(i+2)&1)
         moved={move(m):v for m,v in ns.items()};seen[(c,ds,tuple(moved.get(m,0) for m in range(32)))]=(oid,perm,swap)
      oid,perm,swap=seen[key];labelled.append(dict(center_codegree=c,neighbor_degrees=ds,counts=ns,orbit=oid,from_representative_high_permutation=perm,from_representative_center_swap=swap))
 (HERE/'C2_HIGH_DOMAIN.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,labelled=labelled,orbits=orbits)),indent=2)+'\n');print('domain',len(labelled),'orbits',len(orbits),flush=True)
 selected=range(len(orbits))
 if args.pilot:selected=sorted(set(round(i*(len(orbits)-1)/(args.pilot-1)) for i in range(args.pilot)))
 old={}
 if not args.pilot and (HERE/'C2_HIGH_PILOT.json').exists():old={r['id']:r for r in json.loads((HERE/'C2_HIGH_PILOT.json').read_text())['cases']}
 out=[]
 for i in selected:
  r=orbits[i]
  if i in old:z=old[i];z['bound']=Fraction(z['bound'])
  else:
   eng=SubsetEngine(21,5,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1
  out.append(z)
 for c in (2,):
  for ds in [(8,8,10),(8,9,10),(9,9,10),(8,10,10)]:
   rr=[r for r in out if r['center_codegree']==c and tuple(r['degrees'][2:])==ds];print(c,ds,'cases',len(rr),'strict',sum(r['strict'] for r in rr),'max',max((r['bound'] for r in rr),default=None),flush=True)
 name='C2_HIGH_PILOT.json' if args.pilot else 'C2_HIGH_DP.json'
 (HERE/name).write_text(json.dumps(serial(dict(scope=__doc__,complete=not args.pilot,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st,flush=True)
if __name__=='__main__':main()
