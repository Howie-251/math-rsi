from probe import *
from avoided_lock_quotas import certificate as dual
start=time.time();out=[]
for idx,r in enumerate(json.load(open(Path(__file__).with_name('ONE7_REMAINING.json')))['canonical']):
 counts={int(t):n for t,n in r['counts'].items()};options=[]
 for pp in [pp for k in range(5,14) for pp in permutations(range(k,k+4))]:
  p=Profile(20,5,pp,counts);cs=[dual(p,i) for i in range(4)]
  rs=rows(p,deductions={pp[i]:cs[i]['loss'] for i in range(4)})
  row=dict(index=idx,old_indices=r['indices'],v=20,ds=(7,8,8,8),counts=counts,pos=pp,cs=cs,rows=rs,bound=total_bound(rs));options.append(row)
  if row['bound']<1:break
 bestrow=min(options,key=lambda r:r['bound']);out.append(bestrow)
 print(idx,len(options),bestrow['pos'],bestrow['bound'],flush=True)
Path(__file__).with_name('ONE7_POSITION_REFINEMENT.json').write_text(json.dumps(json_value(dict(seconds=time.time()-start,cases=out)),indent=2))
print('seconds',time.time()-start)
