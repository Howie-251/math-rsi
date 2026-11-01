from probe import *

def profiles(ds,ls):
 triples=[7,11,13,14];pairs=list(combinations(range(4),2));lam={((1<<i)|(1<<j)):c for (i,j),c in zip(pairs,ls)}
 for t4 in range(min(ls)+1):
  caps=[min(c for mask,c in lam.items() if t&mask==mask)-t4 for t in triples]
  for t3 in product(*[range(c+1) for c in caps]):
   counts={15:t4};counts.update(dict(zip(triples,t3)))
   for mask,c in lam.items():counts[mask]=c-t4-sum(n for t,n in zip(triples,t3) if t&mask==mask)
   if min(counts.values())<0:continue
   for i,d in enumerate(ds):counts[1<<i]=d-sum(c for t,c in counts.items() if t&(1<<i))
   counts[0]=34-sum(counts.values())
   if min(counts.values())<0:continue
   yield counts,t4,t3

def quad(v,ds,ls,fast=True):
 out=[]
 for counts,t4,t3 in profiles(ds,ls):
  opts=[]
  positions=[tuple(range(k,k+4)) for k in ((9,8,10) if fast else range(6,13))]
  done=False
  for pos in positions:
   for pp in permutations(pos):
    p=Profile(v,5,pp,counts);cs=[certificate(p,i) for i in range(4)]
    rs=rows(p,deductions={pp[i]:cs[i]['loss'] for i in range(4)})
    rr=dict(v=v,ds=ds,ls=ls,t4=t4,t3=t3,counts=counts,pos=pp,cs=cs,rows=rs,bound=total_bound(rs));opts.append(rr)
    if rr['bound']<1:done=True;break
   if done:break
  out.append(min(opts,key=lambda r:r['bound']))
 return out
if __name__=='__main__':
 start=time.time();out=[]
 for ds,ls in [((7,7,7,8),(2,2,c,2,c,c)) for c in (1,2)]+[((7,7,8,8),(2,a,b,a,b,c)) for a in (1,2) for b in (1,2) for c in (1,2,3)]:
  cases=quad(20,ds,ls);out+=cases
  fail=[(r['t4'],r['t3'],str(r['bound'])) for r in cases if r['bound']>=1]
  print(ds,ls,'pass',len(cases)-len(fail),'of',len(cases),'fails',fail,flush=True)
 Path(__file__).with_name('QUAD_MIXED.json').write_text(json.dumps(json_value(dict(cases=out,seconds=time.time()-start)),indent=2))
 print('seconds',time.time()-start)
