exec(open(__file__.replace('two_arms35_four.py','four_repair.py')).read().split('start=time.process_time()')[0])
exec(open(__file__.replace('two_arms35_four.py','repair35_finalquota.py')).read().split('start=time.process_time()')[0])
start=time.process_time();rows=[];coverage=[];stopped=False
for parent in json.loads((P/'TWO_ARMS35_JOINT.json').read_text())['failures']:
 ds=tuple(parent['degrees']);lam=parent['lam_yz'];tau=parent['tau'];known=([7] if tau else [])+[3]*(1-tau)+[5]*(1-tau)+[6]*(lam-tau)
 E=5*sum(ds)-102-2*(lam-1);pool=32-E//3;D=10+(396-sum(ds)-320)//pool;case=dict(degrees=ds,lam_yz=lam,tau=tau,pool=pool,D=D,rows=0,failures=0,complete=True)
 for d4 in range(10,D+1):
  for extras in itertools.product(range(3),repeat=3):
   if sum(extras)>2:continue
   target=[1]*6;target[pidx[(1,2)]]=lam
   for j,ex in enumerate(extras):target[pidx[(j,3)]]=1+ex
   for blocks in parts(tuple(target)):
    if sorted(b&7 for b in blocks if (b&7).bit_count()>=2)!=sorted(known):continue
    ell={}
    for bl in blocks:ell[bl]=ell.get(bl,0)+1
    for j,d in enumerate(ds+(d4,)):ell[1<<j]=d-sum(n for b,n in ell.items() if b&(1<<j))
    ell[0]=66-sum(ell.values())
    if min(ell.values())<0:continue
    best=None
    orders=[(1,0,3,2),(2,0,3,1)]+list(itertools.permutations(range(4)))
    for order in orders:
     for shift in (0,-1,1,-2,2,-3,3):
      center=tuple(range(15+shift,19+shift));pos=tuple(center[order.index(j)] for j in range(4));u=c.profile_bound(35,pos,ell)
      if best is None or u<best[0]:best=(u,pos)
      if u<1:break
     if best[0]<1:break
    row=dict(degrees=ds+(d4,),parent_lam=lam,parent_tau=tau,newextras=extras,blocks=blocks,U=str(best[0]),positions=best[1],strict=best[0]<1);rows.append(row);case['rows']+=1;case['failures']+=best[0]>=1
    if not row['strict']:print('FAIL',row,flush=True)
    if time.process_time()-start>25:stopped=True;case['complete']=False;break
   if stopped:break
  if stopped:break
 coverage.append(case);print(case,flush=True)
 if stopped:break
out=dict(rows=rows,coverage=coverage,complete=not stopped,failures=[r for r in rows if not r['strict']],cpu_seconds=time.process_time()-start)
(P/'TWO_ARMS35_FOUR.json').write_text(json.dumps(out,indent=2));print('rows',len(rows),'fails',len(out['failures']),'CPU',out['cpu_seconds'])
