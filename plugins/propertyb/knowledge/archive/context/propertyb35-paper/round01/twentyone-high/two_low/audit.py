"""Independent descending-inclusion recovery, residual-projection census, and35-stub replay for two-low seven-rich branches."""
from pathlib import Path
from itertools import product,combinations
from fractions import Fraction
import sys,json,time
HERE=Path(__file__).parent;BASE=HERE.parent;ROOT=HERE.parents[4]
sys.path.insert(0,str(ROOT/'context/propertyb35-paper/round01/twentyone-delta5'))
from replay import verify

def key(ns,s):return tuple(ns.get(str(m),ns.get(m,0)) for m in range(1<<s))
def rec(inc,s):
 out={}
 for m in sorted(range(1<<s),key=int.bit_count,reverse=True):out[m]=inc[m]-sum(v for u,v in out.items() if u&m==m)
 return out if min(out.values())>=0 else None

def moments(ns,s):
 ns={int(m):n for m,n in ns.items()}
 return {m:sum(v for u,v in ns.items() if u&m==m) for m in range(1,1<<s)}
def project(inc,S):return {m:inc[sum(1<<S[i] for i in range(len(S)) if m>>i&1)] for m in range(1,1<<len(S))}
def lift(inc,S):return {sum(1<<S[i] for i in range(len(S)) if m>>i&1):v for m,v in inc.items()}

def join_domain(src,s):
 # Prefix extension: start at the view omitting the last outsider; then index
 # remaining allowed views by all already-known shared inclusions.
 views=[(0,1)+S for S in combinations(range(2,s),s-3)];rows=[moments(r['counts'],s-1) for r in src if not r['strict']];seen=set()
 def go(j,inc):
  if j==len(views):yield inc;return
  S=views[j]
  shared=[m for m in range(1,1<<(s-1)) if sum(1<<S[i] for i in range(s-1) if m>>i&1) in inc]
  need={m:inc[sum(1<<S[i] for i in range(s-1) if m>>i&1)] for m in shared}
  for r in rows:
   if all(r[m]==need[m] for m in shared):yield from go(j+1,inc|lift(r,S))
 for base in rows:
  for inc in go(1,lift(base,views[0])):
   outs=sum(1<<i for i in range(2,s));caps={}
   missing=(outs,outs|1,outs|2,(1<<s)-1)
   assert set(inc)==set(range(1,1<<s))-set(missing)
   for m in missing:
    upper=min((inc[u] for u in inc if u&m==u),default=35)
    if m.bit_count()==5:upper=min(upper,1)
    if m.bit_count()>5:upper=0
    caps[m]=range(upper+1)
   for vals in product(*(caps[m] for m in missing)):
    ns=rec({0:35}|inc|dict(zip(missing,vals)),s)
    if ns is not None:seen.add(key(ns,s))
 return seen

def main():
 st=time.time();checks=[];tr=json.loads((BASE/'TWO_SIXES_TRIPLES.json').read_text())['cases'];allow={}
 for r in tr:
  if not r['strict']:allow.setdefault(tuple(r['codegrees']),set()).add(r['triple']) if r['degrees']==[6,6,7] else None
 seen=set();pairs=list(combinations(range(4),2));triples=list(combinations(range(4),3))
 for c in (1,2):
  for aa in product((1,2),repeat=4):
   a,b,d,e=aa
   for zw in (1,2,3):
    pv=(c,a,b,d,e,zw);inc={0:35,1:6,2:6,4:7,8:7}|{sum(1<<i for i in S):v for S,v in zip(pairs,pv)}
    opts=[allow.get((c,*sorted((a,d))),()),allow.get((c,*sorted((b,e))),()),range(min(a,b,zw)+1),range(min(d,e,zw)+1)]
    for ts in product(*opts):
     for q in range(min(ts)+1):
      ns=rec(inc|{sum(1<<i for i in S):v for S,v in zip(triples,ts)}|{15:q},4)
      if ns is not None:seen.add(key(ns,4))
 four=[r for r in json.loads((HERE/'FOUR_DP.json').read_text())['cases'] if r['degrees']==[6,6,7,7]];assert seen=={key(r['counts'],4) for r in four};checks.append(dict(file='FOUR_DP.json degree6677',domain=len(seen)))
 five=json.loads((HERE/'FIVE_SEVENS_DP.json').read_text())['cases'];seen=join_domain(four,5);assert seen=={key(r['counts'],5) for r in five};checks.append(dict(file='FIVE_SEVENS_DP.json',domain=len(seen)))
 six=json.loads((HERE/'SIX_SEVENS_DP.json').read_text())['cases'];seen=join_domain(five,6);assert seen=={key(r['counts'],6) for r in six};checks.append(dict(file='SIX_SEVENS_DP.json',domain=len(seen)))
 replay=[]
 for name,rows in [('FOUR_DP.json degree6677',four),('FIVE_SEVENS_DP.json',five),('SIX_SEVENS_DP.json',six)]:
  vals=[verify(r) for r in rows];replay.append(dict(file=name,cases=len(rows),strict=sum(v<1 for v in vals),max_strict=str(max((v for v in vals if v<1),default=Fraction()))))
 result=dict(status='PASS',scope=__doc__,domain_checks=checks,fixed_replay=replay,profiles=sum(len(rows) for rows in (four,five,six)),elapsed_seconds=time.time()-st)
 (HERE/'AUDIT.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
if __name__=='__main__':main()
