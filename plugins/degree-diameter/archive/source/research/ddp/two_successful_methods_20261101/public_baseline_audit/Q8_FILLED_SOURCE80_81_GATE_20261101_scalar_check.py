"""Only the two q8 filled-source candidates; scalar published-family gate."""
from pathlib import Path
from datetime import datetime,timezone
import json,math,time
HERE=Path(__file__).resolve().parent;start=time.process_time();capmax=81
def prime(n):return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))
def pp(n):
    if n<2:return False
    for p in range(2,n+1):
        if prime(p):
            z=p
            while z<n:z*=p
            if z==n:return True
    return False
def best(xs):return max(xs,key=lambda r:r['n']) if xs else None
qs=[q for q in range(2,capmax) if pp(q)]
rows=[]
for cap,candidate in [(80,327744),(81,342290)]:
    IQ=[];Paley=[];gq=[];rep=[];fold=[];dual=[];prod=[]
    for q in qs:
        for d in range(cap-q):
            if d%4 in [0,3]:IQ.append(dict(family='PolarStarIQ',q=q,dprime=d,degree=q+1+d,n=(q*q+q+1)*(2*d+2)))
            if d%2==0 and pp(2*d+1):Paley.append(dict(family='PolarStarPaley',q=q,dprime=d,degree=q+1+d,n=(q*q+q+1)*(2*d+1)))
        for name,s,t in [('balanced',q,q),('Payne',q-1,q+1),('quadric_rectangular',q,q*q),('Hermitian_rectangular',q*q,q**3)]:
            delta=(s+1)*(t+1)
            if delta<=cap:gq.append(dict(family='oppositeGQ_'+name,q=q,s=s,t=t,degree=delta,n=delta*(1+s*t)**2))
        delta=(q+1)**2
        if delta<=cap:
            O=q*q+1 if q%2==0 else 33 if q==7 else 18 if q==5 else 2*q+1
            R=q*q+1;rep.append(dict(family='balanced_published_partialO_spread_generalReplication',q=q,source_degree=delta,source_n=delta*R*R,centers=O*R,copies=cap-delta,n=delta*R*R+(cap-delta)*O*R))
    # The q8 full-O/spread interface has just been reproduced. Even its
    # classical unfilled-source replication at81 stays below balancedq8.
    if cap>=80:rep.append(dict(family='q8_Payne_fullO64_spread64_replication_envelope',q=8,source_degree=80,source_n=327680,centers=4096,copies=cap-80,n=327680+(cap-80)*4096,conservative_gate=True))
    for e in range(1,7):
        q=2**e
        if q+1<=cap and e%2==1:fold.append(dict(family='Delorme_folded',q=q,degree=q+1,n=cap*(q*q+1)))
        if 3*(q+1)<=cap:dual.append(dict(family='Delorme_standard12_duality',q=q,degree=3*(q+1),n=4*cap*(q*q+1)))
    for q in [1,2,8,32]:
        for r in [1,2,8,32]:
            delta=(q+1)*(r+1)
            if delta<=cap:prod.append(dict(family='GQpolarity_x_GQpolarity_replication',q=q,r=r,degree=delta,source_n=delta*(q*q+1)*(r*r+1),centers=(q*q+1)*(r*r+1),n=cap*(q*q+1)*(r*r+1)))
        for r in [1]+qs:
            delta=(q+1)*(r+1)
            if delta<=cap:
                source=(q+1)*(q*q+1)*(r*r+r+1);centers=(q*q+1)*(r+1)
                prod.append(dict(family='GQpolarity_x_projectiveTriangle_replication',q=q,r=r,degree=delta,source_n=source,centers=centers,n=source+(cap-delta)*centers))
    cats=dict(PolarStarIQ=best(IQ),PolarStarPaley=best(Paley),GQdirect=best(gq),published_product_replication=best(rep),folded_replication=best(fold),standard12_duality_replication=best(dual),composed_polarity_replication=best(prod))
    strongest=best([x for x in cats.values() if x])
    rows.append(dict(Delta=cap,D=3,conditional_filled_source_n=candidate,strongest_checked_published_guarantee=strongest['n'],candidate_gain=candidate-strongest['n'],strongest_construction=strongest,category_maxima=cats,IQ_legal_cases=len(IQ),Paley_legal_cases=len(Paley),new_graph_generated_or_validated=False))
assert [r['strongest_checked_published_guarantee'] for r in rows]==[327680,342225]
assert [r['candidate_gain'] for r in rows]==[64,65]
chained=327744+4096;assert chained==331840 and chained<342225
elapsed=time.process_time()-start;assert elapsed<5
out=dict(status='PASS_TWO_Q8_SOURCE_GATES_GAIN64_AND65_PRIVATE_PAYNE_TO81_BLOCKED',checked_UTC=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),degree_caps=[80,81],rows=rows,
    private_Payne_filled_to_degree81=dict(source_n=327744,source_degree=80,copy_centers=4096,conditional_n=chained,public_balanced_degree81_n=342225,deficit=10385,status='BLOCKED_BY_REAL_PUBLISHED_BALANCED_SOURCE_NOT_IMPOSSIBILITY',graph_generated=False),
    selection='If root proceeds, source80 is Payne and source81 switches to balanced; no automatic cloning source80 into81.',
    exact_fill_priority=dict(status='UNKNOWN_JGT1985_FULLTEXT_GAP',audit='SPREAD_FILL_SOURCE_PRIORITY_20261101.md',public_same_fill_recipe_confirmed=False,world_SOTA_or_priority_certified=False,
        if_exact_sourcefill_publicly_confirmed='candidate source80/source81 margins may become0, unchanged legality'),
    primary_formula_sources=dict(oppositeGQ='https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2',PolarStar='https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf',Delorme='https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf'),
    current_local_geometry_reproduction='retained_edge_transfer/even_q8_gq_geometry_pilot/',local_filled_source_used_as_public=False,
    scalar_CPU_seconds=elapsed,CPU_budget_seconds=5,new_web_queries=0,old_P33_windows_rerun=False,q8_field_or_geometry_rechecked=False,new_graphs=0,new_validated_graph_instances=0,BFS_runs=0,Lean_runs=0,external_reviews=0,wiki_helper_runs=0,
    root_counts_modified=False,frozen_expert_packets_modified=False,source_generators_only_preparing=True,degree82plus_authorized=False,all_local_processes_terminal=True)
(HERE/'Q8_FILLED_SOURCE80_81_GATE_20261101.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=out['status'],sources=[{k:r[k] for k in ['Delta','conditional_filled_source_n','strongest_checked_published_guarantee','candidate_gain']} for r in rows],blocked_private_Payne_to81=out['private_Payne_filled_to_degree81'],CPU=elapsed),ensure_ascii=False,indent=2))
