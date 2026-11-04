"""Independent finite checks of new restriction/kernel mechanism and frozen boundary."""
import pathlib,json,hashlib
Rdir=pathlib.Path(__file__).resolve().parent
def sha(n):return hashlib.sha256((Rdir/n).read_bytes()).hexdigest()
m=json.loads((Rdir/'TWELVE_MIXED_HALF_LAYER_MANIFEST.json').read_text())
for n,h in m['files'].items():assert sha(n)==h,n
H={0,1,3,31};U={0,31};K=set(range(32))-H;fixed=((4,6),(8,10),(13,15),(16,18),(21,23),(25,27),(28,30));L=K-{x for e in fixed for x in e}
assert len(K)==28 and len(L)==14 and len({x for e in fixed for x in e})==14
oddhalf={tuple(sorted((x,x^2))) for x in range(32) if not x&2 and x.bit_count()%2}
assert oddhalf==set(fixed)|{(1,3)} and not U&{x for e in oddhalf for x in e}
assert list(map(int,(Rdir/'TWELVE_ROOT_STAR_MIXED_probe_config.txt').read_text().split()))==[0,1,3,31,0,31]
degrees={x:0 if x in U else 2 if x in H else 1 for x in range(32)}
assert sum(degrees[x] for x in range(32) if not x&2 and x.bit_count()%2)==9
assert sum(degrees[x] for x in range(32) if not x&2 and x.bit_count()%2==0)==7
def matchings(vertices):
 if not vertices:yield ();return
 a,*rest=vertices
 for i,b in enumerate(rest):
  for sub in matchings(rest[:i]+rest[i+1:]):yield ((a,b),)+sub
def conn(P,F):
 adj={x:[] for e in P+F for x in e}
 for a,b in P+F:adj[a].append(b);adj[b].append(a)
 seen=set();todo=[next(iter(adj))]
 while todo:
  x=todo.pop()
  if x not in seen:seen.add(x);todo.extend(adj[x])
 return len(seen)==len(adj)
def compress(P,fixed,terminals):
 adj={x:[] for e in P+fixed for x in e}
 for a,b in P+fixed:adj[a].append(b);adj[b].append(a)
 seen=set();pairs=[]
 for a in terminals:
  if a in seen:continue
  previous=None;x=a;path=set()
  while True:
   path.add(x);nexts=[y for y in adj[x] if y!=previous]
   if x!=a and x in terminals:break
   assert len(nexts)==1
   previous,x=x,nexts[0]
  pairs.append((a,x));seen|=path
 if seen!=set(adj):return None # leftover cycles, including labelled shared edges
 return tuple(pairs)
def rank(rows):
 basis={}
 for x in rows:
  while x:
   p=x.bit_length()-1
   if p not in basis:basis[p]=x;break
   x^=basis[p]
 return len(basis)
cases=[];entrychecks=0;separatorchecks=0;liftchecks=0
for n,r in [(6,1),(8,1),(8,2),(8,3)]:
 allP=list(matchings(list(range(n))));fixedsmall=tuple((2*i,2*i+1) for i in range(r));terminals=list(range(2*r,n));allG=list(matchings(terminals))
 rows=[]
 for P in allP:
  compressed=compress(P,fixedsmall,terminals);bits=0
  for j,G in enumerate(allG):
   actual=conn(P,fixedsmall+G);expected=False if compressed is None else conn(compressed,G)
   assert actual==expected
   bits|=int(actual)<<j;entrychecks+=1
  rows.append(bits)
 expectedrank=1<<(len(terminals)//2-1);assert rank(rows)==expectedrank
 for G in allG:
  a,b=G[0];lift=[];current=a
  for p,q in fixedsmall:lift.append((current,p));current=q
  lift.append((current,b));lift.extend(G[1:]);lift=tuple(lift)
  assert set(x for e in lift for x in e)==set(range(n)) and len({x for e in lift for x in e})==n
  assert {frozenset(e) for e in compress(lift,fixedsmall,terminals)}=={frozenset(e) for e in G};liftchecks+=1
 for F in allP:
  FS={frozenset(e) for e in F}
  missing=[e for e in fixedsmall if frozenset(e) not in FS]
  for p,q in missing:
   mate={a:b for x,y in F for a,b in [(x,y),(y,x)]};a,b=mate[p],mate[q]
   ordered=[(a,p),(q,b)]+[e for e in F if p not in e and q not in e]
   P=tuple((ordered[i][1],ordered[(i+1)%len(ordered)][0]) for i in range(len(ordered)))
   assert frozenset((p,q)) in {frozenset(e) for e in P} and conn(P,F)
   assert all(not conn(P,fixedsmall+G) for G in allG);separatorchecks+=1
 cases.append({'terminals':n,'fixed_R_pairs':r,'bad_restriction_rank':rank(rows),'expected_rank':expectedrank})
out={'status':'PASS','frozen_hashes_checked':len(m['files']),'half_layer_exact_R_plus_1_3':True,'retained_A_odd_degree':9,'retained_A_even_degree':7,'bad_terminal_count':14,'ambient_terminal_count':28,'ambient_rank':8192,'bad_column_restriction_rank':64,'kernel_dimension':8128,'small_restriction_compression_entries_checked':entrychecks,'small_all_row_lifts_checked':liftchecks,'small_separator_constructions_checked':separatorchecks,'small_cases':cases,'all_frozen_hashes':m['files']}
(Rdir/'TWELVE_MIXED_HALF_LAYER_REVIEW_math.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='all_frozen_hashes'},indent=2))
