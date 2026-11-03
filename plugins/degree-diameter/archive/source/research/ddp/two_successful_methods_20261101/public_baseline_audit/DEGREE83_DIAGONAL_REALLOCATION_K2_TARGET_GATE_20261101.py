"""Only cap83: inherited published formulas versus one conditional k2 rule.
No graph generation, old-gate execution, BFS, geometry or solver.
"""
import time
START=time.process_time()
from pathlib import Path
from datetime import datetime,timezone
import json,math,resource
resource.setrlimit(resource.RLIMIT_CPU,(5,6))
HERE=Path(__file__).resolve().parent
CAP=83
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
def best(xs):
    return max(xs,key=lambda r:r['n']) if xs else None

qs=[q for q in range(2,CAP) if pp(q)]
IQ=[];PAL=[];GQ=[];REP=[];FOLD=[];DUAL=[];PROD=[]
for q in qs:
    for d in range(CAP-q):
        if d%4 in (0,3):
            IQ.append(dict(family='PolarStarIQ',q=q,dprime=d,degree=q+1+d,
                           n=(q*q+q+1)*(2*d+2)))
        if d%2==0 and pp(2*d+1):
            PAL.append(dict(family='PolarStarPaley',q=q,dprime=d,degree=q+1+d,
                            n=(q*q+q+1)*(2*d+1)))
    for name,s,t in [('balanced',q,q),('Payne',q-1,q+1),
                      ('quadric_rectangular',q,q*q),('Hermitian_rectangular',q*q,q**3)]:
        delta=(s+1)*(t+1)
        if delta<=CAP:
            GQ.append(dict(family='oppositeGQ_'+name,q=q,s=s,t=t,degree=delta,
                           n=delta*(1+s*t)**2))
    delta=(q+1)**2
    if delta<=CAP:
        O=q*q+1 if q%2==0 else 33 if q==7 else 18 if q==5 else 2*q+1
        R=q*q+1;centers=O*R
        REP.append(dict(family='balanced_published_partialO_spread_generalReplication',
                        q=q,source_degree=delta,source_n=delta*R*R,
                        centers=centers,copies=CAP-delta,
                        n=delta*R*R+(CAP-delta)*centers))
# Inherited conservative q8 Payne envelope, not a newly located numeric table.
REP.append(dict(family='q8_Payne_fullO64_spread64_replication_envelope',q=8,
                source_degree=80,source_n=327680,centers=4096,copies=CAP-80,
                n=327680+(CAP-80)*4096,conservative_gate=True))
for e in range(1,7):
    q=2**e
    if q+1<=CAP and e%2==1:
        FOLD.append(dict(family='Delorme_folded',q=q,source_degree=q+1,n=CAP*(q*q+1)))
    if 3*(q+1)<=CAP:
        DUAL.append(dict(family='Delorme_standard12_duality',q=q,
                         source_degree=3*(q+1),n=4*CAP*(q*q+1)))
# Exactly the already checked known GQ-polarity parameters, not arbitrary PP.
for q in [1,2,8,32]:
    for r in [1,2,8,32]:
        delta=(q+1)*(r+1)
        if delta<=CAP:
            centers=(q*q+1)*(r*r+1)
            PROD.append(dict(family='GQpolarity_x_GQpolarity_replication',q=q,r=r,
                             source_degree=delta,source_n=delta*centers,
                             centers=centers,copies=CAP-delta,n=CAP*centers))
    for r in [1]+qs:
        delta=(q+1)*(r+1)
        if delta<=CAP:
            source=(q+1)*(q*q+1)*(r*r+r+1)
            centers=(q*q+1)*(r+1)
            PROD.append(dict(family='GQpolarity_x_projectiveTriangle_replication',q=q,r=r,
                             source_degree=delta,source_n=source,centers=centers,
                             copies=CAP-delta,n=source+(CAP-delta)*centers))
categories=dict(PolarStarIQ=best(IQ),PolarStarPaley=best(PAL),GQdirect=best(GQ),
                published_product_replication=best(REP),folded_replication=best(FOLD),
                standard12_duality_replication=best(DUAL),composed_polarity_replication=best(PROD))
strongest=best([x for x in categories.values() if x])
R=p=65;delta=81;k=2;centers=p*R;source_n=342290;source_m=13862745
candidate_n=source_n+k*(centers+1)
candidate_m=source_m+k*(delta*centers+R-p)
assert (candidate_n,candidate_m)==(350742,14547195)
public_unfilled=342225+k*4225
assert public_unfilled==350675
public_filled_fullN_if_confirmed=source_n+k*centers
assert public_filled_fullN_if_confirmed==350740
gain=candidate_n-strongest['n']
status=('PASS_SCOPED_DEGREE83_GATE_CANDIDATE_NOT_BLOCKED' if gain>0
        else 'BLOCKED_BY_LOCATED_PUBLISHED_FAMILY_STOP_TARGET')
out=dict(status=status,checked_UTC=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
         Delta=CAP,D=3,conditional_candidate=dict(
             source='accepted private balanced81 filled H',source_n=source_n,source_m=source_m,
             R=R,ovoid_size=p,center_count=centers,uniform_copies=k,hub_count=k,
             n=candidate_n,m=candidate_m,rule='Each clone uses only original U-neighbors; each hub meets all65 original fillers; all H edges retained',
             degree_cap=83,graph_generated=False,repeat_same_center_clones=True,
             no_new_7532_or_346516_validation=True),
         strongest_checked_published_guarantee=strongest['n'],strongest_recipe=strongest,
         published_unfilled_q8_fullO_k2_guarantee=public_unfilled,
         strongest_versus_unfilled_guarantee_consistent=strongest['n']==public_unfilled,
         candidate_gain_over_best_located= gain,
         category_maxima=categories,legal_IQ_cases=len(IQ),legal_Paley_cases=len(PAL),
         q8_Payne_replication_envelope=next(x for x in REP if x['family']=='q8_Payne_fullO64_spread64_replication_envelope'),
         legal_direct_GQ_cases=len(GQ),legal_published_replication_cases=len(REP),
         legal_composed_polarity_cases=len(PROD),
         strongest_public_attribution=dict(
             formula='585^2+2*65^2=350675',base_degree=81,copies=2,
             primary='Isham et al.2026v2 sections7.4/7.7 with Delorme1985 replication',
             literal_degree83_numeric_edge_table_located=False,
             value_is_scalar_consequence_of_published_methods_not_a_located_printed_record=True),
         scope='Only cap83: all legal scalar substitutions in inherited named formulas plus one three-primary-query batch. Not global exhaustion or a degree83 world record table.',
         bounded_primary_query=dict(batches=1,queries=3,
             query_text=['"degree diameter" "83" "diameter 3"','"350742" graph diameter','"350675" graph diameter replication'],
             domains=['arxiv.org','github.com','upc.edu','ethz.ch'],
             outcome='No relevant matching construction or stronger83 result located; unrelated SVG IDs, repository ticket IDs and UPC numeric handles discarded',
             negative_search_proves_global_optimality=False),
         exact_priority=dict(status='UNKNOWN_INHERITED_SOURCEFILL_AND_CHANGED_RULE_ATTRIBUTION',
             source_audit='SPREAD_FILL_SOURCE_PRIORITY_20261101.md',
             changed_rule_audit='DIAGONAL_FILL_REALLOCATION_TARGETED_QUERY_20261101.md',
             JGT1985_gap_researched_again=False,
             if_filled_H_and_standard_fullN_replication_public=dict(public_n=350740,candidate_remaining_gain=2),
             if_same_diagonal_reallocation_rule_already_public=dict(public_n=350742,candidate_gain=0),
             global_record_certified=False),
         primary_sources=dict(
             product_and_replication='https://arxiv.org/html/2608.27253v2#S7.SS7',
             opposite_GQ='https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2',
             PolarStar='https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf',
             Delorme='https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf'),
         cached_primary_inputs=['arxiv_2608_27253v2.txt','polarstar2024_primary_text.txt','delorme1985_primary_text.txt'],
         scalar_CPU_seconds=time.process_time()-START,CPU_budget_seconds=5,
         old82_gate_executed=False,new_graphs=0,new_validated_instances=0,field_or_geometry_retests=0,
         BFS_runs=0,Lean_runs=0,solver_calls=0,external_reviews=0,wiki_helper_runs=0,
         root_counts_modified=False,frozen_expert_packets_modified=False,automatic_degree84plus=False,
         production_authorized_by_this_gate=False,all_local_processes_terminal=True)
assert out['scalar_CPU_seconds']<5
(HERE/'DEGREE83_DIAGONAL_REALLOCATION_K2_TARGET_GATE_20261101.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','conditional_candidate','strongest_checked_published_guarantee','candidate_gain_over_best_located','category_maxima','scalar_CPU_seconds']},ensure_ascii=False,indent=2))
