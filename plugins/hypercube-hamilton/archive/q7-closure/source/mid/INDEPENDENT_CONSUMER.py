"""Independent E38 raw-face and author record consumer; no author execution."""
from pathlib import Path
import collections,hashlib,json,struct
P=Path(__file__).resolve().parent
R=P.parents[2]
A=P.parent/'high'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(name,obj):(P/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
def read(p):return json.loads(p.read_bytes())
def verts(mask):return [v for v in range(64) if mask>>v&1]
E=[v for v in range(64) if v.bit_count()%2==0]
O=[v for v in range(64) if v.bit_count()%2]
def physical(mask,labels):return sum(1<<labels[i] for i in range(32) if mask>>i&1)
def delta(u,y):return [sum(1 for v in verts(u) if not(v>>j&1))-sum(1 for v in verts(y) if not(v>>j&1)) for j in range(6)]
author=collections.defaultdict(dict)
for line in (A/'FACE19_ALL.jsonl').read_text().splitlines():
 z=json.loads(line);r=z['r'];key=(physical(z['even_mask'],E),physical(z['odd_mask'],O))
 assert z['id'] not in author[r]
 author[r][z['id']]=key
checks=[]
for r in range(6,10):
 b=(P/f'R{r}_RAW.bin').read_bytes();assert len(b)%16==0
 raw=list(struct.iter_unpack('<QQ',b));assert raw==sorted(set(raw))
 assert len(raw)==len(author[r]) and set(raw)==set(author[r].values())
 for u,y in raw:
  assert u.bit_count()==r and y.bit_count()==19-r
  assert set(verts(u))<=set(E) and set(verts(y))<=set(O)
  assert all((v^w).bit_count()!=1 for v in verts(u) for w in verts(y))
 checks.append(dict(r=r,raw_faces=len(raw),exact_author_set=True,raw_sha256=sha(P/f'R{r}_RAW.bin')))
hist=collections.defaultdict(collections.Counter);n=collections.Counter();weighted=collections.defaultdict(collections.Counter)
sizes=collections.Counter()
for line in (A/'FACE19_ALL.jsonl').read_text().splitlines():
 z=json.loads(line);sizes[z['r'],z['orbit']]+=1
orbit_by_id={}
for line in (A/'FACE19_ALL.jsonl').read_text().splitlines():
 z=json.loads(line);orbit_by_id[z['r'],z['id']]=z['orbit']
seen=set()
for line in (A/'FACE19_COMPATIBLE.jsonl').read_text().splitlines():
 z=json.loads(line);r=z['r'];a=z['a_id'];b=z['b_id'];assert (r,a,b) not in seen;seen.add((r,a,b))
 u,y=author[r][a];v,w=author[r][b];assert not(u&v or y&w)
 H=verts(u)+verts(y)+[x+64 for x in verts(v)]+[x+64 for x in verts(w)]
 assert len(set(H))==38 and sum(x.bit_count()%2 for x in H)==19
 assert all((x^y).bit_count()!=1 for x in H for y in H if x!=y)
 d=[sum((1 if x.bit_count()%2==0 else -1) for x in H if not(x>>j&1)) for j in range(7)]
 assert d==z['delta'] and max(map(abs,d))==z['max_abs'] and z['max_abs']>7
 n[r]+=1;hist[r][z['max_abs']]+=1;weighted[r][z['max_abs']]+=sizes[r,orbit_by_id[r,a]]
for t in read(A/'FACE19_RESULT.json')['tiers']:
 r=t['r'];raw=read(P/f'R{r}_RESULT.json')
 assert t['faces']==len(author[r]) and t['compatible_pairs']==n[r]
 assert {int(k):v for k,v in t['max_abs_histogram'].items()}==dict(hist[r])
 assert {int(k):v for k,v in raw['histogram'].items()}==dict(weighted[r])
 assert raw['ordered_independent_pairs']==sum(weighted[r].values())
 assert raw['min_max_abs_delta']==t['min_max_abs_delta'] and raw['bad']==0
dump('AUTHOR_GEOMETRY_CONSUMED.json',dict(status='PASS',raw_complete_set_checks=checks,author_actual_pairs_consumed=sum(n.values()),weighted_all_raw_pairs=sum(sum(x.values()) for x in weighted.values()),weighted_histograms={str(r):dict(h) for r,h in weighted.items()}))
bindings=[R/'seven_directions/e36_2026_11_19/E36_COMPLETE_AUTHOR_BINDING.json',R/'seven_directions/e36_2026_11_19/mid/review_complete/REVIEW_BINDING.json']
allitems={};reports=[]
for binding in bindings:
 d=read(binding);count=0;total=0
 for z in d['items']:
  p=Path(z['path']);p=p if p.is_absolute() else R/p
  b=p.read_bytes();assert len(b)==z['bytes'] and hashlib.sha256(b).hexdigest()==z['sha256'],str(p)
  count+=1;total+=len(b);allitems[str(p)]=dict(path=str(p),bytes=len(b),sha256=z['sha256'])
 reports.append(dict(path=str(binding),sha256=sha(binding),count=count,total_bytes=total))
dump('E36_COMPLETE_IMPORT_ACTUAL_CHECK.json',dict(status='PASS',bindings=reports,unique_items=len(allitems),imports=list(allitems.values())))
print('PASS raw35360 author7608 completeE36 author1182/review1190')
