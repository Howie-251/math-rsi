"""Independent full positive-path audit and perfect-endpoint dependency rebuild."""
import collections,hashlib,itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
V=set(range(16));ODD={x for x in V if x.bit_count()%2};EVEN=V-ODD

def edges(m):return {tuple(sorted((x,y))) for x,y in enumerate(m) if y!=255}
def validate(m,H):
 assert len(m)==16 and {x for x in V if m[x]==255}==H
 assert all(m[x] in V-H and m[x]!=x and m[m[x]]==x for x in V-H)
def pairings(vertices):
 m=[255]*16
 def rec(v):
  if not v:yield bytes(m);return
  x=v[0]
  for j,y in enumerate(v[1:],1):
   m[x]=y;m[y]=x
   yield from rec(v[1:j]+v[j+1:])
   m[x]=m[y]=255
 yield from rec(tuple(vertices))
def verifywalk(seq,allowed,M,cycle):
 assert len(seq)==len(set(seq))==len(allowed) and set(seq)==allowed
 pairs=list(zip(seq,seq[1:]))
 if cycle:pairs.append((seq[-1],seq[0]))
 es={tuple(sorted(e)) for e in pairs};assert M<=es
 assert all((x^y).bit_count()==1 for x,y in es-M)

def prove_negative(m,H):
 # Enumerate every disjoint short complementary perfect matching.
 c=[255]*16;leaves=0
 def rec(left):
  nonlocal leaves
  if not left:
   leaves+=1;unseen=set(V-H);components=0
   while unseen:
    components+=1;stack=[unseen.pop()]
    while stack:
     x=stack.pop()
     for y in (m[x],c[x]):
      if y in unseen:unseen.remove(y);stack.append(y)
   assert components>1
   return
  x=min(left)
  for j in range(4):
   y=x^(1<<j)
   if y in left and y!=m[x]:
    c[x]=y;c[y]=x;rec(left-{x,y});c[x]=c[y]=255
 rec(V-H)
 return leaves

def main():
 files=[];negative={};negative_completions=0
 for p in (1,7):
  name=f'q4_distance{p.bit_count()}_avoided_table.bin';data=(ROOT/name).read_bytes()
  assert len(data)==135135*30
  seen=set();neg=[];positive=0
  for off in range(0,len(data),30):
   m=data[off:off+16];c=data[off+16:off+30];validate(m,{0,p})
   assert m not in seen;seen.add(m)
   if c==bytes([255])*14:
    negative_completions+=prove_negative(m,{0,p});neg.append(edges(m))
   else:verifywalk(c,V-{0,p},edges(m),True);positive+=1
  assert seen==set(pairings(sorted(V-{0,p})))
  assert len(neg)==(51 if p==1 else 53)
  negative[p]=neg
  files.append({'file':name,'records':len(seen),'positive_cycles':positive,'certified_negative':len(neg),'sha256':hashlib.sha256(data).hexdigest()})
 transforms=[tuple(sum(((x>>p[j])&1)<<j for j in range(4)) for x in range(16)) for p in itertools.permutations(range(4))]
 neg_for={}
 for y in ODD:
  source=1 if y.bit_count()==1 else 7
  tr=next(tr for tr in transforms if tr[source]==y)
  neg_for[y]={frozenset(tuple(sorted((tr[a],tr[b]))) for a,b in M) for M in negative[source]}
 candidates={}
 for y,tables in neg_for.items():
  for M in tables:
   for a,b in M:
    for u,w in ((a,b),(b,a)):
     P=frozenset((set(M)-{(a,b)})|{tuple(sorted((0,u))),tuple(sorted((y,w)))})
     assert len(P)==8 and sorted(x for e in P for x in e)==list(range(16))
     candidates[P]=None
 assert len(candidates)==4708
 imported=json.loads((ROOT/'q4_perfect_endpoint_abundance_check.json').read_text())
 stored={frozenset(tuple(e) for e in r['matching']):set(r['bad_odd_endpoints']) for r in imported['all_exceptional_matchings']}
 assert set(stored)==set(candidates)
 hist=collections.Counter();badsets=[]
 for M in candidates:
  mate={x:y for a,b in M for x,y in ((a,b),(b,a))};bad=set()
  for y in ODD:
   if mate[0]==y:bad.add(y);continue
   a,b=mate[0],mate[y]
   T=frozenset(set(M)-{tuple(sorted((0,a))),tuple(sorted((y,b)))}|{tuple(sorted((a,b)))})
   if T in neg_for[y]:bad.add(y)
  assert bad==stored[M] and len(bad)<=4
  badsets.append(bad);hist[len(bad)]+=1
 units=[1,2,4,8]
 triples={frozenset(t) for t in itertools.combinations(units,3)}
 for a,b in itertools.combinations(units,2):
  for c in set(units)-{a,b}:triples.add(frozenset((a,b,a^b^c)))
 assert len(triples)==16 and all(not t<=bad for t in triples for bad in badsets)
 histogram=collections.Counter();lowsets=collections.Counter();paths=0
 pathfiles=[]
 for p in (3,15):
  for b,t in itertools.combinations(sorted(EVEN-{0,p}),2):
   name=f'q4_t44_path_abundance_{p}_{b}_{t}.bin';data=(ROOT/name).read_bytes()
   pos=0;seen=set();localhist=collections.Counter()
   while pos<len(data):
    m=data[pos:pos+16];count=data[pos+16];pos+=17;validate(m,{0,p,b,t})
    assert m not in seen;seen.add(m);S=set();M=edges(m)
    for _ in range(count):
     seq=data[pos:pos+14];pos+=14
     verifywalk(seq,V-{0,p},M,False)
     assert seq[0]==b and seq[-1] in ODD and seq[-1] not in S
     S.add(seq[-1])
    assert len(S)==count
    relative=frozenset(q^b for q in S)
    assert count>=5 or any(tr<=relative for tr in triples)
    if count<=4:
     assert all(not relative<=bad for bad in badsets)
     lowsets[tuple(sorted(relative))]+=1
    histogram[count]+=1;localhist[count]+=1;paths+=count
   assert pos==len(data) and seen==set(pairings(sorted(V-{0,p,b,t})))
   pathfiles.append({'file':name,'records':len(seen),'paths':sum(k*n for k,n in localhist.items()),'sha256':hashlib.sha256(data).hexdigest()})
 assert len(pathfiles)==30 and sum(histogram.values())==311850 and paths==2486610
 assert histogram=={3:180,4:36,5:10,6:1040,7:5036,8:305548}
 assert sum(lowsets.values())==216 and len(lowsets)==13
 result={'status':'PASS','perfect_endpoint_dependency':{'files':files,'negative_short_completions_checked':negative_completions,'exceptions_reconstructed':4708,'bad_endpoint_histogram':dict(hist),'imported_json_exactly_matches_rebuilt_exceptions':True,'hitting_triples':sorted(map(sorted,triples))},'path_files':pathfiles,'records':sum(histogram.values()),'positive_paths':paths,'endpoint_histogram':dict(histogram),'low_records':sum(lowsets.values()),'distinct_low_endpoint_sets':len(lowsets),'low_sets':[{'set':list(s),'count':n} for s,n in sorted(lowsets.items())],'proof_sha256':hashlib.sha256((ROOT/'T44_SAMEFACE_ZERO_CROSSING.md').read_bytes()).hexdigest(),'full_T44_5_proved':False,'full_T15_proved':False,'R8_covered_proved':False,'full_P6_proved':False}
 (ROOT/'T44_SAMEFACE_ZERO_CROSSING_REVIEW_check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k not in ('perfect_endpoint_dependency','path_files','low_sets')}),flush=True)

if __name__=='__main__':main()
