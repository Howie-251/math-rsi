"""Receipt-only check: every one of 140 transported labels and failed signatures.
No DP, catalogue regeneration, probability search or original-H search.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction
import json,time

P=Path(__file__).resolve().parent
start=time.process_time()
allrows=json.loads((P/'ALL140_CERTIFICATES.json').read_text())
assert len(allrows)==140
assert len({(z['base'],tuple(z['low'])) for z in allrows})==140
failed=[];strict=0;classes={}
for z in allrows:
    ns={int(t):n for t,n in z['counts'].items()}
    L=set(z['low']);H=set(range(9))-L
    assert len(L)==6 and len(H)==3
    assert sum(ns.values())==35
    assert all(n>0 and 0<=t<512 and t.bit_count()<=5 for t,n in ns.items())
    for x in range(9):
        assert sum(n for t,n in ns.items() if t>>x&1)==(6 if x in L else 7)
    for x,y in combinations(range(9),2):
        assert sum(n for t,n in ns.items() if (t>>x&1) and (t>>y&1))==1
    lm=sum(1<<x for x in L);hm=sum(1<<x for x in H)
    assert all((t&lm).bit_count()<=2 for t in ns)
    assert sum(n for t,n in ns.items() if not t&lm)==14
    assert sorted(z['positions'])==sorted(set(z['positions']))
    assert min(z['positions'])>=1 and max(z['positions'])<=25
    score=Fraction(z['bound']);assert z['strict']==(score<1)
    if score<1:
        strict+=1;continue
    private=sorted(sum(n for t,n in ns.items() if t>>x&1 and (t&lm).bit_count()==1) for x in H)
    common_pure=sum(n for t,n in ns.items() if t&hm==hm and not t&lm)
    key=','.join(map(str,private))+(' / common pure' if common_pure else ' / no common pure')
    classes[key]=classes.get(key,0)+1
    fail={'base':z['base'],'low':z['low'],'s':private,'common_pure_edge_count':common_pure,'bound':z['bound']}
    failed.append(fail)
    if 0 in private:
        assert (private==[0,2,4] and common_pure==1) or private==[0,0,6]
withzero=[z for z in failed if 0 in z['s']]
assert len(withzero)==2 and strict==128 and len(failed)==12
integer_patterns=[]
for g0 in range(1,6):
    for g2 in range(23):
        for g4 in range(3,6):
            if g0+g2+g4>=13 and g2+2*g4<=12 and g0>=g4+1:
                integer_patterns.append([g0,g2,g4])
assert integer_patterns==[[4,6,3],[5,4,4],[5,5,3],[5,6,3]]
assert max(a*b*c for a in range(6) for b in range(6) for c in range(6) if a+b+c<=5)==4
out={'status':'PASS','scope':'140 exact count/degree/unit-pair/low-trace signatures and chosen-layout receipt metadata; no new DP or independent probability implementation',
     'labels':140,'strict_labels':strict,'failed_labels':len(failed),'failed_label_classes':classes,'failed_with_zero':withzero,
     'zero_selection_integer_patterns':integer_patterns,'pure_high_edges':14,'rainbow_capacity_per_edge':4,'capacity_all_edges':56,
     'selection_lower_bounds':[60,75,60], 'CPU_seconds':time.process_time()-start}
(P/'FINAL_SCOPE_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
