from pilot import *
old=json.loads((HERE/'TWENTY_DELTA5_REFINED.json').read_text());out=[];start=time.time()
for idx,r in enumerate(old['cases']):
 if r['strict']:out.append(r);continue
 ns={int(t):n for t,n in r['counts'].items()};winner=r|{'bound':Q(r['bound'])};tried=0
 for pos in permutations(range(1,21),3):
  z=evaluate(20,ns,pos);tried+=1
  if z['bound']<winner['bound']:winner=z
  if winner['strict']:break
 zz=evaluate(20,ns,winner['positions'],True)
 zz.update(degrees=r['degrees'],codegrees=r['codegrees'],triple=r['triple'],tested_new_layouts=tried,full_search_exhausted=tried==6840)
 out.append(zz);print(idx,r['degrees'],r['codegrees'],r['triple'],r['bound'],'->',zz['bound'],tried,flush=True)
(HERE/'TWENTY_DELTA5_FULL.json').write_text(json.dumps(json_value(dict(scope='Complete necessary triples; all placements checked if no strict witness',cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
print('profiles',len(out),'strict',sum(z['strict'] for z in out),'seconds',time.time()-start)
