"""Direct finite checks of repair-blocking rates and local deblocking scope.
Only five chosen bad-edge profiles and compatible critical edges are tested;
no full H or previous color/moment domain is enumerated.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();full=2**25-1
G=[set(range(5*i,5*i+5)) for i in range(5)];owner={v:i for i,g in enumerate(G) for v in g};q=[3,3,3,2,2]
A=set().union(*(set(sorted(g)[:n]) for g,n in zip(G,q)));Am=sum(1<<v for v in A)
allcritical=[set(vs) for vs in combinations(range(25),5) if len(set(vs)&A) in (1,4)]
def actions(A,G):
 out=[]
 for g in G:
  for v in sorted(g&A):
   for u in sorted(g-A):out.append(('swap',[v,u],A^{v,u}))
 for g in G:
  if len(A)==13 and len(A&g)==3:
   for v in sorted(A&g):out.append(('flip',[v],A^{v}))
  if len(A)==12 and len(A&g)==2:
   for u in sorted(g-A):out.append(('flip',[u],A^{u}))
 assert len(out)==39
 return out
moves=actions(A,G)
profiles={'11111':[0,5,10,15,20],'2111':[0,1,5,10,15],'221':[0,1,5,6,10],'311':[0,1,2,5,10],'32':[0,1,2,15,16]}
rows=[];no_free=None;caseB=Counter();total=0
for name,ev in profiles.items():
 e=set(ev);assert e<=A
 repairs=[(kind,uv,z) for kind,uv,z in moves if not(e<=z)]
 assert len(repairs)==15
 hist=Counter();n=0
 for f in allcritical:
  inter=e&f
  if len(inter)>=2 and len({owner[v] for v in inter})!=1:continue
  n+=1;total+=1;k=len(f&A);y=next(iter(f&A)) if k==1 else next(iter(f-A));i=owner[y];t=len(f&G[i])
  B=sum(len(f&z) in (0,5) for kind,uv,z in repairs)
  expected=(4-t if y in e else 0) if k==1 else len((e&G[i])-f)
  assert B==expected and B<=(3 if k==1 else max(len(e&g) for g in G))
  hist[(k,B)]+=1
  if B and k==4 and f-G[i]<=e:
   assert t in (2,3);caseB[t]+=1
   assert not(f&G[i]&e)
   candidates=[(uv,z) for kind,uv,z in moves if kind=='swap' and not(set(uv)&e) and len(f&z)==3]
   assert candidates
  if B and k==1:
   candidates=[uv for kind,uv,z in moves if kind=='swap' and not(set(uv)&e) and len(f&z)==2]
   if not candidates and no_free is None:no_free=dict(bad_profile=name,bad_edge=sorted(e),critical_edge=sorted(f),bad_color_A=sorted(A),minority_A_point=y,repair_block_count=B)
  h=sum(len(f&g)*(len(f&g)-1)//2 for g in G)
  if B and h>=4:assert h==4 and B<=2
 rows.append(dict(profile=name,edge=ev,compatible_critical_edges=n,histogram=[dict(A_points=k,blocking=B,count=c) for (k,B),c in sorted(hist.items())]))
assert no_free is not None
# The explicit no-free-swap pattern is compatible with all pair capacities of
# two edges only; it is not asserted to extend to a complete design.
e={0,1,2,15,16};f={0,3,4,17,18};assert e<=A and len(f&A)==1
assert e&f=={0}
assert not any(kind=='swap' and not(set(uv)&e) and len(f&z)==2 for kind,uv,z in moves)
# On one actual H, independently compare all 9 exact B rates with literal 15
# repair outcomes, including multi-blocking and unique-bad transfer outcomes.
root=P.parents[3];HH=json.loads((root/'context/propertyb36-40-diagnosis-20261015/high-structure/AFFINE_PLANE_OBSTRUCTION.json').read_text());E=[set(z) for z in HH['edges']]
d=json.loads((P/'BALANCED_FLEXIBLE_REPAIR.json').read_text());GG=[set(g) for g in d['actual_scope']['groups']];red=set(d['actual_scope']['trap_red']);AA=set(range(25))-red;eo=E[29]
assert eo<=AA and len(AA)==13
act=actions(AA,GG);rep=[(kind,uv,z) for kind,uv,z in act if not(eo<=z)];assert len(rep)==15
critical=[j for j,f in enumerate(E) if len(f&AA) in (1,4)];rates=[]
for j in critical:
 ff=E[j];k=len(ff&AA);y=next(iter(ff&AA)) if k==1 else next(iter(ff-AA));ii=next(i for i,g in enumerate(GG) if y in g);tt=len(ff&GG[ii])
 b=sum(len(ff&z) in (0,5) for kind,uv,z in rep)
 expected=(4-tt if y in eo else 0) if k==1 else len((eo&GG[ii])-ff)
 assert b==expected;rates.append(dict(edge=j,A_points=k,blocking=b))
psi=sum(r['blocking'] for r in rates);xx=sum(r['A_points']==4 for r in rates);m=max(len(eo&g) for g in GG)
assert psi<=27-(3-m)*xx
transfers=[]
for kind,uv,z in rep:
 bb=[j for j,f in enumerate(E) if len(f&z) in (0,5)];assert bb
 if len(bb)==1:transfers.append(dict(kind=kind,vertices=uv,new_bad_edge=bb[0]))
assert len(transfers)>=30-psi>=3
out=dict(scope=__doc__,elementary_profiles=rows,total_compatible_critical_edges=total,caseB_trace_size_counts=dict(caseB),first_F1_no_free_deblocking_pattern=no_free,explicit_F1_no_free_pattern=dict(bad_edge=sorted(e),critical_edge=sorted(f),scope='two-edge pair-compatible local pattern, not a full H'),actual_check=dict(Psi=psi,x=xx,m=m,bound=27-(3-m)*xx,blocking_rates=rates,unique_transfers=transfers,unique_transfer_lower_bound=30-psi),elapsed_seconds=time.perf_counter()-st)
(P/'BAD_EDGE_TRANSFER_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['elementary_profiles','actual_check']},indent=2));print('actual',psi,xx,m,len(transfers))
