from pathlib import Path
from math import comb
from fractions import Fraction as F
import importlib.util,json
OWNED=Path(__file__).resolve().parent
P=OWNED/'work/archive/context/propertyb-m7-131-20261029'
spec=importlib.util.spec_from_file_location('pilot_copy',P/'pilot.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
old=json.loads((P/'CANDIDATE.json').read_text())
ceil=lambda n,d:-(-n//d)
records={}
for M in [130,131]:
    budget=7*M
    vertex=[v for v in range(1,100) if v*ceil(v-1,6)<=budget]
    small=[str(F(M*(comb(v//2,7)+comb(v-v//2,7)),comb(v,7))) for v in range(13,37)]
    keys=[]
    for v in range(54,67):
        for d in range(ceil(v-1,6),budget//v+1):
            s=2*(v-1)-6*d
            assert s>0
            B=next(b for b in range(d,budget+1) if v*d+s*(b+1-d)>budget)
            keys.extend((v,d,e) for e in range(d,B+1))
    tail=[dict(v=v,r_lower=13*v-budget,max_conflict_degree=73-v,independent_lower=ceil(13*v-budget,74-v)) for v in range(71,74)]
    records[str(M)]=dict(degree_budget=budget,vertex_upper=max(vertex),balanced_max=str(max(map(F,small))),balanced_37=str(F(M*(comb(18,7)+comb(19,7)),comb(37,7))),two_profile_count=len(keys),two_keys=keys,tail=tail)
oldkeys=set(map(tuple,records['130']['two_keys']));newkeys=set(map(tuple,records['131']['two_keys']))
records['new_two_keys_at_131']=sorted(newkeys-oldkeys)
records['omitted_old_keys_at_131']=sorted(oldkeys-newkeys)
# A targeted diagnostic of the old worst necessary profile, not a full M131 proof search.
p.c.M=131
ell={0:105,1:12,2:13,3:1};trials=[]
for pos in [(33,34),(33,32)]:
    u=p.bound(66,pos,ell,True)
    trials.append(dict(positions=pos,U=str(u),strict=u<1))
records['M131_old_worst_profile_lift']=dict(v=66,degrees=[13,14],ell=ell,trials=trials,scope='two old menu layouts only; necessary local profile, not an actual noncolorable hypergraph')
assert all(not r['strict'] for r in trials)
records['five_uniform_26']=dict(v=26,M=33,pair_bound_lhs=26*25,pair_bound_rhs=33*5*4,min_degree=ceil(25,4),degree_sum_lower=26*ceil(25,4),degree_sum_upper=5*33,contradiction=26*ceil(25,4)>5*33)
assert records['five_uniform_26']['contradiction']
(OWNED/'SCOPE_RESULTS.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps({k:v for k,v in records.items() if k not in ['130','131']},indent=2))
for M in ['130','131']:
    print(M,json.dumps({k:v for k,v in records[M].items() if k!='two_keys'}))
