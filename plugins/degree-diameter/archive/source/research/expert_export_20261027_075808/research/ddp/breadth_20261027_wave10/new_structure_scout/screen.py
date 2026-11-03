from pathlib import Path
from math import comb
import json,time

P=Path(__file__).resolve().parent
ROOT=P.parents[3]
t=time.process_time()
snapshot=ROOT/'context/DD_PORTFOLIO_START_20261026/registry/cases.json'
cases=json.loads(snapshot.read_text())['cases']
q_values=[2,3,4,5,7,8,9,11,13]
cells=[];parameters=[]
for case in cases:
    delta,D,L=case['degree_cap'],case['diameter_cap'],case['baseline_order']
    candidates=[]
    for q in q_values:
        for s in range(1,delta//(q-1)+1):
            degree=s*(q-1)
            volume=sum(comb(s,j)*(q-1)**j for j in range(min(s,D)+1))
            power=1;rank=0
            while rank<s and power*q<=volume:power*=q;rank+=1
            row=dict(target_Delta=delta,target_D=D,savedL=L,q=q,projective_column_directions=s,
                     actual_degree=degree,sphere_covering_order_upper_bound=volume,
                     largest_q_power_allowed_by_bound=power,rank_upper_bound=rank,
                     interpretation='upper bound only; no matrix or code of this order is claimed to exist',
                     can_exceed_savedL_by_necessary_bound=power>L)
            candidates.append(row);parameters.append(row)
    best=max(candidates,key=lambda c:c['largest_q_power_allowed_by_bound'])
    count_bound=max(c['sphere_covering_order_upper_bound'] for c in candidates)
    assert count_bound==sum(comb(delta,j) for j in range(min(delta,D)+1))
    cells.append(dict(Delta=delta,D=D,savedL=L,baseline_as_of=case['baseline_as_of'],
                      binary_volume_upper_bound=count_bound,
                      maximum_field_power_order_upper_bound=best['largest_q_power_allowed_by_bound'],
                      witness_parameter_for_order_bound=dict(q=best['q'],directions=best['projective_column_directions'],rank_upper_bound=best['rank_upper_bound']),
                      order_shortfall_from_savedL=L-best['largest_q_power_allowed_by_bound'],
                      field_direction_parameter_options=len(candidates),
                      capacity_survivors=sum(c['can_exceed_savedL_by_necessary_bound'] for c in candidates)))
assert len(cells)==27 and all(row['capacity_survivors']==0 for row in cells)
out=dict(status='ALL_27_CELLS_LINEAR_CODE_COSET_MECHANISM_ORDER_OBSTRUCTED',
         mechanism='Hamming-graph quotient by a linear code; syndrome Cayley representation',
         ledger_checked='research-wiki/DDP_METHOD_LEDGER.md introduction, family directory, targeted code/Hamming search',
         identical_prior_entry_found=False,
         relation_to_old_work='New explicit code/covering-radius representation, but within the broad abelian Cayley class; not claimed as a new independent construction class.',
         generation=dict(vertices='F_q^r, H is a full-row-rank r by s parity-check matrix with nonzero pairwise nonproportional columns h_i',
                         edges='x--x+a*h_i for every x, i and a in F_q^*',
                         order='q^r',degree='s*(q-1)',diameter='covering radius of ker(H)',
                         complete_routing_condition='Every syndrome is a linear combination of at most D distinct columns of H.'),
         source=dict(title='On nested completely regular codes and distance regular graphs',authors=['J.Borges','J.Rifa','V.A.Zinoviev'],year=2014,
                     primary_url='https://ddd.uab.cat/pub/poncom/2014/142913/intworalg_a2014p85.pdf',
                     read_scope='pp85-89: covering-radius definitions, Section2 Lemmas1/2, explicit nested-code construction and Section4 Theorem3; not only abstract.',
                     binary_source_family=dict(m_even_at_least=4,i_range='1..m/2',vertices='2^(m+i)',degree='2^m-1',diameter=3,
                                               smallest_degree=15,within_goal_degree_range=False),
                     source_scope_note='Source distance-regularity guarantee is for completely regular binary codes. The general q-ary syndrome graph and its distance formula are derived directly here; no q-ary distance-regularity is assumed.'),
         necessary_bound='q^r <= sum_{j=0}^{min(s,D)} binom(s,j)*(q-1)^j; repeated directions and zero columns can be removed without changing the simple graph.',
         prime_powers_considered=q_values,
         all_finite_degree_feasible_q_s_comparisons=len(parameters),cells=cells,parameters=parameters,
         all_27_cells_below_saved_lower_bounds=True,
         CPU_seconds=time.process_time()-t,matrix_assignments_tested=0,codes_generated=0,graphs_generated=0,BFS_performed=False,
         distance_regular_graphs_claimed_as_new=False,pending=[])
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],'CPU',out['CPU_seconds'],'parameter comparisons',len(parameters))
for c in cells:print(c['Delta'],c['D'],'L',c['savedL'],'volume',c['binary_volume_upper_bound'],'q-power bound',c['maximum_field_power_order_upper_bound'],'gap',c['order_shortfall_from_savedL'])
