"""Independent stdlib audit. Imports only the two frozen data files, no generator."""
import itertools as it,json,time
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent; S=P.parent; start=time.process_time()
edges=list(it.combinations(range(5),2)); ix={e:i for i,e in enumerate(edges)}
perms=[(0,)+p for p in it.permutations(range(1,5))]
trans=[[ix[tuple(sorted((p[a],p[b])))] for a,b in edges] for p in perms]
def canon(g):
 return min(tuple(g[j] for j in t) for t in trans)
def graph(sets):
 out=[0]*10
 for x in set().union(*sets):
  lab=tuple(i for i,A in enumerate(sets) if x in A)
  assert 1<=len(lab)<=2
  if len(lab)==2:out[ix[lab]]+=1
 return out
# Independently enumerate the complete labelled cap(3,4,4,4,4) domain.
full=set(); labels=0; deg=[0]*5; g=[0]*10; byE={}
def visit(k,E):
 global labels
 if E>8:return
 if k==10:
  if E<2:return
  M=sum(g[i]*g[j] for i,e in enumerate(edges) for j,f in enumerate(edges) if i<j and not(set(e)&set(f)))
  if not ((1<=M<=6) or (E==3 and M==0)):return
  labels+=1;byE[E]=byE.get(E,0)+1;full.add(canon(g));return
 a,b=edges[k]
 for m in range(min((3,4,4,4,4)[a]-deg[a],(3,4,4,4,4)[b]-deg[b],8-E)+1):
  g[k]=m;deg[a]+=m;deg[b]+=m;visit(k+1,E+m);deg[a]-=m;deg[b]-=m
visit(0,0)
dat=json.load(open(S/'CHECK_MIXED_EIGHT.json')); rows=dat['rows']; assert len(rows)==384
stored=set(); counts={}; raw=[]; minimum=10**6
for row in rows:
 sets=[set(A) for A in row['sets']]; assert list(map(len,sets))==[3,4,4,4,4] or sorted(map(len,sets))==[3,4,4,4,4]
 # Move the actual marked three label to 0; remaining labels retain relative order.
 mark=next(i for i,A in enumerate(sets) if len(A)==3); sets=[sets[mark]]+[A for i,A in enumerate(sets) if i!=mark]
 stored.add(canon(graph(sets))); counts[row['source']]=counts.get(row['source'],0)+1
 U=sorted(set().union(*sets)); masks=[sum(1<<x for x in A) for A in sets]
 families={k:[sum(1<<x for x in R) for R in it.combinations(U,k) if all(set(R)&A for A in sets)] for k in (3,4)}
 assert len(families[3])==row['C3'] and len(families[4])==row['C4']
 prefixes={}
 for k in (3,4):
  pair=[sum(R&target==target for R in families[k]) for xy in it.combinations(U,2) for target in [sum(1<<x for x in xy)]]
  pair.sort(reverse=True); prefixes[k]=[0,pair[0],sum(pair[:2])]
  assert prefixes[k]==row[f'C{k}_pair_prefix']
 h3=max(sum(R&target==target for R in families[4]) for xyz in it.combinations(U,3) for target in [sum(1<<x for x in xyz)])
 assert h3==row['h3']
 failures=[]
 for t in range(3):
  for r in range(t+1):
   for v in range(5-r):
    B3=prefixes[3][r]+t-r+v; B4=prefixes[4][r]+(t-r+v)*h3+19-v
    margin=max(len(families[3])-B3,len(families[4])-B4)
    if margin<=0:failures.append((r,t,v))
    else:minimum=min(minimum,margin)
 assert failures==[(q['r'],q['t'],q['v']) for q in row['nongated_parameters']]
 if failures:raw.append(row['name'])
assert stored==full,(len(full),len(stored),len(full-stored),len(stored-full))
required={G for G in full if sum(G[i]*G[j] for i,e in enumerate(edges) for j,f in enumerate(edges) if i<j and not(set(e)&set(f)))>=1}
assert len(required)==259 and len(full-required)==11
assert counts=={'old7':35,'old86':347,'old59':2}
# Certificate checker: reconstruct all candidates directly, then every possible
# target of all four origins, including zero-weight columns and repeated-source sets.
duals=[]; columns=0
for row in json.load(open(S/'SOLVE_TWO_E2.json'))['rows']:
 sets=[set(A) for A in row['sets']];U=sorted(set().union(*sets)); N=len(U); assert U==list(range(N))
 cand=[frozenset(R) for k in (3,4) for R in it.combinations(U,k) if all(set(R)&A for A in sets)]
 assert set(cand)=={frozenset(R) for R in row['candidate_red_sets']} and len(cand)==len(row['candidate_red_sets'])
 cert=row['dual_certificate']; assert not cert['upper_bound_weights']
 alpha={frozenset(q['red_set']):F(q['weight']) for q in cert['coverage_weights']}
 assert len(alpha)==len(cert['coverage_weights']) and set(alpha)<=set(cand)
 assert all(a>=0 for a in alpha.values()) and sum(alpha.values())==1
 beta=list(map(F,cert['budget_weights']));assert len(beta)==N+3 and all(b>=0 for b in beta)
 budget=[2,4,21]+[7-sum(x in A for A in sets) for x in U]; assert budget==row['budgets']
 cost=sum(a*b for a,b in zip(beta,budget));assert cost==F(cert['coverage_upper_bound'])<1
 local=0
 for typ,k,T,X in [('N2',2,1,1),('T3',3,1,0),('Bx3',3,0,1),('N4',4,0,0)]:
  for target in it.combinations(U,k):
   Fset=set(target);lhs=sum(a for R,a in alpha.items() if Fset<=R)
   rhs=beta[2]+T*beta[0]+X*beta[1]+sum(beta[3+x] for x in target)
   assert lhs<=rhs,(row['name'],typ,target,lhs,rhs)
   columns+=1;local+=1
 duals.append({'name':row['name'],'cost':str(cost),'all_columns':local,'candidate_count':len(cand)})
# Independent low-occurrence budget, storing every (d,e) scalar.
low=[]
for d in range(4):
 vals=[]
 for e in range((28-d)//2+1):
  types=[(3-d,F(1,3),6),(28-d-2*e,F(1,4),6),(d,F(1,2),5),(e,F(7,16),5)]
  base=sum(n*cap*p**4/4 for n,p,cap in types); bumps=[]
  for n,p,cap in types:bumps.extend([p**3/3-p**4/4]*(n*cap))
  val=base+sum(sorted(bumps,reverse=True)[:6]);assert val<1;vals.append(val)
 low.append(str(max(vals)))
assert low==['29831/36864','47849/55296','6556667/7077888','61999/65536']
# Remaining double-three-star integer budgets, and the exact equality implications.
core=[]
for j in range(3):
 poss=[((4-j)*p+q+d,p,q,d) for p in range(3-j) for q in range(3-j) for d in range(5-j) if p+q<=2-j and 2*p+q+2*d<=8-2*j]
 maximum=max(z[0] for z in poss);assert maximum==[10,5,2][j]
 core.append({'j':j,'maximum':maximum,'equality_budget_types':[list(z[1:]) for z in poss if z[0]==maximum]})
assert core[2]['equality_budget_types']==[[0,0,2]]
out={'status':'PASS','scope':'Independent complete graph enumeration + direct candidate counting + all rational dual target columns; no source Python imports','full_labelled_graphs':labels,'by_E':byE,'canonical_marked_graphs':len(full),'necessary_domain_canonical_graphs':len(required),'safe_extra_E3_M2_zero_canonical_graphs':len(full-required),'stored_384_distinct_marked_graphs':len(stored),'transport_row_counts':counts,'all_26_parameters_per_row':384*26,'raw_sum_boundary_rows':raw,'minimum_positive_raw_margin':minimum,'duals':duals,'all_target_columns':columns,'low_occurrence_maxima_by_d':low,'double_core_integer_budgets':core,'cpu_seconds':time.process_time()-start}
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
