"""Same actual five-neighbour join using all required complete four-point residual domains."""
from pathlib import Path
import itertools,json,time,argparse
from star_low import recover,SubsetEngine,json_value
from domain_audit import partitions,canon,restrict,moments,mapped,compatible
HERE=Path(__file__).parent
FILES={'7777':'FOUR_SEVENS_DP.json','7778':'FOUR_THREE_SEVENS_DP.json','7788':'GENERIC_7788_DP.json','7888':'GENERIC_7888_DP.json','8888':'GENERIC_8888_DP.json'}

def main():
 p=argparse.ArgumentParser();p.add_argument('degrees',choices=['77788','77888','78888','88888']);p.add_argument('--domain-only',action='store_true');args=p.parse_args();ds=tuple(int(c) for c in args.degrees);st=time.time();views=list(itertools.combinations(range(5),4));prepared={}
 for S in views:
  degree=''.join(str(ds[i]) for i in S)
  if degree not in prepared:
   src=json.loads((HERE/FILES[degree]).read_text());assert src['complete'];prepared[degree]=[(r,moments(r)) for r in src['cases'] if not r['strict']]
 dom=[];seen=set();joins=0
 for pp in partitions(5):
  opts=[[(r,mapped(mm,S)) for r,mm in prepared[''.join(str(ds[i]) for i in S)] if canon(r['center_partition'])==restrict(pp,S)] for S in views];opts.sort(key=len)
  if any(not z for z in opts):continue
  def rec(i,inc):
   if i==len(opts):yield inc;return
   for r,new in opts[i]:
    if compatible(inc,new):yield from rec(i+1,inc|new)
  for inc in rec(0,{}):
   joins+=1;assert set(inc)==set(range(1,31));assert time.time()-st<55
   for t in range(min(1,min(inc[m] for m in (15,23,27,29,30)))+1):
    vals=inc|{31:t};ps=[vals[(1<<i)|(1<<j)] for i,j in itertools.combinations(range(5),2)];ns=recover(5,ds,ps,pp,{m:v for m,v in vals.items() if m.bit_count()>=3})
    if ns is None:continue
    key=tuple(ns.get(m,0) for m in range(64))
    if key in seen:continue
    seen.add(key);dom.append(dict(neighbor_degrees=ds,neighbor_codegrees=ps,center_partition=pp,inclusive=vals,counts=ns))
 (HERE/f'GENERIC_{args.degrees}_DOMAIN.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=dom,join_count=joins,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('domain',len(dom),'joins',joins,'seconds',time.time()-st,flush=True)
 if args.domain_only:return
 out=[]
 for i,r in enumerate(dom):
  eng=SubsetEngine(21,6,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;out.append(z)
  if i%100==0:print(i,z['bound'],flush=True)
  if time.time()-st>55:break
 (HERE/f'GENERIC_{args.degrees}_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(dom),domain_size=len(dom),cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('done',len(out),'strict',sum(z['strict'] for z in out),'max',max((z['bound'] for z in out),default=None),'seconds',time.time()-st)
if __name__=='__main__':main()
