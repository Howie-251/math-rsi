from repair import *
def profile_for(ds,triple):
 if triple:return{0:M-sum(ds)+2,1:ds[0]-1,2:ds[1]-1,4:ds[2]-1,7:1}
 return{0:M-sum(ds)+3,1:ds[0]-2,2:ds[1]-2,4:ds[2]-2,3:1,5:1,6:1}
if __name__=='__main__':
 start=time.process_time();cal=AvoidCalculator(K,M);base=json.loads((P/'PROFILE.json').read_text());rows=[r|dict(deduction='full_pool')for r in base['rows']if r['strict']];branches=[];more_two=[]
 for v in range(135,140):
  for degree in range(src.CEIL(v-1,8),BUDGET//v+1):
   ell={0:M-degree,1:degree};pos=(v//2,);U=cal.bound(v,pos,ell)
   rows.append(asrow(v,'one',ell,pos,U,degrees=[degree],deduction='max_R'))
 # Every nonstrict originalone case selects an actual minimumunitpartner.
 for r in base['failures']:
  if r['kind']!='one':continue
  v=r['v'];degree=r['degrees'][0];n=2*(v-1)-8*degree;upper=degree+(BUDGET-v*degree)//n
  branches.append(dict(v=v,minimum=degree,stage='one_to_two',n=n,partner_upper=upper))
  for e in range(degree,upper+1):
   ell={0:M-degree-e+1,1:degree-1,2:e-1,3:1};pos=(v//2,v//2+1);U=cal.bound(v,pos,ell)
   r2=asrow(v,'two',ell,pos,U,degrees=[degree,e],deduction='max_R')
   if U<1:rows.append(r2)
   else:more_two.append(r2)
 # Only failedtwo types need third; two previous repairs failedall73.
 parents=[r for r in base['failures']if r['kind']=='two']+more_two
 for r in parents:
  v=r['v'];degree,e=r['degrees'];n=2*(v-1)-8*degree;t=n-1-(8*e-(v-1));assert t>0
  excess=BUDGET-v*degree-n*(e-degree);fmax=e+excess//t
  branches.append(dict(v=v,minimum=degree,partner=e,stage='two_to_three',n=n,common_unit_lower=t,budget=excess,fmax=fmax))
  for f in range(e,fmax+1):
   for triple in(0,1):
    ds=(degree,e,f);ell=profile_for(ds,triple);best=None
    for pos in((v//2-1,v//2,v//2+1),(v//2-2,v//2-1,v//2)):
     U=cal.bound(v,pos,ell)
     if best is None or U<best[0]:best=(U,pos)
     if U<1:break
    rows.append(asrow(v,'conditional_three',ell,best[1],best[0],degrees=ds,triple=triple,deduction='max_R'))
  for func in(cal.context,cal.endpoint,cal.weight):func.cache_clear()
 failures=[r for r in rows if not r['strict']];out=dict(status='complete candidate'if not failures else'NOT COMPLETE',k=K,M=M,degree_budget=BUDGET,vertex_domain=[57,195],rows=rows,branches=branches,failures=failures,cpu_seconds=time.process_time()-start)
 (P/'CANDIDATE.json').write_text(json.dumps(out,indent=2));print('profiles',len(rows),'failures',len(failures),'CPU',out['cpu_seconds'])
 for r in failures[:30]:print(r['v'],r.get('degrees'),r.get('triple'),r['U'])
