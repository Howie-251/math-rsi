"""Independent verification of lifted Hamilton cycles; no generator imports."""
import json,sys
from pathlib import Path
data=json.loads(Path(sys.argv[1]).read_text(encoding='utf8'))
for c in data['examples']:
    n=c['n'];p=c['cycle'];size=1<<n
    assert len(p)==size and set(p)==set(range(size))
    cycle=set()
    for a,b in zip(p,p[1:]+p[:1]):
        assert (a^b).bit_count()==1
        cycle.add(tuple(sorted((a,b))))
    covered=set();directions=set()
    for a,b in c['matching']:
        assert 0<=a<size and 0<=b<size and (a^b).bit_count()==1
        assert a not in covered and b not in covered
        covered.update((a,b));directions.add(a^b)
        assert tuple(sorted((a,b))) in cycle
    assert len(directions)==6
    print(json.dumps({'n':n,'vertices':size,'matching_edges':len(c['matching']),'directions':len(directions),'verified':True}))
