"""Independent Cartesian high-trace domain and exact saved-position/partition replay."""
from core_pilot import *
from fractions import Fraction
def independent_domain(name):
 ds,edges=CORES[name];s=len(ds);edges={tuple(sorted(e)) for e in edges}
 pairs={(1<<i)|(1<<j):1+int((i,j) in edges) for i,j in itertools.combinations(range(s),2)}
 high=[m for m in range(1,1<<s) if m.bit_count()>=3]
 ranges=[range(1+min([v for p,v in pairs.items() if p&m==p]+([1] if m.bit_count()==5 else []))) for m in high]
 out=[]
 for values in itertools.product(*ranges):
  ns=dict(zip(high,values))
  for p,v in pairs.items():ns[p]=v-sum(n for m,n in zip(high,values) if m&p==p)
  if min(ns.values())<0:continue
  for i,d in enumerate(ds):ns[1<<i]=d-sum(n for m,n in ns.items() if m>>i&1)
  ns[0]=35-sum(ns.values())
  if min(ns.values())>=0:out.append(tuple(ns[m] for m in range(1<<s)))
 return set(out)
def automorphisms(name):
 ds,ed=CORES[name];ed={tuple(sorted(e)) for e in ed};s=len(ds)
 return [p for p in itertools.permutations(range(s)) if all(ds[i]==ds[p[i]] for i in range(s)) and {tuple(sorted((p[i],p[j]))) for i,j in ed}==ed]
def canonical(ns,autos):
 return min(tuple(ns[sum(1<<p[i] for i in range(len(p)) if m>>i&1)] for m in range(len(ns))) for p in autos)
def main():
 st=time.time();raw=json.loads((HERE/'CORE_PILOT.json').read_text())['profiles'];part=json.loads((HERE/'PARTITION_PROBE.json').read_text())['profiles'];report=[];allreps={}
 for name in CORES:
  dom=list(domain(name));a={tuple(ns[m] for m in range(len(ns))) for ns in dom};b=independent_domain(name);assert a==b
  rr=[z for z in raw if z['core']==name];pp=[z for z in part if z['core']==name];assert len(rr)==len(pp)==len(dom)
  for ns,r,z in zip(dom,rr,pp):
   assert {int(k):v for k,v in r['counts'].items()}==ns
   exact=evaluate(23,ns,tuple(r['positions']),True)['bound'];assert exact==Fraction(r['bound']);assert (exact<1)==r['strict']
   s=sum(d==6 for d in CORES[name][0]);dem=[0]*(1<<s)
   for m,n in ns.items():
    low=m&((1<<s)-1)
    if low:dem[low]+=(5-m.bit_count())*n
   assert dem==z['demands']
   if 'partition_witness' in z:
    got=[0]*(1<<s);N=0
    for w in z['partition_witness']:
     blocks=w['blocks'];count=w['count'];assert count>=0 and sum(blocks)==(1<<s)-1
     assert sum(m.bit_count() for m in blocks)==s
     N+=count
     for m in blocks:got[m]+=count
    assert N==z['outside'] and got==dem
   else:
    assert name=='five_cycle_six' and z['lp_status']==2
    hi={m:n for m,n in ns.items() if m.bit_count()>=3 and n}
    if not hi or len(hi)==1 and next(iter(hi)).bit_count()==3:
     assert sum(dem[m] for m in range(len(dem)) if m.bit_count()>=2)>2*z['outside']
    else:
     assert len(hi)==1;quad=next(iter(hi));assert quad.bit_count()==4 and hi[quad]==1
     v=((1<<s)-1)^quad;assert dem[v]==0 and dem[quad]>0
  autos=automorphisms(name)
  groups={}
  for i,(ns,r,p) in enumerate(zip(dom,rr,pp)):
   key=canonical(tuple(ns[m] for m in range(len(ns))),autos)
   groups.setdefault(key,[]).append((i,ns,r,p))
  reps=[]
  for key,gg in groups.items():
   if any(r['strict'] or 'partition_witness' not in p for i,ns,r,p in gg):continue
   i,ns,r,p=gg[0];reps.append(dict(index=i,high_traces={m:n for m,n in ns.items() if m.bit_count()>=3 and n},counts=ns,orbit_size=len(gg)))
  allreps[name]=reps
  report.append(dict(core=name,domain=len(dom),automorphisms=len(autos),orbits=len(groups),strict=sum(z['strict'] for z in rr),strict_orbits=sum(any(r['strict'] for i,ns,r,p in gg) for gg in groups.values()),partition_feasible=sum('partition_witness' in z for z in pp),residual_orbits=len(reps),residual_labels=sum(z['orbit_size'] for z in reps),minimum=str(min(Fraction(z['bound']) for z in rr)),maximum=str(max(Fraction(z['bound']) for z in rr))))
 print(json.dumps(dict(status='PASS',elapsed_seconds=time.time()-st,cores=report),indent=2))
 (HERE/'REPLAY.json').write_text(json.dumps(dict(status='PASS',elapsed_seconds=time.time()-st,cores=report),indent=2)+'\n')
 (HERE/'RESIDUAL_ORBITS.json').write_text(json.dumps(allreps,indent=2)+'\n')
if __name__=='__main__':main()
