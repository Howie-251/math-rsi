"""Independent semantic reconstruction of each exported CNF obligation."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
meta=json.loads((ROOT/'obligations.json').read_text(encoding='utf8'))
mapping={int(i):tuple(e) for i,e in meta['edge_variables'].items()}
expected_edges={(a,b) for a in range(1,64) for b in range(a+1,64) if (a^b).bit_count()==1}
assert set(mapping.values())==expected_edges and len(mapping)==186
base=[]
for x in range(1,64):
    ids=[i for i,e in mapping.items() if x in e]
    for i in ids:
        for j in ids:
            if i<j:base.append(frozenset((-i,-j)))
for a,b in expected_edges:
    base.append(frozenset(i for i,e in mapping.items() if a in e or b in e))
assert len(base)==meta['base_clauses']
for end,b in meta['branches'].items():
    expected=list(base)
    for p in b['covering_paths']:
        assert len(p)==64 and set(p)==set(range(64)) and p[0]==0 and p[-1]==int(end)
        pe=set()
        for a,z in zip(p,p[1:]):
            assert (a^z).bit_count()==1;pe.add(tuple(sorted((a,z))))
        expected.append(frozenset(i for i,e in mapping.items() if e not in pe))
    actual=[]
    for line in (ROOT/b['file']).read_text().splitlines():
        if line.startswith(('c','p')):continue
        ints=list(map(int,line.split()));assert ints[-1]==0
        actual.append(frozenset(ints[:-1]))
    from collections import Counter
    assert Counter(actual)==Counter(expected)
print(json.dumps({'verified_branches':3,'variables_each':186,'clauses_each':1137,'proves_unsat':False}))
