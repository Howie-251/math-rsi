"""Fresh audit supplement. Read production data; write only this audit directory."""
from pathlib import Path
import hashlib, itertools, json, math, collections, subprocess, datetime
W=Path(__file__).resolve().parent
R=W.parent
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda:f.read(8*1024*1024),b''):h.update(block)
    return 'sha256:'+h.hexdigest()
manifest=read(R/'T15_CORE8_FULL_CLOSURE_VERIFICATION.json')
hashes={p:sha(R/p) for p in manifest['audited_input_hashes']}
assert hashes==manifest['audited_input_hashes']
extra=['T15_CORE8_FULL_CLOSURE_VERIFICATION.json','t15_r3_c5_negative_kernels.json',
       't15_r3_small_core8_c1.json','t15_r3_small_core8_c3.json']
hashes.update({p:sha(R/p) for p in extra})
prior=read(R/'T15_BALANCED_BRIDGE_REVIEW.json')
for p in ['Q4_CORE_AND_A4_SPLIT.md','q4_two_hole_3.bin','q4_two_hole_15.bin']+[p.name for p in R.glob('q4_balanced_two_avoided_*.bin')]:
    assert hashes[p]==prior['audited_input_hashes'][p]
B=read(W/'B_rerun.json'); assert B==read(R/'t15_core8_B_verification.json')
for row in B:
    c=row['c']
    assert row['B_types']==read(R/f't15_r3_small_core8_c{c}.json')['B_types']
    expected=[tuple(map(int,l.split())) for l in (R/f't15_core8_c{c}_B_inputs.txt').read_text().splitlines()[1:]]
    observed=[]
    for l in (W/f't15_core8_checked_core8_c{c}_B_exceptions.txt').read_text().splitlines():
        t=l.split(); k=t.index('F'); observed.append(tuple(map(int,t[1:k]+t[k+1:])))
    assert len(expected)==len(set(expected))==len(observed)==len(set(observed))
    assert set(expected)==set(observed)
    if c==3:
        assert all(m=='0' or max(int(m).bit_count() if int(m)<8 else (int(m)&7).bit_count(),(int(m)>>3).bit_count())>=2 for m in row['B_types'])
        J={(2,4),(5,6),(9,11),(10,13)}; S={3,8,12,14,15}
        assert {frozenset(zip(r[3::2],r[4::2])) for r in expected}=={frozenset(J|{e}) for e in itertools.combinations(sorted(S),2)}
block=read(W/'t15_core8_blockers_verification.json')
assert block==read(R/'t15_core8_blockers_verification.json')
res=[read(W/f'c{c}_rerun.json') for c in [1,3,5]]
for r in res: assert r==read(R/f"t15_core8_c{r['c']}_residual_verification.json")
assert sum(r['records'] for r in res)==35405370
# Exhaustive combinadic/permutation range checks independent of input order.
rankchecks=[]
for c in (1,3,5):
    ranks={sum(math.comb(p,i+1) for i,p in enumerate(s)) for s in itertools.combinations(range(13),c)}
    assert ranks==set(range(math.comb(13,c)))
    def permscore(p):
        return sum(sum(q<x for q in p[i+1:])*math.factorial(c-i-1) for i,x in enumerate(p))
    assert {permscore(p) for p in itertools.permutations(range(c))}==set(range(math.factorial(c)))
    rankchecks.append({'c':c,'subsets':len(ranks),'permutations':math.factorial(c)})
# Assertion activation and malformed-certificate rejection, on tiny files only.
with (R/'t15_core8_c1_residual.bin').open('rb') as f: record=f.read(56)
mutations={'empty':b'','partial':record[:55],'duplicate':record+record,
           'bad_vertex':record[:26]+bytes([255])+record[27:],
           'matching_loop':record[:1]+record[:1]+record[2:],
           'one_valid_but_incomplete':record}
rejected={}
for name,data in mutations.items():
    p=W/f'mutation_{name}.bin';p.write_bytes(data)
    result=subprocess.run([str(W/'residual_check.exe'),'1',str(R/'t15_core8_c1_B_inputs.txt'),str(p)],capture_output=True)
    assert result.returncode!=0
    rejected[name]=result.returncode
# Geometry is independently obtained directly from the marked vertex labels.
swap=lambda v:(v&28)|((v&1)<<1)|((v&2)>>1)
H={swap(v) for v in (0,1,2,7,13,31)}
assert H=={0,1,2,7,14,31}
assert {v//2 for v in H if v%2}=={0,3,15}
assert {v//2 for v in H if not v%2}=={0,1,7}
# Optional read-only ledger recount. Do not run the production refresh script.
base=read(R/'eight_after_balanced_bridge_candidates.json'); ledger=read(R/'eight_current_core_ledger.json')
extra_cores=set(map(int,ledger['extra_review_files']))
remaining=[r for r in base['rows'] if not extra_cores.intersection(r['core_choices'])]
counts=dict(collections.Counter(str(r['target']) for r in remaining))
assert len(remaining)==ledger['remaining'] and counts==ledger['by_target']
assert sum(not r['core_choices'] for r in remaining)==ledger['without_a2b1']==50
assert set(base['proved_T15_core_orbits'])|extra_cores==set(ledger['closed_t15_orbits'])
assert sha(R/'eight_after_balanced_bridge_candidates.json').removeprefix('sha256:')==ledger['base_geometry_sha256']
for target in (1,7,31):
    raw=b''.join(bytes(r['Z']+r['W']) for r in remaining if r['target']==target)
    assert (R/f'remaining_eight_current_{target}.bin').read_bytes()==raw
context_hashes={p:sha(R/p) for p in ['eight_current_core_ledger.json','eight_after_balanced_bridge_candidates.json']+[f'remaining_eight_current_{t}.bin' for t in (1,7,31)]}
with8=[r for r in remaining if 8 not in r['core_choices']]
out={'status':'PASS','audited_input_hashes':hashes,'context_snapshot_hashes':context_hashes,
     'context_snapshot_metadata':{'sampled_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'role':'Read-only parent ledger background; not core8 theorem dependencies; may change on integration.'},'positive_residuals':res,
     'rank_component_checks':rankchecks,'mutation_rejections':rejected,
     'B_spectra_match':True,'exception_lists_equal':True,'blockers_match':True,
     'import_hashes_match':True,'current_ledger':{'remaining':len(remaining),'by_target':counts,'without_a2b1':50},
     'hypothetical_after_core8':{'remaining':len(with8),'by_target':dict(collections.Counter(str(r['target']) for r in with8))}}
(W/'fresh_supplement.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='audited_input_hashes'}))
