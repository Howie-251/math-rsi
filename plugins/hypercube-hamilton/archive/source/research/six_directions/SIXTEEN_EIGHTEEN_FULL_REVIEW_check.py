"""Independent final assembly binding/partition check; never imports producers."""
import hashlib, itertools, json, pathlib, struct
from datetime import datetime, timezone
R = pathlib.Path(__file__).resolve().parent
def rd(n): return json.loads((R/n).read_text(encoding='utf-8-sig'))
def sha(n):
    h = hashlib.sha256()
    with (R/n).open('rb') as f:
        for b in iter(lambda:f.read(1048576), b''): h.update(b)
    return h.hexdigest()
proof = 'SIXTEEN_EIGHTEEN_FULL_CLOSURE.md'
assert sha(proof) == '24e2d63b517540f20b30258521f742595e78442794057b6115379e5fec015c4c'
gates = [n+'_REVIEW.json' for n in ['HIGHER_Q5_FULL','HIGHER_POST12_REUSE','HIGHER_POST12_T39','SIXTEEN_LOCAL','SIXTEEN_STAR','SIXTEEN_SMALLCUT']]
predecessor='FOURTEEN_HOLE_FULL_REVIEW.json'
assert sha(predecessor)=='1a0cdb802f41bd7f8df31b47ce3980d092005ebe0c4e204e233c783aed17d634'
gates.insert(0,predecessor)
bindings = {}; checked = {}; gate_hashes = {}
for n in gates:
    d = rd(n); assert d['verdict']=='PASS', n
    gate_hashes[n] = sha(n)
    count = 0
    for field in ['audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes','evidence']:
        for f, h in d.get(field,{}).items():
            if not isinstance(h,str) or len(h.removeprefix('sha256:'))!=64: continue
            h = h.removeprefix('sha256:')
            if f not in checked: checked[f] = sha(f)
            assert checked[f] == h, (n,field,f,h,checked[f])
            count += 1
    if 'report_hash' in d:
        assert sha(n[:-5]+'.md') == d['report_hash'],n
        count += 1
    bindings[n] = count
local=rd('SIXTEEN_LOCAL_REVIEW.json')['details']
pred=rd(predecessor)['details']
assert pred['full_fourteen_hole_proved'] and pred['covered_targets_included']
assert pred['uniform_over_every_realizing_original_short_matching']
assert pred['remaining_covered_target_geometries']==pred['remaining_free_target_geometries']==0
assert pred['dependency_DAG_acyclic'] and not pred['full_P6_proved']
endpoint_maps=0
for u in range(64):
    for v in range(64):
        if (u.bit_count()-v.bit_count())%2==0: continue
        t=u^v
        ones=[i for i in range(6) if (t>>i)&1]
        perm=ones+[i for i in range(6) if i not in ones]
        def tr(x): return sum((((x^u)>>p)&1)<<i for i,p in enumerate(perm))
        assert tr(u)==0 and tr(v)==(1<<len(ones))-1 and tr(v) in (1,7,31)
        assert len({tr(x) for x in range(64)})==64
        assert all((tr(x)^tr(x^(1<<i))).bit_count()==1 for x in range(64) for i in range(6))
        endpoint_maps+=1
assert endpoint_maps==2048
assert local['remaining_covered_target_geometries']==148
assert rd('HIGHER_POST12_T39_REVIEW.json')['details']['complete16_implies_complete18_proved']
small=rd('SIXTEEN_SMALLCUT_application.json')['witnesses']
small_indices={}
for w in small:
    key=(w['v'],w['input_index'])
    assert key not in small_indices
    small_indices[key]=bytes(w['record'])
star_indices={}
raw=(R/'SIXTEEN_STAR_actual_witnesses.bin').read_bytes()
assert len(raw)==30*6
for v,i,pi in struct.iter_unpack('<BIB',raw):
    assert (v,i) not in star_indices and v==31 and pi<120
    star_indices[v,i]=pi
reports=[]; seen_small=set();seen_star=set()
for v in (1,7,31):
    srcname=f'SIXTEEN_LOCAL_remaining_v{v}_covered.bin'
    raw=(R/srcname).read_bytes();assert len(raw)%15==0
    src=[raw[i:i+15] for i in range(0,len(raw),15)]
    assert len(src)==len(set(src))
    star_yes=[];small_yes=[];star_no=[];small_no=[]
    star_ix=[];small_ix=[]
    for i,r in enumerate(src):
        z,w=list(r[:7]),list(r[7:])
        assert z==sorted(set(z)) and w==sorted(set(w))
        assert all(x!=0 and x<64 and x.bit_count()%2==0 for x in z)
        assert all(x<64 and x.bit_count()%2==1 for x in w) and v not in w
        assert all((x^y).bit_count()!=1 for x in z for y in w)
        key=(v,i); sy=key in star_indices; cy=key in small_indices
        assert sy != cy, ('not complementary',key)
        if sy: seen_star.add(key);star_ix.append(i)
        if cy:
            seen_small.add(key);small_ix.append(i)
            assert small_indices[key]==r,('index drift',key)
        (star_yes if sy else star_no).append(r)
        (small_yes if cy else small_no).append(r)
    names={f'SIXTEEN_STAR_remaining_v{v}_covered.bin':b''.join(star_no),
           f'SIXTEEN_SMALLCUT_remaining_v{v}_covered.bin':b''.join(small_no),
           f'SIXTEEN_SMALLCUT_positive_v{v}_covered.bin':b''.join(small_yes)}
    for n,b in names.items():
        assert (R/n).read_bytes()==b,('subsequence mismatch',n)
    assert b''.join(star_no)==b''.join(small_yes)
    assert b''.join(small_no)==b''.join(star_yes)
    reports.append({'v':v,'source':len(src),'star_positive':len(star_yes),
                    'smallcut_positive':len(small_yes),'remaining_after_union':0,
                    'star_positive_source_indices':star_ix,'smallcut_positive_source_indices':small_ix,
                    'stream_sha256':{n:sha(n) for n in [srcname,*names]}})
assert seen_star==set(star_indices) and seen_small==set(small_indices)
assert len(seen_star)==30 and len(seen_small)==118
out={'status':'PASS',
     'generated_at':datetime.now(timezone.utc).isoformat(),
     'frozen_proof_sha256':sha(proof),'gate_sha256':gate_hashes,
     'binding_comparisons_by_gate':bindings,'distinct_bound_files':len(checked),
     'reports':reports,'total_source':148,'union_positive':148,
     'remaining_covered_target_geometries':0,'remaining_free_target_geometries':0,
     'full_fourteen_hole_predecessor_sha256':sha(predecessor),
     'predecessor_conditions_discharged':True,'all_ordered_endpoint_maps_checked':endpoint_maps,
     'producer_code_executed_or_imported':False,'producer_or_main_state_modified':False}
(R/'SIXTEEN_EIGHTEEN_FULL_REVIEW_check.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'bindings':sum(bindings.values()),'distinct':len(checked),'partition':[(d['v'],d['source'],d['star_positive'],d['smallcut_positive']) for d in reports]}))
