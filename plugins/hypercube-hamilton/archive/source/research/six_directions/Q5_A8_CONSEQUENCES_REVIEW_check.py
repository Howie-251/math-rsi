"""Independent six-cut replay on the previously accepted exact residual domain."""
from pathlib import Path
from collections import Counter
import hashlib,json
P=Path(__file__).resolve().parent
GOOD={(0,1),(1,1),(0,2),(3,4),(4,4),(3,5)}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def match_hash(actual,expected):return actual==expected.removeprefix('sha256:')
names=['Q5_A8_ENDPOINT_AND_TEN_CONSEQUENCES.md','ten_covered_after_full_A8.py',
 'ten_covered_after_full_A8.json','Q5_A8_FULL_CLOSURE.md','Q5_A8_FULL_REVIEW.json',
 'Q5_A8_FULL_REVIEW.md','TEN_HOLE_COVERED_PARTIAL_A8_TRANSFER.md',
 'TEN_HOLE_COVERED_PARTIAL_REVIEW.md','TEN_HOLE_COVERED_PARTIAL_REVIEW.json',
 'HIGHER_HOLE_UNIFIED_TRANSFER.md','HIGHER_HOLE_UNIFIED_TRANSFER_REVIEW.json',
 'Q5_K8_CLOSURE.md','Q5_K8_REVIEW.json','A6_AND_EIGHT_FREE_CLOSED.md',
 'A6_CLOSURE_REVIEW.json','A6_CLOSURE_REVIEW.md']
for v in (1,7,31):names += [f'TEN_HOLE_COVERED_PARTIAL_REVIEW_remaining_v{v}.bin',f'ten_covered_after_full_A8_v{v}.bin']
hashes={n:sha(P/n) for n in names}
assert hashes['Q5_A8_FULL_REVIEW.json']=='625a3c3ac4db6742a23e3e6a9291c87b5ab8588da691445a0426cce07da5bf47'
imports={}
for report in ['Q5_A8_FULL_REVIEW.json','TEN_HOLE_COVERED_PARTIAL_REVIEW.json',
 'HIGHER_HOLE_UNIFIED_TRANSFER_REVIEW.json','Q5_K8_REVIEW.json','A6_CLOSURE_REVIEW.json']:
 j=json.loads((P/report).read_text());assert j['verdict']=='PASS'
 # Rebind theorem-bearing/direct import source bytes; old large certificates remain accepted imports.
 for group in ('audited_input_hashes','imported_dependency_hashes'):
  for n,expected in j.get(group,{}).items():
   path=P/n
   assert path.exists(),(report,n)
   actual=sha(path);assert match_hash(actual,expected),(report,n,'stale')
   imports[n]=actual
baseline=json.loads((P/'TEN_HOLE_COVERED_PARTIAL_REVIEW.json').read_text())
approved={r['v']:r for r in baseline['details']['exact_residual_comparisons']}
producer=json.loads((P/'ten_covered_after_full_A8.json').read_text())
by_target={r['v']:r for r in producer['reports']}
assert set(by_target)=={1,7,31} and len(producer['reports'])==3
rows=[]
for v in (1,7,31):
 inp=f'TEN_HOLE_COVERED_PARTIAL_REVIEW_remaining_v{v}.bin'
 raw=(P/inp).read_bytes();assert match_hash(sha(P/inp),approved[v]['independent_sha256'])
 assert len(raw)==approved[v]['count']*9
 original=[raw[i:i+9] for i in range(0,len(raw),9)]
 assert len(set(original))==len(original)
 faces=[{x for x in range(64) if (x&(1<<d))==(v&(1<<d))} for d in range(6)]
 candidates={};kept=[];rule_counts=Counter();source_checks=0
 for i,rec in enumerate(original):
  Z=set(rec[:4]);W=set(rec[4:])
  assert len(Z)==4 and len(W)==5 and not(Z&W) and 0 not in Z|W and v not in Z|W
  assert all(x in range(1,64) and x.bit_count()%2==0 for x in Z)
  assert all(x in range(64) and x.bit_count()%2==1 for x in W)
  assert list(rec[:4])==sorted(Z) and list(rec[4:])==sorted(W)
  assert all((z^w).bit_count()!=1 for z in Z for w in W)
  cuts=[]
  for d,A in enumerate(faces):
   za,wa=Z&A,W&A;a,b=len(za),len(wa)
   if (a,b) not in GOOD:continue
   cuts.append((d,a,b))
   # Geometric existence of legal optional bridge sources, independently from row counts.
   if (a,b) in {(0,2),(3,5)}:
    eligible={w for w in wa if w^(1<<d)!=0}
    assert eligible and len(eligible)>=b-1 and v not in eligible
    for w in eligible:assert w^(1<<d) not in Z|W|{0}
    source_checks+=1
   if (a,b) in {(1,1),(4,4)}:
    assert za and all(z^(1<<d) not in Z|W|{0} for z in za)
    source_checks+=1
  if cuts:
   candidates[i]=cuts;_,a,b=min(cuts);rule_counts[str((a,b))]+=1
  else:kept.append(rec)
 # Independently computed complete covered-index set, then replay every supplied witness.
 report=by_target[v];witness=report['witnesses']
 assert len(witness)==len(candidates)
 seen=set()
 for w in witness:
  i=w['input_index'];assert i in candidates and i not in seen;seen.add(i)
  assert (w['cut'],w['a'],w['b']) in candidates[i]
  assert (w['cut'],w['a'],w['b'])==min(candidates[i])
 assert seen==set(candidates)
 outfile=f'ten_covered_after_full_A8_v{v}.bin';out=(P/outfile).read_bytes()
 assert out==b''.join(kept)
 output_records=[out[i:i+9] for i in range(0,len(out),9)]
 assert len(out)%9==0 and len(set(output_records))==len(output_records)
 assert set(output_records)==set(original)-{original[i] for i in candidates}
 assert len(kept)==report['remaining'] and len(candidates)==report['newly_covered']
 assert len(original)==report['input_count'] and report['input_file']==inp and report['remaining_file']==outfile
 assert sha(P/inp)==report['input_sha256'] and sha(P/outfile)==report['remaining_sha256']
 rows.append({'v':v,'input_count':len(original),'newly_covered':len(candidates),'remaining':len(kept),
  'first_success_row_counts':dict(rule_counts),'source_existence_checks':source_checks,
  'input_sha256':sha(P/inp),'remaining_sha256':sha(P/outfile),'exact_bytes_and_sets_equal':True})
assert [r['remaining'] for r in rows]==[16920,17022,20280]
assert sum(r['newly_covered'] for r in rows)==37003
assert sum(r['input_count'] for r in rows)==91225 and sum(r['remaining'] for r in rows)==54222
assert (producer['input_count'],producer['newly_covered'],producer['remaining'])==(91225,37003,54222)
assert hashes=={n:sha(P/n) for n in names},'Audited input changed'
assert imports=={n:sha(P/n) for n in imports},'Accepted import changed'
out={'status':'PASS','input_count':91225,'newly_covered':37003,'remaining_open':54222,
 'reports':rows,'audited_input_hashes':hashes,'accepted_import_source_bindings':imports,
 'checker_sha256':sha(Path(__file__)),'producer_imported_or_executed':False,
 'large_old_matching_certificates_rerun':False,'full_ten_hole_proved':False,'full_P6_proved':False}
(P/'Q5_A8_CONSEQUENCES_REVIEW_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('audited_input_hashes','accepted_import_source_bindings')},indent=2))
