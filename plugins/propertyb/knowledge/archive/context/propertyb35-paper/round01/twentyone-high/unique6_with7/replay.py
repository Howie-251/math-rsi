"""Independent inclusion recovery, actual orbit transports and exact gates/fixed/joint replay for seven-rich unique6 reductions."""
from pathlib import Path
from itertools import combinations,product
from fractions import Fraction as Q
import importlib.util,json,time
HERE=Path(__file__).parent;BASE=HERE.parent;ROOT=HERE.parents[4]
spec=importlib.util.spec_from_file_location('old_gate_replay',ROOT/'context/propertyb35-paper/round01/twentyone-delta5/replay.py');old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)

def key(ns,s):return tuple(ns.get(str(m),ns.get(m,0)) for m in range(1<<s))
def recover(inc,s):
 ns={}
 for m in sorted(range(1<<s),key=int.bit_count,reverse=True):ns[m]=inc[m]-sum(v for u,v in ns.items() if u&m==m)
 return ns if min(ns.values())>=0 else None

def moments(ns,s):
 ns={int(m):v for m,v in ns.items()};return {m:sum(v for u,v in ns.items() if u&m==m) for m in range(1,1<<s)}
def lift(inc,S):return {sum(1<<S[i] for i in range(len(S)) if m>>i&1):v for m,v in inc.items()}
def triples_inc(ds,cs,t):return {0:35,1:ds[0],2:ds[1],4:ds[2],3:cs[0],5:cs[1],6:cs[2],7:t}

def main():
 st=time.time();unit=json.loads((HERE/'UNIT7_GATES.json').read_text())['cases'];seen=set()
 for d in range(7,16):
  for c in range(1,8):
   for t in (0,1):
    ns=recover(triples_inc((6,7,d),(1,1,c),t),3)
    if ns is not None:seen.add((d,c,t,key(ns,3)))
 assert seen=={(r['degrees'][2],r['codegrees'][2],r['triple'],key(r['counts'],3)) for r in unit};assert len(unit)==117
 doubles=[r for r in json.loads((BASE/'DOUBLES.json').read_text())['cases'] if (r['degrees']==[6,7] and r['codegree']>=4) or (r['degrees']==[7,7] and r['codegree']>=4) or (r['degrees'][0]==6 and r['degrees'][1]>=16 and r['codegree']==1)];assert all(old.verify(r)<1 for r in doubles)
 bare=json.loads((HERE/'ALL677_DP.json').read_text())['cases'];allowed={};seen=set()
 for a in (1,2,3):
  for b in range(a,4):
   for c in (1,2,3):
    for t in range(min(a,b,c)+1):
     ns=recover(triples_inc((6,7,7),(a,b,c),t),3)
     if ns is not None:seen.add(((a,b,c),t,key(ns,3)))
 assert seen=={(tuple(r['codegrees']),r['triple'],key(r['counts'],3)) for r in bare}
 for r in bare:
  if not r['strict']:allowed.setdefault(tuple(r['codegrees']),set()).add(r['triple'])
 assert all(max(r['codegrees'])<=2 for r in bare if not r['strict'])
 dom3=json.loads((HERE/'THREE7_DOMAIN.json').read_text());rows3=json.loads((HERE/'THREE7_DP.json').read_text())['cases'];seen=set();prs=list(combinations(range(4),2));trs=list(combinations(range(4),3))
 for cs in product((1,2),repeat=6):
  pair=dict(zip(prs,cs));opts=[allowed.get((*sorted((pair[0,i],pair[0,j])),pair[i,j]),()) for i,j in combinations(range(1,4),2)]+[range(min(pair[i,j] for i,j in combinations(range(1,4),2))+1)]
  for ts in product(*opts):
   for q in range(min(ts)+1):
    inc={0:35,1:6,2:7,4:7,8:7}|{sum(1<<i for i in S):v for S,v in pair.items()}|{sum(1<<i for i in S):v for S,v in zip(trs,ts)}|{15:q};ns=recover(inc,4)
    if ns is not None:seen.add(key(ns,4))
 assert seen=={key(r['counts'],4) for r in dom3['labelled']};checks=[dict(file='THREE7',domain=len(seen))]
 j3=json.loads((HERE/'THREE7_JOINT.json').read_text())['results'];v3={z['source_id']:Q(z['bound']) for z in j3};rem3={r['id'] for r in rows3 if v3.get(r['id'],Q(r['bound']))>=1};base=[moments(r['counts'],4) for r in dom3['labelled'] if r['orbit'] in rem3];views=[(0,)+S for S in combinations(range(1,5),3)];opts=[[lift(r,S) for r in base] for S in views];seen=set();joins=0
 # Prefix extension from the first actual three-seven view.
 def go(j,inc):
  if j==len(opts):yield inc;return
  for new in opts[j]:
   if all(inc.get(k,v)==v for k,v in new.items()):yield from go(j+1,inc|new)
 for prefix in opts[0]:
  for inc in go(1,prefix):
   joins+=1
   for q in range(min(inc[30^(1<<i)] for i in range(1,5))+1):
    for t in range(min(1,q,min(inc[31^(1<<i)] for i in range(1,5)))+1):
     ns=recover({0:35}|inc|{30:q,31:t},5)
     if ns is not None:seen.add(key(ns,5))
 dom4=json.loads((HERE/'FOUR7_DOMAIN.json').read_text());rows4=json.loads((HERE/'FOUR7_DP.json').read_text())['cases'];assert seen=={key(r['counts'],5) for r in dom4['labelled']};checks.append(dict(file='FOUR7',domain=len(seen),prefix_joins=joins))
 j4=json.loads((HERE/'FOUR7_JOINT.json').read_text())['results'];v4={z['source_id']:Q(z['bound']) for z in j4};rem4=[r for r in rows4 if v4.get(r['id'],Q(r['bound']))>=1];assert len(rem4)==3
 for r in rem4:
  inc=moments(r['counts'],5);assert all(inc[1|(1<<i)]==1 for i in range(1,5));assert all(inc[(1<<i)|(1<<j)]==1 for i,j in combinations(range(1,5),2));P=tuple(sorted(int(m)>>1 for m,v in r['counts'].items() if v and int(m)&1 and int(m)>>1));assert sorted(B.bit_count() for B in P) in ([1,1,1,1],[2,2]);assert sum(inc[sum(1<<i for i in S)] for S in combinations(range(1,5),3))<=1;assert inc[30]==0
 # Independent combinatorial five-seven classification: all center blocks single,
 # all pairs unit, at most one nonzero triple within each four-set.
 seen=set();ts=list(combinations(range(1,6),3));qsets=list(combinations(range(1,6),4))
 for values in product((0,1),repeat=10):
  if any(sum(v for S,v in zip(ts,values) if set(S)<=set(T))>1 for T in qsets):continue
  inc={0:35}
  for m in range(1,64):
   if m&1:inc[m]=6 if m==1 else int((m>>1).bit_count()==1)
   elif m.bit_count()==1:inc[m]=7
   elif m.bit_count()==2:inc[m]=1
   elif m.bit_count()==3:inc[m]=values[ts.index(tuple(i for i in range(1,6) if m>>i&1))]
   else:inc[m]=0
  ns=recover(inc,6)
  if ns is not None:seen.add(key(ns,6))
 dom5=json.loads((HERE/'FIVE7_DOMAIN.json').read_text());rows5=json.loads((HERE/'FIVE7_DP.json').read_text())['cases'];assert seen=={key(r['counts'],6) for r in dom5['labelled']};assert len(seen)==26;checks.append(dict(file='FIVE7',domain=len(seen),combinatorial_classification=True))
 old.joint.check_profile=old.check35;results=[]
 for name,rows,joints in [('UNIT7_GATES',unit,[]),('ALL677',bare,[]),('THREE7',rows3,j3),('FOUR7',rows4,j4),('FIVE7',rows5,[])]:
  vals={r['id']:old.verify(r) for r in rows};byid={r['id']:r for r in rows};nstrict=0
  for z in joints:
   if Q(z['bound'])<1:old.joint.verify(z,v=21,s=len(byid[z['source_id']]['degrees']),expected_degrees=byid[z['source_id']]['degrees']);vals[z['source_id']]=Q(z['bound']);nstrict+=1
  if name=='FIVE7':assert all(v<1 for v in vals.values())
  results.append(dict(file=name,fixed_profiles=len(rows),strict_joint_profiles_verified=nstrict,residuals=sum(v>=1 for v in vals.values()),max_final_strict=str(max((v for v in vals.values() if v<1),default=0))))
 for dom,s in [(dom3,4),(dom4,5),(dom5,6)]:
  for r in dom['labelled']:
   rep=dom['orbits'][r['orbit']];perm=r['from_representative_seven_permutation'];ns={int(m):v for m,v in rep['counts'].items()}
   def move(m):return(m&1)|sum(1<<(perm[i]+1) for i in range(s-1) if m>>(i+1)&1)
   assert key({move(m):v for m,v in ns.items()},s)==key(r['counts'],s)
 result=dict(status='PASS',scope=__doc__,strong_double_gates=len(doubles),independent_domains=checks,four_seven_residual_structure_verified=True,actual_transports=sum(len(d['labelled']) for d in (dom3,dom4,dom5)),certificate_results=results,elapsed_seconds=time.time()-st);(HERE/'REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
if __name__=='__main__':main()
