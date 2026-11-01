"""Independent RGS partitions and explicit Mobius sums for the saved actual unit-star domains."""
from pathlib import Path
from itertools import product,combinations
import json,time
HERE=Path(__file__).parent

def partitions(n):
 for a in product(range(n),repeat=n):
  if a[0] or any(a[i]>max(a[:i])+1 for i in range(1,n)):continue
  pp=tuple(tuple(i for i,v in enumerate(a) if v==b) for b in range(max(a)+1))
  if max(map(len,pp))<=4:yield pp

def canon(pp):return tuple(sorted(tuple(sorted(b)) for b in pp))
def restrict(pp,S):
 mp={i:j for j,i in enumerate(S)};return canon([[mp[i] for i in b if i in mp] for b in pp if any(i in mp for i in b)])
def key(ns,s):return tuple(ns.get(m,ns.get(str(m),0)) for m in range(1<<(s+1)))
def recover(ds,ps,pp,high):
 s=len(ds);inc={1<<i:d for i,d in enumerate(ds)}|{sum(1<<i for i in ij):c for ij,c in zip(combinations(range(s),2),ps)}|high
 J={m:inc[m]-int(any(all(i in b for i in range(s) if m>>i&1) for b in pp)) for m in range(1,1<<s)}
 outside={m:sum(((-1)**(u.bit_count()-m.bit_count()))*J[u] for u in J if u&m==m) for m in J}
 outside[0]=30-sum(outside.values());ns={m<<1:n for m,n in outside.items()};ns[1]=5-len(pp)
 for b in pp:ns[1|sum(1<<(i+1) for i in b)]=1
 return ns if min(ns.values())>=0 else None

def moments(r):
 ns={int(m):n for m,n in r['counts'].items()};s=len(r['neighbor_degrees'])
 return {m:sum(n for t,n in ns.items() if t&(m<<1)==m<<1) for m in range(1,1<<s)}
def mapped(vals,S):return {sum(1<<S[i] for i in range(len(S)) if m>>i&1):v for m,v in vals.items()}
def compatible(a,b):return all(m not in a or a[m]==v for m,v in b.items())

def main():
 st=time.time();checks=[];pilot=json.loads((HERE/'PILOT.json').read_text());lookup={(tuple(r['degrees'][1:]),r['codegrees'][2],r['triple']):r['strict'] for r in pilot['triples']}
 for filename,dss in [('STAR_THREE_DOMAIN.json',[(7,7,7),(7,7,8),(7,8,8),(8,8,8)]),('STAR_LOW_DOMAIN.json',[(5,8,8),(6,7,7),(6,7,8),(6,8,8)])]:
  seen=set()
  for ds in dss:
   for ps in product(range(1,4),repeat=3):
    if any(sum(c-1 for ij,c in zip(combinations(range(3),2),ps) if i in ij)>4*d-20 for i,d in enumerate(ds)):continue
    for pp in partitions(3):
     if any(lookup[(tuple(ds[i] for i in ij),c,int(any(all(i in b for i in ij) for b in pp)))] for ij,c in zip(combinations(range(3),2),ps)):continue
     for t in range(min(ps)+1):
      ns=recover(ds,ps,pp,{7:t})
      if ns is not None:seen.add((ds,key(ns,3)))
  old=json.loads((HERE/filename).read_text())['cases'];expected={(tuple(r['neighbor_degrees']),key(r['counts'],3)) for r in old};assert seen==expected;checks.append(dict(file=filename,count=len(seen)))
 # Unique 6/7/8 residual -> four neighbours p6,q7,z8,w8.
 seen=set()
 for c in (1,2):
  for pp in [((0,1),(2,3)),((0,1),(2,),(3,))]:
   for a,b in product((0,1),repeat=2):
    ns=recover((6,7,8,8),(2,1,1,1,1,c),pp,{7:0,11:0,13:a,14:b,15:0})
    if ns is not None:seen.add(key(ns,4))
 old=json.loads((HERE/'SIX_SEVEN_FOUR_DP.json').read_text())['cases'];assert seen=={key(r['counts'],4) for r in old};checks.append(dict(file='SIX_SEVEN_FOUR_DP.json',count=len(seen)))
 # Four-neighbour domain p6+three8, using arbitrary actual prior projections.
 prev=json.loads((HERE/'STAR_LOW_DP.json').read_text())['cases']+json.loads((HERE/'STAR_THREE_DP.json').read_text())['cases'];allowed={}
 for r in prev:
  if not r['strict']:allowed.setdefault((tuple(r['neighbor_degrees']),tuple(r['neighbor_codegrees']),canon(r['center_partition'])),set()).add(r['neighbor_triple'])
 ds=(6,8,8,8);ss=list(combinations(range(4),3));bits=[sum(1<<i for i in S) for S in ss];seen=set()
 for ps in product((1,2),repeat=6):
  pair=dict(zip(combinations(range(4),2),ps))
  for pp in partitions(4):
   options=[allowed.get((tuple(ds[i] for i in S),tuple(pair[ij] for ij in combinations(S,2)),restrict(pp,S)),()) for S in ss]
   if any(not z for z in options):continue
   for ts in product(*options):
    for q in range(min(ts)+1):
     ns=recover(ds,ps,pp,dict(zip(bits,ts))|{15:q})
     if ns is not None:seen.add(key(ns,4))
 old=json.loads((HERE/'SIX_EIGHTS_FOUR_DOMAIN.json').read_text())['cases'];assert seen=={key(r['counts'],4) for r in old};checks.append(dict(file='SIX_EIGHTS_FOUR_DOMAIN.json',count=len(seen)))
 # Generate all same-partition joins from empty, not via extension of a fixed base view.
 prev=[r for r in json.loads((HERE/'SIX_EIGHTS_FOUR_DP.json').read_text())['cases'] if not r['strict']];prepared=[(r,moments(r)) for r in prev];Ss=[(0,)+S for S in combinations(range(1,5),3)];seen=set();joins=0
 for pp in partitions(5):
  options=[[(r,mapped(mm,S)) for r,mm in prepared if canon(r['center_partition'])==restrict(pp,S)] for S in Ss]
  if any(not z for z in options):continue
  def rec(i,inc):
   if i==len(options):yield inc;return
   for r,vals in options[i]:
    if compatible(inc,vals):yield from rec(i+1,inc|vals)
  for inc in rec(0,{}):
   joins+=1
   assert set(inc)==set(range(1,32))-{30,31}
   for q in range(min(inc[m] for m in (14,22,26,28))+1):
    all4=inc|{30:q}
    for t in range(min(1,min(all4[m] for m in (15,23,27,29,30)))+1):
     vals=all4|{31:t};ps=[vals[(1<<i)|(1<<j)] for i,j in combinations(range(5),2)];ns=recover((6,8,8,8,8),ps,pp,{m:v for m,v in vals.items() if m.bit_count()>=3})
     if ns is not None:seen.add(key(ns,5))
 old=json.loads((HERE/'SIX_EIGHTS_FIVE_DOMAIN.json').read_text())['cases'];assert seen=={key(r['counts'],5) for r in old};checks.append(dict(file='SIX_EIGHTS_FIVE_DOMAIN.json',count=len(seen),pre_completion_joins=joins))
 # Generic four-neighbour7/8 domains with independent RGS/Mobius generation.
 allowed={}
 for r in json.loads((HERE/'STAR_THREE_DP.json').read_text())['cases']:
  if not r['strict']:allowed.setdefault((tuple(r['neighbor_degrees']),tuple(r['neighbor_codegrees']),canon(r['center_partition'])),set()).add(r['neighbor_triple'])
 generated=set();bydegree={}
 for ds in [(7,7,7,7),(7,7,7,8),(7,7,8,8),(7,8,8,8),(8,8,8,8)]:
  own=set()
  for ps in product(range(1,4),repeat=6):
   pair=dict(zip(combinations(range(4),2),ps))
   for pp in partitions(4):
    opts=[allowed.get((tuple(ds[i] for i in S),tuple(pair[ij] for ij in combinations(S,2)),restrict(pp,S)),()) for S in ss]
    if any(not o for o in opts):continue
    for ts in product(*opts):
     for q in range(min(ts)+1):
      ns=recover(ds,ps,pp,dict(zip(bits,ts))|{15:q})
      if ns is not None:own.add(key(ns,4));generated.add((ds,key(ns,4)))
  bydegree[str(ds)]=len(own)
 old=json.loads((HERE/'GENERIC_FOUR_DOMAIN.json').read_text())['cases'];assert generated=={(tuple(r['neighbor_degrees']),key(r['counts'],4)) for r in old};checks.append(dict(file='GENERIC_FOUR_DOMAIN.json',count=len(generated),bydegree=bydegree))
 # The16 complete four-seven residuals have exactly the stated structural forms.
 rr=[r for r in json.loads((HERE/'FOUR_SEVENS_DP.json').read_text())['cases'] if not r['strict']];seen=set()
 for r in rr:
  inc=moments(r);pp=canon(r['center_partition']);pairs4=list(combinations(range(4),2));cs=tuple(inc[sum(1<<i for i in S)] for S in pairs4);ts=tuple(inc[sum(1<<i for i in S)] for S in combinations(range(4),3));seen.add((cs,pp,ts,inc[15]))
 expected=set();singles=canon([(i,) for i in range(4)]);expected.add(((1,)*6,singles,(0,)*4,0))
 for pp in partitions(4):
  if sorted(map(len,pp))==[2,2]:expected.add(((1,)*6,canon(pp),(0,)*4,0))
 trs=list(combinations(range(4),3));prs=list(combinations(range(4),2))
 for pair2 in prs:
  cs=tuple(2 if pair==pair2 else 1 for pair in prs);outside=set(range(4))-set(pair2)
  for endpoint in pair2:
   tr=tuple(sorted(outside|{endpoint}));ts=tuple(int(T==tr) for T in trs);expected.add((cs,singles,ts,0))
 assert seen==expected and len(seen)==16;checks.append(dict(file='FOUR_SEVENS_DP.json residual structure',count=16))
 five=json.loads((HERE/'FIVE_SEVENS_DOMAIN.json').read_text())['cases'];ns={0:10}
 for i in range(5):ns[1|(1<<(i+1))]=1;ns[1<<(i+1)]=2
 for i,j in combinations(range(5),2):ns[(1<<(i+1))|(1<<(j+1))]=1
 assert len(five)==1 and key(five[0]['counts'],5)==key(ns,5);checks.append(dict(file='FIVE_SEVENS_DOMAIN.json structural unique candidate',count=1))
 # Independent prefix-extension joins for the positive five-neighbour mixed domains.
 filemap={'7777':'FOUR_SEVENS_DP.json','7778':'FOUR_THREE_SEVENS_DP.json','7788':'GENERIC_7788_DP.json','7888':'GENERIC_7888_DP.json','8888':'GENERIC_8888_DP.json'}
 five_specs=[('FIVE_FOUR_SEVENS_DOMAIN.json',(7,7,7,7,8)),('GENERIC_77788_DOMAIN.json',(7,7,7,8,8)),('GENERIC_77888_DOMAIN.json',(7,7,8,8,8)),('GENERIC_78888_DOMAIN.json',(7,8,8,8,8)),('GENERIC_88888_DOMAIN.json',(8,8,8,8,8))]
 for filename,ds in five_specs:
  if not (HERE/filename).exists():continue
  views=list(combinations(range(5),4));bydegree={}
  for S in views:
   deg=''.join(str(ds[i]) for i in S)
   if deg not in bydegree:
    src=json.loads((HERE/filemap[deg]).read_text());assert src['complete'];bydegree[deg]=[(r,moments(r)) for r in src['cases'] if not r['strict']]
  seen=set();prefix=''.join(str(d) for d in ds[:4]);joins=0
  for r,base in bydegree[prefix]:
   old=r['center_partition'];extensions=[canon([*old,[4]])]+[canon([list(b)+([4] if j==k else []) for j,b in enumerate(old)]) for k in range(len(old)) if len(old[k])<4]
   for pp in extensions:
    opts=[]
    for S in views:
     if S==(0,1,2,3):continue
     deg=''.join(str(ds[i]) for i in S);opts.append([mapped(m,S) for z,m in bydegree[deg] if canon(z['center_partition'])==restrict(pp,S)])
    def rec(i,inc):
     if i==len(opts):yield inc;return
     for new in opts[i]:
      if compatible(inc,new):yield from rec(i+1,inc|new)
    for inc in rec(0,base):
     joins+=1;assert set(inc)==set(range(1,31))
     for t in range(min(1,min(inc[m] for m in (15,23,27,29,30)))+1):
      vals=inc|{31:t};ps=[vals[(1<<i)|(1<<j)] for i,j in combinations(range(5),2)];ns=recover(ds,ps,pp,{m:v for m,v in vals.items() if m.bit_count()>=3})
      if ns is not None:seen.add(key(ns,5))
  expected=json.loads((HERE/filename).read_text())['cases'];assert seen=={key(r['counts'],5) for r in expected};checks.append(dict(file=filename,count=len(seen),prefix_join_count=joins))
 # Independent five-to-six prefix extensions: enforce six-point count0 and <=5 actual center blocks.
 for fname,basefile,ds,p_bearing in [('GENERIC_788888_DOMAIN.json','GENERIC_78888_DP.json',(7,8,8,8,8,8),True),('GENERIC_888888_DOMAIN.json','GENERIC_88888_DP.json',(8,8,8,8,8,8),False)]:
  if not (HERE/fname).exists():continue
  src=json.loads((HERE/basefile).read_text());assert src['complete'];prep=[(r,moments(r)) for r in src['cases'] if not r['strict']]
  views=[(0,)+S for S in combinations(range(1,6),4)] if p_bearing else list(combinations(range(6),5));seen=set();joins=0
  for r,base in prep:
   old=r['center_partition'];extensions=([canon([*old,[5]])] if len(old)<5 else [])+[canon([list(b)+([5] if j==k else []) for j,b in enumerate(old)]) for k in range(len(old)) if len(old[k])<4]
   for pp in extensions:
    opts=[[mapped(mm,S) for z,mm in prep if canon(z['center_partition'])==restrict(pp,S)] for S in views if S!=(0,1,2,3,4)]
    def rec(i,inc):
     if i==len(opts):yield inc;return
     for new in opts[i]:
      if compatible(inc,new):yield from rec(i+1,inc|new)
    for inc in rec(0,base):
     joins+=1
     if p_bearing:
      assert set(inc)==set(range(1,64))-{62,63};completions=[inc|{62:q,63:0} for q in range(min(1,min(inc[m] for m in (30,46,54,58,60)))+1)]
     else:
      assert set(inc)==set(range(1,63));completions=[inc|{63:0}]
     for vals in completions:
      ps=[vals[(1<<i)|(1<<j)] for i,j in combinations(range(6),2)];ns=recover(ds,ps,pp,{m:v for m,v in vals.items() if m.bit_count()>=3})
      if ns is not None:seen.add(key(ns,6))
  expected=json.loads((HERE/fname).read_text())['cases'];assert seen=={key(r['counts'],6) for r in expected};checks.append(dict(file=fname,count=len(seen),prefix_join_count=joins))
 result=dict(status='PASS',scope=__doc__,checks=checks,elapsed_seconds=time.time()-st);(HERE/'DOMAIN_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
if __name__=='__main__':main()
