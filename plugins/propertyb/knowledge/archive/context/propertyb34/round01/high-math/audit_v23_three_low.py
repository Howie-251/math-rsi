"""Regenerate every common-unit-high domain and bind all exact certificates."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import sys,json,time
sys.dont_write_bytecode=True
HERE=Path(__file__).parent;sys.path.insert(0,str(HERE))
from v23_three_low import generate,verify

if __name__=='__main__':
 start=time.perf_counter();out=[];dual_count=0
 for h in (1,2,3,4):
  src=json.loads((HERE/f'V23_THREE_LOW_H{h}.json').read_text());assert src['complete']
  groups,raw,filtered=generate(h)
  known={(tuple(z['degrees']),tuple(sorted((int(t),n) for t,n in z['counts'].items()))):z for z in src['results']}
  assert len(known)==len(src['results'])==len(groups) and set(known)==set(groups)
  assert raw==src['raw'] and filtered==src['filtered']
  joint=direct=0;remaining=[]
  for (ds,key),gid in groups.items():
   z=known[ds,key];assert z['group']==gid;ns=dict(key);s=len(ds)
   assert sum(ns.values())==34 and all(n>0 and t.bit_count()<=5 for t,n in ns.items())
   assert tuple(sum(n for t,n in ns.items() if t&(1<<i)) for i in range(s))==ds
   assert ds[:3]==(6,6,6) and all(d in (7,8) for d in ds[3:])
   for i in range(3):
    assert sum(sum(n for t,n in ns.items() if t&(1<<i) and t&(1<<j))-1 for j in range(s) if j!=i)<=2
    assert all(sum(n for t,n in ns.items() if t&(1<<i) and t&(1<<j))==1 for j in range(3,s))
   if h==4:assert ds.count(7)>=2
   if Q(z['final_bound'])>=1:remaining.append(z['group']);continue
   if Q(z['bound'])<1:assert z['independent_ABC'] and Q(z['final_bound'])==Q(z['bound']);direct+=1
   else:
    cert=z['joint'];assert cert['counts']==z['counts'] and Q(cert['bound'])==Q(z['final_bound']);verify(cert,23,s,ds);joint+=1;dual_count+=1
  if h==4:assert not remaining
  row=dict(high_count=h,raw=raw,projection_retained=filtered,orbits=len(groups),direct_strict=direct,joint_strict=joint,residue_groups=remaining,complete_regeneration_profile_and_bound_binding=True)
  out.append(row);print('PASS',h,len(groups),direct,joint,len(remaining),time.perf_counter()-start,flush=True)
 result=dict(scope=__doc__,stages=out,independent_duals_replayed=dual_count,all_bindings_pass=True,all_four_high_cases_strict=True,elapsed=time.perf_counter()-start)
 (HERE/'V23_THREE_LOW_COVERAGE_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n')
