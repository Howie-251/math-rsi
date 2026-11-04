"""Cross-check the C++ search against an independent exhaustive Q3 path table."""
import json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parent
n=3;N=8
es=[(a,b) for a in range(N) for b in range(a+1,N) if (a^b).bit_count()==1]
paths={v:[] for v in range(N) if v.bit_count()%2}
def visit(p,used):
    if len(p)==N:
        paths[p[-1]].append({tuple(sorted(e)) for e in zip(p,p[1:])});return
    for y in range(N):
        if y not in used and (y^p[-1]).bit_count()==1:visit(p+[y],used|{y})
visit([0],{0})
ms=[]
def gen(i,used,m):
    if i==len(es):ms.append(m);return
    gen(i+1,used,m)
    a,b=es[i]
    if a not in used and b not in used:gen(i+1,used|{a,b},m+[es[i]])
gen(0,set(),[])
inputs=[];expected=[]
for m in ms:
    mate=[-1]*N
    for a,b in m:mate[a]=b;mate[b]=a
    for v in paths:
        inputs.append(' '.join(map(str,[n,v,1000000,*mate])))
        expected.append(any(set(m)<=p for p in paths[v]))
p=subprocess.run([str(ROOT/'path_search.exe')],input='\n'.join(inputs)+'\n',text=True,capture_output=True,check=True)
lines=p.stdout.splitlines();assert len(lines)==len(expected)
for line,want in zip(lines,expected):assert line.split()[0]==('FOUND' if want else 'EXHAUSTED')
unknown=subprocess.run([str(ROOT/'path_search.exe')],input='3 1 0 '+' '.join(['-1']*8)+'\n',text=True,capture_output=True,check=True)
assert unknown.stdout.startswith('UNKNOWN')
result={'all_Q3_matchings':len(ms),'endpoint_cases':len(expected),'positive':sum(expected),'negative':len(expected)-sum(expected),'node_limit_returns_UNKNOWN':True}
(ROOT/'search_tests.json').write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps(result))
