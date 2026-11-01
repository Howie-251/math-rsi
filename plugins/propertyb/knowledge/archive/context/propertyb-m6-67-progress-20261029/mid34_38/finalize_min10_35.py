import json
from fractions import Fraction
from pathlib import Path
P=Path(__file__).resolve().parent;rows=[]
def ell_unit(ds,blocks):
 ell={b:1 for b in blocks}
 for j,d in enumerate(ds):ell[1<<j]=d-sum(bool(b&(1<<j)) for b in blocks)
 ell[0]=66-sum(ell.values());return {b:n for b,n in ell.items() if n}
a=json.loads((P/'ADAPTIVE_COMPONENT.json').read_text())
for r in a['rows']:
 if r['v']!=35 or len(r['degrees'])!=3 or r['degrees'][:2]!=[10,10]:continue
 f=r['degrees'][2];ell=ell_unit(r['assigned'],r['blocks'])
 if min(ell.values())<0:continue
 assert r['strict'] and Fraction(r['U'])<1
 rows.append(dict(group='exclude_unit_10_pair',input_third_degree=f,trace='separate' if r['blocks']==[3,5,6] else 'triple',assigned_degrees=r['assigned'],positions=r['positions'],ell=ell,U=r['U'],deletion='joint_component_quota_legacy'))
assert len(rows)==79
b=json.loads((P/'TWO_ARMS35.json').read_text())
for r in b['rows']:
 if r['degrees']!=[10,11,11]:continue
 tau=r['tau'];lam=r['lam_yz'];ell={7:tau,3:1-tau,5:1-tau,6:lam-tau}
 for j,d in enumerate(r['degrees']):ell[1<<j]=d-sum(n for b,n in ell.items() if b&(1<<j))
 ell[0]=66-sum(ell.values());ell={b:n for b,n in ell.items() if n};assert min(ell.values())>=0 and r['strict']
 rows.append(dict(group='exclude_two_unit_11_neighbors',lam_other=lam,tau=tau,assigned_degrees=r['degrees'],positions=r['positions'],ell=ell,U=r['U'],deletion='max_avoided_component_quota_final'))
assert len(rows)==100
c=json.loads((P/'LOW_PAIR_MIN10_35.json').read_text())
for r in c['rows']:
 if r['degrees']!=[12,10,10]:continue
 assert r['strict']
 rows.append(dict(group='low_pair_degree12_center',lam_other=2,tau=r['tau'],assigned_degrees=r['degrees'],positions=r['positions'],ell=r['ell'],U=r['U'],deletion='max_avoided_component_quota_final'))
assert len(rows)==102
out=dict(status='complete candidate exact input domain; all rows strict',v=35,M=66,minimum_degree=10,rows=rows,groups={g:sum(r['group']==g for r in rows) for g in {r['group'] for r in rows}},maximum=str(max(Fraction(r['U']) for r in rows)))
(P/'CERT35_MIN10.json').write_text(json.dumps(out,indent=2));print(out['groups'],out['maximum'])
