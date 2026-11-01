"""Independent actual shared-view census and exact witness replay for bounded c2 diagnostics; no global coloring claim."""
from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as Q
import importlib.util,json,time
HERE=Path(__file__).parent;BASE=HERE.parent
spec=importlib.util.spec_from_file_location('c1_independent_replay',HERE/'replay_c1.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);old=mod.old

def moments(ns,s):
 ns={int(m):v for m,v in ns.items()};return {m:sum(v for u,v in ns.items() if u&m==m) for m in range(1,1<<s)}
def lift(inc,S):return {sum(1<<S[i] for i in range(len(S)) if m>>i&1):v for m,v in inc.items()}
def inc5(P,R,ds,cs,t):
 hi={1:ds[0],2:ds[1],4:ds[2],3:cs[0],5:cs[1],6:cs[2],7:t};inc={0:35}
 for m in range(1,32):
  A=m>>2;lo=m&3
  if lo==3:inc[m]=2 if not A else 0
  elif lo in (1,2):inc[m]=6 if not A else int(any(B&A==A for B in (P if lo==1 else R)))
  else:inc[m]=hi[A]
 return inc

def main():
 st=time.time();gate_rows=[r for r in json.loads((BASE/'UNIT_PAIRS.json').read_text())['cases'] if r['degrees'][0]==6 and all(d in (8,9,10) for d in r['degrees'][1:])];gate={(tuple(r['degrees'][1:]),r['codegrees'][2],r['triple']):r['strict'] for r in gate_rows};gatevals=[old.verify(r) for r in gate_rows];assert all(r['strict'] for r in gate_rows if r['codegrees'][2]>=4)
 highdom=json.loads((HERE/'C2_HIGH_DOMAIN.json').read_text());seen=set();prs=list(combinations(range(3),2))
 for ds in [(8,8,10),(8,9,10),(9,9,10),(8,10,10)]:
  for P,R in product(mod.parts(3),repeat=2):
   same=lambda T,A:int(any(B&A==A for B in T))
   for cs in product(range(1,4),repeat=3):
    if any(gate[(tuple(ds[i] for i in S),v,same(T,sum(1<<i for i in S)))] for T in (P,R) for S,v in zip(prs,cs)):continue
    for t in range(min(cs)+1):
     ns=mod.mobius(inc5(P,R,ds,cs,t),5)
     if min(ns)>=0:seen.add((ds,ns))
 assert seen=={(tuple(r['neighbor_degrees']),mod.mod.key(r['counts'])) for r in highdom['labelled']};assert len(seen)==2466
 # Reconstruct four-Q from full-five inclusive joins, rather than enumerating
 # two partitions and six independent pair codegrees.
 src=json.loads((HERE/'UNPAIRED_THREE_DP.json').read_text())['cases'];jj={z['source_id']:Q(z['bound']) for z in json.loads((HERE/'UNPAIRED_THREE_JOINT.json').read_text())['results']};rem={r['id'] for r in src if r['center_codegree']==2 and jj.get(r['id'],Q(r['bound']))>=1};bydeg={}
 for r in json.loads((HERE/'UNPAIRED_THREE_DOMAIN.json').read_text())['labelled']:
  if r['orbit'] in rem:bydeg.setdefault(tuple(r['neighbor_degrees']),[]).append(moments(r['counts'],5))
 seen=set();joins=0
 for ds in [(8,8,8,8),(8,8,8,9),(8,8,9,9),(8,9,9,9),(9,9,9,9)]:
  options=[]
  for S in combinations(range(4),3):options.append([lift(r,(0,1)+tuple(i+2 for i in S)) for r in bydeg[tuple(ds[i] for i in S)]])
  keysets=[];known=set();buckets=[]
  for opt in options:
   ks=tuple(sorted(known&set(opt[0])));keysets.append(ks);b={}
   for r in opt:b.setdefault(tuple(r[k] for k in ks),[]).append(r)
   buckets.append(b);known|=set(opt[0])
  def go(j,inc):
   if j==len(options):yield inc;return
   for r in buckets[j].get(tuple(inc[k] for k in keysets[j]),[]):yield from go(j+1,inc|r)
  for inc in go(0,{}):
   joins+=1;assert set(inc)==set(range(1,64))-{60,61,62,63}
   px=int(all(inc[1|(1<<(i+2))|(1<<(j+2))]==1 for i,j in combinations(range(4),2)));py=int(all(inc[2|(1<<(i+2))|(1<<(j+2))]==1 for i,j in combinations(range(4),2)))
   for q in range(min(inc[sum(1<<(i+2) for i in S)] for S in combinations(range(4),3))+1):
    ns=mod.mobius({0:35}|inc|{60:q,61:px,62:py,63:0},6)
    if min(ns)>=0:seen.add((ds,ns))
 fourdom=json.loads((HERE/'C2_FOUR_DOMAIN.json').read_text());assert seen=={(tuple(r['neighbor_degrees']),tuple(r['counts'].get(str(m),0) for m in range(64))) for r in fourdom['labelled']};assert len(seen)==3288
 results=[];residual=[];old.joint.check_profile=old.check35
 for tag,s,dom in [('C2_FOUR',6,fourdom),('C2_HIGH',5,highdom)]:
  for r in dom['labelled']:
   rep=dom['orbits'][r['orbit']];perm=r['from_representative_high_permutation'];swap=r['from_representative_center_swap'];ns={int(m):v for m,v in rep['counts'].items()}
   def move(m):return ((((m&1)<<1)|((m&2)>>1)) if swap else m&3)|sum(1<<(perm[i]+2) for i in range(s-2) if m>>(i+2)&1)
   moved={move(m):v for m,v in ns.items()};assert tuple(moved.get(m,0) for m in range(1<<s))==tuple(r['counts'].get(str(m),0) for m in range(1<<s));assert all(rep['degrees'][i+2]==rep['degrees'][perm[i]+2] for i in range(s-2))
  rows=json.loads((HERE/f'{tag}_DP.json').read_text())['cases'];byid={r['id']:r for r in rows};assert all(tuple(r['counts'].get(str(m),0) for m in range(1<<s))==tuple(dom['orbits'][r['id']]['counts'].get(str(m),0) for m in range(1<<s)) for r in rows);vals={r['id']:old.verify(r) for r in rows};joint=json.loads((HERE/f'{tag}_JOINT.json').read_text());assert joint['complete'];assert {z['source_id'] for z in joint['results']}=={r['id'] for r in rows if not r['strict']};jstrict=0
  for z in joint['results']:
   r=byid[z['source_id']]
   if Q(z['bound'])<1:old.joint.verify(z,v=21,s=s,expected_degrees=r['degrees']);jstrict+=1
   vals[r['id']]=Q(z['bound'])
  summary=[]
  for ds in sorted({tuple(r['degrees'][2:]) for r in rows}):
   rr=[r for r in rows if tuple(r['degrees'][2:])==ds];ids=[r['id'] for r in rr if vals[r['id']]>=1];summary.append(dict(neighbor_degrees=ds,orbits=len(rr),residual_ids=ids));residual.extend(dict(byid[i],source=tag,final_bound=str(vals[i])) for i in ids)
  results.append(dict(file=tag,independent_labelled=len(dom['labelled']),actual_transports=len(dom['labelled']),fixed_profiles=len(rows),strict_joint_profiles_verified=jstrict,nonstrict_joint_diagnostics_not_used_as_proof=len(joint['results'])-jstrict,summary=summary))
 result=dict(status='PASS',scope=__doc__,new_gate_profiles=len(gate_rows),four_Q_precompletion_joins=joins,results=results,elapsed_seconds=time.time()-st);(HERE/'C2_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');(HERE/'C2_RESIDUAL.json').write_text(json.dumps(dict(scope='Necessary remaining actual c2 inputs; not a global obstruction or coloring proof',cases=residual),indent=2)+'\n');print(result)
if __name__=='__main__':main()
