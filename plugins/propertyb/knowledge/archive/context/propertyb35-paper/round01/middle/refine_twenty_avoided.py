from pilot import *
from avoided_lock_quotas import certificate as avoided

def evaluate_avoided(v,ns,pos,detail=False):
 p=Profile(v,5,pos,ns);cs=[]
 for i in range(len(pos)):
  bit=1<<i;mx=max(max(0,(4*sum(n for t,n in p.counts.items() if t&bit and not t&R)-(v-1-R.bit_count())+2)//3) for R in range(1<<len(pos)) if not R&bit)
  cs.append(avoided(p,i) if mx else dict(loss=Q(),dual=[],inventory=[]))
 _,rr=engine(v,tuple(pos)).bound(ns,True)
 value=sum((min(a,b,c-cs[pos.index(k)]['loss']) if k in pos else min(a,b,c) for k,(a,b,c) in enumerate(rr,1)),Q())
 out=dict(v=v,M=35,counts=ns,positions=pos,bound=value,strict=value<1,quotas=cs)
 if detail:
  rr2=rows(p,deductions={pos[i]:c['loss'] for i,c in enumerate(cs)});assert total_bound(rr2)==value
  out['rows']=rr2
 return out

def main():
 old=json.loads((HERE/'TWENTY_DELTA5_FULL.json').read_text());out=[];start=time.time()
 for idx,r in enumerate(old['cases']):
  if r['strict']:out.append(r);continue
  ns={int(t):n for t,n in r['counts'].items()};win=r|{'bound':Q(r['bound'])}
  poses=[tuple(r['positions'])]+list({p for k in range(7,13) for p in permutations(range(k,k+3))})
  for pos in poses:
   z=evaluate_avoided(20,ns,pos)
   if z['bound']<win['bound']:win=z
   if win['strict']:break
  zz=evaluate_avoided(20,ns,win['positions'],True);zz.update(degrees=r['degrees'],codegrees=r['codegrees'],triple=r['triple'],original_bound=r['bound'])
  out.append(zz);print(idx,r['degrees'],r['codegrees'],r['triple'],r['bound'],'->',zz['bound'],flush=True)
 (HERE/'TWENTY_DELTA5_AVOIDED.json').write_text(json.dumps(json_value(dict(scope='same necessary triple domain; exact dual certificates for all avoided-lock quotas',cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
 print('profiles',len(out),'strict',sum(z['strict'] for z in out),'seconds',time.time()-start)
if __name__=='__main__':main()
