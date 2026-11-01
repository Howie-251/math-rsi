from twentyone_five import dual
from quad_general import *
start=time.time();out=[]
for ds,ls in [((5,7,7,7),(1,1,1,2,2,2))]+[((5,7,7,8),(1,1,1,2,a,b)) for a in (1,2) for b in (1,2)]+[((5,7,8,8),(1,1,1,a,b,c)) for a in (1,2) for b in (1,2) for c in range(1,9)]:
 for counts,q,t3 in profiles(ds,ls):
  # three sevens: all in one x edge; two sevens: same x edge, eight outside.
  if ds==(5,7,7,7) and q!=1:continue
  if ds==(5,7,7,8):
   l=lambda m:sum(n for t,n in counts.items() if t&m==m)
   if l(7)!=1 or l(11)!=0 or l(13)!=0:continue
  if ds==(5,7,8,8):
   l=lambda m:sum(n for t,n in counts.items() if t&m==m)
   if l(7)!=0 or l(11)!=0:continue # eights outside x/y common edge
  opts=[]
  for k in (9,8,10,7,11):
   for pp in permutations(range(k,k+4)):
    p=Profile(21,5,pp,counts);cs=[dual(p,i) for i in range(4)];rs=rows(p,deductions={pp[i]:cs[i]['loss'] for i in range(4)})
    rr=dict(v=21,ds=ds,ls=ls,q=q,t3=t3,counts=counts,pos=pp,cs=cs,rows=rs,bound=total_bound(rs));opts.append(rr)
    if rr['bound']<1:break
   if opts[-1]['bound']<1:break
  r=min(opts,key=lambda x:x['bound']);out.append(r);print(ds,ls,q,t3,r['bound'],flush=True)
Path(__file__).with_name('TWENTYONE_FIVE_SEVENS.json').write_text(json.dumps(json_value(dict(cases=out,seconds=time.time()-start)),indent=2))
print('PASS',sum(r['bound']<1 for r in out),'/',len(out),'seconds',time.time()-start)
