#!/usr/bin/env python3
from math import comb
from pathlib import Path
import json
from time import process_time

base=Path(__file__).resolve().parent
start=process_time()
def event(union):
    return comb(17-union,10-union) if union<=10 else 0
R=comb(13,6);B=comb(13,10);D=comb(17,10)
w=[event(8-j) for j in range(4)]
f0=[event(12-s) for s in range(4)]
f1=[event(10-s) for s in range(3)]
assert (R,B,D,w,f0,f1)==(1716,286,19448,[36,120,330,792],[0,0,1,8],[1,8,36])
assert all(f0[s]<=3*s for s in range(4))
assert all(f1[s]<=30+3*s and f1[s]<=1+18*s for s in range(3))
assert event(8)<=60 and event(7)-63==57 and event(6)==330
forests={'three_heavy':3*w[2]+2*w[0], 'j3_rank2':w[3]+w[2]+3*w[0], 'j3_rank1':w[3]+2*w[1]+2*w[0]}
mins={'linear':min(540+72*m for m in range(7,16)),
      'one_heavy':min(540+174+72*m for m in range(5,15)),
      'two_disjoint':min(540+348+72*m for m in range(3,14)),
      'two_path':min(540+348+72*m-57 for m in range(3,14)),
      'triangle':min(1083+12*m for m in range(1,13))}
assert min([*forests.values(),*mins.values()])==1044
src=base.parent/'twentytwo_min7_gamma_four_20261020'
trans=json.loads((src/'TRANSPORT_RESULT.json').read_text())
fixed=json.loads((src/'FIXED_RESULT.json').read_text())['nonstrict']
rows=[]
for row in trans['rows']:
    k=row['source']
    if k not in range(20,25):continue
    f=fixed[k]
    assert row['traces']==f['traces']==[7,27,29]
    assert row['attachments']==f['attachments']
    assert sum(row['attachments'])==31
    assert all(t&1 for t in row['traces'])
    h=[sum((t>>i)&1 for t in row['traces']) for i in range(5)]
    assert row['F_degrees']==[1+row['attachments'][i]+h[i] for i in range(5)]
    assert f['counts']['31']==1
    assert all(f['counts'][str(t)]==1 for t in (7,27,29))
    assert all(f['counts'][str(1<<i)]==row['attachments'][i] for i in range(5))
    assert sum(f['counts'].values())==35
    a=row['attachments'][0]
    deduction=1044+36*(a-6)
    numerator=a*R+(31-a)*B-deduction
    rows.append({'source':k,'traces':row['traces'],'a':row['attachments'],
        'degrees':row['F_degrees'],'anchor':0,'red_singletons':a,
        'blue_singletons':31-a,'exception_risk':0,'deduction':deduction,
        'numerator':numerator,'D':D,'margin':D-numerator,'strict':numerator<D})
assert len(rows)==5
assert all(r['numerator']==19190 and r['deduction']==1116 and r['strict'] for r in rows[:4])
assert rows[4]['numerator']==20584 and rows[4]['deduction']==1152 and not rows[4]['strict']
out={'status':'PASS','review_independence':'same-family','acceptance_status':'provisional',
     'scope':'Six distinct4sets on17points;10red. Bound1044. Application only existing22q3 sources20..24 anchor0, no whole-H inference.',
     'R':R,'B':B,'D':D,'w':w,'triple_bounds_noheavy':f0,'triple_bounds_oneheavy':f1,
     'forest_deductions':forests,'bonferroni_minima':mins,'uniform_six_deduction':1044,
     'source_files':['../twentytwo_min7_gamma_four_20261020/TRANSPORT_RESULT.json','../twentytwo_min7_gamma_four_20261020/FIXED_RESULT.json'],
     'source_applications':rows,'cpu_seconds':process_time()-start}
base.joinpath('SIX_SEVENTEEN_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
