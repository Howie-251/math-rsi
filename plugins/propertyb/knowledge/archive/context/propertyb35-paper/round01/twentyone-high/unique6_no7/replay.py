"""Independent full-inclusive/prefix-partition census, actual transports, and exact unit8-star fixed/joint witness replay."""
from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as Q
import importlib.util,json,time
HERE=Path(__file__).parent;BASE=HERE.parent;ROOT=HERE.parents[4]
spec=importlib.util.spec_from_file_location('old_unit_star_replay',ROOT/'context/propertyb35-paper/round01/twentyone-delta5/replay.py');old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)

def parts(n):
 def go(i,bs):
  if i==n:yield tuple(sum(1<<j for j in B) for B in bs);return
  for k in range(len(bs)):
   new=[list(B) for B in bs];new[k].append(i);yield from go(i+1,new)
  yield from go(i+1,bs+[[i]])
 yield from go(0,[])
def key(ns,s):return tuple(ns.get(str(m),ns.get(m,0)) for m in range(1<<s))
def mobius(inc,s):
 out=[inc[m] for m in range(1<<s)]
 for i in range(s):
  for m in range(1<<s):
   if not m>>i&1:out[m]-=out[m|(1<<i)]
 return tuple(out)
def moments(ns,s):
 ns={int(m):v for m,v in ns.items()};return {m:sum(v for u,v in ns.items() if u&m==m) for m in range(1,1<<s)}
def partition(ns):return tuple(sorted(int(m)>>1 for m,v in ns.items() if v and int(m)&1 and int(m)>>1))
def lift(inc,S):return {sum(1<<S[i] for i in range(len(S)) if m>>i&1):v for m,v in inc.items()}
def restrict(P,S):return tuple(sorted(sum(1<<j for j,i in enumerate(S) if B>>i&1) for B in P if any(B>>i&1 for i in S)))

def extend(dom,n,allowed,maxblock=4):
 prep=[(partition(r['counts']),moments(r['counts'],n)) for r in dom['labelled'] if r['orbit'] in allowed];views=[(0,)+S for S in combinations(range(1,n+1),n-1)];raw=[];known=set();ks=[]
 for S in views:
  groups={}
  for P,inc in prep:groups.setdefault(P,[]).append(lift(inc,S))
  raw.append(groups);keys=set(next(iter(groups.values()))[0]);ks.append(tuple(sorted(known&keys)));known|=keys
 cache={};seen=set();joined=0
 for baseP,inc0 in prep:
  extensions=[tuple(sorted((*baseP,1<<(n-1))))] if len(baseP)<6 else []
  extensions += [tuple(sorted(B|(1<<(n-1)) if j==k else B for j,B in enumerate(baseP))) for k in range(len(baseP)) if baseP[k].bit_count()<maxblock]
  for P in extensions:
   if max(B.bit_count() for B in P)>maxblock:continue
   def go(j,inc):
    if j==len(views):yield inc;return
    cachekey=(P,j)
    if cachekey not in cache:
     localP=restrict(P,tuple(i-1 for i in views[j][1:]));opts=raw[j].get(localP,[]);b={}
     for vals in opts:b.setdefault(tuple(vals[k] for k in ks[j]),[]).append(vals)
     cache[cachekey]=b
    for vals in cache[cachekey].get(tuple(inc[k] for k in ks[j]),[]):yield from go(j+1,inc|vals)
   for inc in go(1,inc0):
    joined+=1;high=(1<<(n+1))-2;full=high|1;assert set(inc)==set(range(1,1<<(n+1)))-{high,full}
    upper=min(inc[high^(1<<i)] for i in range(1,n+1))
    if n==5:upper=min(upper,1)
    if n>=6:upper=0
    centerfull=int(len(P)==1)
    assert centerfull==0 or n<=4
    for t in range(upper+1):
     ns=mobius({0:35}|inc|{high:t,full:centerfull},n+1)
     if min(ns)>=0:seen.add(ns)
 return seen,joined

def main():
 st=time.time();gate_rows=[r for r in json.loads((BASE/'UNIT_PAIRS.json').read_text())['cases'] if r['degrees']==[6,8,8]];gate={(r['codegrees'][2],r['triple']):r['strict'] for r in gate_rows};gvals=[old.verify(r) for r in gate_rows];assert all(r['strict'] for r in gate_rows if r['codegrees'][2]>=4)
 seen=set();prs=list(combinations(range(3),2))
 for P in parts(3):
  same=lambda A:int(any(B&A==A for B in P))
  for cs in product(range(1,4),repeat=3):
   if any(gate[(v,same(sum(1<<i for i in S)))] for S,v in zip(prs,cs)):continue
   for t in range(min(cs)+1):
    hi={1:8,2:8,4:8,3:cs[0],5:cs[1],6:cs[2],7:t};inc={0:35}
    for m in range(1,16):inc[m]=(6 if m==1 else same(m>>1)) if m&1 else hi[m>>1]
    ns=mobius(inc,4)
    if min(ns)>=0:seen.add(ns)
 domains={tag:json.loads((HERE/f'{tag}_DOMAIN.json').read_text()) for tag in ('THREE','FOUR','FIVE','SIX')};rows={tag:json.loads((HERE/f'{tag}_DP.json').read_text())['cases'] for tag in domains};joint={tag:json.loads((HERE/f'{tag}_JOINT.json').read_text())['results'] for tag in ('THREE','FOUR','FIVE')};remaining={}
 for tag in ('THREE','FOUR','FIVE'):
  vals={z['source_id']:Q(z['bound']) for z in joint[tag]};remaining[tag]={r['id'] for r in rows[tag] if vals.get(r['id'],Q(r['bound']))>=1}
 checks=[];assert seen=={key(r['counts'],4) for r in domains['THREE']['labelled']};checks.append(dict(file='THREE',independent_labelled=len(seen)))
 for prev,tag,n in [('THREE','FOUR',4),('FOUR','FIVE',5)]:
  seen,joined=extend(domains[prev],n,remaining[prev]);assert seen=={key(r['counts'],n+1) for r in domains[tag]['labelled']};checks.append(dict(file=tag,independent_labelled=len(seen),prefix_joins=joined))
 rem5=[r for r in rows['FIVE'] if r['id'] in remaining['FIVE']];assert len(rem5)==26;assert {tuple(sorted(B.bit_count() for B in r['center_partition'])) for r in rem5}=={(2,3),(1,2,2),(1,1,1,2),(1,1,1,1,1)};keep=set()
 for r in rem5:
  inc=moments(r['counts'],6);ones={(i,j) for i,j in combinations(range(1,6),2) if inc[(1<<i)|(1<<j)]==1};assert all(inc[(1<<i)|(1<<j)] in (1,2) for i,j in combinations(range(1,6),2));assert not ones or any(ones=={tuple(sorted((i,j))) for j in range(1,6) if j!=i} for i in range(1,6));assert inc[62]==0
  if not ones and max(B.bit_count() for B in r['center_partition'])<=2:keep.add(r['id'])
 seen,joined=extend(domains['FIVE'],6,keep,maxblock=2);assert seen=={key(r['counts'],7) for r in domains['SIX']['labelled']};checks.append(dict(file='SIX',independent_labelled=len(seen),prefix_joins=joined,source_kept=sorted(keep)))
 results=[];old.joint.check_profile=old.check35
 for tag,s in [('THREE',4),('FOUR',5),('FIVE',6),('SIX',7)]:
  dom=domains[tag]
  for r in dom['labelled']:
   rep=dom['orbits'][r['orbit']];perm=r['from_representative_neighbor_permutation'];ns={int(m):v for m,v in rep['counts'].items()}
   def move(m):return(m&1)|sum(1<<(perm[i]+1) for i in range(s-1) if m>>(i+1)&1)
   moved={move(m):v for m,v in ns.items()};assert key(moved,s)==key(r['counts'],s)
  byid={r['id']:r for r in rows[tag]};assert all(key(r['counts'],s)==key(dom['orbits'][r['id']]['counts'],s) for r in rows[tag]);vals={r['id']:old.verify(r) for r in rows[tag]};jstrict=0
  for z in joint.get(tag,[]):
   r=byid[z['source_id']]
   if Q(z['bound'])<1:old.joint.verify(z,v=21,s=s,expected_degrees=r['degrees']);jstrict+=1
   vals[r['id']]=Q(z['bound'])
  if tag=='SIX':assert all(v<1 for v in vals.values())
  results.append(dict(file=tag,actual_transports=len(dom['labelled']),fixed_profiles=len(rows[tag]),strict_joint_profiles_verified=jstrict,residuals=sum(v>=1 for v in vals.values()),max_final_strict=str(max(v for v in vals.values() if v<1))))
 result=dict(status='PASS',scope=__doc__,pair_gate_profiles=len(gate_rows),independent_domains=checks,five_residual_structure_verified=True,certificate_results=results,elapsed_seconds=time.time()-st);(HERE/'REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
if __name__=='__main__':main()
