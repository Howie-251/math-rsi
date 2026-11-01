"""Exactly seven degree7 pair codegrees and three all-codegree2 degree7 triples.
Only the old fixed2/fixed8 menus; all quotas zero; all best bounds replayed.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction
import sys,json,time

P=Path(__file__).resolve().parent
ROOT=P.parents[4]
START=time.process_time()
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from independent_structure_bounds import independent_rows

def evaluate(ns,menu):
    s=len(menu[0]);engine=SubsetEngine(21,s,ns)
    engine.inv={p:(0,0,[]) for p in engine.inv}
    values=[];cache={}
    for pos in menu:
        bp={k:1<<v for v,k in enumerate(pos)};left=0;rows=[]
        for k in range(1,22):
            pivot=bp.get(k,0);rows.append(engine.value(k,left,pivot));left|=pivot
        value=Fraction(sum(rows),engine.D)
        values.append({'positions':pos,'bound':str(value),'strict':value<1});cache[pos]=rows
    best=min(values,key=lambda z:Fraction(z['bound']))
    masks=[m for m,n in ns.items() for _ in range(n)]
    assert len(masks)==35
    stubs=[frozenset(v+1 for v in range(s) if m>>v&1) for m in masks]
    replay=independent_rows(21,tuple(best['positions']),stubs)
    total=sum((min(r['A'],r['B'],r['C']) for r in replay),Fraction())
    assert total==Fraction(best['bound'])
    for a,b in zip(cache[tuple(best['positions'])],replay):
        assert Fraction(a,engine.D)==min(b['A'],b['B'],b['C'])
    assert time.process_time()-START<5,'5 CPU cutoff'
    return {'counts':ns,'expanded35_masks':masks,'all_layouts':values,'best':best,'zero_quota':True,
            'independent_35_index_bound':str(total),'ordered_distinct_pairs':1190,
            'rows':[{k:str(v) if isinstance(v,Fraction) else v for k,v in r.items()} for r in replay]}

old=json.loads((P.parent.parent/'twentyone-high/DOUBLES.json').read_text())
old77=[z for z in old['cases'] if z['degrees']==[7,7]]
assert {z['codegree'] for z in old77}==set(range(1,8))
pairmenu=[(10,21),(21,10)];pairs=[]
for c in range(1,8):
    ns={0:21+c,1:7-c,2:7-c,3:c}
    z=evaluate(ns,pairmenu);previous=next(r for r in old77 if r['codegree']==c)
    assert {int(m):n for m,n in previous['counts'].items() if n}=={m:n for m,n in ns.items() if n}
    z.update(degrees=[7,7],codegree=c,old_saved_best={'positions':previous['positions'],
             'bound':previous['bound'],'strict':previous['strict'],'certificates':previous['certificates'],
             'has_nonzero_deductions':any(Fraction(r['deduction']) for r in previous['rows'])})
    pairs.append(z)
    print('PAIR',c,z['best'],'OLD',z['old_saved_best']['bound'],flush=True)

# Exactly the prior eight menu positions from delta8 strong-pair TRIPLES.py.
base=[(10,11,21),(1,11,12),(1,21,9),(11,1,21)]
triplemenu=sorted(set(base+[tuple(22-k for k in p) for p in base]))
assert len(triplemenu)==8
triples=[]
for t in (0,1,2):
    ns={0:20-t,1:3+t,2:3+t,4:3+t,3:2-t,5:2-t,6:2-t,7:t}
    assert min(ns.values())>=0 and sum(ns.values())==35
    assert [sum(n for m,n in ns.items() if m>>v&1) for v in range(3)]==[7]*3
    assert [sum(n for m,n in ns.items() if m&pair==pair) for pair in (3,5,6)]==[2]*3
    z=evaluate(ns,triplemenu);z.update(degrees=[7]*3,codegrees=[2]*3,inclusive_triple=t)
    triples.append(z)
    if t==0:
        (P/'PILOT.json').write_text(json.dumps({'scope':'One t0 case before complete three-input scan',
                     'case':z,'menu':triplemenu,'cpu_seconds':time.process_time()-START},indent=2)+'\n')
    print('TRIPLE',t,z['best'],flush=True)

summary={'status':'COMPLETE_FIXED_MENU_DIAGNOSTIC','scope':__doc__,
         'review_independence':'same-family','acceptance_status':'provisional',
         'pair_menu':pairmenu,'triple_menu':triplemenu,
         'pair_domain':7,'triple_domain':3,'old_DOUBLES_total_cases':len(old['cases']),
         'old_DOUBLES_actual_selected77_codegrees':[1,2,3,4,5,6,7],
         'old_saved_best_is_not_zero_quota_for_c1_c2':True,
         'strict_pair_codegrees':[z['codegree'] for z in pairs if z['best']['strict']],
         'failed_pair_codegrees':[z['codegree'] for z in pairs if not z['best']['strict']],
         'strict_triple_t':[z['inclusive_triple'] for z in triples if z['best']['strict']],
         'failed_triple_t':[z['inclusive_triple'] for z in triples if not z['best']['strict']],
         'pairs':pairs,'triples':triples,'all_failed_cases_retained':True,
         'new_positions_or_search':False,'cpu_seconds':time.process_time()-START}
(P/'RESULT.json').write_text(json.dumps(summary,indent=2)+'\n')
print({k:v for k,v in summary.items() if k not in ('pairs','triples')})
