"""Independent mixed-degree domain reconstruction and new fixed-certificate replay; previous pure-seven audit kept separate."""
from pathlib import Path
from itertools import product,combinations
import sys,json,time
HERE=Path(__file__).parent;BASE=HERE.parent
from audit import key,rec,moments,lift,verify

def join_mixed(previous,ds):
 s=len(ds);views=[(0,1)+S for S in combinations(range(2,s),s-3)];options=[]
 for S in views:
  deg=tuple(ds[i] for i in S)
  options.append([lift(moments(r['counts'],s-1),S) for r in previous if not r['strict'] and tuple(r['degrees'])==deg])
 seen=set()
 def go(j,inc):
  if j==len(options):yield inc;return
  # Shared-key buckets are independent of the source join's direct full-dict scan.
  keys=tuple(sorted(set(inc)&set(options[j][0])))
  target=tuple(inc[k] for k in keys)
  buckets={}
  for vals in options[j]:buckets.setdefault(tuple(vals[k] for k in keys),[]).append(vals)
  for vals in buckets.get(target,[]):yield from go(j+1,inc|vals)
 for base in options[0]:
  for inc in go(1,base):
   outs=sum(1<<i for i in range(2,s));missing=(outs,outs|1,outs|2,(1<<s)-1);assert set(inc)==set(range(1,1<<s))-set(missing)
   caps=[]
   for m in missing:
    upper=min((inc[u] for u in inc if u&m==u),default=35)
    if m.bit_count()==5:upper=min(upper,1)
    if m.bit_count()>5:upper=0
    caps.append(range(upper+1))
   for vals in product(*caps):
    ns=rec({0:35}|inc|dict(zip(missing,vals)),s)
    if ns is not None:seen.add(key(ns,s))
 return seen

def main():
 st=time.time();checks=[];tr=json.loads((BASE/'TWO_SIXES_TRIPLES.json').read_text())['cases'];allow={}
 for r in tr:
  if not r['strict']:allow.setdefault((r['degrees'][2],tuple(r['codegrees'])),set()).add(r['triple'])
 four=json.loads((HERE/'FOUR_DP.json').read_text())['cases'];seen=set();pairs=list(combinations(range(4),2));triples=list(combinations(range(4),3))
 for da,db,cap in [(7,7,3),(7,8,3),(8,8,4)]:
  for c in (1,2):
   for aa in product((1,2),repeat=4):
    a,b,d,e=aa
    for zw in range(1,cap+1):
     inc={0:35,1:6,2:6,4:da,8:db}|{sum(1<<i for i in S):v for S,v in zip(pairs,(c,a,b,d,e,zw))}
     opts=[allow.get((da,(c,*sorted((a,d)))),()),allow.get((db,(c,*sorted((b,e)))),()),range(min(a,b,zw)+1),range(min(d,e,zw)+1)]
     for ts in product(*opts):
      for q in range(min(ts)+1):
       ns=rec(inc|{sum(1<<i for i in S):v for S,v in zip(triples,ts)}|{15:q},4)
       if ns is not None:seen.add((da,db,key(ns,4)))
 assert seen=={(*r['degrees'][2:],key(r['counts'],4)) for r in four};checks.append(dict(file='FOUR_DP.json full',domain=len(seen)))
 allfive=json.loads((HERE/'FIVE_SEVENS_DP.json').read_text())['cases'];newfiles=[]
 for pat in ('778','788'):
  path=HERE/f'FIVE_{pat}_DP.json'
  if not path.exists():continue
  src=json.loads(path.read_text())['cases'];ds=(6,6)+tuple(map(int,pat));seen=join_mixed(four,ds);assert seen=={key(r['counts'],5) for r in src};checks.append(dict(file=path.name,domain=len(seen)));allfive+=src;newfiles.append((path.name,src))
 for pat in ('7778','7788'):
  path=HERE/f'SIX_{pat}_DP.json'
  if not path.exists():continue
  src=json.loads(path.read_text())['cases'];ds=(6,6)+tuple(map(int,pat));seen=join_mixed(allfive,ds);assert seen=={key(r['counts'],6) for r in src};checks.append(dict(file=path.name,domain=len(seen)));newfiles.append((path.name,src))
 # Three six-lock views containing the same two sixes and same two sevens.
 path=HERE/'SEVEN_77888_DP.json'
 if path.exists():
  sixsrc=json.loads((HERE/'SIX_7788_DP.json').read_text())['cases'];rows=[moments(r['counts'],6) for r in sixsrc if not r['strict']]
  views=[(0,1,2,3)+S for S in combinations(range(4,7),2)];options=[[lift(r,S) for r in rows] for S in views];seen=set()
  for a in options[0]:
   for b in options[1]:
    if any(a[k]!=v for k,v in b.items() if k in a):continue
    ab=a|b
    for d in options[2]:
     if any(ab[k]!=v for k,v in d.items() if k in ab):continue
     inc=ab|d;missing=sorted(set(range(1,128))-set(inc));assert len(missing)==16;caps=[]
     for m in missing:
      upper=min(inc[u] for u in inc if u&m==u)
      if m.bit_count()==5:upper=min(upper,1)
      if m.bit_count()>5:upper=0
      caps.append(range(upper+1))
     for vals in product(*caps):
      # In-place upper-subset Mobius transform, different from descending elimination.
      ns=[({0:35}|inc|dict(zip(missing,vals)))[m] for m in range(128)]
      for i in range(7):
       for m in range(128):
        if not (m>>i&1):ns[m]-=ns[m|(1<<i)]
      if min(ns)>=0:seen.add(tuple(ns))
  src=json.loads(path.read_text())['cases'];assert seen=={key(r['counts'],7) for r in src};checks.append(dict(file=path.name,domain=len(seen)));newfiles.append((path.name,src))
 replay=[];rr=[r for r in four if r['degrees']!=[6,6,7,7]];newfiles.insert(0,('FOUR_DP.json mixed78/88',rr))
 for fname,rows in newfiles:
  vals=[verify(r) for r in rows];replay.append(dict(file=fname,cases=len(rows),strict=sum(v<1 for v in vals),max_strict=str(max(v for v in vals if v<1))))
 result=dict(status='PASS',scope=__doc__,domain_checks=checks,fixed_replay=replay,profiles=sum(len(rows) for _,rows in newfiles),elapsed_seconds=time.time()-st)
 (HERE/'AUDIT_MIXED.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
if __name__=='__main__':main()
