"""Fresh core23 audit driver: check imports, normalized geometry and rerun outputs.
The two compiled verifiers are separately reviewed source; assertions enabled.
"""
from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parent
read=lambda p:json.loads((R/p).read_text(encoding='utf-8-sig'))
sha=lambda p:'sha256:'+hashlib.sha256((R/p).read_bytes()).hexdigest()
prior=read('T15_BALANCED_BRIDGE_REVIEW.json')
imports=['Q4_CORE_AND_A4_SPLIT.md','q4_two_hole_3.bin','q4_two_hole_15.bin']+[p.name for p in R.glob('q4_balanced_two_avoided_*.bin')]
assert len(imports)==16
for p in imports: assert sha(p)==prior['audited_input_hashes'][p],p
P=[4,1,0,2,3]
def tr(v):return sum(((v>>j)&1)<<P[j] for j in range(5))
assert len({tr(v) for v in range(32)})==32
assert all((tr(v)^tr(v^(1<<j))).bit_count()==1 for v in range(32) for j in range(5))
holes={0,1,7,14,22,26};normalized={tr(v) for v in holes}
assert normalized=={0,7,11,14,16,19} and {tr(1),tr(7)}=={16,19}
assert {v//2 for v in normalized if v%2}=={9,3,5}
assert {v//2 for v in normalized if v%2==0}=={0,7,8}
rows=read('T15_CORE23_REVIEW_small.json');assert len(rows)==2
for row in rows:
 assert row['core']==23
 prod=read('t15_r3_small_core23_c%d.json'%row['c'])
 assert row['B_types']==prod['B_types']
 assert sum(row['B_types'].values())==row['total']==(135135 if row['c']==1 else 1621620)
 if row['c']==3:
  assert row['B_types'].get('0',0)==0
  assert all(max((int(k)&7).bit_count(),(int(k)>>3).bit_count())>=2 for k,n in row['B_types'].items() if n)
 else:assert row['B_types'].get('0')==20
small_ex=[]
for line in (R/'T15_CORE23_REVIEW_core23_c1_B_exceptions.txt').read_text().splitlines():
 t=line.split();i=t.index('F');small_ex.append(tuple(map(int,t[1:i]+t[i+1:])))
req=[tuple(map(int,s.split())) for s in (R/'t15_core23_c1_B_inputs.txt').read_text().splitlines()]
assert len(req)==len(set(req))==len(small_ex)==20 and set(req)==set(small_ex)
for row in req:
 p,*v=row
 assert p in set(range(16))-{0,7,8}
 assert len(v)==12 and len(set(v))==12 and set(v)==set(range(16))-{0,7,8,p}
cert=read('T15_CORE23_REVIEW_residual.json')
assert cert['records']==2702700 and cert['record_bytes']==56 and cert['total_bytes']==151351200
assert (R/'t15_core23_c1_residual.bin').stat().st_size==151351200
assert sha('t15_core23_c1_residual.bin')=='sha256:2f35c5876f7e8f30493353f5bcef742cabea1d075068d39fc38442efed0d4eed'
block=read('T15_CORE23_REVIEW_blockers.json')
assert block['total_explicit_blockers_checked']==2644 and block['c5_common_null_count']==0
assert sum(r['inverse_families'] for r in block['reports'])==2646
assert read('T15_CORE23_FULL_CLOSURE_VERIFICATION.json')['c1_binary_sha256']==sha('t15_core23_c1_residual.bin')[7:]
inputs=['T15_CORE23_FULL_CLOSURE.md','T15_CORE23_FULL_CLOSURE_VERIFICATION.json','T15_BALANCED_BRIDGE_REVIEW.md','T15_BALANCED_BRIDGE_REVIEW.json','T15_R3_SMALL_CROSSING_PROGRESS.md','verify_t15_r3_small_B.cpp','verify_t15_core23_c1_residual.cpp','verify_t15_core23_blockers.py','r3_boundary_blocking_3_8.json','t15_r3_c5_negative_kernels.json','t15_core23_c1_B_inputs.txt','t15_core23_c1_residual.bin','t15_r3_small_core23_c1.json','t15_r3_small_core23_c3.json','T15_CORE23_REVIEW_small.cpp','T15_CORE23_REVIEW_independent_check.py']+imports
out=dict(status='PASS',generated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),audited_input_hashes={p:sha(p) for p in inputs},import_hashes_match=True,geometry_verified=True,B_spectra=rows,c1_exceptions_exact=True,c1_certificates=cert,inverse_families=2646,explicit_blockers=2644,c5_common_null=0,commands=['g++ -O3 -std=c++17 T15_CORE23_REVIEW_small.cpp -o T15_CORE23_REVIEW_small.exe','g++ -O3 -std=c++17 verify_t15_core23_c1_residual.cpp -o T15_CORE23_REVIEW_residual.exe','./T15_CORE23_REVIEW_small.exe','./T15_CORE23_REVIEW_residual.exe t15_core23_c1_B_inputs.txt t15_core23_c1_residual.bin','verify_t15_core23_blockers.py executed with output path changed only','python T15_CORE23_REVIEW_independent_check.py'],base_N14_and_balanced_recomputed=False,producer_search_recomputed=False,full_T15_proved=False,full_eight_holes_proved=False,P6_proved=False)
(R/'T15_CORE23_REVIEW_independent_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('audited_input_hashes','B_spectra','commands')}))
