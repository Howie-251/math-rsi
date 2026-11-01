from five_general import *
from avoided_lock_quotas import certificate as dual
start=time.time();ds=(8,)*5;out=[]
pairs=list(combinations(range(4),2));seen={};groups=[]
for bits in range(64):
 edges=[p for i,p in enumerate(pairs) if bits&(1<<i)];deg=[sum(i in p for p in edges) for i in range(4)]
 if max(deg)>2:continue
 graph=tuple(edges)
 if graph in seen:groups[seen[graph]]['labelled']+=1;continue
 idx=len(groups);groups.append(dict(edges=edges,deg=deg,labelled=1))
 for perm in permutations(range(4)):seen[tuple(sorted(tuple(sorted(perm[i] for i in p)) for p in edges))]=idx
for idx,g in enumerate(groups):
 counts={15:1};edges=g['edges'];degs=g['deg'];e=len(edges)
 for i,j in pairs:counts[(1<<i)|(1<<j)]=0 if (i,j) in edges else 1
 for i,j in edges:counts[(1<<i)|(1<<j)|16]=1
 for i in range(4):counts[(1<<i)|16]=2-degs[i];counts[1<<i]=2+degs[i]
 counts[16]=e;counts[0]=11-e
 assert sum(counts.values())==34
 bestrow=None
 for k in (8,9,7,10):
  for pp in permutations(range(k,k+5)):
   p=Profile(20,5,pp,counts);cs=[dual(p,i) for i in range(5)];rs=rows(p,deductions={pp[i]:cs[i]['loss'] for i in range(5)})
   rr=dict(index=idx,graph=g,v=20,ds=ds,counts=counts,pos=pp,cs=cs,rows=rs,bound=total_bound(rs))
   if bestrow is None or rr['bound']<bestrow['bound']:bestrow=rr
   if rr['bound']<1:break
  if bestrow['bound']<1:break
 out.append(bestrow);print(idx,edges,bestrow['pos'],bestrow['bound'],flush=True)
Path(__file__).with_name('EIGHT_EDGE_FIVE.json').write_text(json.dumps(json_value(dict(cases=out,seconds=time.time()-start,labelled=sum(g['labelled'] for g in groups))),indent=2))
print('PASS',sum(r['bound']<1 for r in out),'/',len(out),'seconds',time.time()-start)
