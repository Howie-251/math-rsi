exec(open(__file__.replace('two_nonunit.py','adaptive.py')).read().split('for v in range(34,39):')[0])
def nonunit(v,d,e,lam):
 ans=None
 for pos in ((v//2,v//2+1),(v//2,v//2-1),(v//2-1,v//2+1),(v//2-2,v//2-1),(v//2+1,v//2+2)):
  for ds in sorted(set(((d,e),(e,d)))):
   ell={3:lam,1:ds[0]-lam,2:ds[1]-lam,0:66-d-e+lam};ell={t:n for t,n in ell.items() if n}
   u=bound(v,pos,ell)
   row=dict(v=v,degrees=[d,e],lam=lam,assigned=ds,positions=pos,U=str(u),strict=u<1)
   if ans is None or u<F(ans['U']):ans=row
   if u<1:return row
 return ans
for v in range(34,39):
 for d in range(c.ceilings(v-1,5),396//v+1):
  E=5*d-v+1
  for q in range(1,min(d,5)+1):
   n=v-1-E//q;emax=d+(396-v*d)//n;fails=[];nrows=0
   for e in range(d,emax+1):
    for lam in range(1,min(q,d,e)+1):
     r=nonunit(v,d,e,lam);rows.append(r);nrows+=1
     if not r['strict']:fails.append(r)
   branches.append(dict(v=v,d=d,q=q,n=n,emax=emax,count=nrows,failures=fails,strict=not fails))
   if not fails:break
result=dict(rows=rows,branches=branches,cpu_seconds=time.process_time()-start,stats=av.stats)
(P/'TWO_NONUNIT.json').write_text(json.dumps(result,indent=2))
for v in range(34,39):
 print('v',v,[(r['d'],r['q'],r['emax'],len(r['failures'])) for r in branches if r['v']==v])
print('CPU',result['cpu_seconds'])
