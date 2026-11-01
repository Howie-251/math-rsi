"""Full selected degree-pair projection of the given15 complete delta8 spectra."""
from pathlib import Path
from collections import Counter,defaultdict
from fractions import Fraction
from itertools import combinations
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];st=time.process_time()
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'))
from subset_position_dp import SubsetEngine
source=P.parent/'min_degree_eight_singleton_star_20261020/CONDITIONAL_SCALAR_RESULT.json'
spectra=json.loads(source.read_text())['jobs'];assert len(spectra)==15
domain=defaultdict(list)
for z in spectra:
 ds=z['degrees'];assert len(ds)==21 and sum(ds)==175 and min(ds)==8
 for du,dv in sorted({tuple(sorted(p)) for p in combinations(ds,2)}):
  for c in range(5,min(du,dv)+1):domain[(du,dv,c)].append(z['spectrum_id'])
def bound(ns,pos):
 e=SubsetEngine(21,len(pos),ns);e.inv={p:(0,0,[]) for p in e.inv}
 lock={k:1<<v for v,k in enumerate(pos)};left=0;U=0
 for k in range(1,22):p=lock.get(k,0);value=e.value(k,left,p);assert value is not None;U+=value;left|=p
 return Fraction(U,e.D)
out=[]
for (du,dv,c),ids in sorted(domain.items()):
 ns={0:35-du-dv+c,1:du-c,2:dv-c,3:c};assert min(ns.values())>=0
 vals=[(bound(ns,pos),pos) for pos in ((10,21),(21,10))];val,pos=min(vals)
 out.append(dict(degrees=[du,dv],codegree=c,spectrum_ids=ids,counts=ns,positions=pos,bound=str(val),strict=val<1,all_fixed=[dict(positions=p,bound=str(v)) for v,p in vals]))
 assert time.process_time()-st<10,'initial10CPU profile cutoff'
res=dict(status='COMPLETE_FIXED_TWO_LAYOUT_PROFILE',scope=__doc__,source=str(source.relative_to(ROOT)),spectra=[dict(id=z['spectrum_id'],e=z['e'],partition=z['high_excess_partition'],degrees=z['degrees']) for z in spectra],degree_pair_types=len({(a,b) for a,b,c in domain}),selected_pair_codegree_keys=len(out),strict_count=sum(z['strict'] for z in out),nonstrict=[z for z in out if not z['strict']],cases=out,cpu_seconds=time.process_time()-st)
(P/'PAIR_RESULT.json').write_text(json.dumps(res,indent=2)+'\n');print({k:v for k,v in res.items() if k not in ('cases','spectra')})
