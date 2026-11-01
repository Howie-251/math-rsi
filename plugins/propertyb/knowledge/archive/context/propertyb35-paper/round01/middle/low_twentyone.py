from pilot import *
start=time.time();out=[]
for a in range(5,9):
 for b in range(a,9):
  if a+19*b>170:continue
  for yz in range(1,a+1):
   for t in range(2):
    ns=triple(21,[5,a,b],(1,1,yz),t)
    if min(ns.values())<0:continue
    z=best(21,ns)
    if not z['strict']:
     for startpos in range(7,13):
      for pos in permutations(range(startpos,startpos+3)):
       zz=evaluate(21,ns,pos)
       if zz['bound']<z['bound']:z=zz
       if z['strict']:break
      if z['strict']:break
    z=evaluate(21,ns,z['positions'],True);z.update(degrees=[5,a,b],codegrees=[1,1,yz],triple=t)
    out.append(z)
(HERE/'TWENTYONE_DELTA5.json').write_text(json.dumps(json_value(dict(scope='Complete necessary x degree5 plus two minimal outside degrees for M35 v21',cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
print('cases',len(out),'strict',sum(z['strict'] for z in out),'max',max(z['bound'] for z in out),'seconds',time.time()-start)
for r in out:
 if not r['strict']:print(r['degrees'],r['codegrees'],r['triple'],r['bound'],r['positions'])
