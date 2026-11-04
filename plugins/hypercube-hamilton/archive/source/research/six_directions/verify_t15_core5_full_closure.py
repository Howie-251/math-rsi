"""Package-level input coverage and positive-certificate checks for core5."""
import json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
def read(p):return json.loads((R/p).read_text(encoding='utf-8-sig'))
small=read('t15_r3_small_verification.json');assert small['status']=='PASS'
rows=[r for r in small['B_results'] if r['core']==5]
assert len(rows)==2
assert {(r['c'],r['zero_B_partial_count']) for r in rows}=={(1,5),(3,0)}
assert all(r['independent_B_spectrum_matches'] for r in rows)
assert next(r for r in rows if r['c']==3)['nonzero_c3_has_two_good_pairings_on_one_bridge']
expected=[]
for line in (R/'t15_r3_small_core5_c1_B_exceptions.txt').read_text().splitlines():
 t=line.split();i=t.index('F');expected.append(tuple(map(int,t[1:i]+t[i+1:])))
actual=[tuple(map(int,s.split())) for s in (R/'t15_core5_c1_B_inputs.txt').read_text().splitlines()]
assert len(actual)==len(set(actual))==5 and set(actual)==set(expected)
base=set(range(16))-{0,7,1}
for row in actual:
 port=row[0];vertices=list(row[1:]);assert len(vertices)==12 and len(set(vertices))==12 and set(vertices)==base-{port}
result=read('t15_core5_c1_residual.json');assert result['total']==result['positive']==675675 and result['unknown']==result['negative']==0
verified=read('t15_core5_c1_residual_verification.json');assert verified['status']=='PASS' and verified['records']==675675
cert=R/'t15_core5_c1_residual.bin';assert cert.stat().st_size==675675*56==verified['total_bytes']
assert (R/'t15_core5_c1_residual_failures.txt').stat().st_size==0
inverse=read('t15_core5_c5_inverse_verification.json');assert inverse['status']=='PASS' and inverse['negative_count']==2 and inverse['inverse_cases']==30 and inverse['max_bad_quotients']==1
out=dict(status='PASS',scope='Core5 complete finite input package; semantic proof in T15_CORE5_FULL_CLOSURE.md awaits fresh overall review',global_holes=[0,1,2,7,13,14],omitted=[1,2],c1_exception_B_inputs=5,c1_complete_residual_inputs=675675,c1_producer=result,c1_independent_positive_verifier=verified,c1_binary_sha256=hashlib.sha256(cert.read_bytes()).hexdigest(),c3_independent_B_inputs=1621620,c3_zero_B_inputs=0,c5_occupied_inverse_inputs=30,c5_max_negative_quotients=1,large_crossings_method='Elementary two-pairing exclusion; no three-pairing finite import',full_T15_proved=False,full_eight_hole_layer_proved=False)
(R/'T15_CORE5_FULL_CLOSURE_VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
