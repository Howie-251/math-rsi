"""Audit actual selection budgets on all76 inherited necessary type profiles.
A>=4; A2/q10; A3/q11; A3/q10 with actual unpaired-unit vs fully-paired-unit split.
"""
from pathlib import Path
from collections import Counter
import json,time
HERE=Path(__file__).parent;start=time.time();source=json.loads((HERE.parent/'R2_C2_ACTUAL_UNIT_BUDGETS.json').read_text());rows=source['high_unit_degree_cap_refinement']['remaining_profiles'];assert len(rows)==76;out=[]
for i,r in enumerate(rows):
 x=r['T_counts'];a=x['A'];t=sum(x.values());q=r['q'];b=x['C']+x['D']+r['Z9'];h=18-q;e=2*q-19-b;rh=16-2*(r['Z8']+r['Z9']);rr=dict(source_index=i,type_profile=r,A_count=a,high_count=h,high_degree_excess=e,high_w_budget=rh)
 if a>=4:rr.update(case='four_A',guaranteed_selection='four actual unpaired unit8 vertices',local_modes=['A4'])
 else:
  assert x==dict(A=a,B=0,C=0,D=0,E=0,F=0)
  if a==2:
   assert q==10 and h==8 and e in (0,1) and rh==0
   rr.update(case='two_A_q10',guaranteed_selection='one A plus two actual unpaired high units; at most one degree11',local_modes=['u8_10_10']+(['u8_10_11'] if e else []),unit_high_lower=8,unpaired_high_lower=2)
  elif a==3 and q==11:
   assert h==7 and 0<=e<=3 and rh==0
   rr.update(case='three_A_q11',guaranteed_selection='two A separate at both stars, plus one actual unpaired high unit',local_modes=['u8_8_10']+(['u8_8_11'] if e else []),unit_high_lower=7,unpaired_high_lower=1)
  elif a==3 and q==10:
   assert h==8 and e in (0,1) and rh==2
   rr.update(case='three_A_q10',guaranteed_selection='if an unpaired high unit exists use it; otherwise choose a paired degree10 unit (at least5 such)',local_modes=['u8_8_10']+(['u8_8_11'] if e else [])+['p8_8_10'],unit_high_lower=6,paired10_lower_if_no_unpaired=5)
  else:raise AssertionError(rr)
 out.append(rr)
result=dict(status='PASS',scope=__doc__,profile_count=76,case_counts=dict(Counter(r['case'] for r in out)),profiles=out,elapsed_seconds=time.time()-start)
(HERE/'SELECTION_MAP.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items() if k!='profiles'})
