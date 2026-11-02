"""Correct the refuted C-triad panel to the source's actual point panel."""
import collections,json,pathlib,time
P=pathlib.Path(__file__).resolve().parent;start=time.process_time()
def save(n,d):(P/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
save('C_PANEL_PREDICTION.json',{'prediction_id':'P_RAJIV441_C_POINT_PANEL','frozen_before_panel_coordinate_count':True,'falsifiable_prediction':'Each observedCtriangle has one fixedpointP,withits3differentincidenttriadsL. The earlierfixedtriadCtriangleguesswasrefuted;do not silentlyretainit.',
 'source_only':True,'no_new_graph_BFS_or_solver':True})
c=json.load(open(P/'COORDINATES.json'));r=json.load(open(P/'RESULT.json'))
flags={int(v):(x['point'],x['triad'])for v,x in c['C_flags'].items()};triads=c['triads']
records=[]
for group in c['C_triangles']:
 marks={flags[v][0]for v in group};lines={flags[v][1]for v in group};point=next(iter(marks))if len(marks)==1 else None
 expected={i for i,T in enumerate(triads)if point in T}if point is not None else set()
 records.append({'source_C_vertices':group,'marks':sorted(marks),'triads':sorted(lines),'same_point':len(marks)==1,'all_incident_triads':lines==expected})
match=all(a['same_point']and a['all_incident_triads']for a in records)
save('C_PANEL_ACTUAL.json',{'prediction_id':'P_RAJIV441_C_POINT_PANEL','prediction_verdict':'SUPPORTED'if match else'REFUTED','components':records,'CPU_seconds':time.process_time()-start})
r['status']='COMPLETE_EXACT_SOURCE_FLAG_MECHANISM_RECOVERED'if match and r['predicted_BC_equals_actual']else'SOURCE_FLAG_RECONSTRUCTION_INCOMPLETE'
r['flag_prediction']='B_and_BC_MATCH_C_fixedtriad_REFUTED_C_fixedpoint_SUPPORTED'if match else'Cpoint_REFUTED'
r['C_triangles_share_point']=match
r['geometric_rule']='A=points;B/C=two copies offlags(P,L),P inL. A_a--B(P,L) iff a inL minus{P}; B(P,L)--C(Q,M) iffP inM minus{Q} andL!=M; C(P,L)--C(P,M) iffL!=M (samepointclique).'
r['full_source_edges_recovered_from_geometry']=match and r['predicted_BC_equals_actual']
r['q_generalized_operator_degree']='Forline sizes andpointincidences,write eachline s+1points,eachpoint t+1lines. Degrees:A=s(t+1),B=s+st=s(t+1),C=st+t=t(s+1);vertices N_A+2N_A(t+1).'
r['CPU_seconds_source_recovery']=r['CPU_seconds'];r['CPU_seconds_panel_check']=time.process_time()-start
r['pending']=[]
save('RESULT.json',r)
print('POINTPANEL',match,'all63','full1323edge rule',r['full_source_edges_recovered_from_geometry'],'CPU',r['CPU_seconds_panel_check'])
