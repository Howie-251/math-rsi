"""Aggregate the exact core8 proof inputs; never treats search exhaustion as proof."""
from pathlib import Path
import json,hashlib,itertools,datetime
R=Path(__file__).resolve().parent
read=lambda p:json.loads((R/p).read_text(encoding='utf-8-sig'))
def digest(p):
 h=hashlib.sha256()
 with (R/p).open('rb') as f:
  for chunk in iter(lambda:f.read(8*1024*1024),b''):h.update(chunk)
 return 'sha256:'+h.hexdigest()
def norm(edges):return tuple(sorted(tuple(sorted(e)) for e in edges))
J=norm([(2,4),(5,6),(9,11),(10,13)]);S={3,8,12,14,15}
B=read('t15_core8_B_verification.json');assert len(B)==2
res=[]
for c in (1,3,5):
 lines=(R/f't15_core8_c{c}_B_inputs.txt').read_text().splitlines();n=int(lines[0]);rows=[tuple(map(int,s.split())) for s in lines[1:]];assert len(rows)==len(set(rows))==n=={1:22,3:10,5:1}[c]
 for row in rows:
  ports=set(row[:c]);vs=list(row[c:]);assert len(ports)==c and len(vs)==13-c
  assert len(vs)==len(set(vs)) and ports.isdisjoint(vs)
  assert ports|set(vs)==set(range(16))-{0,7,1}
 if c in (1,3):
  ex=[]
  for line in (R/f't15_core8_checked_core8_c{c}_B_exceptions.txt').read_text().splitlines():
   t=line.split();i=t.index('F');ex.append(tuple(map(int,t[1:i]+t[i+1:])))
  assert set(rows)==set(ex) and len(ex)==n
  row=next(b for b in B if b['c']==c);assert row['B_types']==read(f't15_r3_small_core8_c{c}.json')['B_types']
  assert row['total']==(135135 if c==1 else 1621620)
  assert row['B_types']['0']==(22 if c==1 else 60)
  if c==3:
   assert all(int(m)==0 or max((int(m)&7).bit_count(),(int(m)>>3).bit_count())>=2 for m in row['B_types'])
   actual={norm(zip(q[c::2],q[c+1::2])) for q in rows}
   assert actual=={norm(J+(e,)) for e in itertools.combinations(sorted(S),2)}
 else:
  assert norm(zip(rows[0][c::2],rows[0][c+1::2]))==J and set(rows[0][:c])==S
 p=read(f't15_core8_c{c}_residual.json');v=read(f't15_core8_c{c}_residual_verification.json')
 expected={1:2972970,3:16216200,5:16216200}[c]
 assert p['total']==p['positive']==expected and p['unknown']==p['negative']==0
 assert v['status']=='PASS' and v['records']==expected and v['total_bytes']==expected*56
 assert (R/f't15_core8_c{c}_residual_failures.txt').stat().st_size==0
 assert (R/f't15_core8_c{c}_residual.bin').stat().st_size==expected*56
 res.append(dict(c=c,B_exception_count=n,producer=p,independent_verifier=v))
block=read('t15_core8_blockers_verification.json');assert block['status']=='PASS'
assert {norm(f) for f in block['c5_common_bad']}=={J}
assert all(r['null_families']==0 for r in block['reports'] if r['c']>=7 or r['mode']=='internal')
geo=read('t15_analytic_geometry.json')['T15']['residual_orbits'][8]
assert geo['avoided']==[1,2] and geo['included']==[7,13,31]
def tr(v):return (v&28)|((v&1)<<1)|((v&2)>>1)
assert {tr(v) for v in {0,1,2,7,13,31}}=={0,1,2,7,14,31}
assert {tr(v) for v in {1,2}}=={1,2}
assert all((tr(v)^tr(v^(1<<j))).bit_count()==1 for v in range(32) for j in range(5))
prior=read('T15_BALANCED_BRIDGE_REVIEW.json')
imports=['Q4_CORE_AND_A4_SPLIT.md','q4_two_hole_3.bin','q4_two_hole_15.bin']+[p.name for p in R.glob('q4_balanced_two_avoided_*.bin')]
for p in imports:assert digest(p)==prior['audited_input_hashes'][p]
inputs=['T15_CORE8_FULL_CLOSURE.md','t15_analytic_geometry.json','T15_BALANCED_BRIDGE_REVIEW.md','T15_BALANCED_BRIDGE_REVIEW.json','T15_R3_SMALL_CROSSING_PROGRESS.md','t15_core8_residual.cpp','verify_t15_core8_residual.cpp','verify_t15_core8_B.cpp','verify_t15_core8_blockers.py','r3_boundary_blocking_3_1.json','r3_boundary_blocking_15_1.json','t15_core8_blockers_verification.json','t15_core8_B_verification.json','verify_t15_core8_full_closure.py']+imports
for c in (1,3,5):inputs += [f't15_core8_c{c}_B_inputs.txt',f't15_core8_c{c}_residual.bin',f't15_core8_c{c}_residual.json',f't15_core8_c{c}_residual_verification.json']
out=dict(status='PASS',scope='Complete candidate proof finite package for core8 only; fresh semantic audit required',generated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),original_holes=[0,1,2,7,13,31],normalized_holes=[0,1,2,7,14,31],omitted=[1,2],coordinate_permutation='swap global bits 0 and 1',positive_residuals=res,total_positive_residuals=35405370,total_certificate_bytes=1982700720,blockers=block,import_hashes_match=True,audited_input_hashes={p:digest(p) for p in inputs},full_T15_proved=False,full_eight_hole_layer_proved=False,P6_proved=False,independent_overall_review_pending=True)
(R/'T15_CORE8_FULL_CLOSURE_VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('audited_input_hashes','blockers','positive_residuals')}))
