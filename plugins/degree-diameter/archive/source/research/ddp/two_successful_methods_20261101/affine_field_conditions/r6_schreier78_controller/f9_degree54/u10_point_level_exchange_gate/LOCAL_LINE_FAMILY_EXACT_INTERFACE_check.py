"""Two/three independent complete-line families: exact local primitive, no solver."""
import time
START=time.process_time()
import resource
resource.setrlimit(resource.RLIMIT_CPU,(3,3))
import itertools,json
from pathlib import Path
D=Path(__file__).resolve().parent;P=json.loads((D.parent/'PARAMETERS.json').read_text());Q=9
add=lambda a,b:(a%3+b%3)%3+3*((a//3+b//3)%3)
neg=lambda a:(-a%3)%3+3*((-(a//3))%3)
MUL=P['field']['multiplication']
def summands(xs):
 s=0
 for x in xs:s=add(s,x)
 return s

def feasible_two(q,A,B):
 assert q>=2 and A>=0 and B>=0
 return (A+q-1)//q+(B+q-1)//q<=q

def profiles_three(q,A,B,C):
 assert q>=2 and min(A,B,C)>0
 return [(a,b,c) for a,b,c in itertools.product(range(1,q),repeat=3)
         if A<=b*c and B<=a*(q-c) and C<=(q-a)*(q-b)]

# Only actualtarget19's three darts; (12,50,11) are line counts, not source IDs.
darts=[]
for source in [17,45,71]:
 port=P['controller'][source].index(19);op=P['inverse_ports'][port];chart=P['dart_chart_index'][source][port]
 darts.append(dict(source=source,target=19,source_port=port,source_port_name=P['ports'][port],target_port=op,target_port_name=P['ports'][op],chart_index=chart,chart_id=P['chart_ids'][chart],matrix=P['matrices'][chart],noise_direction=P['directions'][op]))
cols=[x['noise_direction'] for x in darts];a,b,c=cols
positive=summands([MUL[a[0]][MUL[b[1]][c[2]]],MUL[a[1]][MUL[b[2]][c[0]]],MUL[a[2]][MUL[b[0]][c[1]]]])
negative=summands([MUL[a[0]][MUL[b[2]][c[1]]],MUL[a[1]][MUL[b[0]][c[2]]],MUL[a[2]][MUL[b[1]][c[0]]]])
determinant=add(positive,neg(negative));assert determinant==2

def transform(v):return tuple(summands(MUL[v[k]][cols[k][j]] for k in range(3)) for j in range(3))
def verify_anchors(anchors):
 actual=[];details=[]
 for axis,rows in enumerate(anchors):
  points=set()
  for pair in rows:
   line=set()
   for t in range(Q):
    if axis==0:v=(t,pair[0],pair[1])
    elif axis==1:v=(pair[0],t,pair[1])
    else:v=(pair[0],pair[1],t)
    line.add(transform(v))
   assert len(line)==9 and not line&points
   points|=line
  assert len(points)==9*len(rows)
  actual.append(points);details.append({'axis':axis,'anchors':rows,'lines':len(rows),'actual_target19_pins':len(points)})
 assert all(not actual[i]&actual[j] for i,j in itertools.combinations(range(len(actual)),2))
 return dict(families=details,total_lines=sum(len(x) for x in anchors),actual_target19_total_pins=len(set().union(*actual)),pairwise_pin_intersections=[len(actual[i]&actual[j]) for i,j in itertools.combinations(range(len(actual)),2)])

pair_cases=[];witnesses={}
for A,B in [(50,31),(27,54),(0,81),(0,0),(0,82)]:
 feasible=feasible_two(Q,A,B)
 row={'counts':[A,B],'ceil_supports':[(A+8)//9,(B+8)//9],'feasible':feasible}
 if feasible:
  needA=(A+8)//9;needB=(B+8)//9
  anchorsA=list(itertools.product(range(Q),range(needA)))[:A]
  anchorsB=list(itertools.product(range(Q),range(needA,needA+needB)))[:B]
  w=verify_anchors([anchorsA,anchorsB]);row['actual_witness_verified']=True
  witnesses[f'two_{A}_{B}']=w
 pair_cases.append(row)
assert pair_cases[0]['feasible']==False and pair_cases[1]['feasible']==True
bad=profiles_three(9,12,50,11);good=profiles_three(9,12,50,3)
assert bad==[] and good==[(8,6,2)]
a,b,c=good[0]
R=list(itertools.product(range(b),range(c)))[:12]
G=list(itertools.product(range(a),range(c,Q)))[:50]
B=list(itertools.product(range(a,Q),range(b,Q)))[:3]
w=verify_anchors([R,G,B]);assert w['total_lines']==65 and w['actual_target19_total_pins']==585
w.update(profile=[a,b,c],counts=[12,50,3],profile_rectangle_capacities=[b*c,a*(9-c),(9-a)*(9-b)],unused_rectangle_lines=[b*c-12,a*(9-c)-50,(9-a)*(9-b)-3])
witnesses['three_12_50_3']=w
result=dict(status='INDEPENDENT_TWO_AND_THREE_DIRECTION_IFF_SUPPORTED_BY_PAPER_AND_ACTUAL_LOCAL_WITNESSES',q=9,
 two_direction_iff='ceil(A/q)+ceil(B/q)<=q for nonnegative integer A,B and independent directions',
 three_direction_positive_iff='exists a,b,c in1..q-1: A<=bc,B<=a(q-c),C<=(q-a)(q-b)',
 pair_cases=pair_cases,target19_actual_darts=darts,target19_basis_determinant=determinant,
 three_cases=[{'counts':[12,50,11],'profiles_checked':512,'feasible_profiles':0,'feasible':False},{'counts':[12,50,3],'profiles_checked':512,'feasible_profiles':1,'profile':[8,6,2],'feasible':True,'explicit_lines':65,'actual_disjoint_pins':585}],
 arbitrary_complete_line_unions=True,requires_fixed_W=False,
 local_iff_is_global_all_targets_guarantee=False,remaining_coupling='same source center subset must transport consistently through all six actual darts; independently feasible target line families may have incompatible pullbacks',
 generation_decision='select valid projection supports/slabs first, then transport actual source center subsets across every dart and test simultaneous compatibility; do not optimize only 837/832 counts',
 solver_calls=0,new_point_pool_enumerations=0,old_field_checks=0,old_allrank_checks=0,source_graph_reads=0,BFS_runs=0,Lean_runs=0,new_graphs=0,
 CPU_budget_seconds=3,total_CPU_seconds=time.process_time()-START,all_processes_terminal=True)
(D/'LOCAL_LINE_FAMILY_EXACT_INTERFACE_WITNESSES.json').write_text(json.dumps({'basis':cols,'darts':darts,'witnesses':witnesses},ensure_ascii=False,indent=2)+'\n')
(D/'LOCAL_LINE_FAMILY_EXACT_INTERFACE_RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(D/'LOCAL_LINE_FAMILY_EXACT_INTERFACE_TERMINAL.json').write_text(json.dumps({'status':result['status'],'total_CPU_seconds':result['total_CPU_seconds'],'exit_code':0,'all_processes_terminal':True},indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='target19_actual_darts'},ensure_ascii=False))
print('TARGET19',json.dumps(darts,ensure_ascii=False))
