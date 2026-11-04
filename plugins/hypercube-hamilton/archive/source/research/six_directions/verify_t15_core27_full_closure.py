"""Aggregate the exact core27 proof inputs; never treats search exhaustion as proof."""
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
J=None;S=None
B=read('t15_core27_B_verification.json');assert len(B)==2
res=[]
for c in (1,3,5):
 lines=(R/f't15_core27_c{c}_B_inputs.txt').read_text().splitlines();n=int(lines[0]);rows=[tuple(map(int,s.split())) for s in lines[1:]];assert len(rows)==len(set(rows))==n=={1:82,3:24,5:2}[c]
 for row in rows:
  ports=set(row[:c]);vs=list(row[c:]);assert len(ports)==c and len(vs)==13-c
  assert len(vs)==len(set(vs)) and ports.isdisjoint(vs)
  assert ports|set(vs)==set(range(16))-{0,7,8}
 if c in (1,3):
  ex=[]
  for line in (R/f't15_core27_checked_core27_c{c}_B_exceptions.txt').read_text().splitlines():
   t=line.split();i=t.index('F');ex.append(tuple(map(int,t[1:i]+t[i+1:])))
  assert set(rows)==set(ex) and len(ex)==n
  row=next(b for b in B if b['c']==c);assert row['B_types']==read(f't15_r3_small_core27_c{c}.json')['B_types']
  assert row['total']==(135135 if c==1 else 1621620)
  assert row['B_types']['0']==(82 if c==1 else 144)
  if c==3:
   assert all(int(m)==0 or max((int(m)&7).bit_count(),(int(m)>>3).bit_count())>=2 for m in row['B_types'])
 p=read(f't15_core27_c{c}_residual.json');v=read(f't15_core27_c{c}_residual_verification.json')
 expected={1:11081070,3:38918880,5:32432400}[c]
 assert p['total']==p['positive']==expected and p['unknown']==p['negative']==0
 assert v['status']=='PASS' and v['records']==expected and v['total_bytes']==expected*56
 assert (R/f't15_core27_c{c}_residual_failures.txt').stat().st_size==0
 assert (R/f't15_core27_c{c}_residual.bin').stat().st_size==expected*56
 res.append(dict(c=c,B_exception_count=n,producer=p,independent_verifier=v))
block=read('t15_core27_blockers_verification.json');assert block['status']=='PASS'
c5rows=(R/'t15_core27_c5_B_inputs.txt').read_text().splitlines()[1:]
actual={norm(zip(list(map(int,row.split()))[5::2],list(map(int,row.split()))[6::2])) for row in c5rows}
assert {norm(f) for f in block['c5_unblocked_F']}==actual and len(actual)==2
assert all(r['null_families']==0 for r in block['reports'] if r['c']>=7 or r['mode']=='internal')
geo=read('t15_analytic_geometry.json')['T15']['residual_orbits'][27]
assert geo['avoided']==[1,7] and geo['included']==[26,28,31]
def tr(v):return sum(((v>>j)&1)<<[4,0,1,2,3][j] for j in range(5))
assert {tr(v) for v in {0,1,7,26,28,31}}=={0,13,14,16,19,31}
assert {tr(v) for v in {1,7}}=={16,19}
assert all((tr(v)^tr(v^(1<<j))).bit_count()==1 for v in range(32) for j in range(5))
prior=read('T15_BALANCED_BRIDGE_REVIEW.json')
imports=['Q4_CORE_AND_A4_SPLIT.md','q4_two_hole_3.bin','q4_two_hole_15.bin']+[p.name for p in R.glob('q4_balanced_two_avoided_*.bin')]
for p in imports:assert digest(p)==prior['audited_input_hashes'][p]
inputs=['T15_CORE27_FULL_CLOSURE.md','t15_analytic_geometry.json','T15_BALANCED_BRIDGE_REVIEW.md','T15_BALANCED_BRIDGE_REVIEW.json','T15_R3_SMALL_CROSSING_PROGRESS.md','t15_residual_fast.cpp','verify_t15_residual_rank.cpp','verify_t15_core27_B.cpp','verify_t15_core27_blockers.py','r3_boundary_blocking_3_8.json','r3_boundary_blocking_6_8.json','t15_core27_blockers_verification.json','t15_core27_B_verification.json','verify_t15_core27_full_closure.py']+imports
for c in (1,3,5):inputs += [f't15_core27_c{c}_B_inputs.txt',f't15_core27_c{c}_residual.bin',f't15_core27_c{c}_residual.json',f't15_core27_c{c}_residual_verification.json']
out=dict(status='PASS',scope='Complete candidate proof finite package for core27 only; fresh semantic audit required',generated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),original_holes=[0,1,7,26,28,31],normalized_holes=[0,13,14,16,19,31],omitted=[16,19],coordinate_permutation=[4,0,1,2,3],positive_residuals=res,total_positive_residuals=82432350,total_certificate_bytes=4616211600,blockers=block,import_hashes_match=True,audited_input_hashes={p:digest(p) for p in inputs},full_T15_proved=False,full_eight_hole_layer_proved=False,P6_proved=False,independent_overall_review_pending=True)
(R/'T15_CORE27_FULL_CLOSURE_VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('audited_input_hashes','blockers','positive_residuals')}))
