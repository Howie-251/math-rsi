"""Only degree77 finite scalar substitutions. No graph, BFS, field or Lean."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,math
HERE=Path(__file__).resolve().parent;start=time.process_time();cap=77

def prime(n):return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))
def pp(n):
 if n<2:return False
 for p in range(2,n+1):
  if prime(p):
   a=p
   while a<n:a*=p
   if a==n:return True
 return False
qs=[q for q in range(2,cap) if pp(q)]
IQ=[];Paley=[]
for q in qs:
 for d in range(cap-q):
  if d%4 in [0,3]:IQ.append({'family':'PolarStarIQ','q':q,'dprime':d,'degree':q+1+d,'n':(q*q+q+1)*(2*d+2)})
  if d%2==0 and pp(2*d+1):Paley.append({'family':'PolarStarPaley','q':q,'dprime':d,'degree':q+1+d,'n':(q*q+q+1)*(2*d+1)})
IQ.sort(key=lambda r:(r['n'],r['degree']),reverse=True);Paley.sort(key=lambda r:(r['n'],r['degree']),reverse=True)
gq=[];rectangles=[]
for q in qs:
 for name,s,t in [('balanced',q,q),('Payne',q-1,q+1),('quadric_rectangular',q,q*q),('Hermitian_rectangular',q*q,q**3)]:
  d=(s+1)*(t+1)
  if d<=cap:gq.append({'family':name,'q':q,'s':s,'t':t,'degree':d,'n':d*(1+s*t)**2})
 d=(q+1)**2
 if d<=cap:
  # Only explicitly published source premises: evenq fullovoid;
  # oddq Tallini2q+1 as reported in Ceria etal2022, neverlocalO22.
  O=q*q+1 if q%2==0 else 2*q+1;spread=q*q+1;centers=O*spread;k=cap-d
  rectangles.append({'family':'publishedSymplecticOorTalliniPartialO_x_spread_generalInducedDuplication','q':q,'source_degree':d,'source_n':d*(q*q+1)**2,'published_ovoid_or_partial_size':O,'spread_size':spread,'centers':centers,'copies':k,'degree_cap':cap,'n':d*(q*q+1)**2+k*centers})
gq.sort(key=lambda r:r['n'],reverse=True);rectangles.sort(key=lambda r:r['n'],reverse=True)
fold=[];duality=[]
for exponent in range(1,7):
 q=2**exponent
 if q+1<=cap and exponent%2==1:fold.append({'q':q,'source_degree':q+1,'source_n':(q+1)*(q*q+1),'absolute_centers':q*q+1,'copies':cap-(q+1),'n':cap*(q*q+1)})
 if 3*(q+1)<=cap:duality.append({'q':q,'source_degree':3*(q+1),'source_n':12*(q+1)*(q*q+1),'centers':4*(q*q+1),'copies':cap-3*(q+1),'n':4*cap*(q*q+1)})
# Published composed-polarity products already verified in the earlier audits.
quad=[1,2,8,32];polarity=[]
for q in quad:
 for r in quad:
  d=(q+1)*(r+1)
  if d<=cap:
   n=(q+1)*(q*q+1)*(r+1)*(r*r+1);a=(q*q+1)*(r*r+1)
   polarity.append({'family':'GQpolarity_x_GQpolarity_absoluteReplication','q':q,'r':r,'source_degree':d,'source_n':n,'absolute_centers':a,'copies':cap-d,'n':n+(cap-d)*a})
 for r in [1]+qs:
  d=(q+1)*(r+1)
  if d<=cap:
   n=(q+1)*(q*q+1)*(r*r+r+1);a=(q*q+1)*(r+1)
   polarity.append({'family':'GQpolarity_x_projectiveTriangle_absoluteReplication','q':q,'r':r,'source_degree':d,'source_n':n,'absolute_centers':a,'copies':cap-d,'n':n+(cap-d)*a})
polarity.sort(key=lambda r:r['n'],reverse=True)
best=rectangles[0]['n'];H=best//1331+1;H_three=((H+5)//6)*6
out={'status':'BOUNDED_DEGREE77_PRIMARY_FAMILY_GATE_COMPLETE_NO_CANDIDATE_CONTROLLER_SELECTED','checked_UTC':datetime.now(timezone.utc).isoformat(),'degree_cap':77,'D':3,'best_located_source_derived_guarantee':best,'best_construction':rectangles[0],'comparison_kind':'Publishedsourceingredients and generalinducedmatching replication directly composed; not independentlylocatednumericdegree77edgefile or globallymaintainedrecord','local_unpublished_160050_O22_graphs_used_as_public':False,'PolarStar_all_legal_q_d_checked':True,'PolarStar_host_q_domain':qs,'PolarStar_IQ_legal_cases':len(IQ),'PolarStar_Paley_legal_cases':len(Paley),'PolarStar_IQ_best':IQ[0],'PolarStar_Paley_best':Paley[0],'PolarStar_IQ_all':IQ,'PolarStar_Paley_all':Paley,'known_opposite_GQ_direct':gq,'published_balanced_ovoid_spread_duplications':rectangles,'Delorme_folded_absolute_replication':fold,'Delorme_q16_standard12_duality_replication':duality,'composed_polarity_products':polarity,'F11_fiber_size':1331,'controller_threshold':{'smallest_integer_H_strictly_beating':H,'at_previous_H':1331*(H-1),'at_minimum_H':1331*H,'degree7_controller_even_order_requirement_satisfied':H%2==0,'threebase_even_m_minimum_order':H_three,'threebase_even_m_minimum_m':H_three//3,'at_H132_example':1331*132,'H132_example_gain':1331*132-best,'H132_is_selected_or_feasible':False},'new_query_batches':1,'new_queries':4,'queries':[{'q':'"degree" "77" "diameter" "3" graph','domains':['arxiv.org','web.mat.upc.edu','spcl.inf.ethz.ch','ejc.math.emory.edu']},{'q':'"Payne" "derived" "ovoids" generalized quadrangles','domains':['arxiv.org']},{'q':'"W(3,7)" "partial ovoid"','domains':['arxiv.org']},{'q':'"degree diameter" "77" Delorme graph','domains':['arxiv.org','web.mat.upc.edu','spcl.inf.ethz.ch']}],'new_search_result':'No specificcap77numericprimarygraphorstrongerconstructedguaranteelocated;recallprimarilyofficial<=16table/authorindexandunrelatednetworkpapers. Non-hitisnotexhaustivenessproof.','sources':{'Delorme_generalduplication_and_spread':'https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf','opposite_GQ_formula':'https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2','Tallini15_reported_in_primaryresearchpaper':'https://arxiv.org/html/2203.04553#S1','PolarStar_authorpaper':'https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf','current_officialtable_scope':'https://web.mat.upc.edu/francesc.comellas/delta-d/taula_delta_d.html'},'inherited_scope_gaps':['no maintainedhighdegree77table found','DelormeJGT1985fulltext missing','Tallinioriginalcoordinatesnotobtained,existenceexplicitlyreportedinCeria2022','largerpublishedW3F7partialovoids/otherinducedsetsnotexhausted','PayneGQ6,8arbitraryinducedaugmentationnotoptimized;nofullovoid/spreadpackingpremiseassumed','otherpublicgraphs/novelty/prioritynotexhausted'],'controller_selected':False,'new_full_graphs':0,'large_graph_reads':0,'BFS_Lean_solver_external_review_runs':0,'global_record_confirmed':False,'priority_confirmed':False,'scalar_CPU_seconds':time.process_time()-start,'scalar_CPU_budget_seconds':5,'all_local_processes_terminal':True}
assert best==169750 and H==128 and H_three==132
assert out['scalar_CPU_seconds']<5
(HERE/'DEGREE77_R7_F11_TARGET_GATE_20261101.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['best_located_source_derived_guarantee','PolarStar_IQ_best','PolarStar_Paley_best','controller_threshold','scalar_CPU_seconds']},ensure_ascii=False,indent=2))
