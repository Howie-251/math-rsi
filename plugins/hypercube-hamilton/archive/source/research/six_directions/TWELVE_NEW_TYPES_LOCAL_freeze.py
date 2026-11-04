"""Author-side forest checks; freeze only111 selected positive local claims."""
import json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
summary=json.loads((R/'TWELVE_NEW_TYPES_summary.json').read_text())
selected=json.loads((R/'TWELVE_NEW_TYPES_greedy_registry.json').read_text())['indices']
assert len(selected)==len(set(selected))==111
registry={r['index']:r for r in summary['reports']}
specs={'T28':(22,1024,18),'T19':(22,1024,17),'T84':(24,2048,16),'T105':(22,1024,16)}
names=['TWELVE_NEW_TYPES_LOCAL_PROOF.md','TWELVE_NEW_TYPES_LOCAL_freeze.py',
       'TWELVE_NEW_TYPES_greedy_registry.json','TWELVE_NEW_TYPES_summary.json',
       'TWELVE_NEW_TYPES_profile.json','TWELVE_NEW_TYPES_prepare.py','TWELVE_NEW_TYPES_run.py',
       'A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md']
names.extend(f'TWELVE_NEW_{typ}_search.cpp' for typ in specs)
results=[]
for idx in selected:
    row=registry[idx];assert row['full_rank'];g=row['geometry'];n,r,e=specs[g['type']]
    pre=row['prefix'];H=set(g['minority']+g['majority']);U=set(g['omitted']);K=set(range(32))-H
    assert len(K)==n and U<=H
    forests=(R/(pre+'_forests.bin')).read_bytes();pairs=(R/(pre+'_pairs.bin')).read_bytes();cols=(R/(pre+'_columns.bin')).read_bytes()
    assert len(forests)==r*2*e and len(pairs)==len(cols)==r*n
    for i in range(r):
        f=forests[2*e*i:2*e*(i+1)];adj={x:[] for x in range(32) if x not in U};es=set()
        for a,b in zip(f[::2],f[1::2]):
            assert a in adj and b in adj and (a^b).bit_count()==1
            edge=tuple(sorted((a,b)));assert edge not in es;es.add(edge);adj[a].append(b);adj[b].append(a)
        assert all(len(adj[x])==(1 if x in K else 2) for x in adj)
        seen=set();actual=set()
        for x in sorted(K):
            if x in seen:continue
            prev=None;y=x
            while True:
                assert y not in seen;seen.add(y);nxt=[z for z in adj[y] if z!=prev]
                if not nxt:break
                assert len(nxt)==1;prev,y=y,nxt[0]
            assert y in K;actual.add(tuple(sorted((x,y))))
        assert seen==set(adj)
        p=pairs[n*i:n*(i+1)];c=cols[n*i:n*(i+1)]
        assert set(p)==set(c)==K and len(set(p))==len(set(c))==n
        assert actual=={tuple(sorted(edge)) for edge in zip(p[::2],p[1::2])}
    results.append({'index':idx,'type':g['type'],'forests_checked':r,'rank_claim':r})
    names.extend(pre+s for s in ['_forests.bin','_pairs.bin','_columns.bin','_matrix.bin','_pivots.bin','_combos.bin','_config.txt','.json'])
author='TWELVE_NEW_TYPES_LOCAL_author_check.json'
(R/author).write_text(json.dumps({'status':'PASS_SELECTED_FORESTS_AND_COLUMNS_ONLY','independent_rank_check_pending':True,'reports':results},indent=2)+'\n')
names.append(author)
manifest={'status':'FROZEN_CANDIDATE_INDEPENDENT_REVIEW_PENDING','claimed_indices':selected,
    'files':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in names},
    'full_twelve_hole_proved':False,'full_P6_proved':False}
(R/'TWELVE_NEW_TYPES_LOCAL_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Frozen111 marked inputs;',sum(x['forests_checked'] for x in results),'legal forests; independent rank audit pending.')
