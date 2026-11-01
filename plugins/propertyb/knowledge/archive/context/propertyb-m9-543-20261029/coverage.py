"""Actual minimum/partner decision-tree coverage and all trace identities."""
from profile import *
from collections import Counter
if __name__=='__main__':
 start=time.process_time();data=json.loads((P/'CANDIDATE.json').read_text());rows=data['rows'];table={};expected=set();selections=[]
 def key(v,kind,ds=(),triple=None):return(v,kind,tuple(ds),triple)
 for r in rows:
  k=key(r['v'],r['kind'],r.get('degrees',()),r.get('triple'));assert k not in table;table[k]=r
  assert F(r['U'])<1
  ell={int(T):n for T,n in r['ell'].items()};s=len(r['positions'])
  if not s:continue
  assert len(set(r['positions']))==s and all(1<=h<=r['v']for h in r['positions'])
  assert sum(ell.values())==542 and min(ell.values())>=0
  assert [sum(n for T,n in ell.items()if T>>j&1)for j in range(s)]==list(r['degrees'])
  if s>=2:
   for a,b in itertools.combinations(range(s),2):assert sum(n for T,n in ell.items()if T>>a&1 and T>>b&1)==1
  if s==3:
   assert ell.get(7,0)==r['triple']
 def consume_two(v,d):
  n=2*(v-1)-8*d;assert n>0;upper=d+(4878-v*d)//n
  assert v*d+n*(upper+1-d)>4878
  for e in range(d,upper+1):
   k=key(v,'two',(d,e))
   if k in table:expected.add(k);continue
   t=n-1-(8*e-v+1);assert t>0;budget=4878-v*d-n*(e-d);fmax=e+budget//t
   assert budget>=0 and v*d+n*(e-d)+t*(fmax+1-e)>4878
   selections.append(dict(v=v,d=d,e=e,common_pool=t,fmax=fmax))
   for f in range(e,fmax+1):
    for tri in(0,1):expected.add(key(v,'conditional_three',(d,e,f),tri))
 for v in range(57,196):
  if v<=134:expected.add(key(v,'zero'));continue
  if v<=182:
   for d in range(src.CEIL(v-1,8),4878//v+1):
    k=key(v,'one',(d,))
    if v<=154 and k in table:expected.add(k)
    else:consume_two(v,d)
  else:
   D=28;Z=29*v-4878;T=234-v;assert 16*Z>T*T
   for ds in itertools.combinations_with_replacement(range(src.CEIL(v-1,8),29),3):
    for tri in(0,1):expected.add(key(v,'three',ds,tri))
 assert set(table)==expected,(len(set(table)-expected),len(expected-set(table)))
 summary=[]
 for kind in('zero','one','two','conditional_three','three'):
  rr=[r for r in rows if r['kind']==kind];summary.append(dict(kind=kind,profiles=len(rr),vmin=min(r['v']for r in rr),vmax=max(r['v']for r in rr),maximum=str(max(F(r['U'])for r in rr))))
 out=dict(status='PASS actualbranchcoverage+traceidentities; arithmetickernelnotindependent',k=9,M=542,total_degree=4878,profiles=len(rows),summary=summary,maximum=str(max(F(r['U'])for r in rows)),conditional_parents=selections,cpu_seconds=time.process_time()-start)
 (P/'SUMMARY.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items()if k!='conditional_parents'},indent=2))
