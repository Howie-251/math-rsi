from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,combinations_with_replacement
from collections import Counter
import json,time
st=time.process_time()
P=Path(__file__).resolve().parent
source=P.parent/'a1_rank_component_wedge_budget_20261020/VERIFY.json'
j=json.loads(source.read_text())
edges={tuple(sorted(e)) for e in j['graph_edges']}
assert len(edges)==76 and all(0<=u<v<35 for u,v in edges)
deg=Counter(v for e in edges for v in e)
cover=tuple(sorted(sorted(range(35),key=lambda v:(-deg[v],v))[:3]))
assert all(u in cover or v in cover for u,v in edges)
I=tuple(v for v in range(35) if v not in cover)
assert len(I)==32 and not any(u in I and v in I for u,v in edges)
def ceil(f):return -(-f.numerator//f.denominator)
rows=[]
for r in range(4):
 n=35-r
 q=F(8*n*(n-21),21)
 generic=max(0,ceil(q/9))
 quad8=max(0,ceil((q-40)/4))
 centered=max(0,ceil(F(152*n*(n-21)-16296,1428)))
 old=max(0,14-r)
 rows.append({'deleted':r,'remaining':n,'Q_lower':str(q),'old_edge_lower':old,
              'trace_edge_lower':generic,'with_global_n4_le8_edge_lower':quad8,
              'centered_with_global_n4_le8_edge_lower':centered,
              'top_degree_sum_upper':f'e+{r*(r-1)//2}-{max(old,generic,quad8,centered)}'})
assert [r['with_global_n4_le8_edge_lower'] for r in rows]==[37,33,28,24]
assert [r['trace_edge_lower'] for r in rows]==[21,19,17,15]
assert [r['centered_with_global_n4_le8_edge_lower'] for r in rows]==[41,36,31,27]
# Centered trace coefficients, after multiplication by 21.
assert [21*(j-1)**2-8*(j-1) for j in (0,2,3,4)]==[29,13,68,165]
assert 21*68==1428 and 21*(165-68)==2037 and 8*2037==16296
delete_one_rhs=[F(152*34*13,441)-F(13*t,21) for t in (55,52)]
assert delete_one_rhs==[F(52169,441),F(52988,441)]
assert [ceil(v/2) for v in delete_one_rhs]==[60,61]
assert 35-6-7+1==23
two_deleted_rhs=[F(76*33*12,441)-F(13*t,42) for t in (61,56)]
assert two_deleted_rhs==[F(14513,294),F(7484,147)]
assert [ceil(v) for v in two_deleted_rhs]==[50,51]
assert 2*(6+7+8+8+8)-15==59
assert 648-59==589 and 589-33*32//2==61
assert (2*6-3)+(7-1)+7*(8-1)==64
assert 648-64-33*32//2==56
low_block_determinants={str(zeta):16-zeta*zeta for zeta in (-1,1,2,3)}
assert min(low_block_determinants.values())==7
# For t0=20 the remaining core has exactly 15 nodes.
rank_one_core_edges={a:a*(a-1)//2 for a in range(16)}
assert not any(sum(c)==16 for k in range(4)
               for c in combinations_with_replacement((1,4,9),k))
weak_rank_one=[];shared_rank_one=[]
for a in range(1,16):
 need=4*(15-a)+(a-1)
 for l in range(21):
  if l<need:continue
  for p in range(l//2+1):
   item=(a*(a-1)//2+l-p,a,l,p)
   weak_rank_one.append(item)
   if l-2*p>=need:shared_rank_one.append(item)
assert min(weak_rank_one)[0]==88 and min(shared_rank_one)[0]==98
# Prefix identity verification on this explicit simple graph.
for r in range(4):
 Q=set(sorted(range(35),key=lambda v:(-deg[v],v))[:r]);L=set(range(35))-Q
 eq=sum(u in Q and v in Q for u,v in edges)
 el=sum(u in L and v in L for u,v in edges)
 assert sum(deg[v] for v in Q)==len(edges)+eq-el
out={'status':'PASS','literal_source':str(source.relative_to(P.parents[4])),
 'nonunit_edges':len(edges),'vertex_cover':cover,'independent_set':I,
 'forced_B_principal':'4 I_32','principal_rank':32,'ambient_rank_upper':21,
 'prefix_trace_rows':rows,'Schur_independent_neighbor_square_budget':16,
 'degree_refined_one_deleted':{'T_upper':[55,52],
   'two_e_plus_four_a4_lower':[str(v) for v in delete_one_rhs],
   'e_plus_two_a4_integer_lower':[60,61],
   'edges_avoiding_x_p':23,'node_constraints':['q1<=E-60+2t','q13<=E-61+2t']},
 'degree_refined_two_deleted':{'loss_lower_general':59,'T_upper_general':61,
   'e_plus_two_t_lower_exact':[str(v) for v in two_deleted_rhs],
   'integer_lower_general':50,'top_two_constraint':'q1+q2<=E-49+2t',
   'loss_lower_if_intersection_one':64,'T_upper_if_intersection_one':56,
   'integer_lower_if_intersection_one':51,
   'unit_pair_constraint':'qF+qG<=E-51+2t'},
 'low_degree_elimination':{'low_pair_block_determinants':low_block_determinants,
   'low_degree_nodes_upper_if_E_gt35':20,'degree_at_least_two_nodes_lower':15,
   'rank_one_core_edge_counts_if_20_low_nodes':rank_one_core_edges,
   'core_edge_identity':'E_core=E-l+p',
   'twenty_low_nodes_minimum_E_weak':min(weak_rank_one),
   'twenty_low_nodes_minimum_E_shared_leaves':min(shared_rank_one),
   'low_degree_nodes_upper_if_E_72_to80':19},
 'cpu_seconds':time.process_time()-st}
(P/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
