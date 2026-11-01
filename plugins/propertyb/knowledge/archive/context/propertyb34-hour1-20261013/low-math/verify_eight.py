from probe import *
from multilock import pair_weight
start=time.time();witnesses=[];seen={};coverage=[]
def audit(row,kind):
 v=row.get('v',20);ds=row.get('ds',(7,8,8,8));pos=tuple(row['pos']);counts={int(t):c for t,c in row['counts'].items()};p=Profile(v,5,pos,counts)
 key=(tuple(ds),pos,tuple(sorted(counts.items())),str(row['bound']))
 if key in seen:return seen[key]
 if kind=='pure':cs=[certificate(p,i) for i in range(len(pos))];losses=[c['loss'] for c in cs]
 else:
  cs=row['cs'];losses=[]
  for i,c in enumerate(cs):
   bit=1<<i;k=pos[i];main=Fraction();penalty=Fraction()
   for d in c['dual']:
    R=d['avoid'];alpha=Fraction(d['alpha']);assert alpha>=0 and R&bit==0
    count=sum(n for t,n in counts.items() if t&bit and not t&R)
    q=max(0,(4*count-(v-1-R.bit_count())+2)//3)
    assert count==d['edge_count'] and q==d['q'];main+=alpha*q
   for z in c['inventory']:
    t,u=z['t'],z['u'];cap=counts[t]*(counts[t]-1)//2 if t==u else counts[t]*counts[u]
    weight=pair_weight(v,5,pos,t,u,k)+pair_weight(v,5,pos,u,t,k)
    assert cap==z['capacity'] and weight==Fraction(z['weight'])
    threshold=sum((Fraction(d['alpha']) for d in c['dual'] if not (t|u)&d['avoid']),Fraction())
    penalty+=cap*max(Fraction(),threshold-weight)
   loss=max(Fraction(),main-penalty);assert loss==Fraction(c['loss']);losses.append(loss)
 rs=rows(p,deductions={pos[i]:losses[i] for i in range(len(pos))});bound=total_bound(rs);assert bound==Fraction(row['bound'])<1
 stubs=[frozenset(i+1 for i in range(len(pos)) if int(t)&(1<<i)) for t,c in counts.items() for _ in range(c)]
 for a,b in zip(rs,independent_rows(v,pos,stubs)):
  for term in ('A','B','C'):assert a[term]==b[term]
 idx=len(witnesses);seen[key]=idx;witnesses.append(dict(v=v,ds=ds,pos=pos,counts=counts,kind=kind,cs=cs,rows=rs,bound=bound,independent_ABC=True));return idx
from quad_general import profiles
for lam in range(4,9):audit(best(20,(8,8),(lam,)),'pure')
triples=json.load(open(Path(__file__).with_name('TRIPLE_SCAN.json')))
lookup={}
for r in triples:
 if r['ds']==[8,8,8]:
  lookup[(tuple(r['ls']),r['t'])]=r
  if Fraction(r['bound'])<1:audit(r,'pure')
source=json.load(open(Path(__file__).with_name('EIGHT_QUAD_SCAN.json')))['cases']
duals={r['index']:r for r in json.load(open(Path(__file__).with_name('EIGHT_DUAL.json')))['cases']}
orbit={};residual=[];orbit_witness={}
for r in source:
 idx=r['index'];counts={int(t):c for t,c in r['counts'].items()}
 for perm in permutations(range(4)):
  key=tuple(sorted((sum(1<<perm[i] for i in range(4) if t&(1<<i)),c) for t,c in counts.items() if c))
  if key in orbit:assert orbit[key]==idx
  orbit[key]=idx
 if Fraction(r['bound'])<1:orbit_witness[idx]=audit(r,'pure')
 elif Fraction(duals[idx]['bound'])<1:orbit_witness[idx]=audit(duals[idx],'dual')
 else:
  l=lambda m:sum(c for t,c in counts.items() if t&m==m)
  lam=[l((1<<i)|(1<<j)) for i,j in combinations(range(4),2)];q=l(15);tt=[l(m) for m in (7,11,13,14)]
  if 3 in lam:assert q==0 and tt==[0]*4
  else:
   graph=[(i,j) for (i,j),v in zip(combinations(range(4),2),lam) if v==1];deg=sorted(sum(i in e for e in graph) for i in range(4))
   assert deg in [[0,0,0,0],[0,0,1,1],[1,1,2,2],[1,1,1,3],[2,2,2,2]]
   assert q==(1 if deg==[2,2,2,2] else 0)
  residual.append(dict(index=idx,counts=counts,lambdas=lam,common_triples=tt,common_quad=q,bound=duals[idx]['bound']))
assert len(residual)==16
allcount=filtered=0;coverage_count={};orbit_counts={}
for ls in product((1,2,3),repeat=6):
 for counts,q,t3 in profiles((8,8,8,8),ls):
  allcount+=1;skip=False
  for triple in combinations(range(4),3):
   masks=[(1<<i)|(1<<j) for i,j in combinations(triple,2)];ll=tuple(sorted(sum(c for t,c in counts.items() if t&m==m) for m in masks));m=sum(1<<i for i in triple);tt=sum(c for t,c in counts.items() if t&m==m)
   if Fraction(lookup[(ll,tt)]['bound'])<1:skip=True;break
  if skip:continue
  filtered+=1;key=tuple(sorted((t,c) for t,c in counts.items() if c));idx=orbit[key];orbit_counts[idx]=orbit_counts.get(idx,0)+1
  status='quad_strict' if idx in orbit_witness else 'residual';coverage_count[status]=coverage_count.get(status,0)+1
assert allcount==12103 and filtered==976
assert all(orbit_counts[r['index']]==r['labelled_count'] for r in source)
result=dict(scope='Exact local trace classification and strict formula witnesses; no global hypergraph enumeration or Lean proof',seconds=time.time()-start,all_profiles=allcount,after_triple_elimination=filtered,orbit_count=len(source),coverage_count=coverage_count,witnesses=witnesses,quad_witnesses=orbit_witness,residual=residual)
Path(__file__).with_name('EIGHT_VERIFIED.json').write_text(json.dumps(json_value(result),indent=2))
print('witnesses',len(witnesses),'all_profiles',allcount,'after_triples',filtered,'orbits',len(source),'residues',len(residual),'seconds',time.time()-start)
