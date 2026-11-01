"""Same actual p6 plus four degree8 neighbours; join all four p-bearing residual views, no independent projection pasting."""
from pathlib import Path
import itertools,json,time
from star_low import parts,recover,SubsetEngine,json_value
from six_eights_four import canon,restrict
HERE=Path(__file__).parent

def moments(r):
 ns={int(m):n for m,n in r['counts'].items()};s=len(r['neighbor_degrees'])
 return {m:sum(n for t,n in ns.items() if t&(m<<1)==m<<1) for m in range(1,1<<s)}
def mapped(vals,S):return {sum(1<<S[i] for i in range(len(S)) if m>>i&1):v for m,v in vals.items()}
def compatible(a,b):return all(m not in a or a[m]==v for m,v in b.items())
def main():
 st=time.time();src=[r for r in json.loads((HERE/'SIX_EIGHTS_FOUR_DP.json').read_text())['cases'] if not r['strict']];prepared=[(r,moments(r)) for r in src];dom=[];seen=set()
 Sviews=[(0,1,2,4),(0,1,3,4),(0,2,3,4)]
 for r,base in prepared:
  old=r['center_partition'];pps=[canon([*old,[4]])]+[canon([list(b)+([4] if j==k else []) for j,b in enumerate(old)]) for k in range(len(old)) if len(old[k])<4]
  for pp in pps:
   options=[[(z,mapped(m,S)) for z,m in prepared if canon(z['center_partition'])==restrict(pp,S)] for S in Sviews]
   def rec(i,inc):
    if i<len(options):
     for z,new in options[i]:
      if compatible(inc,new):yield from rec(i+1,inc|new)
     return
    assert all(m in inc for m in range(1,32) if m not in [30,31])
    for q in range(min(inc[m] for m in (14,22,26,28))+1):
     four=inc|{30:q}
     for t in range(min(1,min(four[m] for m in (15,23,27,29,30)))+1):yield four|{31:t}
   for inc in rec(0,base):
    ds=(6,8,8,8,8);ps=[inc[(1<<i)|(1<<j)] for i,j in itertools.combinations(range(5),2)]
    ns=recover(5,ds,ps,pp,{m:v for m,v in inc.items() if m.bit_count()>=3})
    if ns is None:continue
    key=tuple(ns.get(m,0) for m in range(64))
    if key in seen:continue
    seen.add(key);dom.append(dict(neighbor_degrees=ds,neighbor_codegrees=ps,center_partition=pp,inclusive=inc,counts=ns))
 (HERE/'SIX_EIGHTS_FIVE_DOMAIN.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=dom,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('domain',len(dom),flush=True)
 out=[]
 for i,r in enumerate(dom):
  eng=SubsetEngine(21,6,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;out.append(z);print(i,z['bound'],flush=True)
  if time.time()-st>55:break
 (HERE/'SIX_EIGHTS_FIVE_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(dom),domain_size=len(dom),cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('done',len(out),'strict',sum(z['strict'] for z in out),'max',max((z['bound'] for z in out),default=None),'seconds',time.time()-st)
if __name__=='__main__':main()
