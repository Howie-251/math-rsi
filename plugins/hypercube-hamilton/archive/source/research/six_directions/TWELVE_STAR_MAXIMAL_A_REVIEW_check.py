"""Structural geometry and independent small-model checks; NOT the finite A premise."""
import pathlib,json,hashlib,itertools,collections
R=pathlib.Path(__file__).resolve().parent
def load(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
m=load('TWELVE_STAR_MAXIMAL_A_MANIFEST.json')
for n,h in m['files'].items():assert sha(n)==h,n
for n in ['TWELVE_EXTRA_FORCED_REVIEW.json','TWELVE_STAR_B_REVIEW.json','Q5_T17_RANK_BATCH_REVIEW.json','HIGHER_HOLE_UNIFIED_TRANSFER_REVIEW.json']:assert load(n)['verdict']=='PASS'
source=load('TWELVE_EXTRA_FORCED_REVIEW.json');assert source['details']['remaining_covered_target_geometries']==235
representatives=[{39,43,45,51,53},{39,43,45,51,63},{39,43,45,54,63},{39,43,51,60,63},{39,43,53,57,63},{39,43,53,58,63}]
assert {tuple(sorted(z)) for z in representatives}=={tuple(r['Z']) for r in source['details']['supplementary_remaining_geometry']['orbits']}
J={1,2,4,8,16};G={x for x in range(32) if x and (x.bit_count()%2==0 or x not in J)};E={x for x in G if x.bit_count()%2==0};O=G-E
assert (len(G),len(E),len(O))==(26,15,11)
rolechecks=0
for Z in representatives:
 T={z^32 for z in Z};assert len(T)==5 and T<=O
 for t in T-{31}:
  for q in E:
   if (q^t).bit_count()!=1:continue
   for w,b in itertools.permutations(J,2):
    S=J-{w,b};Y={s^32 for s in S};z0=t^32;p=w^32;r=b^32
    HB={32}|(Z-{z0})|Y
    assert len(HB)==8 and len(Y)==3 and not {p,r}&HB and z0 not in HB
    assert {32^(1<<d) for d in range(5)}-Y=={p,r}
    assert p!=63 and r!=63 and len({q^32,z0,*Y})==5
    rolechecks+=1
# Balanced endpoint path-joining lemma: all type populations up to9 components.
joining=0
for k in range(5):
 for l in range(10):
  if not 3<=2*k+l<=9:continue
  types=(['EE']+['OE']*l+['OO']+sum((['EE','OO'] for _ in range(k-1)),[])) if k else ['EO']*l
  color={};n=len(types);D=[]
  for i,t in enumerate(types):color[2*i]=t[0];color[2*i+1]=t[1]
  for i in range(n):
   a=2*i+1;b=2*((i+1)%n);assert color[a]!=color[b] and a//2!=b//2;D.append((a,b))
  assert len({x for e in D for x in e})==2*n;joining+=1
# Independent abstract maximalization-lift identities. Any extension is tested,
# so inclusion-maximality is not silently used for an algebraic step.
Ev=set(range(7));Ov={100,101,102};v=100;w=200;b=201;S={202,203,204};liftchecks=0;branches=collections.Counter();tchecks=0
def matchings(E,O):
 yield frozenset()
 for size in range(1,len(O)+1):
  for odds in itertools.combinations(sorted(O),size):
   for evens in itertools.permutations(sorted(E),size):yield frozenset(zip(odds,evens))
def support(edges):return {x for e in edges for x in e}
def changed(edges):
 target=[e for e in edges if v in e]
 if not target:return edges
 h=target[0][1];return (edges-{target[0]})|{(w,h)}
for star in matchings(Ev,Ov):
 Xstar=(Ev|Ov)-support(star);starprime=changed(star);starv=v in support(star)
 Xstarprime=Xstar if starv else (Xstar-{v})|{w}
 for subset in range(1<<len(star)):
  seq=list(star);L=frozenset(e for i,e in enumerate(seq) if subset>>i&1);Lprime=changed(L);actualv=v in support(L)
  X=(Ev|Ov)-support(L);Xprime=X if actualv else (X-{v})|{w}
  assert Lprime<=starprime
  for q in Ev-support(star):
   Qstar=(Xstarprime-{q})|S;Q=(Xprime-{q})|S
   even=sorted(Qstar&Ev);odd=sorted(Qstar-Ev);assert len(even)==len(odd) and len(Qstar)>=6
   Dstar=frozenset(zip(odd,even));diff=starprime-Lprime;D=Dstar|diff
   assert not support(Dstar)&support(diff) and len(support(D))==2*len(D) and support(D)==Q
   assert not support(D)&support(Lprime) and q not in support(D)
   if actualv:branch='actual_internal'
   elif starv:branch='actual_crossing_max_new_internal';assert w in support(diff)
   else:branch='actual_crossing_max_unmatched'
   branches[branch]+=1;liftchecks+=1
   for t in (support(L)&Ov)-{v}:assert t not in support(D);tchecks+=1
arith=0
for ml in range(5,12):
 for ms in range(ml,12):
  c=26-2*ml;assert c>=4
  assert (26-2*ms)+2==2*(14-ms) and 14-ms>=3
  assert (14-ms)+(ms-ml)==14-ml and 2*(14-ml)==c+2
  assert 30-((14-ml)+1)==15+ml and 30-(15+ml)==15-ml
  assert 2*(15-ml)==c+4;arith+=1
out={'status':'PASS','frozen_hashes_checked':len(m['files']),'G_populations':[26,15,11],'static_q_t_w_b_role_checks':rolechecks,'balanced_path_endpoint_type_populations_checked':joining,'small_submatching_extension_lift_checks':liftchecks,'lift_branches':dict(branches),'covered_t_avoids_completion_checks':tchecks,'all_integer_degree_component_population_checks':arith,'conditional_reduction_math_only':True,'finite_A_premise_proved':False,'finite_maximal_matching_enumeration_executed_or_trusted':False,'finite_search_successes_accepted':False,'new_Q6_covered_records_accepted':0,'full_twelve_hole_proved':False,'full_P6_proved':False}
(R/'TWELVE_STAR_MAXIMAL_A_REVIEW_check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
