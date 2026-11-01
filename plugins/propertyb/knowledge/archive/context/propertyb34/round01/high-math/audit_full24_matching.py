"""Complete catalogue regeneration/binding and independent probability certificates.

Extension regeneration uses the documented generator; it is a coverage-binding
audit, not a claim of a second independent classification implementation.
The probability/dual replay uses the independent labelled-injection code.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import sys,json,time
sys.dont_write_bytecode=True
HERE=Path(__file__).parent;sys.path.insert(0,str(HERE))
from eighth_matching import canonical,extensions,graph
from complete_eight_matching import drop
from verify_joint import verify
from mixed_six import profiles

def key(ns):return tuple(sorted((int(t),n) for t,n in ns.items()))
def invariant(ns,s,qmax=None):
 ns={int(t):n for t,n in ns.items()}
 assert sum(ns.values())==34 and all(n>0 and t.bit_count()<=5 for t,n in ns.items())
 ds=[sum(n for t,n in ns.items() if t&(1<<i)) for i in range(s)]
 assert all(d in (6,7) for d in ds)
 if qmax is not None:assert ds.count(6)<=qmax
 md=[0]*s
 for i in range(s):
  for j in range(i):
   c=sum(n for t,n in ns.items() if t&(1<<i) and t&(1<<j));assert c in (1,2)
   if c==2:assert ds[i]==ds[j];md[i]+=1;md[j]+=1
 assert max(md)<=1
 return ns,ds

if __name__=='__main__':
 start=time.perf_counter();report=dict(scope=__doc__)
 bases=[]
 for m in range(4):
  gs,raw,valid=profiles([7]*6,[3<<(2*i) for i in range(m)])
  assert raw==valid
  bases.append(dict(matching=m,raw=raw,all_seven_degree_restorations_nonnegative=True,orbits=len(gs)))
 report['six_bases']=bases
 cat=json.loads((HERE/'SEVEN_HOMOGENEOUS_MATCHING.json').read_text());assert cat['complete']
 expected={j:x for j,x in enumerate(cat['profiles']) if x['low_count']<=3}
 seven=json.loads((HERE/'SEVEN_HOMOGENEOUS_MATCHING_BOUNDS.json').read_text());assert seven['complete']
 records={x['group']:x for x in seven['results']};assert set(records)==set(expected)
 good={};bad=[]
 for j,x in records.items():
  assert x['counts']==expected[j]['counts'];ns,ds=invariant(x['counts'],7,3)
  assert ds.count(6)==x['low_count']
  if Q(x['bound'])<1:assert x['independent_ABC'];good[key(ns)]=dict(group=j,source='seven_direct',bound=x['bound'])
  elif x['low_count']>=1:bad.append(x)
 q0joint=json.loads((HERE/'SEVEN_MATCHING_QMAX0_JOINT.json').read_text())['results']
 joint_checks=[]
 for x in q0joint:
  if Q(x['bound'])<1:joint_checks.append(verify(x,24,'mixed'));good[key(x['counts'])]=dict(group=x['group'],source='q0_joint',bound=x['bound'])
 report['seven']=dict(orbits=len(records),direct_strict=sum(Q(x['bound'])<1 for x in records.values()),mixed_bad=len(bad),all_invariants_and_bound_binding=True)
 table=json.loads((HERE/'EIGHTH_LOW_COMPLETE_CATALOGUE.json').read_text());assert table['complete']
 known={key(x['counts']):x for x in table['covered']+table['residuals']};assert len(known)==table['orbits']
 seen=set();raw=0;parentcounts=[]
 for x in bad:
  ns,ds=invariant(x['counts'],7,3);matched={i for p in graph(ns,7) for i in p}
  for p in [None]+[i for i in range(7) if i not in matched and ds[i]==6]:
   nr=0
   for nc in extensions(ns,7,6,p):
    nr+=1;raw+=1;k=canonical(nc,8);assert k in known;seen.add(k)
   parentcounts.append(dict(group=x['group'],partner=p,raw=nr))
 assert parentcounts==table['parents'] and raw==table['raw'] and seen==set(known)
 for x in table['covered']:
  ns,ds=invariant(x['counts'],8,4);w=x['projection'];k=canonical(drop(ns,w['dropped']),7)
  assert k in good and all(w[a]==good[k][a] for a in ('group','source','bound'))
 bb=json.loads((HERE/'EIGHTH_LOW_COMPLETE_BOUNDS.json').read_text());assert bb['complete']
 byid={x['group']:x for x in table['residuals']};boundbyid={x['group']:x for x in bb['results']};assert set(byid)==set(boundbyid)
 joint=json.loads((HERE/'EIGHTH_LOW_COMPLETE_JOINT.json').read_text());assert joint['complete'];jd={x['group']:x for x in joint['results']}
 for j,x in boundbyid.items():
  assert x['counts']==byid[j]['counts'] and x['independent_ABC'];invariant(x['counts'],8,4)
  if Q(x['bound'])>=1:
   y=jd[j];assert y['counts']==x['counts'];joint_checks.append(verify(y,24,'mixed'))
 assert set(jd)=={j for j,x in boundbyid.items() if Q(x['bound'])>=1}
 report['mixed_eighth']=dict(parents=len(bad),raw=raw,orbits=len(known),strict_projection=len(table['covered']),direct_strict=sum(Q(x['bound'])<1 for x in bb['results']),joint_strict=len(jd),complete_regeneration_and_binding=True)
 q0=json.loads((HERE/'SEVEN_MATCHING_QMAX0_BOUNDS.json').read_text());assert q0['complete']
 q0done={x['group'] for x in q0joint if Q(x['bound'])<1};q0bad=[x for x in q0['results'] if Q(x['bound'])>=1 and x['group'] not in q0done]
 ext=json.loads((HERE/'EIGHTH_MATCHING_Q0.json').read_text());assert ext['complete'];known0={key(x['counts']):x for x in ext['results']};seen0=set();raw0=0;stats=[]
 for x in q0bad:
  ns,ds=invariant(x['counts'],7,0);matched={i for p in graph(ns,7) for i in p}
  for degree in (6,7):
   for p in [None]+[i for i in range(7) if i not in matched and ds[i]==degree]:
    nr=0
    for nc in extensions(ns,7,degree,p):
     nr+=1;raw0+=1;k=canonical(nc,8);assert k in known0;seen0.add(k)
    stats.append(dict(group=x['group'],new_degree=degree,partner=p,raw=nr))
 assert seen0==set(known0) and raw0==ext['raw'] and stats==ext['parents']
 j0=json.loads((HERE/'EIGHTH_MATCHING_Q0_JOINT.json').read_text())['results'];j0={x['group']:x for x in j0}
 for x in ext['results']:
  invariant(x['counts'],8,1);assert x['independent_ABC']
  if Q(x['bound'])>=1:
   y=j0[x['group']];assert y['counts']==x['counts'];joint_checks.append(verify(y,24,'mixed'))
 assert set(j0)=={x['group'] for x in ext['results'] if Q(x['bound'])>=1}
 report['q0_eighth']=dict(parents=len(q0bad),raw=raw0,orbits=len(known0),direct_strict=len(known0)-len(j0),joint_strict=len(j0),complete_regeneration_and_binding=True)
 report.update(independent_dual_checks=joint_checks,all_covered=True,elapsed=time.perf_counter()-start)
 (HERE/'FULL24_MATCHING_COVERAGE_AUDIT.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2),flush=True)
