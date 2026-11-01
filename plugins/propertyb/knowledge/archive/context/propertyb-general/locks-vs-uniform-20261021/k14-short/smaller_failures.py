"""Supplementary concrete e witnesses, not a completeness argument."""
import time,json
from screen import *
t=time.process_time();out=[]
for m,v,d in [(19647,876,134),(19605,1013,155)]:
 c=FastExact(14,m);tests=[]
 for e in sorted({d,d+1,d+10,2*d,3*d,4*d,8*d,16*d,32*d,64*d}):
  if e>m-d+1:continue
  z=c.two(v,d,e);tests.append({'e':e,'two_z':z,'gap':S-z})
 scalar=FixedCertificate(14,m)
 bad=next(x for x in tests if x['two_z']>=S)
 assert scalar.two(v,d,bad['e'])==bad['two_z']
 out.append({'M':m,'v':v,'d':d,'tests':tests,'smaller_failure_scalar_replayed':bad})
(OUT/'SMALLER_FAILURES.json').write_text(json.dumps({'rows':out,'cpu_seconds':time.process_time()-t},indent=2))
