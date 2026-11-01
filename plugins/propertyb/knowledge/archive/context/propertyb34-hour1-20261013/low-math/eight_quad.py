from quad_general import *
start=time.time();ds=(8,8,8,8);triples=json.load(open(Path(__file__).with_name('TRIPLE_SCAN.json')));lookup={(tuple(r['ls']),r['t']):Fraction(r['bound']) for r in triples if r['ds']==[8,8,8]}
seen={};orbits=[];allcount=0;filtered=0
for ls in product((1,2,3),repeat=6):
 for counts,q,t3 in profiles(ds,ls):
  allcount+=1;skip=False
  for triple in combinations(range(4),3):
   masks=[(1<<i)|(1<<j) for i,j in combinations(triple,2)];lams=tuple(sorted(sum(c for t,c in counts.items() if t&m==m) for m in masks));m=sum(1<<i for i in triple);tt=sum(c for t,c in counts.items() if t&m==m)
   if lookup[(lams,tt)]<1:skip=True;break
  if skip:continue
  filtered+=1;key=tuple(sorted((t,c) for t,c in counts.items() if c))
  if key in seen:orbits[seen[key]]['labelled_count']+=1;continue
  index=len(orbits);orbits.append(dict(index=index,counts=counts,q=q,t3=t3,ls=ls,labelled_count=1))
  for perm in permutations(range(4)):
   pp=tuple(sorted((sum(1<<perm[i] for i in range(4) if t&(1<<i)),c) for t,c in counts.items() if c));seen[pp]=index
print('domain',allcount,'after_triples',filtered,'orbits',len(orbits),'seconds',time.time()-start,flush=True)
Path(__file__).with_name('EIGHT_QUAD_DOMAIN.json').write_text(json.dumps(dict(allcount=allcount,filtered=filtered,orbits=orbits,seconds=time.time()-start),indent=2))
out=[]
for g in orbits:
 opts=[]
 for k in (9,8,10):
  for pp in permutations(range(k,k+4)):
   p=Profile(20,5,pp,g['counts']);cs=[certificate(p,i) for i in range(4)];rs=rows(p,deductions={pp[i]:cs[i]['loss'] for i in range(4)})
   row=dict(**g,v=20,ds=ds,pos=pp,cs=cs,rows=rs,bound=total_bound(rs));opts.append(row)
   if row['bound']<1:break
  if opts[-1]['bound']<1:break
 bestrow=min(opts,key=lambda r:r['bound']);out.append(bestrow)
 print(g['index'],g['ls'],g['q'],g['t3'],bestrow['bound'],flush=True)
Path(__file__).with_name('EIGHT_QUAD_SCAN.json').write_text(json.dumps(json_value(dict(cases=out,seconds=time.time()-start)),indent=2))
print('PASS',sum(r['bound']<1 for r in out),'of',len(out),'seconds',time.time()-start)
