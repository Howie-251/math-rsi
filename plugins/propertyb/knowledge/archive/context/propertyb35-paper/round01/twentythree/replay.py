"""Fixed-witness exact replay of the v23 pilots; no layout search or floating point."""
from pair_pilot import *
from star_template import evaluate_q
from four_eight_star import domain
st=time.time();count=0;strict=0
for name in ['PAIR_PILOT.json','TRIPLE_PILOT.json','EIGHT_PAIR_STAR.json','RARE_LOW_DEFECT_TRIPLES.json','FOUR_EIGHT_STAR.json']:
 z=json.loads((HERE/name).read_text())
 for r in z['profiles']:
  ns={int(k):v for k,v in r['counts'].items()};ev=evaluate(23,ns,tuple(r['positions']),True)
  assert ev['bound']==Q(r['bound']) and ev['strict']==r['strict'];count+=1;strict+=ev['strict']
 if name=='FOUR_EIGHT_STAR.json':
  saved={(r['graph'],tuple(tuple(b) for b in r['partition']),tuple(r['counts'].get(str(m),0) for m in range(32))) for r in z['profiles']}
  generated={(name,tuple(tuple(b) for b in pp),tuple(ns[m] for m in range(32))) for name in ['empty','one','two_matching','path3','double','triangle','path4','double_one'] for pp,ns in domain(name) if not any(n and not(m&1) and m.bit_count()>=3 for m,n in ns.items())}
  assert saved==generated
z=json.loads((HERE/'STAR_TEMPLATE.json').read_text())
for r in z['profiles']:
 ns={int(k):v for k,v in r['counts'].items()};p=tuple(r['positions']);ev=evaluate_q(ns,p,r['center_actual_bad_pairs']);assert ev['bound']==Q(r['bound']);count+=1;strict+=r['strict']
 _,abc=engine(23,p).bound(ns,True)
 assert all((a['A'],a['B'],a['C'])==b for a,b in zip(ev['rows'],abc))
# Independent necessary total-degree cases for exactly two low unit neighbours.
spectra=set();cases=[]
for a in (6,7):
 for b in range(a,8):
  for eu in range(2):
   for en in range(2):
    if a+b+18*8+2*6+eu+en!=169:continue
    ds=[6,a,b]+[8]*(18-eu)+([9] if eu else [])+[6]*(2-en)+([7] if en else [])
    assert len(ds)==23 and sum(ds)==175;spec=tuple(ds.count(i) for i in [6,7,8,9]);spectra.add(spec);cases.append(dict(low_unit_degrees=[a,b],extra_unit=eu,extra_nonunit=en,spectrum_6_7_8_9=spec))
assert spectra=={(4,1,18,0),(5,0,17,1)}
out=dict(scope=__doc__,passed=True,fixed_profiles=count,strict_profiles=strict,independent_A_B_C_rows=23*count,rare_low_unit_cases=cases,elapsed_seconds=time.time()-st)
(HERE/'REPLAY.json').write_text(json.dumps(json_value(out),indent=2)+'\n');print(out)
