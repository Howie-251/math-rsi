"""Finite scalar competition window only: no graph, old-gate execution, or queue."""
import time
START=time.process_time()
from pathlib import Path
from datetime import datetime,timezone
import json,math,resource
resource.setrlimit(resource.RLIMIT_CPU,(5,6))
HERE=Path(__file__).resolve().parent
CAPS=list(range(84,99))
SELECTED=[86,90,94,98]
def prime(n):
    return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))
def pp(n):
    if n<2:return False
    for p in range(2,n+1):
        if not prime(p):continue
        z=p
        while z<n:z*=p
        if z==n:return True
    return False
PPS=[q for q in range(2,99)if pp(q)]
PPSET=set(PPS)
def best(xs):
    return max(xs,key=lambda x:x['n'])if xs else None
def row(family,n,**kw):return dict(family=family,n=n,**kw)
outputs=[]
for cap in CAPS:
    iq=[];pal=[];gq=[];rep=[];fold=[];dual=[];prod=[];upper=[]
    for q in PPS:
        if q>=cap:continue
        for d in range(cap-q):
            if d%4 in (0,3):iq.append(row('PolarStarIQ',(q*q+q+1)*(2*d+2),q=q,dprime=d,degree=q+1+d))
            if d%2==0 and (2*d+1 in PPSET or pp(2*d+1)):
                pal.append(row('PolarStarPaley',(q*q+q+1)*(2*d+1),q=q,dprime=d,degree=q+1+d))
        for name,s,t in [('balanced',q,q),('Payne',q-1,q+1),('rectangular',q,q*q),('Hermitian_rectangular',q*q,q**3)]:
            degree=(s+1)*(t+1)
            if degree<=cap:gq.append(row('oppositeGQ_'+name,degree*(s*t+1)**2,q=q,s=s,t=t,degree=degree))
        degree=(q+1)**2
        if degree<=cap:
            R=q*q+1;p=R if q%2==0 else 33 if q==7 else 18 if q==5 else 2*q+1
            rep.append(row('balanced_published_partialO_spread_replication',degree*R*R+(cap-degree)*p*R,q=q,source_degree=degree,centers=p*R,copies=cap-degree))
    # Published q8 polarity-product plus replication is independently sufficient
    # for this guarantee; no private filled source is used as public input.
    rep.append(row('public_q8_polarity_product_abs_code_replication',cap*4225,q=8,r=8,source_degree=81,source_n=342225,centers=4225,copies=cap-81))
    # This inherited envelope is not promoted to a new existence/literature claim.
    upper.append(row('q8_Payne_fullO64_spread64_replication_conservative_envelope',327680+(cap-80)*4096,source_degree=80,centers=4096,scope='inheritedoptimisticrectangularcomparisonenvelope'))
    if cap>=85:
        direct=85*65*65
        assert direct==359125
        upper.append(row('GQ4_16_rectangular_fullO_spread_replication_envelope',direct+(cap-85)*4225,source_degree=85,source_n=direct,centers=4225,
            scope='bestfull65by65rectangularcodeenvelope;notanupperboundonallcodesandnotnewfullOspreadexistenceclaim'))
    for e in range(1,7):
        q=2**e
        if q+1<=cap and e%2==1:fold.append(row('Delorme_polarity_folded_replication',cap*(q*q+1),q=q,source_degree=q+1,centers=q*q+1))
        if 3*(q+1)<=cap:dual.append(row('Delorme_standard12_duality_replication',4*cap*(q*q+1),q=q,source_degree=3*(q+1),centers=4*(q*q+1)))
    for q in [1,2,8,32]:
        for r in [1,2,8,32]:
            degree=(q+1)*(r+1)
            if degree<=cap:
                centers=(q*q+1)*(r*r+1)
                prod.append(row('GQpolarity_x_GQpolarity_absolute_code_replication',cap*centers,q=q,r=r,source_degree=degree,centers=centers,copies=cap-degree))
        for r in [1]+PPS:
            degree=(q+1)*(r+1)
            if degree<=cap:
                source=(q+1)*(q*q+1)*(r*r+r+1)
                # One fixed triangle coordinate gives a genuine distance>=3
                # code indexed by the GQ absolute vertices. Do not assume all
                # triangle absolutes have disjoint open neighborhoods.
                centers=q*q+1
                prod.append(row('GQpolarity_x_projectiveTriangle_one_coordinate_replication',source+(cap-degree)*centers,q=q,r=r,source_degree=degree,source_n=source,centers=centers))
                upper.append(row('GQpolarity_x_projectiveTriangle_all_absolute_optimistic_envelope',source+(cap-degree)*(q*q+1)*(r+1),q=q,r=r,source_degree=degree,
                    scope='comparisonenvelopeonly;triangleabsoluteproductload1notasserted'))
        # All digon orders are legal, not just prime powers. This source has
        # fewer vertices than relevant GQ factors; use one digon coordinate.
        for a in range(2,cap//(q+1)+1):
            degree=(q+1)*a
            source=(q+1)*(q*q+1)*a
            prod.append(row('GQpolarity_x_digon_one_coordinate_replication',source+(cap-degree)*(q*q+1),q=q,digon_size=a,source_degree=degree,centers=q*q+1))
    maxima={name:best(xs)for name,xs in dict(PolarStarIQ=iq,PolarStarPaley=pal,GQdirect=gq,published_GQ_product_replication=rep,
        Delorme_folded_replication=fold,Delorme_standard12_duality_replication=dual,legal_composed_polarity_replication=prod).items()}
    strongest=best([x for x in maxima.values()if x])
    envelope=best(upper)
    k=cap-81;r=cap-82
    candidate=342290+k*4226;edges=13862745+k*342225
    assert candidate==346516+r*4226==4226*cap-16
    assert strongest['n']==cap*4225
    assert envelope['n']<=strongest['n']
    outputs.append(dict(Delta=cap,D=3,r_additional_role_copies_from_G1=r,k_total_copies_from_H=k,
        candidate_n=candidate,candidate_m=edges,candidate_graph_generated=False,
        best_located_public_guarantee=strongest['n'],candidate_margin=candidate-strongest['n'],
        best_recipe=strongest,category_maxima=maxima,conservative_envelope_maximum=envelope,
        GQ4_16_direct=359125 if cap>=85 else None,
        GQ4_16_rectangular_replication_envelope=cap*4225 if cap>=85 else None,
        candidate_remaining_gain_if_filled_H_and_fullN_copy_public=k,
        candidate_gain_if_same_reallocation_public=0,
        gate='PASS_SCOPED_PRIMARY_FORMULA_WINDOW_ONLY',production_dispatched=False,
        named_scalar_case_counts={key:len(xs)for key,xs in dict(IQ=iq,Paley=pal,GQdirect=gq,replication=rep,folded=fold,duality=dual,polarity=prod,conditional_envelopes=upper).items()}))
chosen=[]
for d in SELECTED:
    x=next(x for x in outputs if x['Delta']==d)
    chosen.append(dict(Delta=d,n=x['candidate_n'],m=x['candidate_m'],public_guarantee=x['best_located_public_guarantee'],margin=x['candidate_margin'],
        decision='WORTH_PRODUCING_AFTER_CURRENT_THREE_TARGET_DELIVERY_ONLY_IF_ROOT_DISPATCHES',
        reason={86:'firstselectednewparameter;testsmultiplicity5usingunchangedG1roleinterface',90:'distributedinteriorparameter;samerecipewithnopublicformulaobstruction',94:'distributedupperinteriorparameter;modestmarginbutnewparameterandsharedproofinterface',98:'finitewindowendpoint;largestmargin82andlargestselectedmultiplicity17'}[d],
        independent_mechanism_claimed=False,production_authorized_by_gate=False))
out=dict(status='FINITE84_98_WINDOW_ALL_PASS_SCOPED_PUBLIC_FORMULAS_NO_PRODUCTION',checked_UTC=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    private_source=dict(n=346516,Delta=82,role_centers=4226,source_n_from_H=342290,source_m_from_H=13862745),
    window=outputs,selected_four_decisions=chosen,
    closed_form=dict(candidate_n='4226*Delta-16',best_located_guarantee='4225*Delta',margin='Delta-16',candidate_m='13862745+(Delta-81)*342225'),
    public_GQ4_16_scope='actualpublishedoppositeGQsource85/359125;full65by65rectangularcopyenvelopeequals4225Deltaanddoesnotblock;noarbitrarypackingupperclaim',
    inherited_triangle_product_scope_clarification='All-absolute triangle Cartesian products are only optimistic comparison envelopes here, not asserted load1/public replication guarantees. Valid single-coordinate codes and actualsource orders are separately included. Neither changes the winning q8xq8 guarantee.',
    bounded_primary_query=dict(batches=1,queries=3,query_text=['"degree diameter" "diameter 3" "98" graph','"359125" graph diameter','"generalized quadrangle" "4,16" spread ovoid'],
        outcome='No strongerwindowconstructionlocated;numericsoftware/csvhitsdiscarded;GQ4_16uniquenesspapersnotnewdegree-diameterrecords',negative_search_certifies_global=False),
    primary_sources=dict(oppositeGQ='https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2',product='https://arxiv.org/html/2608.27253v2#S7.SS4',replication='https://arxiv.org/html/2608.27253v2#S7.SS7',
        Delorme='https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf',PolarStar='https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf'),
    primary_input_files=['arxiv_2608_27253v2.txt','delorme1985_primary_text.txt','polarstar2024_primary_text.txt'],
    attribution_priority='UNKNOWN_SOURCEFILL_AND_CHANGED_RULE;SOURCE_PUBLIC_IF_CONFIRMED_REDUCES_MARGIN_TO_k;SAME_RULE_PUBLIC_ZEROES_MARGIN',
    fixed_R_full_ovoid_source_selection_identity=dict(conditional_n='Delta*(R^2+1)-(s+t)',requires_actual_full_ovoid_and_spread=True,
        balanced8_8_constant=-16,conditional4_16_constant=-20,new_graphs=0,general_code_capacity_upper_claimed=False),
    scope='Onlycap84..98 substitutionsinheritednamedformulasplusoneboundedprimarybatch.Notglobalexhaustion,notallkgraphgeneration,notnewfieldsorspreads.',
    scalar_CPU_seconds=time.process_time()-START,CPU_budget_seconds=5,new_graphs=0,new_validated_instances=0,new_Lean=0,
    BFS_runs=0,field_geometry_or_old_gate_runs=0,solver_calls=0,external_reviews=0,wiki_helper_runs=0,root_counts_modified=False,frozen_packets_modified=False,
    root_snapshot=dict(named=146,parameters=37,Lean=38,scope='Latestrootmessageduringreportwrite;thisgateaddsnoLean'),automatic_production_authorized=False,automatic84plus_queue=False,old83_gate_executed=False,JGT_queried_again=False,all_local_processes_terminal=True)
assert out['scalar_CPU_seconds']<5
(HERE/'Q8_NEW_ROLE_REPLICATION_WINDOW84_98_20261101.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=out['status'],rows=[{k:x[k]for k in ['Delta','candidate_n','candidate_m','best_located_public_guarantee','candidate_margin']}for x in outputs],scalar_CPU_seconds=out['scalar_CPU_seconds']),ensure_ascii=False,indent=2))
