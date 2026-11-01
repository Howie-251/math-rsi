from probe import *
start=time.time();opts=[]
for pos in combinations(range(1,22),3):
 for pp in (pos,(pos[1],pos[0],pos[2]),(pos[2],pos[0],pos[1])):
  r=calc(21,(5,8,8),(1,1,1),0,pp);opts.append(r)
  if r['bound']<1:
   print('PASS',pp,r['bound'],flush=True)
   break
 if opts[-1]['bound']<1:break
bestrow=min(opts,key=lambda r:r['bound'])
Path(__file__).with_name('FULL588.json').write_text(json.dumps(json_value(dict(tested=len(opts),best=bestrow,elapsed=time.time()-start)),indent=2))
print('BEST',bestrow['pos'],bestrow['bound'],'tested',len(opts),'time',time.time()-start)
