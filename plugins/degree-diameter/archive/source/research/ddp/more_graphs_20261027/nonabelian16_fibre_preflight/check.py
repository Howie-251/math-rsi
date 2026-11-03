"""Exhaustive genuineAut(D8xC2) and nonidentityh repeated-label capacity."""
from pathlib import Path
from itertools import product
from collections import Counter
import json,resource,time

OUT=Path(__file__).resolve().parent
resource.setrlimit(resource.RLIMIT_CPU,(5,5))
START=time.process_time()
assert json.loads((OUT/'PREDICTION.json').read_text())['frozen_before_enumeration']
# ID i+4j+8k is r^i s^j t^k. All products are composed left to right.
def decode(x):return x%4,(x//4)%2,x//8
def mul(x,y):
 i,j,k=decode(x);u,v,w=decode(y)
 return ((i+(-1 if j else 1)*u)%4)+4*(j^v)+8*(k^w)
M=[[mul(x,y) for y in range(16)] for x in range(16)]
inverse=[next(y for y in range(16) if M[x][y]==M[y][x]==0) for x in range(16)]
def power(x,n):
 z=0
 for _ in range(n):z=M[z][x]
 return z
r,s,t=1,4,8
assert power(r,4)==power(s,2)==power(t,2)==0 and M[M[s][r]][s]==inverse[r]
assert all(M[t][x]==M[x][t] for x in range(16))
automorphisms=[];relational_triples=0;candidate_triples=0
for R,S,T in product(range(16),repeat=3):
 # Order4 of the image of r is necessary for every automorphism.
 if power(R,4)!=0 or power(R,2)==0 or power(S,2)!=0 or power(T,2)!=0:continue
 candidate_triples+=1
 if M[M[S][R]][S]!=inverse[R] or M[T][R]!=M[R][T] or M[T][S]!=M[S][T]:continue
 relational_triples+=1
 phi=[]
 for x in range(16):
  i,j,k=decode(x);phi.append(M[M[power(R,i)][power(S,j)]][power(T,k)])
 if len(set(phi))!=16:continue
 assert all(phi[M[x][y]]==M[phi[x]][phi[y]] for x in range(16) for y in range(16))
 automorphisms.append(dict(generator_images=[R,S,T],permutation=phi))
assert len({tuple(a['permutation']) for a in automorphisms})==len(automorphisms)
hits=[];hist=Counter();first_diagnostic=None
for ai,a in enumerate(automorphisms):
 phi=a['permutation']
 for h in range(1,16):
  orbit=[h]
  for _ in range(3):orbit.append(phi[orbit[-1]])
  ordered=orbit[::-1];endpoints=[]
  for eps in product(range(2),repeat=4):
   z=0
   for g,e in zip(ordered,eps):
    if e:z=M[z][g]
   endpoints.append(z)
  coverage=len(set(endpoints));hist[coverage]+=1
  diagnostic=dict(automorphism_index=ai,generator_images=a['generator_images'],psi_permutation=phi,
    h=h,h_normalform=decode(h),ordered_directions=ordered,epsilon_order='lexicographic e0,e1,e2,e3 in{0,1}',
    ordered_product_endpoints=endpoints,distinct_endpoints=coverage)
  if first_diagnostic is None:first_diagnostic=diagnostic
  if coverage==16:hits.append(diagnostic)
first=hits[0] if hits else None
if first:
 phi=first['psi_permutation'];h=first['h']
 # Actual four applications of R(x)={psi(x),psi(x)h}, for all16 startingfibres.
 reachable=[]
 for x in range(16):
  states={x}
  for _ in range(4):states={z for u in states for z in [phi[u],M[phi[u]][h]]}
  assert states==set(range(16));reachable.append(sorted(states))
 first['all16_starting_fibres_four_step_reachable']=reachable
 first['commutators_ordered_directions']=[[M[M[M[inverse[x]][inverse[y]]][x]][y] for y in first['ordered_directions']] for x in first['ordered_directions']]
 first['g0']=0;first['g1']=h;first['relation']='R_a(x)={psi(x),psi(x)*h}'
 (OUT/'first_witness.json').write_text(json.dumps(first,indent=2)+'\n')
result=dict(status='POSITIVE_AAAA_PREFLIGHT' if hits else 'COMPLETE_ZERO_AAAA_PREFLIGHT',
 automorphisms=len(automorphisms),generator_triples_after_order_filter=candidate_triples,
 presentation_satisfying_triples=relational_triples,nonidentity_h_per_automorphism=15,
 cases_tested=15*len(automorphisms),successful_cases=len(hits),distinct_endpoint_histogram=dict(hist),
 first_witness=first,first_diagnostic=first_diagnostic,
 target_Delta=8,target_D=4,hypothetical_n=1152,actual_n=None,actual_D=None,
 controller_vertices=72,real_tight_word_requirement='aaaa is one of26 requiredfixed-controllerwords',
 remaining25_tight_words_checked=False,controller_pair_fullcoverage_checked=False,
 fibre_only=True,graph_generated=False,old_binary_model_reenumerated=False,
 CPU_seconds=time.process_time()-START,pending=[])
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'successful_cases.json').write_text(json.dumps(hits,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['first_witness','first_diagnostic']},indent=2))
if first:print('WITNESS',json.dumps({k:first[k] for k in ['generator_images','h','ordered_directions','ordered_product_endpoints']}))
