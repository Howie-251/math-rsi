from profile import *
class AvoidCalculator(src.Calculator):
 def deletion(self,v,pos,counts,j):
  typ=[T for T,n in counts.items()if n and T>>j&1];cells=[]
  for i,T in enumerate(typ):
   for U in typ[i:]:
    cap=src.C(counts[T],2)if T==U else counts[T]*counts[U]
    if cap:cells.append((self.weight(v,pos,pos[j],T,U)+self.weight(v,pos,pos[j],U,T),cap,T|U))
  best=F(0)
  for R in range(1<<len(pos)):
   if R>>j&1:continue
   f=sum(n for T,n in counts.items()if T>>j&1 and not T&R)
   q=max(0,src.CEIL(8*f-(v-1-R.bit_count()),7));val=F(0)
   for w,cap,U in sorted(cells):
    if U&R:continue
    z=min(q,cap);q-=z;val+=z*w
   assert q==0
   best=max(best,val)
  return best
if __name__=='__main__':
 start=time.process_time();cal=AvoidCalculator(9,542);base=json.loads((P/'PROFILE.json').read_text());rows=[]
 for r in base['failures']:
  if r['kind']!='two':continue
  v=r['v'];ell={int(t):n for t,n in r['ell'].items()};best=None
  for pos in((v//2,v//2+1),(v//2,v//2-1),(v//2-1,v//2),(v//2+1,v//2)):
   u=cal.bound(v,pos,ell)
   if best is None or u<best[0]:best=(u,pos)
   if u<1:break
  rows.append(r|dict(U=str(best[0]),positions=best[1],strict=best[0]<1))
  for fun in(cal.context,cal.endpoint,cal.weight):fun.cache_clear()
 out=dict(rows=rows,failures=[r for r in rows if not r['strict']],cpu_seconds=time.process_time()-start)
 (P/'REPAIR.json').write_text(json.dumps(out,indent=2));print('rows',len(rows),'failures',len(out['failures']),'CPU',out['cpu_seconds'])
 for r in out['failures']:print(r['v'],r['degrees'],r['U'])
