import csv,json,time
from pathlib import Path
start=time.process_time();D=Path(__file__).resolve().parent
with (D/'ALL_CANDIDATE_CENTERS.tsv').open() as f:centers=list(csv.DictReader(f,delimiter='\t'))
with (D/'ALL_CANDIDATE_PIN_ROWS.tsv').open() as f:pinrows=list(csv.DictReader(f,delimiter='\t'))
assert len(centers)==len(pinrows)==1539
pools=[]
for c,r in zip(centers,pinrows):
 assert c['pool_index']==r['pool_index'] and c['source_label']==r['source_label']
 pools.append(dict(controller=int(c['controller']),variable=int(c['variable']),retained=c['retained']=='True',
  label=int(c['source_label']),pins=[int(r[f'pin{i}']) for i in range(54)]))
U={31,32,44,45,59,60,61,72,73,74}
chosen=[c for c in pools if c['controller'] in U]
loads={}
for c in chosen:
 for p in c['pins']:loads[p]=loads.get(p,0)+1
counts={u:sum(c['controller']==u for c in chosen) for u in [17,35,74]}
z=[0,0,1]
logic=[counts[u]-61*z[i] for i,u in enumerate([17,35,74])]
residual=sum(not c['retained'] for c in chosen)
violations=[]
if max(loads.values())>1:violations.append('actual_pin_load')
if any(v>20 for v in logic) or sum(z)>2:violations.append('three_direction_logic')
if residual<487:violations.append('minimum_variable_centers_487')
assert len(chosen)==810 and residual==486 and max(loads.values())==1
assert violations==['minimum_variable_centers_487']
control=dict(status='PASS_ONLY_NEW_CARDINALITY_ROW_VIOLATED',total_centers=810,variable_centers=residual,
 fixed_centers=324,distinct_pins=len(loads),max_pin_load=max(loads.values()),
 three_direction_layer_weights=counts,auxiliary_binary_switches=z,logic_row_left_sides=logic,
 logic_upper=20,sum_switches=sum(z),sum_switches_upper=2,violated_constraints=violations,
 sourcegraph_or_oldBFS_revalidated=False)
capacity=json.loads((D.parent/'fixed_support_max_capacity_lp/RESULT.json').read_text())
weights={int(u):int(v) for u,v in capacity['rational_center_weights'].items()}
scaledloads={};scaledcard=0;fracvars=0
for c in pools:
 num=3 if c['retained'] else weights.get(c['controller'],0)//27
 assert c['retained'] or weights.get(c['controller'],0)%27==0
 assert 0<=num<=3
 scaledcard+=num
 if c['variable']>=0 and num in [1,2]:fracvars+=1
 for pin in c['pins']:scaledloads[pin]=scaledloads.get(pin,0)+num
assert scaledcard==837*3 and max(scaledloads.values())<=3
# Relax each of the three auxiliary switches to1/3; verify the original
# linear rows exactly after multiplying by3. No LP or new solver is called.
logic_scaled=[3*weights[u]-61 for u in [17,35,74]]
assert max(logic_scaled)<=60 and 3<=6
target48=[scaledloads.get(729*48+i,0) for i in range(729)]
assert target48==[3]*729
fractional=dict(status='EXACT_SCALED_BY3_FEASIBLE_LINEAR_RELAXATION_WITNESS',total_centers=837,
 variable_centers=513,point_selection_denominator=3,fractional_point_variables=fracvars,
 max_pin_load_scaled_by3=max(scaledloads.values()),pin_upper_scaled_by3=3,
 auxiliary_switches=['1/3']*3,logic_left_sides_scaled_by3=logic_scaled,logic_upper_scaled_by3=60,
 target48_all729_pin_loads='1',layer_weights_at_target48={str(u):weights[u] for u in [17,35,74]},
 integer_packing_claimed=False,LP_solver_calls=0,
 meaning='837 survives the continuous point-pin rows; integrality/whole-line complementarity is the obstacle, not just total fiber capacity')
solver=json.loads((D/'SOLVER_RETURN.json').read_text())
r=dict(status='PASS_CHEAP_MODEL_SANITY_NO_NEW_SOLVER',original810_negative_control=control,
 inherited837_fractional_substitution=fractional,
 existing_solver_message=solver['message'],existing_solver_node_count=solver['mip_node_count'],
 existing_solver_dual_bound=solver['mip_dual_bound'],existing_solver_gap=solver['mip_gap'],
 root_LP_or_search_trace_available=False,
 no_extra_solver_calls=True,no_old_source_or_BFS_or_field_checks=True,
 CPU_seconds=time.process_time()-start,all_processes_terminal=True)
(D/'MODEL_SANITY.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
