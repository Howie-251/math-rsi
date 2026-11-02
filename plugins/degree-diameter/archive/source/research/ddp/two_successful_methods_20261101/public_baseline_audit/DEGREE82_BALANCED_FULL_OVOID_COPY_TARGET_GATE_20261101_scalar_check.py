"""Only degree82: published formula scalar comparison; no graph or old-gate execution."""
from pathlib import Path
from datetime import datetime,timezone
import json,math,time,resource
START=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(5,5))
HERE=Path(__file__).resolve().parent;CAP=82

def prime(n):return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))
def pp(n):
 if n<2:return False
 for p in range(2,n+1):
  if not prime(p):continue
  z=p
  while z<n:z*=p
  if z==n:return True
 return False
def best(xs):return max(xs,key=lambda r:r['n']) if xs else None
qs=[q for q in range(2,CAP) if pp(q)]
IQ=[];PAL=[];GQ=[];REP=[];FOLD=[];DUAL=[];PROD=[]
for q in qs:
 for d in range(CAP-q):
  if d%4 in (0,3):IQ.append(dict(family='PolarStarIQ',q=q,dprime=d,degree=q+1+d,n=(q*q+q+1)*(2*d+2)))
  if d%2==0 and pp(2*d+1):PAL.append(dict(family='PolarStarPaley',q=q,dprime=d,degree=q+1+d,n=(q*q+q+1)*(2*d+1)))
 for name,s,t in [('balanced',q,q),('Payne',q-1,q+1),('quadric_rectangular',q,q*q),('Hermitian_rectangular',q*q,q**3)]:
  deg=(s+1)*(t+1)
  if deg<=CAP:GQ.append(dict(family='oppositeGQ_'+name,q=q,s=s,t=t,degree=deg,n=deg*(1+s*t)**2))
 deg=(q+1)**2
 if deg<=CAP:
  o=q*q+1 if q%2==0 else 33 if q==7 else 18 if q==5 else 2*q+1
  spread=q*q+1;centers=o*spread
  REP.append(dict(family='balanced_published_partialO_spread_generalReplication',q=q,source_degree=deg,source_n=deg*spread**2,centers=centers,copies=CAP-deg,n=deg*spread**2+(CAP-deg)*centers))
REP.append(dict(family='q8_Payne_fullO64_spread64_replication_envelope',q=8,source_degree=80,source_n=327680,centers=4096,copies=2,n=327680+2*4096,conservative_gate=True))
for e in range(1,7):
 q=2**e
 if q+1<=CAP and e%2==1:FOLD.append(dict(family='Delorme_folded',q=q,source_degree=q+1,n=CAP*(q*q+1)))
 if 3*(q+1)<=CAP:DUAL.append(dict(family='Delorme_standard12_duality',q=q,source_degree=3*(q+1),n=4*CAP*(q*q+1)))
# Only already verified polarity parameters; never assume arbitrary prime powers admit GQ polarity.
for q in [1,2,8,32]:
 for r in [1,2,8,32]:
  deg=(q+1)*(r+1)
  if deg<=CAP:PROD.append(dict(family='GQpolarity_x_GQpolarity_replication',q=q,r=r,source_degree=deg,source_n=deg*(q*q+1)*(r*r+1),centers=(q*q+1)*(r*r+1),copies=CAP-deg,n=CAP*(q*q+1)*(r*r+1)))
 for r in [1]+qs:
  deg=(q+1)*(r+1)
  if deg<=CAP:
   source=(q+1)*(q*q+1)*(r*r+r+1);centers=(q*q+1)*(r+1)
   PROD.append(dict(family='GQpolarity_x_projectiveTriangle_replication',q=q,r=r,source_degree=deg,source_n=source,centers=centers,copies=CAP-deg,n=source+(CAP-deg)*centers))
categories=dict(PolarStarIQ=best(IQ),PolarStarPaley=best(PAL),GQdirect=best(GQ),published_product_replication=best(REP),folded_replication=best(FOLD),standard12_duality_replication=best(DUAL),composed_polarity_replication=best(PROD))
strongest=best([x for x in categories.values() if x]);source_n=342290;source_m=13862745;centers=65*65
candidate_n=source_n+centers;candidate_m=source_m+81*centers
assert (candidate_n,candidate_m)==(346515,14204970)
public=342225+centers
assert strongest['n']==public==346450
out=dict(status='PASS_SINGLE_DEGREE82_GATE_BEST_LOCATED346450_CANDIDATE_GAIN65_PRIORITY_UNKNOWN',checked_UTC=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),Delta=82,D=3,
 candidate=dict(source='mathematically accepted private balanced81 filledsource',source_n=source_n,source_m=source_m,centers=centers,immutable_N_size=81,copy_count=1,n=candidate_n,m=candidate_m,graph_generated=False,source_is_Payne=False),
 strongest_checked_published_guarantee=public,candidate_gain=candidate_n-public,
 strongest_public_recipe=dict(base_family='publishedq8xq8GQpolarityproduct',q=8,r=8,base_degree=81,base_n=342225,absolute_points=4225,copies=1,new_degree=82,new_n=public,source='arxiv2608.27253v2 sections7.4/7.7; Delorme replication',separate_numeric_edgefile_located=False),
 category_maxima=categories,IQ_legal_cases=len(IQ),Paley_legal_cases=len(PAL),
 literal_primary_degree82_table_located=False,author_repo_degree82_entry_located=False,
 located_public_construction_at_least_candidate=False,gate_scope='all legal scalar substitutions in inherited listed formulas plus one3queryprimarybatch/currentauthorrepository; not global exhaustion',
 exact_sourcefill_priority=dict(status='UNKNOWN_JGT1985_FULLTEXT_GAP_INHERITED_NO_NEW_SEARCH',audit='SPREAD_FILL_SOURCE_PRIORITY_20261101.md',if_same_fill_and_fullO_interface_publicly_confirmed='degree82guarantee346515,current65gainbecomes0',global_record_certified=False),
 primary_sources=dict(oppositeGQ='https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2',product_and_replication='https://arxiv.org/html/2608.27253v2#S7.SS7',PolarStar='https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf',Delorme='https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf',maintained_table='https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/taula_delta_d.html',author_repo='https://github.com/f4t4nt/degree-diameter-graphs'),
 primary_query_batch=dict(batches=1,queries=3,queries_text=['"degree diameter" "82" "diameter 3"','"346515" graph diameter','"degree-diameter-graphs" "diameter 3" "bounds"'],domains=[['arxiv.org','github.com','upc.edu','ethz.ch'],['arxiv.org','github.com','upc.edu'],['github.com']],outcome='No relevant stronger82constructionlocated;Comellaslowdegreepageandunrelatedgistsreturned;latterdiscarded'),
 scalar_CPU_seconds=time.process_time()-START,CPU_budget_seconds=5,new_graphs=0,new_validated_instances=0,BFS_runs=0,Lean_runs=0,solver_runs=0,external_reviews=0,wiki_helper_runs=0,
 old_q8_field_spread_source_BFS_rechecks=0,old_q7_rechecks=0,old_80_81_or_P33_gates_executed=0,JGT_fulltext_queries=0,root_counts_modified=False,frozen_expert_packets_modified=False,degree83plus_authorized=False,all_local_processes_terminal=True)
assert out['scalar_CPU_seconds']<5
(HERE/'DEGREE82_BALANCED_FULL_OVOID_COPY_TARGET_GATE_20261101.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','Delta','candidate','strongest_checked_published_guarantee','candidate_gain','category_maxima','scalar_CPU_seconds']},ensure_ascii=False,indent=2))
