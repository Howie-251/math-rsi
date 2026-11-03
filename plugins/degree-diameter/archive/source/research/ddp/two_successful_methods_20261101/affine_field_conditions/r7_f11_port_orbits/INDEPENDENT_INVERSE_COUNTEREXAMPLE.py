"""One actual-chart counterexample, not orbit or full-chart revalidation."""
import json,time
from pathlib import Path

start=time.process_time()
D=Path(__file__).resolve().parent
data=json.loads((D/'PARAMETERS.json').read_text())
chart=next(c for c in data['actual_charts'] if c.get('PGL_coefficients')==[1,1,8,5])
p,q=chart['source_port'],chart['target_port']
assert [data['selected_role_order_points'][p],data['selected_role_order_points'][q]]==[1,4]
a,b,c,d=chart['PGL_coefficients']
assert [a,b,c,d]==[1,1,8,5]
def act(M,x):return [sum(z*y for z,y in zip(row,x))%11 for row in M]
def matmul(A,B):return [[sum(A[i][j]*B[j][k] for j in range(len(B)))%11 for k in range(len(B[0]))] for i in range(len(A))]
def diagQ(Q):return [[1,0,0],[0,Q[0][0],Q[0][1]],[0,Q[1][0],Q[1][1]]]
raw_inverse=[d,(-b)%11,(-c)%11,a]
first=next(x for x in raw_inverse if x)
normalizer=pow(first,-1,11)
normalized=[normalizer*x%11 for x in raw_inverse]
aa,bb,cc,dd=normalized
Q=[[d,c],[b,a]]
Qnormalized_inverse=[[dd,cc],[bb,aa]]
lam=((a*d-b*c)*normalizer)%11
assert lam==6 and matmul(Qnormalized_inverse,Q)==[[lam,0],[0,lam]]
fake_reverse=matmul(matmul(data['H_inverse'][p],diagQ(Qnormalized_inverse)),data['H'][q])
x=act(data['H_inverse'][p],[0,1,0])
y=act(chart['matrix'],x)
correct=act(chart['literal_inverse'],y)
wrong=act(fake_reverse,y)
ell=data['directions'][p]
assert correct==x
assert wrong==[lam*z%11 for z in x]
noise_solutions=[s for s in range(11) if [(wrong[i]+s*ell[i])%11 for i in range(3)]==x]
assert noise_solutions==[]
result={'status':'PREDICTED_NORMALIZED_PGL_INVERSE_FAILURE_CONFIRMED_ON_ONE_ACTUAL_CHART','chart_id':chart['chart_id'],'source_port':p,'target_port':q,'actual_port_orbit_size':data['port_orbit_sizes'][p],'forward_PGL_coefficients':[a,b,c,d],'normalized_projective_inverse_coefficients':normalized,'quotient_inverse_scale_relative_to_true_inverse':lam,'actual_forward_matrix':chart['matrix'],'actual_literal_reverse_matrix':chart['literal_inverse'],'wrong_normalized_inverse_lift':fake_reverse,'source_x':x,'forward_y_with_zero_noise':y,'correct_reverse_y':correct,'wrong_reverse_y':wrong,'wrong_reverse_minus_x':[(wrong[i]-x[i])%11 for i in range(3)],'source_port_direction':ell,'reverse_noise_values_returning_x':noise_solutions,'same_projective_inverse_verified':True,'literal_line_relation_reversal_failed':True,'producer_true_inverse_defect_found':False,'full_chart_or_orbit_classification_rerun':False,'charts_tested':1,'quotient_vector_tested':1,'CPU_seconds':time.process_time()-start,'CPU_budget_seconds':5,'controller_searches_graphs_BFS_Lean_solver':0,'all_local_processes_terminal':True}
(D/'INDEPENDENT_INVERSE_COUNTEREXAMPLE.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
