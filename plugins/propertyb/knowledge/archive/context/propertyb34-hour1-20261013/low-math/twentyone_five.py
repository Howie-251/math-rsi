from quad_general import *
from avoided_lock_quotas import certificate as original_dual
def dual(p,i):
 bit=1<<i;qs=[max(0,(4*sum(c for t,c in p.counts.items() if t&bit and not t&R)-(p.v-1-R.bit_count())+2)//3) for R in range(16) if not R&bit]
 return original_dual(p,i) if max(qs)>0 else dict(loss=Fraction(0),dual=[],inventory=[],note='all quota zero')
def main():
 start=time.time();out=[]
 for ds in [(5,8,8,8)]:
  for ll in product((1,2),repeat=3):
   ls=(1,1,1)+ll
   for counts,q,t3 in profiles(ds,ls):
    options=[]
    for k in (9,8,10,7,11):
     for pp in permutations(range(k,k+4)):
      p=Profile(21,5,pp,counts);cs=[dual(p,i) for i in range(4)];rs=rows(p,deductions={pp[i]:cs[i]['loss'] for i in range(4)})
      rr=dict(v=21,ds=ds,ls=ls,q=q,t3=t3,counts=counts,pos=pp,cs=cs,rows=rs,bound=total_bound(rs));options.append(rr)
      if rr['bound']<1:break
     if options[-1]['bound']<1:break
    r=min(options,key=lambda z:z['bound']);out.append(r);print(ls,q,t3,r['bound'],flush=True)
 Path(__file__).with_name('TWENTYONE_FIVE_QUAD.json').write_text(json.dumps(json_value(dict(cases=out,seconds=time.time()-start)),indent=2))
 print('PASS',sum(r['bound']<1 for r in out),'/',len(out),'seconds',time.time()-start)

if __name__=="__main__":main()
