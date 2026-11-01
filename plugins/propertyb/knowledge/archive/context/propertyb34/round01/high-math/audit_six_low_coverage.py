"""Replay local generators and bind all residue / certificate projections for the r=6 proof."""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,time
sys.dont_write_bytecode=True
HERE=Path(__file__).parent;ROOT=HERE.parents[3]
sys.path.insert(0,str(HERE))
from six_low_extension import extensions as first_extensions
from six_low_two_high import extensions as second_extensions,canonical7,remove_first_high
from six_low_three_high import canonical8

def counts(x):return {int(t):n for t,n in x['counts'].items()}
def key(ns):return tuple(sorted(ns.items()))
def valid(ns,s,high_codegree=1):
 assert sum(ns.values())==34 and all(n>0 and t.bit_count()<=5 for t,n in ns.items())
 assert all(sum(n for t,n in ns.items() if t&(1<<i))==(6 if i<6 else 7) for i in range(s))
 for i in range(s):
  for j in range(i):
   assert sum(n for t,n in ns.items() if t&(1<<i) and t&(1<<j))==(high_codegree if i>=6 and j>=6 else 1)

if __name__=='__main__':
 start=time.perf_counter();src=json.loads((ROOT/'context/propertyb34-hour1-20261013/high-math/MIXED_SIX_v24_low6_badnone.json').read_text())['results']
 first=json.loads((HERE/'SIX_LOW_EXTENSION.json').read_text())['results'];joint=json.loads((HERE/'SIX_EXTENSION_JOINT.json').read_text())['results']
 first_by={x['group']:x for x in first};joint_by={canonical7(counts(x)):x for x in joint};bad7={k:x for k,x in joint_by.items() if Q(x['bound'])>=1}
 assert len(bad7)==5;good7=set();all7=set();first_n=0
 for x in src:
  if x['group'] not in (1,3,5,8):continue
  generated=list(first_extensions(counts(x)));saved=first_by[x['group']]['cases']
  assert {key(n) for n in generated}=={key(counts(z)) for z in saved};assert len(generated)==len(saved)
  for z in saved:
   ns=counts(z);valid(ns,7);k=canonical7(ns);all7.add(k);first_n+=1
   if Q(z['bound'])<1:good7.add(k)
   else:
    assert k in joint_by
    if Q(joint_by[k]['bound'])<1:good7.add(k)
 assert all7==good7|set(bad7) and not good7&set(bad7)
 second=[];saved8=[]
 for filename,cs in [('SIX_LOW_TWO_HIGH.json',(1,2)),('SIX_LOW_HIGHER_CODEGREE.json',(3,4))]:
  data=json.loads((HERE/filename).read_text());assert data['complete']
  for g in data['results']:
   x=next(x for x in bad7.values() if x['graph']==g['graph'] and x['group']==g['group']);ns=counts(x)
   generated=0;covered=0;remain={};badn=0
   for c in cs:
    for nc in second_extensions(ns,c):
     generated+=1;valid(nc,8,c);p=canonical7(remove_first_high(nc));assert p in all7
     if p in good7:covered+=1;continue
     remain[c,key(nc)]=nc
   assert generated==g['complete_extensions'] and covered==g['covered_by_second_high_projection']
   assert set(remain)=={(z['codegree'],key(counts(z))) for z in g['cases']}
   for z in g['cases']:
    if Q(z['bound'])>=1:
     assert z['codegree']==1;badn+=1;saved8.append(z)
   second.append(dict(source=filename,low_type=g['graph'],first_high_type=g['group'],generated=generated,covered_by_other_projection=covered,position_cases=len(g['cases']),residues=badn))
 bad8={canonical8(counts(z)) for z in saved8};assert len(saved8)==12 and len(bad8)==4
 third=json.loads((HERE/'SIX_LOW_THREE_HIGH.json').read_text());assert third['complete'] and third['base_orbits']==4
 assert {canonical8(counts(g)) for g in third['results']}==bad8
 assert all(not g['cases'] and g['covered_by_other_projection']==g['complete_extensions'] for g in third['results'])
 out=dict(scope=__doc__,elapsed=time.perf_counter()-start,first_labelled=first_n,first_colored_orbits=len(all7),first_remaining_orbits=len(bad7),second=second,second_remaining_labels=len(saved8),second_remaining_orbits=len(bad8),third_extensions=sum(g['complete_extensions'] for g in third['results']),third_residues=0,all_bindings_pass=True)
 (HERE/'SIX_LOW_COVERAGE_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
