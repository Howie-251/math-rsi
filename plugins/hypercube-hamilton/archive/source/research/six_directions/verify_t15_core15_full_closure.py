import json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
read=lambda p:json.loads((R/p).read_text(encoding='utf-8-sig'))
small=read('t15_r3_small_verification.json');assert small['status']=='PASS'
rows=[r for r in small['B_results'] if r['core']==15];assert len(rows)==2
assert {(r['c'],r['zero_B_partial_count']) for r in rows}=={(1,12),(3,1)}
assert all(r['independent_B_spectrum_matches'] for r in rows)
assert next(r for r in rows if r['c']==3)['nonzero_c3_has_two_good_pairings_on_one_bridge']
reports=[]
for c,prefix,expected_cases in [(1,'fast',12),(3,'hybrid',1)]:
 expected=[]
 for line in (R/f't15_r3_small_core15_c{c}_B_exceptions.txt').read_text().splitlines():
  t=line.split();i=t.index('F');expected.append(tuple(map(int,t[1:i]+t[i+1:])))
 actual=[tuple(map(int,s.split())) for s in (R/f't15_core15_c{c}_B_inputs.txt').read_text().splitlines()]
 assert len(actual)==len(set(actual))==expected_cases and set(actual)==set(expected)
 for row in actual:
  ports=set(row[:c]);vertices=list(row[c:]);assert len(ports)==c and len(vertices)==13-c and len(set(vertices))==13-c and set(vertices)==set(range(16))-{0,7,1}-ports
 result=read(f't15_core15_c{c}_{prefix}.json');assert result['c']==c and result['total']==result['positive']==1621620 and result['unknown']==result['negative']==0
 verified=read(f't15_core15_c{c}_residual_verification.json');assert verified['status']=='PASS' and verified['c']==c and verified['records']==1621620
 cert=R/f't15_core15_c{c}_{prefix}.bin';assert cert.stat().st_size==1621620*56==verified['total_bytes']
 assert (R/f't15_core15_c{c}_{prefix}_failures.txt').stat().st_size==0
 reports.append(dict(c=c,exception_B_inputs=expected_cases,producer=result,independent_positive_verifier=verified,certificate_file=cert.name,certificate_sha256=hashlib.sha256(cert.read_bytes()).hexdigest()))
table=read('t15_core15_table_verification.json');assert table['status']=='PASS' and table['negative_count']==1 and table['bridge']==10 and table['B_omitted']==1
p=(0,1,2,4,3)
def tr(v):return sum(((v>>j)&1)<<p[j] for j in range(5))
original_holes={0,1,2,13,22,31};assert {tr(v) for v in original_holes}=={0,1,2,14,21,31};assert {tr(1),tr(2)}=={1,2}
for a in range(32):
 for j in range(5):assert (tr(a)^tr(a^(1<<j))).bit_count()==1
out=dict(status='PASS',scope='Core15 complete finite input manifest; full semantic proof awaits fresh independent review',original_holes=sorted(original_holes),original_omitted=[1,2],coordinate_destination_map=p,normalized_holes=[0,1,2,14,21,31],normalized_omitted=[1,2],complete_positive_residual_inputs=3243240,residual_reports=reports,c3_independent_B_inputs=1621620,c3_zero_B_partial_inputs=1,bridge_table=table,large_crossing_method='At most one forbidden output; choose the artificial boundary matching equal to it',full_T15_proved=False,full_eight_hole_layer_proved=False)
(R/'T15_CORE15_FULL_CLOSURE_VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
