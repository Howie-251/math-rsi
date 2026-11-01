from pathlib import Path
import sys,runpy,json,time,contextlib,importlib.util
from math import comb
from fractions import Fraction as Q
from collections import Counter
ROOT=Path('/Users/rfy_naiveai/Desktop/aris4math');P=ROOT/'context/propertyb35-paper/round01';OUT=P/'audit-unique-six-two-three-seven-20261020/native';sys.dont_write_bytecode=True
write=Path.write_text;active='';records=[]
def redirect(self,data,*a,**kw):
 assert self.resolve().is_relative_to(ROOT)
 return write(OUT/(active+'__'+self.name),data,*a,**kw)
Path.write_text=redirect
for i,rel in enumerate(['middle/generic_high_degree_pair_gates_20261020/VERIFY.py','middle/generic_degree_six_star_count_20261020/VERIFY.py','middle/generic_c3_high_degree_saturation_20261020/VERIFY.py','twentyone-high/unique6_with7/new_structure_20261020/independent_pool_replay.py'],10):
 active=f'RUN{i:02d}';st=time.monotonic()
 with (OUT/(active+'.log')).open('w') as log,contextlib.redirect_stdout(log):runpy.run_path(str(P/rel),run_name='__main__')
 records.append(dict(id=active,source=str((P/rel).relative_to(ROOT)),status='PASS',seconds=time.monotonic()-st))
 print(active,'PASS',round(records[-1]['seconds'],4),flush=True)
Path.write_text=write
# Exact original-H constants, independent of supplied moment implementation.
D=comb(21,10)
p=Q(comb(16,5)+comb(16,10),D);q=Q(comb(12,5)+comb(12,6),D)
w=[comb(8+j,1+j)+comb(8+j,6) for j in range(5)]
assert (D,p,q,w)==(352716,Q(2,57),Q(11,2261),[36,120,330,792,1716])
assert Q(5)*(2-35*p)/(2*q)==Q(1190,3)
assert 10*D*(2-35*p)==2722720
# Moment survivor binding to the fresh replay, not to old survivors only.
new=json.loads((OUT/'RUN01__NO_CRITICAL_SURVIVORS33.json').read_text());orig=json.loads((P/'middle/a2_a3_min4_cap13_closure_20261020/NO_CRITICAL_SURVIVORS33.json').read_text());assert new==orig
pre=json.loads((OUT/'RUN01__NO_CRITICAL_BEFORE_ROW202.json').read_text());assert pre==json.loads((P/'middle/a2_a3_min4_cap13_closure_20261020/NO_CRITICAL_BEFORE_ROW202.json').read_text())
assert len(new)==33 and {z['a'] for z in new}=={3}
edges=Counter(595-z['n'][1] for z in new);assert edges=={70:24,71:7,72:2}
assert max(595-z['n'][1] for z in pre)==77
assert 6*5+29*4==146 and 146//2==73
# Verify row-tau inequality over every allowed codegree and double-counting constants.
assert all(comb(l-1,2)>=l-2 for l in range(1,5))
assert all(comb(l-1,2)<=l-1 for l in range(1,5))
assert 35*comb(5,2)-comb(21,2)==140
assert 164896-29*6006+4*2002+7*132+17*22==28
assert comb(20,10)-2*(comb(15,9)-5*3**5)==177176
# Old low-degree strong pair interfaces: reconstruct exact 2-lock inventory and re-evaluate fixed bounds.
sp=importlib.util.spec_from_file_location('selected_pair_replay',P/'twentyone-delta5/replay.py');mod=importlib.util.module_from_spec(sp);sp.loader.exec_module(mod)
old=json.loads((P/'twentyone-high/DOUBLES.json').read_text())['cases'];extra=json.loads((P/'middle/high_edge_intersection_repair_20261020/RESULT.json').read_text())['extra_pair_gates']
by={(tuple(z['degrees']),z['codegree']):z for z in old+extra}
selected=[]
for ds in [(7,7),(7,8),(7,9),(8,8),(8,9),(9,9)]:
 for c in range(5,min(ds)+1):
  r=by[(ds,c)];ns={int(k):v for k,v in r['counts'].items() if v};expected={0:35-sum(ds)+c,1:ds[0]-c,2:ds[1]-c,3:c};assert ns=={k:v for k,v in expected.items() if v}
  val=mod.verify(r);assert val<1;selected.append(dict(degrees=ds,codegree=c,bound=str(val)))
# Check exact high-pair domain is really all118, including8 nonstrict tails.
high=json.loads((P/'middle/generic_high_degree_pair_gates_20261020/FULL.json').read_text())['cases']
assert {(tuple(z['degrees']),z['codegree']) for z in high}=={((d1,d2),c) for d2 in range(10,14) for d1 in range(7,d2+1) for c in range(5,d1+1)}
assert len(high)==118 and sum(z['strict'] for z in high)==110
out=dict(status='PASS',extra_runs=records,probability_numerators=w,one_flip_threshold='1190/3',two_flip_threshold=2722720,fresh_survivors33_exactly_equal=True,E_distribution=dict(edges),before_row_E_max=77,actual_six_star_E_lower=73,selected_low_pair_certificates=selected,high_pair_complete_inputs=118,high_pair_strict=110,scalar_counterexample_tests='all allowed pointpair λ1..4; no rowτ half-factor; fully rebound202/33 outputs; exact one/two-flip orientation factors')
(OUT/'EXTRA_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print('EXTRA_CHECKS PASS',len(selected),'low pair certificates')
