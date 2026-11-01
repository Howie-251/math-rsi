from probe import *
start=time.time();out=[]
for dy in (5,6,7):
 for dz in range(dy,9):
  for lam in (range(1,2) if dy==5 else range(1,dy+1)):
   for t in (0,1):
    r=best(21,(5,dy,dz),(1,1,lam),t)
    if r:
     out.append(r);print(dy,dz,lam,t,r['bound'],flush=True)
Path(__file__).with_name('TWENTYONE_FIVE_LOW.json').write_text(json.dumps(json_value(dict(cases=out,seconds=time.time()-start)),indent=2))
print('PASS',sum(r['bound']<1 for r in out),'/',len(out),'seconds',time.time()-start)
