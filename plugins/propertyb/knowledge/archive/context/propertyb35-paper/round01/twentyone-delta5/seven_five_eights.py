"""One actual seven-degree plus five eight-degree neighbours; all five p-bearing five-point residual views."""
from pathlib import Path
import itertools,json,time
from star_low import recover,json_value
from domain_audit import partitions,canon,restrict,moments,mapped,compatible
HERE=Path(__file__).parent

def main():
 st=time.time();src=json.loads((HERE/'GENERIC_78888_DP.json').read_text());assert src['complete'];prep=[(r,moments(r)) for r in src['cases'] if not r['strict']];views=[(0,)+S for S in itertools.combinations(range(1,6),4)];ds=(7,8,8,8,8,8);dom=[];seen=set();joins=0
 for pp in partitions(6):
  if len(pp)>5:continue
  opts=[[(r,mapped(mm,S)) for r,mm in prep if canon(r['center_partition'])==restrict(pp,S)] for S in views];opts.sort(key=len)
  if any(not z for z in opts):continue
  def rec(i,inc):
   if i==len(opts):yield inc;return
   for r,new in opts[i]:
    if compatible(inc,new):yield from rec(i+1,inc|new)
  for inc in rec(0,{}):
   assert time.time()-st<55;joins+=1;assert set(inc)==set(range(1,64))-{62,63}
   for q in range(min(1,min(inc[m] for m in (30,46,54,58,60)))+1):
    vals=inc|{62:q,63:0};ps=[vals[(1<<i)|(1<<j)] for i,j in itertools.combinations(range(6),2)];ns=recover(5,ds,ps,pp,{m:v for m,v in vals.items() if m.bit_count()>=3})
    if ns is None:continue
    key=tuple(ns.get(m,0) for m in range(128))
    if key in seen:continue
    seen.add(key);dom.append(dict(neighbor_degrees=ds,neighbor_codegrees=ps,center_partition=pp,inclusive=vals,counts=ns))
 (HERE/'GENERIC_788888_DOMAIN.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=dom,join_count=joins,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('domain',len(dom),'joins',joins,'seconds',time.time()-st)
if __name__=='__main__':main()
