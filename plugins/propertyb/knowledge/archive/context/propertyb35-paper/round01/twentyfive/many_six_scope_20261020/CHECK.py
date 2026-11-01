"""Scope arithmetic and the supplied AG(2,5) r=19 realization.

No unknown hypergraph, lock layout or negative-family domain is searched.
Degree partitions and six low-trace counts are necessary scalar domains only.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import ceil, comb
from pathlib import Path
import json

def partitions(n, cap, previous=None):
    if n == 0:
        yield ()
        return
    if previous is None:
        previous = cap
    for x in range(min(n,cap,previous),1-1,-1):
        for tail in partitions(n-x,cap,x):
            yield (x,)+tail

rows=[]
for r in range(3,22):
    k=25-r
    dcap=min(7+r,18,35-r)
    spectra=[p for p in partitions(r,dcap-7) if len(p)<=k]
    # Exact low-count moment domain. This is a deliberately broad numerical
    # relaxation; each scalar tuple need not be realized by H.
    moment_count=0
    min_low_edges=36
    witnesses=[]
    for a5 in range(36):
      for a4 in range(36-a5):
       for a3 in range(36-a5-a4):
        a2=comb(r,2)-10*a5-6*a4-3*a3
        a1=6*r-5*a5-4*a4-3*a3-2*a2
        a0=35-a1-a2-a3-a4-a5
        a=(a0,a1,a2,a3,a4,a5)
        if min(a)<0 or a0>comb(k,5):
            continue
        assert sum(a)==35 and sum(j*a[j] for j in range(6))==6*r
        assert sum(comb(j,2)*a[j] for j in range(6))==comb(r,2)
        moment_count+=1
        L=35-a0
        if L<min_low_edges:
            min_low_edges=L
            witnesses=[a]
        elif L==min_low_edges:
            witnesses.append(a)
    bounds=[Fraction(36*r,r+5)]
    bounds += [Fraction(r*(12*j-r+1),j*(j+1)) for j in range(1,5)]
    # r=5 and r>=6 yield a uniform low-hit unique-bad source.
    quadratic_lb=max(ceil(x) for x in bounds)
    assert min_low_edges>=quadratic_lb
    if r>=6:
        assert quadratic_lb>=20
    rows.append(dict(r=r,nonlow_points=k,maximum_degree_bound=dcap,
                     higher_degree_partition_count=len(spectra),
                     higher_excess_partitions=[list(p) for p in spectra],
                     possible_h=sorted({len(p) for p in spectra}),
                     scalar_low_trace_count=moment_count,
                     scalar_minimum_low_hit_edges=min_low_edges,
                     scalar_minimum_witnesses=witnesses,
                     analytic_quadratic_lower_bound=quadratic_lb,
                     unique_low_bad_source_probability_lower_bound=
                     str(Fraction(9*min_low_edges-170,230))))

# r>=22 violates the universal nonlow-degree capacity (r=25 separately).
excluded={}
for r in range(22,25):
    required=175-6*r
    upper=(25-r)*(35-r)
    assert required>upper
    excluded[r]=dict(required_nonlow_degree_sum=required,upper=upper)
assert 6*25!=175

# The supplied concrete r=19 class member, independently reconstructed.
lines=[]
for x in range(5):
    lines.append(frozenset(5*x+y for y in range(5)))
for slope in range(5):
    for intercept in range(5):
        lines.append(frozenset(5*x+(slope*x+intercept)%5 for x in range(5)))
S=(0,1,2,5,6,7)
extra=[frozenset(set(S)-{v}) for v in S[:5]]
assert len(set(lines))==30 and not set(lines)&set(extra)
E=lines+extra
assert len(set(E))==35 and all(len(e)==5 for e in E)
degree={v:sum(v in e for e in E) for v in range(25)}
low=[v for v in range(25) if degree[v]==6]
assert len(low)==19 and Counter(degree.values())=={6:19,10:5,11:1}
codegree={(x,y):sum({x,y}<=e for e in E) for x,y in combinations(range(25),2)}
assert min(codegree.values())>=1
assert all(codegree[min(v,w),max(v,w)]==1 for v in low for w in range(25) if v!=w)
assert sum(n-1 for n in codegree.values())==50
assert sum(bool(set(low)&e) for e in E)==30
out=dict(status='PASS',scope='necessary scalar domains and one supplied actual realization',
         remaining_r_domain=list(range(3,22)),excluded_r=excluded,
         r25_excluded_by_degree_sum=True,rows=rows,
         example=dict(edges=[sorted(e) for e in E],additional_edges=[sorted(e) for e in extra],
                      degree=degree,low_points=low,low_hit_edge_count=30,
                      pair_cover=True,all_low_codegrees_one=True),
         claims_not_made=['all listed spectra realized','all scalar moments realized',
                          'r20 or r21 exist','r>=6 is colorable'])
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
for z in rows:
    print(z['r'],z['maximum_degree_bound'],z['possible_h'],z['higher_degree_partition_count'],
          z['scalar_minimum_low_hit_edges'])
print('PASS: explicit r19 realization; r22..25 excluded; scalar scopes saved')
