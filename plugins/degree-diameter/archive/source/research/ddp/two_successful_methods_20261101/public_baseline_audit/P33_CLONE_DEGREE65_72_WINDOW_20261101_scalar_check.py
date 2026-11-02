"""Eight fixed degree endpoints; scalar reuse of already-read primary formulas only."""
from pathlib import Path
from datetime import datetime,timezone
import json,time

HERE=Path(__file__).resolve().parent
start=time.process_time()
previous=json.loads((HERE/'DEGREE77_R7_F11_TARGET_GATE_20261101.json').read_text())
rows=[]
def best(items):
    return max(items,key=lambda x:x['n']) if items else None
for degree in range(65,73):
    k=degree-64
    candidate=160050+1650*k
    IQ=[x for x in previous['PolarStar_IQ_all'] if x['degree']<=degree]
    Paley=[x for x in previous['PolarStar_Paley_all'] if x['degree']<=degree]
    direct=[x for x in previous['known_opposite_GQ_direct'] if x['degree']<=degree]
    balanced=[]
    for x in previous['published_balanced_ovoid_spread_duplications']:
        if x['source_degree']>degree:continue
        y=dict(x)
        # The original cap77 snapshot used a general odd-q bound. Both of
        # these small-q computational lower bounds are actually in Table5.
        if x['q']==7:y['published_ovoid_or_partial_size']=33
        if x['q']==5:y['published_ovoid_or_partial_size']=18
        y['centers']=y['published_ovoid_or_partial_size']*y['spread_size']
        y['copies']=degree-y['source_degree'];y['degree_cap']=degree
        y['n']=y['source_n']+y['copies']*y['centers'];balanced.append(y)
    categories={}
    for key in ['Delorme_folded_absolute_replication','Delorme_q16_standard12_duality_replication','composed_polarity_products']:
        a=[]
        for x in previous[key]:
            if x['source_degree']>degree:continue
            y=dict(x);y['copies']=degree-y['source_degree']
            center=y.get('absolute_centers',y.get('centers'))
            y['n']=y['source_n']+y['copies']*center;a.append(y)
        categories[key]=a
    guarantees=[best(IQ),best(Paley),best(direct),best(balanced)]+[best(v) for v in categories.values()]
    strongest=best([g for g in guarantees if g])
    payne=151312+2401*(degree-63)
    row=dict(Delta=degree,D=3,k=k,candidate_n=candidate,candidate_m=5121600+105600*k,
             current_published_method_guarantee=strongest['n'],candidate_minus_guarantee=candidate-strongest['n'],
             strongest_comparison=strongest,PolarStar_IQ_best=best(IQ),PolarStar_Paley_best=best(Paley),
             PolarStar_IQ_legal_cases=len(IQ),PolarStar_Paley_legal_cases=len(Paley),
             known_GQ_direct_best=best(direct),published_balanced_product_replication_best=best(balanced),
             Delorme_folded_best=best(categories['Delorme_folded_absolute_replication']),
             Delorme_standard12_duality_best=best(categories['Delorme_q16_standard12_duality_replication']),
             composed_polarity_product_best=best(categories['composed_polarity_products']),
             Payne63_most_favorable_specific_packing_upper=payne,candidate_minus_Payne_packing_upper=candidate-payne,
             Payne_expression_is_constructed_public_lower_bound=False,
             any_checked_public_guarantee_at_least_candidate=strongest['n']>=candidate,
             graph_production_acceptance_or_formalization_claimed_here=False)
    assert strongest['n']==160000+1650*k and row['candidate_minus_guarantee']==50
    assert candidate>payne
    rows.append(row)
elapsed=time.process_time()-start
assert elapsed<5
out=dict(status='PASS_FIXED_P33_DEGREE65_72_ALL_EIGHT_POSITIVE50_AGAINST_CHECKED_PUBLISHED_FAMILIES',
         checked_UTC=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),window=[65,72],
         endpoints=rows,shared_candidate_recipe=dict(source_n=160050,source_edges=5121600,source_degree=64,
             public33_times50_centers=1650,neighborhood_size=64,clones_per_center='k=1..8',
             n='160050+1650k',m='5121600+105600k',candidate_not_used_as_public=True),
         public_recipe=dict(source_n=160000,source_degree=64,partial_ovoid=33,spread=50,
             n='160000+1650k',kind='direct composition of published premises and general matching duplication, not separate published numeric edgefile'),
         Payne_upper_scope=dict(expression='151312+2401*(Delta-63)',
             scope='most favorable upper envelope for this specified fullO/spread product packing, not all Payne augmentations',
             full_ovoid_and_spread_premises_confirmed_here=False,constructed_public_lower_bound=False,
             at_degree72=172921,candidate_degree72=173250,remaining_gap=329),
         new_parameter_pairs_if_accepted=[66,67,68,69,71,72],old_representative_pairs_if_improved=[65,70],
         source_formula_snapshot='DEGREE77_R7_F11_TARGET_GATE_20261101.json historical formula arrays, degree<=cap re-evaluation only',
         sources=dict(PolarStar='https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf',
             Delorme='https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf',
             GQ_formula_and_polarity_product='https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2',
             W3F7_primary33='https://combinatorialpress.com/article/jcmcc/Volume%20063/vol-063-paper%2012.pdf'),
         scalar_CPU_seconds=elapsed,CPU_budget_seconds=5,new_primary_query_batches=0,new_web_queries=0,
         new_graphs=0,large_graph_reads=0,BFS_runs=0,Lean_runs=0,solver_runs=0,external_reviews=0,
         wiki_helper_runs=0,degrees73_and_above_checked=False,global_record_or_priority_certified=False,
         scope_gaps=['not an exhaustive global literature audit','arbitrary induced augmentations are not optimized',
                     'Payne upper only bounds the specified full-product packing mechanism, not all mechanisms'],
         all_local_processes_terminal=True)
(HERE/'P33_CLONE_DEGREE65_72_WINDOW_20261101.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=out['status'],rows=[{k:r[k] for k in ['Delta','candidate_n','candidate_m','current_published_method_guarantee','candidate_minus_guarantee','Payne63_most_favorable_specific_packing_upper','candidate_minus_Payne_packing_upper']} for r in rows],scalar_CPU_seconds=elapsed),ensure_ascii=False,indent=2))
