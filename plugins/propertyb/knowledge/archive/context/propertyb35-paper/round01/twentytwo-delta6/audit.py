"""Independent binomial/Fraction replay and RGS/Mobius domain reconstruction."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from itertools import product
from functools import lru_cache
import json,time
HERE=Path(__file__).resolve().parent
V=22
F=Q
@lru_cache(None)
def binom(n,k):return comb(n,k) if 0<=k<=n else 0
@lru_cache(None)
def pair(N,a,b,r,q,free):
 r-=int(free);q-=int(free);s=r+q+int(free)
 if min(r,q)<0 or s>N:return Q()
 den=binom(N,s)*(s*binom(s-1,r) if free else binom(s,r))
 return Q(binom(a,r)*binom(b,q),den)
def ABC(ns,pos):
 s=len(pos);N=V-s;full=(1<<s)-1;out=[]
 for k in range(1,V+1):
  L=sum(1<<i for i,p in enumerate(pos) if p<k);R=sum(1<<i for i,p in enumerate(pos) if p>k);p=full^L^R;free=p==0;a=k-1-L.bit_count();b=V-k-R.bit_count();A=B=C=Q();left=[];right=[]
  for t,c in ns.items():
   r=5-t.bit_count()
   if not p and r and not t&~L or p and t&p and not (t^p)&~L:
    A+=c*Q(binom(a,r-int(free)),binom(N,r));left.append((t,c,r))
   if not p and r and not t&~R or p and t&p and not (t^p)&~R:
    B+=c*Q(binom(b,r-int(free)),binom(N,r));right.append((t,c,r))
  for t,c,r in left:
   for u,d,q in right:
    assert t&u==p;C+=(c*d-(c if t==u else 0))*pair(N,a,b,r,q,free)
  out.append((A,B,C))
 return out
def w(t,u,i,pos):
 p=1<<i;k=pos[i];L=sum(1<<j for j,z in enumerate(pos) if z<k);R=sum(1<<j for j,z in enumerate(pos) if z>k)
 if t&u!=p or (t^p)&~L or (u^p)&~R:return Q()
 return pair(V-len(pos),k-1-L.bit_count(),V-k-R.bit_count(),5-t.bit_count(),5-u.bit_count(),False)
def deduction(ns,pos,i,c):
 p=1<<i;ts=sorted(t for t in ns if t&p);d=sum(ns[t] for t in ts);qt=max(0,(4*d-21+2)//3);qp=max(0,(4*ns.get(p,0)-(V-len(pos))+2)//3)
 assert (qt,qp)==(c['q_total'],c['q_pure']);slots=[]
 for j,t in enumerate(ts):
  for u in ts[j:]:
   cap=comb(ns[t],2) if t==u else ns[t]*ns[u]
   if cap:slots.append([w(t,u,i,pos)+w(u,t,i,pos),cap,t,u])
 loss=Q();left=qp
 for z in sorted(slots):
  if z[2]==z[3]==p:
   take=min(left,z[1]);left-=take;z[1]-=take;loss+=take*z[0]
 assert not left;left=max(0,qt-qp)
 for z in sorted(slots):
  take=min(left,z[1]);left-=take;loss+=take*z[0]
 assert not left and loss==Q(c['loss']);return loss
def verify(r):
 ns={int(t):n for t,n in r['counts'].items() if n};pos=r['positions'];s=len(pos)
 assert sum(ns.values())==35 and len(set(pos))==s and all(1<=p<=V for p in pos)
 ds=[sum(n for t,n in ns.items() if t>>i&1) for i in range(s)]
 if 'neighbor_degrees'in r:assert ds==[6]+r['neighbor_degrees']
 else:assert ds==r['degrees']
 if 'neighbor_degrees'in r:assert all(sum(n for t,n in ns.items() if t&(1|1<<i)==(1|1<<i))==1 for i in range(1,s))
 loss={pos[i]:deduction(ns,pos,i,c) for i,c in enumerate(r.get('certificates',r.get('quotas')))}
 z=sum((min(A,B,C-loss.get(k,Q())) for k,(A,B,C) in enumerate(ABC(ns,pos),1)),Q());assert z==Q(r['bound']) and r['strict']==(z<1);return z
def partitions(n):
 def gen(a):
  if len(a)==n:
   yield tuple(tuple(i for i,x in enumerate(a) if x==b) for b in range(max(a)+1));return
  for x in range(max(a)+2):yield from gen(a+[x])
 yield from gen([0])
def domain(n,d):
 out=set();full=(1<<n)-1
 higher=[t for t in range(1,full+1) if t.bit_count()>=3]
 for P in partitions(n):
  for values in product((0,1),repeat=len(higher)):
   I={1<<i:d for i in range(n)}|{t:1 for t in range(1,full+1) if t.bit_count()==2}|dict(zip(higher,values))
   J={t:I[t]-int(any(t&sum(1<<i for i in B)==t for B in P)) for t in I}
   ns={t<<1:sum((-1)**(u.bit_count()-t.bit_count())*J[u] for u in J if u&t==t) for t in J}
   ns[0]=29-sum(ns.values());ns[1]=6-len(P)
   for B in P:ns[1+sum(2<<i for i in B)]=1
   if any(c<0 for c in ns.values()):continue
   out.add(tuple(sorted((t,c)for t,c in ns.items()if c)))
 return out
def main():
 start=time.process_time();out=[]
 for file in ['PAIRS.json','NONUNIT_PAIRS.json','EIGHT_PAIRS.json','UNIT_STAR_THREE.json','FOUR_UNITS.json','EIGHT_THREE.json','EIGHT_FOUR_PILOT.json']:
  rr=json.loads((HERE/file).read_text())['cases'];vals=[verify(r) for r in rr]
  out.append(dict(file=file,cases=len(rr),strict=sum(x<1 for x in vals),maximum_strict=str(max((x for x in vals if x<1),default=Q()))))
  if file=='FOUR_UNITS.json':
   for d in (6,7,8):
    rs=[r for r in rr if r['neighbor_degrees']==[d]*4]
    assert domain(4,d)=={tuple(sorted((int(t),c) for t,c in r['counts'].items() if c))for r in rs}
  if file=='UNIT_STAR_THREE.json':
   for d in (6,7,8):
    rs=[r for r in rr if r['neighbor_degrees']==[d]*3]
    assert domain(3,d)=={tuple(sorted((int(t),c) for t,c in r['counts'].items() if c))for r in rs}
 # Independent full 246-domain reconstruction, all three pair moments 1..3.
 full3=set()
 for part in partitions(3):
  for ps in product(range(1,4),repeat=3):
   for tau in range(min(ps)+1):
    I={1:8,2:8,4:8,3:ps[0],5:ps[1],6:ps[2],7:tau}
    J={t:I[t]-int(any(t&sum(1<<i for i in B)==t for B in part))for t in I}
    ns={t<<1:sum((-1)**(u.bit_count()-t.bit_count())*J[u]for u in J if u&t==t)for t in J}
    ns[0]=29-sum(ns.values());ns[1]=6-len(part)
    for B in part:ns[1+sum(2<<i for i in B)]=1
    if all(c>=0 for c in ns.values()):full3.add(key(ns))
 triples=json.loads((HERE/'EIGHT_THREE.json').read_text())['cases'];byid={r['source_id']:r for r in triples}
 assert full3=={key(r['counts'])for r in triples}
 joint_values=[]
 for r in json.loads((HERE/'EIGHT_THREE_JOINT.json').read_text())['results']:
  if Q(r.get('bound','2'))<1:
   assert key(r['counts'])==key(byid[r['source_id']]['counts']);joint_values.append(verify_joint(r))
 result=dict(status='PASS',method=__doc__,results=out,joint_strict_replayed=len(joint_values),cpu_seconds=time.process_time()-start,review_independence='same-family',acceptance_status='provisional')
 (HERE/'AUDIT.json').write_text(json.dumps(result,indent=2)+'\n');print(result)


def key(ns):return tuple(sorted((int(t),n)for t,n in ns.items()if n))
def verify_joint(x):
    ns=dict(key(x['counts']));s=max(t.bit_length() for t in ns);expected=[]
    for i in range(s):
        ts=sorted(t for t in ns if t>>i&1)
        for a,t in enumerate(ts):
            for u in ts[a:]:
                cap=comb(ns[t],2) if t==u else ns[t]*ns[u]
                if cap: expected.append(dict(center=i,t=t,u=u,capacity=cap))
    assert expected==x['slots'];slots_=expected;demand=[F()]*len(expected);quota=F()
    for c in x['quotas']:
        i,R=c['center'],c['avoid'];alpha=F(c['delta']);assert alpha>=0 and not R&(1<<i)
        f=sum(v for t,v in ns.items() if t>>i&1 and not t&R)
        q=max(0,(4*f-21+R.bit_count()+2)//3)
        ids=[j for j,z in enumerate(expected) if z['center']==i and not (z['t']|z['u'])&R]
        assert c.get('kind') is None and (f,q,ids)==(c['edge_count'],c['q'],c['slots'])
        quota+=q*alpha
        for j in ids:demand[j]+=alpha
    free=linear=mass=F();ws=[F()]*len(expected)
    for layout in x['layouts']:
        g=F(layout['probability']);assert g>0;mass+=g;pos=layout['positions'];rr=ABC(ns,pos)
        free0=sum((min(z) for k,z in enumerate(rr,1) if k not in pos),F());assert free0==F(layout['free'],x['scale']);free+=g*free0
        for i,c in enumerate(layout['centers']):
            beta=F(layout['betas'][i]);assert 0<=beta<=g
            A,B,C=rr[pos[i]-1];ab=min(A,B)
            assert (ab,C)==(F(c['a'],x['scale']),F(c['c'],x['scale']));linear+=(g-beta)*ab+beta*C
            ww=[]
            for j,z in enumerate(expected):
                if z['center']==i:
                    weight0=w(z['t'],z['u'],i,pos)+w(z['u'],z['t'],i,pos);ww.append(weight0);ws[j]+=beta*weight0
            assert ww==[F(w,x['scale']) for w in c['weights']]
    assert mass==1
    penalties=[max(F(),d-w) for d,w in zip(demand,ws)]
    assert penalties==[F(z) for z in x['penalties']]
    penalty=sum((z['capacity']*p for z,p in zip(expected,penalties)),F());z=free+linear-quota+penalty
    assert (free,linear,quota,penalty)==tuple(F(x[k]) for k in ['free_average','linear_part','quota_part','capacity_penalty'])
    assert z==F(x['bound'])<1
    return z

if __name__=='__main__':main()
