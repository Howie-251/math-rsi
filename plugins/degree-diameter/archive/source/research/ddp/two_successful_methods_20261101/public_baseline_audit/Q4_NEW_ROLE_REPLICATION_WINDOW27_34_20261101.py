"""Only the new cap27..34 scalar window. No old26/83 gate is executed.

Pre-execution source check predicts that the mixed q2*q8 GQ-polarity product
already blocks this window. The script verifies the legal formula substitutions,
and optionally makes one current read of three primary author-index endpoints.
It generates no graphs, parses no graph data, and does not run Lean or BFS.
"""
import argparse,base64,json,math,resource,time,urllib.request
from datetime import datetime,timezone
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(5,5))
HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('--refresh-author',action='store_true');args=parser.parse_args()
def prime(n):return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))
def pp(n):
 if n<2:return False
 for p in range(2,n+1):
  if not prime(p):continue
  z=p
  while z<n:z*=p
  if z==n:return True
 return False
def best(rows):return max(rows,key=lambda x:x['n'])if rows else None

author=dict(current_primary_read_requested=args.refresh_author,endpoints=[],claim_is_limited_to_inspected_indices=True)
if args.refresh_author:
 for key,path in [('README','README.md'),('results_index','results.json'),('results_directory','results')]:
  url='https://api.github.com/repos/rmizuno42/ddp/contents/'+path+'?ref=main'
  try:
   request=urllib.request.Request(url,headers={'User-Agent':'degree-diameter-bounded-source-check','Cache-Control':'no-cache','Accept':'application/vnd.github+json'})
   with urllib.request.urlopen(request,timeout=20)as response:
    obj=json.load(response);status=response.status
   entry=dict(name=key,url=url,HTTP_status=status,ref='main',accessed_UTC=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'))
   if key=='README':
    text=base64.b64decode(obj['content']).decode();entry['contains_exact_35875']=bool(__import__('re').search(r'\b35875\b',text));entry['target_degree_paths']=[f'degree{d}-diameter3'for d in range(27,35)if f'degree{d}-diameter3'in text]
   elif key=='results_index':
    index=json.loads(base64.b64decode(obj['content']).decode());rows=index['results'];entry['all_D3_rows']=[{k:r[k]for k in['id','degree','diameter','vertices','summary']if k in r}for r in rows if r.get('diameter')==3];entry['window_rows']=[r for r in entry['all_D3_rows']if 27<=r['degree']<=34];entry['degree35_D3_rows']=[r for r in entry['all_D3_rows']if r['degree']==35]
   else:
    entry['directory_names']=[r['name']for r in obj];entry['window_directories']=[x for x in entry['directory_names']if any(x==f'degree{d}-diameter3'for d in range(27,35))];entry['degree35_directory']='degree35-diameter3'in entry['directory_names']
   author['endpoints'].append(entry)
  except Exception as exc:author['endpoints'].append(dict(name=key,url=url,status='PRIMARY_FETCH_FAILED_NO_RETRY',error=str(exc)))

rows=[]
for cap in range(27,35):
 candidate_n=7532+290*(cap-26);candidate_m=97750+7225*(cap-26);assert candidate_n==290*cap-8
 qs=[q for q in range(2,cap)if pp(q)];IQ=[];PAL=[];DIRECT=[];POLPROD=[];FOLDED=[];DUAL=[]
 for q in qs:
  for d in range(cap-q):
   if d%4 in(0,3):IQ.append(dict(family='PolarStarIQ',q=q,dprime=d,degree=q+1+d,n=(q*q+q+1)*(2*d+2)))
   if d%2==0 and pp(2*d+1):PAL.append(dict(family='PolarStarPaley',q=q,dprime=d,degree=q+1+d,n=(q*q+q+1)*(2*d+1)))
  for name,s,t in [('balanced',q,q),('Payne',q-1,q+1),('quadric_rectangular',q,q*q),('Hermitian_rectangular',q*q,q**3)]:
   delta=(s+1)*(t+1)
   if delta<=cap:DIRECT.append(dict(family='opposite_GQ_'+name,q=q,s=s,t=t,degree=delta,n=delta*(1+s*t)**2))
 for q in[1,2,8,32]:
  for r in[1,2,8,32]:
   delta=(q+1)*(r+1)
   if delta<=cap:
    centers=(q*q+1)*(r*r+1);POLPROD.append(dict(family='published_GQpolarity_product_absolute_replication',q=q,r=r,source_degree=delta,source_n=delta*centers,absolute_product=centers,copies=cap-delta,n=cap*centers))
 for e in[1,3,5]:
  q=2**e
  if q+1<=cap:FOLDED.append(dict(family='Delorme_folded_absolute_replication',q=q,source_degree=q+1,source_n=(q+1)*(q*q+1),absolute_points=q*q+1,copies=cap-(q+1),n=cap*(q*q+1)))
 for e in range(1,6):
  q=2**e
  if 3*(q+1)<=cap:DUAL.append(dict(family='Delorme_standard12_duality_replication',q=q,source_degree=3*(q+1),n=4*cap*(q*q+1)))
 categories=dict(PolarStarIQ=best(IQ),PolarStarPaley=best(PAL),direct_opposite_GQ=best(DIRECT),GQ_polarity_product_replication=best(POLPROD),Delorme_folded_replication=best(FOLDED),standard12_duality_replication=best(DUAL),q4_unfilled_ovoid_spread_replication=dict(family='q4_unfilled_O17_S17_replication',source_degree=25,source_n=7225,centers=289,copies=cap-25,n=289*cap))
 strongest=best([x for x in categories.values()if x])
 if cap<=30:blocker=dict(family='direct_published_q2_q8_polarity_product',degree=27,n=8775,q=2,r=8)
 elif cap==31:blocker=dict(family='PolarStarIQ',degree=31,n=9144,q=19,dprime=11)
 elif cap==32:blocker=dict(family='PolarStarIQ',degree=32,n=9954,q=23,dprime=8)
 else:blocker=dict(family='direct_Delorme_q32_folded_source',degree=33,n=33825,q=32)
 assert candidate_n<blocker['n']<=strongest['n']
 rows.append(dict(Delta=cap,r=cap-26,conditional_n=candidate_n,conditional_m=candidate_m,best_checked_guarantee=strongest['n'],strongest_recipe=strongest,margin=candidate_n-strongest['n'],independent_direct_blocker=blocker,category_maxima=categories,status='BLOCKED'))
correction=dict(q=23,dprime=8,degree=32,fiber_vertices=18,structure_vertices=553,n=9954,previous_11060_correct=False,explanation='11060=553*20 would correspond to dprime9, which is not an allowed IQ degree; Table2 requires dprime0 or3mod4')
result=dict(status='ALL_EIGHT_Q4_ROLE_REPLICATION_ENDPOINTS_BLOCKED_STOP',checked_UTC=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),scope='Only cap27..34, same accepted private7532 source and290new-role centers, scalar conditional targets only',source=dict(n=7532,m=97750,maxdegree=26,roles=290,disjoint_pin_union=7225),candidate_formula=dict(n='290*Delta-8',m='97750+7225*(Delta-26)'),cases=rows,positive_margin_caps=[],recommended_endpoints=[],PolarStar_q23_d8_correction=correction,current_author_repo=author,Comellas_current_primary_check=dict(main='https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html',D3_details='https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g3.html',actual_table_degree_range=[3,16],window_entries_not_provided=True,absence_not_a_global_bound=True),cached_35875_provenance=dict(primary='Charles Delorme,EJC6(1985),291-302,sections2,7,8(c)',q=32,q_legal_reason='32=2^5,odd exponent',base_degree=33,base_order=33825,absolute_points=1025,degree35_order=35875,replications_at35=2,formula='33825+2*1025=35875',direct35_graph_not_used_at_lower_cap=True,current_repo35_absence_not_nonexistence=True,source_credit='The cached35875 guarantee is Delorme folded-polarity+replication, not a newly established Mizuno35 package'),primary_sources=dict(product_and_replication='https://arxiv.org/html/2608.27253v2#S7.SS4',replication='https://arxiv.org/html/2608.27253v2#S7.SS7',PolarStar='https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf',Delorme='https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf',Mizuno_repo='https://github.com/rmizuno42/ddp'),primary_query_batch=dict(batches=1,queries=3,query_text=['"35875" "Mizuno" graph','site:github.com/rmizuno42/ddp "diameter3" "degree27" OR "degree28" OR "degree29" OR "degree30" OR "degree31" OR "degree32" OR "degree33" OR "degree34"','"degree diameter" "diameter 3" "27" "34"'],outcome='No additional relevant target construction located; numerical false positives and unrelated graph repositories discarded',global_exhaustion_claim=False),CPU_seconds=time.process_time(),CPU_budget_seconds=5,new_graphs=0,graph_parsing_or_revalidation=0,field_geometry_or_BFS_or_Lean_or_solver_runs=0,old26_or83_gate_executed=False,JGT_fulltext_recheck=False,root_state_or_progress_or_recovery_or_wiki_or_frozen_files_changed=False,global_record_or_priority_certified=False,all_processes_terminal=True)
assert result['CPU_seconds']<5
(HERE/'Q4_NEW_ROLE_REPLICATION_WINDOW27_34_20261101.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=result['status'],cases=[{k:r[k]for k in['Delta','conditional_n','conditional_m','best_checked_guarantee','margin']}for r in rows],current_author_repo=author,CPU_seconds=result['CPU_seconds']),ensure_ascii=False,indent=2))
