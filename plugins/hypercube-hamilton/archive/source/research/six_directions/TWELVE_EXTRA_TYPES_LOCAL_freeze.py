"""Check and freeze eleven newly needed local marked inputs."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent
selected=json.loads((R/'TWELVE_EXTRA_TYPES_greedy_registry.json').read_text())['indices']
assert selected==[0,3,5,51,77,183,32,18,58,52,12]
rows={r['index']:r for r in json.loads((R/'TWELVE_EXTRA_TYPES_summary.json').read_text())['reports']}
names=['TWELVE_EXTRA_TYPES_LOCAL_PROOF.md','TWELVE_EXTRA_TYPES_LOCAL_freeze.py',
       'TWELVE_EXTRA_TYPES_greedy_registry.json','TWELVE_EXTRA_TYPES_summary.json',
       'TWELVE_EXTRA_TYPES_profile.json','TWELVE_EXTRA_TYPES_run.py',
       'Q5_T26_RANK_search.cpp','Q5_T17_RANK_search.cpp','A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md']
for idx in selected:
    row=rows[idx];assert row['full_rank'] and row['rank']==2048
    g=row['geometry'];pre=row['prefix'];e=18 if g['type']=='T26' else 17
    H=set(g['minority']+g['majority']);U=set(g['omitted']);K=set(range(32))-H
    assert len(K)==24
    forests=(R/(pre+'_forests.bin')).read_bytes();pairs=(R/(pre+'_pairs.bin')).read_bytes();cols=(R/(pre+'_columns.bin')).read_bytes()
    assert len(forests)==2048*2*e and len(pairs)==len(cols)==2048*24
    for i in range(2048):
        adj={x:[] for x in range(32) if x not in U};es=set();f=forests[2*e*i:2*e*(i+1)]
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
        p=pairs[24*i:24*(i+1)];c=cols[24*i:24*(i+1)]
        assert set(p)==set(c)==K and len(set(p))==len(set(c))==24
        assert actual=={tuple(sorted(edge)) for edge in zip(p[::2],p[1::2])}
    names.extend(pre+s for s in ['_forests.bin','_pairs.bin','_columns.bin','_matrix.bin','_pivots.bin','_combos.bin','_config.txt','.json'])
manifest={'status':'FROZEN_CANDIDATE_INDEPENDENT_REVIEW_PENDING','claimed_indices':selected,
          'author_check':'22528 forests and columns checked, independent rank audit pending',
          'files':{n:hashlib.sha256((R/n).read_bytes()).hexdigest() for n in names},
          'full_twelve_hole_proved':False,'full_P6_proved':False}
(R/'TWELVE_EXTRA_TYPES_LOCAL_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Frozen11 marked inputs and22528 author-checked short forests.')
