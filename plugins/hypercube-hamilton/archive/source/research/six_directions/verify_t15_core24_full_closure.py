import json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
read=lambda p:json.loads((R/p).read_text(encoding='utf-8-sig'))
assert read('t15_core24_c0_B_verification.json')['status']=='PASS'
assert read('t15_core24_c0_B_verification.json')['residual_full_input_list_rebuilt']==2650725
c0=read('t15_core24_c0_residual.json');assert c0['total']==c0['positive']==2650725 and c0['unknown']==c0['negative']==0
assert read('t15_core24_c0_residual_verification.json')==dict(status='PASS',verified=2650725)
cert=R/'t15_core24_c0_residual.bin';assert cert.stat().st_size==2650725*56
assert (R/'t15_core24_c0_residual_failures.txt').stat().st_size==0
c2=read('t15_core24_c2_types_verification.json');assert c2['status']=='PASS' and c2['A_inputs']==62370 and c2['B_inputs']==945945 and c2['exceptional_B_inputs']==786 and c2['residual_full_inputs']==98045640
zero=set()
for line in (R/'t15_core24_c2_B_types.txt').read_text().splitlines():
 t=list(map(int,line.split()))
 if t[0]==0:zero.add(tuple(t[3:]))
b2={tuple(map(int,l.split())) for l in (R/'r4_joint_fourbridge_core24_B2.txt').read_text().splitlines()}
assert len(zero)==len(b2)==786 and zero==b2
joint=read('r4_joint_blocking_check.json');rows=[]
for c,A,B,total in [(2,62370,786,98045640),(4,51975,312,389188800),(6,13860,34,339292800),(8,1485,1,59875200)]:
 p=read(f'r4_joint_fourbridge_core24_c{c}.json');v=read(f'r4_joint_fourbridge_core24_c{c}_verification.json');assert p=={k:z for k,z in v.items() if k!='status'} and v['status']=='PASS'
 assert p['c']==c and p['A']==A and p['B']==B and p['inputs']==total and p['residual']==0
 assert (R/f'r4_joint_fourbridge_core24_c{c}_residual_inputs.bin').stat().st_size==0
 if c>=4:
  j=next(r for r in joint['reports'] if r['core']==24 and r['c']==c)
  expected={tuple(z for e in F for z in e) for F in j['matchings']}
  actual={tuple(map(int,l.split())) for l in (R/f'r4_joint_fourbridge_core24_B{c}.txt').read_text().splitlines()}
  assert actual==expected and len(actual)==B
 rows.append(v)
for c in (10,12):
 j=next(r for r in joint['reports'] if r['core']==24 and r['c']==c);assert not j['matchings']
prep=read('r4_parent_fourbridge_preparation.json');assert prep['status']=='PASS';tables=[r for r in prep['rows'] if r['core']==24];assert len(tables)==18
for row in tables:assert hashlib.sha256((R/row['file']).read_bytes()).hexdigest()==row['sha256']
review=read('R4_DOUBLE_BRIDGE_REVIEW.json');assert review['status']=='PASS'
p=(1,0,2,3,4)
def tr(v):return sum(((v>>j)&1)<<p[j] for j in range(5))
H={0,1,7,14,22,31};assert {tr(v) for v in H}=={0,2,7,13,21,31} and {tr(1),tr(7)}=={2,7}
for a in range(32):
 for j in range(5):assert (tr(a)^tr(a^(1<<j))).bit_count()==1
out=dict(status='PASS',scope='Core24 complete finite manifest; fresh overall semantic review pending',original_holes=sorted(H),original_omitted=[1,7],coordinate_destination_map=p,normalized_holes=[0,2,7,13,21,31],normalized_omitted=[2,7],c0_positive_certificates=2650725,c0_certificate_size=cert.stat().st_size,c0_certificate_sha256=hashlib.sha256(cert.read_bytes()).hexdigest(),c2_spectrum=c2,four_bridge_checks=rows,four_bridge_total_inputs=sum(r['inputs'] for r in rows),four_bridge_tables_checked=18,large_crossing_import='R4_DOUBLE_BRIDGE_REVIEW.json',large_crossing_import_acceptance=review.get('acceptance_status'),full_T15_proved=False,full_eight_hole_layer_proved=False)
(R/'T15_CORE24_FULL_CLOSURE_VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
