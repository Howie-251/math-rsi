"""a7=4: four actual unit7 residuals plus one guaranteed unit8/9, one real degree6-center partition."""
from pathlib import Path
from itertools import product,combinations,permutations
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;BASE=HERE.parent;ROOT=HERE.parents[5]
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(BASE.parent/'two_low_high_star')]
from subset_position_dp import SubsetEngine
from unpaired_three import serial

def moments(ns,s):
 ns={int(m):v for m,v in ns.items()};return {m:sum(v for u,v in ns.items() if u&m==m) for m in range(1,1<<s)}
def part(ns):return tuple(sorted(int(m)>>1 for m,v in ns.items() if v and int(m)&1 and int(m)>>1))
def recover(P,hi):
 J={A:v-int(any(B&A==A for B in P)) for A,v in hi.items()};outside={A:sum((-1)**(B.bit_count()-A.bit_count())*v for B,v in J.items() if B&A==A) for A in range(1,32)};outside[0]=29-sum(outside.values())
 if min(outside.values())<0:return None
 ns={A<<1:v for A,v in outside.items()};ns[1]=6-len(P)
 for B in P:ns[1|(B<<1)]=1
 return ns

def main():
 st=time.time();src=json.loads((BASE/'FOUR7_DP.json').read_text())['cases'];jj={z['source_id']:Q(z['bound']) for z in json.loads((BASE/'FOUR7_JOINT.json').read_text())['results']};rem={r['id'] for r in src if jj.get(r['id'],Q(r['bound']))>=1};bases=[(part(r['counts']),{m>>1:v for m,v in moments(r['counts'],5).items() if not m&1}) for r in json.loads((BASE/'FOUR7_DOMAIN.json').read_text())['labelled'] if r['orbit'] in rem];gate={(r['degrees'][2],r['codegrees'][2],r['triple']):r['strict'] for r in json.loads((BASE/'UNIT7_GATES.json').read_text())['cases'] if r['degrees'][2] in (8,9)};labels=[];orbits=[];seen={};seven_pairs=list(combinations(range(4),2));seven_triples=list(combinations(range(4),3))
 for d in (8,9):
  for P4,hi4 in bases:
   extensions=[tuple(sorted((*P4,16)))]+[tuple(sorted((B|16) if j==k else B for j,B in enumerate(P4))) for k in range(len(P4)) if P4[k].bit_count()<4]
   for P in extensions:
    same=lambda A:int(any(B&A==A for B in P))
    for cs in product(range(1,4),repeat=4):
     if any(gate[(d,c,same((1<<i)|16))] for i,c in enumerate(cs)):continue
     fixed=hi4|{16:d}|{(1<<i)|16:c for i,c in enumerate(cs)}
     for ts in product((0,1),repeat=6):
      inc=fixed|{sum(1<<i for i in S)|16:v for S,v in zip(seven_pairs,ts)};quad_opts=[]
      for S in seven_triples:
       A=sum(1<<i for i in S);quad_opts.append(range(min(inc[A],min(inc[(1<<i)|(1<<j)|16] for i,j in combinations(S,2)))+1))
      for qs in product(*quad_opts):
       hi=inc|{sum(1<<i for i in S)|16:v for S,v in zip(seven_triples,qs)}|{31:0};ns=recover(P,hi)
       if ns is None:continue
       assert sum(ns.values())==35
       k=(d,tuple(ns.get(m,0) for m in range(64)))
       if k not in seen:
        oid=len(orbits);orbits.append(dict(id=oid,degrees=[6]+[7]*4+[d],center_partition=P,counts=ns))
        for perm in permutations(range(4)):
         def move(m):return(m&1)|(m&32)|sum(1<<(perm[i]+1) for i in range(4) if m>>(i+1)&1)
         moved={move(m):v for m,v in ns.items()};seen[(d,tuple(moved.get(m,0) for m in range(64)))]=(oid,perm)
       oid,perm=seen[k];labels.append(dict(outsider_degree=d,counts=ns,orbit=oid,from_representative_seven_permutation=perm))
 (HERE/'DOMAIN.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,labelled=labels,orbits=orbits)),indent=2)+'\n');print('domain',len(labels),'orbits',len(orbits),flush=True)
 out=[]
 for r in orbits:
  eng=SubsetEngine(21,6,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;out.append(z)
 for d in (8,9):
  rr=[r for r in out if r['degrees'][-1]==d];print(d,'orbits',len(rr),'strict',sum(r['strict'] for r in rr),'max',max((r['bound'] for r in rr),default=None),flush=True)
 (HERE/'DP.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st,flush=True)
if __name__=='__main__':main()
