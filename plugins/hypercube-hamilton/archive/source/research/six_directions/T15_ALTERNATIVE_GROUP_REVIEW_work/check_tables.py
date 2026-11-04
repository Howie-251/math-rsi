import json, itertools, hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
rows=[]; transformed={}
def tr(v,p): return sum(((v>>j)&1)<<p[j] for j in range(4))
for f in sorted(R.glob('q4_balanced_two_avoided_*.bin')):
    z,y=map(int,f.stem.rsplit('_',2)[1:]); raw=f.read_bytes()
    assert len(raw)==10395*30
    holes={0,7,z,y}; seen=set(); negatives=[]
    assert len(holes)==4
    for i in range(0,len(raw),30):
        m=raw[i:i+16]; cyc=raw[i+16:i+30]
        assert {v for v in range(16) if m[v]==255}==holes
        assert all(m[v]<16 and m[v]!=v and m[m[v]]==v for v in set(range(16))-holes)
        assert m not in seen; seen.add(m)
        req={tuple(sorted((v,m[v]))) for v in range(16) if m[v]<16}
        if cyc[0]==255:
            assert cyc==bytes([255])*14; negatives.append(req); continue
        assert len(set(cyc))==14 and set(cyc)==set(range(16))-{z,y}
        edges={tuple(sorted((cyc[j],cyc[(j+1)%14]))) for j in range(14)}
        assert req<=edges
        assert all((a^b).bit_count()==1 for a,b in edges-req)
    for p0 in itertools.permutations(range(3)):
        p=(*p0,3); key=(tr(z,p),tr(y,p))
        ns={frozenset(tuple(sorted((tr(a,p),tr(b,p)))) for a,b in e) for e in negatives}
        if key in transformed: assert transformed[key]==ns
        transformed[key]=ns
    rows.append(dict(file=f.name,records=len(seen),positive=len(seen)-len(negatives),negative=len(negatives),sha256=hashlib.sha256(raw).hexdigest()))
assert len(rows)==13 and len(transformed)==49
target_counts={(6,1):2,(12,1):1,(10,1):1,(3,8):10,(6,8):10}
for key,n in target_counts.items(): assert len(transformed[key])==n
# All text-list negatives used for core25 transport must equal the raw-table images.
textneg={}
for ln in (R/'t15_r3_small_negative_inputs.txt').read_text().splitlines():
    z,y,*m=map(int,ln.split()); textneg.setdefault((z,y),set()).add(frozenset((a,m[a]) for a in range(16) if a<m[a]<16))
for key in ((3,8),(5,8),(6,8)): assert textneg[key]==transformed[key]
out=dict(status='PASS',records=sum(r['records'] for r in rows),rows=rows,target_negative_counts={str(k):n for k,n in target_counts.items()},text_transport_lists_equal_raw_tables=True)
(R/'tables_run.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
