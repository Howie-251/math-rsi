"""Check all selected forest witnesses and freeze candidate sources/certificates."""
import json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
registry=json.loads((R/'Q5_T63_RANK_batch_summary.json').read_text())['reports']
results=[];files=['Q5_T63_RANK_PROOF.md','Q5_T63_RANK_search.cpp','prepare_T63_rank_search.py','Q5_T63_RANK_profile.py','Q5_T63_RANK_profile.json','Q5_T63_RANK_run.py','Q5_T63_RANK_batch_summary.json','Q5_T63_RANK_coverage.py','Q5_T63_RANK_coverage.json','A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md','A10_ORBIT3_UNIVERSAL_REVIEW.json','Q5_T26_RANK_BATCH_REVIEW.json','HIGHER_HOLE_UNIFIED_TRANSFER.md','HIGHER_HOLE_UNIFIED_TRANSFER_REVIEW.json']
for row in registry:
    pre=row['prefix'];H=set(row['geometry']['holes']);U=set(row['geometry']['omitted']);K=set(range(32))-H
    forests=(R/(pre+'_forests.bin')).read_bytes();pairs=(R/(pre+'_pairs.bin')).read_bytes();cols=(R/(pre+'_columns.bin')).read_bytes()
    assert len(forests)==4096*32 and len(pairs)==len(cols)==4096*26
    for i in range(4096):
        f=forests[32*i:32*(i+1)];adj={x:[] for x in range(32) if x not in U};es=set()
        for a,b in zip(f[::2],f[1::2]):
            assert a in adj and b in adj and (a^b).bit_count()==1
            e=tuple(sorted((a,b)));assert e not in es;es.add(e);adj[a].append(b);adj[b].append(a)
        assert all(len(adj[x])==(1 if x in K else 2) for x in adj)
        seen=set();actual=set()
        for x in sorted(K):
            if x in seen:continue
            prev=None;y=x
            while True:
                assert y not in seen;seen.add(y)
                nxt=[z for z in adj[y] if z!=prev]
                if not nxt:break
                assert len(nxt)==1;prev,y=y,nxt[0]
            assert y in K;actual.add(tuple(sorted((x,y))))
        assert seen==set(adj)
        p=pairs[26*i:26*(i+1)];assert set(p)==K and len(set(p))==26
        assert actual=={tuple(sorted(e)) for e in zip(p[::2],p[1::2])}
        c=cols[26*i:26*(i+1)];assert set(c)==K and len(set(c))==26
    results.append({'index':row['orbit_index'],'forests_checked':4096,'status':'PASS_SELECTED_FORESTS_AND_COLUMNS_ONLY'})
    files.extend(pre+s for s in ['_forests.bin','_pairs.bin','_columns.bin','_matrix.bin','_pivots.bin','_combos.bin','_config.txt','.json'])
for v in (1,7,31):files.extend([f'Q5_T26_RANK_BATCH_REVIEW_remaining_v{v}.bin',f'Q5_T63_RANK_remaining_v{v}.bin'])
report=R/'Q5_T63_RANK_author_check.json';report.write_text(json.dumps({'status':'PASS_SELECTED_FORESTS_AND_COLUMNS_ONLY','full_rank_independent_review_pending':True,'reports':results},indent=2)+'\n')
files.extend(['Q5_T63_RANK_freeze.py',report.name])
manifest={'status':'FROZEN_CANDIDATE_INDEPENDENT_REVIEW_PENDING','files':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in files},'full_ten_hole_proved':False,'full_P6_proved':False}
(R/'Q5_T63_RANK_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Frozen seven marked inputs, 28672 selected legal forests, and 4096-input conditional application.')
