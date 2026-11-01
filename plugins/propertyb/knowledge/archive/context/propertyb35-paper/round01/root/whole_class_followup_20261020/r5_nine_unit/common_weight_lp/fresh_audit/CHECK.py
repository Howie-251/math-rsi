#!/usr/bin/env python3
from pathlib import Path
from itertools import combinations,permutations,product
from collections import Counter
from fractions import Fraction as Q
from math import comb
from time import process_time
import sys,json
P=Path(__file__).resolve().parent;B=P.parent;ROOT=next(p for p in P.parents if (p/'computations/independent_structure_bounds.py').exists())
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows
start=process_time();E=list(combinations(range(5),2));graphs=[]
def grow(k,weights,left):
 if k==10:
  if left==[0]*5:graphs.append(tuple(weights))
  return
 i,j=E[k]
 for w in range(min(3,left[i],left[j])+1):
  rem=left.copy();rem[i]-=w;rem[j]-=w
  if any(rem[z]>3*sum(z in pair for pair in E[k+1:]) for z in range(5)):continue
  grow(k+1,weights+[w],rem)
grow(0,[],[8]*5);assert len(graphs)==len(set(graphs))==148
idx={e:i for i,e in enumerate(E)}
def relabel(w,p):return tuple(w[idx[tuple(sorted((p[i],p[j])))]] for i,j in E)
def canonical(w):return min(relabel(w,p) for p in permutations(range(5)))
classes=Counter(map(canonical,graphs));assert len(classes)==6 and classes[(2,)*10]==1
certs=json.loads((B/'NONUNIFORM_RESULT.json').read_text())['records'];assert len(certs)==5
assert {canonical(r['w']) for r in certs}==set(classes)-{(2,)*10}
types=[]
for ell in (0,1,2):
 for mask in range(32):
  rest=5-ell-mask.bit_count()
  if rest<0:continue
  for a in range(rest+1):
   for b in range(rest-a+1):types.append((ell,a,b,rest-a-b,mask))
assert len(types)==len(set(types))==512

def true_rows(t,w):
 ell,a,b,c,mask=t;G=(a,b,c);Y=[(mask>>j)&1 for j in range(5)];D={}
 for l,n in enumerate((15,10,10)):D['edge_low_count_'+str(l)]=(int(ell==l),n)
 for g,n in enumerate(G):
  D[f'G{g}_degree_total']=(n,35);D[f'G{g}_internal_pair_incidence']=(comb(n,2),20);D[f'low_G{g}_pair_incidence']=(ell*n,25)
 for g,h in combinations(range(3),2):D[f'G{g}_G{h}_cross_pair_incidence']=(G[g]*G[h],25)
 for y,v in enumerate(Y):
  D[f'Y{y}_degree']=(v,8);D[f'low_Y{y}_pair_incidence']=(ell*v,5)
  for g,n in enumerate(G):D[f'G{g}_Y{y}_cross_pair_incidence']=(n*v,5)
 for k,(y,z) in enumerate(E):D[f'Y{y}_Y{z}_pair_incidence']=(Y[y]*Y[z],1+w[k])
 assert len(D)==50
 return D
receipts=[]
for r in certs:
 w=r['w'];eq=r['exact_equality_dual'];ub=r['exact_inequality_dual'];is_farkas=r.get('excluded_by_exact_Farkas',False)
 assert len({z['name'] for z in eq})==len(eq)
 assert len({tuple(z['Y_pair']) for z in ub})==len(ub)
 assert all(Q(z['coefficient'])>=0 and z['rhs']==1 and w[idx[tuple(z['Y_pair'])]]==3 for z in ub)
 rhs=None;slacks=[]
 for t in types:
  D=true_rows(t,w);ell,a,b,c,mask=t
  assert all(D[z['name']][1]==z['rhs'] for z in eq)
  val=sum((Q(z['coefficient'])*D[z['name']][0] for z in eq),Q())
  val+=sum((Q(z['coefficient'])*ell*int(all(mask>>v&1 for v in z['Y_pair'])) for z in ub),Q())
  cost=ell*(comb(a,2)+comb(b,2)+comb(c,2)+sum(w[k] for k,(i,j) in enumerate(E) if mask>>i&1 and mask>>j&1))
  if not is_farkas:val-=cost
  slacks.append(val)
  right=sum((Q(z['coefficient'])*D[z['name']][1] for z in eq),Q())+sum((Q(z['coefficient']) for z in ub),Q())
  if rhs is None:rhs=right
  else:assert rhs==right
 assert min(slacks)>=0
 if is_farkas:assert rhs<0 and str(rhs)==r['exact_farkas_rhs']
 else:assert rhs<130 and str(rhs)==r['exact_optimum']
 receipts.append({'w':w,'kind':'Farkas' if is_farkas else 'upper','rhs':str(rhs),'minimum_slack':str(min(slacks)),'types':len(slacks)})
# Reconstruct complete four-lock pair budget domain and compare saved profiles.
F=json.loads((B/'two_low_gate/RESULT.json').read_text());expected={};pairs=list(combinations(range(4),2));large=[m for m in range(16) if m.bit_count()>2]
for chosen in product((0,1),repeat=5):
 counts=Counter({m:1 for m,on in zip(large,chosen) if on})
 valid=True
 for i,j in pairs:
  rem=(4 if (i,j)==(2,3) else 1)-sum(v for m,v in counts.items() if m>>i&1 and m>>j&1)
  if rem<0:valid=False;break
  if rem:counts[(1<<i)|(1<<j)]=rem
 if not valid:continue
 for i,d in enumerate((6,6,8,8)):counts[1<<i]=d-sum(v for m,v in counts.items() if m>>i&1)
 counts[0]=35-sum(counts.values());assert min(counts.values())>=0
 expected[tuple(sorted(m for m in counts if m.bit_count()>2 and counts[m]))]={m:v for m,v in counts.items() if v}
assert len(expected)==7
assert {tuple(z['large_traces']):{int(k):v for k,v in z['counts'].items()} for z in F['records']}==expected
# Only concrete positions are evaluated: no SubsetEngine, DP, or optimization.
checks=[]
def abc(counts,pos,bound,source_rows=None,label=''):
 ns={int(k):v for k,v in counts.items()};s=len(pos)
 assert sum(ns.values())==35
 stubs=[frozenset(i+1 for i in range(s) if m>>i&1) for m,n in ns.items() for _ in range(n)]
 rows=independent_rows(25,tuple(pos),stubs);value=sum((min(z['A'],z['B'],z['C']) for z in rows),Q());assert value==Q(bound)
 if source_rows is not None:
  if isinstance(source_rows[0],list):old=[[Q(v) for v in row] for row in source_rows]
  else:old=[[Q(row[k]) for k in ('A','B','C')] for row in source_rows]
  assert [[row[k] for k in ('A','B','C')] for row in rows]==old
 checks.append({'label':label,'bound':str(value),'positions':pos,'rows':25,'strict':value<1})
R=json.loads((B.parent/'K5_EXCEPTION_RESULT.json').read_text())
for z in R['pair_cases']:
 if z['lambda']>=6:
  c=z['lambda'];ns={0:19+c,1:8-c,2:8-c,3:c};assert {int(k):v for k,v in z['counts'].items()}=={k:v for k,v in ns.items() if v}
  abc(ns,z['positions'],z['raw_bound'],z['independent_rows'],'pair_c'+str(c))
T=json.loads((B/'LOW_EIGHT_PAIR_RESULT.json').read_text())
for z in T['records']:
 if z['lambda_xy']==5:
  c=5;t=z['triple_inclusive'];ns={7:t,3:1-t,5:1-t,6:c-t,1:4+t,2:7-c+t,4:7-c+t,0:15+c-t}
  assert {int(k):v for k,v in z['counts'].items()}=={k:v for k,v in ns.items() if v}
  abc(ns,z['positions'],z['raw_bound'],z['raw_rows'],'low_pair_c5_t'+str(t))
for z in F['records']:abc(z['counts'],z['positions'],z['raw_bound'],z['raw_rows'],'four_'+str(z['large_traces']))
T=json.loads((B/'two_low_gate/THIRD_LOW_RESULT.json').read_text())
for z in T['records']:
 k=z['selected_T_lows'];ns=Counter({3:1,5:1,6:1,24:4-k})
 for i in range(k):ns[24|(1<<i)]=1
 for i in range(k,3):ns[8|(1<<i)]=1;ns[16|(1<<i)]=1
 for i,d in enumerate((6,6,6,8,8)):ns[1<<i]=d-sum(v for m,v in ns.items() if m>>i&1)
 ns[0]=35-sum(ns.values());assert {int(m):n for m,n in z['counts'].items()}=={m:n for m,n in ns.items() if n}
 abc(ns,z['positions'],z['raw_bound'],z['raw_rows'],'five_selected_T'+str(k))
# Uniform proof's finite local delta claims, not its optional LP/MILP.
delta=[]
for ell,a,b,c,mask in types:
 j=mask.bit_count();u=comb(a,2)+comb(b,2)+comb(c,2)
 val=u+j*(j+ell-2)+3*(ell==2)-ell*(u+j*(j-1));assert val>=0
 if ell==2:delta.append({'j':j,'groups':[a,b,c],'delta':val})
zero=[v for v in delta if v['delta']==0]
assert all((v['j']==3 and v['groups']==[0,0,0]) or (v['j']==0 and 3 in v['groups']) for v in zero)
assert min(v['delta'] for v in delta if v['delta']>0)==2
assert all(v['j']==0 for v in delta if v['delta']==2)
out={'status':'PASS_WITH_DECLARED_IMPORTS','review_independence':'same-family','acceptance_status':'provisional','graphs':148,'orbits':6,'orbit_multiplicities':sorted(classes.values()),'certificates':receipts,'all_types_per_certificate':512,'four_lock_profiles':7,'concrete_ABC_replays':checks,'concrete_rows':sum(v['rows'] for v in checks),'uniform_delta_types':512,'cpu_seconds':process_time()-start}
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
