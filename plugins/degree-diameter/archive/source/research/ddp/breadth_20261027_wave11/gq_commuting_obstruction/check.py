"""Exact integer substitutions for the paper obstruction; no graph construction."""
from pathlib import Path
import json,sys,time
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
sys.path.insert(0,str(ROOT/'aris_repo/tools'))
from capture_filter import screen
start=time.process_time()
cases=[]
for q,p,s,L in [(3,1,1,72),(5,2,2,253),(7,3,3,715),(8,2,3,810)]:
    N=(q+1)*(q*q+1)
    terms=dict(merged_endpoint_internal_routes=p*q*q,
               opposite_side_internal_relay=s*q*(q+1),
               internal_two_steps=p*(p-1),internal_three_steps=p*(p-1)**2)
    upper=sum(terms.values())
    assert upper<q**3
    deficit=q**3-upper
    cases.append(dict(q=q,side_order=N,n=2*N,target_D=3,target_Delta=q+1+s,savedL=L,
                      commuting_side_degree=p,other_side_max_degree=s,
                      far_targets_per_root=q**3,pointwise_capacity_upper_bound=upper,
                      terms=terms,uncovered_far_targets_per_commuting_side_root_at_least=deficit,
                      unordered_bad_pairs_on_commuting_side_at_least=(N*deficit+1)//2,
                      obstruction='D3 impossible if either side commutes with its closed collinearity matrix',
                      scope='max-degree-3 near-regular allowed; commutation forces regular degree<=2 on an odd side' if q==8 else 'original equal-r-regular scope, also valid if other side has maximum degree<=r'))
x=dict(status='PAPER_DERIVATION_COMPLETE_NO_GRAPH_SEARCH',
       claim='If P is a simple undirected internal adjacency and PC=CP, the endpoint-internal path supports merge; arbitrary other-side internal Q of maximum degree<=s need not commute.',
       formula=dict(equal_degree_upper='r*q^2 + r*q*(q+1) + r*(r-1) + r*(r-1)^2',
                    mixed_degree_upper='p*q^2 + s*q*(q+1) + p*(p-1) + p*(p-1)^2',
                    type='pointwise on the commuting side, after commutation forces degree p to be constant'),
       algebra=dict(C_square='C^2=q^2*I+(q+1)*J',
                    regularity='PC=CP implies P*J=J*P; since P is undirected this makes all vertex degrees equal',
                    support='support(P*C)=support(C*P), including restriction to far targets',
                    automorphism_subclass='P=sum of collinearity-automorphism permutation matrices only when the sum is symmetric, has zero diagonal, and already has entries in {0,1}; this sum commutes with C',
                    excluded_generalization='Deleting loops or thresholding multiplicities need not preserve commutation; arbitrary automorphism-derived deduplicated graphs are not excluded without checking PC=CP'),
       cases=cases,
       max_degree_scope_note='Parity is only an obstruction to exact regularity. In particular q8 max3 internal graphs with one degree2 vertex remain legal; noncommuting choices on both sides are unresolved.',
       residual_status=dict(q3r1='one separate complete finite MILP was UNKNOWN with no incumbent; not rerun',
                            q5r2='existing two-start finite profile D4/4090 bad; not rerun or generalized to all choices',
                            q7r3='no graph construction or search',q8max3='no graph construction or search; open noncommuting near-regular case'),
       evidence=['research/ddp/breadth_20261027_wave11/gq_internal_capacity/REPORT.md',
                 'research/ddp/breadth_20261027_wave11/gq80_paired_matchings/terminal.json',
                 'research/ddp/breadth_20261027_wave10/gq312_internal_cycles/best.independent_check.json'],
       review_scope='Self-contained same-model paper derivation; no external-review or formal-proof claim',
       graph_generation_count=0,BFS_count=0,solver_calls=0,new_lower_bounds=0,
       CPU_seconds=time.process_time()-start)
text=json.dumps(x,indent=2)+'\n'
assert not screen(text)
(OUT/'RESULT.json').write_text(text)
print(json.dumps(cases,indent=2))
