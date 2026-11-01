src=open(__file__.replace('pairs_finalquota.py','adaptive_component.py')).read().split('for v in range(34,39):')[0]
src=src.replace('u=5 if t==1 else max(6,5*alpha)','u=5 if t==1 else max(6,5*alpha)\n   if t>=2 and e<comb(t,2)-t//2:u=max(u,11)')
exec(src)
A=json.loads((P/'ADAPTIVE_COMPONENT.json').read_text());rows=[]
for b in A['branches']:
 if b['v'] not in (34,35) or b['status']!='pool_gap':continue
 v=b['v'];ds=(b['d'],b['e']);ell=ell_for(ds,[3]);ans=None;count=0
 for pos in itertools.permutations(range(v//2-7,v//2+9),2):
  u=bound(v,pos,ell);count+=1
  if ans is None or u<F(ans['U']):ans=dict(v=v,degrees=ds,positions=pos,U=str(u),strict=u<1,quotas=[quota(d,v-1) for d in ds])
  if u<1:break
 rows.append(ans|dict(evaluations=count));print(rows[-1],flush=True)
out=dict(rows=rows,failures=[r for r in rows if not r['strict']],cpu_seconds=time.process_time()-start)
(P/'PAIRS_FINALQUOTA.json').write_text(json.dumps(out,indent=2));print('CPU',out['cpu_seconds'])
