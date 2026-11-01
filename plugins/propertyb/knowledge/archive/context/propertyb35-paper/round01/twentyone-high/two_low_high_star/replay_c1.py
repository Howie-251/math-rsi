"""Independent full-inclusive domains, actual relabel transports and exact terminal fixed/joint certificates for a0,c1."""
from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as Q
import importlib.util,json,time
HERE=Path(__file__).parent;BASE=HERE.parent;ROOT=HERE.parents[4]
spec=importlib.util.spec_from_file_location('double_star_replay',HERE/'replay.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);old=mod.old

def parts(n):
 def go(i,bs):
  if i==n:yield tuple(sum(1<<j for j in B) for B in bs);return
  for k in range(len(bs)):
   new=[list(B) for B in bs];new[k].append(i);yield from go(i+1,new)
  yield from go(i+1,bs+[[i]])
 yield from go(0,[])
def mobius(inc,s):
 ns=[inc[m] for m in range(1<<s)]
 for i in range(s):
  for m in range(1<<s):
   if not m>>i&1:ns[m]-=ns[m|(1<<i)]
 return tuple(ns)
def inclusive(P,R,hi,s):
 inc={0:35}
 for m in range(1,1<<s):
  A=m>>2;lo=m&3
  if lo==3:inc[m]=int(A==0)
  elif lo in (1,2):inc[m]=6 if not A else int(any(B&A==A for B in (P if lo==1 else R)))
  else:inc[m]=hi[A]
 return inc

def main():
 st=time.time();dp=json.loads((HERE/'UNPAIRED_THREE_DP.json').read_text())['cases'];jj={z['source_id']:Q(z['bound']) for z in json.loads((HERE/'UNPAIRED_THREE_JOINT.json').read_text())['results']};remaining={r['id'] for r in dp if r['center_codegree']==1 and jj.get(r['id'],Q(r['bound']))>=1};allowed={}
 for r in json.loads((HERE/'UNPAIRED_THREE_DOMAIN.json').read_text())['labelled']:
  if r['orbit'] in remaining:allowed.setdefault(tuple(r['neighbor_degrees']),set()).add(mod.key(r['counts']))
 assert len(remaining)==9
 generated=set();trs=list(combinations(range(4),3))
 for ds in [(8,8,8,8),(8,8,8,9),(8,8,9,9),(8,9,9,9),(9,9,9,9)]:
  for P,R in product(parts(4),repeat=2):
   for ts in product((0,1),repeat=4):
    hi={1<<i:ds[i] for i in range(4)}|{sum(1<<i for i in S):2 for S in combinations(range(4),2)}|{sum(1<<i for i in S):t for S,t in zip(trs,ts)}|{15:0};inc=inclusive(P,R,hi,6)
    good=True
    for S in trs:
     lift=(0,1)+tuple(i+2 for i in S);proj={m:inc[sum(1<<lift[i] for i in range(5) if m>>i&1)] for m in range(32)}
     if mobius(proj,5) not in allowed[tuple(ds[i] for i in S)]:good=False;break
    if not good:continue
    for q in range(min(ts)+1):
     inc[60]=q;ns=mobius(inc,6)
     if min(ns)>=0:generated.add((ds,ns))
 four=json.loads((HERE/'C1_FOUR_DOMAIN.json').read_text());assert generated=={(tuple(r['neighbor_degrees']),tuple(r['counts'].get(str(m),0) for m in range(64))) for r in four['labelled']};assert len(generated)==127
 gates=[r for r in json.loads((BASE/'UNIT_PAIRS.json').read_text())['cases'] if r['degrees']==[6,8,10]];gate={(r['codegrees'][2],r['triple']):r['strict'] for r in gates};gvals=[old.verify(r) for r in gates];assert all(r['strict'] for r in gates if r['codegrees'][2]>=4)
 mixed=set()
 for P,R in product(parts(3),repeat=2):
  same=lambda T,A:int(any(B&A==A for B in T))
  if same(P,3)+same(R,3)>1:continue
  for a,b in product(range(1,4),repeat=2):
   if any(gate[(v,same(T,A))] for T in (P,R) for A,v in [(5,a),(6,b)]):continue
   for t in range(min(2,a,b)+1):
    inc=inclusive(P,R,{1:8,2:8,4:10,3:2,5:a,6:b,7:t},5);ns=mobius(inc,5)
    if min(ns)>=0:mixed.add(ns)
 md=json.loads((HERE/'C1_8810_DOMAIN.json').read_text());assert mixed=={mod.key(r['counts']) for r in md['labelled']};assert len(mixed)==290
 results=[];old.joint.check_profile=old.check35
 for tag,s,dom in [('C1_FOUR',6,four),('C1_8810',5,md)]:
  for r in dom['labelled']:
   rep=dom['orbits'][r['orbit']];perm=r['from_representative_high_permutation'];swap=r['from_representative_center_swap'];ns={int(m):v for m,v in rep['counts'].items()}
   def move(m):return ((((m&1)<<1)|((m&2)>>1)) if swap else m&3)|sum(1<<(perm[i]+2) for i in range(s-2) if m>>(i+2)&1)
   moved={move(m):v for m,v in ns.items()};assert tuple(moved.get(m,0) for m in range(1<<s))==tuple(r['counts'].get(str(m),0) for m in range(1<<s));assert all(rep['degrees'][i+2]==rep['degrees'][perm[i]+2] for i in range(s-2))
  rows=json.loads((HERE/f'{tag}_DP.json').read_text())['cases'];assert all(tuple(r['counts'].get(str(m),0) for m in range(1<<s))==tuple(dom['orbits'][r['id']]['counts'].get(str(m),0) for m in range(1<<s)) for r in rows);vals={r['id']:old.verify(r) for r in rows};joint=json.loads((HERE/f'{tag}_JOINT.json').read_text());assert joint['complete']
  assert {z['source_id'] for z in joint['results']}=={r['id'] for r in rows if not r['strict']}
  byid={r['id']:r for r in rows}
  for z in joint['results']:
   r=byid[z['source_id']];old.joint.verify(z,v=21,s=s,expected_degrees=r['degrees']);vals[r['id']]=Q(z['bound'])
  assert all(v<1 for v in vals.values());results.append(dict(file=tag,independent_labelled=len(dom['labelled']),actual_transports=len(dom['labelled']),fixed_profiles=len(rows),joint_profiles=len(joint['results']),max_final_bound=str(max(vals.values()))))
 result=dict(status='PASS',scope=__doc__,prior_three_unpaired_replay='REPLAY.json',new_pair_gate_profiles=len(gates),results=results,elapsed_seconds=time.time()-st);(HERE/'C1_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
if __name__=='__main__':main()
