import json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
checks=['t15_core1_c0_B_verification.json','t15_core1_route_c0_residual_verification.json','t15_core1_c2_types_verification.json','t15_core1_c2_B_list_verification.json','t15_core1_joint_B_verification.json','t15_core1_five_avoided_inputs.json']
checks += [f't15_core1_joint_fourbridge_c{c}_verification.json' for c in (2,4,6,8)]
checks += [f't15_core1_joint_fourbridge_c{c}_residual_verification.json' for c in (4,6,8)]
for f in checks:assert json.loads((R/f).read_text())['status']=='PASS'
expected={2:(52390800,0),4:(261954000,1575),6:(279417600,6300),8:(59875200,2520)}
for c,(n,k) in expected.items():
 a=json.loads((R/f't15_core1_joint_fourbridge_c{c}.json').read_text());b=json.loads((R/f't15_core1_joint_fourbridge_c{c}_verification.json').read_text())
 assert a['inputs']==b['inputs']==n and a['residual']==b['residual']==k
 assert a['A']==b['A']=={2:62370,4:51975,6:13860,8:1485}[c]
 assert a['B']==b['B']=={2:420,4:210,6:28,8:1}[c]
 f=R/f't15_core1_joint_fourbridge_c{c}_residual_inputs.bin';assert f.stat().st_size==26*k
 if k:assert (R/f't15_core1_joint_fourbridge_c{c}_residual.bin').stat().st_size==56*k
assert json.loads((R/'t15_core1_c0_B_verification.json').read_text())['residual_full_input_list_rebuilt']==1091475
rows=json.loads((R/'t15_core1_five_avoided_inputs.json').read_text())['rows']
for t in rows:assert hashlib.sha256((R/t['file']).read_bytes()).hexdigest()==t['sha256']
files=set(checks+['verify_t15_core1_full_closure.py','T15_CORE1_FULL_CLOSURE.md','R4_DOUBLE_BRIDGE_BLOCKING.md','Q4_CORE_AND_A4_SPLIT.md','r4_boundary_blocking_3_5_1.json','r4_inverse_blockers_3_5_1_verification.json','verify_r4_inverse_blockers.py','q4_three_avoided_3_5_1.bin','t15_core1_route_negative.txt','t15_core1_joint_fourbridge_spectra.cpp','verify_t15_core1_joint_fourbridge.cpp','t15_core1_c2_types.cpp','verify_t15_core1_c2_types.cpp','verify_t15_core1_c0_B.py','verify_t15_core1_joint_B.py','verify_t15_core1_route_c0_residual.cpp','verify_t15_core1_joint_residual.cpp','t15_core1_route_c0_residual.cpp','t15_core1_route_c0_residual_inputs.bin','t15_core1_route_c0_residual.bin','t15_core1_c2_A_types.txt','t15_core1_c2_B_types.txt'])
files.update(t['file'] for t in rows)
for c in (2,4,6,8):
 files.update(f't15_core1_joint_fourbridge_c{c}'+suffix for suffix in ('.json','_residual_inputs.bin'))
for c in (4,6,8):files.add(f't15_core1_joint_fourbridge_c{c}_residual.bin')
for c in (2,4,6,8,10,12):files.add(f't15_core1_route_B{c}.txt')
hashes={f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in sorted(files)}
out={'status':'PASS','scope':'All finite obligations for full core1; fresh semantic audit pending; no dynamic global ledger is a proof dependency','core':1,'original_holes':[0,1,2,7,11,19],'omitted':[1,2],'fourbridge_verified_full_inputs':sum(n for n,k in expected.values()),'direct_positive_certificates':1091475+1575+6300+2520,'proof_input_hashes':hashes}
(R/'t15_core1_full_closure_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k!='proof_input_hashes'})
