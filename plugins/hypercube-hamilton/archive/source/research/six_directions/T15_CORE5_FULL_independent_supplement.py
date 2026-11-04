import json, hashlib, itertools
from pathlib import Path
from datetime import datetime, timezone
R=Path(__file__).resolve().parent
def read(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def digest(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
base=read('T15_BALANCED_BRIDGE_REVIEW.json')
assert base['verdict']=='PASS'
# Check exact current identity of imported foundations against their prior audit.
foundation_names=['Q4_CORE_AND_A4_SPLIT.md','q4_two_hole_3.bin','q4_two_hole_15.bin','q4_balanced_two_avoided_3_1.bin','q4_balanced_two_avoided_3_4.bin','T15_BALANCED_BRIDGE_REVIEW.md']
for n in foundation_names:assert base['audited_input_hashes'][n]=='sha256:'+digest(n),(n,'STALE')
actual=read('T15_CORE5_FULL_independent_check.json')
for i,c in enumerate((1,3)):
    assert actual['histograms'][i]==read(f't15_r3_small_core5_c{c}.json')['B_types']
    assert sum(actual['histograms'][i].values())==(135135 if c==1 else 1621620)
assert digest('t15_core5_c1_residual.bin')=='929204e08c9337ff76f778b6edd3586e42ecdcba2cf5734e56d03c8b3869b1b8'
# Additional independent c5 inverse rows, set representation and all coordinate images.
negative=None
sources=[]
for path in sorted(R.glob('q4_balanced_two_avoided_*_*.bin')):
    r,y=map(int,path.stem.split('_')[-2:])
    for p in itertools.permutations(range(3)):
        def tr(v):return sum(((v>>j)&1)<< (p[j] if j<3 else 3) for j in range(4))
        if (tr(r),tr(y))!=(6,1):continue
        raw=path.read_bytes()
        rows=set()
        for i in range(0,len(raw),30):
            if raw[i+16]==255:
                assert raw[i+16:i+30]==b'\xff'*14
                rows.add(frozenset(tuple(sorted((tr(a),tr(raw[i+a])))) for a in range(16) if a<raw[i+a]<16))
        assert len(rows)==2
        if negative is not None:assert rows==negative
        negative=rows;sources.append({'file':path.name,'permutation':list(p)+[3]})
assert negative is not None
parts={L-frozenset(pair) for L in negative for pair in itertools.combinations(L,2)}
assert len(parts)==30
inverse=[]
for f in sorted(parts,key=lambda x: sorted(x)):
    pts=set(range(16))-{0,1,7,6}-{v for e in f for v in e}
    assert len(pts)==4
    a,b,c,d=sorted(pts)
    qs=[frozenset((tuple(sorted(x)),tuple(sorted(y)))) for x,y in [((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))]]
    bad=[q for q in qs if f|q in negative]
    assert len(bad)==1
    inverse.append({'F_B':sorted(f),'quotient_vertices':sorted(pts),'bad_Q':sorted(bad[0])})
extra={'status':'PASS','foundation_import_hashes_match':True,
       'B_histograms_match_author_as_secondary_check':True,
       'negative_L':sorted([sorted(x) for x in negative]),
       'consistent_coordinate_sources':sources,'inverse_cases':inverse}
(R/'T15_CORE5_FULL_independent_supplement.json').write_text(json.dumps(extra,indent=2)+'\n',encoding='utf-8')
names=['T15_CORE5_FULL_CLOSURE.md','T15_CORE5_FULL_CLOSURE_VERIFICATION.json',
'T15_BALANCED_BRIDGE_REVIEW.json',*foundation_names,
'T15_R3_SMALL_CROSSING_PROGRESS.md','t15_r3_small_verification.json',
't15_r3_small_core5_c1.json','t15_r3_small_core5_c3.json',
't15_r3_small_core5_c1_B_exceptions.txt','t15_core5_c1_B_inputs.txt',
't15_core5_c1_residual.bin','t15_core5_c1_residual.cpp',
'verify_t15_core5_c1_residual.cpp','verify_t15_core5_c5_inverse.py',
'verify_t15_r3_small_B.cpp','T15_CORE5_FULL_independent_check.cpp',
'T15_CORE5_FULL_independent_supplement.py',
'T15_CORE5_FULL_independent_check.json','T15_CORE5_FULL_independent_supplement.json']
out={'audit_skill':'proof-checker','verdict':'PASS','reason_code':'all_proofs_complete',
'summary':'Complete exact marked core5 closure, conditional only on explicitly retained hash-matched audited Q4 N14 and exact balanced tables; new finite inputs independently recomputed. Same-family provisional semantic judgment.',
'reviewer_model':'gpt-6.1-sol','reviewer_reasoning':'high','fork_turns':'none',
'reviewer_family':'openai','review_independence':'same-family','acceptance_status':'provisional',
'reviewer_agent_id':'/root/t15_core5_complete_audit',
'nominal_skill_model_override':'Parent requested actual gpt-6.1-sol high fork_turns none; no Astra/ultra or cross-family review claimed.',
'generated_at':datetime.now(timezone.utc).isoformat(),
'scope':{'core':5,'holes':[0,1,2,7,13,14],'omitted':[1,2],'retained_free_vertices':[0,7,13,14],
         'A_holes':[0,3,6],'A_omitted':0,'B_holes':[0,7,1],'B_omitted':1,
         'all_original_matching_edges_arbitrary':True,'all_crossing_bijections':True,
         'all_crossing_counts':[1,3,5,7,9,11,13],
         'cube_automorphic_images':True,'full_T15':False,'full_eight_holes':False,'P6':False},
'audited_input_hashes':{n:'sha256:'+digest(n) for n in dict.fromkeys(names)},
'trace_path':'T15_CORE5_FULL_independent_check.json',
'details':{'theorems_audited':1,'issues':[],
'foundation_imports':'N14 all arbitrary matchings with same-parity holes, plus exact balanced tables, from hash-matched T15_BALANCED_BRIDGE_REVIEW; no new base run claimed.',
'independent_algorithm':'Fresh C++17: choose port subsets, independently pair complementary vertices; DSU component compression instead of author suppression/path tracing; reconstruct expected residual inputs and remove their required edges from certificate cycles.',
'independent_checks':actual,'supplement':'T15_CORE5_FULL_independent_supplement.json',
'certificate_bytes':(R/'t15_core5_c1_residual.bin').stat().st_size,
'large_crossings':'Elementary shared-edge obstruction for <=2 forbidden pairings on >=6 vertices; internal c>=5, occupied c>=7.',
'long_edges_preserved':True,'global_files_modified':False,
'counterexample_pass':['N=2 obstruction inapplicable and separately handled by c1','N=4 two-bad possibility separately excluded by exact c5 inverse','occupied c3 loops/closed components explicitly rejected','c13 zero internal edges','arbitrary non-short and same-parity required edges','suppressed kz recovered on expansion','all artificial D edges removed','no restriction on C permutation']}}
(R/'T15_CORE5_FULL_REVIEW.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','audited_input_hashes':len(out['audited_input_hashes']),'c5_rows':len(inverse),'consistent_sources':sources}))

