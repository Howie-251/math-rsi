"""Shared four-eight domain after 246 triple projections, for >=11 unit degree8 points.
The chosen four-subset minimizes weight; W<=6 and 6*a_i+2W<=33.
"""
from pathlib import Path
import sys,json,time,importlib.util
from fractions import Fraction as Q
P=Path(__file__).resolve();ROOT=P.parents[4];HERE=P.parent
spec=importlib.util.spec_from_file_location('earlier_domain_audit',HERE.parent/'delta6-audit/audit.py');audit=importlib.util.module_from_spec(spec);spec.loader.exec_module(audit)
source=json.loads((HERE/'EIGHT_THREE.json').read_text())['cases'];joint=json.loads((HERE/'EIGHT_THREE_JOINT.json').read_text())['results'];jids={r['source_id']for r in joint if Q(r.get('bound','2'))<1};residual=[r for r in source if not r['strict']and r['source_id']not in jids]
start=time.process_time();got,stats=audit.join_domain(4,(8,)*4,residual);out=[]
for ds,key in got:
 ns=dict(key);I={u:sum(n for t,n in ns.items()if(t>>1)&u==u)for u in range(1,16)}
 ps={u:I[u]-1 for u in I if u.bit_count()==2};W=sum(ps.values());degrees=[sum(v for u,v in ps.items()if u>>i&1)for i in range(4)]
 if W>6 or any(6*a+2*W>33 for a in degrees):continue
 part=[tuple(i for i in range(4)if t>>(i+1)&1)for t,n in ns.items()if t&1 and t!=1 and n];part=tuple(sorted(part))
 out.append(dict(neighbor_degrees=ds,center_partition=part,counts=ns,moments=I,weight=W,weight_degrees=degrees))
out.sort(key=lambda r:(r['weight'],tuple(sorted(r['counts'].items()))))
(HERE/'EIGHT_FOUR_DOMAIN.json').write_text(json.dumps(dict(scope=__doc__,triple_residuals=len(residual),full_join=stats,filtered_cases=len(out),cases=out,cpu_seconds=time.process_time()-start),indent=2)+'\n');print('residuals',len(residual),'join',stats,'selected',len(out),'cpu',time.process_time()-start)
