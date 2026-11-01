from probe import *
start=time.time();out=[]
for v,ds,cap in [(20,(7,7,7),3),(20,(8,8,8),3),(20,(7,8,8),3),(20,(7,7,8),3)]:
 count=passed=0;fails=[]
 for ls in combinations(range(1,cap+1),3):pass
 for ls in product(range(1,cap+1),repeat=3):
  if len(set(ds))==1 and tuple(sorted(ls))!=ls:continue
  for t in range(min(ls)+1):
   r=best(v,ds,ls,t);out.append(r);count+=1
   if r['bound']<1:passed+=1
   else:fails.append((ls,t,str(r['bound']),r['pos']))
 print(v,ds,passed,count,'FAILS',fails,flush=True)
Path(__file__).with_name('TRIPLE_SCAN.json').write_text(json.dumps(json_value(out),indent=2))
print('seconds',time.time()-start)
