"""Small complement-cover classification, 22 proper triples and fixed-frequency arithmetic."""
from itertools import combinations,combinations_with_replacement
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent;P=127
points=range(7);pairs=[sum(1<<i for i in q) for q in combinations(points,2)]
trios=[sum(1<<i for i in q) for q in combinations(points,3)]
def clique(mask):return sum(1<<i for i,p in enumerate(pairs) if p&mask==p)
allpairs=(1<<21)-1
A=15;Bs=[113,51,23,15] # intersections with0123 have sizes1,2,3,4.
classes=[]
for r,B in enumerate(Bs,1):
    assert (A&B).bit_count()==r
    base=clique(A)|clique(B);solutions=[]
    for tris in combinations_with_replacement(trios,3):
        left=allpairs^(base|clique(tris[0])|clique(tris[1])|clique(tris[2]))
        need=[i for i in range(21) if left>>i&1]
        if len(need)>2:continue
        for f0,f1 in combinations(range(21),2):
            if any(i not in (f0,f1) for i in need):continue
            missing=[pairs[f0],pairs[f1]];internal=[P^x for x in missing]
            triples=[P^A,P^B];quads=[P^x for x in tris]
            c=[sum(T>>i&1 for T in internal) for i in points]
            a=[sum(T>>i&1 for T in triples) for i in points]
            b=[sum(T>>i&1 for T in quads) for i in points]
            u=[8-c[i]-a[i]-b[i] for i in points]
            assert r==2 and u==[4]*7
            proper=lambda Q:all(Q&T and Q&T!=T for T in internal+triples+quads)
            good=[Q for Q in trios if proper(Q)]
            assert not any(proper(Q) for Q in pairs) and len(good)==22
            solutions.append(dict(missing=missing,triple_masks=triples,quad_masks=quads,u=u,proper_three_count=22))
    assert len(solutions)==(2 if r==2 else 0)
    classes.append(dict(intersection=r,no_proper_pair_solutions=solutions))
# Complete positive-frequency spectra under48 incidences and at most17 points.
spectra=[]
for n1 in range(18):
    for n2 in range(18):
        for n3 in range(18):
            if n1+n2+n3<=17 and n1+2*n2+3*n3==48:
                spectra.append(dict(n1=n1,n2=n2,n3=n3,minimum_singleton_degree_without_old_gate=2*n1+5*n2+7*n3))
assert {(x['n1'],x['n2'],x['n3']) for x in spectra}=={(0,0,16),(0,3,14),(1,1,15)}
# A point of total singleton frequency2: all28 distributions across7 P-stars.
max_constant_one=0
for i in points:
    d=[0]*7;d[i]=2
    assert sum(sum(d[v] for v in points if Q>>v&1)==1 for Q in trios)==0
for i,j in combinations(points,2):
    d=[0]*7;d[i]=d[j]=1
    count=sum(sum(d[v] for v in points if Q>>v&1)==1 for Q in trios)
    assert count==20;max_constant_one=max(max_constant_one,count)
result=dict(PASS=True,triangle_multisets_per_intersection_case=7770,intersection_cases=classes,
            all_positive_frequency_spectra=spectra,total_singleton_associations=112,
            count_of_point_frequency2_star_distributions=28,max_three_sets_with_point_positive_frequency1=max_constant_one,
            proper_three_count=22,strict_comparison='20<22')
(HERE/'ANALYTIC_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS no-pair complement classification:0/2/0/0; allu4;22proper triples;48inc spectra;20<22')
