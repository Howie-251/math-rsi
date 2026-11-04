"""Author-side positive forest check and immutable local theorem manifest."""
import json, hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
summary=json.loads((R/'Q5_T37_INDEPENDENT_summary.json').read_text())
registry=[r for r in summary['reports'] if r['full_rank']]
assert len(registry)==55
files=['Q5_T37_INDEPENDENT_PROOF.md','Q5_T37_INDEPENDENT_summary.json',
       'Q5_T37_INDEPENDENT_geometry.py','Q5_T37_INDEPENDENT_geometry.json',
       'Q5_T37_INDEPENDENT_search.cpp','prepare_T37_rank_search.py',
       'Q5_T37_INDEPENDENT_run.py','Q5_T37_INDEPENDENT_freeze.py',
       'A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md','A10_ORBIT3_UNIVERSAL_REVIEW.json']
results=[]
for row in registry:
    pre=row['prefix'];g=row['geometry'];H=set(g['minority']+g['majority']);U=set(g['omitted']);K=set(range(32))-H
    assert len(H)==10 and len(U)==2 and U<=H and len(K)==22
    forests=(R/(pre+'_forests.bin')).read_bytes();pairs=(R/(pre+'_pairs.bin')).read_bytes();cols=(R/(pre+'_columns.bin')).read_bytes()
    assert len(forests)==1024*38 and len(pairs)==len(cols)==1024*22
    for i in range(1024):
        f=forests[38*i:38*(i+1)];adj={x:[] for x in range(32) if x not in U};edges=set()
        for a,b in zip(f[::2],f[1::2]):
            assert a in adj and b in adj and (a^b).bit_count()==1
            edge=tuple(sorted((a,b)));assert edge not in edges;edges.add(edge)
            adj[a].append(b);adj[b].append(a)
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
        p=pairs[22*i:22*(i+1)];c=cols[22*i:22*(i+1)]
        assert set(p)==set(c)==K and len(set(p))==len(set(c))==22
        assert actual=={tuple(sorted(e)) for e in zip(p[::2],p[1::2])}
    results.append({'index':row['index'],'forests_checked':1024})
    files.extend(pre+s for s in ['_forests.bin','_pairs.bin','_columns.bin','_matrix.bin','_pivots.bin','_combos.bin','_config.txt','.json'])
name='Q5_T37_INDEPENDENT_author_check.json'
(R/name).write_text(json.dumps({'status':'PASS_SELECTED_FORESTS_AND_COLUMNS_ONLY','independent_rank_check_pending':True,'reports':results},indent=2)+'\n')
files.append(name)
manifest={'status':'FROZEN_CANDIDATE_INDEPENDENT_REVIEW_PENDING','claimed_indices':[r['index'] for r in registry],
          'open_indices':[r['index'] for r in summary['reports'] if not r['full_rank']],
          'files':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in files},
          'full_twelve_hole_proved':False,'full_P6_proved':False}
(R/'Q5_T37_INDEPENDENT_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Frozen 55 local inputs and 56320 legal selected forests; independent rank review pending.')
