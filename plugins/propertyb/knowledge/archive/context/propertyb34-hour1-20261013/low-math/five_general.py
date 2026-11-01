from probe import *

def profiles(s,ds,ls,forbid=()):
 pairs=list(combinations(range(s),2));pairmask=[(1<<i)|(1<<j) for i,j in pairs]
 caps=dict(zip(pairmask,ls));large=[m for m in range(1<<s) if 3<=m.bit_count()<=5 and m not in forbid]
 large.sort(key=lambda m:(-m.bit_count(),m))
 def rec(j,chosen,remaining):
  if j==len(large):
   counts=chosen.copy();counts.update(remaining)
   for i,d in enumerate(ds):counts[1<<i]=d-sum(c for m,c in counts.items() if m&(1<<i))
   counts[0]=34-sum(counts.values())
   if min(counts.values())>=0:yield counts
   return
  m=large[j];inc=[p for p in pairmask if p&m==p]
  for c in range(min(remaining[p] for p in inc)+1):
   nr=remaining.copy()
   for p in inc:nr[p]-=c
   if c:chosen[m]=c
   else:chosen.pop(m,None)
   yield from rec(j+1,chosen,nr)
  chosen.pop(m,None)
 yield from rec(0,{},caps)

def calc_counts(v,ds,counts,pos):
 p=Profile(v,5,pos,counts);cs=[certificate(p,i) for i in range(len(ds))]
 rs=rows(p,deductions={pos[i]:cs[i]['loss'] for i in range(len(ds))})
 return dict(v=v,ds=ds,pos=pos,counts=counts,cs=cs,rows=rs,bound=total_bound(rs))
if __name__=='__main__':
 start=time.time();out=[]
 s=5;ds=(7,7,8,8,8);ls=(2,1,1,1,1,1,1,2,2,2)
 forbid=[m for m in range(1<<s) if m.bit_count()>=3 and m&3==3]
 for idx,counts in enumerate(profiles(s,ds,ls,forbid)):
  bestrow=None
  for k in (8,9,7,10):
   for pp in permutations(range(k,k+s)):
    r=calc_counts(20,ds,counts,pp)
    if bestrow is None or r['bound']<bestrow['bound']:bestrow=r
    if r['bound']<1:break
   if bestrow['bound']<1:break
  out.append(bestrow)
  print(idx,bestrow['pos'],bestrow['bound'],flush=True)
 Path(__file__).with_name('FIVE_77888.json').write_text(json.dumps(json_value(dict(cases=out,seconds=time.time()-start)),indent=2))
 print('PASS',sum(r['bound']<1 for r in out),'/',len(out),'sec',time.time()-start)
