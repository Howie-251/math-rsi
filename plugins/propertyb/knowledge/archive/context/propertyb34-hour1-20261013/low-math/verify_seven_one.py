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
for ds in [(7,8),(8,8)]:
 for lam in range(4,min(ds)+1):audit(best(20,ds,(lam,)),'pure')
source=json.load(open(Path(__file__).with_name('QUAD_ONE7.json')))['cases']
duals={r['index']:r for r in json.load(open(Path(__file__).with_name('DUAL_REFINEMENT.json')))['cases'] if r['source']=='QUAD_ONE7.json'}
triples=json.load(open(Path(__file__).with_name('TRIPLE_SCAN.json')))
lookup={(tuple(r['ds']),tuple(r['ls']),r['t']):r for r in triples}
for r in triples:
 if r['ds']==[7,8,8] and 3 in r['ls']:audit(r,'pure')
refined=json.load(open(Path(__file__).with_name('ONE7_POSITION_REFINEMENT.json')))['cases']
refmap={tuple(sorted((int(t),c) for t,c in r['counts'].items() if c)):r for r in refined}
def canonical(counts):
 opts=[]
 for perm8 in permutations((1,2,3)):
  perm=(0,)+perm8;cc=tuple(sorted((sum(1<<perm[i] for i in range(4) if t&(1<<i)),c) for t,c in counts.items() if c));opts.append((cc,perm))
 return min(opts)
residual={}
for idx,r in enumerate(source):
 counts={int(t):c for t,c in r['counts'].items()};covered=False
 for a,b in combinations(range(1,4),2):
  ls=tuple(sum(c for t,c in counts.items() if t&mask==mask) for mask in (1|(1<<a),1|(1<<b),(1<<a)|(1<<b)))
  tm=1|(1<<a)|(1<<b);tt=sum(c for t,c in counts.items() if t&tm==tm);tri=lookup[((7,8,8),ls,tt)]
  if Fraction(tri['bound'])<1:
   coverage.append(dict(index=idx,via='triple',selected=(0,a,b),witness=audit(tri,'pure')));covered=True;break
 if covered:continue
 ls888=tuple(sum(c for t,c in counts.items() if t&mask==mask) for mask in (6,10,12));tt=sum(c for t,c in counts.items() if t&14==14);tri=lookup[((8,8,8),tuple(sorted(ls888)),tt)]
 if Fraction(tri['bound'])<1:
  coverage.append(dict(index=idx,via='triple_888_relabel',selected=(1,2,3),witness=audit(tri,'pure')));continue
 if Fraction(r['bound'])<1:
  coverage.append(dict(index=idx,via='pure_quad',witness=audit(r,'pure')));continue
 if idx in duals and Fraction(duals[idx]['bound'])<1:
  coverage.append(dict(index=idx,via='dual_quad',witness=audit(duals[idx],'dual')));continue
 key,perm=canonical(counts)
 if key in refmap and Fraction(refmap[key]['bound'])<1:
  coverage.append(dict(index=idx,via='canonical_dual_quad',permutation=perm,witness=audit(refmap[key],'dual')));continue
 residual.setdefault(key,[]).append(idx);coverage.append(dict(index=idx,via='residual',permutation=perm,canonical_counts=dict(key)))
assert len(residual)==6
for key,ids in residual.items():
 c=dict(key);l=lambda m:sum(n for t,n in c.items() if t&m==m)
 print(ids,'xL',[l(1|(1<<i)) for i in range(1,4)],'LL',[l((1<<i)|(1<<j)) for i,j in combinations(range(1,4),2)],'triples',[l(m) for m in (7,11,13,14)])
result=dict(scope='Complete trace-table coverage at pairs 1/2; strict witnesses plus six structural residues; not all hypergraphs enumerated',seconds=time.time()-start,witnesses=witnesses,coverage=coverage,residual=[dict(indices=ids,counts=dict(k)) for k,ids in residual.items()])
Path(__file__).with_name('SEVEN_ONE_VERIFIED.json').write_text(json.dumps(json_value(result),indent=2))
print('witnesses',len(witnesses),'profile coverage',len(coverage),'residues',len(residual),'seconds',time.time()-start)
