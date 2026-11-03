#!/usr/bin/env python3
"""Independent targeted target48 check; no solver, graph, BFS, Lean or field revalidation."""
import time
START=time.process_time()
import resource
resource.setrlimit(resource.RLIMIT_CPU,(5,5))
import itertools,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
P=json.loads((HERE.parent/'PARAMETERS.json').read_text())
assert (HERE/'THREE_DIRECTION_PRED.md').is_file()
MUL=P['field']['multiplication']; INV=P['inverse_ports'];Q=9
add=lambda a,b:(a%3+b%3)%3+3*((a//3+b//3)%3)
neg=lambda a:(-a%3)%3+3*((-(a//3))%3)
def plus(xs):
 out=0
 for x in xs:out=add(out,x)
 return out
def det(cols):
 a,b,c=cols
 pos=plus([MUL[a[0]][MUL[b[1]][c[2]]],MUL[a[1]][MUL[b[2]][c[0]]],MUL[a[2]][MUL[b[0]][c[1]]]])
 minus=plus([MUL[a[0]][MUL[b[2]][c[1]]],MUL[a[1]][MUL[b[0]][c[2]]],MUL[a[2]][MUL[b[1]][c[0]]]])
 return add(pos,neg(minus))
darts=[]
for u in [17,35,74]:
 port=P['controller'][u].index(48); target_port=INV[port];chart=P['dart_chart_index'][u][port]
 darts.append(dict(source=u,target=48,source_port=port,source_port_name=P['ports'][port],
                   target_port=target_port,target_port_name=P['ports'][target_port],chart=chart,
                   chart_id=P['chart_ids'][chart],matrix=P['matrices'][chart],noise_direction=P['directions'][target_port]))
cols=[d['noise_direction'] for d in darts]
determinant=det(cols)
assert determinant!=0
# Counts in each family are arbitrary subsets of their 2D anchor plane; this small
# table checks the sharp extrema of the proven projection inequalities, not all line sets.
profiles=[]
for a,b,c in itertools.product(range(1,9),repeat=3):
 A=b*c;B=a*(Q-c);C=(Q-a)*(Q-b)
 profiles.append(dict(a=a,b=b,c=c,A=A,B=B,C=C,total=A+B+C,product=A*B*C))
maxsum=max(r['total'] for r in profiles);maxprod=max(r['product'] for r in profiles)
assert len(profiles)==512 and maxsum==73 and maxprod==8000
assert 27*3>maxsum and 27**3>maxprod

def transform(v):return tuple(plus(MUL[v[k]][cols[k][j]] for k in range(3)) for j in range(3))
def witness(a,b,c):
 XG=set(range(a));XB=set(range(Q))-XG;YR=set(range(b));YB=set(range(Q))-YR;ZR=set(range(c));ZG=set(range(Q))-ZR
 anchors=[list(itertools.product(sorted(YR),sorted(ZR))),
          list(itertools.product(sorted(XG),sorted(ZG))),
          list(itertools.product(sorted(XB),sorted(YB)))]
 points=[];actual_points=[]
 for family in range(3):
  lines=[]
  for anchor in anchors[family]:
   line=[]
   for t in range(Q):
    if family==0:v=(t,anchor[0],anchor[1])
    elif family==1:v=(anchor[0],t,anchor[1])
    else:v=(anchor[0],anchor[1],t)
    line.append(v)
   assert len(set(line))==9
   lines.append(set(line))
  union=set().union(*lines)
  assert len(union)==9*len(lines)
  points.append(union)
  transported={transform(v) for v in union}
  assert len(transported)==len(union)
  actual_points.append(transported)
 assert all(not points[i]&points[j] for i,j in itertools.combinations(range(3),2))
 assert all(not actual_points[i]&actual_points[j] for i,j in itertools.combinations(range(3),2))
 counts=[len(a) for a in anchors]
 return dict(a=a,b=b,c=c,line_counts=counts,line_count_sum=sum(counts),line_count_product=counts[0]*counts[1]*counts[2],
             axis_anchors={'x_lines_yz':anchors[0],'y_lines_xz':anchors[1],'z_lines_xy':anchors[2]},
             coordinate_family_pin_counts=[len(x) for x in points],actual_target48_family_pin_counts=[len(x) for x in actual_points],
             pairwise_pin_intersections=[len(actual_points[i]&actual_points[j]) for i,j in itertools.combinations(range(3),2)],
             actual_direction_basis=cols,local_only_not_a_source_center_packing=True)
balanced=witness(5,4,5);sharp_sum=witness(1,1,1)
assert balanced['line_counts']==[20,20,20] and sharp_sum['line_counts']==[1,8,64]
(HERE/'THREE_DIRECTION_WITNESSES.json').write_text(json.dumps({'balanced_product_sharp':balanced,'sum_sharp':sharp_sum},ensure_ascii=False,indent=2)+'\n')
result=dict(status='TARGET48_THREE_DIRECTION_OBSTRUCTION_SUPPORTED',target=48,actual_darts=darts,
            noise_directions_form_basis=True,determinant=determinant,field_encoding=P['field']['encoding'],
            projection_profiles_checked=len(profiles),maximum_positive_three_family_total=maxsum,
            maximum_positive_three_family_product=maxprod,
            sum_maximizers=[r for r in profiles if r['total']==maxsum],
            product_maximizers=[r for r in profiles if r['product']==maxprod],
            proposed_line_counts=[27,27,27],proposed_total=81,proposed_product=19683,
            proposed_837_vector_impossible_for_arbitrary_complete_line_unions=True,
            balanced_witness_counts=balanced['line_counts'],sum_witness_counts=sharp_sum['line_counts'],
            scope='only this837weightvector ruled out by this target; not all weights/fixedWpool/811packing',
            solver_calls=0,source_graph_reads=0,BFS_runs=0,Lean_runs=0,new_graphs=0,old_allranks_field_checks=0,
            CPU_budget_seconds=5,total_CPU_seconds=time.process_time()-START,all_processes_terminal=True)
(HERE/'THREE_DIRECTION_RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(HERE/'THREE_DIRECTION_TERMINAL.json').write_text(json.dumps(dict(status=result['status'],total_CPU_seconds=result['total_CPU_seconds'],exit_code=0,all_processes_terminal=True),indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('sum_maximizers','product_maximizers','actual_darts')},ensure_ascii=False))
print('actual_darts',json.dumps(darts,ensure_ascii=False))
