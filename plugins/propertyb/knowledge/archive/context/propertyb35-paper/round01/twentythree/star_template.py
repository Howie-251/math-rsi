"""Distinct-center-link-block unit star templates, with exact actual center bad-pair count."""
from pair_pilot import *
from multilock import pair_weight
from fractions import Fraction as Q

def quota(p,i,total):
 bit=1<<i;k=p.positions[i];ts=sorted(t for t,n in p.counts.items() if n and t&bit);inv=[]
 for j,t in enumerate(ts):
  for u in ts[j:]:
   c=p.counts[t]*(p.counts[t]-1)//2 if t==u else p.counts[t]*p.counts[u]
   if c:inv.append([pair_weight(23,5,p.positions,t,u,k)+pair_weight(23,5,p.positions,u,t,k),c,t==bit and u==bit])
 pure=max(0,(4*p.counts.get(bit,0)-(p.v-len(p.positions))+2)//3);loss=Q();remaining=pure
 for z in sorted(inv):
  if z[2]:take=min(remaining,z[1]);z[1]-=take;remaining-=take;loss+=take*z[0]
 assert not remaining;remaining=max(0,total-pure)
 for z in sorted(inv):take=min(remaining,z[1]);remaining-=take;loss+=take*z[0]
 assert not remaining
 return loss

def ns_for(s,d):
 ns={m:0 for m in range(1<<(s+1))}
 for i in range(s):ns[1|(1<<(i+1))]=1
 ns[1]=6-s
 for i,j in itertools.combinations(range(s),2):ns[(1<<(i+1))|(1<<(j+1))]=1
 for i in range(s):ns[1<<(i+1)]=d-s
 ns[0]=35-sum(ns.values());return ns

def evaluate_q(ns,pos,q):
 p=Profile(23,5,pos,ns);cs=[certificate(p,i) for i in range(len(pos))];cs[0]['loss']=quota(p,0,q);cs[0]['q_total']=q
 rr=rows(p,deductions={pos[i]:c['loss'] for i,c in enumerate(cs)});return dict(bound=total_bound(rr),positions=pos,rows=rr,quotas=cs)

def main():
 st=time.time();out=[]
 for s in (4,5,6):
  pos=set();seeds=[tuple(range(k,k+s+1)) for k in range(1,24-s)]
  seeds += [tuple(range(1,s))+tuple([12,13]),tuple(range(8,8+s))+tuple([23])]
  for p in seeds:
   for i in range(s+1):pos.add((p[i],)+tuple(x for j,x in enumerate(p) if j!=i))
  for d in (6,7,8):
   ns=ns_for(s,d)
   for q in (1,2,3):
    z=min((evaluate_q(ns,p,q) for p in pos),key=lambda z:z['bound']);strict=z['bound']<1
    out.append(dict(neighbors=s,neighbor_degree=d,center_actual_bad_pairs=q,counts=ns,strict=strict,**z))
    print(s,d,q,z['bound'],z['positions'],flush=True)
 (HERE/'STAR_TEMPLATE.json').write_text(json.dumps(json_value(dict(scope=__doc__,elapsed_seconds=time.time()-st,profiles=out)),indent=2)+'\n')
 print('seconds',time.time()-st)
if __name__=='__main__':main()
