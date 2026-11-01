from probe import *
from avoided_lock_quotas import certificate as original_dual
def dual(p,i):
 bit=1<<i
 qs=[max(0,(4*sum(c for t,c in p.counts.items() if t&bit and not t&R)-(p.v-1-R.bit_count())+2)//3) for R in range(1<<len(p.positions)) if not R&bit]
 return original_dual(p,i) if max(qs)>0 else dict(loss=Fraction(0),dual=[],inventory=[],note="all quota zero")
start=time.time();out=[]
for file in ['FULL588.json','FIVE_77888.json','QUAD_ONE7.json','QUAD_MIXED.json']:
 data=json.load(open(Path(__file__).with_name(file)));source=data.get('cases',[data.get('best')])
 for idx,r in enumerate(source):
  if Fraction(r['bound'])<1:continue
  p=Profile(r['v'] if 'v' in r else 20,5,r['pos'],{int(k):v for k,v in r['counts'].items()});cs=[dual(p,i) for i in range(len(p.positions))]
  rs=rows(p,deductions={p.positions[i]:cs[i]['loss'] for i in range(len(p.positions))});b=total_bound(rs)
  rr=dict(source=file,index=idx,old_bound=r['bound'],v=p.v,ds=r.get('ds'),pos=p.positions,counts=p.counts,cs=cs,rows=rs,bound=b);out.append(rr)
  print(file,idx,r['bound'],'->',b,flush=True)
Path(__file__).with_name('DUAL_REFINEMENT.json').write_text(json.dumps(json_value(dict(seconds=time.time()-start,cases=out)),indent=2))
print('seconds',time.time()-start)
