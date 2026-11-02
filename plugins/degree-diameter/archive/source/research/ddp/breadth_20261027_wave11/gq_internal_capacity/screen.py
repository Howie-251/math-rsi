#!/usr/bin/env python3
"""Finite arithmetic screen only: no geometry construction or graph traversal."""
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'aris_repo/tools'))
from capture_filter import screen

started = time.process_time()
baseline_path = ROOT / 'context/DD_PORTFOLIO_START_20261026/registry/cases.json'
snapshot = json.loads(baseline_path.read_text())
baselines = {(c['degree_cap'], c['diameter_cap']): c['baseline_order'] for c in snapshot['cases']}
rows = []
for q in [2, 3, 4, 5, 7, 8, 9, 11]:
    N = (q+1)*(q*q+1)
    for r in range(12-q):
        delta = q+1+r
        terms = dict(internal_then_incidence_average=r*q*q,
                     incidence_then_internal_average=r*q*q,
                     opposite_side_internal_relay=r*q*(q+1),
                     pure_internal_two_steps=r*(r-1),
                     pure_internal_three_steps=r*(r-1)**2)
        U = sum(terms.values())
        regular_possible = r < N and (N*r)%2 == 0
        comparisons = [dict(target_D=D, savedL=baselines.get((delta, D)),
                            strict_order_improvement=(2*N > baselines[(delta,D)]) if (delta,D) in baselines else None,
                            routing_guarantee='D<=4 from retained incidence graph' if D>=4 else 'D3 requires additional coverage')
                       for D in [3,4,5]]
        L3 = baselines.get((delta,3))
        improvement = L3 is not None and 2*N>L3
        capacity_pass = U>=q**3
        if not regular_possible:
            status = 'REGULARITY_PARITY_IMPOSSIBLE'
        elif not 4 <= delta <= 12:
            status = 'OUTSIDE_ACTIVE_DEGREE_RANGE'
        elif not improvement:
            status = 'NO_STRICT_D3_ORDER_IMPROVEMENT'
        elif not capacity_pass:
            status = 'D3_AVERAGE_CAPACITY_IMPOSSIBLE'
        elif (q,r)==(5,2):
            status = 'NECESSARY_PASS_ALREADY_TESTED_FINITE_PROFILE_FAILED'
        else:
            status = 'NECESSARY_PASS_NO_GRAPH_CONSTRUCTED'
        rows.append(dict(q=q,r=r,side_order=N,n=2*N,degree=delta,target_D=3,
                         savedL=L3,far_targets_per_root=q**3,average_capacity_upper_bound=U,
                         capacity_terms=terms,capacity_margin=U-q**3,
                         capacity_pass=capacity_pass,regularity_parity_possible=regular_possible,
                         active_degree_range=4<=delta<=12,strict_D3_order_improvement=improvement,
                         status=status,all_target_comparisons=comparisons))
survivors = [r for r in rows if r['regularity_parity_possible'] and r['active_degree_range'] and r['strict_D3_order_improvement'] and r['capacity_pass']]
max_degree_survivors = [r for r in rows if r['active_degree_range'] and r['strict_D3_order_improvement'] and r['capacity_pass']]
summary = dict(parameter_pairs=len(rows),legal_by_regular_graph_parity=sum(r['regularity_parity_possible'] for r in rows),
               active_legal_pairs=sum(r['regularity_parity_possible'] and r['active_degree_range'] for r in rows),
               strict_D3_order_improving_pairs=sum(r['strict_D3_order_improvement'] for r in rows),
               legal_strict_D3_order_improving_pairs=sum(r['regularity_parity_possible'] and r['strict_D3_order_improvement'] for r in rows),
               legal_strict_D3_necessary_passes=len(survivors),
               legal_strict_D3_capacity_excluded=sum(r['regularity_parity_possible'] and r['strict_D3_order_improvement'] and not r['capacity_pass'] for r in rows),
               D4_or_D5_strict_order_improvements=sum(c['strict_order_improvement'] is True for r in rows for c in r['all_target_comparisons'] if c['target_D'] in (4,5)))
result = dict(status='COMPLETE_NECESSARY_CAPACITY_SCREEN_NO_GRAPH_SEARCH',
              mechanism='GQ(q,q) incidence retained; arbitrary simple r-regular internal graph on each side',
              baseline_snapshot=str(baseline_path.relative_to(ROOT)),baseline_as_of=snapshot['snapshot_date'],
              scope=dict(q='prime powers 2<=q<=11',degree_cap=12,r='integer 0<=r<=11-q; Nr even required',
                         graph_order='2(q+1)(q^2+1)',graph_degree='q+1+r',target_diameter=3),
              formula=dict(far='q^3',upper='2*r*q^2 + r*q*(q+1) + r*(r-1) + r*(r-1)^2',
                           simplified_upper='3*r*q^2 + r*q + r^2*(r-1)',
                           type='average over all roots in one bipartition side; necessary only'),
              summary=summary,necessary_passes=[{k:r[k] for k in ('q','r','n','degree','target_D','savedL','far_targets_per_root','average_capacity_upper_bound','status')} for r in survivors],
              max_degree_relaxation=dict(
                  scope='Allow arbitrary simple internal graphs of maximum degree at most r on each side. The same average U bound remains valid; parity is not an obstruction to this larger scope.',
                  proof='The CA far route total is 2*m_P*q^2 <= N*r*q^2. All other upper bounds already use degree upper bounds only.',
                  strict_D3_order_improving_pairs=19,capacity_excluded_pairs=15,
                  necessary_passes=[{k:r[k] for k in ('q','r','n','degree','savedL','far_targets_per_root','average_capacity_upper_bound')} for r in max_degree_survivors],
                  important_open_case=dict(q=8,internal_max_degree=3,n=1170,graph_max_degree=12,savedL=810,
                      status='NECESSARY_PASS_NEAR_REGULAR_CHOICES_NOT_SEARCHED',
                      detail='Each side has 585 vertices. An internal graph may have one degree-2 vertex and 584 degree-3 vertices. Exact 3-regular parity failure does not exclude this maximum-degree template.'),
                  followup='research/ddp/breadth_20261027_wave11/gq_commuting_obstruction/REPORT.md'),
              existing_profile=dict(path='research/ddp/breadth_20261027_wave10/gq312_internal_cycles/best.independent_check.json',
                                    q=5,r=2,n=312,degree=8,actual_D=4,bad_unordered_pairs_gt3=4090,
                                    verification='root independent all-312-root BFS already completed; not rerun',
                                    scope='two finite internal-2-factor search starts only, not all 2-regular internal choices'),
              positive_routing_basis='Retaining all GQ incidence edges keeps every opposite-side pair within 3 and every collinear same-side pair within 2, and gives full D<=4. Far same-side pairs are the only D3 obligation.',
              graph_generation_count=0,BFS_count=0,parameter_search_proposals=0,new_lower_bounds=0,
              parameters=rows)
result['CPU_seconds']=time.process_time()-started
payload=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
assert not screen(payload)
(OUT/'RESULT.json').write_text(payload)
print(json.dumps(dict(summary=summary,necessary_passes=result['necessary_passes'],CPU_seconds=result['CPU_seconds']),ensure_ascii=False,indent=2))
