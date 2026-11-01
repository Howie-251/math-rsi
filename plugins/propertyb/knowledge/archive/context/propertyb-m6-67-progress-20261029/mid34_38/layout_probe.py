exec(open(__file__.replace('layout_probe.py','adaptive_component.py')).read().split('for v in range(34,39):')[0])
for v,ds,blocks in [(38,(8,8,8),(3,5,6)),(37,(8,11,11),(3,5,6)),(38,(10,10,11),(3,5,6))]:
 bestrow=None;count=0
 for pos in itertools.combinations(range(v//2-5,v//2+6),3):
  for perm in sorted(set(itertools.permutations(ds))):
   u=bound(v,pos,ell_for(perm,blocks));count+=1
   if bestrow is None or u<F(bestrow['U']):bestrow=dict(v=v,degrees=ds,assigned=perm,blocks=blocks,positions=pos,U=str(u),strict=u<1)
  if bestrow['strict']:break
 rows.append(bestrow|dict(evaluations=count));print(rows[-1],flush=True)
result=dict(rows=rows,cpu_seconds=time.process_time()-start)
(P/'LAYOUT_PROBE.json').write_text(json.dumps(result,indent=2));print('CPU',result['cpu_seconds'])
