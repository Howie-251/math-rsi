"""Fresh exhaustive row(4,5) cut scan and exact combined residual binding."""
from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parent
def load(p):return json.loads((R/p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
hashes={}; gates=['Q5_A10_FULL_REVIEW.json','Q5_T63_COMPLETE_SPLIT_REVIEW.json','TEN_COVERED_T63_SPLIT_REVIEW.json','HIGHER_HOLE_UNIFIED_TRANSFER_REVIEW.json','Q5_A8_CONSEQUENCES_REVIEW.json']
for p in gates:
    d=load(p);assert d['verdict']=='PASS';hashes[p]=sha(p)
    for key in ['audited_input_hashes','evidence_hashes']:
        for f,h in d.get(key,{}).items():
            assert sha(f)==h.removeprefix('sha256:'),(p,f)
            hashes[f]=sha(f)
producer=load('ten_covered_full_q5_endpoint_filter.json')
reports=[]
def records(p):
    raw=(R/p).read_bytes();assert len(raw)%9==0
    recs=[raw[i:i+9] for i in range(0,len(raw),9)]
    assert len(set(recs))==len(recs);hashes[p]=sha(p)
    return raw,recs
for v in (1,7,31):
    p=next(a for a in producer['reports'] if a['v']==v)
    raw,recs=records(f'ten_covered_after_full_A8_v{v}.bin')
    assert hashlib.sha256(raw).hexdigest()==p['input_sha256']
    tbytes,tleft=records(f'ten_covered_t63_complete_split_remaining_v{v}.bin')
    assert hashlib.sha256(tbytes).hexdigest()==p['t63_remaining_sha256']
    assert set(tleft)<=set(recs)
    good=[];cutw=[]
    for n,rec in enumerate(recs):
        Z,W=rec[:4],rec[4:]
        assert len(set(rec))==9 and 0 not in rec and v not in rec
        assert list(Z)==sorted(Z) and list(W)==sorted(W)
        assert all(z.bit_count()%2==0 and 0<=z<64 for z in Z)
        assert all(w.bit_count()%2==1 and 0<=w<64 for w in W)
        assert all((z^w).bit_count()!=1 for z in Z for w in W)
        # Construct actual target-oriented faces as sets, then count each
        # parity's hole intersection; no producer all-bits predicate reused.
        cuts=[]
        for coord in range(6):
            A={x for x in range(64) if (x//(2**coord))%2==(v//(2**coord))%2}
            a,b=len(set(Z)&A),len(set(W)&A)
            if (a,b)==(4,5):cuts.append(coord)
        if cuts:good.append(rec);cutw.append({'input_index':n,'cut':min(cuts)})
    assert cutw==p['witnesses']
    goodset=set(good);tset=set(tleft)
    assert goodset<=tset # endpoint additions avoid all accepted T63 additions
    assert not goodset.intersection(set(recs)-tset)
    remaining=[rec for rec in recs if rec not in goodset]
    combo=[rec for rec in recs if rec not in goodset and rec in tset]
    eraw,erecs=records(f'ten_covered_full_q5_endpoint_remaining_v{v}.bin')
    craw,crecs=records(f'ten_covered_q5_and_t63_remaining_v{v}.bin')
    assert b''.join(remaining)==eraw and set(remaining)==set(erecs)
    assert b''.join(combo)==craw and set(combo)==set(crecs)
    assert len(good)==p['newly_covered'] and len(combo)==p['combined_remaining']
    assert hashlib.sha256(eraw).hexdigest()==p['endpoint_remaining_sha256']
    assert hashlib.sha256(craw).hexdigest()==p['combined_remaining_sha256']
    reports.append({'v':v,'input':len(recs),'endpoint_new':len(good),'T63_new':len(recs)-len(tleft),
       'addition_overlap':0,'endpoint_only_remaining':len(remaining),'combined_remaining':len(combo),
       'all_declared_actual_cut_witnesses_verified':True,'exact_remaining_bytes_and_sets':True,
       'combined_sha256':hashlib.sha256(craw).hexdigest()})
assert [r['endpoint_new'] for r in reports]==[10,30,30]
assert [r['combined_remaining'] for r in reports]==[12910,12696,15630]
for p in ['TEN_COVERED_Q5_ENDPOINT_APPLICATION.md','ten_covered_full_q5_endpoint_filter.py','ten_covered_full_q5_endpoint_filter.json']:hashes[p]=sha(p)
out={'status':'PASS','reports':reports,'total_inputs':54222,'endpoint_new':70,'T63_new':12916,
     'new_addition_overlap':0,'combined_remaining':41236,'all_import_gates_final_PASS':True,
     'producer_imported_or_executed':False,'audited_input_hashes':hashes}
(R/'TEN_COVERED_Q5_ENDPOINT_REVIEW_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='audited_input_hashes'},indent=2))
