"""New endpoints73..80 only; scalar published-family gate, no graphs or queries."""
from pathlib import Path
from datetime import datetime,timezone
import math,json,time
HERE=Path(__file__).resolve().parent;start=time.process_time();maximum_cap=80
def prime(n):return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))
def pp(n):
    if n<2:return False
    for p in range(2,n+1):
        if prime(p):
            z=p
            while z<n:z*=p
            if z==n:return True
    return False
def best(xs):return max(xs,key=lambda x:x['n']) if xs else None
qs=[q for q in range(2,maximum_cap) if pp(q)]
IQ=[];Paley=[];direct=[];balanced=[];fold=[];dual=[];products=[]
for q in qs:
    for d in range(maximum_cap-q):
        if d%4 in [0,3]:IQ.append(dict(family='PolarStarIQ',q=q,dprime=d,degree=q+1+d,n=(q*q+q+1)*(2*d+2)))
        if d%2==0 and pp(2*d+1):Paley.append(dict(family='PolarStarPaley',q=q,dprime=d,degree=q+1+d,n=(q*q+q+1)*(2*d+1)))
    for name,s,t in [('balanced',q,q),('Payne',q-1,q+1),('quadric_rectangular',q,q*q),('Hermitian_rectangular',q*q,q**3)]:
        degree=(s+1)*(t+1)
        if degree<=maximum_cap:direct.append(dict(family=name,q=q,s=s,t=t,degree=degree,n=degree*(1+s*t)**2))
    degree=(q+1)**2
    if degree<=maximum_cap:
        O=q*q+1 if q%2==0 else (33 if q==7 else 18 if q==5 else 2*q+1)
        balanced.append(dict(family='publishedSymplecticPartialO_x_spread_generalInducedDuplication',q=q,source_degree=degree,source_n=degree*(q*q+1)**2,partial_ovoid=O,spread=q*q+1,centers=O*(q*q+1)))
for e in range(1,7):
    q=2**e
    if q+1<=maximum_cap and e%2==1:fold.append(dict(family='DelormeFoldedAbsoluteReplication',q=q,source_degree=q+1,source_n=(q+1)*(q*q+1),centers=q*q+1))
    if 3*(q+1)<=maximum_cap:dual.append(dict(family='DelormeStandard12DualityReplication',q=q,source_degree=3*(q+1),source_n=12*(q+1)*(q*q+1),centers=4*(q*q+1)))
for q in [1,2,8,32]:
    for r in [1,2,8,32]:
        d=(q+1)*(r+1)
        if d<=maximum_cap:products.append(dict(family='GQpolarity_x_GQpolarity',q=q,r=r,source_degree=d,source_n=(q+1)*(q*q+1)*(r+1)*(r*r+1),centers=(q*q+1)*(r*r+1)))
    for r in [1]+qs:
        d=(q+1)*(r+1)
        if d<=maximum_cap:products.append(dict(family='GQpolarity_x_projectiveTriangle',q=q,r=r,source_degree=d,source_n=(q+1)*(q*q+1)*(r*r+r+1),centers=(q*q+1)*(r+1)))
def replication(xs,cap):
    a=[]
    for x in xs:
        if x['source_degree']<=cap:
            y=dict(x);y['copies']=cap-y['source_degree'];y['n']=y['source_n']+y['copies']*y['centers'];a.append(y)
    return a
rows=[]
for degree in range(73,81):
    k=degree-64
    iq=[x for x in IQ if x['degree']<=degree];pa=[x for x in Paley if x['degree']<=degree]
    gq=[x for x in direct if x['degree']<=degree]
    b=replication(balanced,degree);f=replication(fold,degree);d=replication(dual,degree);p=replication(products,degree)
    categories=dict(PolarStarIQ=best(iq),PolarStarPaley=best(pa),GQdirect=best(gq),balanced_product_replication=best(b),folded_replication=best(f),standard12_duality_replication=best(d),composed_polarity_replication=best(p))
    strongest=best([x for x in categories.values() if x]);candidate=160050+1650*k;oldP33=160000+1650*k
    upper=151312+2058*(degree-63)
    rows.append(dict(Delta=degree,D=3,k=k,candidate_n=candidate,candidate_m=5121600+105600*k,
        public_P33_guarantee=oldP33,candidate_minus_public_P33=50,current_strongest_checked_public_guarantee=strongest['n'],
        strongest_construction=strongest,candidate_minus_strongest=candidate-strongest['n'],
        passes_checked_public_gate=candidate>strongest['n'],category_maxima=categories,
        IQ_legal_cases=len(iq),Paley_legal_cases=len(pa),standard_Payne_q7_rectangular_upper=upper,
        candidate_minus_standard_Payne_q7_upper=candidate-upper,Payne_q7_upper_is_constructed_lower_bound=False,
        graph_generated_accepted_or_formalized_here=False))
assert all(r['candidate_minus_strongest']==50 for r in rows[:7])
assert rows[7]['strongest_construction']['family']=='Payne'
assert rows[7]['strongest_construction']['q']==8 and rows[7]['current_strongest_checked_public_guarantee']==327680
assert rows[7]['candidate_n']==186450 and rows[7]['candidate_minus_strongest']==-141230
elapsed=time.process_time()-start;assert elapsed<5
out=dict(status='PASS_DEGREES73_TO79_BLOCK_DEGREE80_BY_PUBLISHED_PAYNE_Q8_GQ7_9',checked_UTC=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    requested_window=[73,80],passed_degrees=list(range(73,80)),blocked_degrees=[80],production_eligible_k=list(range(9,16)),
    automatic_production_authorized_by_this_scalar_file=False,endpoints=rows,
    decisive_stop80=dict(published_family='opposite_GQ(q-1,q+1)',q=8,s=7,t=9,degree=80,n=327680,
        formula='(s+1)(t+1)(1+st)^2=8*10*64^2',candidate_n=186450,gain=-141230,
        actual_published_constructed_GQ_premise=True,full_ovoid_or_spread_premise_needed=False),
    additional_stop81=dict(scope='specified direct q8 balanced formula only, no81plus parameter window',q=8,s=8,t=8,degree=81,n=342225,
        candidate_k17=188100,candidate_minus_direct=-154125,earlier_degree80_stop_already_applies=True),
    formula_sources=dict(opposite_GQ='https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2',
        cached_primary_text='arxiv_2608_27253v2.txt',cached_primary_HTML='arxiv_2608_27253v2.html',
        PolarStar='https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf',
        Delorme='https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf',
        public33='https://combinatorialpress.com/article/jcmcc/Volume%20063/vol-063-paper%2012.pdf'),
    private160050_source_used_as_public=False,standard_Payne_q7_upper_report='PAYNE68_FULL_OVOID_SPREAD_CONTINUATION_GATE_20261101.md',
    standard_Payne_q7_upper_does_not_replace_other_q_guarantees=True,
    scalar_CPU_seconds=elapsed,CPU_budget_seconds=5,old_degree65_72_window_rerun=False,
    new_web_queries=0,new_graphs=0,large_graph_reads=0,BFS_runs=0,Lean_runs=0,solver_runs=0,external_reviews=0,wiki_helper_runs=0,
    global_record_or_priority_certified=False,all_local_processes_terminal=True)
(HERE/'P33_CLONE_DEGREE73_80_WINDOW_20261101.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=out['status'],rows=[{k:r[k] for k in ['Delta','k','candidate_n','current_strongest_checked_public_guarantee','candidate_minus_strongest','passes_checked_public_gate']} for r in rows],scalar_CPU_seconds=elapsed),ensure_ascii=False,indent=2))
