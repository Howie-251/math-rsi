"""Actual x5+p6+three degree8 neighbours after every prior three-neighbour projection."""
from pathlib import Path
import sys,itertools,time,json
from star_low import parts,recover,SubsetEngine,json_value
HERE=Path(__file__).parent

def canon(pp):return tuple(sorted(tuple(sorted(b)) for b in pp))
def restrict(pp,S):
 mp={v:i for i,v in enumerate(S)};return canon([[mp[i] for i in b if i in mp] for b in pp if any(i in mp for i in b)])
def main():
 st=time.time();lookup={}
 src=json.loads((HERE/'STAR_LOW_DP.json').read_text())['cases']+json.loads((HERE/'STAR_THREE_DP.json').read_text())['cases']
 for r in src:
  if r['strict']:continue
  key=(tuple(r['neighbor_degrees']),tuple(r['neighbor_codegrees']),canon(r['center_partition']))
  lookup.setdefault(key,set()).add(r['neighbor_triple'])
 ds=(6,8,8,8);pairs=list(itertools.combinations(range(4),2));subs=list(itertools.combinations(range(4),3));bits=[sum(1<<i for i in ss) for ss in subs];dom=[]
 for ps in itertools.product((1,2),repeat=6):
  pmap=dict(zip(pairs,ps))
  for pp in parts(4):
   opts=[]
   for S in subs:
    key=(tuple(ds[i] for i in S),tuple(pmap[ij] for ij in itertools.combinations(S,2)),restrict(pp,S));opts.append(lookup.get(key,set()))
   if any(not o for o in opts):continue
   for ts in itertools.product(*opts):
    for q in range(min(ts)+1):
     ns=recover(5,ds,ps,pp,dict(zip(bits,ts))|{15:q})
     if ns is None:continue
     dom.append(dict(neighbor_degrees=ds,neighbor_codegrees=ps,center_partition=pp,triples=ts,four=q,counts=ns))
 (HERE/'SIX_EIGHTS_FOUR_DOMAIN.json').write_text(json.dumps(json_value(dict(scope=__doc__,cases=dom,domain_seconds=time.time()-st)),indent=2)+'\n');print('domain',len(dom),flush=True)
 out=[]
 for i,r in enumerate(dom):
  eng=SubsetEngine(21,5,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;out.append(z)
  if i%25==0:print(i,z['bound'],flush=True)
  if time.time()-st>55:break
 (HERE/'SIX_EIGHTS_FOUR_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(dom),domain_size=len(dom),cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('done',len(out),'strict',sum(z['strict'] for z in out),'max',max(z['bound'] for z in out),'seconds',time.time()-st)
if __name__=='__main__':main()
