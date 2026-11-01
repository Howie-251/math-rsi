from pathlib import Path
import importlib.util,time,json
P=Path(__file__).resolve().parent
def load(name,path):
 q=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(q);q.loader.exec_module(m);return m
pilot=load('pilot_top',P.parent/'pilot.py')
ns={0:5}
for i in range(6):ns[63^(1<<i)]=1;ns[1<<i]=3;ns[64|(1<<i)]=1
r=pilot.evaluate(21,ns,(9,10,11,12,13,14,1),True)
assert str(r['bound'])=='485/572' and r['strict']
(P/'FIXED_CERTIFICATE.json').write_text(json.dumps(pilot.json_value(r),indent=2)+'\n')
replay=load('independent_top_replay',P.parents[1]/'twentyone-delta5/replay.py')
st=time.process_time();v=replay.verify(json.loads((P/'FIXED_CERTIFICATE.json').read_text()));assert v==r['bound']
out={'status':'PASS','scope':'one forced actual seven-lock inventory; 35 original edge stubs,1190 ordered distinct edge-index pairs,21 positions; independently derived injection rows and nested quotas','bound':str(v),'strict':v<1,'cpu_seconds':time.process_time()-st,'degrees':[9]*6+[6],'positions':[9,10,11,12,13,14,1],'quota_losses':[str(c['loss']) for c in r['quotas']]}
(P/'REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
