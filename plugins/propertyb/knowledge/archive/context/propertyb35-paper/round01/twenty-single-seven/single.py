from pilot import *
start=time.time();out=[]
for d in range(8,25):
 ns={0:35-7-d+1,1:6,2:d-1,3:1}
 if min(ns.values())<0:continue
 en=SubsetEngine(20,2,ns);z=en.verify(en.solve());z.update(degree=d,strict=z['bound']<1);out.append(z);print(d,z['bound'])
(HERE/'SINGLE_UNIT.json').write_text(json.dumps(json_value(dict(cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
