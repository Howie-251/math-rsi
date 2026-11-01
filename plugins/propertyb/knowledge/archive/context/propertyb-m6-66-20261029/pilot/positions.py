exec(open(__file__.replace('positions.py','pilot.py')).read().split('rows=[]')[0])
base=json.loads((OUT/'baseline.json').read_text()); start=time.process_time(); rows=[];evals=0
# Complete all single-lock positions for baseline one-lock failures.
# For pair/triple failures: every degree order and sorted positions in center +/-3 (local only).
for r in base['failures']:
 if r['kind']=='zero':continue
 v=r['v'];s=len(r['degrees']); ctr=v//2
 slots=list(range(max(1,ctr-3),min(v,ctr+3)+1))
 positions=[(p,) for p in range(1,v+1)] if s==1 else itertools.combinations(slots,s)
 best=None;bp=None;bd=None;tested=0
 for pos in positions:
  for ds in set(itertools.permutations(r['degrees'])):
   if s==1:ell={0:65-ds[0],1:ds[0]}
   elif s==2:ell={0:66-sum(ds),1:ds[0]-1,2:ds[1]-1,3:1}
   elif r['tri']:ell={0:67-sum(ds),1:ds[0]-1,2:ds[1]-1,4:ds[2]-1,7:1}
   else:ell={0:68-sum(ds),1:ds[0]-2,2:ds[1]-2,4:ds[2]-2,3:1,5:1,6:1}
   u=c.profile_bound(v,pos,ell);evals+=1;tested+=1
   if best is None or u<best:best,bp,bd=u,pos,ds
  if time.process_time()-start>100:break
 rows.append(dict(v=v,kind=r['kind'],degrees=r['degrees'],tri=r['tri'],best_U=str(best),best_approx=float(best),positions=bp,ordered_degrees=bd,pass_strict=best<1,evaluations=tested))
 (OUT/'positions.json').write_text(json.dumps(dict(scope='all single positions; all degree orders with positions in center +/-3 for pairs/triples; failures only',cpu_seconds=time.process_time()-start,evaluations=evals,complete=time.process_time()-start<=100,rows=rows),indent=2))
 if time.process_time()-start>100:break
print(json.dumps(dict(cpu=time.process_time()-start,evaluations=evals,profiles=len(rows),rescued=sum(r['pass_strict'] for r in rows),remaining=sum(not r['pass_strict'] for r in rows)),indent=2))
for r in rows:
 if r['pass_strict']:print(r)
