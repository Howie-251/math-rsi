from pathlib import Path
import importlib.util,itertools,json,time
P=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('d',P.parent/'small31_33/diagnose.py');d=importlib.util.module_from_spec(s);s.loader.exec_module(d)
c=d.c
start=time.process_time();rows=[]
for v,a in ((34,9),(34,10),(35,9)):
 for b in range(a,15):
  for lam in (1,2,3,4):
   ell=d.two(v,a,b,lam);best=None
   for ps in itertools.permutations(range(v//2-5,v//2+7),2):
    u=c.profile_bound(v,ps,ell)
    if best is None or u<best[0]:best=(u,ps)
    if u<1:break
   rows.append(dict(v=v,d=a,e=b,lam=lam,U=str(best[0]),pos=best[1],strict=best[0]<1))
print(json.dumps(rows,indent=2));print('CPU',time.process_time()-start)
(P/'PAIRS_PROBE.json').write_text(json.dumps(rows,indent=2))
