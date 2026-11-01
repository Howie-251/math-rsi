from pathlib import Path
import sys
HERE=Path(__file__).parent;sys.path.insert(0,str(HERE.parent))
from pilot import *
HERE=Path(__file__).parent
start=time.time();out=[]
for a in (6,7,8):
 for b in range(a,36-a):
  cs=range(1,a+1) if b<=a+2 else (1,)
  for c in cs:
   ns=double(20,a,b,c)
   if min(ns.values())<0:continue
   z=best(20,ns,True);z.update(degrees=[a,b],codegree=c);out.append(z)
   print(a,b,c,z['bound'],z['positions'],flush=True)
(HERE/'PAIRS.json').write_text(json.dumps(json_value(dict(scope='M35 v20 exact double-lock diagnosis with all labelled positions',cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
print('elapsed',time.time()-start)
