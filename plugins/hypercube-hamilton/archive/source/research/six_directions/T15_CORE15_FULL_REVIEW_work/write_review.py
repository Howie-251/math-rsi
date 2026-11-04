import hashlib,json,math
from datetime import datetime,timezone
from pathlib import Path
W=Path(__file__).resolve().parent;R=W.parent
checks=json.loads((W/'fresh_input_verification.json').read_text())
assert checks['status']=='PASS'
p=(0,1,2,4,3)
tr=lambda v:sum(((v>>j)&1)<<p[j] for j in range(5))
assert {tr(v) for v in (0,1,2,13,22,31)}=={0,1,2,14,21,31}
assert [tr(v) for v in (1,2)]==[1,2]
for v in range(32):
    for j in range(5):assert (tr(v)^tr(v^(1<<j))).bit_count()==1
assert {v//2 for v in (0,1,2,14,21,31) if v%2}=={0,10,15}
assert {v//2 for v in (0,1,2,14,21,31) if not v%2}=={0,1,7}
df=lambda n:math.prod(range(n,0,-2))
by_c={c:math.comb(13,c)**2*df(12-c)**2*math.factorial(c) for c in range(1,14,2)}
assert sum(by_c.values())==df(25)
names=['T15_CORE15_FULL_CLOSURE.md','T15_CORE15_FULL_CLOSURE_VERIFICATION.json',
 'verify_t15_core15_residual.cpp','verify_t15_core15_table.py','verify_t15_core15_full_closure.py',
 'verify_t15_r3_small_B.cpp','verify_t15_r3_small_results.py','T15_R3_SMALL_CROSSING_PROGRESS.md',
 't15_r3_small_verification.json','t15_core15_c1_B_inputs.txt','t15_core15_c3_B_inputs.txt',
 't15_r3_small_core15_c1_B_exceptions.txt','t15_r3_small_core15_c3_B_exceptions.txt',
 't15_r3_small_core15_c1.json','t15_r3_small_core15_c3.json',
 't15_core15_c1_fast.bin','t15_core15_c3_hybrid.bin','q4_two_hole_3.bin','q4_two_hole_15.bin']
names += [x.name for x in sorted(R.glob('q4_balanced_two_avoided_*_*.bin'))]
hashes={n:'sha256:'+hashlib.sha256((R/n).read_bytes()).hexdigest() for n in names}
for n in ['fresh_inputs.py','core15_small_B.cpp','verify_t15_core15_residual.cpp','fresh_input_verification.json','small_B_fresh.json','c1_fresh.json','c3_fresh.json']:
    hashes[f'{W.name}/{n}']='sha256:'+hashlib.sha256((W/n).read_bytes()).hexdigest()
out=dict(audit_skill='proof-checker',verdict='PASS',reason_code='all_proofs_complete',
 summary='Complete arbitrary-matching core15 closure passes semantic review and fresh exhaustive checks; same-family provisional acceptance only.',
 reviewer_model='gpt-6.1-sol',reviewer_reasoning='high',reviewer_family='openai',reviewer_agent_id='/root/t15_core15_complete_audit',
 review_independence='same-family',acceptance_status='provisional',generated_at=datetime.now(timezone.utc).isoformat(),
 audited_input_hashes=hashes,trace_path=W.name+'/',
 scope=dict(core=15,original_holes=[0,1,2,13,22,31],omitted=[1,2],all_KQ5_matchings=True,all_crossing_bijections=True,
            cube_automorphic_images=True,full_T15=False,full_eight_hole_layer=False),
 details=dict(theorems_audited=1,issues=[],open_fatal=0,open_critical=0,
    N14_base_positive_records=270270,balanced_complete_records=135135,balanced_tables=13,
    bridge10_uncertified_outputs=1,B_c1_inputs=135135,B_c1_exception_partial_inputs=12,
    B_c3_bijection_inputs=1621620,B_c3_exception_partial_inputs=1,B_c3_exception_bijections=6,
    positive_residual_records=3243240,residual_bytes_per_file=90810720,
    fresh_compilation='g++ -O3 -std=c++17, no -DNDEBUG',
    checked_original_matchings_partition=by_c,total_original_matchings=df(25),
    global_ledger_modified=False,original_proof_and_manifest_modified=False,
    nominal_skill_model_override='User-requested GPT-6.1-sol/high; no Astra/ultra or cross-family acceptance claimed.'))
(R/'T15_CORE15_FULL_REVIEW.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'verdict':'PASS','input_hashes':len(hashes),'original_matching_count':df(25)}))
