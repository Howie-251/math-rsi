from probe import *
from avoided_lock_quotas import certificate as dual
start=time.time();out=[]
for old in json.load(open(Path(__file__).with_name('EIGHT_QUAD_SCAN.json')))['cases']:
 if Fraction(old['bound'])<1:continue
 counts={int(t):n for t,n in old['counts'].items()};bestrow=None;tested=0
 positions=[tuple(old['pos'])]+[pp for k in range(6,14) for pp in permutations(range(k,k+4))]
 for pp in positions:
  p=Profile(20,5,pp,counts);cs=[dual(p,i) for i in range(4)];rs=rows(p,deductions={pp[i]:cs[i]['loss'] for i in range(4)})
  row=dict(index=old['index'],v=20,ds=(8,8,8,8),ls=old['ls'],q=old['q'],t3=old['t3'],counts=counts,pos=pp,cs=cs,rows=rs,bound=total_bound(rs));tested+=1
  if bestrow is None or row['bound']<bestrow['bound']:bestrow=row
  if row['bound']<1:break
 bestrow['tested']=tested;out.append(bestrow)
 print(old['index'],tested,bestrow['bound'],flush=True)
Path(__file__).with_name('EIGHT_DUAL.json').write_text(json.dumps(json_value(dict(cases=out,seconds=time.time()-start)),indent=2))
print('PASS',sum(r['bound']<1 for r in out),'/',len(out),'seconds',time.time()-start)
