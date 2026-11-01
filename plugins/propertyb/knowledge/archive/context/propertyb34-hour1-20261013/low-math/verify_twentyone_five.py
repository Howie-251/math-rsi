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
for lam in range(3,9):
 for t in (0,1):
  rr=best(21,(5,8,8),(1,1,lam),t)
  if rr:audit(rr,'pure')
low=json.load(open(Path(__file__).with_name('TWENTYONE_FIVE_LOW.json')))['cases'];failed_low=[]
for r in low:
 if Fraction(r['bound'])<1:audit(r,'pure')
 else:failed_low.append(dict(ds=r['ds'],ls=r['ls'],t=r['t'],bound=r['bound']))
quad=json.load(open(Path(__file__).with_name('TWENTYONE_FIVE_QUAD.json')))['cases'];failed_quad=[]
for r in quad:
 if Fraction(r['bound'])<1:audit(r,'dual')
 else:
  assert r['q']==0;failed_quad.append(dict(ls=r['ls'],q=r['q'],t3=r['t3'],bound=r['bound']))
sevens=json.load(open(Path(__file__).with_name('TWENTYONE_FIVE_SEVENS.json')))['cases'];failed_seven=[]
for r in sevens:
 if r['ds']==[5,7,8,8] and r['ls'][-1]>2:continue
 if Fraction(r['bound'])<1:audit(r,'dual')
 else:
  assert r['ds']==[5,7,8,8] and r['ls']==[1,1,1,1,1,2] and r['q']==0 and r['t3']==[0,0,0,0]
  failed_seven.append(dict(ds=r['ds'],ls=r['ls'],q=r['q'],t3=r['t3'],bound=r['bound']))
assert len(failed_quad)==5 and len(failed_seven)==1
result=dict(scope='Full 21-vertex degree-five candidate: exact local arithmetic and actual selected profile coverage; not Lean',seconds=time.time()-start,witnesses=witnesses,residual_low=failed_low,residual_5888=failed_quad,residual_sevens=failed_seven)
Path(__file__).with_name('TWENTYONE_FIVE_VERIFIED.json').write_text(json.dumps(json_value(result),indent=2))
print('strict witnesses',len(witnesses),'residual_5888',len(failed_quad),'residual_sevens',len(failed_seven),'seconds',time.time()-start)
