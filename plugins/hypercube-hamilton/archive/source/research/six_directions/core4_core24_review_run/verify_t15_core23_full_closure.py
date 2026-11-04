"""Complete finite-input package checks for candidate T15 core23 closure."""
import json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
read=lambda p:json.loads((R/p).read_text(encoding='utf-8-sig'))
small=read('t15_r3_small_verification.json');assert small['status']=='PASS'
rows=[r for r in small['B_results'] if r['core']==23];assert len(rows)==2
assert {(r['c'],r['zero_B_partial_count']) for r in rows}=={(1,20),(3,0)}
assert all(r['independent_B_spectrum_matches'] for r in rows)
assert next(r for r in rows if r['c']==3)['nonzero_c3_has_two_good_pairings_on_one_bridge']
expected=[]
for line in (R/'t15_r3_small_core23_c1_B_exceptions.txt').read_text().splitlines():
 t=line.split();i=t.index('F');expected.append(tuple(map(int,t[1:i]+t[i+1:])))
actual=[tuple(map(int,s.split())) for s in (R/'t15_core23_c1_B_inputs.txt').read_text().splitlines()]
assert len(actual)==len(set(actual))==20 and set(actual)==set(expected)
for row in actual:
 port=row[0];vertices=list(row[1:]);assert len(vertices)==12 and len(set(vertices))==12 and set(vertices)==set(range(16))-{0,7,8,port}
result=read('t15_core23_c1_residual.json');assert result['total']==result['positive']==2702700 and result['unknown']==result['negative']==0
verified=read('t15_core23_c1_residual_verification.json');assert verified['status']=='PASS' and verified['records']==2702700
cert=R/'t15_core23_c1_residual.bin';assert cert.stat().st_size==2702700*56==verified['total_bytes']
assert (R/'t15_core23_c1_residual_failures.txt').stat().st_size==0
blockers=read('t15_core23_blockers_verification.json');assert blockers['status']=='PASS' and blockers['total_explicit_blockers_checked']==2644 and blockers['c5_common_null_count']==0
p=(4,1,0,2,3)
def tr(v):return sum(((v>>j)&1)<<p[j] for j in range(5))
original_holes={0,1,7,14,22,26};assert {tr(v) for v in original_holes}=={0,7,11,14,16,19};assert {tr(1),tr(7)}=={16,19}
for a in range(32):
 for j in range(5):assert (tr(a)^tr(a^(1<<j))).bit_count()==1
out=dict(status='PASS',scope='Core23 complete finite input package; full semantic proof awaits fresh review',original_holes=sorted(original_holes),original_omitted=[1,7],coordinate_destination_map=p,normalized_holes=[0,7,11,14,16,19],normalized_omitted=[16,19],c1_exception_B_inputs=20,c1_complete_residual_inputs=2702700,c1_producer=result,c1_independent_positive_verifier=verified,c1_binary_sha256=hashlib.sha256(cert.read_bytes()).hexdigest(),c3_independent_B_inputs=1621620,c3_zero_B_inputs=0,blocker_verification=blockers,full_T15_proved=False,full_eight_hole_layer_proved=False)
(R/'T15_CORE23_FULL_CLOSURE_VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='blocker_verification'}))
