import json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
rows=json.loads((R/'t15_r3_small_B_independent.json').read_text(encoding='utf-8-sig'))
result=[]
for row in rows:
 k,c=row['core'],row['c'];p=json.loads((R/f't15_r3_small_core{k}_c{c}.json').read_text(encoding='utf-8-sig'))
 assert row['B_types']==p['B_types'],(k,c)
 assert row['total']==p['B_bijection_count']
 bad=row['B_types'].get('0',0)
 if c==3:
  assert all(int(m)==0 or max((int(m)&7).bit_count(),(int(m)>>3).bit_count())>=2 for m in row['B_types'])
 ex=(R/f't15_r3_small_core{k}_c{c}_B_exceptions.txt').read_text().splitlines()
 assert len(ex)*(1 if c==1 else 6)==bad
 result.append(dict(core=k,c=c,independent_B_spectrum_matches=True,B_bijection_count=row['total'],zero_B_partial_count=len(ex),zero_B_bijection_count=bad,nonzero_c3_has_two_good_pairings_on_one_bridge=(True if c==3 else None)))
producer=[]
for line in (R/'t15_r3_small_core0_c1_B_inputs.txt').read_text().splitlines():
 t=list(map(int,line.split()));producer.append((t[0],tuple(tuple(t[j:j+2]) for j in range(1,13,2))))
independent=[]
for line in (R/'t15_r3_small_core0_c1_B_exceptions.txt').read_text().splitlines():
 t=line.split();fi=t.index('F');v=list(map(int,t[fi+1:]));independent.append((int(t[1]),tuple(tuple(v[j:j+2]) for j in range(0,12,2))))
assert set(producer)==set(independent) and len(producer)==6
cert=R/'t15_r3_small_core0_c1_residual.bin'
checks=json.loads((R/'t15_r3_small_core0_c1_residual_verification.json').read_text(encoding='utf-8-sig'))
assert checks['status']=='PASS' and checks['records']==810810 and cert.stat().st_size==45405360
out=dict(status='PASS',scope='Independent B graph-compression kernels for c1/c3 on seven profiles; complete Q5 positive residual verification for core0 c1',B_results=result,core0_c1_exception_inputs_match=True,core0_c1_certificates=checks,core0_c1_certificate_sha256=hashlib.sha256(cert.read_bytes()).hexdigest(),full_T15_proved=False)
(R/'t15_r3_small_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
