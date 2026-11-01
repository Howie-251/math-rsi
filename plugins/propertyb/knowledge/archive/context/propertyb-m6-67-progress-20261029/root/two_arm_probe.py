from pathlib import Path
import importlib.util,itertools,json,time
P=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('d',P.parent/'small31_33/diagnose.py');d=importlib.util.module_from_spec(s);s.loader.exec_module(d)
c=d.c
start=time.process_time();rows=[];cases=[]
for v,a,e in ((34,9,12),(34,9,13),(34,10,12),(34,10,13),(35,9,12)):
 n=2*(v-1)-5*a;L=396-v*a;F=a+(L-(e-a))//(n-1)
 for f in range(e,F+1):
  fails=[]
  for lam in range(1,min(e,f)+1):
   for tau in (0,1):
    ell={7:tau,3:1-tau,5:1-tau,6:lam-tau,1:a-2+tau,2:e-1-lam+tau,4:f-1-lam+tau}
    ell[0]=66-sum(ell.values())
    if min(ell.values())<0:continue
    best=None
    menu=[(16,17,18),(17,18,19),(19,20,21),(12,13,14),(11,12,19),(11,13,20),(10,11,19),(15,16,19),(10,18,19),(10,16,20)]
    for pos in menu:
     for order in itertools.permutations(range(3)):
      ps=tuple(pos[order.index(j)] for j in range(3));u=c.profile_bound(v,ps,ell)
      if best is None or u<best[0]:best=(u,ps)
      if u<1:break
     if best[0]<1:break
    row=dict(v=v,d=a,e=e,f=f,lam=lam,tau=tau,ell=ell,U=str(best[0]),pos=best[1],strict=best[0]<1)
    rows.append(row)
    if not row['strict']:fails.append({k:row[k] for k in ('lam','tau','U')})
  cases.append(dict(v=v,d=a,e=e,f=f,fails=fails));print(cases[-1],flush=True)
out=dict(cases=cases,rows=rows,cpu_seconds=time.process_time()-start)
(P/'TWO_ARM_PROBE.json').write_text(json.dumps(out,indent=2));print('CPU',out['cpu_seconds'])
