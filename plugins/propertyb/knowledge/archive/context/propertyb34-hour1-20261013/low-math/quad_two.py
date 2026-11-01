from probe import *
start=time.time();out=[]
# Four degree-seven locks, each pair codegree two.
for t4 in range(3):
 for t3 in product(range(3-t4),repeat=4):
  counts={15:t4};triples=[7,11,13,14]
  counts.update(dict(zip(triples,t3)))
  for i,j in combinations(range(4),2):
   mask=(1<<i)|(1<<j)
   counts[mask]=2-t4-sum(c for t,c in zip(triples,t3) if t&mask==mask)
  if min(counts.values())<0:continue
  for i in range(4):counts[1<<i]=7-sum(c for t,c in counts.items() if t&(1<<i))
  counts[0]=34-sum(counts.values())
  if min(counts.values())<0:continue
  opts=[]
  for k in range(6,13):
   for pp in permutations(range(k,k+4)):
    p=Profile(20,5,pp,counts);cs=[certificate(p,i) for i in range(4)]
    rs=rows(p,deductions={pp[i]:cs[i]['loss'] for i in range(4)})
    opts.append(dict(t4=t4,t3=t3,counts=counts,pos=pp,cs=cs,rows=rs,bound=total_bound(rs)))
  bestrow=min(opts,key=lambda r:r['bound']);out.append(bestrow)
  print(t4,t3,bestrow['pos'],bestrow['bound'],flush=True)
Path(__file__).with_name('QUAD_TWO.json').write_text(json.dumps(json_value(dict(cases=out,seconds=time.time()-start)),indent=2))
print('PASS',sum(r['bound']<1 for r in out),'of',len(out),'seconds',time.time()-start)
