from pathlib import Path
import importlib.util,time,json
P=Path(__file__).resolve().parent
q=importlib.util.spec_from_file_location('pilot',P.parent/'pilot.py');m=importlib.util.module_from_spec(q);q.loader.exec_module(m)
# bits0..5 Q; bit6 center x. Six top five-traces; each q has
# one actual xq edge, three singleton edges; five emptyQ (avoidx).
ns={0:5}
for i in range(6):ns[(63^(1<<i))]=1;ns[1<<i]=3;ns[(1<<i)|64]=1
assert sum(ns.values())==35
positions=[(8,9,10,11,12,13,1),(7,8,9,10,11,12,13),(9,10,11,12,13,14,1),(1,2,3,4,5,6,11)]
st=time.process_time();out=[]
for pos in positions:
 z=m.evaluate(21,ns,pos,False);out.append({'positions':pos,'bound':str(z['bound']),'strict':z['strict']});print(out[-1],flush=True)
(P/'LOCK_PILOT.json').write_text(json.dumps({'scope':'one forced actual7lock inventory; four fixed layouts, no domain enumeration','cpu_seconds':time.process_time()-st,'rows':out},indent=2)+'\n')
