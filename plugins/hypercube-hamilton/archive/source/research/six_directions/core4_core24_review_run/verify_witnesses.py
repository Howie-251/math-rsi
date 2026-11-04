"""Independent checker: no imports from case generator or path search."""
import json, sys, hashlib
from pathlib import Path

def check(c):
    n,u,v=c['n'],c['u'],c['v']; size=1<<n
    assert u==0 and v.bit_count()%2==1
    used=set(); required=set()
    for a,b in c['matching']:
        assert 0<=a<size and 0<=b<size and (a^b).bit_count()==1
        assert a not in used and b not in used
        used.update((a,b)); required.add(tuple(sorted((a,b))))
    assert u not in used
    p=c['path']; assert len(p)==size and set(p)==set(range(size))
    assert p[0]==u and p[-1]==v
    edges=set()
    for a,b in zip(p,p[1:]):
        assert (a^b).bit_count()==1
        edges.add(tuple(sorted((a,b))))
    assert required<=edges

if __name__=='__main__':
    file=Path(sys.argv[1]); data=json.loads(file.read_text(encoding='utf8'))
    count=0
    for c in data['cases']:
        if c['status']=='FOUND':check(c);count+=1
    print(json.dumps({'verified_paths':count,'total_cases':len(data['cases']),
                      'sha256':hashlib.sha256(file.read_bytes()).hexdigest()}))
