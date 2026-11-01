"""39 balanced actions: 30 within-group swaps and 9 quota-changing flips.
Check elementary edge rates on all five-subsets, then diagnose one saved
actual H. No hypergraph enumeration, moment LP, or model call is used.
"""
from pathlib import Path
from itertools import combinations,product
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;root=P.parents[3];st=time.perf_counter();full=2**25-1
G0=[list(range(5*i,5*i+5)) for i in range(5)];quota=[2,2,2,3,3]
R0=sum(1<<v for g,q in zip(G0,quota) for v in g[:q]);owner0={v:i for i,g in enumerate(G0) for v in g}
def moves(red,G):
 total=red.bit_count();assert total in (12,13)
 for g in G:
  for v in g:
   if not red>>v&1:continue
   for w in g:
    if not red>>w&1:yield dict(kind='swap',vertices=[v,w],red=red^(1<<v)^(1<<w))
 for g in G:
  r=sum(red>>v&1 for v in g)
  if total==12 and r==2:
   for v in g:
    if not red>>v&1:yield dict(kind='flip',vertices=[v],red=red^(1<<v))
  if total==13 and r==3:
   for v in g:
    if red>>v&1:yield dict(kind='flip',vertices=[v],red=red^(1<<v))
acts=list(moves(R0,G0));assert Counter(a['kind'] for a in acts)==dict(swap=30,flip=9)
hist=Counter()
for vs in combinations(range(25),5):
 em=sum(1<<v for v in vs);k=(R0&em).bit_count();old=k in(0,5)
 C=D=0
 for a in acts:
  after=(a['red']&em).bit_count();new=after in(0,5)
  C+=new and not old;D+=old and not new
 if old:
  expected=15 if k==0 else 10+sum(quota[owner0[v]]==2 for v in vs)
  assert D==expected and C==0
 elif k in(1,4):
  y=next(v for v in vs if bool(R0>>v&1)==(k==1));i=owner0[y]
  q=5-quota[i] if k==1 else quota[i]
  expected=q-(sum(owner0[v]==i for v in vs)-1)+(k==4 and quota[i]==2)
  assert C==expected and D==0 and C<=3
 else:assert C==D==0
 hist[(k,C,D)]+=1
# Actual H: independently verify original a5 hypotheses, then the old one-step
# trap under all 39 expanded actions.
H=json.loads((root/'context/propertyb36-40-diagnosis-20261015/high-structure/AFFINE_PLANE_OBSTRUCTION.json').read_text());E=[sum(1<<v for v in e) for e in H['edges']]
G=[sorted(5*x+(x*x+c)%5 for x in range(5)) for c in range(5)];owner={v:i for i,g in enumerate(G) for v in g}
assert len(E)==35 and len(set(E))==35 and all(e.bit_count()==5 for e in E)
assert all(sum(bool(e&(1<<v)) for e in E)==7 for v in range(25))
assert all(sum(bool(e&(1<<u)) and bool(e&(1<<v)) for e in E)==(2 if owner[u]==owner[v] else 1) for u,v in combinations(range(25),2))
def bad(red):return [j for j,e in enumerate(E) if red&e in (0,e)]
def bits(red):return [v for v in range(25) if red>>v&1]
trap=sum(1<<v for v in json.loads((P/'BALANCED_REPAIR_PLATFORM.json').read_text())['trap_red']);before=set(bad(trap));assert len(before)==1
rows=[];C=D=0
for a in moves(trap,G):
 bb=set(bad(a['red']));cre=sorted(bb-before);des=sorted(before-bb);C+=len(cre);D+=len(des)
 rows.append(dict(kind=a['kind'],vertices=a['vertices'],bad_edges=sorted(bb),created=cre,destroyed=des))
assert len(rows)==39 and all(z['bad_edges'] for z in rows)
assert C==20 and D==15
trap_edge=E[next(iter(before))];bad_red=(trap_edge&trap)==trap_edge
bad_color=trap if bad_red else full^trap
critical=[j for j,e in enumerate(E) if (e&trap).bit_count() in (1,4)]
trap_x=sum((E[j]&bad_color).bit_count()==4 for j in critical)
h=sum(sum(bool(bad_color&(1<<v)) for v in G[owner[w]])==3 for w in range(25) if trap_edge>>w&1)
n3=sum((e&bad_color).bit_count()==3 for j,e in enumerate(E) if j not in before and j not in critical)
assert bad_color.bit_count()==13 and 1<=trap_x<=9-h and n3==27-3*trap_x and n3>=3*h
# Short exit uses one newly allowed flip followed by an ordinary swap.
s1=trap^(1<<14);s2=s1^(1<<2)^(1<<16)
assert any(a['red']==s1 for a in moves(trap,G)) and bad(s1)==[29]
assert any(a['red']==s2 for a in moves(s1,G)) and bad(s2)==[]
# Find just one actual minority-bad state and check the new normalization lemma.
choices=[[sum(1<<v for v in ss) for ss in combinations(g,q)] for g,q in zip(G,quota)];scanned=0;minor=None
for cs in product(*choices):
 red=sum(cs);bb=bad(red);scanned+=1
 if len(bb)==1 and red&E[bb[0]]==E[bb[0]]:minor=red;break
assert minor is not None
bb=bad(minor);critical=[j for j,e in enumerate(E) if (e&minor).bit_count() in (1,4)];x=sum((E[j]&minor).bit_count()==4 for j in critical)
assert len(critical)==9 and x<=6
single=[a for a in moves(minor,G) if a['kind']=='flip'];free=[a for a in single if bad(a['red'])==bb]
assert len(single)==9 and len(free)>=3
normal=dict(red=bits(minor),bad_edges=bb,minority_majority_critical_count=x,free_flip_vertices=[a['vertices'][0] for a in free],first_normalized_red=bits(free[0]['red']),first_normalized_bad=bad(free[0]['red']),first_normalized_bad_color_size=13,actual_colorings_scanned=scanned)
out=dict(scope=__doc__,elementary_scope=dict(groups=G0,red=bits(R0),all_five_sets=53130,actions=39,histogram=[dict(red_count=k,creates=c,destroys=d,sets=n) for (k,c,d),n in sorted(hist.items())]),actual_scope=dict(source='context/propertyb36-40-diagnosis-20261015/high-structure/AFFINE_PLANE_OBSTRUCTION.json',groups=G,quotas=quota,a5_parameters_verified=True,trap_red=bits(trap),bad_edges=sorted(before),trap_majority_constraints=dict(h=h,x=trap_x,n3=n3),all_39_actions=rows,neighbor_bad_count_histogram=dict(Counter(len(z['bad_edges']) for z in rows)),creation_sum=C,destruction_sum=D,exit_path=[dict(kind='flip',vertices=[14],red=bits(s1),bad_edges=bad(s1)),dict(kind='swap',vertices=[2,16],red=bits(s2),bad_edges=bad(s2))],minority_normalization_witness=normal),elapsed_seconds=time.perf_counter()-st)
(P/'BALANCED_FLEXIBLE_REPAIR.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(dict(elapsed_seconds=out['elapsed_seconds'],neighbors=out['actual_scope']['neighbor_bad_count_histogram'],C=C,D=D,normalization=normal),indent=2))
