"""Verify T63 witnesses, full input coverage, and every negative analytically.
Independent of the producer and its Hamilton search.
"""
import itertools,json,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
V=set(range(16));E={x for x in V if x.bit_count()%2==0};O=V-E

def edge(a,b):return tuple(sorted((a,b)))
def allmatchings(v):
 if not v:yield frozenset();return
 a=min(v)
 for b in sorted(v-{a}):
  for F in allmatchings(v-{a,b}):yield F|{edge(a,b)}
def short(a,b):return (a^b).bit_count()==1
rows=[];cover=set();negcount=poscount=0
manifest=json.loads((P/'A8_Q4_T63_manifest.json').read_text())
for row in manifest['rows']:
 h=set(row['holes']);f=set(row['forbidden']);assert len(h)==6 and h<=E and len(f)==3 and f<=h
 domain=set(allmatchings(V-h));assert len(domain)==945
 raw=(P/row['file']).read_bytes();assert len(raw)==945*29
 pos=neg=0
 for k in range(945):
  rec=raw[29*k:29*k+29];m=rec[:16];c=rec[16:]
  assert {i for i in V if m[i]==255}==h
  assert all(m[i] in V-h and m[i]!=i and m[m[i]]==i for i in V-h)
  F=frozenset(edge(i,m[i]) for i in V-h if i<m[i]);assert F in domain;domain.remove(F)
  obstacles=[]
  for a in O:
   neighbors={x for x in V-f if short(a,x)}
   if len(neighbors)==1:
    b=next(iter(neighbors))
    if edge(a,b) in F:obstacles.append((a,b))
  if c==bytes([255])*13:
   assert obstacles;neg+=1
  else:
   assert not obstacles and len(c)==len(set(c))==13 and set(c)==V-f
   CE={edge(a,b) for a,b in zip(c,c[1:]+c[:1])}
   assert len(CE)==13 and F<=CE and all(short(a,b) for a,b in CE-F);pos+=1
 assert not domain and pos==row['positive'] and neg==row['negative']
 orbit=set()
 for shift in E:
  for perm in itertools.permutations(range(4)):
   def tr(x):return sum((((x^shift)>>i)&1)<<perm[i] for i in range(4))
   orbit.add((tuple(sorted(map(tr,h))),tuple(sorted(map(tr,f)))))
 assert len(orbit)==row['orbit'] and not orbit&cover;cover|=orbit
 rows.append(dict(file=row['file'],positive=pos,negative=neg,orbit=len(orbit),sha256=hashlib.sha256(raw).hexdigest()))
 poscount+=pos;negcount+=neg
assert cover=={(h,f) for h in itertools.combinations(sorted(E),6) for f in itertools.combinations(h,3)}
result=dict(status='PASS',scope='Q4 six same-parity holes, three prescribed avoided holes; complete exact classification by degree obstruction',geometries=len(cover),orbits=len(rows),records=poscount+negcount,positive=poscount,negative=negcount,rows=rows,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),fresh_proof_checker_review_pending=True)
(P/'A8_Q4_T63_verified.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
