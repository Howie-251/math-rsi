from pilot import *

def main():
 old=json.loads((HERE/'TWENTY_DELTA5.json').read_text());out=[];start=time.time()
 for idx,r in enumerate(old['cases']):
  if r['strict']:out.append(r);continue
  ns={int(t):n for t,n in r['counts'].items()}
  opts=[r|{'bound':Q(r['bound'])}]
  poses={p for k in range(7,13) for p in permutations(range(k,k+3))}
  for pos in poses:
   z=evaluate(20,ns,pos)
   if z['bound']<opts[-1]['bound']:opts.append(z)
   if z['strict']:break
  z=min(opts,key=lambda r:r['bound']);zz=evaluate(20,ns,z['positions'],True)
  zz.update(degrees=r['degrees'],codegrees=r['codegrees'],triple=r['triple'],original_bound=r['bound'])
  out.append(zz)
  print(idx,r['degrees'],r['codegrees'],r['triple'],r['bound'],'->',zz['bound'],flush=True)
 (HERE/'TWENTY_DELTA5_REFINED.json').write_text(json.dumps(json_value(dict(scope='Complete v20 delta5 triple domain, permuted contiguous layout witnesses',cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
 print('profiles',len(out),'strict',sum(z['strict'] for z in out),'seconds',time.time()-start)
if __name__=='__main__':main()
