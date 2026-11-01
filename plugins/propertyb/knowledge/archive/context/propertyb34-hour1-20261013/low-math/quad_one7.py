from quad_general import *
start=time.time();out=[]
for ls in product((1,2),repeat=6):
 # Every permutation of the three degree-eight labels is tested numerically;
 # for pilot simplicity leave the 64 pair-labels intact.
 cases=quad(20,(7,8,8,8),ls);out+=cases
 fail=[(r['t4'],r['t3'],str(r['bound'])) for r in cases if r['bound']>=1]
 print(ls,'pass',len(cases)-len(fail),'of',len(cases),'fails',fail,flush=True)
Path(__file__).with_name('QUAD_ONE7.json').write_text(json.dumps(json_value(dict(cases=out,seconds=time.time()-start)),indent=2))
print('seconds',time.time()-start)
