"""Read-only audit of raw Q4 inputs and isolated fresh Q5 checks."""
import hashlib,itertools,json
from pathlib import Path
R=Path(__file__).resolve().parent.parent
W=Path(__file__).resolve().parent
def matching_set(vs):
    if not vs:
        yield ();return
    a=vs[0]
    for j,b in enumerate(vs[1:],1):
        for rest in matching_set(vs[1:j]+vs[j+1:]):yield ((a,b),)+rest
def check_table(path,holes,omitted,width):
    raw=path.read_bytes();assert len(raw)%width==0
    expected=set(matching_set(tuple(sorted(set(range(16))-set(holes)))))
    seen=set();positives=0;negatives=[]
    for offset in range(0,len(raw),width):
        m=raw[offset:offset+16];cyc=raw[offset+16:offset+width]
        assert {v for v in range(16) if m[v]==255}==set(holes)
        for v in set(range(16))-set(holes):assert m[v]!=v and m[v]<16 and m[m[v]]==v
        f=tuple((v,m[v]) for v in range(16) if v<m[v]<16)
        assert f in expected and f not in seen;seen.add(f)
        if cyc[0]==255:
            assert all(v==255 for v in cyc);negatives.append(f);continue
        assert len(cyc)==len(set(cyc))==16-len(omitted)
        assert set(cyc)==set(range(16))-set(omitted)
        es={tuple(sorted((u,v))) for u,v in zip(cyc,cyc[1:]+cyc[:1])}
        assert set(f)<=es
        assert all((u^v).bit_count()==1 for u,v in es-set(f))
        positives+=1
    assert seen==expected
    return dict(file=path.name,records=len(seen),positive=positives,negative=len(negatives))
out={"status":"PASS","Q4_balanced":[],"Q4_N14":[]}
for p in sorted(R.glob('q4_balanced_two_avoided_*_*.bin')):
    z,y=map(int,p.stem.removeprefix('q4_balanced_two_avoided_').split('_'))
    out['Q4_balanced'].append(check_table(p,{0,7,z,y},{z,y},30))
assert len(out['Q4_balanced'])==13
for z in (3,15):
    result=check_table(R/f'q4_two_hole_{z}.bin',{0,z},{0},31)
    assert result['records']==135135 and result['negative']==0
    out['Q4_N14'].append(result)
# Regenerate bridge-10 negative list through the exact cube-coordinate swap.
raw=(R/'q4_balanced_two_avoided_9_2.bin').read_bytes()
p=(1,0,2,3)
tr=lambda v:sum(((v>>j)&1)<<p[j] for j in range(4))
assert {tr(v) for v in (0,7,9,2)}=={0,7,10,1}
negative=[]
for i in range(0,len(raw),30):
    if raw[i+16]==255:
        m=raw[i:i+16]
        negative.append(sorted(tuple(sorted((tr(a),tr(m[a])))) for a in range(16) if a<m[a]<16))
assert negative==[[(2,4),(3,13),(5,15),(6,8),(9,11),(12,14)]]
out['bridge10_negative']=negative
fresh=json.loads((W/'small_B_fresh.json').read_text(encoding='utf-8-sig'))
for row in fresh:
    c=row['c'];orig=json.loads((R/f't15_r3_small_core15_c{c}.json').read_text(encoding='utf-8-sig'))
    assert row['B_types']==orig['B_types'] and row['total']==orig['B_bijection_count']
    assert all(int(m)==0 or c==1 or max((int(m)&7).bit_count(),(int(m)>>3).bit_count())>=2 for m in row['B_types'])
    lines=(W/f't15_r3_small_core15_c{c}_B_exceptions.txt').read_text().splitlines()
    cases=[]
    for line in lines:
        s=line.split();k=s.index('F');cases.append(tuple(map(int,s[1:k]+s[k+1:])))
    expected=[tuple(map(int,l.split())) for l in (R/f't15_core15_c{c}_B_inputs.txt').read_text().splitlines()]
    assert set(cases)==set(expected) and len(cases)==len(expected)==(12 if c==1 else 1)
    for case in expected:
        assert len(set(case))==13 and set(case)==set(range(16))-{0,7,1}
    assert row['B_types']['0']==len(cases)*(1 if c==1 else 6)
out['core15_B']=fresh
manifest=json.loads((R/'T15_CORE15_FULL_CLOSURE_VERIFICATION.json').read_text(encoding='utf-8-sig'))
for row in manifest['residual_reports']:
    path=R/row['certificate_file'];assert path.stat().st_size==90810720
    assert hashlib.sha256(path.read_bytes()).hexdigest()==row['certificate_sha256']
    v=json.loads((W/f"c{row['c']}_fresh.json").read_text(encoding='utf-8-sig'))
    assert v==row['independent_positive_verifier']
out['positive_residual_records']=3243240
(W/'fresh_input_verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','balanced_records':sum(t['records'] for t in out['Q4_balanced']),'N14_records':270270,'residual_records':3243240}))
