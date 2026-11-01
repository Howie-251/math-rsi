from probe import *
start=time.time();out=[]
def independent(r):
 stubs=[frozenset(i+1 for i in range(len(r['ds'])) if int(t)&(1<<i)) for t,c in r['counts'].items() for _ in range(c)]
 for a,b in zip(r['rows'],independent_rows(20,r['pos'],stubs)):
  for term in ('A','B','C'):assert a[term]==b[term]
 r['independent_ABC_check']=True
for ds in [(7,7),(7,8),(8,8)]:
 for lam in range(4,min(ds)+1):
  r=best(20,ds,(lam,));assert r['bound']<1;independent(r);out.append(r)
for r in json.load(open(Path(__file__).with_name('TRIPLE_SCAN.json'))):
 if r['ds']==[7,7,8] and (r['ls'][0]==3 or (r['ls'][0]==2 and not ((r['ls'][1:]==[1,1] and r['t']==0) or r['ls'][1:]==[2,2]))):
  rr=calc(20,r['ds'],r['ls'],r['t'],r['pos']);assert rr['bound']<1;independent(rr);out.append(rr)
source=json.load(open(Path(__file__).with_name('QUAD_MIXED.json')))['cases']
duals={r['index']:r for r in json.load(open(Path(__file__).with_name('DUAL_REFINEMENT.json')))['cases'] if r['source']=='QUAD_MIXED.json'}
residual=[]
for idx,r in enumerate(source):
 if r['ds']!=[7,7,8,8]:continue
 rr=r;typ='pure'
 if Fraction(r['bound'])>=1:
  rr=duals[idx];typ='avoided_dual'
 if Fraction(rr['bound'])>=1:
  assert r['ls']==[2,1,1,1,1,2] and r['t4']==0 and r['t3']==[0,0,0,0]
  residual.append(dict(index=idx,profile=r));continue
 p=Profile(20,5,rr['pos'],{int(k):v for k,v in rr['counts'].items()})
 cs=rr['cs'];losses=[]
 if typ=='pure':
  cc=[certificate(p,i) for i in range(4)];losses=[c['loss'] for c in cc]
 else:
  cc=[]
  for i,c in enumerate(cs):
   bit=1<<i;k=p.positions[i];main=Fraction();penalty=Fraction()
   for d in c['dual']:
    R=d['avoid'];alpha=Fraction(d['alpha']);assert alpha>=0 and R&bit==0
    count=sum(n for t,n in p.counts.items() if t&bit and not t&R)
    q=max(0,(4*count-(p.v-1-R.bit_count())+2)//3)
    assert count==d['edge_count'] and q==d['q'];main+=alpha*q
   for z in c['inventory']:
    t,u=z['t'],z['u'];cap=p.counts[t]*(p.counts[t]-1)//2 if t==u else p.counts[t]*p.counts[u]
    from multilock import pair_weight
    weight=pair_weight(20,5,p.positions,t,u,k)+pair_weight(20,5,p.positions,u,t,k)
    assert cap==z['capacity'] and weight==Fraction(z['weight'])
    threshold=sum((Fraction(d['alpha']) for d in c['dual'] if not (t|u)&d['avoid']),Fraction())
    penalty+=cap*max(Fraction(),threshold-weight)
   loss=max(Fraction(),main-penalty);assert loss==Fraction(c['loss']);losses.append(loss);cc.append(c)
 rs=rows(p,deductions={p.positions[i]:losses[i] for i in range(4)})
 record=dict(v=20,ds=r['ds'],ls=r['ls'],t4=r['t4'],t3=r['t3'],counts=p.counts,pos=p.positions,certificate_kind=typ,cs=cc,rows=rs,bound=total_bound(rs))
 assert record['bound']==Fraction(rr['bound'])<1;independent(record);out.append(record)
assert len(residual)==1
Path(__file__).with_name('SEVEN_TWO_VERIFIED.json').write_text(json.dumps(json_value(dict(seconds=time.time()-start,cases=out,residual=residual)),indent=2))
print('strict witnesses',len(out),'residual',len(residual),'maximum',max(r['bound'] for r in out),'seconds',time.time()-start)
