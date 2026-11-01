"""Complete necessary triple domain for v20, M35, minimum degree5."""
from pilot import *

def main():
 out=[];start=time.time()
 for a in range(5,9):
  for b in range(a,10):
   if a+18*b>170:continue
   for ax,az in ((1,1),(1,2),(2,1)):
    for ayz in range(1,a+1):
     for t in range(min(ax,az,ayz)+1):
      ns=triple(20,[5,a,b],(ax,az,ayz),t)
      if min(ns.values())<0:continue
      # Actual degree-five center has only one unit of global pair excess.
      z=best(20,ns);z.update(degrees=[5,a,b],codegrees=[ax,az,ayz],triple=t)
      out.append(z)
 print('profiles',len(out),'strict',sum(z['strict'] for z in out),'max',max(z['bound'] for z in out),'seconds',time.time()-start)
 (HERE/'TWENTY_DELTA5.json').write_text(json.dumps(json_value(dict(scope=__doc__,cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
 for r in out:
  if not r['strict']:print(r['degrees'],r['codegrees'],r['triple'],r['bound'],flush=True)
if __name__=='__main__':main()
