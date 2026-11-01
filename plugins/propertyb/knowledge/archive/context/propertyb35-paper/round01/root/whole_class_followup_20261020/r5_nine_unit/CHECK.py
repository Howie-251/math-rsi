"""Full generic nine-unit domain for five low and four seven locks.
Only old17 affine layouts; optional first3 residual-orbit exact DP pilots.
No original-H search, new layout family or full-domain DP sweep.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[5]
S=ROOT/'context/propertyb34/round01/high-math'
sys.dont_write_bytecode=True;sys.path.insert(0,str(S))
from unit_catalogue import fullblocks,canonical
start=time.process_time()
src=json.loads((S/'UNIT_CATALOGUE_9.json').read_text())
assert src['complete'] and len(src['orbits'])==374
old=json.loads((ROOT/'context/propertyb35-paper/round01/twentyfive/UNIT9_MIXED_AFFINE.json').read_text())
assert old['complete'] and old['catalogue_families']==374
oldfamilies={z['base']:z for z in old['families']}
records=[];groups={};summary={'all_markings':374*126,'excluded_low_intersection':0,'excluded_negative_multiplicity':0}
for base,big in enumerate(src['orbits']):
    bs=fullblocks(big,9);h=[7-sum(bool(t>>i&1) for t in bs) for i in range(9)]
    for low in combinations(range(9),5):
        lm=sum(1<<i for i in low)
        if any((t&lm).bit_count()>2 for t in bs):
            summary['excluded_low_intersection']+=1;continue
        singles=[h[i]-int(i in low) for i in range(9)];empty=40-len(bs)-sum(h)
        if min(singles+[empty])<0:
            summary['excluded_negative_multiplicity']+=1;continue
        ns={t:1 for t in bs};ns.update({1<<i:n for i,n in enumerate(singles) if n})
        if empty:ns[0]=empty
        assert sum(ns.values())==35
        assert all(sum(n for t,n in ns.items() if t>>i&1)==7-int(i in low) for i in range(9))
        assert all(sum(n for t,n in ns.items() if (t>>i&1) and (t>>j&1))==1 for i,j in combinations(range(9),2))
        assert all((t&lm).bit_count()<=2 for t in ns)
        f=oldfamilies[base];assert f['feasible']
        c=next(z for z in f['cases'] if z['q']==5)
        oldns={t:1 for t in f['full']}
        oldns.update({1<<i:n-int(i in low) for i,n in enumerate(f['single_high']) if n-int(i in low)})
        if c['empty']:oldns[0]=c['empty']
        assert ns==oldns
        values=[Fraction(a)+sum(Fraction(lay['slopes'][i]) for i in low) for a,lay in zip(c['layout_constants'],f['layouts'])]
        value=min(values);positions=f['layouts'][values.index(value)]['positions']
        key,perm=canonical(big,9,extra=[int(i in low) for i in range(9)],with_perm=True)
        color=sum(1<<perm[i] for i in low)
        z={'base':base,'low':low,'counts':ns,'canonical_large':key,'canonical_lowmask':color,'old_to_canonical':perm,'old_bound':value,'positions':positions}
        groups.setdefault((key,color),[]).append(len(records));records.append(z)
summary.update(feasible_labels=len(records),families=len({z['base'] for z in records}),colored_orbits=len(groups),
               old_strict_labels=sum(z['old_bound']<1 for z in records),old_residual_labels=sum(z['old_bound']>=1 for z in records),
               old_strict_orbits=sum(all(records[i]['old_bound']<1 for i in ids) for ids in groups.values()),
               old_maximum=max(z['old_bound'] for z in records),CPU_seconds=time.process_time()-start)
def serial(x):
    if isinstance(x,Fraction):return str(x)
    if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [serial(v) for v in x]
    return x
out={'scope':'Full374 catalogue plus all126 low-label sets, low intersection<=2, actual M35 degree6^5/7^4. Requires actual independent four-seven caller; threeK5 exception separate.',
     'complete_domain':True,'summary':summary,'records':records}
(P/'DOMAIN.json').write_text(json.dumps(serial(out),indent=2)+'\n')
(P/'SUMMARY.json').write_text(json.dumps(serial(summary),indent=2)+'\n')
print(json.dumps(serial(summary),indent=2),flush=True)
if 'profile' not in sys.argv:raise SystemExit
from subset_position_dp import SubsetEngine
from bare_layout import BareLayout
profile=[]
for key,ids in groups.items():
    if all(records[i]['old_bound']<1 for i in ids):continue
    z=records[ids[0]];ns={int(t):n for t,n in z['counts'].items()};tm=time.process_time()
    eng=SubsetEngine(25,9,ns);w=eng.verify(eng.solve())
    raw=BareLayout(25,w['positions']).bound(ns)
    profile.append({'base':z['base'],'low':z['low'],'labels_in_orbit':[records[i]['low'] for i in ids],
                    'old_bound':z['old_bound'],'raw_witness_bound':raw,'CPU_seconds':time.process_time()-tm,**w})
    print('profile',len(profile),'base',z['base'],'bound',w['bound'],'raw',raw,'CPU',profile[-1]['CPU_seconds'],flush=True)
    if len(profile)==3:break
(P/'PROFILE.json').write_text(json.dumps(serial({'scope':'Only first3 old-residual colored orbit pilots; not full probability sweep',
    'profile_cases':len(profile),'CPU_seconds':sum(z['CPU_seconds'] for z in profile),'records':profile}),indent=2)+'\n')
