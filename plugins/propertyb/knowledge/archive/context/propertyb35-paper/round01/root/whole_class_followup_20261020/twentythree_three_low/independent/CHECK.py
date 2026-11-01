"""Fresh restricted r13 domain and actual-index cost reconstruction.
No imports from production domain/fee/menu functions. Reuse only the declared
14 single-center exact-count table and the canonical fourset deduction table.
"""
from pathlib import Path
from itertools import product,combinations
from collections import Counter
from math import comb
from fractions import Fraction
from functools import lru_cache
import json,sys,time
P=Path(__file__).resolve().parent;SRC=P.parent
star=json.loads((SRC.parent/'twentythree_internal_map/independent/RESULT.json').read_text())['direct_counts']
assert len(star)==14
def C(n,k):return comb(n,k) if 0<=k<=n else 0
@lru_cache(None)
def edge_bad(q,outside,pin):
    if not pin:return C(18-outside,q)+C(18-outside,q-outside)
    if pin=='R':return C(18-outside,q)
    if pin=='B':return C(18-outside,q-outside)
    return 0
# Exactly the already-proved table in TWENTYTHREE_FOUR_LOW_EDGE §3.
OVERLAP={(8,'R'):(0,0,45,126,234,600,1125),
         (8,'B'):(0,0,1,3,6,30,75),
         (9,'R'):(0,0,10,29,56,180,400),
         (9,'B'):(0,0,10,29,56,180,400)}
def overlap(q,pin,m):
    tab=OVERLAP[q,pin]
    return tab[min(6,m)]+max(0,m-6)*tab[2]
@lru_cache(None)
def center_bad(q,pingroups):
    pins=[p for group in pingroups for p in group]
    if not pins:
        keys=[k for k in star if k.startswith('w0_')]
        return max(star[k][str(q)] for k in keys),'w0'
    if len(pins)==1:
        name='w1_'+pins[0]
        return max(star['w1_'+s+'_'+pins[0]][str(q)] for s in ('34','44')),name
    assert len(pins)==2
    sig='RR' if pins.count('R')==2 else 'BB' if pins.count('B')==2 else 'RB'
    kind='double' if len(pingroups)==1 else 'two'
    assert len(pingroups) in (1,2)
    key='w2_'+kind+'_'+sig
    return star[key][str(q)],key
def key(U,tr,d):return (U,tuple(sorted(tr)),d)
def generate(U):
    # Derive the seven patterns from independent integer pin counts:
    # a copies low-u, b copies low-v, c copies low-u-v, a+b+2c<=2.
    patterns=[(a,b,c) for a,b,c in product(range(3),repeat=3) if a+b+2*c<=2]
    assert len(patterns)==7
    answer={};inventories=set();candidates=0
    for three in product(patterns,repeat=3):
        for highcopies in range(U):
            candidates+=1;inter=Counter({24:highcopies}) if highcopies else Counter()
            for z,(a,b,c) in enumerate(three):
                for mask,n in [(1<<z|8,a),(1<<z|16,b),(1<<z|24,c)]:
                    if n:inter[mask]+=n
            inc=[sum(n for t,n in inter.items() if t>>i&1) for i in range(5)]
            used=[sum(n*(t.bit_count()-1) for t,n in inter.items() if t>>i&1) for i in range(5)]
            if inc[3]>U-1 or used[3]>4*U-22:continue
            for d in range(7,36):
                nonG=inter.copy();degrees=[6,6,6,U,d]
                singles=[degrees[i]-1-inc[i] for i in range(5)]
                if min(singles)<0 or used[4]>4*d-22:continue
                for i,n in enumerate(singles):
                    if n:nonG[1<<i]=n
                # Direct original34-edge recovery, not primary's K/d interval.
                pure=34-sum(nonG.values())
                if pure<0:continue
                if pure:nonG[0]=pure
                assert sum(nonG.values())==34
                assert [sum(n for t,n in nonG.items() if t>>i&1)+1 for i in range(5)]==degrees
                tr=tuple(t for t,n in inter.items() for _ in range(n))
                assert all((t&7).bit_count()<=1 for t in tr)
                k=key(U,tr,d);assert k not in answer
                answer[k]=nonG;inventories.add(tuple(sorted(tr)))
    assert candidates==343*U
    return answer,len(inventories),candidates
def source(U):
    name='RESULT.json' if U==7 else f'RESULT_U{U}_R13.json'
    records=json.loads((SRC/name).read_text())['rows'];ret={}
    for z in records:
        tr=tuple(sum(1<<i for i in t) for t in z['traces'])
        restricted=all((t&7).bit_count()<=1 for t in tr)
        assert restricted==z['r13']
        if restricted:
            k=key(U,tr,z['d']);assert k not in ret;ret[k]=z
    return ret
def check(k,nonG,z):
    U,tr,d=k;free=set(z['free']);fixed={int(i):v for i,v in z['fixed'].items()};q=z['quota']
    assert 1<=len(free)<=3 and free<=set(range(3))
    assert set(fixed)==set(range(5))-free and set(fixed.values())=={'R','B'}
    assert q in (8,9)
    # One entry for each actual nonG original edge, retaining multiplicities.
    edges=[t for t,n in sorted(nonG.items()) for _ in range(n)];assert len(edges)==34
    owner={};fee_stars=0;labels=[]
    for center in sorted(free):
        indices=[j for j,t in enumerate(edges) if t>>center&1];assert len(indices)==5
        pin_groups=[]
        for j in indices:
            assert j not in owner;owner[j]=center
            others=[i for i in range(5) if edges[j]>>i&1 and i!=center]
            assert all(i in fixed for i in others)
            if others:pin_groups.append(tuple(fixed[i] for i in others))
        assert sum(map(len,pin_groups))<=2
        fee,label=center_bad(q,tuple(sorted(pin_groups)));fee_stars+=fee;labels.append(label)
    assert labels==z['types']
    remaining=[j for j in range(34) if j not in owner]
    assert len(remaining)==34-5*len(free)
    fee_fixed=0;single_groups=Counter()
    for j in remaining:
        t=edges[j];pins=[fixed[i] for i in range(5) if t>>i&1]
        assert all(i in fixed for i in range(5) if t>>i&1)
        pin='' if not pins else pins[0] if len(set(pins))==1 else 'mixed'
        fee_fixed+=edge_bad(q,5-t.bit_count(),pin)
        if t.bit_count()==1:single_groups[pin]+=1
    deduction=sum(overlap(q,pin,n) for pin,n in single_groups.items())
    fee=fee_stars+fee_fixed-deduction
    assert fee>=0 and fee==z['total'] and C(18,q)==z['space']
    assert single_groups['R']==z['red_singletons'] and single_groups['B']==z['blue_singletons']
    assert fee<C(18,q)
    return {'U':U,'internal_masks':list(tr),'v_degree':d,'free':sorted(free),'fixed':fixed,'quota':q,
            'star_import_cost':fee_stars,'indexed_fixed_cost':fee_fixed,'within_singleton_deduction':deduction,
            'total':fee,'space':C(18,q)}
start=time.process_time();summaries=[];receipts=[];pilot='profile' in sys.argv
for U in [7,8,9]:
    domain,ni,nc=generate(U);given=source(U)
    assert set(domain)==set(given)
    ks=sorted(domain);chosen=ks[:5] if pilot else ks
    rr=[check(k,domain[k],given[k]) for k in chosen];receipts+=rr
    tight=max(rr,key=lambda z:Fraction(z['total'],z['space']))
    summaries.append({'U':U,'cartesian_candidates':nc,'inventories':ni,'complete_keys':len(domain),'checked_keys':len(rr),
       'source_key_sets_equal':True,'min_v_degree':min(k[2] for k in domain),'max_v_degree':max(k[2] for k in domain),
       'keys_with_v_degree_less_than_U':sum(k[2]<U for k in domain),'min_margin':min(z['space']-z['total'] for z in rr),
       'tight_ratio':str(Fraction(tight['total'],tight['space'])),'tight_witness':tight,
       'free_size_distribution':dict(Counter(len(z['free']) for z in rr)),'quota_distribution':dict(Counter(z['quota'] for z in rr))})
out={'status':'PILOT_PASS' if pilot else 'PASS_WITH_DECLARED_IMPORTS','review_independence':'same-family','acceptance_status':'provisional',
     'scope':__doc__,'complete_domain':not pilot,'checked_keys':len(receipts),'imported_single_center_types':14,
     'summaries':summaries,'CPU_seconds':time.process_time()-start,'receipts':receipts}
(P/('PROFILE.json' if pilot else 'RESULT.json')).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='receipts'},indent=2))
