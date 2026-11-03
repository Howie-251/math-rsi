"""Exact quotient walk arithmetic and conditional q4 degree gate only."""
import collections,json,pathlib,time
P=pathlib.Path(__file__).resolve().parent;start=time.process_time()
def save(n,d):(P/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
Q=[[0,6,0],[2,0,4],[0,4,2]];budgets=[]
for root in range(3):
 rows=[[int(i==root)for i in range(3)]]
 states={(root,t):Q[root][t]for t in range(3)if Q[root][t]}
 rows.append([sum(n for (p,t),n in states.items()if t==v)for v in range(3)])
 for length in range(2,5):
  nxt=collections.Counter()
  for(previous,current),n in states.items():
   for target in range(3):
    ways=Q[current][target]-int(target==previous)
    if ways>0:nxt[current,target]+=n*ways
  states=nxt;rows.append([sum(n for(p,t),n in states.items()if t==v)for v in range(3)])
 budgets.append({'root_type':'ABC'[root],'nonbacktracking_words_by_length_and_target_type':rows,'total_words_by_target_type':[sum(row[t]for row in rows)for t in range(3)],'total':sum(map(sum,rows))})
 assert budgets[-1]['total']==937
save('ROUTE_BUDGET.json',{'status':'EXACT_TYPE_ROUTE_COUNT_ARITHMETIC','source_neighbor_type_matrix':Q,'target_orbit_sizes':[63,189,189],'roots':budgets,
 'interpretation':'Counts of nonbacktracking walks only, not independent endpoint images or a new source diameter verification. No source BFS.',
 'A_A_compression':'For a 3step pointgraph geodesic a-P-R-b with linesL/M/N andQ=thirdpointofM, routeA_a-B(P,L)-C(Q,M)-B(R,N)-A_b haslength4. Shorterpointgraphdistances useABABA orAB A. This only explainsA-A, not everyflagtype pair.',
 'CPU_seconds':time.process_time()-start})
# Exact degree identities for the observed flag operator, valid for any uniform incidence geometry.
# An s+1-point line and t+1 lines through each point give A/B degree s(t+1),Cdegree t(s+1).
rows=[]
for label,A,s,t in [('source_s2_t2',63,2,2),('conditional_unitary_q4_points',208,2,5),('conditional_unitary_q4_dual',416,5,2)]:
 flags=A*(t+1);degrees=[s*(t+1),s*(t+1),t*(s+1)]
 rows.append({'label':label,'A':A,'B':flags,'C':flags,'order':A+2*flags,'line_size':s+1,'lines_per_point':t+1,'degrees_A_B_C':degrees,'max_degree':max(degrees),
 'A_only_split_order':2*A+2*flags,'A_only_split_max_degree_lower_bound':max(degrees[1:]),'within_active_maxdegree12':max(degrees)<=12})
save('Q4_PARAMETER_GATE.json',{'status':'CONDITIONAL_Q4_LITERAL_FLAG_RULE_OUTSIDE_DEGREE_RANGE','operator':'A=points,B/C=flags; A seesotherpoints offlagline;BCcrossusesmarkedpointinotherline, distinctlines;Cinternalclique is samepointpanel.',
 'uniform_formula':{'order':'v+2v(t+1)','degree_A':'s(t+1)','degree_B':'s+st=s(t+1)','degree_C':'st+t=t(s+1)'},'cases':rows,
 'unitary_coordinate_identification_status':'Notattempted. Sourceabstractflaggeometry isexact; itsidentificationwithnaturalHermitianpointsversusdual isnotassumed. Bothnaturalq4orientationcounts failthedegreegate beforethisidentificationcouldhelp.',
 'unitary_parameter_derivation':'PG2(q^2) hasq^4+q^2+1points; nondegenerateHermitianisotropiclocus hasq^3+1, so v=q^2(q^2-q+1). Nonisotropicpointperpline hasq^2+1points ofwhichq+1isotropic, givingr=q(q-1)orthogonalnonisopoints,pairedbyuniquethirdorthogonalpoint into r/2 triads. Atq4: v208, r12, pointdegreeintriadgeometry6,triads416,flags1248. Itsdual interchanges s2/t5 withs5/t2.',
 'no_route_claim':'No q4diameter theorem or q4candidate was generated; degree15 alreadyexceedsDelta<=12. MerelysplittingA cannotlowerB/Cdegrees. Alteringcrossorpanelruleswouldbe anewmechanism requiringfullrouteproof.',
 'CPU_seconds':time.process_time()-start,'source_BFS':0,'q4_graphs_generated':0,'pending':[]})
print('BUDGET',[(a['root_type'],a['total_words_by_target_type'])for a in budgets]);print('PARAMETER',[(a['label'],a['order'],a['degrees_A_B_C'])for a in rows])
