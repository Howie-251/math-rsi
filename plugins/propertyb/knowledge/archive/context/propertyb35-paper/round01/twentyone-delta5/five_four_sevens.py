"""Four actual seven-degree plus one eight-degree unit neighbour; all same-H four-point residual views."""
from pathlib import Path
import itertools,json,time
from star_low import recover,SubsetEngine,json_value
from domain_audit import partitions,canon,restrict,moments,mapped,compatible
HERE=Path(__file__).parent

def main():
 st=time.time();prepared=[]
 for name in ['FOUR_SEVENS_DP.json','FOUR_THREE_SEVENS_DP.json']:
  prepared.extend((r,moments(r)) for r in json.loads((HERE/name).read_text())['cases'] if not r['strict'])
 ds=(7,7,7,7,8);views=list(itertools.combinations(range(5),4));dom=[];seen=set()
 for pp in partitions(5):
  opts=[[(r,mapped(mm,S)) for r,mm in prepared if tuple(r['neighbor_degrees'])==tuple(ds[i] for i in S) and canon(r['center_partition'])==restrict(pp,S)] for S in views]
  if any(not z for z in opts):continue
  def rec(i,inc):
   if i==len(opts):yield inc;return
   for r,new in opts[i]:
    if compatible(inc,new):yield from rec(i+1,inc|new)
  for inc in rec(0,{}):
   assert set(inc)==set(range(1,31))
   for t in range(min(1,min(inc[m] for m in (15,23,27,29,30)))+1):
    vals=inc|{31:t};ps=[vals[(1<<i)|(1<<j)] for i,j in itertools.combinations(range(5),2)];ns=recover(5,ds,ps,pp,{m:v for m,v in vals.items() if m.bit_count()>=3})
    if ns is None:continue
    key=tuple(ns.get(m,0) for m in range(64))
    if key in seen:continue
    seen.add(key);dom.append(dict(neighbor_degrees=ds,neighbor_codegrees=ps,center_partition=pp,inclusive=vals,counts=ns))
 (HERE/'FIVE_FOUR_SEVENS_DOMAIN.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=dom)),indent=2)+'\n');print('domain',len(dom),flush=True)
 out=[]
 for i,r in enumerate(dom):
  eng=SubsetEngine(21,6,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;out.append(z);print(i,z['bound'],flush=True)
 (HERE/'FIVE_FOUR_SEVENS_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('strict',sum(z['strict'] for z in out),'seconds',time.time()-st)
if __name__=='__main__':main()
