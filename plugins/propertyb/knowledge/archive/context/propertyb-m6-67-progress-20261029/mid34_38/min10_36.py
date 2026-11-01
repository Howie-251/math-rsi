exec(open(__file__.replace('min10_36.py','four_repair.py')).read().split('start=time.process_time()')[0])
start=time.process_time();rows=[];four=[];coverage=[];stopped=False
for a,b in itertools.combinations_with_replacement(range(10,13),2):
 ds=(10,a,b)
 for double in (-1,0,1,2):
  oldpairs=list(itertools.combinations(range(3),2));lam=[1]*3
  if double>=0:lam[double]=2
  for tau in (0,1):
   blocks=[]
   if tau:blocks.append(7)
   for pair,l in zip(oldpairs,lam):blocks += [sum(1<<j for j in pair)]*(l-tau)
   ell={}
   for bl in blocks:ell[bl]=ell.get(bl,0)+1
   for j,d in enumerate(ds):ell[1<<j]=d-sum(n for bl,n in ell.items() if bl&(1<<j))
   ell[0]=66-sum(ell.values());best=None
   for order in itertools.permutations(range(3)):
    for shift in (0,-1,1,-2,2):
     center=tuple(range(17+shift,20+shift));pos=tuple(center[order.index(j)] for j in range(3));u=c.profile_bound(36,pos,ell)
     if best is None or u<best[0]:best=(u,pos)
     if u<1:break
    if best[0]<1:break
   row=dict(degrees=ds,double=double,tau=tau,blocks=blocks,U=str(best[0]),positions=best[1],strict=best[0]<1);rows.append(row)
   if row['strict']:continue
   E=5*sum(ds)-3*35-2*(double>=0);pool=33-E//2;D=10+(396-sum(ds)-330)//pool;case=dict(degrees=ds,double=double,tau=tau,pool=pool,D=D,rows=0,failures=0,complete=True)
   for d4 in range(10,D+1):
    for newdouble in (-1,0,1,2):
     target=[1]*6
     if double>=0:target[pidx[oldpairs[double]]]=2
     if newdouble>=0:target[pidx[(newdouble,3)]]=2
     for bs in parts(tuple(target)):
      if sorted(bl&7 for bl in bs if (bl&7).bit_count()>=2)!=sorted(blocks):continue
      ell={}
      for bl in bs:ell[bl]=ell.get(bl,0)+1
      for j,d in enumerate(ds+(d4,)):ell[1<<j]=d-sum(n for bl,n in ell.items() if bl&(1<<j))
      ell[0]=66-sum(ell.values())
      if min(ell.values())<0:continue
      best=None
      orders=[]
      if double>=0:
       p,q=oldpairs[double];mid=[j for j in range(4) if j not in (p,q)];orders += [(p,*mid,q),(q,*mid,p)]
      if newdouble>=0:
       mid=[j for j in range(3) if j!=newdouble];orders += [(newdouble,*mid,3),(3,*mid,newdouble)]
      orders+=list(itertools.permutations(range(4)))
      for order in orders:
       for shift in (0,-1,1,-2,2,-3,3):
        center=tuple(range(16+shift,20+shift));pos=tuple(center[order.index(j)] for j in range(4));u=c.profile_bound(36,pos,ell)
        if best is None or u<best[0]:best=(u,pos)
        if u<1:break
       if best[0]<1:break
      four.append(dict(degrees=ds+(d4,),parent_double=double,parent_tau=tau,newdouble=newdouble,blocks=bs,U=str(best[0]),strict=best[0]<1,positions=best[1]));case['rows']+=1;case['failures']+=best[0]>=1
      if time.process_time()-start>55:stopped=True;case['complete']=False;break
     if stopped:break
    if stopped:break
   coverage.append(case);print(case,flush=True)
   if stopped:break
  if stopped:break
 if stopped:break
out=dict(three=rows,four=four,coverage=coverage,complete=not stopped,failures=[r for r in four if not r['strict']],cpu_seconds=time.process_time()-start)
(P/'MIN10_36.json').write_text(json.dumps(out,indent=2));print('three',len(rows),'four',len(four),'fails',len(out['failures']),'CPU',out['cpu_seconds'])
